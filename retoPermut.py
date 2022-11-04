import itertools 
x = 1
y = 1
z = 2
n = 3

i=[]
j=[]
k=[] 
for num in range (x,-1,-1):
    i.append(num)
for num in range (y,-1,-1):
    j.append(num)
for num in range (z,-1,-1):
    k.append(num)

perI= list(itertools.combinations(i,1))

perJ= list(itertools.combinations(j,1))

perK= set(itertools.combinations(k,1))




for val in perI:
    print(val)
#     if val[0]+val[1]+val[2]!=n:
#         print(val)


#CREO QUE YA , REVISAR COMPARANDO RESUTADOS

# for val in perI:
#     print(val)