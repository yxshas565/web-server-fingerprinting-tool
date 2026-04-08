import socket
import ssl
import threading

HOST = "127.0.0.1"
PORT = 8443

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE


def scan(target):
    try:
        sock = socket.socket()
        secure_sock = context.wrap_socket(sock, server_hostname=HOST)

        secure_sock.connect((HOST, PORT))
        secure_sock.send(target.encode())

        response = secure_sock.recv(4096).decode()
        print("\nResponse for", target)
        print(response)

        secure_sock.close()
    except:
        print("Error with", target)


def main():
    targets = input("Enter websites (comma separated for multiple websites!): ").split(",")

    threads = []
    for t in targets:
        target = t.strip()
        thread = threading.Thread(target=scan, args=(target,))
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()