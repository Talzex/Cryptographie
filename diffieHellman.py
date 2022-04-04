import random
MIN = 100000
MAX = 100000000000000000000000000

def main():
    p = random.randint(MIN, MAX) 
    g = random.randint(MIN, p)

    while(not test_premier(p) or not test_premier(g)):
        p = random.randint(MIN, MAX)
        g = random.randint(MIN, p)
    print("Les 2 nombres premiers sont : p=" + str(p) + " et g=" + str(g))
    a = random.randint(MIN, MAX) #Alice
    b = random.randint(MIN, MAX) #Bob
    ga = puissance(g, a, p) #Message de Alice à Bob
    gb = puissance(g,b,p) #Message de Bob à Alice
    gba = puissance(gb,a,p) #Alice calcul
    gab = puissance(ga,b,p) #Bob Calcul
    k = gab
    print("La clé échangée est k : " + (str(k)))

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
main()