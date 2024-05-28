from socket import create_connection

with create_connection(("localhost", 8000)) as conn:
    conn.sendall(b"3;0;1;28;0;7;5;0;")
    response = conn.recv(1024).decode()

print(f"Response Recieved: {response}")
