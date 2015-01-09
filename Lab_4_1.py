import Lab_1
import Lab_2
import Lab_3
import socket
keyTXT = raw_input('Enter the name of vijiner key file(*.txt): ')
key2TXT = raw_input('Enter the name of AES key file(*.txt): ')
try:
	keyFile = open(keyTXT,"rb")
	key2File = open(key2TXT,"rb")
except IOError:
	print('File error')
	exit()
tmp = ""
key = keyFile.read()
key2 = key2File.read()
sock = socket.socket()
sock.bind(('', 1101))
sock.listen(1)
conn, addr = sock.accept()
while True:
	data = conn.recv(1024)
	if not data:
		break
	tmp += data
conn.close()
dataFile = open('srv.bmp','wb')
dataFile.write(tmp)
dataFile.close()

LSB = Lab_3.decrypt('srv.bmp')
AES = Lab_2.crypt(LSB, key2, True)
VIJ = Lab_1.decrypt(AES, key)
rez = open('out.txt', 'wb')
rez.write(VIJ)
rez.close()
