from tkinter import *
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.71'
port = 5008

clients = []


# root = Tk()
# root.title("Multithreading Chat Application")

# chat_frame = Frame(root, width=150, height=50, bg="light blue")
# chat_frame.pack(padx=10)

# entry = Entry(chat_frame)
# entry.pack(side=LEFT)

# send = Button(chat_frame, text="send", command=send_data)
# send.pack(side=LEFT)

def start_server():
    global clients
    s.bind((host, port))
    s.listen(10)
    while True:
        conn, addr = s.accept()
        clients.append(conn)
        threading.Thread(target=receive_data, args=(conn,)).start()

# def send_data(conn):
#     data = entry.get()
#     if data:
#         data_label = Label(chat_frame, text=data)
#         data_label.pack()
#         conn.sendall(data.encode()) 

def receive_data(conn):
    while True:
        data = conn.recv(1024)
        d2 = data.decode()
        if d2 == "leave":
            conn.close()
            clients.remove(conn)
        for each in clients:
            if each != conn:
                each.sendall(data)

start_server()

# root.mainloop()
