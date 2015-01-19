import Lab_1
import Lab_2
import Lab_3
import socket
import sys


def main():
    print "Example of main string for encode[-c]:"
    print "[*.py] [input file name] [vijiner key file name] \
        [AES key file name] [container file name]"
    countPar = len(sys.argv)
    if (countPar != 5):
        print "There is wrong number of parameters."
        exit()
    inFileName = sys.argv[1]
    keyFileName = sys.argv[2]
    key2FileName = sys.argv[3]
    inIMG = sys.argv[4]
    try:
        with open(inFileName, 'rb') as inFile:
            TXT = inFile.read()
        with open(keyFileName, 'rb') as keyFile:
            key = keyFile.read()
        with open(key2FileName, 'rb') as key2File:
            key2 = key2File.read()
    except IOError:
        print('File error')
        exit()

    VIJ = Lab_1.encrypt(TXT, key)
    AES = Lab_2.crypt(VIJ, key2, False)
    LSB = Lab_3.encrypt(inIMG, AES)
    LSB.save('out.bmp', "BMP")
    with open('out.bmp', 'rb') as imFile:
        IMG = imFile.read()
    sock = socket.socket()
    sock.connect(('localhost', 1101))
    sock.send(IMG)
    sock.close()
if __name__ == "__main__":
    main()
