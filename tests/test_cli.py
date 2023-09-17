from typer.testing import CliRunner

import crispy_guacamole
from crispy_guacamole.cli import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    assert f"Version: {crispy_guacamole.__version__}" == result.stdout
