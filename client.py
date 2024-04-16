import socket
import threading
import time

def recv_data(client_socket):
    while True:
        try:
            blen=0
            tot_data=""
            tot_len=0
            data=client_socket.recv(6).decode()
            if data[0:3]=='len':
                tot_len=int(data[3:])
                print(data)
            if tot_len < 5:
                data=client_socket.recv(6).decode()
                print("recive : ", int(data))
            else :
                while (tot_len-blen>0):
                    data = client_socket.recv(tot_len).decode()
                    blen+=len(data)
                    tot_data+=data
                print("table: \n", repr(tot_data))
                
        except ConnectionResetError as e:
            print(e)

if __name__ == "__main__":
    
    # HOST = socket.gethostbyname(socket.gethostname())
    # PORT = 8888
    # cc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # cc_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # cc_socket.bind((HOST, PORT))

    # cc_socket.listen()
    
    
    
    HOST = '210.110.39.169' ## server에 출력되는 ip를 입력해주세요 ##
    PORT = 9999
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(client_socket)
    #client_socket.send(message.encode())
    t=threading.Thread(target=recv_data, args=(client_socket, ))
    t.start()
    print('>> Connect Server')
    
    while True:
        message = input()
        if message == 'quit':
            break
        if message=='close':
            client_socket.send(message.encode())
            client_socket.close()
            print('client-server socket closed')
            time.sleep(5)
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((HOST, PORT))

        client_socket.send(message.encode())

client_socket.close()