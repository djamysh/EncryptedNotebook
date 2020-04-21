from encryption import encrypt,decrypt
from passlib.hash import sha256_crypt
import pickle,os,base64,sys

def get_path():
    encoding = sys.getfilesystemencoding()
    if hasattr(sys, "frozen"):# Checks is it exe.Frozen script.
        return os.path.realpath(sys.executable)
    return os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1])+os.sep

def encrypting(data,password,dataType = "path"):# dataType:"path","string"
	if dataType == "path":
		with open(data,"r") as file:
			data = file.read()
	elif dataType == "string":
		pass
	else:
		raise Exception("Invalid dataType!")

	data = data.encode("utf-8")
	password = password.encode("utf-8")
	hashed = sha256_crypt.hash(password)
	encrypted = encrypt(password,data)

	return (hashed,encrypted)

def getEncryptedData(tag):
	file_name = tagB64(tag,direction="encode")
	path = loadSystemInfo()["path"] + "Data{}Operands{}{}.pkl".format(os.sep,os.sep,file_name)
	try:
		encrypted_data = pickle.load(open(path,"rb"))
		return encrypted_data

	except FileNotFoundError:
		return False


def loadSystemInfo():
	path = get_path()
	data = pickle.load(open(path+"Data{}sysInfo.pkl".format(os.sep),"rb"))
	return data

def tagB64(tag,direction ="encode"):
	if direction == "encode":
		b64tag = base64.b64encode(tag.encode("utf-8")).decode("utf-8")
	elif direction == "decode":
		b64tag = base64.b64decode(tag.encode("utf-8")).decode("utf-8")
	else:
		raise Exception("Wrong direction !")

	return b64tag

def HandleFile(tag,data,password,dataType = "path",createNew = False):# datatype : path or string
	path = loadSystemInfo()["path"] + "Data{}".format(os.sep)
	if not os.path.isdir(path+"Operands{}".format(os.sep)):
		os.mkdir(path+"Operands{}".format(os.sep))

	if createNew:
		data = path+"blank.txt"
		open(data,"w")

	hashed,encrypted = encrypting(data,password,dataType = dataType)
	tagb64 = tagB64(tag,direction = "encode")
	encrypted_data = {"hashed":hashed,"encrypted":encrypted}

	pickle.dump(encrypted_data,open(path+"Operands{}{}.pkl".format(os.sep,tagb64),"wb"))


def checkData(tag,password):

	encrypted_data = getEncryptedData(tag)
	if encrypted_data:

		if sha256_crypt.verify(password,encrypted_data["hashed"]):
			return True

		else:# Wrong password
			return False
	else:
		return False

def LoadText(tag,password):
	encrypted_data = getEncryptedData(tag)
	decrypted_data = decrypt(password.encode("utf-8"),encrypted_data["encrypted"])
	return decrypted_data.decode("utf-8")

