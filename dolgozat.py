filepath = "valaszok.txt"
fileobject = open(filepath)
print("1. feladat: Az adatok beolvasása.")

try:
    input("3. feladat: Kérem adja meg a versenyző azonosítóját: ")

fileobject.close()
