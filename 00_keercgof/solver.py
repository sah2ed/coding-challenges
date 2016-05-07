from collections import Counter
import os

def count_occurrences():
	counter = Counter()

	# The input file 'problem.txt' should be in the same folder.
	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	
	with open(os.path.join(__location__, 'problem.txt'), 'r') as corpus:
		for line in corpus:
			line = line.strip()
			for i in range(0, len(line)):
				counter[line[i]] = counter[line[i]] + 1

	return counter


def main():
	counter = count_occurrences()
	answer = ''.join([k for k,v in counter.most_common()])
	print( answer[0:answer.index('_')] ) # will print "binoculars"



if __name__ == "__main__":
	main()
