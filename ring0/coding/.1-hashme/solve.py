#!/usr/bin/python3

from lxml import html
import requests
import hashlib
import re

session = "7uvlvl1ci3tho8pdl2pgrp7ag0"


def process(data):
	print("="*35 + " Input " + "="*35)
	print(data)

	data=data.encode('utf-8')
	ret = hashlib.sha512(data).hexdigest()

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

	flag = re.findall(r"FLAG-\w+",data[1])
	print(flag)

main()
