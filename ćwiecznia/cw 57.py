# n!= n*(n-1)*(n-2)...
def sil(n):
    result = 1
    while(n>1):
        result *= n # result = result*n
        n-=1        # n=n-1
    return result


n=5
print("%d!=%d" %(n,sil(n)))



def factorialRec(n):
    if(n==2):
        return n
    return n* factorialRec(n-1);

n = 5
print("%d!=%d" % (n, factorialRec(n)))

