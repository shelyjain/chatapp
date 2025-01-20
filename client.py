from tkinter import *
import socket 
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.71'
port = 5008
s.connect((host, port))

client = []


def get_data():
    while True:
        data = s.recv(1000)
        data = data.decode()
        chat_label = Label(chat_frame, text=data)
        chat_label.pack()
        if data == "!close":
            s.close()

def send_msg():
    msg = entry.get()
    if msg:
        if msg == "!close":
            s.close()
            root.destroy()
        else:
            data_label = Label(chat_frame, text = msg)
            data_label.pack()
            s.sendall(msg.encode())

rec_thread = threading.Thread(target=get_data)
rec_thread.start()

root = Tk()
root.title("Multithreading Chat Application")

chat_frame = Frame(root, width=150, height=50, bg="light blue")
chat_frame.pack(padx=10)  

entry_frame = Frame(root, width = 150)
entry_frame.pack(side=BOTTOM)

entry = Entry(entry_frame)
entry.pack(side=LEFT) 

send = Button(entry_frame, text="send", command = send_msg)
send.pack(side=LEFT) 


root.mainloop()
