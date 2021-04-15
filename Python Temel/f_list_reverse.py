"""
Verilen listenin elemanlarını tersine döndüren fonksiyon.
Listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürür.
"""

def f_list_reverse(liste):
    liste1 =[]
    for i in liste:
        if(type(i) == list):
            liste1.append(f_list_reverse(i))
        else:
            liste1.append(i)
    return list(reversed(liste1))

liste = [[1,2], [3, 4], [5, 6, 7]]
liste2 = list(f_list_reverse(liste))
print(liste2)