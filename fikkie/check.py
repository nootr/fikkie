import subprocess
from tinydb import TinyDB, Query

from .config import DB_FILENAME


class Check:
    """A command which is run on a given host with a certain expected output."""

    def __init__(self, host, username, command, expected, description=""):
        self.host = host
        self.username = username
        self.command = command
        self.expected = expected
        self.description = description

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
    def _last_stdout(self) -> str:
        db = TinyDB(DB_FILENAME)
        Stdout = Query()

        values = db.search(Stdout.id == self._db_id)
        return values[-1]["stdout"] if values else ""

    @_last_stdout.setter
    def _last_stdout(self, value) -> None:
        db = TinyDB(DB_FILENAME)
        Stdout = Query()

        if self._last_stdout:
            db.update({"id": self._db_id, "stdout": value}, Stdout.id == self._db_id)
        else:
            db.insert({"id": self._db_id, "stdout": value})

    @property
    def _db_id(self) -> str:
        return hash(f"{self.host}:{self.command}")

    def run(self) -> tuple[bool, bool, str, str]:
        """Executes the command and checks the results."""

        stdout, stderr = self._execute_ssh_command()

        stdout_changed = stdout != self._last_stdout
        self._last_stdout = stdout

        return stdout_changed, stdout == self.expected, stdout, stderr
