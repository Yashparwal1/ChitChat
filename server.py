#imports and dependencies
import socket
import threading

#thread recieve function
def thread_recv(s,signal):
  while True:
      tmp_recv = s.recv(1024)
      print("\n[+] Data:", tmp_recv.strip().decode())
      if(tmp_recv.strip() == b'exit'):
        print("[!] byebye!")
        s.close()
        break

#main function for establishing connection and sending data
def main():
  HOST = "127.0.0.1" #IP address
  PORT = 1234 #Port no. to connect with
  s = socket.socket()
  s.connect((HOST,PORT))
  print("[+] Connection established...")
  new_thread = threading.Thread(target=thread_recv, args=(s,True)) #calling thread_recv function as a thread
  new_thread.start() # run the thread
  print("[+] recv is running as a thread!")
  while True:
    tmp_send = input("[+] input: ").encode()
    s.send(tmp_send+b'\n')

main() #calling main function
