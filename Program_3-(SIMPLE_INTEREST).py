"""
Simple Interest = (P * R * T) / 100
P = Principal Amount
R = Rate Of Interest
T = Time Duration
"""

principal = float(input("Please enter your Principal Amount:- "))
rate = float(input("Please enter your Intrest Rate:- "))
time = float(input("Please enter your Given Time (In Years):- "))

principal_amount = (principal * rate * time) / 100777

print ("your Simple Interest is", principal_amount)