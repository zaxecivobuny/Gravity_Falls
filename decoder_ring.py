
#code1 = "ZHOFRPH WR JUDYLWB IDOOV"
#code2 = "QHAW ZHHN: UHWXUQ WR EXWW LVODQG"
#code3 = "KH'V VWLOO LQ WKH YHQWV"
#code4 = "FDUOD, ZKB ZRQW BRX FDOO PH?"
#code5 = "RQZDUGV DRVKLPD!"
#code6 = "PU. FDHVDULDQ ZLOO EH RXW QHAW ZHHN. PU. DWEDVK ZLOO VXEVWLWXWH."
#code7 = "KZKVI QZN WRKKVI HZBH: 'ZFFTSDCJSTZWHZWFS!'"
#code8 = "V. KOFIRYFH GIVNYOVB"
#code9 = "MLG S.T.DVOOH ZKKILEVW"
#code10 = "HLIIB, WRKKVI, YFG BLFI DVMWB RH RM ZMLGSVI XZHGOV."
#code11 = "GSV RMERHRYOV DRAZIW RH DZGXSRMT."
#code12 = "YILFTSG GL BLF YB SLNVDLIP: GSV XZMWB"
#code13 = "SVZEB RH GSV SVZW GSZG DVZIH GSV UVA"
#code14 = "14-5-24-20 21-16: "6-15-15-20-2-15-20 20-23-15: 7-18-21-14-11-12-5'19 7-18-5-22-5-14-7-5"
#code14i = "14-5-24-20- -21-16-:- -\"-6-15-15-20-2-15-20- -20-23-15-:- -7-18-21-14-11-12-5-\'-19- -7-18-5-22-5-14-7-5-\""
#code15 = "22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1"
#code15i = "22-9-22-1-14- -12-15-19- -16-1-20-15-19- -4-5- -12-1- -16-9-19-3-9-14-1"
#code16 = "2-21-20 23-8-15 19-20-15-12-5 20-8-5 3-1-16-5-18-19?"
#code16i = "2-21-20- -23-8-15- -19-20-15-12-5- -20-8-5- -3-1-16-5-18-19-?"
#code17 = "8-1-16-16-25 14-15-23, 1-18-9-5-12?"
#code17i = "8-1-16-16-25- -14-15-23-,- -1-18-9-5-12-?"
#code18 = "9-20 23-15-18-11-19 6-15-18 16-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-7-19!"
#code18i = "9-20- -23-15-18-11-19- -6-15-18- -16-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-7-19-!"
#code20 = "5-19-23-6-21-16 18-9-6 4-16-19 22-12-15-10-20-19-25-19"
#code20i = "5-19-23-6-21-16- -18-9-6- -4-16-19- -22-12-15-10-20-19-25-19"
#codestansmind = "PBVWHUB VKDFN"

#code_mary = "NGKNGL YGLR CYQW"
code = "5-19-23-6-21-16- -18-9-6- -4-16-19- -22-12-15-10-20-19-25-19"
offset = 0

def forward_decoder (code,offset):
	output = ""
	decoder = {}

	for i in range(65,91):
		if (i + offset <= 90):
			decoder[chr(i)] = chr(i+offset)
		else:
			decoder[chr(i)] = chr(i+offset - 26)

	#print decoder['A']
	#print decoder

	for char in code:
		if ord(char) < 65 or ord(char) > 90:
			output += char
		else:
			output += decoder[char]

	return output

def decodify(code, decoder):
	output = ""
	for char in code:
		if ord(char) < 65 or ord(char) > 90:
			output += char
		elif char in decoder:
			output += decoder[char]
		else:
			output += '-'	
	return output

def reverse_decoder(code):
	output = ""
	decoder = {}

	for i in range(65, 91):
		decoder[chr(i)] = chr(90-(i-65))

	

	for char in code:
		if ord(char) < 65 or ord(char) > 90:
			output += char
		else:
			output += decoder[char]

	return output

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def number_decode(code):
	code_chop = code.split('-')
	output = ""

	print code_chop
	for i in code_chop:
		if is_number(i):
			output+= chr(int(i)+64)
		else:
			output+=i

	return output

#code = number_decode(code)
#print code
#for i in range(0,26):
#	print forward_decoder(code,offset +i)

#print reverse_decoder(code)

print forward_decoder(reverse_decoder(number_decode(code)), 23)


# ord('A')
# ord('Z')