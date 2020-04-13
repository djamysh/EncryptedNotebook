

import screeninfo,os,pickle
from functions import HandleFile,get_path


def get_resulation():
	resulationInfo = screeninfo.get_monitors()[0]# Assuming the first monitor.			
	return resulationInfo

def systemSetup():
	path = get_path()
	resulation = get_resulation()
	Info = {"path":path,"width":resulation.width,"height":resulation.height}
	if not os.path.isdir(path+"Data/"):
		os.mkdir(path+"Data/")

	pickle.dump(Info,open(path+"Data/sysInfo.pkl","wb"))
	print("Setup completed.")


if __name__ == "__main__":
	systemSetup()
	HandleFile("test","/home/brad/testfile.txt","123456789")



	"""

	pickle.dump(resulation,open("resulationInfo.pkl","wb"))

	filePath = input("File Path : ")
	password = input("Password : ")
	setup(filePath,password)
	print("Setup Finished !")
	"""
