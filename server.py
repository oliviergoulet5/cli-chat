import socket
import threading
import termcolor

class ServerNode:
    def __init__(self):
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = ('127.0.0.1', 12345)
        self.node.bind(port_and_ip)
        self.node.listen(5)
        self.connection, addr = self.node.accept()
    
    def send_msg(self, msg):
        self.connection.send(msg.encode())
    
    def receive_msg(self):
        while True:
            data = self.connection.recv(1024).decode()
            print(data)


    def run(self):
        termcolor.cprint("Chat session has started.", "green")
        while True:
            message = input()
            self.send_msg(message)



def main():
    server = ServerNode()
    always_receive = threading.Thread(target = server.receive_msg)
    always_receive.daemon = True
    always_receive.start()
    server.run()

if __name__ == '__main__':
    main()
