#!/usr/bin/python3
"""
This script contains a series of tests that benchmark SSL/TLS connections
to a server using different configurations for reading a specified number of
lines from a file.

Each test function benchmarks the performance of a client connection
to the server under varying conditions (reread vs. no reread) and with
different numbers of lines being read by the server (10, 100, 500, 1 million).
"""
import ssl
from . import env_vars  # Assuming env_vars is defined in the __init__.py file
from socket import create_connection


def test_10k_no_reread(server_10_no_reread, benchmark):
    def client_connection():
        with create_connection(
            (str(env_vars.HOST), env_vars.TEST_PORT)
        ) as conn:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations("cert.pem")
            ssl_conn = context.wrap_socket(conn, server_hostname="localhost")
            ssl_conn.sendall(b"3;0;1;28;0;7;5;0;")
            response = ssl_conn.recv(1024).decode()
            assert response == "STRING EXISTS"
            return True

    result = benchmark(client_connection)
    print(result)


def test_10k_reread(server_10_reread, benchmark):
    def client_connection():
        with create_connection(
            (str(env_vars.HOST), env_vars.TEST_PORT)
        ) as conn:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations("cert.pem")
            ssl_conn = context.wrap_socket(conn, server_hostname="localhost")
            ssl_conn.sendall(b"3;0;1;28;0;7;5;0;")
            response = ssl_conn.recv(1024).decode()
            return response

    result = benchmark(client_connection)
    print(result)


def test_100k_no_reread(server_100_no_reread, benchmark):
    def client_connection():
        with create_connection(
            (str(env_vars.HOST), env_vars.TEST_PORT)
        ) as conn:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations("cert.pem")
            ssl_conn = context.wrap_socket(conn, server_hostname="localhost")
            ssl_conn.sendall(b"3;0;1;28;0;7;5;0;")
            response = ssl_conn.recv(1024).decode()
            return response

    result = benchmark(client_connection)
    print(result)


def test_100k_reread(server_100_reread, benchmark):
    def client_connection():
        with create_connection(
            (str(env_vars.HOST), env_vars.TEST_PORT)
        ) as conn:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations("cert.pem")
            ssl_conn = context.wrap_socket(conn, server_hostname="localhost")
            ssl_conn.sendall(b"3;0;1;28;0;7;5;0;")
            response = ssl_conn.recv(1024).decode()
            return response

    result = benchmark(client_connection)
    print(result)


def test_500k_no_reread(server_500_no_reread, benchmark):
    def client_connection():
        with create_connection(
            (str(env_vars.HOST), env_vars.TEST_PORT)
        ) as conn:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations("cert.pem")
            ssl_conn = context.wrap_socket(conn, server_hostname="localhost")
            ssl_conn.sendall(b"3;0;1;28;0;7;5;0;")
            response = ssl_conn.recv(1024).decode()
            return response

    result = benchmark(client_connection)
    print(result)


def test_500k_reread(server_500_reread, benchmark):
    def client_connection():
        with create_connection(
            (str(env_vars.HOST), env_vars.TEST_PORT)
        ) as conn:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations("cert.pem")
            ssl_conn = context.wrap_socket(conn, server_hostname="localhost")
            ssl_conn.sendall(b"3;0;1;28;0;7;5;0;")
            response = ssl_conn.recv(1024).decode()
            return response

    result = benchmark(client_connection)
    print(result)


def test_1m_no_reread(server_1m_no_reread, benchmark):
    def client_connection():
        with create_connection(
            (str(env_vars.HOST), env_vars.TEST_PORT)
        ) as conn:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations("cert.pem")
            ssl_conn = context.wrap_socket(conn, server_hostname="localhost")
            ssl_conn.sendall(b"3;0;1;28;0;7;5;0;")
            response = ssl_conn.recv(1024).decode()
            return response

    result = benchmark(client_connection)
    print(result)


def test_1m_reread(server_1m_reread, benchmark):
    def client_connection():
        with create_connection(
            (str(env_vars.HOST), env_vars.TEST_PORT)
        ) as conn:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations("cert.pem")
            ssl_conn = context.wrap_socket(conn, server_hostname="localhost")
            ssl_conn.sendall(b"3;0;1;28;0;7;5;0;")
            response = ssl_conn.recv(1024).decode()
            return response

    result = benchmark(client_connection)
    print(result)
