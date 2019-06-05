import codecs

def ch25():
	c = 'SYNTPrfneVfPbbyOhgAbgFrpher'
	t = 'FLAG'
	for i in range(0, len(t)):
		cc, tc  = c[i], t[i]
		co, to = ord(cc), ord(tc)
		print(i, cc, tc, co, to, co - to, to - co, to ^ co)
	# => rot13
	print(c.encode('rot13'))


c = 'SYNTPrfneVfPbbyOhgAbgFrpher'
print(codecs.decode(c, "rot_13"))
