from multiprocessing import Process, Pipe
from random import randint
from os import getpid
from time import sleep

# define a example function
def ponger(child_conn, parent_conn):
    while True:
        msg = parent_conn.recv()
        print(f"Process{getpid()} got message: {msg}")
        child_conn.send(f"Pong {getpid()}")
        sleep(randint(0, 2))
        child_conn.send(f"Ping {getpid()}")


if __name__ == '__main__':
    # Setup a list of processes
    parent_conn_1, child_conn_1 = Pipe()
    parent_conn_2, child_conn_2 = Pipe()

    process_1 = Process(target=ponger, args=(child_conn_1, parent_conn_2)).start()
    process_2 = Process(target=ponger, args=(child_conn_2, parent_conn_1)).start()

    child_conn_1.send(f"Ping {getpid()}")
