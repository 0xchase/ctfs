#!/usr/bin/python3

from lxml import html
import requests
import hashlib
import re
import os
import subprocess

session = "7uvlvl1ci3tho8pdl2pgrp7ag0"
challenge = "125"


def process(data):
	#data = int(data, base=2)
	code = data
	program = "char code[] = \"" + code + "\";int main(int argc, char **argv){	int (*ret)() = (int(*)())code;	ret();}"

	text_file = open("file.c", "w")
	text_file.write(program)
	text_file.close()

	os.system("gcc -z execstack -fno-stack-protector -Wall file.c -o file.x")
	os.system("script -c ./file.x output.txt")
	
	f = open("output.txt", "r")
	ret = f.read().split("\n")[1]

	print("")
	print("Printed: " + ret)

	exit()


	#exit()
	print("-"*80)
	print(ret)
	return ret

def cmd(cmd):
	return subprocess.check_output(cmd.split(" "))

def main():
	cookie = {'PHPSESSID': session}
	page = requests.get('https://ringzer0team.com/challenges/' + challenge, cookies=cookie)
	text = page.text

	if "Do not brute" in text:
		print("Login failed")
		exit()

	tree = html.fromstring(page.content)
	message = tree.xpath('/html/body/div[2]/div/div[2]/div/text()[2]').pop().strip()

	print("="*35 + " Input " + "="*35)
	print(message)
	result = process(message)

	answerUrl = 'https://ringzer0team.com/challenges/' + challenge + "/" + result
	data = requests.get(answerUrl, cookies=cookie).content
	data=data.decode().split('<div class="alert alert-info">')

	print("")


	for l in data:
		if "FLAG" in l:
			print("Found flag:")
		else:
			print("No flag")

	try:
		flag = re.findall(r"FLAG-\w+",data[1])
		print(flag)
	except:
		pass

main()
