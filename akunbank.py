class AkunBank:
   def __init__(self, nomor, pemilik, saldo_awal):
    self.nomor = nomor 
    self.pemilik = pemilik
    self.saldo = saldo_awal
    self.riwayat = []
    
   def cek_saldo(self):
    print(f"Saldo {self.pemilik}: Rp{self.saldo}")
    
   def tarik_tunai(self, jumlah):
    if jumlah <= 0:
        print("jumlah harus lebih besar dari 0")
    elif jumlah <= self.saldo:
        self.saldo -= jumlah
        pesan = f"{self.pemilik}menarik Rp{jumlah}"
        self.riwayat.append(pesan)
        print(pesan)
    else:
        print("saldo tidak cukup!")
  
   def transfer(self, tujuan, jumlah):
    if self.saldo >= jumlah:
        self.saldo -= jumlah
        tujuan.saldo += jumlah
        self.saldo -= 2500
        pesan = f"Transfer Rp{jumlah} ke {tujuan.pemilik} Berhasil dipotong admin Rp2.500"
        self.riwayat.append(pesan)
        print(pesan)
    else:
      print("Transfer Gagal: Saldo tidak cukup.")
      
   def lihat_riwayat(self):
       print(f"riwayat transaksi {self.pemilik}")
       for r in self.riwayat:
           print("-",r)
       
      
