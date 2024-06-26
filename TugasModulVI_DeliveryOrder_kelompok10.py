print ('\nKelompok : 10')
print ('Sabtu, shift kedua')
print ('\nAnggota Kelompok :')
print ('1. Ahmad Aldani Herlangga (21120120140168)')
print ('2. Enrico Gathan Agung (21120123140127)')
print ('3. Naufal Labib Nugroho (21120123130109)')
print ('4. Rafi Rai Pasha Afandi (21120123100073)\n')
print()

print (100*('-'))
txt = 'Silahkan Lengkapi data diri anda'
x = txt.center (100)
print (x)
print (100*('-'))
print()


class registrasiCustomer:
    def __init__(self, namaCustomer, alamatCustomer, emailCustomer):#Method berparameter dengan non-return
        self.namaCustomer = namaCustomer
        self.alamatCustomer = alamatCustomer
        self.emailCustomer = emailCustomer

namaCustomer = input("Silahkan masukan nama anda: ")
alamatCustomer = input('Silahkan masukan alamat lengkap anda : ')
emailCustomer = input('Silahkan masukkan email Anda : \n')

class tambahkanMakanan: 
    def __init__(self):#method non-parameter non-return
        self.pesanItem = []

    def tambahkanMakanan(self, namaMakanan, jumlahMakanan):#method berparameter non-return
        self.pesanItem.append({'namaMakanan': namaMakanan, 'jumlahMakanan': jumlahMakanan})
        print(f"{namaMakanan} sejumlah {jumlahMakanan} telah ditambahkan ke dalam keranjang!")

    def liatKeranjang(self):#Method berparameter dengan non-return
        print('Pesanan Anda sebagia Berikut : ')
        for item in self.pesanItem:
            print(f'-{item["jumlahMakanan"]} {item["namaMakanan"]}')

    def calculatorHarga(self):#Method berparameter dengan return
        total = 0
        for item in self.pesanItem:
            total += self.hargaMakanan(item['namaMakanan']) * item['jumlahMakanan']
        return total

    def konfirmasiPesanan(self):#Method non-parameter dengan return
        konfirmasi = input("Silahkan tekan 'Ya' untuk mengonfirmasi pesanan anda (Ya/Tidak): ")
        if konfirmasi.lower() == 'ya':
            print('Terima kasih telah melakukan pemesanan^^')
            return True
        else:
            print('Pesanan Anda telah dibatalkan.')
            return False

    def hargaMakanan(self, namaMakanan):#Method berparameter dengan return
        hargaMakanan = {"Gudeg": 20000, "Gulai Kambing": 45000, "Es Teh": 5000, "Sop Ayam": 20000, "Air Es": 2000, "Jus Jeruk": 6000}
        return hargaMakanan.get(namaMakanan, 0)

def main():#fuction utama non-parameter dengan non return
    deliveryOrder = tambahkanMakanan()


    while True:
        print (100*('-'))
        txt = 'SELAMAT DATANG DI WARUNG SEDERHANA'
        x = txt.center (100)
        print (x)
        print (100*('-'))
        print()

        print('MENU MAKANAN')
        print('1. Gudeg : Rp20000')
        print('2. Gulai Kambing : Rp45000')
        print('3. Sop Ayam : 20000')
        print('4. Es Teh : 5000')
        print('5. Air Es: 2000')
        print('6. Jus Jeruk : 6000')

        print('Silahkan pilih :\n ')
        print('1. Tambahkan Makanan ke keranjang')
        print('2. Lihat keranjang')
        print('3. Lihat total pembayaran')
        print('4. Konfirmasi pesanan anda')

        pilihan = input('Silahkan masukan pilihan Anda : ')

        if pilihan == '1':
            namaMakanan = input('Tambahkan makanan : ')
            jumlahMakanan = int(input('Masukan jumlah yang Anda inginkan : '))
            deliveryOrder.tambahkanMakanan(namaMakanan, jumlahMakanan)

        elif pilihan == '2':
            deliveryOrder.liatKeranjang()

        elif pilihan == '3':
            total = deliveryOrder.calculatorHarga()
            print(f"Total pembayaran: Rp{total}")
            
        elif pilihan == '4':
            if deliveryOrder.konfirmasiPesanan():
                break
        else:
            print('Pilihan tidak valid, silahkan masukan pilihan kembali')

if __name__ == "__main__":
    main()
