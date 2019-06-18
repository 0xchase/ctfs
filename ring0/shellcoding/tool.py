#!/usr/bin/python3

import os
import subprocess

# Color output
# Can automatically encode with msfvenom
# Can auto encode with simple encoder than pushes onto stack, increments, and jumps
# Can change file with "f" or "file"
# Move badchars to text file for persistance
# Fix badchar detection only in hex columns

shellcode_mode = True

badchars = "\\x01\\x02\\x03\\x04"

def main():
	global badchars
	with open("badchars.txt", "r") as f:
		badchars = f.read()
	print("Badchars: " + badchars)

	while True:
		print(">> ", end="")
		cmd2 = input()
		cmd = cmd2.split(" ")

		if cmd[0] == "r":
			if shellcode_mode:
				cmd[0] = "r2"
			else:
				cmd[0] = "r1"
		if cmd[0] == "g":
			if shellcode_mode:
				cmd[0] = "g2"
			else:
				cmd[0] = "g1"
	
		if cmd[0] == "q":
			exit()
		elif cmd[0] == "e":
			os.system("vim main.s")
		elif cmd[0] == "r1":
			os.system("nasm -f elf64 -o main.o main.s")
			os.system("ld -o main.x main.o")
			os.system("./main.x")
			os.system("rm main.o && rm main.x")
		elif cmd[0] == "r2":
			os.system("nasm -f elf64 -o main.o main.s")
			os.system("ld -o main.x main.o")
			os.system("objdump -d ./main.x|grep \'[0-9a-f]:\'|grep -v \'file\'|cut -f2 -d:|cut -f1-6 -d\' \'|tr -s \' \'|tr \'\t\' \' \'|sed \'s/ $//g\'|sed \'s/ /\\\\x/g\'|paste -d \'\' -s |sed \'s/^/\"/\'|sed \'s/$/\"/g\' > shellcode.txt")
			with open("shellcode.txt", "r") as f:
				shellcode = f.read()
			with open("main.c", "w") as f:
				code = "int main(void){char shellcode[] = " + shellcode + ";(*(void (*)()) shellcode)();return 0;}"
				f.write(code)
			os.system("gcc -fno-stack-protector -z execstack main.c -o main.x")
			os.system("./main.x")
			os.system("rm main.c && rm main.o && rm main.x")
		elif cmd[0] == "g2":
			os.system("nasm -f elf64 -o main.o main.s")
			os.system("ld -o main.x main.o")
			os.system("objdump -d ./main.x|grep \'[0-9a-f]:\'|grep -v \'file\'|cut -f2 -d:|cut -f1-6 -d\' \'|tr -s \' \'|tr \'\t\' \' \'|sed \'s/ $//g\'|sed \'s/ /\\\\x/g\'|paste -d \'\' -s |sed \'s/^/\"/\'|sed \'s/$/\"/g\' > shellcode.txt")
			with open("shellcode.txt", "r") as f:
				shellcode = f.read()
			with open("main.c", "w") as f:
				code = "int main(void){char shellcode[] = " + shellcode + ";(*(void (*)()) shellcode)();return 0;}"
				f.write(code)
			os.system("gcc -fno-stack-protector -z execstack main.c -o main.x")
			os.system("gdb -q main.x")
			os.system("rm main.c && rm main.o && rm main.x")
			#os.system("rm peda*")
		elif cmd[0] == "a":
			print(assemble(cmd2[2:]))
		elif cmd[0] == "p":
			os.system("nasm -f elf64 -o main.o main.s")
			os.system("ld -o main.x main.o")
			asm = subprocess.run(["objdump", "-d", "-M", "intel", "main.x"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip("\n")
			os.system("rm main.o")
			os.system("rm main.x")
			for line in asm.split("\n"):
				if line != "" and "main.x" not in line and ".text" not in line:
					bad = False
					for c in badchars.split("\\x"):
						if c in line[9:] and len(c) == 2:
							bad = True
					if bad:
						print("*" + line[9:])
					else:
						print(line[9:])
		elif cmd[0] == "g1":
			os.system("nasm -f elf64 -o main.o main.s")
			os.system("ld -o main.x main.o")
			os.system("gdb -q main.x")
			os.system("rm main.o && rm main.x")
			os.system("rm peda*")
		elif cmd[0] == "badchars" or cmd[0] == "b":
			if len(cmd) == 1:
				print(badchars)
			else:
				badchars = cmd[1]
				with open("badchars.txt", "w") as f:
					f.write(badchars)
		elif cmd[0] == "s":
			os.system("nasm -f elf64 -o main.o main.s")
			os.system("ld -o main.x main.o")
			os.system("objdump -d ./main.x|grep \'[0-9a-f]:\'|grep -v \'file\'|cut -f2 -d:|cut -f1-6 -d\' \'|tr -s \' \'|tr \'\t\' \' \'|sed \'s/ $//g\'|sed \'s/ /\\\\x/g\'|paste -d \'\' -s |sed \'s/^/\"/\'|sed \'s/$/\"/g\' > shellcode.txt")
			with open("shellcode.txt", "r") as f:
				shellcode = f.read()
			print(shellcode)
			print("Length: " + str(len(shellcode.replace("\\" , "").replace("x", "").replace("\"", ""))))
			os.system("rm main.o && rm main.x && rm shellcode.txt")
		elif cmd[0] == "c" or cmd[0] == "clear":
			os.system("clear")
		elif cmd[0] == "h" or cmd[0] == "help":
			print("p -> print")
			print("e -> edit")
			print("r -> run")
			print("g -> gdb")
			print("s -> shellcode")
			print("b -> badchars")
			print("a -> assemble")
			print("c -> clear")
			print("h -> help")
			print("q -> quit")
		else:
			print("Unknown command")

def assemble(i):
	i = i.replace("\t", "")
	return subprocess.run(["rasm2", i], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode("utf-8").strip("\n")

main()
