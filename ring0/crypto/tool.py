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

def main():
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
			elif cmd[1] == "file":
				with open(cmd[1], 'r') as f:
					val = f.read()
				history.append(val)
				print(val)
			else:
				val = cmd2[6:].strip("\n")
				history.append(val)
				print_val(val)
		if cmd[0] == "rot13":
			print_val(rot13(val))
		if cmd[0] == "base64":
			print_val(b64(val))
		if cmd[0] == "xor":
			print_vals(xor(val))
		if cmd[0] == "history":
			for i in history:
				print_val(i)
		if cmd[0] == "clear":
			os.system("clear")
		if cmd[0] == "exit":
			exit()

def xor(val):
	arr = []
	for j in range(16):
		f = ''.join(chr(ord(i) ^ j) for i in val)
		arr.append(f)
	return arr

def rot13(val):
	return codecs.decode(val, "rot_13")

def b64(val):
	return base64.b64decode(val).decode("utf-8")

def print_vals(vals):
	for i in vals:
		print_val(i)

def print_val(val):
	global form

	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

	if form in val:
		print(OKGREEN + val + ENDC)
	else:
		print(val)

def scan():
	print("Not implemented")

main()
