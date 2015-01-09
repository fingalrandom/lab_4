import Lab_1
import Lab_2
import Lab_3
import socket
inTXT = raw_input('Enter the name of text file(*.txt): ')
keyTXT = raw_input('Enter the name of vijiner key file(*.txt): ')
key2TXT = raw_input('Enter the name of AES key file(*.txt): ')
inIMG = raw_input('Enter the name of conteiner file(*.jpg): ')
try:
	inFile = open(inTXT,"rb")
	keyFile = open(keyTXT,"rb")
	key2File = open(key2TXT,"rb")
except IOError:
	print('File error')
	exit()
TXT = inFile.read()
key = keyFile.read()
key2 = key2File.read()

VIJ = Lab_1.encrypt(TXT, key)
AES = Lab_2.crypt(VIJ, key2, False)
LSB = Lab_3.encrypt(inIMG, AES)
LSB.save('out.bmp', "BMP")
imFile = open('out.bmp', 'rb')
IMG = imFile.read()
sock = socket.socket()
sock.connect(('localhost',1101))
sock.send(IMG)
sock.close()

inFile.close()
keyFile.close()
key2File.close()
