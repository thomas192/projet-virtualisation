import socket
from time import sleep


REC_HOST = ""
REC_PORT = 4444

DEST_HOST = "officer"
DEST_PORT = 4444


def listen():
    print("[*] Listening for command...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((REC_HOST, REC_PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                command = conn.recv(1024)
                if not command:
                    break
                command = command.decode("utf-8")
                print(f"Received command: {command}")
                return command
                

def relay(command):
    print(f"[*] Relaying command to {DEST_HOST}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((DEST_HOST, DEST_PORT))
        s.sendall(command.encode())
        print("Command relayed")


while(True):
    command = listen()
    relay(command)
    sleep(1)

