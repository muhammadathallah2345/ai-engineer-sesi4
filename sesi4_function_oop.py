# Materi Sesi 4 - Function & OOP

# 1. Contoh Function
def hitung_rata_rata(nilai_list):
    if not nilai_list:
        return 0
    return sum(nilai_list) / len(nilai_list)

# 2. Contoh OOP
class PesertaBootcamp:
    def __init__(self,nama, program, nilai):
        self.nama = nama
        self.program = program
        self.nilai = nilai

    def tampilkan_profil(self):
        rata_rata = hitung_rata_rata(self.nilai)
        return f"peserta: {self.nama} | Program: {self.program} | Rata_rata Nilai: {rata_rata:.2f}"


if __name__ == "__main__":
    peserta1 = PesertaBootcamp("Muhammad Athallah Ghatfaan", "AI Engineer", [85, 90, 78, 92])
    print(peserta1.tampilkan_profil())

           
