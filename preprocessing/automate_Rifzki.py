# automate_Rifzki.py (Versi yang disempurnakan)
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os
import argparse # Ditambahkan untuk menangani argumen baris perintah

def preprocess_data(input_path, output_path):
    """
    Fungsi untuk memuat, membersihkan, dan memproses data kanker paru-paru.
    """
    print("Memulai proses otomatisasi...")
    if not os.path.exists(input_path):
        print(f"Error: File input tidak ditemukan di '{input_path}'")
        return

    try:
        df = pd.read_csv(input_path)
        print(f"Data berhasil dimuat dari '{input_path}'. Shape: {df.shape}")
    except Exception as e:
        print(f"Gagal memuat data: {e}")
        return

    initial_rows = len(df)
    df_cleaned = df.drop_duplicates()
    final_rows = len(df_cleaned)
    print(f"Menghapus data duplikat. {initial_rows - final_rows} baris dihapus.")

    print("Memulai proses encoding...")
    le = LabelEncoder()
    df_cleaned['GENDER'] = le.fit_transform(df_cleaned['GENDER'])
    df_cleaned['LUNG_CANCER'] = df_cleaned['LUNG_CANCER'].map({'YES': 1, 'NO': 0})
    columns_to_map = [col for col in df_cleaned.columns if col not in ['GENDER', 'AGE', 'LUNG_CANCER']]
    for column in columns_to_map:
        df_cleaned[column] = df_cleaned[column].map({2: 1, 1: 0})
    print("Encoding selesai.")

    try:
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir) and output_dir:
            os.makedirs(output_dir)
        df_cleaned.to_csv(output_path, index=False)
        print(f"Data yang sudah diproses berhasil disimpan di '{output_path}'. Shape: {df_cleaned.shape}")
    except Exception as e:
        print(f"Gagal menyimpan data: {e}")
        return
        
    print("Proses otomatisasi selesai.")

if __name__ == '__main__':
    # Setup parser untuk argumen dari command line
    parser = argparse.ArgumentParser(description='Script untuk preprocessing data kanker paru-paru.')
    parser.add_argument('--input', type=str, required=True, help='Path ke file CSV data mentah.')
    parser.add_argument('--output', type=str, required=True, help='Path untuk menyimpan file CSV yang sudah diproses.')
    args = parser.parse_args()

    # Menjalankan fungsi preprocessing dengan argumen yang diberikan
    preprocess_data(args.input, args.output)