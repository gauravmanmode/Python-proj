def main():
    print(boyermoore("hello" ,"lo"))

def boyermoore(T,P):
    n,m=len(T),len(P)
    last = {}
    if m==0: return 0
#define func last(c)
    for k in range(0,m):
        last[P[k]] = k
    i=m-1
    k=m-1
    while i<n:
        if T[i]==P[k]:
            if k==0:
                return i
            else:
                i-=1
                k-=1
        else:
            j = last.get(T[i],-1)
            i+=m - min(j+1, k)
            k = m-1
    return -1

if __name__== "__main__":
    main()


