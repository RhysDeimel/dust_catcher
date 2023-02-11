import socket


def server():
    # Open socket
    addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print("listening on", addr)

    # Listen for connections
    while True:
        try:
            cl, addr = s.accept()
            print("client connected from", addr)
            cl_file = cl.makefile("rwb", 0)
            while True:
                line = cl_file.readline()
                print(line)
                if not line or line == b"\r\n":
                    break
            response = "<h1>Hi</h1>"
            cl.send("HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
            cl.send(response)
            cl.close()

        except OSError as e:
            cl.close()
            print("connection closed")
