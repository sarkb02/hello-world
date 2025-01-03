# Code aus der Übung

projektname = input("Wie heißt du?")
zusatz = " - digital"
print(projektname+zusatz)


k = int(input("Wie viele Tassen Kaffee hattest du?"))
if 3 <= k <=8:
    print("ich hatte", k, "Kaffee. Das passt.")  # = print(f"ich hatte {k} Kaffee.")
elif k <= 2:
    print("Ich hatte noch nicht genug KAffee.")
else:
    print("Das war zu viel! Lass mal nicht.")

n = 1
while n < 8:
    print(f"Kaffekonsum {n} ist akzeptabel")
    n = n + 1

else:
    print("Das war zu viel.")

# Zusätzliche Übungen
#1
n = 1
while n <= 100:
  print(n)
  n = n + 1 # n += 1

#2
n = 1
while n <= 100:
    if n % 3 == 0:
        print("Digital")
    else:
        print(n)
    n = n + 1 # n += 1

#3
n = 1
while n <= 100:
    if n % 5 == 0:
        print("History")
    else:
        print(n)
    n = n + 1 # n += 1

#4
n = 1
while n <= 100:
    if n % 5 == 0:
        print("History")
    elif n % 3 == 0:
        print("Digital")
    else:
        print(n)
    n = n + 1 # n += 1

#5
n = 1
while n <= 100:
    if (n % 3 == 0) & (n % 5 == 0):
        print("Digital History")
    elif n % 5 == 0:
        print("History")
    elif n % 3 == 0:
        print("Digital")
    else:
        print(n)
    n = n + 1 # n += 1
