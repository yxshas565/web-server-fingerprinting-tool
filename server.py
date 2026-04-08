#!/usr/bin/env python3
import socket
import ssl
import threading
import re

HOST = "0.0.0.0"
PORT = 8443


def grab_http_banner(host, port=80):
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((host, port))

        req = "HEAD / HTTP/1.1\r\nHost: " + host + "\r\nConnection: close\r\n\r\n"
        s.send(req.encode())

        data = s.recv(4096).decode(errors="ignore")
        s.close()
        return data
    except:
        return None


def grab_https_banner(host, port=443):
    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        raw = socket.socket()
        raw.settimeout(3)
        raw.connect((host, port))

        s = context.wrap_socket(raw, server_hostname=host)

        req = "HEAD / HTTP/1.1\r\nHost: " + host + "\r\nConnection: close\r\n\r\n"
        s.send(req.encode())

        data = s.recv(4096).decode(errors="ignore")
        s.close()
        return data
    except:
        return None


def extract_server(banner):
    if not banner:
        return "Unknown"
    match = re.search(r"Server:\s*(.*)", banner)
    return match.group(1).strip() if match else "Unknown"


def handle_client(conn):
    try:
        target = conn.recv(1024).decode().strip()

        banner = None
        protocol = "Unknown"
        port = "Unknown"

        # Try HTTPS first
        banner = grab_https_banner(target, 443)
        if banner:
            protocol = "HTTPS"
            port = 443

        # Try HTTP if HTTPS fails
        if not banner:
            banner = grab_http_banner(target, 80)
            if banner:
                protocol = "HTTP"
                port = 80

        if banner:
            server = extract_server(banner)

            version_match = re.search(r"\d+\.\d+(\.\d+)?", server)
            version = version_match.group(0) if version_match else "Unknown"

            response = ""
            response += "Target: " + target + "\n"
            response += "Protocol: " + protocol + "\n"
            response += "Port: " + str(port) + "\n"
            response += "Server: " + server + "\n"
            response += "Version: " + version + "\n"
        else:
            response = "Could not retrieve server info\n"

        conn.send(response.encode())

    except:
        conn.send(b"Error processing request\n")
    finally:
        conn.close()


def main():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    sock = socket.socket()
    sock.bind((HOST, PORT))
    sock.listen(5)

    print("Secure Server running on port", PORT)

    while True:
        client_sock, addr = sock.accept()
        secure_conn = context.wrap_socket(client_sock, server_side=True)

        thread = threading.Thread(target=handle_client, args=(secure_conn,))
        thread.start()


if __name__ == "__main__":
    main()