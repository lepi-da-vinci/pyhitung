import random
import time

# --- Bagian 1: Fungsi untuk Mengelola High Score ---
def simpan_high_score(skor_baru):
    """Membaca high score dari file dan menyimpannya jika skor baru lebih tinggi."""
    try:
        with open("high_score.txt", "r") as file:
            skor_lama = int(file.read())
    except (IOError, ValueError):
        # File tidak ada atau isinya bukan angka, jadi anggap skor lama 0
        skor_lama = 0

    if skor_baru > skor_lama:
        with open("high_score.txt", "w") as file:
            file.write(str(skor_baru))
        print(f"Selamat! Anda mencetak high score baru: {skor_baru}")
    else:
        print(f"High score Anda saat ini adalah: {skor_lama}")

def tampilkan_high_score():
    """Menampilkan high score yang tersimpan."""
    try:
        with open("high_score.txt", "r") as file:
            skor = file.read()
            print(f"High score saat ini: {skor}")
    except (IOError, ValueError):
        print("Belum ada high score yang tercatat.")

# --- Bagian 2: Fungsi Logika Permainan ---
def buat_soal(level):
    """Membuat soal berdasarkan level yang dipilih."""
    if level == "mudah":
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)
        operasi = random.choice(["+", "-"])
    elif level == "sedang":
        angka1 = random.randint(1, 50)
        angka2 = random.randint(1, 50)
        operasi = random.choice(["+", "-", "*"])
    else:  # level "sulit"
        angka1 = random.randint(1, 100)
        angka2 = random.randint(1, 100)
        operasi = random.choice(["+", "-", "*", "/"])
        # Pastikan pembagian tidak menghasilkan desimal
        if operasi == "/":
            angka1 = angka1 * angka2
    
    soal = f"Berapa hasil dari {angka1} {operasi} {angka2}? = "
    jawaban_benar = eval(f"{angka1}{operasi}{angka2}") # Gunakan eval untuk menghitung ekspresi string
    
    return soal, jawaban_benar

def main_game(mode, level):
    """Fungsi utama game berdasarkan mode dan level."""
    skor = 0
    jumlah_soal_benar = 0
    waktu_mulai = time.time()
    
    print(f"\nMode: {mode.title()} | Level: {level.title()}\n")
    
    if mode == "latihan":
        jumlah_soal = 10
        for i in range(jumlah_soal):
            soal, jawaban_benar = buat_soal(level)
            try:
                jawaban_user = int(input(f"Soal {i+1}: {soal} "))
                if jawaban_user == jawaban_benar:
                    print("Benar!")
                    skor += 10
                    jumlah_soal_benar += 1
                else:
                    print(f"Salah. Jawaban yang benar adalah {jawaban_benar}.")
            except ValueError:
                print("Input tidak valid. Soal dianggap salah.")
        
        waktu_selesai = time.time()
        waktu_total = round(waktu_selesai - waktu_mulai, 2)
        
        print("\n--- Permainan Selesai ---")
        print(f"Skor Anda: {skor}")
        print(f"Anda menjawab benar {jumlah_soal_benar} dari {jumlah_soal} soal.")
        print(f"Waktu total: {waktu_total} detik.")
        
    elif mode == "bertahan hidup":
        while True:
            soal, jawaban_benar = buat_soal(level)
            try:
                jawaban_user = int(input(soal))
                if jawaban_user == jawaban_benar:
                    print("Benar!")
                    skor += 10
                else:
                    print(f"Salah! Jawaban yang benar adalah {jawaban_benar}.")
                    break
            except ValueError:
                print("Input tidak valid. Permainan berakhir.")
                break
        
        print("\n--- Game Over ---")
        print(f"Skor akhir Anda: {skor}")
        simpan_high_score(skor)

# --- Bagian 3: Fungsi Menu Utama ---
def menu_utama():
    """Menampilkan menu utama dan mengelola pilihan pemain."""
    while True:
        print("\n=== Game Hitung Sederhana ===")
        print("1. Main Game")
        print("2. Lihat High Score")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            mode = input("Pilih mode (latihan/bertahan hidup): ").lower()
            if mode not in ["latihan", "bertahan hidup"]:
                print("Mode tidak valid. Silakan coba lagi.")
                continue
            
            level = input("Pilih level (mudah/sedang/sulit): ").lower()
            if level not in ["mudah", "sedang", "sulit"]:
                print("Level tidak valid. Silakan coba lagi.")
                continue
                
            main_game(mode, level)
        elif pilihan == "2":
            tampilkan_high_score()
        elif pilihan == "3":
            print("Terimakasih. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan game dari menu utama
if __name__ == "__main__":
    menu_utama()