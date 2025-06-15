Proyek Sistem Machine Learning: Eksperimen dan Otomatisasi Preprocessing
Repositori ini adalah implementasi dari Kriteria 1: Eksperimen Terhadap Dataset Pelatihan dalam proyek Membangun Sistem Machine Learning. Proyek ini mencakup seluruh siklus eksperimen data, mulai dari analisis manual di notebook, konversi ke skrip otomatis, hingga penerapan workflow Continuous Integration (CI) menggunakan GitHub Actions untuk level 'Advance'.

Nama: Rifzki Adiyaksa

Deskripsi Dataset
Judul: Survey Lung Cancer Dataset
Sumber: Kaggle
Deskripsi: Dataset ini berisi hasil survei tentang kanker paru-paru dengan 16 atribut, termasuk usia, jenis kelamin, dan berbagai gejala atau faktor risiko. Target utamanya adalah kolom LUNG_CANCER yang menunjukkan apakah responden menderita kanker paru-paru atau tidak.
Struktur Repositori
Struktur repositori ini dirancang untuk mengikuti praktik terbaik dalam proyek machine learning, memisahkan data mentah, kode, dan hasil.

/
├── .github/
│   └── workflows/
│       └── main.yml         # File workflow untuk otomasi CI
├── survey_lung_cancer_raw/
│   └── survey_lung_cancer_raw.csv  # Dataset mentah
├── preprocessing/
│   ├── Eksperimen_MSML_Rifzki.ipynb  # Notebook untuk eksperimen awal
│   ├── automate_Rifzki.py          # Skrip Python untuk otomasi preprocessing
│   └── survey_lung_cancer_preprocessing.csv  # Hasil akhir dari data yang bersih
└── README.md                  # Dokumentasi proyek
Tahapan Pengerjaan
Proyek ini diselesaikan melalui tiga tahapan utama:

Tahap 1: Eksperimen Data di Notebook Jupyter
Tujuan: Menganalisis dan memahami dataset mentah secara mendalam, serta mencoba berbagai teknik preprocessing untuk membersihkan data.
File Terkait: preprocessing/Eksperimen_MSML_Rifzki.ipynb
Langkah-langkah yang Dilakukan:
Data Loading: Memuat dataset survey_lung_cancer_raw.csv menggunakan library pandas.
Exploratory Data Analysis (EDA): Menganalisis statistik dasar, memeriksa nilai yang hilang (missing values), mencari dan mengidentifikasi data duplikat, serta memvisualisasikan distribusi data untuk mendapatkan wawasan.
Data Preprocessing:
Menghapus Data Duplikat: Berdasarkan temuan di EDA, data duplikat dihapus untuk menjaga integritas data.
Encoding Data Kategorikal: Mengubah fitur-fitur kategorikal menjadi format numerik agar dapat diproses oleh model machine learning.
GENDER: Diubah menggunakan LabelEncoder (M -> 1, F -> 0).
LUNG_CANCER dan fitur lainnya: Diubah menggunakan metode mapping (YES/2 -> 1, NO/1 -> 0).
Output Tahap Ini: Sebuah pemahaman yang solid tentang karakteristik dataset dan sebuah file data bersih bernama survey_lung_cancer_preprocessing.csv sebagai hasil awal.
Tahap 2: Otomatisasi Preprocessing dengan Skrip Python
Tujuan: Mengonversi semua langkah preprocessing dari notebook menjadi sebuah skrip Python (.py) yang mandiri dan dapat dieksekusi secara otomatis.
File Terkait: preprocessing/automate_Rifzki.py
Fungsionalitas Skrip:
Modular: Dibuat dalam bentuk fungsi yang dapat digunakan kembali.
Dinamis: Menggunakan argparse untuk menerima path file input (data mentah) dan output (data bersih) dari baris perintah, membuatnya fleksibel dan tidak terikat pada nama file yang statis.
Replikatif: Menjalankan semua logika preprocessing yang sama persis seperti yang ada di notebook untuk memastikan konsistensi hasil.
Output Tahap Ini: Sebuah skrip automate_Rifzki.py yang siap diintegrasikan ke dalam workflow otomatis.
Tahap 3: Implementasi Continuous Integration (CI) dengan GitHub Actions
Tujuan: Membuat sistem yang secara otomatis menjalankan skrip preprocessing setiap kali ada perubahan pada repositori. Ini memastikan dataset yang telah diproses (survey_lung_cancer_preprocessing.csv) selalu sinkron dan mutakhir. Tahapan ini memenuhi kriteria level 'Advance'.
File Terkait: .github/workflows/main.yml
Alur Kerja (Workflow):
Pemicu (Trigger): Workflow berjalan secara otomatis setiap kali ada push ke branch main.
Setup Environment: GitHub menyiapkan sebuah runner (server virtual) dengan sistem operasi Ubuntu dan menginstal versi Python yang ditentukan.
Install Dependencies: Menginstal semua library yang dibutuhkan oleh skrip, seperti pandas dan scikit-learn.
Run Script: Menjalankan skrip automate_Rifzki.py, dengan memberikan path ke data mentah dan path untuk menyimpan data hasil proses sebagai argumen.
Commit & Push Otomatis: Jika eksekusi skrip menghasilkan perubahan pada file survey_lung_cancer_preprocessing.csv, sebuah action khusus (stefanzweifel/git-auto-commit-action) akan secara otomatis melakukan commit dan push file yang diperbarui tersebut kembali ke repositori.
Output Tahap Ini: Sistem CI/CD yang fungsional, di mana file data bersih di repositori selalu terjamin sebagai versi terbaru hasil dari pemrosesan data mentah terkini.
