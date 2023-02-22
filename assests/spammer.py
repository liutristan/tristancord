import requests
import random
import threading


def main(channel, message):
    tokens = open("tokens.txt").read().splitlines()
    token = random.choice(tokens)
    headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,fr;q=0.8",
    "authorization": token,
    "connection": "keep-alive",
    "content-length": "72",
    "content-type": "application/json",
    "host": "discord.com",
    "origin": "https://discord.com",
    "referer": "https://discord.com/channels/@me/",
    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "en-US",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwOS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA5LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3MDQ1OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }
    json = {
    "content": message,
    "tts": False,
    #"flags": 0
    }
    r = requests.post('https://discord.com/api/v9/channels/' + channel + '/messages',headers=headers, json=json)
    if r.status_code == 200:
        print("Sent")

channel = input("Channel id: ")
message = input("Message: ")
threads = input("Threads: ")
for _ in range(int(threads)):
    threading.Thread(target=main, args=(channel, message)).start()


