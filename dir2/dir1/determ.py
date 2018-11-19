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