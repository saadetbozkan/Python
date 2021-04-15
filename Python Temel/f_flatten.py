"""
Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabilen ya da 
non-scalar verilerden de oluşabilen bir listeyi düzleştiren (flatten) fonksiyon. 
"""
def f_flatten(liste):
    liste1 = []
    
    for i in liste:
        if(type(i) == list):
            for j in f_flatten(i):
                liste1.append(j)
        else:
            liste1.append(i)
    return liste1

listt = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(f_flatten(listt))