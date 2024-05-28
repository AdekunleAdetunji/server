#!/usr/bin/python3
"""
This module contains the client module used to establish client connection
with the server
"""
import ssl
from socket import *


with create_connection(
    ("localhost", 9000),
) as conn:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations("cert.pem")
    ssl_conn = context.wrap_socket(conn, server_hostname="localhost")
    search_list = [
        "18;0;1;28;0;6;5;0;",
        "20;0;23;16;0;18;3;0;",
        "23;0;1;26;0;7;3;0;",
        "10;0;1;28;0;9;5;0;",
        "18;0;1;21;0;7;3;0;",
        "13;0;1;28;0;7;3;0;",
        "8;0;23;11;0;19;5;0;",
        "3;0;1;28;0;23;4;0;",
        "21;0;23;21;0;22;3;0;",
        "4;0;1;26;0;8;4;0;",
        "4;0;1;28;0;8;5;0;",
        "11;0;6;28;0;24;5;0;",
        "16;0;1;28;0;7;3;0;",
        "2;0;1;28;0;10;5;0;",
        "11;0;1;11;0;5;5;0;",
        "25;0;1;28;0;7;3;0;",
        "8;0;1;28;0;9;5;0;",
        "21;0;6;28;0;24;4;0;",
        "3;0;6;26;0;7;3;0;",
        "12;0;1;28;0;23;4;0;",
        "18;0;1;28;0;6;4;0;",
        "22;0;21;16;0;19;3;0;",
        "13;0;1;11;0;7;5;0;",
        "12;0;1;28;0;10;5;0;",
        "24;0;1;26;0;7;4;0;",
        "7;0;1;26;0;7;3;0;",
        "5;0;1;28;0;23;4;0;",
        "18;0;1;28;0;7;3;0;",
        "9;0;1;11;0;8;5;0;",
        "12;0;1;28;0;9;5;0;",
        "22;0;1;11;0;7;5;0;",
        "9;0;1;6;0;8;3;0;",
        "23;0;1;26;0;6;4;0;",
        "17;0;1;28;0;8;4;0;",
        "16;0;1;26;0;9;5;0;",
        "7;0;1;28;0;8;3;0;",
        "18;0;1;28;0;7;4;0;",
        "24;0;23;16;0;19;3;0;",
        "6;0;1;26;0;8;5;0;",
        "3;0;6;26;0;7;4;0;",
        "24;0;23;11;0;18;5;0;",
        "2;0;1;16;0;7;5;0;",
        "1;0;6;28;0;23;5;0;",
        "21;0;1;26;0;23;3;0;",
        "19;0;23;21;0;20;3;0;",
        "3;0;6;26;0;24;5;0;",
        "11;0;1;16;0;7;5;0;",
        "17;0;1;28;0;7;5;0;",
        "13;0;1;26;0;9;4;0;",
        "11;0;23;16;0;19;5;0;",
        "9;0;1;6;0;10;5;0;",
        "11;0;23;11;0;19;5;0;",
        "17;0;1;26;0;7;3;0;",
        "3;0;1;28;0;7;3;0;",
        "4;0;1;28;0;8;3;0;",
        "5;0;1;26;0;8;3;0;",
        "22;0;23;11;0;19;5;0;",
        "12;0;1;28;0;7;3;0;",
        "3;0;1;16;0;8;5;0;",
        "2;0;1;26;0;8;4;0;",
        "2;0;6;28;0;24;5;0;",
        "16;0;1;28;0;7;5;0;",
        "2;0;1;28;0;9;4;0;",
        "19;0;1;28;0;7;4;0;",
        "8;0;6;28;0;23;4;0;",
        "1;0;1;16;0;7;5;0;",
        "7;0;1;26;0;8;4;0;",
        "11;0;1;28;0;7;5;0;",
        "20;0;23;21;0;22;3;0;",
        "5;0;6;28;0;22;4;0;",
        "15;0;1;28;0;7;3;0;",
        "16;0;23;16;0;18;4;0;",
        "13;0;1;21;0;7;5;0;",
        "1;0;1;26;0;7;3;0;",
        "19;0;6;28;0;23;5;0;",
        "9;0;1;6;0;21;4;0;",
        "2;0;1;28;0;9;3;0;",
        "19;0;6;28;0;23;4;0;",
        "21;0;23;21;0;20;3;0;",
        "11;0;1;16;0;7;4;0;",
        "5;0;6;16;0;7;5;0;",
        "20;0;1;28;0;7;5;0;",
        "17;0;1;16;0;8;3;0;",
        "9;0;1;11;0;7;5;0;",
        "1;0;1;28;0;24;3;0;",
        "16;0;6;28;0;23;4;0;",
        "15;0;1;16;0;7;5;0;",
        "15;0;1;26;0;6;4;0;",
        "19;0;23;16;0;18;4;0;",
        "3;0;6;28;0;23;4;0;",
        "1;0;6;28;0;24;4;0;",
    ]
    for i in search_list:
        ssl_conn.sendall(i.encode())
        data = ssl_conn.recv(1024).decode()
        print(f"'{data}'")
