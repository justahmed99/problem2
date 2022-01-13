# Petunjuk Penggunaan dan Dokumentasi Software Soccer API (Problem 2)

## Dibuat oleh :
Ahmad Mujahid Abdurrahman (ahmadm.abdurrahman@gmail.com)

## Penginstalan Environment dan Dependensi
- Pastikan bahwa Python 3 dan pip sudah terinstal terlebih dahulu.
- Masukkan terminal / cmd pada root path dari folder project
- Untuk membuat environment, gunakan perintah berikut :
    ```
    $ python -m venv env
    ``` 
- Jika sudah terdapat folder **env** pada folder project, artinya environment telah berhasil dibuat.
- Untuk mengaktifkan environment, gunakan perintah :
    - Pada Windows, gunakan perintah :
        ```
        .\env\Script\activate 
        ```
    - Pada Linux / Mac, gunakan perintah :
        ```
        source env/bin/activate
        ```
- Untuk menginstal dependensi, gunakan perintah :
    ```
    pip install -r requirement.txt
    ```

## Menjalankan program
- Untuk menjalankan program, gunakan perintah :
    ```
    python app/app.py
    ```

## Dokumentasi Project
Untuk mendapatkan daftar dan dokumentasi dari API project ini, kita dapat melihatnya pada halaman Swagger UI dengan URL :

http://localhost:5000/swagger atau http://127.0.0.1:5000/swagger

Terdapat 4 buah API pada project ini, yaitu :
- POST http://localhost:5000/teams atau http://127.0.0.1:5000/teams (digunakan untuk menambahkan daftar tim).
- GET http://localhost:5000/teams?name={nama_team} atau http://127.0.0.1:5000/teams?name={nama_team} (digunakan untuk mendapatkan detail tim, termasuk daftar pemain).
- POST http://localhost:5000/players atau http://127.0.0.1:5000/players (digunakan untuk menambahkan daftar pemain).
- GET http://localhost:5000/teams?number={nomor_pemain}&team={nama_team} atau http://127.0.0.1:5000/teams?name={nama_team} (digunakan untuk mendapatkan detail pemain).

Untuk mendapatkan Postman collection, dapat dengan menimport file **Problem 2.postman_collection.json** atau melalui link https://documenter.getpostman.com/view/6648039/UVXhpweb.

## Unit Test

Ada beberapa langkah yang perlu dilakukan untuk melakukan unit test, yaitu :
- Pastikan program utama sudah berjalan.
- Script yang digunakan untuk melakukan unit test adalah **app/app_test.py**.
- Untuk menjalankan script, gunakan perintah :
    - Jika prompt terminal / CMD berada di root path project :
        ```
        python unittest -m app.app_test
        ```
    - Jika prompt terminal / CMD  berada dalam folder **app** :
        ```
        python unittest -m app.app_test
        ```

## Catatan Penting dalam Menajalankan Program

Jika Anda menggunakan sistem operasi Linux atau Mac, mungkin Anda akan mendapatkan **error** ketika mengeksekusi perintah **python** pada terminal. Gunakan perintah **python3** jika mendapatkan error pada saat menjalankan program.

Hal ini dikarenakan umumnya pada Linux ata Mac, perintah untuk menjalankan script program Python 3 dieksekusi melalui perintah **python3**.