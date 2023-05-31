r_rabu = {1: "anista", 2: "dito", 3: "el", 4: "fajar", 5: "febriansyah", 6: "fernando", 7: "ridwan", 8: "zidan", 9: "fadhil"}

rabu_sudah = []
denda_rabu = []
while True:
    konfir = int(input("Yang sudah piket: "))
    if konfir == 0:
        break;
    if r_rabu.get(konfir) != None:
        rabu_sudah.append(r_rabu.get(konfir))
    else:
        print("Absen salah!!")
print(rabu_sudah)
for i in r_rabu.values():
    if not i in rabu_sudah:
        denda_rabu.append(i)
total_denda_rabu = 20000 * len(denda_rabu)
print(denda_rabu)
print("Total denda: " + str(total_denda_rabu))
