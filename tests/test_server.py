#!/usr/bin/env python3
"""
This module contains tests for verifying the functionality of a TCP server
with both secure (SSL) and unsecure connections.
"""
import ssl
from . import env_vars
from socket import create_connection


def test_client_secure(protected_server):
    """Test secure server connection using SSL."""
    with create_connection((str(env_vars.HOST), env_vars.TEST_PORT)) as conn:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.load_verify_locations("cert.pem")
        ssl_conn = context.wrap_socket(conn, server_hostname="localhost")
        ssl_conn.sendall(b"3;0;1;28;0;7;5;0;")
        response = ssl_conn.recv(1024).decode()
        assert response == "STRING EXISTS\n"


def test_client_unsecure(unprotected_server):
    """Test unprotected server without secure shell"""
    with create_connection((str(env_vars.HOST), env_vars.TEST_PORT)) as conn:
        conn.sendall(b"3;0;1;28;0;7;5;0;")
        response = conn.recv(1024).decode()
        assert response == "STRING EXISTS\n"


def test_client_secure_not_found(protected_server):
    """Test secure server connection with a string that does not exist."""
    with create_connection((str(env_vars.HOST), env_vars.TEST_PORT)) as conn:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.load_verify_locations("cert.pem")
        ssl_conn = context.wrap_socket(conn, server_hostname="localhost")
        ssl_conn.sendall(b"not;exist;")
        response = ssl_conn.recv(1024).decode()
        assert response == "STRING NOT FOUND\n"


def test_client_unsecure_not_found(unprotected_server):
    """Test unprotected server connection with a string that does not exist."""
    with create_connection((str(env_vars.HOST), env_vars.TEST_PORT)) as conn:
        conn.sendall(b"not;exist;")
        response = conn.recv(1024).decode()
        assert response == "STRING NOT FOUND\n"
