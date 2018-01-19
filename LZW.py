import string
from bitstring import BitArray, BitStream

BITS_INDEX = 12

def encode(word):
	
	# we build a dictionnary with all possible symbols and an associated number
	size = 0
	symbols ={}
	for letter in string.printable:
		bits = BitArray(BITS_INDEX)
		bits.int = size
		symbols[letter] = bits
		size+=1
	
	
	code = BitArray()
	P = ""
	for c in word:
		temp = P+c
		if temp in symbols:
			P = temp
		else:
			code.append(symbols[P])
			bits = BitArray(BITS_INDEX)
			bits.int = size
			symbols[temp] = bits
			size += 1
			P = c
	code.append(symbols[P])
	
	
	return code.tobytes()

def decode(code):
	
	bitCode = BitStream(bytes = code )
	offsets = []
	for i in xrange(len(code)*8/BITS_INDEX):
		bits = bitCode.read("uint:"+ str(BITS_INDEX))
		offsets.append(bits)
	
	word = ""

	symbols = []
	for letter in string.printable:
		symbols.append(letter)

	P = None
	for c in offsets:
		word += symbols[c]
		if P != None :
			symbols.append(symbols[P] + symbols[c][0])
		P = c
	
	return word #, symbols



	
#print("code :"),
#for t in code :
#	print(t),
#print

#print("symbols :")
#for t in sorted(symbols) :
#	print t + " : " + str(symbols[t]) + ", ",
#print

#print("word : " + word )






