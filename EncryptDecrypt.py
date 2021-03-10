import random
from string import ascii_lowercase
msg = input('enter string:')
alph =''
for i in ascii_lowercase:
    alph+=i
print(alph)

key = random.randint(1,10)
encrypt=''
decrypt=''
for i in msg:
    pos = alph.find(i)
    newpos=(pos+5)%26
    encrypt+=alph[newpos]
print(encrypt)
for i in encrypt:
    pos2 = alph.find(i)
    newpos2=(pos2-5)%26
    decrypt+=alph[newpos2]
print(decrypt)

