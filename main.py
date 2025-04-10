## Aplikasi genetic algorithm untuk memenuhi tugas besar mata kuliah kecerdasan buatan
## Dibuat oleh Kelompok 11: Daniyal Arshaq Sudrajat, Riziq Rizwan.

##  =========== HAL YANG HARUS ANDA ANALISIS DAN DESAIN ===========
    ##  Ukuran populasi, rancangan kromosom, dan cara decode-nya
    ##  Metode pemilihan orangtua
    ##  Metode operasi genetik (pindah silang dan mutasi)
    ##  Probabilitas operasi genetik (𝑃𝑐 dan 𝑃𝑚)
    ##  Metode pergantian generasi (seleksi survivor)
    ##  Kriteria penghentian evolusi (loop)

##  =========== OUTPUT PROGRAM ===========
##  Dengan masalah yang didefinisikan di atas, output dari program Anda:
    ##  kromosom terbaik, dan
    ##  nilai 𝒙𝟏 dan 𝒙𝟐 hasil dekode kromosom terbaik tersebut.

##  =========== PEMBAGIAN TUGAS ===========
##  Sistem 50/50
##  Daniyal: 
    ## insialisasi_populasi()
    ## dekode_kromosom()
    ## fitness()
    ## selection()
##  Riziq:
    ## def crossover():
    ## def mutation():
    ## def Generation_Switch():
    ## def main():

## 1. Definisi Tugas
## Diberikan suatu fungsi untuk mencari nilai 𝑥1 dan 𝑥2 sehingga diperoleh nilai minimum dari fungsi matematis berikut:
## 𝑓(𝑥1, 𝑥2) = − (𝑠𝑖𝑛(𝑥1)𝑐𝑜𝑠(𝑥2)tan(𝑥1 + 𝑥2) + 3/4 𝑒𝑥𝑝 (1 − √𝑥1^2)) dengan domain (batas nilai) untuk 𝑥1 dan 𝑥2 adalah −10 ≤ 𝑥1 ≤ 10 dan −10 ≤ 𝑥2 ≤ 10

## Buatlah program menggunakan Algoritma Genetika (GA) untuk menyelesaikan permasalahan di atas. Program menggunakan Python, dan tidak diperbolehkan menggunakan Library yang secara langsung melakukan proses-proses pada GA, 
## sebagaimana tercantum pada deskripsi Case Based. Lakukan analisis dan desain program GA yang Anda buat, lalu implementasikan dengan tepat.

## Hal yang harus Anda analisis dan desain:
## • Ukuran populasi, rancangan kromosom, dan cara decode-nya
## • Metode pemilihan orangtua
## • Metode operasi genetik (pindah silang dan mutasi)
## • Probabilitas operasi genetik (𝑃𝑐 dan 𝑃𝑚)
## • Metode pergantian generasi (seleksi survivor)
## • Kriteria penghentian evolusi (loop)

## Proses yang harus Anda bangun/implementasikan ke dalam baris-baris program:
## • Inisialisasi populasi
## • Dekode kromosom
## • Perhitungan fitness
## • Pemilihan orangtua
## • Crossover (pindah silang)
## • Mutasi
## • Pergantian Generasi
## Catatan: Proses-proses di atas harus dibangun tanpa menggunakan Library!

## 2. Output Program
## Dengan masalah yang didefinisikan di atas, output dari program Anda:
## • kromosom terbaik, dan
## • nilai 𝒙𝟏 dan 𝒙𝟐 hasil dekode kromosom terbaik tersebut

## ================================================================================================================== 
##                                                 PROGRAM
## ================================================================================================================== 

#inisialiasi populasi
def insialisasi_populasi():

#Dekode kromosom
def dekode_kromosom():

#perhitungan fitness
def fitness():

#pemilihan orang tua
def selection():

#Crossover (pindah silang)
def crossover():

#mutasi
def mutation():

#penggantian generasi
def Generation_Switch():

#main function
def main():
    # inisialisasi populasi awal
    populasi_awal = insialisasi_populasi()

