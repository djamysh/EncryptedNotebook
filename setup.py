

import screeninfo,os,pickle
from functions import HandleFile,get_path


def get_resulation():
	resulationInfo = screeninfo.get_monitors()[0]# Assuming the first monitor.			
	return resulationInfo

def systemSetup():
	path = get_path()
	resulation = get_resulation()
	Info = {"path":path,"width":resulation.width,"height":resulation.height}
	if not os.path.isdir(path+"Data{}".format(os.sep)):
		os.mkdir(path+"Data{}".format(os.sep))

	pickle.dump(Info,open(path+"Data{}sysInfo.pkl".format(os.sep),"wb"))
	print("Setup completed.")


if __name__ == "__main__":
	systemSetup()