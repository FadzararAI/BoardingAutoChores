r_rabu = {}
r_jumat = {}
# nama_rabu = {}
# nama_jumat = {}
with open('daftar_nama/nama_rabu.txt','r') as r_nama:
    for lines in r_nama:
        line = lines.strip("\n").split(":")
        r_rabu[line[0]] = line[1]
with open('daftar_nama/nama_jumat.txt','r') as r_nama:
    for lines in r_nama:
        line = lines.strip("\n").split(":")
        r_jumat[line[0]] = line[1]
# with open('daftar_nama/nama_jumatOri.txt','r') as r_nama:
#     for lines in r_nama:
#         line = lines.strip("\n").split(":")
#         nama_jumat[line[0]] = line[1]
# with open('daftar_nama/nama_rabuOri.txt','r') as r_nama:
#     for lines in r_nama:
#         line = lines.strip("\n").split(":")
#         nama_rabu[line[0]] = line[1]
