import sys, os
import numpy as np
from random import randint

def quickMulMod(a,b,m):
    '''a*b%m,  quick'''
    ret = 0
    while b:
        if b&1:
            ret = (a+ret)%m
        b//=2
        a = (a+a)%m
    return ret

def quickPowMod(a,b,m):
    '''a^b %m, quick,  O(logn)'''
    ret =1
    while b:
        if b&1:
            ret =quickMulMod(ret,a,m)
        b//=2
        a = quickMulMod(a,a,m)
    return ret

def isPrime(n, t=5):
    '''miller rabin primality test, probability result'''
    t = min(n-3,t) #number of iteration
    if n < 2 :
        return
    if n == 2 : 
        return True
    d = n-1
    r = 0
    while d%2 == 0:
        r += 1
        d //= 2
    tested = set()
    for _ in range(t):
        a = randint(2, n-2)
        while a in tested:
            a = randint(2, n-2)
        tested.add(a)
        x= quickPowMod(a,d,n)
        if x == 1 or x == n-1 : 
            continue  #success,
        for _ in range(r-1):
            x= quickMulMod(x,x,n)
            if x == n-1 : 
                break
        else:
            return False
    return True


def gcd(a,b):
    while b != 0 :
        a,b = b,a%b
    return a

def factor(n):
    '''pollard's rho algorithm'''
    if n == 1: 
        return []
    if isPrime(n):
        return [n]
    fact = 1
    cycle_size = 2
    x = x_fixed = 2
    c = randint(1,n)
    while fact == 1:
        for _ in range(cycle_size):
            if fact>1:
                break
            x = ( x * x + c ) % n
            if x == x_fixed:
                c = randint(1,n)
                continue
            fact = gcd(x-x_fixed,n)
        cycle_size *= 2
        x_fixed = x
    return factor(fact) + factor(n//fact)

def factorize(numbers):
    """
        A Faire:         
        - Ecrire une fonction qui prend en paramètre une liste de nombres et qui retourne leurs decompositions en facteurs premiers
        - cette fonction doit retourner un dictionnaire Python où :
            -- la clé est un nombre n parmi la liste de nombres en entrée
            -- la valeur est la liste des facteurs premiers de n (clé). Leur produit correpond à n (clé).  
            
        - Attention : 
            -- 1 n'est pas un nombre premier
            -- un facteur premier doit être répété autant de fois que nécessaire. Chaque nombre est égale au produit de ses facteurs premiers. 
            -- une solution partielle est rejetée lors de la soumission. Tous les nombres en entrée doivent être traités. 
            -- Ne changez pas le nom de cette fonction, vous pouvez ajouter d'autres fonctions appelées depuis celle-ci.
            -- Ne laissez pas trainer du code hors fonctions car ce module sera importé et du coup un tel code sera exécuté et cela vous pénalisera en temps.
    """
    result = {}
    for n in numbers:
        num = n
        res = []
        res = factor(num)
        #add in dectionary
        result[n] = res

    return result # ceci n'est pas une bonne réponse

"""


Sol 1: native algo
    result = {}
    for n in numbers:
        num = n
        res = []
        #factorisation of number num
        while num % 2 == 0:
            num = num / 2
            res.append(2)
        for i in range(1, int(np.sqrt(num)/2)): 
            j = i*2+1
            while num % j == 0:
                num = num / j
                res.append(j)
        if num != 1:
            res.append(int(num))

        #add in dectionary
        result[n] = res

"""

#########################################
#### Ne pas modifier le code suivant ####
#########################################
if __name__=="__main__":
    input_dir = os.path.abspath(sys.argv[1])
    output_dir = os.path.abspath(sys.argv[2])
    
    # un repertoire des fichiers en entree doit être passé en parametre 1
    if not os.path.isdir(input_dir):
	    print(input_dir, "doesn't exist")
	    exit()

    # un repertoire pour enregistrer les résultats doit être passé en parametre 2
    if not os.path.isdir(output_dir):
	    print(input_dir, "doesn't exist")
	    exit()       

     # Pour chacun des fichiers en entrée 
    for data_filename in sorted(os.listdir(input_dir)):
        # importer la liste des nombres
        data_file = open(os.path.join(input_dir, data_filename), "r")
        numbers = [int(line) for line in data_file.readlines()]        
        
        # decomposition en facteurs premiers
        D = factorize(numbers)

        # fichier des reponses depose dans le output_dir
        output_filename = 'answer_{}'.format(data_filename)             
        output_file = open(os.path.join(output_dir, output_filename), 'w')
        
        # ecriture des resultats
        for (n, primes) in D.items():
            output_file.write('{} {}\n'.format(n, primes))
        
        output_file.close()

    
