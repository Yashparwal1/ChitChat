#imports and dependencies
import socket
import threading

#function for encryption
def enc_xor(data,key):
  res = b''
  for each_chr in data:
    temp = ord(each_chr)^key
    res = res + chr(temp).encode()
  return res

#function for decryption
def dec_xor(data,key):
  res = b''
  for each_chr in data:
    temp = each_chr^key
    res = res + chr(temp).encode()
  return res 

#tread recieve function
def thread_recv(s,key):
  while True:
      encrypted_msg = s.recv(1024)
      dec_msg = dec_xor(encrypted_msg,key) #calling decrytion function
      print("\n[+] Data:", dec_msg.strip().decode())
      if(dec_msg.strip() == b'exit'):
        print("[!] byebye!")
        s.close()
        break

#main function for establishing connection and sending data
def main():
  HOST = "192.168.29.167" #IP address
  PORT = 1234 #Port no. to connect with
  s = socket.socket()
  s.connect((HOST,PORT))
  print("[+] Connection established...")
  key = 25 #the key used in the XOR encryption
  new_thread = threading.Thread(target=thread_recv, args=(s,key))
  new_thread.start() # run the thread
  print("[+] recv is running as a thread!")
  while True:
    normal_msg = input("[+] input: ")
    enc_msg = enc_xor(normal_msg,key) #calling encrytion function
    s.send(enc_msg+b'\n')

main()
