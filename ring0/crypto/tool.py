#!/usr/bin/python3

# Figure out best way to layer: update command lists value
# Scan tries everything on layer
# Brute tries everything with no bad characters or failures recursivley
# Print command automatically colors anything with flag, ctf, or { and }
# Sequence commands with ;
# Get capital lettors
# Variable rotation amount
# base16/32

import codecs
import os
import base64

form = "FLAG"
found_flag = False
last = ""

def main():
	global found_flag
	global last

	history = []
	val = "RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS"
	print("input, rot13, exit")
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
		if cmd[0] == "rot13":
			print_val(rot13(val))
		if cmd[0] == "base64":
			print_val(b64(val))
		if cmd[0] == "xor":
			print_vals(xor(val))
		if cmd[0] == "getupper":
			print_val(getupper(val))
		if cmd[0] == "history":
			for i in history:
				print_val(i)
		if cmd[0] == "brute":
			try:
				found_flag = False
				brute(val, 0)
			except:
				print("Exception")
		if cmd[0] == "help":
			help()
		if cmd[0] == "clear":
			os.system("clear")
		if cmd[0] == "exit":
			exit()

def help():
	print("input, read, update")
	print("rot13, base64, xor, getupper")
	print("history, brute, clear, exit")

def getupper(val):
	s = ""
	for c in val:
		if c.isupper():
			s += c
	return s

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

def print_vals(vals):
	for i in vals:
		print_val(i)

def brute(val, depth):
	global found_flag

	if depth > 4 or val == None or found_flag:
		return None

	arr = []
	arr.append(rot13(val))
	arr.append(b64(val))
	arr += xor(val)
	
	for i in arr:
		if i == None:
			pass
		elif is_flag(i):
			found_flag = True
			print_val(i)
			return
		else:
			brute(i, depth + 1)

def is_flag(val):
	global form

	if val == None:
		return

	if form in val:
		return True
	else:
		return False
	

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

	if is_flag(val):
		print(OKGREEN + val + ENDC)
	else:
		print(val)
	last = val

def scan():
	print("Not implemented")

main()
