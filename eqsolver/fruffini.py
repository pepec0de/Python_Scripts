#!/usr/bin/python3

import string

alpha = string.ascii_lowercase

# Printing table:
out = []
# Math ops:
table = []

def main(lenght):
	for i in range(0, lenght):
		out.append(alpha[i])
		out
	print(out)

if __name__ == "__main__":
	main(3)
