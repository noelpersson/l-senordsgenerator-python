import string
import random


## tecken som används för att generara lösenordet från
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## användaren anger hur långt lösenoreet ska vara
	length = int(input("Ange längden på lösenordet: "))

	## blandar tecken för att skapa lösenordet
	random.shuffle(characters)
	
	## väljer ett tecken till lösenordet
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## blandar det slutgiltiga lösenordet
	random.shuffle(password)

	## konverterar tecken till ett läsvänligt lösenord
	## skriver ut lösenordet
	print("".join(password))



## invoking the function
generate_random_password()