import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

RED_SUITS = ["heart", "diamond"]
BLACK_SUITS = ["spade", "club"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    while True:
        print("Red or black?")
        msg = input()

        sock.sendall(bytes(msg, "utf-8"))
        sock.sendall(b"\n")
        received = str(sock.recv(1024), "utf-8")
        print(received)

        if any(s in received for s in RED_SUITS):
            if "red" in msg:
                print("The card is red.  You win.")
            else:
                print("The card is red.  You lose.")
        elif any(s in received for s in BLACK_SUITS):
            if "black" in msg:
                print("The card is black.  You win.")
            else:
                print("The card is black.  You lose")
        

        