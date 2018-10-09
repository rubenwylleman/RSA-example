#!usr/bin/python3
import random

def inputnumbers():
  global p
  global q
  print("1) Select Primes")
  p = int(input("p = "))
  q = int(input("q = "))

def calcmodulus():
  global n
  n = p * q
  print('modulus n = p * q = {}'.format (n))

def calcphi():
  global phi
  phi=(p-1)*(q-1)
  print('phi = (p-1) * (q-1) = {} '.format (phi))

def Select_e():
  global e
  e = random.randrange(1,phi)
  g = gcd(e,phi) 
  while g != 1:
    e = random.randrange(1,phi)
    g = gcd (e,phi)
  print("choose public key e: {}".format (e))
  print("[*] {} and {} have no common factors except 1".format(e,phi))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_d():
  global d
  d = 1
  temp = (e*d)-1
  while temp % phi != 0:   
    d = d+1
    temp = (e*d)-1
  print("computed private key d = {}".format (d))
  calc=(e*d)%phi
  print("[*] {} * {} mod {} = {}".format (e,d,phi,calc))
 
def encrypt(a):
  global c
  c = a ** e % n
  print("encrypted message c = m ** e % n = {}".format(c))

def decrypt(a):
  global mm
  mm = a ** d % n
  print ("decrypted message mm = c ** d % n = {}".format(mm))

def test(a,b):
  if a == b:
    print("is m == mm ? ... OK working example")
  else:
    print("is m == mm ? ... ERROR, RSA code faulty")



inputnumbers()
print()
calcmodulus()
calcphi()
print()
Select_e()
print()
find_d()
print()
m=int(input("Select message m: "))
print()
encrypt(m)
decrypt(c)
print()
test(m,mm)
