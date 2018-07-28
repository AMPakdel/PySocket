import socket
import threading
import socketserver


class Server():

    class MyTCPHandler(socketserver.BaseRequestHandler):
        """
        The request handler class for our server.

        It is instantiated once per connection to the server, and must
        override the handle() method to implement communication to the
        client.
        """

        def handle(self):
            # self.request is the TCP socket connected to the client
            self.data = self.request.recv(1024).strip().decode("utf-8")
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)

            # just send back the same data, but upper-cased
            self.request.sendall(bytes(self.data, "utf-8").upper())

    HOST = "localhost"

    PORT = 4252

    def __init__(self):
        # Create the server, binding to localhost on port 4252
        with socketserver.TCPServer((self.HOST, self.PORT), self.MyTCPHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C
            server.serve_forever()
            print("server listening on port : "+str(self.PORT))


class Async_Server:

    def __init__(self, port):
        # Port 0 means to select an arbitrary unused port
        self.HOST = "localhost"
        self.PORT = port

    class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

        def handle(self):
            data = str(self.request.recv(1024), 'ascii')
            cur_thread = threading.current_thread()
            response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
            self.request.sendall(response)


    class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
        pass


    def start(self):

        server = self.ThreadedTCPServer((self.HOST, self.PORT), self.ThreadedTCPRequestHandler)
        with server:

            self.server = server

            ip, port = server.server_address

            print("ip:{} port:{}".format(ip,port))

            # Start a thread with the server -- that thread will then start one
            # more thread for each request
            server_thread = threading.Thread(target=server.serve_forever)
            # Exit the server thread when the main thread terminates
            server_thread.daemon = True
            server_thread.start()
            print("Server loop running in thread:", server_thread.name)


    def shutdown(self):

        self.server.shutdown()