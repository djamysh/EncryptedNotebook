from encryption import encrypt

from passlib.hash import sha256_crypt

def setup(filePath,password):
	with open(filePath,"r") as file:
		data = file.read()
	
	data = data.encode("utf-8")
	password = password.encode("utf-8")
	hashed = sha256_crypt.hash(password)
	encrypted = encrypt(password,data)
	with open("encrypted.txt","w") as file:
		file.write(encrypted)
	
	with open("hashed.txt","w") as file:
		file.write(hashed)
		
if __name__ == "__main__":
	filePath = input("File Path : ")
	password = input("Password : ")
	setup(filePath,password)
	print("Setup Finished !")

