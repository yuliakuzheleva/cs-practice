p = float(input('Введите порог в градусах Цельсиях: '))
n = int(input('Введите количество показаний: '))
c = 0
cind = 0
mx = -1000000000000
sum = 0
er = 0
for i in range(n):
    indications = input()
    if indications == 'error':
        er += 1
    else:
        indications = float(indications)
        c += 1 
        sum += indications
        if indications > p:
            cind+=1
        if indications > mx:
            mx = indications
print(n, er, cind, f'{mx:.1f}', f'{sum/c:.1f}')
    
        

