
with open('C:/Новый текстовый документ.txt', 'r+') as f:
    k = 0
    schetchik = 0
    for i1 in f:
        schetchik += 1
        print(len(i1))
    print(schetchik)
