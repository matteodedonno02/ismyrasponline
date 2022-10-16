from socket import socket
from time import sleep
import requests


URL = "https://www.python.org/"
timeout = 5
connected = False

TOKEN = "my_bot_token"
CHAT_ID = "my_chat_id"

while connected == False:
  try:

    request = requests.get(URL, timeout=timeout)
    connected = True
    print("Connected to the Internet")

  except (requests.ConnectionError, requests.Timeout) as exception:
    sleep(timeout)

message = "Your Raspberry is Online."
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
print(requests.get(url).json())