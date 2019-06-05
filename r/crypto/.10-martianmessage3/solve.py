#!/usr/bin/python3

import base64

c = 'RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS'
d = base64.b64decode(c)

for j in range(0xf):
	f = ''.join(chr(i ^ j) for i in d)
	print(f)
