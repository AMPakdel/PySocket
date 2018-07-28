from Server import Async_Server
import asyncio
import time
import socket

loop = asyncio.get_event_loop()

async def domath_async():

    x = 1
    while True:

        x = x*2

        await time.sleep(0.01)

        print(x)


def domath():

    x = 2
    while True:

        x = x*2

        print(x)


async def sayHello():

    while True:

        print("Hellooooooooooooooo!!!")



loop.run_until_complete(domath_async())

loop.run_until_complete(sayHello())
#domath_async()

#server = Async_Server(4252)

#server.start()

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:


    #sock.connect(("127.0.0.1", 4252))

    #sock.sendall(bytes("Hellllllloooo", 'ascii'))

    #response = str(sock.recv(1024), 'ascii')

    #print("Received: {}".format(response))

