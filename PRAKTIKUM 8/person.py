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