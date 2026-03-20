# Fuzzy Logic System for Credit Risk Assessment

# trinagular and trapezoidal membership functions
# it takes the value of x and the parameters of the function and returns the degree of membership for that value
def triangular(x,a,b,c):
    if x<= a or x >= c:
        return 0
    elif a < x < b:
        return (x-a) / (b-a)
    elif b <= x < c:
        return (c-x) / (c-b)
    else:
        return 0
def trapezoidal(x, a, b, c, d):
    if x <= a or x >= d:
        return 0
    elif a < x < b:
        return (x - a) / (b - a) if b != a else 1
    elif b <= x <= c:
        return 1
    elif c < x < d:
        return (d - x) / (d - c) if d != c else 1
    else:
        return 0

# Fuzzification: it takes the credit score and returns the degree of membership for each risk category
def fuzzification(credit):
    return {
        'high_risk': trapezoidal(credit, 0, 0, 280, 400),
        'med_risk': triangular(credit, 280, 400, 620),
        'low_risk': trapezoidal(credit, 400, 620, 800, 800)
    }

# Inference: it takes the degree of membership for each risk category and applies the rules to determine the degree of membership for each credit category
def ap_rules(fuzzy_var):
    rules = {
        'low_credit': fuzzy_var['high_risk'],
        'med_credit': fuzzy_var['med_risk'],
        'high_credit': fuzzy_var['low_risk']
    }
    return rules

# credit categories membership functions
def low_credits(x):
    return trapezoidal(x, 0, 0, 35, 50)

def med_credits(x):
    return triangular(x, 35, 50, 77.5)

def high_credits(x):
    return trapezoidal(x, 50, 77.5, 100, 100)

# Defuzzification: it takes the degree of membership for each credit category and returns a crisp value for the credit score
def deffuzification(rules):
    denominator = 0
    numerator = 0

    for x in range(0, 1010):
        x = x / 10
        mu_low = min(rules['low_credit'], low_credits(x))
        mu_med = min(rules['med_credit'], med_credits(x))
        mu_high = min(rules['high_credit'], high_credits(x))

        agregation = max(mu_low, mu_med, mu_high)

        numerator += x * agregation
        denominator += agregation

    if denominator == 0:
        return 0
    return numerator / denominator

client_credit = 700
fuzzy_credit = fuzzification(client_credit)
rules = ap_rules(fuzzy_credit)
client_risk = deffuzification(rules)
client_risk = 100 - client_risk

# Output the results
print(f'Client credits: {client_credit}')
print('\n ',rules)
print(f'  {fuzzy_credit}')
print(f'\nClient risk: {client_risk}%')
