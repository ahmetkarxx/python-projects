#-*- coding:utf-8 -*-

"""
@Author: Ahmet Kar
-For döngüsü ve listeler yardımıyla fibonacci dizisi oluşturmak
"""

#Dizinin boyutunu alalım
h = int(input("Yüksekliği girin :"))


fibonacci = []

#Diziye sayı ekleyeceğimiz alanları sıfırla dolduralım
#index out of range hatasından kurtulmak için
for k in range(h+1):
    fibonacci.insert(k,[])
    for n in range(k+1):
        fibonacci[k].insert(n,0)

#Dizi oluşturma işlemleri
for i in range(h+1):
    if i==0:
        #İlk satırımıza bir tane 1 var
        fibonacci[i][0] =1
    if i>0:
        #İlk satırdan sonra hepsinin ilk ve son satırı 1 olacak
        fibonacci[i][0] = 1
        fibonacci[i][len(fibonacci[i])-1] = 1
    if i>=2:
        #For döngüsü yardımıyla her satırda 1 den i ye
        #yani o anki satırımızın sayısına kadar sutun oluşturduk
        #sonra birönceki satırımızdaki sayıları toplayıp o anki satırımız ve sutunumuzun değerine eşitledik.
        for j in range(1,i):
            #i.satırdaki ve j.sutundaki sayı bizim toplamı yazacağımız sayı
            #i-1 bir önceki satır j-1 bir önceki satırdaki bir önceki sutundaki eleman j ise bir önceki satırdaki
            #j sutunundaki eleman
            fibonacci[i][j] = fibonacci[i-1][j-1]+fibonacci[i-1][j]

#Ekrana yazdırma işlemleri
for n in range(len(fibonacci)):
    #Boşluk oluşturma
    for c in range(h-n):
        print(" ",end="")
    #Diziyi yazdırma
    for k in range(n+1):
        print(fibonacci[n][k],end=" ")
    print()
