
def tax(states, income):
    net_income = 0
    federal_tax = 0.1 * income
    if states == 'nyc':
        state_tax = 0.11 * income
        net_income = income - (federal_tax + state_tax)
    if states == 'la':
        state_tax = 0.5 * income
        net_income = income - (federal_tax + state_tax)
    if states == 'boston':
        state_tax = 0.15 * income
        net_income = income - (federal_tax + state_tax)
    return net_income

x = tax('nyc', 1000)

print(x)