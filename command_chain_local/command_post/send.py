import socket
from time import sleep


DEST_HOST = 'radio_op1'
DEST_PORT = 4444


def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((DEST_HOST, DEST_PORT))
        s.sendall(command.encode())
        print(f"[*] Sent command {command}")


def spawn_and_kill():
    send_command("spawn")
    print("Waiting for army to grow...")
    sleep(15)
    send_command("kill")
    

spawn_and_kill()

