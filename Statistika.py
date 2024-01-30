import numpy as np
from collections import Counter
from Aritmatika import Aritmatika


class Statistika(Aritmatika):
    def __init__(self, data):
        self.data = data

    def mean(self):
        return np.mean(self.data)

    def median(self):
        return np.median(self.data)

    def modus(self):
        counter = Counter(self.data)
        modus = counter.most_common(3)[0][0]
        jml_modus = counter[modus]
        modus = [k for k, f in counter.items() if f == jml_modus]
        return modus

    def standar_deviasi(self):
        return np.std(self.data)

    def quartil(self):
        q1 = np.percentile(self.data, 25)
        q2 = np.percentile(self.data, 50)
        q3 = np.percentile(self.data, 75)
        return q1, q2, q3

    def faktorial(self):
        self.angka1 = int(input("Masukkan bilangan bulat positif :"))
        if self.angka1 < 0:
            return "Faktorial tidak terdefinisi untuk bilangan negatif"
        elif self.angka1 == 0:
            return 1
        else:
            fak = self.faktorial(self.angka1 - 1)
            print(f"Faktorial dari !{self.angka1} adalah {fak}")
            return fak


def masukkanBatas(batas):
    array = np.array([])
    while len(array) < batas:
        nilai = input("Masukkan Nilai,lalu klik enter :")
        if nilai.lower() == "done":
            if len(array) < 2:
                print("Minimal ada 2 nilai diperlukan")
                continue
            else:
                break
        try:
            nilai = float(nilai)
            array.append(nilai)
        except ValueError:
            print(
                "Masukkan tidak valid,Masukkan angka atau ketik 'done' untuk mengakhiri"
            )
            return array


print("Selamat datang di Kalkulator Statistika : ")
batas = int(input("Masukkan batas Jumlah nilai yang akan dimasukkan :"))
data = masukkanBatas(batas)

if data:
    print("Hasil :")
