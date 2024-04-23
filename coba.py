
#melihat dari https://www.w3schools.com/python/ref_string_replace.asp dan https://jagongoding.com/python/menengah/manipulasi-string-part-1/#string

#capitalize digunakan untuk mengubah huruf menjadi kapital pada huruf pertama
var = "hallo saya kindy"
text = var.capitalize()
print (text)

#casefold adalah mengubah semua kalimat menjadi huruf kecil
casefo = "Hallo saya Kindy"
huruf = casefo.casefold()
print(huruf)

#center adalah mengembalikan kalimat posisinya ditengah berdasarkan angka didalamnya
txt = "Saya belajar AWS"
x = txt.center(20)
print(x)

#Mengabungkan kalimat
depan = "Muhammad"
tengah = "Al"
belakang = "Kindy"
nama_lengkap = depan+" "+tengah+" "+belakang
print(nama_lengkap)

#lower juga digunakan untuk mengubah semua kalimat menjadi huruf kecil
kalimat = "Belajar MTK Menyenangkan SEKALI"
perubahan = kalimat.lower()
print(perubahan)

#upper digunakan untuk mengubah semua kalimat menjadi huruf kapital
lagu = "aku sakit, aku sakit hatii"
perubahan2 = lagu.upper()
print(perubahan2)

#split digunakan untuk memisahkan kata menggunakan pemisah seperti koma dan dikembalikan dalam bentuk list
kalimatsplit = "hallo guys david disini"
kalimatperubahansplit = kalimatsplit.split()
print(kalimatperubahansplit)

#replace digunakan untuk merubah kata pada kalimat
kalimatsebelumreplace = "Saya suka mangga"
kalimatreplace = kalimatsebelumreplace.replace("mangga","Manggis")
print(kalimatreplace)

#Menggunakan dua tanda petik dalam satu kalimat 
#Escape Characters
print('Saya berkata: "Apa kabar?"')
print('Aku ingin: "Kamu pergi sari sini\'angkat kaki\'?!"')

#operasi in pada string akan menghasilkan true false
satukalimat = 'Anto bermain sepeda'
print('Anto' in satukalimat)

#memotong string
nama_saya = 'Muhammad Al Kindy'
print(nama_saya[3])

#memotong string dengan range dalam hal ini spaci dianggap satu charakter
print(nama_saya[0:8])

#menghitung panjang string
print(len('Muhammad Al Kindy'))

#memeriksa karakter awal dan mengembalikan nilai dalam bentuk bolean
nomor_telepon = '0812190475212'
nomor_telepon2= '+6281261721941'

kode_negara = '+62'
print(nomor_telepon.startswith(kode_negara))
print(nomor_telepon2.startswith(kode_negara))

#memeriksa karakter akhir dan mengembalikan dalam bentuk bolean
email_1 = 'al.kindy@gmail.com'
email_2 = 'wasedaboy@outlook.com'

print(email_1.endswith('gmail.com'))
print(email_2.endswith('gmail.com')) 

#mengabungkan string dengan nonstring dengan cara merubah angka dengan fungsi str
print('Sekarang tahun: '+str(2024))

#perkalian dengan string yang akan menghasilkan perulangan sebanyak angka yang diinginkan dalam contoh '2' * 5 maka angka 2 akan diulang sebanyak 5 kali
print('2'* 5)

