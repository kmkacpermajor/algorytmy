import random
import time

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
    for i in range(1, len(tab)):     #  iterujemy od lewej do prawej po tablicy:
        key = tab[i]                        # bierzemy pierwszy nieuporządkowany element tablicy
        j = i                               # iterujemy od tego elementu
        while j>=0 and key<tab[j-1]:            # szukamy pierwszego mniejszego elementu
            tab[j]=tab[j-1]                     # 
            j-=1                                # przesuwamy kolejno większe elementy w prawo
        tab[j] = key                        # ustawiamy mniejszy element po prawej od elementu i

def shell_sort(tab):
    h = len(tab) // 2   # przyjmujemy skok (zgodnie z metodą Shella)
    while h > 0:
        for i in range(h, len(tab)):
            key = tab[i]    # bierzemy pierwszy nieuporządkowany element (pod)tablicy
            j = i           # iterujemy od tego elementu
            while j >= h and key<tab[j - h]:  # szukamy pierwszego mniejszego elementu
                tab[j] = tab[j - h]           # 
                j -= h                        # przesuwamy kolejno większe elementy w prawo
            tab[j] = key    # ustawiamy mniejszy element po prawej od elementu i
        h = h // 2      # zmniejszamy skok (zgodnie z metodą Shella)

def podzial(tab,i, j, wybor):

    if wybor == "los":
        r = random.randint(i,j)
        tab[r], tab[i] = tab[i], tab[r]

    ind_pivot = i

    pivot = tab[ind_pivot] # wybieramy pivot

    while True:
        while i <= j and tab[i] <= pivot:       # szukamy indeks pierwszego większego elementu od lewej
                i += 1
        while i <= j and tab[j] >= pivot:       # szukamy indeks pierwszego mniejszego elementu od prawej
                j -= 1
        if i <= j:
            tab[i], tab[j] = tab[j], tab[i] # zamieniamy elementy póki pointery się nie zamienią miejscami
        else:
            break                           # jeśli tak się stanie to wychodzę z pętli

    tab[ind_pivot], tab[j] = tab[j], tab[ind_pivot]         # zamieniamy pivot z elementem na drugim pointerze (jeśli nie zrobimy tego, miejsce pivota zostanie bez zmian)

    return j                                # zwracamy drugi pointer (aktualne miejsce pivota)

def quick_sort(tab, start, end, wybor=""):
    if len(tab) == 1:
        return 

    if start < end:
        p = podzial(tab, start, end, wybor)    # szukamy indeksu rozdzielającego tablice (po lewej mniejsze od pivota, po prawej większe)
        quick_sort(tab, start, p-1, wybor)     # 
        quick_sort(tab, p+1, end, wybor)       # dzielimy tablicę na pół i sortujemy podtablice
        

def kopcowanie(tab, n, i):
    korzen = i
    lewa = 2*i+1
    prawa = 2*i+2

    if lewa<n and tab[korzen] < tab[lewa]: # sprawdzamy czy jest dziecko i czy lewe dziecko jest większe od rodzica
        korzen = lewa                           # zmieniamy korzeń na lewe dziecko

    if prawa<n and tab[korzen] < tab[prawa]: # sprawdzamy czy jest dziecko i czy prawe dziecko jest większe od rodzica
        korzen = prawa                          # zmieniamy korzeń na prawe dziecko

    if korzen != i:                          # sprawdzamy czy zaszły zmiany
        tab[i], tab[korzen] = tab[korzen], tab[i] # swap
        kopcowanie(tab, n, korzen)                # podajemy kolejny korzeń

def heap_sort(tab):
    for i in range(len(tab) // 2, -1, -1): # tworzymy kopiec tylko od korzeni
        kopcowanie(tab, len(tab), i)            # kopcujemy dla całej tablicy

    for i in range(len(tab)-1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0] # podmieniamy korzeń z i-tym elementem
        kopcowanie(tab, i, 0)           # powtarzamy kopcowanie dla korzenia i podajemy tablicę i-elementową (nie całą)
        


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
    print("1 - selection sort\n2 - insertion sort\n3 - shell sort\n4 - heap sort\n5 - quick sort (pierwszy)\n6 - quick sort (losowy)")
    alg = input()
    if alg.isnumeric():
        alg = int(alg)
        break

dane = [8,10,6,8,0,1,0,2,6,0]

pocz = time.time()

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
elif alg==6:
    quick_sort(dane, 0, len(dane)-1, "los")

kon = time.time()

print(*dane)

print("Kod wykonywał się {} s".format(kon-pocz))
