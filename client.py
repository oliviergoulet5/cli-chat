import socket
import threading
import termcolor
import json
import os.path
from util import *

class ClientNode:
    def __init__(self):
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = ('127.0.0.1', 12345)
        self.node.connect(port_and_ip)

    def send_msg(self, msg):
        self.node.send(msg.encode())
    
    def receive_msg(self):
        while True:
            data = self.node.recv(1024).decode()
            print(data)
    
    def setup_profile(self):
        existing_profile = os.path.isfile("profile.json")

        if existing_profile:
            with open("profile.json", "r") as read_file:
                profile = json.load(read_file)
                print(profile)
                return "d"

        termcolor.cprint("We have detected that this is your first time using cli-chat.\nPlease fill in the following information:", "yellow")
        username = input("Username: ")

        timestamps = query_yes_no("Display timestamps?")

        profile_data = {
            "user": {
                "username": username,
                "color": "yellow"
            },
            "timestamps": timestamps
        }

        with open("profile.json", "w") as write_file:
            json.dump(profile_data, write_file)

        return profile_data
        
    def main(self):
        self.setup_profile()

        while True:
            message = input()
            self.send_msg(message)

Client = ClientNode()
always_receive = threading.Thread(target=Client.receive_msg)
always_receive.daemon = True
always_receive.start()
Client.main()