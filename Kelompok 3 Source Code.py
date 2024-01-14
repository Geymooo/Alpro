def Garis():
    print("-----------------------------------------------------------------------------------------")

Garis()
print("List HARGA TIKET CONSER COLDPLAY DIJAKARTA 2023 ")
print("KODE PEMBELIAN         |Paket Pembelian Kursi          | Harga Ticket ")
Garis()
print("101                    |ULTIMATE EXPERIENCE (CAT 1)    | Rp.11.000.000")
print("102                    |MY UNIVERSE (FESTIVAL)         | Rp.5.700.000")
print("103                    |CAT 1 (NUMBERING SEATING)      | Rp.5.000.000")
print("104                    |FESTIVAL (FREE STANDING)       | Rp.3.500.000")
print("105                    |CAT 2 (NUMBERING SEAT)         | Rp.4.000.000")
print("106                    |CAT 3 (NUMBERING SEAT)         | Rp.3.250.000")
print("107                    |CAT 4 (NUMBERING SEAT)         | Rp.2.500.000")
print("108                    |CAT 5 (NUMBERING SEAT)         | Rp.1.750.000")
print("109                    |CAT 6 (NUMBERING SEAT)         | Rp.1.250.000")
print("110                    |CAT 7 (RESTRICTED VIEW)        | Rp.1.250.000")
print("111                    |CAT 7 (RESTRICTED VIEW)        | Rp.800.000")
Garis()

nama = input("Nama Pembeli : ")
nomor = input("Nomor Telepon : ")
paket = []
harga_total = 0

while True:
    tiket = input("Masukkan KODE PEMBELIAN TIKET (ketik q jika sudah): ")

    if tiket == "q":
        break

    if tiket in ["101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111"]:
        jumlah_pembelian = int(input(f"Masukkan JUMLAH PEMBELIAN untuk {tiket}: "))
        if tiket == "101":
            harga_tiket = 11000000
            paket.append({
                "Jenis Tiket": "ULTIMATE EXPERIENCE (CAT 1)",
                "Jumlah Pembelian": jumlah_pembelian,
                "Harga": harga_tiket
            })
            harga_total += harga_tiket * jumlah_pembelian
        elif tiket == "102":
            harga_tiket = 5700000
            paket.append({
                "Jenis Tiket": "MY UNIVERSE (FESTIVAL)",
                "Jumlah Pembelian": jumlah_pembelian,
                "Harga": harga_tiket
            })
            harga_total += harga_tiket * jumlah_pembelian
        elif tiket == "103":
            harga_tiket = 5000000 
            paket.append({
                "Jenis Tiket": "CAT 1 (NUMBERING SEATING)",
                "Jumlah Pembelian": jumlah_pembelian,
                "Harga": harga_tiket
            })
            harga_total += harga_tiket * jumlah_pembelian
        elif tiket == "104":
            harga_tiket = 3500000
            paket.append({
                "Jenis Tiket": "FESTIVAL (FREE STANDING)",
                "Jumlah Pembelian": jumlah_pembelian,
                "Harga": harga_tiket
            })
            harga_total += harga_tiket * jumlah_pembelian
        elif tiket == "105":
            harga_tiket = 4000000
            paket.append({
                "Jenis Tiket": "CAT 2 (NUMBERING SEAT)",
                "Jumlah Pembelian": jumlah_pembelian,
                "Harga": harga_tiket
            })
            harga_total += harga_tiket * jumlah_pembelian
        elif tiket == "106":
            harga_tiket = 3250000
            paket.append({
                "Jenis Tiket": "CAT 3 (NUMBERING SEAT)",
                "Jumlah Pembelian": jumlah_pembelian,
                "Harga": harga_tiket
            })
            harga_total += harga_tiket * jumlah_pembelian
        elif tiket == "107":
            harga_tiket = 2500000
            paket.append({
                "Jenis Tiket": "CAT 4 (NUMBERING SEAT)",
                "Jumlah Pembelian": jumlah_pembelian,
                "Harga": harga_tiket
            })
            harga_total += harga_tiket * jumlah_pembelian
        elif tiket == "108":
            harga_tiket = 1750000
            paket.append({
                "Jenis Tiket": "CAT 5 (NUMBERING SEAT)",
                "Jumlah Pembelian": jumlah_pembelian,
                "Harga": harga_tiket
            })
            harga_total += harga_tiket * jumlah_pembelian
        elif tiket == "109":
            harga_tiket = 1250000
            paket.append({
                "Jenis Tiket": "CAT 6 (NUMBERING SEAT)",
                "Jumlah Pembelian": jumlah_pembelian,
                "Harga": harga_tiket
            })
            harga_total += harga_tiket * jumlah_pembelian
        elif tiket == "110":
            harga_tiket = 1250000
            paket.append({
                "Jenis Tiket": "CAT 7 (RESTRICTED VIEW)",
                "Jumlah Pembelian": jumlah_pembelian,
                "Harga": harga_tiket
            })
            harga_total += harga_tiket * jumlah_pembelian
        elif tiket == "111":
            harga_tiket = 800000
            paket.append({
                "Jenis Tiket": "CAT 3 (NUMBERING SEAT)",
                "Jumlah Pembelian": jumlah_pembelian,
                "Harga": harga_tiket
            })
            harga_total += harga_tiket * jumlah_pembelian
        else:
            print("KODE PEMBELIAN TIKET TIDAK SESUAI ! ")
    else:
        print("KODE PEMBELIAN TIKET TIDAK SESUAI ! ")

ppn = harga_total*0.15
biaya_layanan = harga_total*0.05
total_harga = harga_total+ppn+biaya_layanan

Garis()
print("Nama Pembeli :", nama)
print("Nomor Telepon :", nomor)
Garis()

for item in paket:
    print("Jenis Tiket :",item["Jenis Tiket"])
    print("Jumlah Pembelian :",item["Jumlah Pembelian"])
    print("Harga Tiket per Unit :",item["Harga"])
    print()

print("PPN (15%) :", ppn)
print("Biaya Layanan (5%) :", biaya_layanan)
print("Total Harga Keseluruhan :", total_harga)