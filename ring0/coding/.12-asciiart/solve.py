#!/usr/bin/python3

from lxml import html
import requests
import hashlib
import re

session = "7uvlvl1ci3tho8pdl2pgrp7ag0"
challenge = "119"


def process(data):
	data = data.replace("&nbsp;", " ")
	data = data.replace("<br />", "\n")
	data = data.replace("\n\n", "\n")
	print(data)

	arr = data.split("\n")
	if arr[0] == "" or arr[0] == "\n" or arr[0] == "\t":
		del arr[0]
	
	nums = []

	for j in range(0, 10):
		nums.append("")
		for i in range(0, 5):
			try:
				nums[j] += arr[j*5+i+1] + "\n"
			except:

				print("Out of range")

	ret = ""
	
	for num in nums:
		n = num.replace("\n", "n").replace(" ", "s")
		if "sxxxsnxsssxnxsssxnxsssxnsxxxsn" in n:
			print("ZERO")
			ret += "0"
		elif "sxxssnxsxssnssxssnssxssnxxxxxn" in n:
			print("ONE")
			ret += "1"
		elif "sxxxsnxsssxsnssxxsnsxsssnxxxxxn" in n:
			print("TWO")
			ret += "2"
		elif "sxxxsnxsssxnssxxsnxsssxnsxxxsn" in n:
			print("THREE")
			ret += "3"
		elif "sxsssxnxssssxnsxxxxxnsssssxnssssxn" in n:
			print("FOUR")
			ret += "4"
		elif "xxxxxnxssssnsxxxxnssssxnxxxxxn" in n:
			print("FIVE")
			ret += "5"
		else:
			print(num)
			print(n)

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

	message = ""
	go = False

	for line in text.split("\n"):
		if "END" in line:
			go = False
		if go:
			message += line
		if "BEGIN" in line:
			go = True
		
	print("="*35 + " Input " + "="*35)
	#print(message)
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

	for l2 in l.split("\n"):
		if "FLAG" in l2:
			print(l2)
	try:
		flag = re.findall(r"FLAG-\w+",data[1])
		print(flag)
	except:
		pass

main()
