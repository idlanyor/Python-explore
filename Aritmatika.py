class Aritmatika:
    def __init__(self,angka1 =0,angka2=0) :
        self.angka1 = angka1
        self.angka2 = angka2
        
    @staticmethod
    def inputan(self):
        try:
            self.angka1 = int(input("Masukkan bilangan pertama : "))
            self.angka2 = int(input("Masukkan bilangan kedua : "))
        except ValueError:
            "Input harus berupa Integer !"
    
    def penjumlahan(self):
        self.inputan(self)
        print(f"Hasil dari {self.angka1} + {self.angka2} adalah {self.angka1 + self.angka2}")
    
    def pengurangan(self):
        self.inputan(self)
        print(f"Hasil dari {self.angka1} - {self.angka2} adalah {self.angka1 - self.angka2}")

    
    def perkalian(self):
        self.inputan(self)
        print(f"Hasil dari {self.angka1} x {self.angka2} adalah {self.angka1 * self.angka2}")
    
    def pembagian(self):
        self.inputan(self)
        if(self.angka2 ==0):
            return "Pembagian dengan 0 tidak diperbolehkan"
        print(f"Hasil dari {self.angka1} / {self.angka2} adalah {self.angka1 / self.angka2}")
    
    def modulo(self):
        self.inputan(self)
        print(f"Hasil dari {self.angka1} % {self.angka2} adalah {self.angka1 % self.angka2}")
    
    def pangkat(self):
        try:
            self.angka1 = float(input("Masukkan Angka yang ingin dipangkatkan : "))
            self.angka2 = float(input("Eksponen/Pangkat : "))
        except ValueError:
            return "Input harus berupa angka"
        print(f"Hasil dari {self.angka1} ^ {self.angka2} adalah {self.angka1 ** self.angka2}")
    
    def faktorial(self):
        self.angka1 = int(input("Masukkan bilangan bulat positif :"))
        if self.angka1 < 0:
            return "Faktorial tidak terdefinisi untuk bilangan negatif"
        elif self.angka1 == 0:
            return 1
        else:
            faktorial = 1
            for i in range(1,self.angka1 +1):   
                faktorial *= i
        print(f"Faktorial dari !{self.angka1} adalah {faktorial}")
    
    
menu = [
    "penjumlahan","Pengurangan",
]
my = Aritmatika()
print(str(my.faktorial()))