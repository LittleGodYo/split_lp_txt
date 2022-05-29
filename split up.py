# Splitting into a username/password from notepad

with open('up.txt', 'r') as dictionary:
 f = dictionary.read()
 mydict = {}
 listKey = []
 listValue = []
 a = 1
 for line in f.split("\n"):
    if not line.strip():
        continue
    k, v = [word.strip() for word in line.split(":")]
    mydict[k] = v
    listKey.append(k) #List Login
    listValue.append(v) #List Pass
