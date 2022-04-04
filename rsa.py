import random
import numpy as np
MIN = 100000
MAX = 100000000000000000000000000

def main():
    p = random.randint(MIN, MAX)
    q = random.randint(MIN, MAX)
    while(not test_premier(p) or not test_premier(q)):
        p = random.randint(MIN, MAX)
        q = random.randint(MIN, MAX)
    print("Les 2 nombres premiers sont : p=" + str(p) + " et q=" + str(q))
    n=p*q
    phi=(p-1)*(q-1)
    print("n=p*q = "+str(n))
    print("phi(n) = "+str(phi))
    
    #Clé publique
    e = random.randint(1,1000)%(phi-1)+1 #Demander au prof
    while(pgcd(e,phi) != 1):
        e = random.randint(1,1000)%(phi-1)+1
    print("clé publique :" + str(e) + " , " + str(n))

    #Clé privée
    d = bezout(e,phi)
    if(d < 0):
        d+=phi
    print("clé privée : " + str(d)+ " , " + str(n))

    #Chiffrement de m
    m = random.randint(1,1000)%(n-1)+1
    print("Message en clair m=" + str(m))
    c = puissance(m,e,n)
    print("Message chiffré c=" + str(c))
    m1 = puissance(c,d,n)
    print("Message en clair m1=" + str(m1))

def puissance(a,e,n):
  p = 1
  while (e > 0) :
    if (e % 2 != 0) :
        p = (p * a) % n
    a = (a * a) % n
    e = e // 2
  return p

def test_premier(n):#test de Fermat
  if ((puissance(2,n-1,n)==1) and (puissance(3,n-1,n)==1) and (puissance(5,n-1,n)==1) and
       (puissance(7,n-1,n)==1) and (puissance(11,n-1,n)==1) and (puissance(13,n-1,n)==1)):
    return True #probablement premier (garantie si n<2^15)
  return False

def pgcd(u,v):

  t = 0
  while (v):
    t = u
    u = v
    v = t % v
  return -u if u < 0 else u

def  bezout(a,  b) :
    # On sauvegarde les valeurs de a et b.
    a0 = a
    b0 = b
    # On laisse invariant p*a0 + q*b0 = a et  r*a0 + s*b0 = b.
    p = s = 1
    q = r = c = quotient = nouveau_r = nouveau_s = 0
    
    # La boucle principale.
    while (b != 0) :
        c = a % b
        quotient = a // b
        a = b
        b = c
        nouveau_r = p - quotient * r
        nouveau_s = q - quotient * s
        p = r
        q = s
        r = nouveau_r
        s = nouveau_s
    return p%b0
main()

