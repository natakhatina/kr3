# ОПРЕДЕЛИТЕЛЬ МАТРИЦЫ:
import copy

L=[[1,2,3,4],
   [4,5,6,7],
   [7,8,9,8],
   [1,2,3,4]]

# L=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]

# L=[[1,2],
#    [3,4]]

n=len(L) # кол-во строк и соотв-но размерность

def foo(A):
    d2=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return d2

def Hallo(M):
    d3=0
    for i in range (0,3):
        A = copy.deepcopy(M)
        A.pop(0)
        for j in range (0,2):
            A[j].pop(i)
        d2=foo(A)
        d3=d3+(-1)**i*M[0][i]*d2
    return d3

def Goodbuy (L):
    d4=0
    for i in range (0,4):
        M=copy.deepcopy(L)
        M.pop(0)
        for j in range (0,3):
            M[j].pop(i)
        d3 = Hallo(M)
        d4 = d4+(-1)**i*L[0][i]*d3
    return d4

if n==2:
    d=foo(L)
elif n==3:
    d=Hallo(L)
elif n==4:
    d=Goodbuy(L)

print('det =',d)

def Final(n):
    if n == 2:
        d = foo(L)
        print('det =', d)
    elif n == 3:
        d = Hallo(L)
        print('det =', d)
    elif n == 4:
        d = Goodbuy(L)
        print('det =', d)