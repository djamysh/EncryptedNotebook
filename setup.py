from encryption import encrypt

from passlib.hash import sha256_crypt

import screeninfo
import pickle

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
	resulationInfo = screeninfo.get_monitors()[0]# 0'th index, because I assume the first monitor.
	resulation = (resulationInfo.width,resulationInfo.height)
	pickle.dump(resulation,open("resulationInfo.pkl","wb"))

	filePath = input("File Path : ")
	password = input("Password : ")
	setup(filePath,password)
	print("Setup Finished !")
	
