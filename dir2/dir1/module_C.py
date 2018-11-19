# def funC(n):
#     for i in range(n):
#         x=(-1) **i
#         yield x
# n=5
# nex=funC(n)
# for j in range(n):
#     print(next(nex))

if __name__=='__main__':
    print('Это исполняемый файл')

def funC(n):
    for i in range(n):
        x=(-1) **i
        yield x
n=5
nex=funC(n)
L=[]
for j in range(n):
    L.append(next(nex))

print(L)
