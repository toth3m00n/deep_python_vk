''' Module of server '''

import json
import socket
import threading
from queue import Queue
import sys


from most_common_words import count_words


class Worker(threading.Thread):
    ''' Represents class worker that processing clients request '''

    def __init__(self, worker_id, url_queue, result_queue, k):
        super().__init__()
        self.worker_id = worker_id
        self.url_queue = url_queue
        self.result_queue = result_queue
        self.k = k
        self.lock = threading.Lock()

    def run(self):

        print(f"Start worker # {self.worker_id}")

        while True:
            url = self.url_queue.get()

            if url is None:
                break

            response = count_words(url, self.k)

            with self.lock:
                self.result_queue.put({url: response})

            self.url_queue.task_done()

        print(f"End work id {self.worker_id}")


class Server:

    ''' Class Server who communicates with clients threads '''

    def __init__(self, count_workers, top_freq_word):
        self.count_workers = count_workers
        self.urls = []
        self.lock = threading.Lock()
        self.workers = []
        self.url_queue = Queue()
        self.result_queue = Queue()
        self.top_freq_word = top_freq_word

    def handle_client(self, conn):

        while True:
            data = conn.recv(1024).decode("utf-8")

            if not data:
                break

            with self.lock:
                self.url_queue.put(data)

            with self.lock:
                result = self.result_queue.get()

            conn.send(json.dumps(result).encode("utf-8"))

    def awake_workers(self):

        for worker_id in range(self.count_workers):
            worker = Worker(
                worker_id, self.url_queue, self.result_queue, self.top_freq_word
            )
            self.workers.append(worker)
            worker.start()

    def start(self):

        self.awake_workers()

        host = socket.gethostname()
        port = 5000

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))

        server_socket.listen(5)

        print("Start server listening port 5000...")

        while True:
            conn, _ = server_socket.accept()
            threading.Thread(target=self.handle_client, args=(conn,)).start()


if __name__ == "__main__":
    argv = sys.argv

    if argv[1] != "-w":
        print("enter count of workers!")
    elif argv[3] != "-k":
        print("enter count of top frequent word!")
    else:
        server = Server(int(argv[2]), int(argv[4]))
        server.start()
