#!/usr/bin/python3

from lxml import html
import requests
import hashlib
import re

session = "7uvlvl1ci3tho8pdl2pgrp7ag0"
challenge = "32"


def process(data):
	#data = int(data, base=2)

	arr = data.split(" ")
	print(arr)
	ret = int(arr[0]) + int(arr[2], 16) - int(arr[4], base=2)

	ret = str(ret)

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
