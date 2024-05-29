#!/usr/bin/python3
"""
This script defines pytest fixtures to start and stop a server process
with various configurations using the xprocess plugin. The configurations
include different numbers of lines in the input file and whether the server
re-reads data on each query.

Fixtures:
    server_10k_no_reread: Start a server with 10k lines, re-reading disabled.
    server_10k_reread: Start a server with 10k lines, re-reading enabled.
    server_100k_no_reread: Start a server with 100k lines, re-reading disabled.
    server_100k_reread: Start a server with 100k lines, re-reading enabled.
    server_500k_no_reread: Start a server with 500k lines, re-reading disabled.
    server_500k_reread: Start a server with 500k lines, re-reading enabled.
    server_1m_no_reread: Start a server with 1 million lines, re-reading
     disabled.
    server_1m_reread: Start a server with 1 million lines, re-reading enabled.

Each fixture ensures the server is started before tests and terminated after
     tests.
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
def server_10_no_reread(xprocess):
    class ServerStarter(ProcessStarter):
        # Command to start the server with SSL enabled
        args = [
            "/bin/bash",
            "-c",
            "cd "
            + str(BASE_DIR)
            + " ; reread_on_query=false port=9001"
            + " linux_path='speed_test/10k.txt'"
            + " python -m server.server_script",
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
def server_10_reread(xprocess):
    class ServerStarter(ProcessStarter):
        # Command to start the server without SSL
        args = [
            "/bin/bash",
            "-c",
            "cd "
            + str(BASE_DIR)
            + " ; reread_on_query=True port=9001"
            + " linux_path='speed_test/10k.txt'"
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


@pytest.fixture
def server_100_no_reread(xprocess):
    class ServerStarter(ProcessStarter):
        # Command to start the server without SSL
        args = [
            "/bin/bash",
            "-c",
            "cd "
            + str(BASE_DIR)
            + " ; reread_on_query=false port=9001"
            + " linux_path='speed_test/100k.txt'"
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


@pytest.fixture
def server_100_reread(xprocess):
    class ServerStarter(ProcessStarter):
        # Command to start the server without SSL
        args = [
            "/bin/bash",
            "-c",
            "cd "
            + str(BASE_DIR)
            + " ; reread_on_query=True port=9001"
            + " linux_path='speed_test/100k.txt'"
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


@pytest.fixture
def server_500_no_reread(xprocess):
    class ServerStarter(ProcessStarter):
        # Command to start the server without SSL
        args = [
            "/bin/bash",
            "-c",
            "cd "
            + str(BASE_DIR)
            + " ; reread_on_query=False port=9001"
            + " linux_path='speed_test/500k.txt'"
            + " python -m server.server_script"
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


@pytest.fixture
def server_500_reread(xprocess):
    class ServerStarter(ProcessStarter):
        # Command to start the server without SSL
        args = [
            "/bin/bash",
            "-c",
            "cd "
            + str(BASE_DIR)
            + " ; reread_on_query=True port=9001"
            + " linux_path='speed_test/500k.txt'"
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


@pytest.fixture
def server_1m_no_reread(xprocess):
    class ServerStarter(ProcessStarter):
        # Command to start the server without SSL
        args = [
            "/bin/bash",
            "-c",
            "cd "
            + str(BASE_DIR)
            + " ; reread_on_query=False port=9001"
            + " linux_path='speed_test/1m.txt'"
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


@pytest.fixture
def server_1m_reread(xprocess):
    class ServerStarter(ProcessStarter):
        # Command to start the server without SSL
        args = [
            "/bin/bash",
            "-c",
            "cd "
            + str(BASE_DIR)
            + " ; reread_on_query=True port=9001"
            + " linux_path='speed_test/1m.txt'"
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
