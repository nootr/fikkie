import subprocess

from tinydb import TinyDB, Query
from typing import Literal, Tuple

from .config import DB_FILENAME


class Check:
    """A command which is run on a given host with a certain expected output."""

    def __init__(self, host, username, command, expected, description=""):
        self.host = host
        self.username = username
        self.command = command
        self.expected = expected
        self.description = description

    def dump(self, short: bool = False) -> dict:
        """Returns a dictionary containing all relevant data."""
        data = {
            "host": self.host,
            "command": self.command,
            "expected": self.expected,
            "description": self.description,
        }
        if not short:
            status, stdout, stderr = self._get_status()
            data["status"] = status
            data["stdout"] = stdout
            data["stderr"] = stderr

        return data

    def _execute_ssh_command(self) -> str:
        """Executes an SSH command and returns stdout and stderr."""
        result = subprocess.run(
            [
                "ssh",
                "-l",
                self.username,
                self.host,
                "--",
                self.command,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        def _decode(b):
            return b.decode("utf-8").strip() if b else ""

        return _decode(result.stdout), _decode(result.stderr)

    @property
    def status(self) -> str:
        """Returns the last result status."""
        last_result_status, _, _ = self._get_status()
        return last_result_status

    @property
    def stdout(self) -> str:
        """Returns the last result stdout."""
        _, last_result_stdout, _ = self._get_status()
        return last_result_stdout

    @property
    def stderr(self) -> str:
        """Returns the last result stderr."""
        _, _, last_result_stderr = self._get_status()
        return last_result_stderr

    def _get_status(self) -> Tuple[str, str, str]:
        """Returns a tuple of (last result status, last result stdout)."""
        db = TinyDB(DB_FILENAME)
        Status = Query()

        values = db.search(Status.id == self._db_id)

        if not values:
            raise ValueError("This check hasn't run yet")

        last_result_status = values[-1]["status"]
        last_result_stdout = values[-1]["stdout"]
        last_result_stderr = values[-1]["stderr"]
        return last_result_status, last_result_stdout, last_result_stderr

    def _set_status(
        self, status: Literal["OK", "NOT OK", "UNKNOWN"], stdout: str, stderr: str
    ) -> None:
        """Sets the last result status and stdout."""
        db = TinyDB(DB_FILENAME)
        Status = Query()

        data = {
            "id": self._db_id,
            "status": status,
            "stdout": stdout,
            "stderr": stderr,
        }

        try:
            self._get_status()
        except ValueError:
            db.insert(data)
            return

        db.update(data, Status.id == self._db_id)

    @property
    def _db_id(self) -> str:
        return f"{self.host}:{self.command}"

    def run(self) -> Tuple[bool, bool, str, str]:
        """Executes the command and checks the results."""

        stdout, stderr = self._execute_ssh_command()

        try:
            last_result_stdout = self.stdout
        except ValueError:
            last_result_stdout = None

        stdout_changed = stdout != last_result_stdout
        status = "OK" if stdout == self.expected else "NOT OK"

        self._set_status(status, stdout, stderr)

        return stdout_changed, stdout == self.expected, stdout, stderr
