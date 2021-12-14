import subprocess


class Check:
    """
    A command which is run on a given host with a certain expected output.
    """
    def __init__(self, host, username, command, expected, description=""):
        self.host = host
        self.username = username
        self.command = command
        self.expected = expected
        self.description = description
        self._last_stdout = None

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

    def run(self) -> tuple[bool, bool, str, str]:
        """Executes the command and checks the results."""
        stdout, stderr = self._execute_ssh_command()
        stdout_changed = stdout == self._last_stdout
        self._last_stdout = stdout
        return stdout_changed, stdout == self.expected, stdout, stderr
