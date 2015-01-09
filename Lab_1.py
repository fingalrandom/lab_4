def encrypt(text, key):
	alph = ''
	for i in range(256):
		alph += chr(i)
	i=0;lenth=len(text)
	code=''
	while len(text) > len(key):
		key = key + key[i]
		i = i + 1
	i=0
	while i < lenth:
		cur = alph.find(key[i])
		ch = alph.find(text[i])
		code = code + alph[(ch+cur)%len(alph)]
		i=i+1
	return code
def decrypt(text, key):
	alph = ''
	for i in range(256):
		alph += chr(i)
	i=0;lenth=len(text)
	decode=''
	while len(text) > len(key):
		key = key + key[i]
		i = i + 1
	i=0
	while i < lenth:
		ch = alph.find(text[i])
		cur = alph.find(key[i])
		decode = decode + alph[(ch-cur)%len(alph)]
		i=i+1
	return decode
