class Mangga:

    # Magic Method

    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah
    
    def __repr__(self):
        return "Debug - Mangga : {} dengan jumlah : {}".format(self.nama, self.jumlah)
    
    def __str__(self):
        return "Mangga : {} dengan jumlah : {}".format(self.nama, self.jumlah)
        
    def __add__(self, objek):
        return self.jumlah + objek.jumlah

    @property
    def __dict__(self):
        return "Objek ini mempunyai nama dan jumlah"
    

belanja1 = Mangga("Arumanis", 10)
belanja2 = Mangga("Mana Lagi", 30)

print(belanja1)
print(belanja2)
print()

print(belanja1 + belanja2)
print()

print(belanja1.__dict__)



'''
    NB :
        - def __init__(self)        ~> Berfungsi untuk mengeksekusi method langsung saat object dibuat.
        - def __repr__(self)		~> Berfungsi untuk mengeksekusi method apabila object diprint, biasanya dipakai saat debuging.
        - def __str__(self)			~> Berfungsi untuk mengeksekusi method apabila object diprint, biasanya dipakai saat program sudah jadi.
        - def __add__(self, objek)	~> Berfungsi untuk menjumlahkan suatu variable dari kedua object. 
        - def __dict__(self)		~> Berfungsi untuk mengoverride method __dict__.



'''
        
        