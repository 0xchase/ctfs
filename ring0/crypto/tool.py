#!/usr/bin/python3

# Substitution cipher for default challenge
# Scan tries everything on layer
# Print command automatically colors anything with flag, ctf, or { and }
# Sequence commands with ;
# Variable shift amount, different alphabets
# vigenere cipher
# Number array to ascii
# Transportation cipher
# RSACTFTool - Recover private key with various attacks
# RSATool - Generate private key using p and q
# FeatherDuster - Automated tool
# Rsa package: decrypt with private, etc
# crack: built in john commands with rockyou.txt. Links to websites with crackers.
# Everything in the pycipher docs
# Change form to contents
# Add start variable. Will highlight characters in correct location
# Add end variable. Will highlight characters in correct location

import codecs
import os
import base64
import string
from bubblepy import BubbleBabble

form = "FLAG"
found_flag = False
last = ""

def main():
	global found_flag
	global last
	global form

	history = []
	val = "RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS"
	val = "SYNTPrfneVfPbbyOhgAbgFrpher"
	val = "Ayowe awxewr nwaalfw die tiy rgw fklf ua xgixiklrw! Tiy lew qwkxinw."
	help()
	while True:
		print(">> ", end="")
		cmd2 = input()
		cmd = cmd2.split(" ")
		
		if cmd[0] == "input":
			if len(cmd) == 1:
				print(val)
			else:
				val = cmd2[6:].strip("\n")
				history.append(val)
				print_val(val)
		if cmd[0] == "read":
			with open(cmd[1], 'r') as f:
				val = f.read()
			history.append(val)
			print(val)
		if cmd[0] == "update":
			history.append(val)
			val = last
		if cmd[0] == "form":
			if len(cmd) > 1:
				form = cmd[1]
			else:
				print(form)
		if cmd[0] == "rot13":
			print_val(rot13(val))
		if cmd[0] == "base64":
			print_val(b64(val))
		if cmd[0] == "base32":
			print_val(b32(val))
		if cmd[0] == "base16":
			print_val(b16(val))
		if cmd[0] == "xor":
			print_vals(xor(val))
		if cmd[0] == "baconian":
			print_val(baconian(val))
			temp = val.lower()
			temp = temp.replace("a", "B")
			temp = temp.replace("b", "A")
			print_val(baconian(temp))
		if cmd[0] == "shift":
			print_vals(shift(val))
		if cmd[0] == "bubblebabble":
			print_val(bubblebabble(val))
		if cmd[0] == "getupper":
			print_val(getupper(val))
		if cmd[0] == "tolower":
			print_val(tolower(val))
		if cmd[0] == "toupper":
			print_val(toupper(val))
		if cmd[0] == "replace":
			print_val(replace(val, cmd[1], cmd[2]))
		if cmd[0] == "remove":
			print_val(replace(val, cmd[1], ""))
		if cmd[0] == "history":
			for i in history:
				print_val(i)
		if cmd[0] == "brute":
			#try:
			found_flag = False
			brute(val, 0, [])
			#except Exception as e:
			#	print(e)
		if cmd[0] == "help":
			help()
		if cmd[0] == "clear":
			os.system("clear")
		if cmd[0] == "exit" or cmd[0] == "q":
			exit()

def help():
	print(" Inputs:	input, read, update")
	print(" Ciphers:	rot13, xor, shift, bubblebabble, baconian")
	print(" Decoders:	base64, base32, base16")
	print(" Mod:		remove, getupper, toupper, tolower")
	print(" Replace:	upper, lower, symbols, newlines, spaces")
	print(" Utility:	history, brute, clear, exit")

def shift(val):
	letters = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"]
	ret = []
	for i in letters:
		ret += shift2(val, i)
	return ret

def shift2(message, LETTERS):
	#LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	ret = []

	for key in range(len(LETTERS)):
		translated = ''
		for symbol in message:
			if symbol in LETTERS:
				num = LETTERS.find(symbol)
				num = num - key
				if num < 0:
					num = num + len(LETTERS)
				translated = translated + LETTERS[num]
			else:
				translated = translated + symbol
		ret.append(translated)
	return ret


def baconian(message):
	lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab', 'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba', 'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb', 'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}
	failures = 0

	message = message.lower()
	decipher = '' 
	i = 0
	while True: 
		if(i < len(message)-4): 
			substr = message[i:i + 5] 
			if(substr[0] != ' '): 
				try:
					decipher += list(lookup.keys())[list(lookup.values()).index(substr)] 
				except:
					failures += 1
				i += 5
			else: 
				decipher += ' '
				i += 1
		else: 
			break
	if failures > 0:
		print("Encountered " + str(failures) + " lookup failures")
	return decipher

def bubblebabble(val):
	bb = BubbleBabble()
	try:
		return str(bb.decode(val).decode("utf-8"))
	except:
		return None

def replace(val, a, b):
	ret = ""
	if a == "upper":
		for i in val:
			if i.isupper():
				ret += b
			else:
				ret += i
		return ret
	elif a == "lower":
		for i in val:
			if i.islower():
				ret += b
			else:
				ret += i
		return ret
	elif a == "space" or a == "spaces":
		return val.replace(" ", b)
	elif a == "symbols":
		s = "!@#$%^&*,.\'"
		for c in s:
			val = val.replace(c, b)
		return val
	elif a == "newline" or a == "newlines":
		return val.replace("\n", b)
	else:
		return val.replace(a, b)

def getupper(val):
	s = ""
	for c in val:
		if c.isupper():
			s += c
	return s

def toupper(val):
	return val.upper()

def tolower(val):
	return val.lower()

def xor(val):
	arr = []
	for j in range(16):
		f = ''.join(chr(ord(i) ^ j) for i in val)
		arr.append(f)
	return arr

def rot13(val):
	try:
		return codecs.decode(val, "rot_13")
	except:
		return None

def b64(val):
	try:
		return base64.b64decode(val).decode("utf-8")
	except:
		return None
def b32(val):
	try:
		return base64.b32decode(val).decode("utf-8")
	except:
		return None
def b16(val):
	try:
		return base64.b16decode(val).decode("utf-8")
	except:
		return None

def print_vals(vals):
	for i in vals:
		print_val(i)

def brute(val, depth, path):
	global found_flag

	if depth == 0:
		print("Do these once")

	if depth > 4 or val == None or found_flag:
		return None

	arr = []
	arr.append((rot13(val), path + ["rot13"]))
	arr.append((b64(val), path + ["b64"]))
	k = 0
	for a in xor(val):
		arr.append((a, path + ["xor " + str(k)]))
		k = k + 1
	
	for i, j in arr:
		if i == None:
			pass
		elif is_flag(i):
			found_flag = True
			print(j)
			print_val(i)
			return
		else:
			brute(i, (depth + 1), j)

def is_flag(val):
	global form

	if val == None:
		return

	if form.lower() in val:
		return True
	else:
		return False
	
def like_flag(val):
	global form
	contains = True
	
	for c in form.lower():
		if not c in val:
			contains = False

	return contains

def print_val(val):
	global form
	global last

	if val == None:
		print("Invalid string")
		return

	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	
	if is_flag(val.lower()):
		print(OKGREEN + val + ENDC)
	elif like_flag(val.lower()):
		print(WARNING + val + ENDC)
	else:
		print(val)

	last = val

def scan():
	print("Not implemented")

main()
