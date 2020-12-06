print('='*60)
print('URAI KATA')
print('='*60)

def urai(kata):
    """
    Metode yang digunakan untuk memecahkan masalah pada kasus urai kata adalah
    dengan mengunakan fungsi iterasi for dan fungsi .append() untuk list. Dari
    output yang dicontohkan pada soal, saya menemukan bahwa output yang dikehendaki 
    memiliki pola penambahan index yang sederhana, yakni [1,2,3,4,..]. Maka dari itu,
    saya membuat melakukan iterasi pada variabel `kata` dan melakukan slicing berdasarkan
    pola tersebut. Hasil dari slicing secara iteratif tersebut kemudian saya masukkan ke
    dalam list `output`. Sebagai treatment akhir, saya membuah elemen pertama (index 0) dari
    list `output` karena elemen itu hanya merupakan list kosong, dan menggabungkan list `output`
    tersebut menjadi sebuah string dengan fungsi .join()
    """
    output = []

    for i in range(len(kata)+1):
        uraian = kata[:i]
        output.append(uraian)
    output.pop(0)

    output = ''.join(output)

    return output

print(urai('Purwadhika'))
print(urai('Python'))
print(urai('Code'))

print('')

def rajut(kata):
    """
    Sama seperti fungsi urai, fungsi rajut ini dibuat pertama-tama dengan terlebih dahulu
    memecahkan pola yang saya dapat pada soal. Saya menemukan bahwa kata asli dari inputan
    awal memiliki panjang yang bisa dicari dengan pola : 
                            N - 1 - 2 - 3 - ... x-1 = x
    di mana N adalah panjang inputan dan x adalah panjang kata asli yang hendak dicari.

    Untuk memecahkan masalah ini, saya menggunakan fungsi iterasi while untuk melakukan
    pengurangan secara iteratif dari panjang kata awal, dan hasil dari pengurangan tersebut
    saya update kedalam variabel `index_list`. Sesuai dengan pola di atas, panjang kata asli
    adalah index terakhir sebelum hasil pengurangan bernilai 0. Jika dilihat pada variabel
    `index_list`, maka panjang kata asli adalah index kedua terakhir (index_list[:-2]).
    
    Akhirnya, kata asli dapat diekstrak dari inputan awal dengan cara mengambil x index dari
    belakang dengan menggunakan metode slicing biasa
    """
    len_kata = len(kata)
    i = 1
    index_list = []

    while len_kata != 0:
        len_kata -= i
        i += 1
        index_list.append(len_kata)

    panjang_kata = index_list[-2]
    output = kata[-panjang_kata:]

    return output


print('='*60)
print('RAJUT KATA')
print('='*60)

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))