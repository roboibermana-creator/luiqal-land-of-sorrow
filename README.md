# Luiqal — Land of Sorrow

Website kenangan pasangan bergaya *pixel art* 16-bit JRPG. Satu halaman HTML tanpa
framework, seluruh animasinya memakai CSS murni (`@keyframes`), JavaScript hanya
dipakai untuk berpindah tampilan dan membuka lightbox.

## Cara menjalankan

Buka `index.html` langsung di browser. Tidak ada proses build.

Kode masuk: `01052026`

## Isi tampilan

| Layar | Isi |
|---|---|
| Judul | Teks "OUR ADVENTURE" & "PRESS START" bergerak, kelopak bunga berjatuhan (2 lapis) |
| Password | Dua penjaga gerbang menunduk saat kolom sandi diketik (sprite sheet 2 frame) |
| Dashboard | Lanskap berjalan (*treadmill*) + kuda berjalan di tempat (sprite sheet 3 frame) |
| Photobooth | Galeri kisi berisi foto photobooth |
| Photo Random | 7 halaman, tiap halaman 4 foto di atas gulungan dokumen |
| Photo Romance | 3 halaman, tiap halaman 3 foto di dalam bingkai vas |

Klik foto mana pun untuk membukanya dalam ukuran penuh (panah kiri/kanan, Esc untuk menutup).

## Struktur folder

```
index.html                 seluruh markup, CSS, dan JS
gambarpixel/               aset pixel art
  anim/                    aset turunan untuk animasi (sprite sheet, bingkai, panel)
  motion/                  sprite sheet mentah (kelopak, penjaga, kuda)
  page_photorandom/        aset terpisah halaman photo random
  bagian */                aset terpisah per halaman
photo/                     foto asli
  thumb/                   versi kecil yang dipertajam untuk tampilan galeri
musik/                     musik latar
fonts/                     berkas font
```

## Catatan teknis

- Semua aset pixel art memakai `image-rendering: pixelated` supaya tidak diburamkan browser.
- Panel galeri disimpan hasil *upscale* nearest-neighbour ×6 (`gambarpixel/anim/panel_*_hi.png`)
  lalu dikecilkan browser — tepi pikselnya tetap tegas tanpa blok yang ukurannya tidak rata.
- Foto galeri memakai thumbnail 256 px yang sudah dipertajam; lightbox memuat berkas aslinya.
- Panggung memakai rasio tetap 1024:516 agar tata letaknya tidak bergeser di layar mana pun.
