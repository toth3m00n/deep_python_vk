import socket
import unittest
from unittest.mock import patch, MagicMock
from client import Client


class Test(unittest.TestCase):

    def setUp(self):
        self.client = Client("test_urls.txt", 2)

    def test_load_urls(self):
        with patch("builtins.open", create=True) as mock_open:
            mock_open.return_value.__enter__.return_value.readlines.return_value = ["url1", "url2"]
            self.client.load_urls()
        self.assertEqual(self.client.urls, ["url1", "url2"])

    @patch("socket.socket")
    def test_send_to_server(self, mock_socket):
        mock_connect = MagicMock()
        mock_socket.return_value.connect = mock_connect
        mock_socket.return_value.recv.return_value.decode.return_value = "response"

        urls = ["url1", "url2"]
        self.client.send_to_server(urls)

        mock_socket.assert_called_with(socket.AF_INET, socket.SOCK_STREAM)
        mock_connect.assert_called_with((socket.gethostname(), 5000))
        mock_socket.return_value.send.assert_any_call("url1".encode("utf-8"))
        mock_socket.return_value.send.assert_any_call("url2".encode("utf-8"))
        mock_socket.return_value.recv.assert_any_call(1024)
        mock_socket.return_value.close.assert_called_once()


if __name__ == "main":
    unittest.main()