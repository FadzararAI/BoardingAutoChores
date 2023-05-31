from datetime import datetime

def isi_pesan(day, names, nama_asli):
	if day == "wed":
		pesan_rabu = f'''
		Jadwal piket rutin untuk Rabu, {datetime.today().day}-{datetime.today().month}-{datetime.today().year}

		Dimohon untuk melaporkan Nama sesuai dengan daftar piket yang sudah ditetapkan dengan memberikan tanda "✅" di sebelah Nama

		Daftar Nama:
		-{nama_asli['1']} 
		-{nama_asli['2']}
		-{nama_asli['3']}
		-{nama_asli['4']}
		-{nama_asli['5']}
		-{nama_asli['6']}
		-{nama_asli['7']}
		-{nama_asli['8']}
		-{nama_asli['9']}


		Jenis Piket:
		1. Sapu Teras dan Bersihkan Halaman: {names[0]}
		2. Sapu + Pel Ruang Depan: {names[1]}
		3. Sapu + Pel Ruang Tengah: {names[2]}
		4. Bersihkan Toilet Depan: {names[3]}
		5. Bersihkan Toilet Belakang: {names[4]}
		6. Sapu, Pel + Rapihkan Dapur 1: {names[5]}
		7. Sapu, Pel + Rapihkan Dapur 2 : {names[6]}
		8. Bersihkan Garasi, Rapihkan Sepatu, Area Wudu + Buang Sampah: {names[7]}
		9. Bersihkan Rooftop Jemuran belakang: {names[8]}


		Note: Akan dikenakan Denda Rp 20.000 bagi yg tidak melaporkan list dalam seminggu hari kerja
		'''
		return pesan_rabu
	elif day == "fri":
		pesan_jumat = f'''
		Jadwal piket rutin untuk Jum'at, {datetime.today().day}-{datetime.today().month}-{datetime.today().year}

		Dimohon untuk melaporkan Nama sesuai dengan daftar piket yang sudah ditetapkan dengan memberikan tanda "✅" di sebelah Nama

		Daftar Nama:
		-{nama_asli['1']} 
		-{nama_asli['2']}
		-{nama_asli['3']}
		-{nama_asli['4']}
		-{nama_asli['5']}
		-{nama_asli['6']}
		-{nama_asli['7']}
		-{nama_asli['8']}
		-{nama_asli['9']}


		Jenis Piket:
		1. Sapu Teras dan Bersihkan Halaman:{names[0]}
		2. Sapu + Pel Ruang Depan: {names[1]}
		3. Sapu + Pel Ruang Tengah: {names[2]}
		4. Bersihkan Toilet Depan: {names[3]}
		5. Bersihkan Toilet Belakang: {names[4]}
		6. Sapu, Pel + Rapihkan Dapur 1: {names[5]}
		7. Sapu, Pel + Rapihkan Dapur 2 : {names[6]}
		8. Bersihkan Garasi, Rapihkan Sepatu, Area Wudu + Buang Sampah: {names[7]}
		9. Bersihkan Rooftop Jemuran belakang: {names[8]}


		Note: Akan dikenakan Denda Rp 20.000 bagi yg tidak melaporkan list dalam seminggu hari kerja
		'''
		return pesan_jumat