import random 
import string

def random_uid():
	pool = string.ascii_uppercase + string.digits
	random_id = ''.join(random.choice(pool) for _ in range(6))
	return random_id
print(random_uid())
