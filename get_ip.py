import socket
import requests
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("pwnbit.kr", 443))
print(f"inside IP : {sock.getsockname()[0]}")

req = requests.get("http://ipconfig.kr")
print("outside IP : " + str(re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]))
