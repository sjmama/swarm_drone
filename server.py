import json
import socket
import threading
import time 
#{node_id:0}
#{server_address:???.???.???.??}
#{neighbor:3}
#{nearest_address:0}
#{nearest_distance:0}
#{information:}

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
print('>> Server Start with ip :', HOST)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

server_socket.listen()
client_sockets = []
threads=[]

def work(client_socket, addr, timer1):
    print('>> Connected by :', addr[0], ':', addr[1])
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break
            
            print('>> Received from ' + addr[0], ':', addr[1], data.decode())
            # for client in client_sockets:
            #     client.send(str(timer1.clock).encode())
        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break
        
    if client_socket in client_sockets:
        client_sockets.remove(client_socket)
        print('remove client list : ', len(client_sockets))
        
    for i in threads:
        if addr[0] == i.name:
            threads.remove(i)
    print(threads, client_sockets)
    client_socket.close()

class timer():
    def __init__(self):
        self.clock=0
    
    def timesgoon(self):
        while True:
            if self.clock%5==0:
                for client in client_sockets:
                    print(('len'+str(len(str(client_sockets)))))
                    client.send(('len'+str(len(str(client_sockets)))).encode())
                    client.send((str(client_sockets)).encode())
                time.sleep(0.5)
                    
            for client in client_sockets:
                print(str(self.clock))
                client.send(('len'+str(len(str(self.clock)))).encode())
                client.send((str(self.clock)).encode())
                
            time.sleep(1)
            
            self.clock+=1
            if self.clock>=100:
                self.clock=0
            
       
def mainT(timer1):
    while True:
            print('listening')
            client_socket, addr = server_socket.accept()
            client_sockets.append(client_socket)
            
            t=threading.Thread( target=work, args=(client_socket, addr, timer1), name=addr[0])
            t.start()
            threads.append(t)
            print("참가자 수 : ", len(client_sockets))

if __name__=="__main__":
    timer1=timer()
    maint=threading.Thread( target=mainT, args=(timer1, ), name='main')
    maint.start()
    clockt = threading.Thread(target=timer1.timesgoon, args=(), daemon=True)
    clockt.start()
    while True:
        message = input()
        if message == 'check':
            print(client_sockets)
        elif message == "quit":
            break
        elif message == "close":
            client_sockets[0].close()
            client_sockets.pop(0)