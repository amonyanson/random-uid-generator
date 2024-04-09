import random

import string

import time

def random_uid(): 
	num_characters = int(input('Enter number of characters:\n')) 
	time.sleep(0.5)
	num_ids = int(input('Enter number of IDS:\n'))
	time.sleep(0.5)
	pool = string.ascii_uppercase + string.digits
	random_ids = [''.join(random.choice(pool) for _ in range(num_characters)) for _ in range(num_ids)]
	for key in random_ids:
		time.sleep(1)
		print(key)
		time.sleep(1)
		print("Successfully done")
random_uid()
