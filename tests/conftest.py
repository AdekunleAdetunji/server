#!/usr/bin/env python3
"""
This script defines pytest fixtures to start and stop a server process
with or without SSL enabled, using the xprocess plugin.
"""
import pytest
import socket
import ssl
import time
from pathlib import Path
from xprocess import ProcessStarter  # type: ignore

# Define the base directory for new processes
BASE_DIR = Path(__file__).resolve().parent.parent


@pytest.fixture
def protected_server(xprocess):
    """
    Fixture to start a server process with SSL enabled before tests and
    ensure it is terminated after tests.

    :param xprocess: xprocess plugin to manage external processes
    """

    class ServerStarter(ProcessStarter):
        # Command to start the server with SSL enabled
        args = [
            "/bin/bash",
            "-c",
            "cd "
            + str(BASE_DIR)
            + " ; ssl=True port=9001"
            + " python3 -m server.server_script",
        ]
        timeout = 5  # Maximum time to wait for the server to start

        def startup_check(self):
            # Sleep for a short duration to ensure the server has time to start
            time.sleep(2)
            return True

    # Ensure the server is started
    logfile = xprocess.ensure("protected_server", ServerStarter)

    # Wait for the server to start
    info = xprocess.getinfo("protected_server")
    yield

    # Terminate the server after tests are done
    xprocess.getinfo("protected_server").terminate()


@pytest.fixture
def unprotected_server(xprocess):
    """
    Fixture to start a server process without SSL enabled before tests and
    ensure it is terminated after tests.

    :param xprocess: xprocess plugin to manage external processes
    """

    class ServerStarter(ProcessStarter):
        # Command to start the server without SSL
        args = [
            "/bin/bash",
            "-c",
            "cd "
            + str(BASE_DIR)
            + " ; ssl=False port=9001"
            + " python -m server.server_script",
        ]
        timeout = 5  # Maximum time to wait for the server to start

        def startup_check(self):
            # Sleep for a short duration to ensure the server has time to start
            time.sleep(2)
            return True

    # Ensure the server is started
    logfile = xprocess.ensure("unprotected_server", ServerStarter)

    # Wait for the server to start
    info = xprocess.getinfo("unprotected_server")
    yield

    # Terminate the server after tests are done
    xprocess.getinfo("unprotected_server").terminate()
