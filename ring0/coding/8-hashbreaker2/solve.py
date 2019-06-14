#!/usr/bin/python3

from lxml import html
import requests
import hashlib
import re

session = "7uvlvl1ci3tho8pdl2pgrp7ag0"
challenge = "57"


def process(data):
	#data = int(data, base=2)
	data = data.split("\n")
	h = data[1]
	s = data[7]
	
	h = h.replace("<br />", "").replace(" ", "").replace("	", "")
	s = s.replace("<br />", "").replace(" ", "").replace("	", "")
	print(h)
	print(s)
	

	for i in range(0, 10000):
		m = hashlib.sha1()
		m.update(str(i).encode())
		h = m.hexdigest()
		if h == data:
			ret = str(i)
	
	exit()	
			

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
	message = ""

	is_m = False
	for line in text.split("\n"):
		if "BEGIN HASH" in line:
			is_m = True
		elif "END SALT" in line:
			is_m = False
		elif is_m:
			message = message + "\n" + line

	print("="*35 + " Input " + "="*35)
	result = process(message)

	answerUrl = 'https://ringzer0team.com/challenges/' + challenge + "/" + result
	data = requests.get(answerUrl, cookies=cookie).content
	data=data.decode().split('<div class="alert alert-info">')

	print("")


	try:
		flag = re.findall(r"FLAG-\w+",data[1])
		print(flag)
	except:
		print("No flag")

main()
