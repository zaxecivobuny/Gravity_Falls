
code = "ESWFUP RIF DPS VLOJTSYS"

def decodify(code, decoder):
	output = ""
	for char in code:
		if ord(char) < 65 or ord(char) > 90:
			output += char
		elif char in decoder:
			output += decoder[char]
		else:
			output += '-'	
	print output

decoder = {}

while True:
	print ""
	print code
	decodify(code, decoder)
	print ""
	code_char = raw_input("What letter in the code would you like to replace?")
	if len(code_char) > 1 or ord(code_char) < 65 or ord(code_char) > 90:
		break
	key_char = raw_input("With which letter?")
	if len(key_char) > 1 or ord(key_char) < 65 or ord(key_char) > 90:
		break
	decoder[code_char] = key_char
