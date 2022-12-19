class person :
    # Property:=>variable
    nama =""
    alamat =""
    jurusan =""
    # Method:=>function

    def tampilkan_data(self):
        print(f"Nama: {self, nama}")
        print(f"Alamat: {self, alamat}")
        print(f"Jurusan: {self, jurusan}")

person = Person()


# Assignment ==> isi nilai / value data property

person.nama ="Alenino"        
person.alamat ="Jakarta Timur"        
person.jurusan ="Sistem Informasi"        

# Panggil method / fungsi
person.tampilkan_data()

person2 = Person()

person2.nama="Joko"
person2.alamat="Jakarta Timur"
person2.jurusan="Sistem Informasi"

person2.tampilkan_data()
        