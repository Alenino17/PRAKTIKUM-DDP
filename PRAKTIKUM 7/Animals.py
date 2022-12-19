class Animals:
    animals =[]


    def __init__(self,  animals):
       self.animals = animals

    def index(self):
        # Perulangan
        for animal in self.animals:
            print(f"Nama hewan:  {animal}") 

    def show(self):
        print(f"Menampilkan animal ke- {self.animals[position]}")

    def update(self) 