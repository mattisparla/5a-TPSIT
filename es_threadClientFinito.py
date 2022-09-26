import socket

from threading import Thread
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.bind(("192.168.0.112",5000))
s.connect(("192.168.0.119",5000))

class receive(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
    
    def run(self):
        while self.running:
            data = s.recv(4096)
            print(data.decode())
           # msg, ind_client = s.recvfrom(4096)
           # print("\n>" + msg.decode())

    def stop(self):
        self.running = False

def main():

    #s.sendto("Connesso".encode(),("192.168.0.127",5000))
    r = receive()
    r.start()

    while True:
        #msg = input("Inserisci una stringa composta da: Messaggio che si vuole inviato, Nome (luca, galletta, sparla, sulko) separati da |:\n")
        #s.sendto(msg.encode(),("192.168.0.136",5000))
        data = input("Inserisci una stringa composta da: Messaggio che si vuole inviato, Nome (luca, galletta, sparla, sulko) separati da |:\n")
        s.sendall(data.encode())
        if data == "break":
            r.stop()
            r.join()
            r.run()
            break
    
if __name__ == "__main__":
    main()