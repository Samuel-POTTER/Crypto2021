import hashlib
from sys import argv
EXPECTED = "3281e6de7fa3c6fd6d6c8098347aeb06bd35b0f74b96f173c7b2d28135e14d45"
EXPECTED1 = "26cf6104795a1e5b6bd235c3a3420053703807a212048ceb49b4b9d260a608bb"
SALT = "5UA@/Mw^%He]SBaU"

def getFileContent(file):
    with open(file) as f:
        data = f.readlines()
        data = [x.strip() for x in data]

    for i in range(len(data)):
        if EXPECTED == hashlib.sha256((data[i] + SALT).encode('utf-8')).hexdigest() or EXPECTED1 == hashlib.sha256((data[i] + SALT).encode('utf-8')).hexdigest():
            print("Resultat: {}".format(data[i]))
            break


if __name__ == "__main__":
    getFileContent(argv[1])