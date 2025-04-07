#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Diffie-Hellman Key Exchange

import math
import random
from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime
import time

def easy_form(num):
    # This function checks whether p is of the form 2q+1.
    q = (num - 1) / 2

    if q % int(q) == 0:
        is_int = True
    else:
        is_int = False
    
    return is_int

def generator(num, zp):
    # This function finds all factors of p-1 and checks each factor whether its a generator.
    check = easy_form(num)
    
    if check:
        factors = []
        generators = []
        p_minus_one = num - 1

        for i in range(1, p_minus_one+1):
            if p_minus_one % i == 0:
                factors.append(i)
            else:
                continue

        #print("\nFactors of p-1 are:", factors)

        for i in zp:
            # Excluding factors 1 and p-1. 
            # For factor of 1, k = p-1, and every value raised to the Euler's totient (p-1) is equal to 1, so trivial.
            # For factor of p-1, k = 1, and every value except for 1 does not equal 1, so trivial, again.
            # All factors must be g_check == True for it to be a generator.
            for j in factors[1:len(factors)-1]:
                k = int(p_minus_one / j)
                g_check = pow(i, k, num) != 1
                
                if g_check == False:
                    break

            if g_check:
                generators.append(i)
            else:
                continue

        return generators
        
    else:
        print("\nModulus is not of the form 2q+1.")
        return None

def generate_keys(p: int, g: int, private_key=0):
    # Initializing p-2 boundary.
    bound = p - 2

    if private_key == 0:
        # Radnomly choosing an integer betwen 1 <= A <= bound for private key.
        private_key = random.randint(1, bound)
    
    # Calculating public key y = g^x (mod p)
    public_key = pow(g, private_key, p)

    # Organizing the private key and public key into a tuple.
    keys = (private_key, public_key)
    
    return keys

def main():
    # This is the main function.
    try:
        # Enter input if available. If not, generate random values for running program.
        p = int(input("Enter prime number p (enter 0 if none): "))
        g = int(input("Enter generator value g (enter 0 if none): "))

        if p == 0 or g == 0:
            print("\nInsufficient custom values entered.. Generating values...\n")
            
            # Generate a prime number.
            p = getPrime(16)
            print("Prime number is set as:", p)
            
            # Find the Zp (integers mod p that are relatively prime to p).
            Zp = (i for i in range(1, p))
        
            # Assign a generator from Zp (integers mod p that are relatively prime to p).
            # A generator is aka primitive root.
            g = generator(p, Zp)
            g = random.choice(g)
            print("Generator value is set as:", g)
            print()

        # Alice (sender) chooses a private key, then generates a public key.
        # Inputfield for custom key values. Only enter private key if public key is not provided.
        A_pub = int(input("Enter Alice's public key (enter 0 if none): "))
        
        if A_pub == 0:
            A_priv = int(input("Enter Alice's private key (enter 0 if none): "))

        # If Alice's public key is provided, just use the public key. It will be too hard to figure out the private key.
        # If Alice's public key is not provided but her private key is provided, use the private key to calculate the public key.
        # For anything else, just generate both public and private keys.
        if A_pub != 0:
            A_keys = (0, A_pub)
            print("\nOnly public key provided, Alice's private key will remain unknown.")
        elif A_pub == 0 and A_priv != 0:
            A_keys = generate_keys(p, g, A_priv)
            print("\nOnly private key provided. Alice's public key is calculated from this key.")
        else:
            A_keys = generate_keys(p, g)
            print("\nInsufficient input for Alice's keys. Public and private keys are generated")
            
        print("\nAlice's private key:", A_keys[0])
        print("Alice's public key:", A_keys[1])
        print()

        # Bob (receiver) chooses a private key, then generates a public key.
        # Inputfield for custom key values. Only enter private key if public key is not provided.
        B_pub = int(input("Enter Bob's public key (enter 0 if none): "))
        
        if B_pub == 0:
            B_priv = int(input("Enter Bob's private key (enter 0 if none): "))
        
        # If Alice's public key is provided, just use the public key. It will be too hard to figure out the private key.
        # If Alice's public key is not provided but her private key is provided, use the private key to calculate the public key.
        # For anything else, just generate both public and private keys.
        if B_pub != 0:
            B_keys = (0, B_pub)
            print("\nOnly public key provided, Bob's private key will remain unknown.")
        elif B_pub == 0 and B_priv != 0:
            B_keys = generate_keys(p, g, B_priv)
            print("\nOnly private key provided. Bob's public key is calculated from this key.")
        else:
            B_keys = generate_keys(p, g)
            print("\nInsufficient input for Bob's keys. Public and private keys are generated")
        
        print("\nBob's private key:", B_keys[0])
        print("Bob's public key:", B_keys[1])
        print()
    
        # Generate shared key.
        # If one of Alice or Bob does not have a private key, use the one who has the private key. If both do not have private keys, no shared key will be available.
        if A_keys[0] == 0 and B_keys[0] == 0:
            shared_key = 0
        elif A_keys[0] != 0 and B_keys[0] == 0:
            shared_key = pow(B_keys[1], A_keys[0], p)
        elif A_keys[0] == 0 and B_keys[0] != 0:
            shared_key = pow(A_keys[1], B_keys[0], p)
        else:
            shared_key = pow(g, A_keys[0] * B_keys[0], p)
        
        print("Shared Key:", shared_key)
        print()

        if A_keys[0] != 0 and A_keys[1] != 0 and B_keys[0] != 0 and B_keys[1] != 0:
            # Checking whether shared key is correct.
            double_check = pow(A_keys[1], B_keys[0], p) == pow(B_keys[1], A_keys[0], p)
            print("Shared key calculation validation:", double_check)
        else:
            pass

    except ValueError:
        print("\nInvalid input. Please try again.\n")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




