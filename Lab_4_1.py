import Lab_1
import Lab_2
import Lab_3
import socket
import sys
def main():
	print "Example of main string for encode[-c]:"
	print "[*.py] [vijiner key file name] [AES key file name]"
	countPar = len(sys.argv)
	if (countPar != 3):
		print "There is wrong number of parameters."
		exit()
	keyFileName = sys.argv[1]
	key2FileName = sys.argv[2]
	try:
		with open(keyFileName, 'rb') as keyFile:
			key = keyFile.read()
		with open(key2FileName, 'rb') as key2File:
			key2 = key2File.read()
	except IOError:
		print('File error')
		exit()
	tmp = ""
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
	with open('srv.bmp', 'wb') as dataFile:
		dataFile.write(tmp)
	LSB = Lab_3.decrypt('srv.bmp')
	AES = Lab_2.crypt(LSB, key2, True)
	VIJ = Lab_1.decrypt(AES, key)
	with open('out.txt', 'wb') as rez:
		rez.write(VIJ)
if __name__ == "__main__":
    main()
