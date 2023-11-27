import string
import random
from base64 import b64encode, b64decode

file_path = 'intercepted.txt'
with open(file_path, 'r') as file:
     intercepted_text= file.read()

def Decrypt_step1(s):
	d_step1 = str.maketrans("mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON","zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA")
	step1_dconvertedstr=str.translate(s, d_step1)
	print('Decrypted Converted string after Step1:',step1_dconvertedstr)
	return step1_dconvertedstr

def Decrypt_step2(s):
	step2_decoded=b64decode(s.encode())
	return step2_decoded.decode()


def Decrypt_step3(ciphertext, shift=4):
	loweralpha = string.ascii_lowercase
	shifted_string = loweralpha[shift:] + loweralpha[:shift] #creating Key for Caeser cipher with shift=4
	print('KEY string:',shifted_string)
	converted = str.maketrans(shifted_string,loweralpha) # creating Translation table: Dictionary[a:e,b:f,c:g....]
	step3_convertedstr= str.translate(ciphertext,converted)  #encrypting via Ceaser cipher, substituting characters
	print('Decrypted converted string after Step3:',step3_convertedstr)
	return step3_convertedstr


#intercepted_text='132FTIjsT9FrKE3rJj='
print('Intercepted Ciphertext: ',intercepted_text)
ia = intercepted_text
while(ia[:1].isnumeric()):
		r = 'Decrypt_step'+ia[:1]
		ia = ia[1:]
		ia = ia +'='
		_a = globals()[r](ia)
		ia=_a
		print('partial decrypted text:',ia)

print('Plaintext (i.e. Secret Message) = ',ia)

