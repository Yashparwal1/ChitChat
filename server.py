#imports and dependencies
import socket
import threading

#thread recieve function
def thread_recv(sock_fd):
  while True:
      tmp_recv = sock_fd.recv(1024)
      print("\n[+] Data:", tmp_recv.strip().decode())
      if(tmp_recv.strip() == b'exit'):
        print("[!] byebye!")
        sock_fd.close()
        break

#main function for listening for connection from client and sending data
def main():
  HOST = "127.0.0.1" #IP address
  PORT = 1234 #Port no. to listen on
  s = socket.socket()
  s.bind((HOST, PORT))
  s.listen(1)
  print("[+] Listining...")
  sock_fd, conn = s.accept()
  if(conn):
    print("[+] new connection:", conn)
    new_thread = threading.Thread(target=thread_recv, args=[sock_fd,])
    new_thread.start() # run the thread
    print("[+] recv is running as a thread!")
    while True:
      tmp_recv = sock_fd.recv(1024)
      print("\n[+] Data:", tmp_recv.strip().decode())
      if(tmp_recv.strip() == b'exit'):
        print("[!] byebye!")
        sock_fd.close()
        break


main()
