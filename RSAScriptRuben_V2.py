#!usr/bin/python3
import random
from fractions import gcd

__author__="Wylleman Ruben"
__version__="Version 2"


def inputnumbers():
  '''
  # input: manual !! prime integer value

  This function will take care of the input and make this input available
  for futur functions.
  '''
  global p
  global q
  print("1) Select Primes")
  p = int(input("p = "))
  q = int(input("q = "))

def calcmodulus(a,b):
  '''
  # input: prime a, prime b

  this functions will calculate the modulus from 2 prime numbers
  '''
  global n
  n = a * b
  print('modulus n = p * q = {}'.format (n))

def calcphi(a,b):
  '''
  # input: prime a, prime b

  this functions calculates the phi value from 2 prime numbers
  for RSA calculation
  '''
  global phi
  phi=(a-1)*(b-1)
  print('phi = (p-1) * (q-1) = {} '.format (phi))

def Select_e(a):
  '''
  #input: phi

  this function will calculate a value for e to work with the input phi.
  '''
  global e
  e = random.randrange(1,a)
  g = gcd(e,a) 
  while g != 1:
    e = random.randrange(1,a)
    g = gcd (e,a)
  print("choose public key e: {}".format (e))
  print("[*] {} and {} have no common factors except 1".format(e,a))

def find_d(a,b):
  '''
  # input: the value for e, the value for phi

  this function will find a value for d to use RSA encryption
  '''
  global d
  d = 1
  temp = (a*d)-1
  while temp % b != 0:   
    d = d+1
    temp = (a*d)-1
  print("computed private key d = {}".format (d))
  calc=(e*d)%b
  print("[*] {} * {} mod {} = {}".format (a,d,b,calc))
 
def encrypt(a):
  '''
  # input: message to encrypt

  this function will encrypt a message using the generated public key and return  it's output
  '''
  output = a ** e % n
  print("encrypted message c = m ** e % n = {}".format(output))
  return output

def decrypt(a):
  '''
  # input: message to decrypt

  this function will decrypt the message using the private key generated 
  in this  script. the decrypted message will return as output.
  '''
  output = a ** d % n
  print ("decrypted message mm = c ** d % n = {}".format(output))
  return output

def test(a,b):
  '''
  # input: message before encryption (m), message after decryption (mm)

  this function will test the functionality of this script.
  '''
  if a == b:
    print("is m == mm ? ... OK working example")
  else:
    print("is m == mm ? ... ERROR, RSA code faulty")

def main():
  '''
  This is the main script for the RSA calculation.
  '''
  inputnumbers()
  print()
  calcmodulus(p,q)
  calcphi(p,q)
  print()
  Select_e(phi)
  print()
  find_d(e,phi)
  print()
  m=int(input("Select message m: "))
  print()
  m_enc=encrypt(m)
  mm=decrypt(m_enc)
  print()
  test(m,mm)


