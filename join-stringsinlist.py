# -*- coding: utf-8 -*-

# Oncelikle recursion fonksiyon kullandığımızda sorun çıkmaması için global bir bir birleşim değişkeni kullanmalıyız.

birlesim = ""

def birlestir(liste):
    global birlesim
    for i in liste:
        if isinstance(i,list): # her elemanının liste olup olmadığını kontrol ediyoruz
            return birlestir(i) # listeyse fonksiyona tekrar gönderiyoruz
        else:
            birlesim=birlesim+i+" " # artık liste değilse birlesim adlı biriktiricimize ekliyoruz.
    return birlesim

liste = ["ahmet","mehmet",["ali","hasan",["can",["cenk"]]],"salih"] 

print(birlestir(liste))
