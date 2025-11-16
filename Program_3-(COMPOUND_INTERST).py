"""
P = PRINCIPAL
R = RATE
T = TIME
A = AMOUNT
Amount = P ( 1 + R / 100) ** T (POWER OF T)
COMPOUND INTEREST = A - P
"""


principal = float(input("Please enter your Principal Amount:-  "))
rate = float(input("Please enter your Intrest Rate:- "))
time = float(input("Please enter your Given Time (In Years):- "))

amount1 = principal * ( 1 + rate / 100) ** time
amount2 = principal * pow((1 + rate / 100), time)
print (amount1, amount2, round(4))

compound_interest1 = amount1 - principal
compound_interest2 = amount2 - principal
print ("Your Compound Interest is", compound_interest1, "\n", compound_interest2, round(4))
# print ("Your Compound Interest is", round(compound_interest1, 4), "\n", round(compound_interest2, 4)) # We can write as this also