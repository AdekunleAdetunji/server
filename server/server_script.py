#!/usr/bin/env python3
"""
This module starts up the server waiting for client connection
"""
from . import env_vars
from . import logger
from .server import Server
from .server import TCPHandler
from pydantic_core import ValidationError

if __name__ == "__main__":
    try:
        # env_vars: LoadEnv = LoadEnv()  # type: ignore
        server_addr = (str(env_vars.HOST), env_vars.PORT)
        with Server(server_addr, TCPHandler, env_vars) as server:
            # activate the server and leave it running until closed
            # print("Server is up and running")
            server.serve_forever()

    # catch operating system error
    except OSError as OSE:
        logger.error(f"unable to start server\n{OSE}")

    # catch keyboard interrupt signal
    except KeyboardInterrupt as k:
        logger.info("SIGINT recieved, shutting down server.....")
        server.server_close()
