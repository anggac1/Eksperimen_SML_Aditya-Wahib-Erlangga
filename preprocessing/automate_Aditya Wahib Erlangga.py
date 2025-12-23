import pandas as pd
import os

def preprocess_data():
    # Mendapatkan lokasi script ini berada
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Mendapatkan lokasi root project (naik satu level)
    project_root = os.path.dirname(script_dir)
    
    # REVISI PATH DI SINI:
    # Mengarah ke folder 'emails_raw'
    input_csv = os.path.join(project_root, 'emails_raw', 'emails.csv')
    
    # Mengarah ke folder 'emails_preprocessing' (di dalam folder script_dir)
    output_dir = os.path.join(script_dir, 'emails_preprocessing')
    output_csv = os.path.join(output_dir, 'emails_preprocessing.csv')

    print(f"Mencari dataset di: {input_csv}")
    print(f"Mencari dataset di: {input_csv}")

    # load data
    df = pd.read_csv(input_csv)
    print(f"Ukuran awal: {df.shape}")

    # preprocessing
    # Hapus Kolom Identifier
    if 'Email No.' in df.columns:
        df = df.drop(columns=['Email No.'])

    # Penghapusan Common Words (Word Drop) pada kedua bagian (spam,ham)
    word_drop = [
        'the', 'to', 'and', 'for', 'of', 'a', 'you', 'in', 'on', 'is',
        'this', 'have', 'will', 'with', 'your', 'at', 'we', 's', 'are',
        'it', 'by', 'com', 'as', 'from', 'or', 'not', 'me', 'deal', 'if',
        'please', 'any', 'our', 'can', 'all', 'has', 'was', 'know', 'need',
        'an', 'new', 'may', 'up', 'should', 'do', 'get', 'out', 'see', 'no',
        'there', 'but', 'been', 'company', 'these', 'let', 'so', 'would', 'into',
        'us', 'information', 'they', 'message', 'day', 'time', 'my', 'one', 'what',
        'only', 'which', 'more', 'about', 'energy', 'question', 'call', 'mail', 'some',
        'original', 'email', 'sent', 'just', 'from', 'now', 'like', 'then', 'go', 'also',
        'report', 'here', 'back', 'good', 'said', 'project', 'make', 'group', 'receive',
        'start', 'business', 'system', 'request', 'work', 'development', 'management',
        'today', 'service', 'thanks', 'team', 'meeting', 'be', 'p', 'w', 's', 'b', 'meter',
        'price', 'contract'
    ]
    
    # Hapus kolom yang ada di list word_drop
    cols_to_drop = [col for col in word_drop if col in df.columns and col != 'Prediction']
    
    if cols_to_drop:
        df = df.drop(columns=cols_to_drop)
        print(f"Berhasil menghapus {len(cols_to_drop)} kata umum (common words).")
    
    # Simpan data yang sudah dipreprocessing
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(output_csv, index=False)
    print(f"Data disimpan di: {output_csv}")
    print(f"Ukuran akhir: {df.shape}")

if __name__ == "__main__":
    preprocess_data()