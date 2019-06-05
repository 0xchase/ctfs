#!/usr/bin/python3
import codecs

def ch25():
	c = 'SYNTPrfneVfPbbyOhgAbgFrpher'
	c = 'Ayowe awxewr nwaalfw die tiy rgw fklf ua xgixiklrw! Tiy lew qwkxinw.'
	t = 'FLAG'
	for i in range(0, len(t)):
		cc, tc  = c[i], t[i]
		co, to = ord(cc), ord(tc)
		print(i, cc, tc, co, to, co - to, to - co, to ^ co)
	# => rot13
	print(codecs.encode(c, 'rot13'))

if __name__ == '__main__':
	ch25()
