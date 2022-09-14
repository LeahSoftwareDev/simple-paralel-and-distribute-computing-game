from socket import *
from tkinter import *
import tkinter as tk


HOST='192.168.49.58'
# HOST='localhost'
PORT = 65432
login = tk.Tk()
clientSocket = socket(AF_INET, SOCK_STREAM)



def sendNumber(message,game):
    clientSocket.send(message.encode('ascii'))
    response = clientSocket.recv(1023)  # Receiving the first message, making contact with server
    print(response.decode('ascii'))
    t = tk.Label(game, text=response.decode(), font=("Times New Roman", 10))
    t.grid(column=3, row=4, padx=10, pady=25)


def connectToServer(message,login):
    print("Connecting to server...\n\n")
    try:  # Handling exceptions that may arise when connecting to the server
        clientSocket.connect((HOST, PORT))
        print(f"Connected to server on port {PORT}:")
    except ConnectionRefusedError:
        print("Connection was refused. Exiting the game")
        exit(0)

    clientSocket.send(message.encode('ascii'))
    login.destroy()
    game=tk.Tk()
    game.geometry("500x300")
    game.wm_title("game")
    t1 = tk.Label(game, text=f"Hi {message}!!!", font=("Times New Roman", 15))
    t1.grid(column=3, row=1, padx=10, pady=25)
    t = tk.Label(game, text="enter your lucky number between 0 and 100 ", font=("Times New Roman", 15))
    t.grid(column=3, row=2, padx=10, pady=25)
    txt = tk.Entry(game)
    txt.grid(column=5, row=2, padx=10, pady=25)

    b = Button(game, text='send', command=lambda: [sendNumber(txt.get(), game)],font=("Times New Roman", 15))

    b.grid(row=3, column=3, pady=10, padx=10)
    b.config(background="darkorange1", foreground="white",
             activebackground="darkorange1", activeforeground="green")

    game.mainloop()


login.geometry("500x300")
login.wm_title("login")
t1 = tk.Label(login, text="Welcome!", font=("Times New Roman", 30))
t1.grid(column=3, row=0, padx=10, pady=25)
t = tk.Label(login, text="please enter your username: ", font=("Times New Roman", 15))
t.grid(column=3, row=1, padx=10, pady=25)
txt = tk.Entry(login)
txt.grid(column=4, row=1, padx=10, pady=25)
t = tk.Label(login, font=("Times New Roman", 10))
t.grid(column=3, row=2, padx=10, pady=25)

b = Button(login, text='connect to game', command=lambda: [connectToServer(txt.get(), login)])

b.grid(row=3, column=3, pady=10, padx=10)
b.config(background="darkorange1", foreground="white",
         activebackground="darkorange1", activeforeground="green")

login.mainloop()