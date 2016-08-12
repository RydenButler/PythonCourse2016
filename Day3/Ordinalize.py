def ordinalize(x):
	x = str(x)
	if x[-2:-1] == '1':
		return '%sth' % x
	if x[-1] == '1':
		return '%sst' % x
	if x[-1] == '2':
		return '%snd' % x
	if x[-1] == '3':
		return '%srd' % x
	else:
		return '%sth' % x