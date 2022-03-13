import random

dane = []
def rosnace(y,dane):
    for i in range(y):
        dane.append(i)


def malejace(y,dane):
    for i in range(y-1,-1,-1):
        dane.append(i)


def stale(y,dane):
    for i in range(y):
        dane.append(1)

def akszt(y,dane):
    for i in range(int(y/2)):
        dane.append(i)
    for i in range(int(y/2),-1,-1):
        dane.append(i)


def losowe(y,dane):
    for i in range(y):
        dane.append(random.randint(0, y))


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



print("Wybierz, ktore dane chcesz przetestowac oraz ich ilosc")
print("1 - rosnace\n2 - malejace\n3 - stale\n4 - A ksztaltne\n5 - losowe")
line = input().split()
x = int(line[0])
y = int(line[1])

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

print("Podaj algorytm")
print("1 - selection sort\n2 - insertion sort\n3 - shell sort\n4 - hip sort\n5 - quick sort")
alg = int(input())

if alg==1:
    selection_sort(dane)
if alg==2:
    insertion_sort(dane)
print(*dane)