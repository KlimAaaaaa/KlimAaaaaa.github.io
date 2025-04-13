

def rabbit_pairs_recursive(n, k):
    
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    return rabbit_pairs_recursive(n - 1, k) + k * rabbit_pairs_recursive(n - 2, k)

n, k = 5, 3
r = rabbit_pairs_recursive(n, k)




def rabbit_pairs(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    F1, F2 = 1, 1
    
    for i in range(3, n + 1):
        Fn = F2 + k * F1
        F1, F2 = F2, Fn
    
    return F2

n, k = 5, 3
с = rabbit_pairs(n, k)
