# To implement Vigenere Cipher 
# This function generates the key in a cyclic manner until 
#it's length isn't equal to the length of original text 
def generateKey(string, key): 
	key = list(key) 
	if len(string) == len(key): 
		return(key) 
	else: 
		for i in range(len(string) - len(key)): 
			key.append(key[i % len(key)]) # return a keyvalue for the keyword entered.
	return("" . join(key)) 
	
# This function returns the 
# encrypted text generated 
# with the help of the key 
def cipherText(string, key): 
	cipher_text = [] 
	for i in range(len(string)): 
		x = (ord(string[i]) + ord(key[i])) % 26 # gives a ascii code to the key.
		x = x + ord('A') 
		cipher_text.append(chr(x)) 
	return("" . join(cipher_text)) 
	
# This function decrypts the 
# encrypted text and returns 
# the original text 
def originalText(cipher_text, key):  # decrypts the cipher
	orig_text = [] 
	for i in range(len(cipher_text)): 
		x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
		x= x + ord('A') 
		orig_text.append(chr(x)) 
	return("" . join(orig_text)) 
	
#if __name__ == "__main__":
def callvigenere(string , keyword): 
	key = generateKey(string, keyword) 
	cipher_text = cipherText(string,key) 
	print "Ciphertext after Vigenere is  :"+ cipher_text 
	return cipher_text , key
	#print("Original/Decrypted Text :", originalText(cipher_text, key)) 

# to Encrypt String using  Caesar Cipher
def ceasorencrypt(text,s): 
	result = "" 
	l = len(text) 
	for i in range(l ): 
		char = text[i] 
		if char == ' ':
			result = result + char
		# To Encrypt uppercase characters 
		elif (char.isupper()): 
			result = result + chr((ord(char) + s-65) % 26 + 65) 
		# To Encrypt lowercase characters 
		else: 
			result = result  + chr((ord(char) + s - 97) % 26 + 97) 

	return result 
# def decryptceasor(ciphertext, n):
# #Decrypt the string and return the plaintext
#     result = ''
#     for l in ciphertext:
#         try:
#             i = (key.index(l) - n) % 26
#             result =result+ key[i]
#         except ValueError:
#             result = result+ l

#     return result
def decryptceasor(text,s): 
	result = "" 
	l = len(text) 
	for i in range(l ): 
		char = text[i] 
		if char == ' ':
			result = result + char
		# To Encrypt uppercase characters 
		elif (char.isupper()): 
			result = result + chr((ord(char) - s-65) % 26 + 65) 
		# To Encrypt lowercase characters 
		else: 
			result = result  + chr((ord(char) - s - 97) % 26 + 97) 

	return result 

#check the above function 

#decryptedceasor = decrypt(encryptedceasor, s)


if __name__ == "__main__":
	text = "ATTACKONCIPHERNOTGOOD"
	s = 4 
	print "the original text is "+ text
	encryptedceasor = ceasorencrypt(text,s)
	print "Encrypted Cipher: after Ceasor  " + ceasorencrypt(text,s)
	#callvigenere(encryptedceasor, keyword)
	encryptedtext , key  = callvigenere(encryptedceasor, "HELLO")
	#print "The Encrypted text is  :"+ encryptedtext
	decryptedvigenere = originalText(encryptedtext , key)	
	originaltext = decryptceasor(decryptedvigenere , s)
	print (originaltext)


