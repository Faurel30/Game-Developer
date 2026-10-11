def hanoi(n, asal, tujuan, bantuan):
    if n == 1:
        print(f"Pindahkan piringan 1 dari tiang {asal} ke tiang {tujuan}")
        return
    
    # 1. Pindahkan n-1 piringan dari asal ke bantuan
    hanoi(n - 1, asal, bantuan, tujuan)
    
    # 2. Pindahkan piringan paling besar ke tujuan
    print(f"Pindahkan piringan {n} dari tiang {asal} ke tiang {tujuan}")
    
    # 3. Pindahkan n-1 piringan dari bantuan ke tujuan
    hanoi(n - 1, bantuan, tujuan, asal)

if __name__ == "__main__":
    jumlah_piringan = 4
    print(f"=== Langkah Penyelesaian Menara Hanoi ({jumlah_piringan} Piringan) ===")
    hanoi(jumlah_piringan, 'A', 'C', 'B')
