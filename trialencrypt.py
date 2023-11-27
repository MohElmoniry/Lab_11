# This is the program we believe was used to encode the intercepted message.
# some of the retrieved program was damaged (show as &&&&)
# Can you use this to figure out how it was encoded and decode it? 
# Good Luck

import string
import random
from base64 import b64encode, b64decode

secret = 'MohamedAbdelsalam'

secret_encoding = ['step1', 'step2', 'step3']

def step1(s):
	_step1 = str.maketrans("zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA","mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON")
	step1_convertedstr=str.translate(s, _step1)
	return step1_convertedstr

def step2(s):
	s=s.encode()
	double_encoded = b64encode(s)
	return double_encoded.decode()

def step3(plaintext, shift=4):
	loweralpha = string.ascii_lowercase
	shifted_string = loweralpha[shift:] + loweralpha[:shift]
	converted = str.maketrans(loweralpha, shifted_string)
	step3_convertedstr= str.translate(plaintext,converted)
	return step3_convertedstr

def make_secret(plain, count):
	a = '2{}'.format(b64encode(plain).decode())
	for count in range(count):		#works same as RANGE function
		r = random.choice(secret_encoding)
		si = secret_encoding.index(r) + 1
		_a = globals()[r](a)
		a = '{}{}'.format(si, _a)
	return a

if __name__ == '__main__':
	print(make_secret(secret.encode(), count=5).encode())




