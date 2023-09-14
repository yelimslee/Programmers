P, K = map(int, input().split())
           
if P >= K:
    print(P-K+1)
else:
    print(K-P+1+999)