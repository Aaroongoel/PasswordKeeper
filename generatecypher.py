from Crypto.Cipher import AES


def ceasorencrypt(text,s): 
	result = "" 
	l = len(text) 
	for i in range(l ): 
		char = text[i] 
		if char == ' ':
			result = result + char
		# To Encrypt uppercase characters 
		else  : 
			result = result + chr((ord(char) + s)) 
		 

	return result 

def decryptceasor(text,s): 
	result = "" 
	l = len(text) 
	for i in range(l ): 
		char = text[i] 
		if char == ' ':
			result = result + char
		# To Encrypt uppercase characters 
		else:
			result = result + chr((ord(char) - s)) 
		# To Encrypt lowercase characters  

	return result 


#check the above function 

#decryptedceasor = decrypt(encryptedceasor, s)
def encryptaes(text):
	message = text
	obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
	ciphertext = obj.encrypt(message)
	print ("encrypted message using aes " ,ciphertext)
	return ciphertext

def decryptaes(text ):
	message = text
	obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
	original = obj2.decrypt(message)
	print ("decrypted after AES is ", original)
	return original
	#decrypted = obj2.decrypt(ciphertext) 


if __name__ == "__main__":
	text = "QWERR ab 23 @" 
	second = text
	result = ""
	s = 4 
	l = len(text)
	required = 17-l 
	if l < 16:
		for i in range(l+1, 17 ): 
			text  = text  + "@"
		print "the complete text " + text
	 	encryptedceasor = ceasorencrypt(text,s)
	 	print "Encrypted Cipher after Ceasor  " + encryptedceasor
	 	encryptedaes =  encryptaes(encryptedceasor)
	 	decryptedaes  = decryptaes (encryptedaes)
	 	originaltext = decryptceasor(decryptedaes , s)	
	 	print originaltext
		original = ""
	for i in range(0,l): 
		original =  original + originaltext[i] 
	print "original text is " + original

	


