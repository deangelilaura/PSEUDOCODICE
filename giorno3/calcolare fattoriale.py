n = int(input("inserisci un numero: "))
fattoriale = 1 

for i in range(1, n + 1):
    fattoriale *= i 
print("il fattoriale di", n, "è:", fattoriale)