#recurse

def stepper(start, step, limit):
	if start < limit:
		print start
		start = start + step
		return summ(start, step, limit)
	else:
		return "finito!"
