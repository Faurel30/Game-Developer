# Solusi Menara Hanoi (Tower of Hanoi)

## Deskripsi Tugas
Program ini dibuat untuk menyelesaikan permasalahan **Menara Hanoi** dengan 4 piringan yang dipindahkan dari **Tiang A (Start)** ke **Tiang C (Finish)** dengan bantuan **Tiang B**.

## Aturan Permainan
1. Hanya satu piringan yang boleh dipindahkan dalam satu langkah.
2. Setiap langkah mengambil piringan teratas dari salah satu tiang.
3. Piringan berukuran besar **tidak boleh** diletakkan di atas piringan yang lebih kecil.

## Pendekatan Algoritma
Solusi ini menggunakan paradigma **Divide and Conquer** dengan metode **Rekursi**. Untuk memindahkan $n$ piringan dari tiang A ke C:
1. Pindahkan $n-1$ piringan teratas dari tiang A ke tiang B.
2. Pindahkan piringan terbesar ($n$) dari tiang A langsung ke tiang C.
3. Pindahkan $n-1$ piringan dari tiang B ke tiang C.

## Analisis Kompleksitas
* **Jumlah Langkah Minimum**: $2^n - 1 = 2^4 - 1 = 15$ langkah.
* **Kompleksitas Waktu (Time Complexity)**: $O(2^n)$ — jumlah ekskusi bertambah dua kali lipat tiap penambahan piringan.
* **Kompleksitas Ruang (Space Complexity)**: $O(n)$ — kedalaman panggilan rekursi pada memori *stack*.
