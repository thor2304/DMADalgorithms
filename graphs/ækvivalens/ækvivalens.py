R = [('a','a'),('a','b'),('a','c'),('b','b'),('b','c'),('c','c')]
s = {'a', 'b', 'c'}

# Check refleksivitet
refleksiv = all((x, x) in R for x in s)

# Check symmetri
symmetrisk = all((y, x) in R for (x, y) in R)

# Check antisymmetri
antisymmetrisk = all((y, x) not in R or x == y for (x, y) in R)

# Check transitivitet
transitiv = all((x, z) in R for (x, y) in R for (w, z) in R if y == w)

# Check ækvivalensrelation og partiel ordning
ækvivalensrelation = refleksiv and symmetrisk and transitiv
partiel_ordning = refleksiv and antisymmetrisk and transitiv

print(R)
print(s)
print(f"1) R er refleksiv: {refleksiv}")
print(f"2) R er symmetrisk: {symmetrisk}")
print(f"3) R er antisymmetrisk: {antisymmetrisk}")
print(f"4) R er transitiv: {transitiv}")
print(f"5) R er en ækvivalensrelation: {ækvivalensrelation}")
print(f"6) R er en partiel ordning: {partiel_ordning}")