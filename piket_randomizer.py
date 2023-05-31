from daftar_nama.name_splitter import r_rabu,r_jumat
def acak(members):
    i = 1
    x = 0
    y = -1
    #global b
    #global loc
    loc = None
    b = list(members.items())
    while i < len(members):
        old = b[x]
        new = b[y]
        b[x] = new
        b[y] = old
        x += 1
        y -= -1
        i += 1
    if members == r_rabu:
        loc = 'nama_rabu.txt'
    elif members == r_jumat:
        loc = 'nama_jumat.txt'
    def nama_new(dictio,loc):
        with open(f'daftar_nama/{loc}','w') as w_nama:
            x = [i for i in dict(b).keys()]
            x2 = [i for i in dict(b).values()]
            k = 0
            for i in x:
                w_nama.writelines(i + ":" + x2[k] + '\n')
                k += 1
    nama_new(dict(b),loc)
    return dict(b)
#WATTAFAK THE SOLUTION:
# r_rabu = acak(r_rabu)
# print(r_rabu)

# r_rabu = acak(r_rabu)
# print(r_rabu)