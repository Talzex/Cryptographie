import random
import numpy as np
import rsa as r
MINCA = 10000000
MAXCA = 10000000000000

def main():
    #############################################################################
    ######################### ALICE #############################################
    #############################################################################
    pA = random.randint(r.MIN, r.MAX)
    qA = random.randint(r.MIN, r.MAX)
    while(not r.test_premier(pA) or not r.test_premier(qA)):
        pA = random.randint(r.MIN, r.MAX)
        qA = random.randint(r.MIN, r.MAX)
    nA = pA*qA
    phiA=(pA-1)*(qA-1)
    print("Alice : 2nb premiers pA : ",pA," et qA : ",qA)
    
    #Clé publique Alice
    eA = random.randint(1,1000)%(phiA-1)+1 
    while(r.pgcd(eA,phiA) != 1):
        eA = random.randint(1,1000)%(phiA-1)+1
    print("Alice : clé publique (",eA,",",nA,")")

    #Clé privée Alice
    dA = r.bezout(eA,phiA)
    if(dA < 0):
        dA+=phiA
    print("Alice : clé privée (",dA,",",nA,")")


    #############################################################################
    ######################### CA ################################################
    #############################################################################


    pCA = random.randint(MINCA, MAXCA)
    qCA = random.randint(MINCA, MAXCA)
    while((not r.test_premier(pCA) or not r.test_premier(qCA)) and pCA > pA and qCA > qA):
        pCA = random.randint(MINCA, MAXCA)
        qCA = random.randint(MINCA, MAXCA)
    nCA = pCA*qCA
    phiCA=(pCA-1)*(qCA-1)
    print("CA : 2nb premiers pCA : ",pCA," et qCA : ",qCA)

    #Clé publique CA
    eCA = random.randint(1,1000)%(phiCA-1)+1 
    while(r.pgcd(eCA,phiCA) != 1):
        eCA = random.randint(1,1000)%(phiCA-1)+1
    print("CA : clé publique (",eCA,",",nCA,")")

    #Clé privée CA
    dCA = r.bezout(eCA,phiCA)
    if(dCA < 0):
        dCA+=phiCA

    #CA : clé privée (dCA,nCA)
    print("CA : clé privée (",dCA,",",nCA,")")

    
    #Calcul Empreinte 
    empreinteA = eA%100
    m = str(eA) + "," + str(empreinteA)
    print("Message d'Alice (Clé publique + empreinte) : " +  str(m))

    # On chiffre la clé publique d'Alice avec la clé publique de CA (destinataire)
    cm = r.puissance(eA,eCA,nCA) 
    print("Clé publique d'Alice chiffrée avec la clé publique de CA : " + str(cm))

    # On chiffre l'empreinte d'Alice avec sa clé privée et avec la clé publique de CA (destinataire)
    cemp = r.puissance(empreinteA,dA,nA)
    cempCA = r.puissance(cemp,eCA,nCA) 
    print("Empreinte d'Alice chiffrée a clé privée et avec la clé publique de CA : " + str(cemp))
    print("Envoie du message au CA....")


    # On déchiffre 
    m1 = r.puissance(cm,dCA,nCA)
    print("Clé publique d'Alice dechiffrée : " + str(m1))

    if(m1 == eA):
        print("Les clés sont identiques")

    cemp1 = r.puissance(cempCA,dCA,nCA)
    empreinteA1 = r.puissance(cemp1,eA,nA)
    print("Empreinte d'Alice dechiffrée avec dCA et eA : " + str(empreinteA1))
    if(empreinteA1 == empreinteA):
        print("Empreinte Verifiée")

    

    certificat = r.puissance(eA,dCA,nCA)
    print("Envoie du cerficat à BOB... : " + str(certificat))

    #############################################################################
    ######################### BOB ###############################################
    #############################################################################

    eABob = r.puissance(certificat,eCA,nCA) # Déchiffrement du certificat par BOB
    if(eABob == eA):
        mBob = random.randint(0,1000)
        print("Certificat vérifié")

        print("Bob envoie le message " + str(mBob) + " à Alice")
        cmBob = r.puissance(mBob,eABob,nA)

        #############################################################################
        ######################### ALICE #############################################
        #############################################################################
        mBob1 = r.puissance(cmBob,dA,nA)
        print("Alice reçoit le message " + str(mBob1))
main()


    
    



    
    



    
    



    
    



    
    



    
    

    
    

    
    


