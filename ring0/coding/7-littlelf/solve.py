#!/usr/bin/python3

from lxml import html
import requests
import hashlib
import base64
import re

session = "7uvlvl1ci3tho8pdl2pgrp7ag0"


def process(data):
	print("="*35 + " Input " + "="*35)
	print(data)

	can_decode = True
	i = 0
	
	while can_decode:
		i += 1
		try:
			temp = base64.b64decode(data)
			print(str(temp))
			print("")
			data = temp

			if "\\" in str(data):
				can_decode = False
				print("Finished after " + str(i) + " decodes")
		except:
			can_decode = False
			print("Finished after " + str(i) + " decodes")

	with open("file.elf", "wb") as f:
		f.write(data)
	
	exit()

	ret = data
	
	print("-"*80)

	print(ret)
	return ret


def main():
	cookie = {'PHPSESSID': session}
	page = requests.get('https://ringzer0team.com/challenges/13', cookies=cookie)
	text = page.text

	if "Do not brute" in text:
		print("Login failed")
		exit()

	tree = html.fromstring(page.content)
	message = tree.xpath('/html/body/div[2]/div/div[2]/div/text()[2]').pop().strip()

	result = process(message)

	answerUrl = 'https://ringzer0team.com/challenges/13/' + result
	data = requests.get(answerUrl, cookies=cookie).content
	data=data.decode().split('<div class="alert alert-info">')

	print("")

	try:
		flag = re.findall(r"FLAG-\w+",data[1])
		print(flag)
	except:
		print("No flag")

main()
