#!/usr/bin/env python3
import random

def main():
    taille=random.randint(1,20)
    liste=[0]*taille
    somme=0
    maxi=liste[0]
    mini=liste[0]
    occurence=0
    sous=[]
    for i in range(taille):
        liste[i]=random.randint(0,100)
    liste.append(-1)
    print("la liste est :",liste)
    for i in range(len(liste)):
        somme+=liste[i]
    somme=somme/taille+1


    for i in liste:
        if i>=maxi:
            maxi=i
        if i<=mini:
            mini=i
        if i==liste[0]:
            occurence+=1
    for i in range(len(liste)-1):
        if liste[i]<=liste[i+1]:

            liste[i]=liste[i].append(liste[i+1])
        else:
            liste[i]=[liste[i]]
    print(liste)
    print(f"le maximum est {maxi} et le minimum est {mini} ")    
    print(f"la moyenne des entiers positifs est de {somme}, le nombre {liste[0]} apparait {occurence} fois")

if __name__=="__main__":
    main() 
