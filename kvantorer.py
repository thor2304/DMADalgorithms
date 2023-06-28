#A
def for_all(elements, predicate):
    for element in elements:
        if not predicate(element):
            return False
    return True
#E
def exists(elements, predicate):
    for element in elements:
        if predicate(element):
            return True
    return False

#Negering
def negate(predicate):
    return lambda x: not predicate(x)

############## A ##################
# Eksempel: Alle heltal
# Genererer alle heltal fra -10 til 10 ved hjælp af range-funktionen.
# Evaluerer, om alle elementer er større end nul ved hjælp af for_all-funktionen og en lambda-funktion som prædikat.
all_integers = range(-10, 11)
all_greater_than_zero = for_all(all_integers, lambda x: x > 0)
print("Alle elementer er større end nul:", all_greater_than_zero)

# Eksempel: Alle positive heltal
# Genererer alle positive heltal fra 1 til 10 ved hjælp af range-funktionen.
# Evaluerer, om alle elementer er lige tal ved hjælp af for_all-funktionen og en lambda-funktion som prædikat.
all_positive_integers = range(1, 11)
all_even_numbers = for_all(all_positive_integers, lambda x: x % 2 == 0)
print("Alle elementer er lige tal:", all_even_numbers)

############## E ##################
# Eksempel: Alle negative heltal
# Genererer alle negative heltal fra -10 til -1 ved hjælp af range-funktionen.
# Evaluerer, om der eksisterer et negativt tal ved hjælp af exists-funktionen og en lambda-funktion som prædikat.
all_negative_integers = range(-10, 10)
exists_negative_numbers = exists(all_negative_integers, lambda x: x < 0)
print("Der eksisterer et negativt tal:", exists_negative_numbers)

# Eksempel: Alle heltal fra 0 og op
# Genererer alle ikke-negative heltal fra 0 til 10 ved hjælp af range-funktionen.
# Evaluerer, om der eksisterer et ulige tal ved hjælp af exists-funktionen og en lambda-funktion som prædikat.
all_non_negative_integers = range(0, 11)
exists_odd_numbers = exists(all_non_negative_integers, lambda x: x % 2 != 0)
print("Der eksisterer et ulige tal:", exists_odd_numbers)

############## Begge både E og A ##################
# Eksempel: For alle x eksisterer et y, så y er større end x
# Genererer værdier for x fra 1 til 5 ved hjælp af range-funktionen.
# Evaluerer, om forudsætningen "for alle x" er opfyldt, hvor der eksisterer et y større end x, ved hjælp af for_all- og exists-funktionerne og en lambda-funktion som prædikat.
for_all_exists = for_all(range(1, 6), lambda x: exists(range(0, 16), lambda y: y > x))
print("For alle x eksisterer et y, så y er større end x:", for_all_exists)

# Eksempel: Der eksisterer et x for alle y
# Genererer værdier for y fra 1 til 5 ved hjælp af range-funktionen.
# Evaluerer, om forudsætningen "der eksisterer et x" er opfyldt for alle y-værdierne ved hjælp af exists- og for_all-funktionerne og en lambda-funktion som prædikat.
exists_for_all1 = for_all(range(1, 6), lambda y: exists(range(1, 6), lambda x: x == y))
print("Der eksisterer et x for alle y:", exists_for_all1)

########## negering #######################

# Eksempel: Negering af et prædikat
# Genererer alle heltal fra -10 til 10 ved hjælp af range-funktionen.
# Evaluerer, om der eksisterer et ikke-negativt tal ved at negere prædikatet "x < 0" ved hjælp af negate-funktionen.
all_integers = range(-10, 11)
exists_non_negative = exists(all_integers, negate(lambda x: x < 0))
print("Der eksisterer et ikke-negativt tal:", exists_non_negative)

# Eksempel: Negering af en kvantorerklæring
# Genererer alle heltal fra -10 til 10 ved hjælp af range-funktionen.
# Evaluerer, om der ikke eksisterer et ulige tal ved at negere kvantorerklæringen "for alle x, x % 2 != 0".
all_integers = range(-10, 11)
not_all_odd = not for_all(all_integers, lambda x: x % 2 != 0)
print("Ikke alle tal er ulige:", not_all_odd)

########## negering både A og E #######################
# Eksempel: Der eksisterer ikke et x for alle y, hvor x^2 = u
# Genererer værdier for u fra 1 til 10 ved hjælp af range-funktionen.
# Evaluerer, om der ikke eksisterer et x for alle y, hvor x^2 = u, ved at negere kvantorerklæringen "for alle y, eksisterer et x, så x^2 = u".
exists_not_for_all = exists(range(1, 11), lambda u: not for_all(range(1, 11), lambda y: exists(range(1, 11), lambda x: x**2 == u)))
# print("Der eksisterer ikke et x for alle y, hvor x^2 = u:", exists_not_for_all)
print("Der eksisterer et u hvor hvor der findes et x^2 = u for alle y:", exists_not_for_all)
## Note the here the y makes no sense, it has no effect on the outcome of the existance check
print()

# Der eksisterer ikke et a for hvilket det gælder for alle b at a^2 = b
print(f"Der eksisterer ikke et a for hvilket det gælder for alle b at a^2 = b: "
      f"{not exists(range(-80, 80), lambda a: for_all(range(-80**2, 81**2), lambda b: a**2 == b))}")

# Der eksisterer et a for hvilket det gælder for alle b at a^2 != b
print(f"Der eksisterer et a for hvilket det gælder for alle b at a^2 != b: "
      f"{exists(range(-80, 80), lambda a: for_all(range(-80**2, 81**2), lambda b: a**2 != b))}")

print()

#### nye ###
not_exists_for_all2 = not exists(range(-80, 80), lambda b: for_all(range(-80, 80), lambda a: a**2 == b))
# print("Der eksisterer ikke et a for alle b, hvor a^2 = b:", not_exists_for_all2)

# Eksempel: Der eksisterer et a for alle b, hvor a^2 != b
# Genererer værdier for b fra -80 til 80 ved hjælp af range-funktionen.
# Evaluerer, om der eksisterer et a for alle b, hvor a^2 != b, ved at negere kvantorerklæringen "for alle b, eksisterer et a, så a^2 != b".
exists_for_all2 = exists(range(-80, 80), lambda b: not for_all(range(-80, 80), lambda a: a**2 != b))
# print("Der eksisterer et a for alle b, hvor a^2 != b:", exists_for_all2)