import sys, os
import numpy as np

pri = [2]
MX = int(1e6)
isprime = [True] * MX

def primelist(n):
    global MX
    if pri[-1] > n:
        return
    for i in range(pri[-1], min(int(np.sqrt(n)),MX)):
        if isprime[i]:
            pri.append(i)
            for j in range(i + i, MX, i):
                isprime[j] = False
    return


def factorization(n):
    global pri
    ret = []
    for i in pri:
        if i * i > n:
            break
        while n % i == 0:
            ret.append(i)
            n //= i
    if pri[-1]**2 < n:
        for i in range(pri[-1], int(np.sqrt(n)), 2):
            while n % i == 0:
                ret.append(i)
                n //= i
    if n != 1:
        ret.append(n)
    return ret


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
        primelist(n)
        result[n] = factorization(n)
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

Sol 2 : miller rabin primality test + pollard's rho algorithm
    Not allowed in this exercice.
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

    
