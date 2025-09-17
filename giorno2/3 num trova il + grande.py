a = int(input("inserisci il primo numero: "))
b = int(input("inserisci il secondo numero: "))
c = int(input("inserisci il terzo numero: "))

if a >= b and a >= c:
    print("il numero più grande è: ", a)
elif b >= a and b >= c:
    print("il numero più grande è: ", b)
else: 
    print("il numero più grande è: ", c)