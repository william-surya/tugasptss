from os import system

daftar_varian = {
	"Coklat" : {
		"harga" : "10000",
		"kode" : "C"
		},
	"Strawberry" : {
		"harga" : "12000",
		"kode" : "S"
		},
	"Vanilla" : {
		"harga" : "12000",
		"kode" : "V"
		},
	}

def mencarikode(x):
	if {daftar_varian[x['kode']]} in daftar_varian:
		return True
	else :
		print("Varian tidak tersedia")
		return False

def mencaribarang(x):
	if x in daftar_varian:
		return True
	elif x not in daftar_varian :
		print("Varian tidak tersedia !")
		return False

def viewlistA() :
		system("cls")
		print(">>> Selamat Datang Di Happy Ice Cream ^_^ <<<")
		print("""
[A] Tampilkan Varian
[B] Mencari Varian
[C] Masuk Mode Admin
[Q] Keluar
""")

def tampilkan_varian() :
		system("cls")
		print(">>> Varian Rasa Es Krim <<<\n")
		for varian in daftar_varian:
			varian = varian
			harga = daftar_varian[varian]['harga']
			kode = daftar_varian[varian]['kode']
			print(f">> {varian} <<\n   Harga = {harga}\n   Kode = {kode}")
		input("=== Tekan ENTER untuk kembali ===")

def verifyans(x):
		x = x.upper()
		if x == "X" :
			return True
		else :
			return False

def menambah_varian() :
		system("cls")
		print(">>> Menambah Varian Baru <<<")
		varian = input("Varian Baru : ")
		harga = (input("Harga = "))
		kode = input("Kode = ")

		verif = input("Tekan X Untuk Menyimpan :")

		if verifyans(verif):
			print("Data Tersimpan")
			daftar_varian[varian] = {
				"harga" : harga,
				"kode" : kode
			}
			tampilkan_varian()
		else : (" Data tidak tersimpan ")

def mengedit_harga(x):
	system("cls")
	hargabaru = input("Harga Baru : ")
	pilihanA = input("Ketik X Untuk melanjutkan ! : ")
	if verifyans(pilihanA):
		daftar_varian[x]['harga'] = hargabaru
		print("Harga diperbaharui !")
		tampilkan_varian()
	else :
		print("Harga gagal diperbaharui")

def mengedit_kode(x):
	system("cls")
	kodebaru = input("Kode Baru = ")
	pilihanA = input("Ketik X Untuk Melanjutkan ! : ")
	if verifyans(pilihanA):
		daftar_varian[x]['kode'] = kodebaru
		print("Kode diperbaharui ! ")
		tampilkan_varian()
	else:
		print("Kode gagal diperbaharui")

def mengedit_varian() :
	system("cls")
	print(" === Pengeditan Varian === \n")
	varian = input("Varian apa yang ingin diperbaharui ? = ")
	hasil = mencaribarang(varian)
	if hasil:
		print("Apa yang ingin diperbaharui ? \n [1] Harga\n [2] Kode")
		pilihan1 = input("Pilihan :")
		if pilihan1 == "1" :
			mengedit_harga(varian)
		elif pilihan1 == "2" : 
			mengedit_kode(varian)
	input("Tekan ENTER untuk kembali")

def mencari_varian() :
	system("cls")
	print("Mencari Varian Es Krim")
	varian = input("Rasa apa yang ingin dicari ? = ")
	hasil = mencaribarang(varian)
	if hasil :
		print(f">> {varian} <<\n   Harga = {daftar_varian[varian]['harga']}\n   Kode = {daftar_varian[varian]['kode']}")
	input("Tekan ENTER untuk kembali")

def viewlistB() :
	system("cls")
	print("""
[A] Tampilkan Varian
[B] Menambah Varian
[C] Mengedit Varian
[D] Menghapus Varian
[Q] Keluar Dari Mode Admin?
""")

def menghapus_varian():
	system("cls")
	print("< Menghapus Varian >")
	varian = input("Varian apa yang akan dihapus ? :")
	hasil = mencaribarang(varian)
	if hasil:
		pilihanA = input("Ketik X untuk menghapus ! : ")
		if verifyans(pilihanA):
			del daftar_varian[varian]
			print("Varian Telah Dihapus")
		else:
			print("Varian Gagal Dihapus")
	tampilkan_varian()

def cekinputadmin(x) :
	x = x.upper()
	if x == "Q" :
		return True
	elif x == "A" :
		tampilkan_varian()
	elif x == "B" :
		menambah_varian()
	elif x == "C" :
		mengedit_varian()
	elif x == "D" : 
		menghapus_varian()

def modeadmin() :
	system("cls")
	Password = input("Masukkan Password = ")
	while Password != "WILLIAM" :
		print("Password Salah !")
		Password = input("Masukkan Password = ")
	stop = False
	while not stop :
		viewlistB()
		pilihan = input("Pilihan ? :")
		stop = cekinputadmin(pilihan)


def cekinputpembeli(x) :
		x = x.upper()
		if x == "Q" :
			return True
		elif x == "A" :
			tampilkan_varian()
		elif x == "B" : 
			mencari_varian()
		elif x == "C" : 
			modeadmin()


stop = False
while not stop : 
	viewlistA()
	inputpembeli = input("Pilihan : ")
	stop = cekinputpembeli(inputpembeli)