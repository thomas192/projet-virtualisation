import socket
import subprocess
from time import sleep

REC_HOST = ""
REC_PORT = 4444


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


def spawn():
    print("[*] Spawning zombies...")
    subprocess.Popen(["./spawn"])


def kill(pid):
    print(f"[*] Killing spawner {pid}...")
    subprocess.call(["./kill", pid])
    

def get_pid():
    proc_list = subprocess.Popen(["ps"], stdout=subprocess.PIPE).communicate()[0].splitlines()
    for p in proc_list:
        p = p.decode("utf-8")
        if "./spawn" in p:
            return p.split()[0]


def count_zombies():
    n = 0
    proc_list = subprocess.Popen(["ps"], stdout=subprocess.PIPE).communicate()[0].splitlines()
    for p in proc_list:
        if "[spawn]" in p.decode("utf-8"):
            n += 1
    return n


def print_proc():
    proc_list = subprocess.Popen(["ps", "-ef"], stdout=subprocess.PIPE).communicate()[0].splitlines()
    for p in proc_list:
        print(p)


while(True):
    command = listen()
    if command == "spawn":
        spawn()
        
    elif command == "kill":
        pid = get_pid()
        kill(pid)
        print(f"Spawner is down but zombies are NOT!")
        print(f"{count_zombies()} zombies remaining we should inform command post")
        
        


