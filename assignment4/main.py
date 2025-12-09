#1)ATM
def bill(n,denomination = [2000,500,200,100,50],i = 0,result = None):
    if result is None:
        result = {}
    if i == len(denomination):
        return result
    result[denomination[i]] = n // denomination[i]
    n = n % denomination[i]
    
    return bill(n,denomination,i + 1,result)

#2)discounts
def dis(n):
    if n == 500:
        return 10
    return dis(n-500) + 5

#3)library day count
def fine(days):
    if days == 0:
        return 0
    
    if days <= 5:
        cost = 2
    elif days <= 10:
        cost = 5
    else:
        cost = 10
    
    return cost + fine(days - 1)