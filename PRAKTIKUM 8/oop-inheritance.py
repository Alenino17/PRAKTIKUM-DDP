
class Person():
    #Definisikan awal variable

    name = ""
    addres = ""
    age = ""

    # Constructor :=> Pembungkus
    def __init__(self, name, addres, age):
        self.name = name
        self.addres = addres
        self.age = age


    # Method / function

    def sayHello(self):
        print("Hello nama saya", self.name, "usia saya", self.age, "alamat saya di", self.addres)


# Extand :=> nurunin sifat dari class person
class Student(Person):
    # Manggil constructor class Person
    def __init__(self, name, addres, age, nim, jurusan):
        super(). __init__(name, addres, age,)
        self.nim = nim
        self.jurusan = jurusan


# Instance object 

bintang = Student("bintang", "Jakarta Timur, Dki Jakarta", 20, "0112011044", "Sistem Informasi")

bintang.sayHello()
print("Nim: ", bintang.nim)
print("Jurusan:  ", bintang.jurusan)