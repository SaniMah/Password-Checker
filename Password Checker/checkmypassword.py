import requests
import hashlib #allows you to do SHA1 hashing
import sys

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code!= 200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
	return res

def get_password_leaks_count(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	#splitline - returns the lines in a string
	for h,count in hashes:
		if h == hash_to_check:
			return count #the number of times the password has being hacked
	return 0

#hash_to_check is the tail end of the password that I never sent to anybody


def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char)
	print(first5_char, tail)
	print(response)
	return get_password_leaks_count(response,tail)

def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count: 
			print(f'{password} was found {count} times...you should probably change your password')
		else:
			print(f'{password} was NOT found. Carry on!')
	return 'done!'

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))




#hashing a password 
#hash a passowrd when storing a user's password
#run it through a hashing algorithm to make it gibberish 
#SHA1 is a type of hashing algorithms
#kanonmity - allows someone to receive infomation about but not know who we are 
#idempotent - a function given an input always outputs the same output 
