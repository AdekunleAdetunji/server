#!/usr/bin/python3
"""
This module contains the server script to configure and run the server.
It defines the Server and TCPHandler classes for handling incoming requests.
"""
import socketserver
import time
from . import logger
from .database import Database
from .setup import LoadEnv
from datetime import datetime
from pathlib import Path
from ssl import create_default_context
from ssl import Purpose
from ssl import SSLContext
from typing import Any
from typing import Callable


class Server(socketserver.ThreadingTCPServer):
    """
    A subclass of ThreadingMixIn TCPServer to instantiate a server that listens
    for incoming requests, starting new connection to the server in a new
    thread.

    Attributes:
        ssl (bool): Whether SSL is enabled.
        certfile (Path or None): Path to the SSL certificate file.
        keyfile (Path or None): Path to the SSL key file.
        reread_on_query (bool): Whether to reload data from the file on each
        query.
        linuxpath (Path): Path to the data file.
        debug (Path): Debugging options.
    """

    def __init__(
        self,
        server_address: tuple[str | bytes | bytearray, int],
        RequestHandlerClass: Callable[
            [Any, Any, socketserver.TCPServer],
            socketserver.StreamRequestHandler,
        ],
        env_vars_obj: LoadEnv,
    ):
        """
        Initialize a new server instance.

        Args:
            server_address (tuple): The server address as a (host, port) tuple.
            RequestHandlerClass (Callable): The request handler class to use.
            env_vars_obj (LoadEnv): An object containing environment variables.
        """
        self.ssl: bool = env_vars_obj.SSL
        self.certfile: Path | None = env_vars_obj.CERTFILE
        self.keyfile: Path | None = env_vars_obj.KEYFILE
        self.reread_on_query: bool = env_vars_obj.REREAD_ON_QUERY
        self.linuxpath: Path = env_vars_obj.LINUXPATH
        self.debug: Path = env_vars_obj.DEBUG
        self.daemon_threads: bool = True

        super().__init__(server_address, RequestHandlerClass)

    def server_activate(self) -> None:
        """
        Activate the server instance, initialize the database, and set up SSL if
        enabled.
        """
        # make the read file data available to the server instance
        self.database: Database = Database(
            self.reread_on_query, self.linuxpath, sorted
        )

        # secure the server if SSL authentication is set to True
        if self.ssl:
            context: SSLContext = create_default_context(Purpose.CLIENT_AUTH)
            context.load_cert_chain(self.certfile, self.keyfile)  # type: ignore
            self.socket = context.wrap_socket(self.socket, server_side=True)

        # activate the TCP server
        super().server_activate()
        logger.info("server is up and running, waiting for client sockets")


class TCPHandler(socketserver.StreamRequestHandler):
    """
    A subclass of StreamRequestHandler to handle incoming client requests.
    """

    def handle(self) -> None:
        """
        Handle a request sent to the server.
        Continuously read and process data from the client until the connection
        is closed.
        """
        # supply the database object to the request handler
        database = self.server.database  # type: ignore
        client_ip = self.client_address[0]
        comm_port = self.client_address[1]

        while True:
            try:
                # fetch the request query and strip off \x00 from the end
                req_data = self.request.recv(1024).strip().strip(b"\x00")
                # time request was recieved
                query_time = datetime.now().isoformat()
                process_start = time.time()

                # decode the recieved data packet
                req_str = req_data.decode()

                if not req_str:
                    break

                # search the database wether the search string exists
                if req_str and database.search(search_str=f"{req_str}\n"):
                    self.request.sendall(b"STRING EXISTS")
                else:
                    self.request.sendall(b"STRING NOT FOUND")
                # self.request.sendall(b"\n")
                resp_time = datetime.now().isoformat()
                # time response was sent
                process_end = time.time()
                duration = round((process_end - process_start) * 1000, 2)

                log_message = (
                    "{"
                    f"client_ip: {client_ip}, "
                    f"comm_port: {comm_port}, "
                    f"query: {req_data}, "
                    f"time: {query_time}, "
                    f"duration(ms): {duration}"
                    "}"
                )
                # print to the tcp output using the logging module
                logger.debug(log_message)

            # catch undecodable bytes query error
            except UnicodeDecodeError as e:
                err_msg = (
                    "{"
                    f"client_error: {str(e)}, "
                    f"action: closing connection to client"
                    "}"
                )
                logger.error(err_msg)
                break  # break out of the loop
