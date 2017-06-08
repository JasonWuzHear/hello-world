# This will find the number of combinations of ntuples 
# where each element divides the next. Only unique
# combinations are counted. Call answer( [yourlist], ntuple_len )
# to find how many ntuples there are. Useful for counting
# nprimes (primes with n divisors other than 1).
dic = {}
lucky = 0

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def answer(l, dmax):
    global lucky
    lucky = dmax
    global dic
    dic = {}

    count = 0
    for i in range(len(l)):
        if str(l[i]) not in dic:
           dic[str(l[i])] = 0
        dic[str(l[i])] += 1

        try:
            if l[i] == l[i+1]:
                continue
            count += div(l[i], lucky)
        except IndexError:
            count += div(l[i], lucky)

    return count

def div(n, d):
    global dic
    dic[str(n)] -= 1

    if dic[str(n)] < 0:
        dic[str(n)] += 1
        return 0
    elif d == 1:
        dic[str(n)] += 1
        return 1 
    elif str(n) + ',' + str(d) in dic:
        if d == lucky:
            dic[str(n) + ',' + str(d)] *= -1
        else:
            dic[str(n)] += 1
            return dic[str(n) + ',' + str(d)]
    else:
        dic[str(n) + ',' + str(d)] = 0

    sqrt = isqrt(n)
    for i in range(1, sqrt+1):
        if n%i == 0:
            if str(i) in dic:
                dic[str(n) + ',' + str(d)] += div(i, d-1)
            if (i**2 != n) and (str(n//i) in dic):
                dic[str(n) + ',' + str(d)] += div(n//i, d-1)

    dic[str(n)] += 1    
    return dic[str(n) + ',' + str(d)]