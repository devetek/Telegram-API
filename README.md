# Tentang

Simple Sample Telegram API (SSTA) adalah contoh sederhana aplikasi python untuk integrasi dengan telegram bot. Hal yang dapat dilakukan di dalam contoh sederhana ini adalah, saat melakukan chat dengan bot, bot akan otomatis membalas dengan text yang sama dan akan melakukan broadcast ke channel yang dituju, sebagai contoh saat ini menggunakan channel public [`@terpusat`](https://t.me/terpusat) dan bot yang digunakan sebagai sample `@TerpusatBot`.

Untuk tingkat lanjut, kamu dapat melakukan integrasi dengan beberapa system yang ada. Sebagai contoh, integrasi dengan schedular saat terjadi error di network atau di database atau di sistem lain, untuk melakukan alerting ke channel atau ke personal atau bahkan ke atasan biar sekalian dapet SP.


## Cara Menggunakan

Pastikan anda menggunakan UNIX untuk saat ini, karena saat ini belum ada test yang dilakukan ke OS Windows. Jalankan command di bawah ini untuk melakukan pengaturan dasar:

```sh
make run-setup
```

Selanjutnya, buka file `development.ini` dan isi pengaturan `TelegramToken` dengan token ID yang telah anda buat sebelumnya. Asumsinya kamu sudah paham cara membuat bot, untuk cara membuat bot silahkan kunjungi [Telegram Bot](https://core.telegram.org/bots).

Setelah menjalankan command di atas, jalankan (SSTA) dengan command di bawah ini:

```sh
make run-dev
```

Setelah semua pengaturan dipenuhi, buka telegram dan lakukan chat dengan bot `@<BOT-KAMU>Bot`. Lihat apa yang akan dilakukan bot pada chat tersebut dan yang akan dilakukan bot terhadap channel.

## Masalah ?

Jika kamu menemui masalah saat menjalankan aplikasi ini, jangan sungkan untuk menghubungi kami di [DEVETEK](http://www.devetek.com).