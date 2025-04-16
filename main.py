# -*- coding: utf-8 -*-

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

## Buatlah program menggunakan Algoritma Genetika (GA) untuk menyelesaikan permasalahan di atas. Program menggunakan Python, 
## dan tidak diperbolehkan menggunakan Library yang secara langsung melakukan proses-proses pada GA, 
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

import random
import math

# konstanta
PANJANG_KROMOSOM = 20 # panjang kromosom binary
BIT_PER_VAR = 10 # variable x1 dan x2 direpresentasikan dengan 10 bit dalam kromosaom binary
POPULATION_SIZE = 30 # ukuran populasi
P_C = 0.8 # propability crossover
P_M = 0.01 # propability mutation
GENERASI = 100 # jumlah generasi

# fungsi matematis untuk mencari nilai 𝑥1 dan 𝑥2 sehingga diperoleh nilai minimum
def fungsi_matematis(x1, x2):
    try:
        return - (math.sin(x1) * math.cos(x2) * math.tan(x1 + x2) + (3 / 4) * math.exp(1 - math.sqrt(x1 ** 2)))
    except:
        return float('inf')

#inisialiasi populasi
def insialisasi_populasi():
    # menggunakan library random dari python untuk membuat kromosom binary berjumlah POPULATION_SIZE, atau 30 
    return [''.join(random.choice('01') for _ in range(PANJANG_KROMOSOM)) for _ in range(POPULATION_SIZE)]

#dekode kromosom
def dekode_kromosom(kromosom):
    #kromosom 20 bit dibagi menjadi dua bagian 10 bit
    x1_binary = kromosom[:BIT_PER_VAR] #ambil 10 bit pertama sebagai x1
    x2_binary = kromosom[BIT_PER_VAR:] #ambil 10 bit pertama sebagai x2

    #ubah biner ke desimal
    x1_desimal = int(x1_binary, 2) #ubah dari biner ke integer
    x2_desimal = int(x2_binary, 2) #ubah dari biner ke integer

    #skala ke rentang [-10, 10]
    #menggunakan linear scaling formula = nilai = batas_bawah + (range * desimal / (maksimum_desimal))
    # xmin = -10
    # range = 20 bit
    # maksimum_desimal = 2^20 - 1 = 1023
    x1 = -10 + (20 * x1_desimal / (2**BIT_PER_VAR - 1))
    x2 = -10 + (20 * x2_desimal / (2**BIT_PER_VAR - 1))

    return x1, x2

#perhitungan fitness
def fitness(populasi)
    fitness_values = []
    for kromosom in populasi:
        # dekode kromosom menjadi nilai x1 dan x2 rentang [-10, 10]
        x1, x2 = dekode_kromosom(kromosom)
        # hitung nilai fitness berdasarkan x1 dan x2
        fungsi = fungsi_matematis(x1, x2)
        #menambahkan satu item ke list
        fitness_values.append((kromosom, x1, x2, fungsi))
    return fitness_values

#pemilihan orang tua
def selection():
    

#Crossover (pindah silang)
def crossover():
    

#mutasi
def mutation():
    

#penggantian generasi
def generation_switch():
    

#main function
def main():
    # inisialisasi populasi awal
    populasi_awal = insialisasi_populasi()
    print("Populasi Awal:")
    for i, kromosom in enumerate(populasi_awal, start=1):
        print(f"{i:2d}: {kromosom}")
    fitness_pop = fitness(populasi_awal)
    print("Fitness awal:")
    for krom, x1, x2, funct in fitness_pop:
        print(f"Kromosom: {krom}, x1: {x1}, x2: {x2}, Fitness: {funct}")

