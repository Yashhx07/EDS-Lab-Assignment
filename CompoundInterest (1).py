def compound_interest(p, r, t):
    amount = p * (1 + r/100) ** t
    ci = amount - p
    return amount, ci

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

amount, ci = compound_interest(p, r, t)
print("Total Amount =", amount)
print("Compound Interest =", ci)
