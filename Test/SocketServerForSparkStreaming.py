import socket

# Configuration
HOST = 'localhost'
PORT = 9999

def start_socket_stream():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"[INFO] Server listening on {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        print(f"[INFO] Spark client connected from {addr}")
        print("[INFO] Type messages and press Enter to send. Ctrl+C to quit.\n")

        with conn:
            try:
                while True:
                    line = input(">> ")  # Read from command line
                    if not line.strip():
                        continue
                    conn.sendall((line + '\n').encode('utf-8'))
            except KeyboardInterrupt:
                print("\n[INFO] Stopping server.")
            finally:
                conn.close()

if __name__ == "__main__":
    start_socket_stream()
