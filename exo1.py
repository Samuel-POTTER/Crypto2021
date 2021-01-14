import hashlib
from sys import argv
EXPECTED = "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b"

def getFileContent(file):
    with open(file) as f:
        data = f.readlines()
        data = [x.strip() for x in data] 
    for i in range(len(data)):
        if EXPECTED == hashlib.sha256(data[i].encode('utf-8')).hexdigest():
            print("Resultat: {}".format(data[i]))

if __name__ == "__main__":
    getFileContent(argv[1])