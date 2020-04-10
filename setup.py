from encryption import encrypt

def setup(filePath,password):
	with open(filePath,"r") as file:
		data = file.read()
	
	data = data.encode("utf-8")
	password = password.encode("utf-8")
	encrypted = encrypt(password,data)
	with open("encrypted.txt","w") as file:
		file.write(encrypted)

if __name__ == "__main__":
	filePath = input("File Path : ")
	password = input("Password : ")
	setup(filePath,password)
	print("Setup Finished !")

