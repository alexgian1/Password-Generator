#Password Generator
import random

numbers = ['1','2','3','4','5','6','7','8','9','0']
letters_lowercase = ["a","b","c","d","e","f",'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letters_uppercase = [letter.upper() for letter in letters_lowercase]
characters = ['!','@','#','$','%','^','&','*','(',')']
password = []

cont_numbers = False
cont_lowercase = False
cont_uppercase = False
cont_characters = False
validPassword = False

length = int(raw_input("Enter Password Length (6-30): "))
if length >= 6 and length <= 30:
	choice_numbers = raw_input("Contain Numbers? Y/N: ")
	if choice_numbers == "y" or choice_numbers == "Y":
		cont_numbers = True
		validPassword = True
	choice_lowercase = raw_input("Contain Lowercase Letters? Y/N: ")
	if choice_lowercase == "y" or choice_lowercase == "Y":
		cont_lowercase = True
		validPassword = True
	choice_uppercase = raw_input("Contain Upercase Letters? Y/N: ")
	if choice_uppercase == "y" or choice_uppercase == "Y":
		cont_uppercase = True
		validPassword = True
	choice_characters = raw_input("Contain Special Characters? Y/N: ")
	if choice_characters == "y" or choice_characters == "Y":
		cont_characters = True
		validPassword = True

if validPassword:
	allowedCharacters = []
	if cont_numbers == True:
		for i in numbers:
			allowedCharacters.append(i)
	if cont_lowercase == True:
		for i in letters_lowercase:
			allowedCharacters.append(i)
	if cont_uppercase == True:
		for i in letters_uppercase:
			allowedCharacters.append(i)
	if cont_characters == True:
		for i in characters:
			allowedCharacters.append(i)
	
	random.shuffle(allowedCharacters)
	while len(password) < length:
		for i in allowedCharacters:
			if len(password) >= length:
				break
			else:
				password.append(i)
	
	print "\n","".join(password)
raw_input()
			
