# from socket import *
# import threading
# from thread import start_new_thread
import threading
import socket
import random

HOST='192.168.49.58'
# HOST='localhost'
PORT=65432


Rnumber = 0
print("[STARTING] Server is starting....")

print(f"[LISTENING] Server is listening on port {PORT}")

Players=[] # רשימה של הSOKCETS שמתחברים למשחק
client_name=[]
guessedNumbers=[]

def send_receive_client_message(client, addr):
    # global client_name, Players
    name = client.recv(1024).decode() #המתנה לקבלת התגובה של שם המשתמש

    client_name.append(name)
    num = client.recv(1024).decode() # המתנה לקבלת התגובה של המספר
    guessedNumbers.append(int(num))
    print("client name", client_name)
    print("guessed Numbers",guessedNumbers)
    if len(guessedNumbers) == 2: # החזרת תשובה רק כאשר שני השחקנים ניחשו מספר

        if abs(Rnumber - guessedNumbers[1]) > abs(Rnumber - guessedNumbers[0]):#אם השחקן הראשון מנצח
            print(f"the winner is {client_name[0]}")
            Players[0].send(f"the nubmer is {Rnumber}\nCongratulation!!! you are the winner!".encode())
            Players[1].send(f"the nubmer is {Rnumber}\n{client_name[0]} is the winner!".encode())
        if abs(Rnumber - guessedNumbers[1]) < abs(Rnumber - guessedNumbers[0]): # אם השחקן השני מנצח
            print(f"the winner is {client_name[1]}")
            Players[0].send(f"the nubmer is {Rnumber}\n{client_name[1]} is the winner!".encode())
            Players[1].send(f"the nubmer is {Rnumber}\nCongratulation!!! you are the winner!".encode())
        else:
            print("It's a draw!")
            Players[0].send(f"the nubmer is {Rnumber}\nIt's a draw!".encode())
            Players[1].send(f"the nubmer is {Rnumber}\nIt's a draw!".encode())


while True:
    Rnumber = random.randint(0, 101)
    print(Rnumber)
    mutex=threading.Lock()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            with mutex:
                conn, addr = s.accept()
                # if len(Players) < 2:
                Players.append(conn)
                print('Connected by', addr)
                print('conn', conn)
                # threading
                threading._start_new_thread(send_receive_client_message, (conn,addr))
                # threading.Thread(target=send_receive_client_message).start()
        s.close()
