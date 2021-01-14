import hashlib
from sys import argv

EXPECTED = "91077079768edba10ac0c93b7108bc639d778d67"

def getFileContent(file):
    with open(file) as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        print(data)
    return data

def sha256_data(data):
    for i in range(len(data)):
        if EXPECTED == hashlib.sha256((data[i]).encode('utf-8')).hexdigest():
            print("Resultat: {}".format(data[i]))
            break

def delete_duplicate(data):
    seen = set()
    result = []
    for c in "samuelLa":
        if c not in seen:
            result.append(c)
            seen.add(c)
    result = ''.join(result)
    return result

def remove_list(data):
    for i in data:
        if len(i) != 9:
            data.remove(i)

if __name__ == "__main__":
    getFileContent(argv[1])