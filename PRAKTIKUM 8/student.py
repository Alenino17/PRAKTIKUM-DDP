# from Person import *
 from Modul.Person import Person

# Extand :=> nurunin sifat dari class person
class Student(Person):
    # Manggil constructor class Person
    def __init__(self, name, addres, age, nim, jurusan):
        super(). __init__(name, addres, age,)
        self.nim = nim
        self.jurusan = jurusan
