import random

dane = []
def rosnace(y,tab):
    for i in range(y):
        tab.append(i)


def malejace(y,tab):
    for i in range(y-1,-1,-1):
        tab.append(i)


def stale(y,tab):
    for _ in range(y):
        tab.append(1)

def akszt(y,tab):
    for i in range(int(y/2)):
        tab.append(i)
    for i in range(int(y/2),-1,-1):
        tab.append(i)


def losowe(y,tab):
    for _ in range(y):
        tab.append(random.randint(0, y))


def selection_sort(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1,len(tab)):
            if tab[j]<tab[min]:
                min = j
        tab[i],tab[min] = tab[min],tab[i]
        


def insertion_sort(tab):
    for i in range(len(tab)-1):
        key = tab[i+1]
        j = i
        while j>=0 and key<tab[j]:
            tab[j+1]=tab[j]
            j-=1
        tab[j+1] = key

def shell_sort(tab):
    pass

def podzial(tab,i, j):
    x = tab[i]
    start = i

    while True:
        while i <= j and tab[i] <= x:
                i += 1
        while i <= j and tab[j] >= x:
                j -= 1
        if i <= j:
            tab[i], tab[j] = tab[j], tab[i]
        else:
            break

    tab[start], tab[j] = tab[j], tab[start]

    print(*tab)

    return j

def quick_sort(tab, start, end):
    if len(tab) == 1:
        return 

    if start < end:
        p = podzial(tab, start, end)
        quick_sort(tab, start, p-1)
        quick_sort(tab, p+1, end)

def kopcowanie(tab, n, i):
    korzen = i
    lewa = 2*i+1
    prawa = 2*i+2

    if lewa<n and tab[korzen] < tab[lewa]:
        korzen = lewa

    if prawa<n and tab[korzen] < tab[prawa]:
        korzen = prawa

    if korzen != i:
        tab[i], tab[korzen] = tab[korzen], tab[i]
        kopcowanie(tab, n, korzen)

def heap_sort(tab):
    for i in range(len(dane) // 2, -1, -1):
        kopcowanie(dane, len(tab), i)

    for i in range(len(tab)-1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        kopcowanie(tab, i, 0)
        


while True:
    print("Wybierz, ktore dane chcesz przetestowac oraz ich ilosc")
    print("1 - rosnace\n2 - malejace\n3 - stale\n4 - A ksztaltne\n5 - losowe")
    line = input().split()
    if len(line) == 2 and line[0].isnumeric() and line[1].isnumeric():
        x = int(line[0])
        y = int(line[1])
        break
    

if x==1:
    rosnace(y,dane)
elif x==2:
    malejace(y,dane)
elif x==3:
    stale(y,dane)
elif x==4:
    akszt(y,dane)
elif x==5:
    losowe(y,dane)

print(*dane)

while True:
    print("Podaj algorytm")
    print("1 - selection sort\n2 - insertion sort\n3 - shell sort\n4 - heap sort\n5 - quick sort")
    alg = input()
    if alg.isnumeric():
        alg = int(alg)
        break

if alg==1:
    selection_sort(dane)
elif alg==2:
    insertion_sort(dane)
elif alg==3:
    shell_sort(dane)
elif alg==4:
    heap_sort(dane)
elif alg==5:
    quick_sort(dane, 0, len(dane)-1)
print(*dane)