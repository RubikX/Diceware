# Description: Passphrase generator emulating the Diceware technique
# Inspired by: Micah Lee's article on The Intercept
# Author: Edison Suen

import secrets

WORDLIST = 'diceware.wordlist.txt'
INDEX_LENGTH = 5

def load():
	word_dict = {}
	with open (WORDLIST) as f:
		for line in f.readlines():
			index, word = line.strip().split('	')
			word_dict[index] = word
	return word_dict

def roll(num_words):
	num_list = [secrets.choice(range(1,6)) for _ in range(INDEX_LENGTH*num_words)]
	list2string = ','.join(str(num_list[i]) for i in num_list)
	list2string = list2string.replace(',','')
	split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
	split_string_list = split_string(list2string,INDEX_LENGTH)
	return split_string_list

def passphrase(num_words):
	passphrase = ''
	word_dict = load()
	list_numbers = roll(num_words)
	for i in list_numbers:
		passphrase += word_dict[i] + ' '
	print("Your passphrase is: {}".format(passphrase))

def main():
	num_words = int(input("Please enter the word length of desired passphrase: "))
	passphrase(num_words)

if __name__ == "__main__":
	main()