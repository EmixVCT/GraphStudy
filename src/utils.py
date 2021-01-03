
debug_v = False

# debug function
def debug(*args):
	if debug_v:
		for i in range(len(args)):
			print(args[i], end='');
		print("")

def set_debug(v):
	global debug_v

	debug_v = v;