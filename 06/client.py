''' Module of client '''

import socket
import sys
import threading


class Client:

    ''' Class represent client that create M threads and send request on server
    to count top K frequent word '''

    def __init__(self, urls_file: str, count_threads: int = 1):
        self.count_threads = count_threads
        self.url_file = urls_file
        self.urls = []

    def load_urls(self):
        with open(self.url_file) as file:
            self.urls = file.readlines()

    @staticmethod
    def send_to_server(urls: list):
        host = socket.gethostname()
        port = 5000

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        for url in urls:
            client_socket.send(url.encode("utf-8"))
            data = client_socket.recv(1024).decode("utf-8")
            print(data)

        client_socket.close()

    def start(self):

        extra_urls_number = 1

        threads = []

        self.load_urls()

        if 10 % self.count_threads != 0:
            extra_urls_number = 10 % self.count_threads

        urls_per_threads = 10 // self.count_threads

        url = self.urls[0: urls_per_threads + extra_urls_number]
        first = threading.Thread(target=self.send_to_server, args=(url,))
        first.start()
        first.join()

        for thread in range(1, self.count_threads):
            url = self.urls[thread * urls_per_threads: (thread + 1) * urls_per_threads]
            thread = threading.Thread(target=self.send_to_server, args=(url,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()


if __name__ == "__main__":
    argv = sys.argv

    if len(argv) < 3:
        print("enter all command: file with urls and count of threads!")
    else:
        url_file = argv[1]
        count_of_thread = argv[2]
        print(url_file, count_of_thread)
        client = Client(url_file, int(count_of_thread))
        client.start()
