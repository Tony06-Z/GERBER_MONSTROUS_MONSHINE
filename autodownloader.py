import os
import sys
import time
import urllib.request
import json

# =====================================================================
# CONFIGURATION VAULT
# =====================================================================
REPO_OWNER = "openai"
REPO_NAME = "math"
TARGET_DIR = "openai_math_vault"

# Base URL untuk GitHub REST API (Mengambil daftar file secara rekursif)
API_URL = f"https://github.com{REPO_OWNER}/{REPO_NAME}/git/trees/main?recursive=1"

# Headers standar agar tidak diblokir oleh GitHub Rate Limit
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/vnd.github.v3+json"
}

def fetch_repository_tree():
    """Mengambil struktur seluruh folder dan berkas dari server GitHub"""
    print(f"[AUTO-FETCH] Menghubungkan ke API GitHub untuk repo {REPO_OWNER}/{REPO_NAME}...")
    req = urllib.request.Request(API_URL, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data.get("tree", [])
    except Exception as e:
        print(f"❌ Gagal mengambil struktur repo dari API: {e}")
        sys.exit(1)

def download_file_stream(download_url, local_path):
    """Mengunduh berkas menggunakan sistem stream chunk untuk hemat memori"""
    req = urllib.request.Request(download_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            # Unduh per blok 512 Kilobyte
            while True:
                chunk = response.read(512 * 1024)
                if not chunk:
                    break
                out_file.write(chunk)
        return True
    except Exception as e:
        print(f"\n❌ Eror saat mengunduh berkas {os.path.basename(local_path)}: {e}")
        return False

def main():
    print("=== STARTING TOTAL AUTOMATED DOWNLOADER FOR OPENAI/MATH ===")
    
    # 1. Ambil semua daftar file
    file_tree = fetch_repository_tree()
    if not file_tree:
        print("❌ Struktur file kosong atau API limit tercapai.")
        return
        
    total_items = len([item for item in file_tree if item["type"] == "blob"])
    print(f"-> Terdeteksi total {total_items} berkas siap diunduh.")
    
    # 2. Iterasi dan unduh secara otomatis
    downloaded_count = 0
    start_time = time.time()
    
    for item in file_tree:
        path = item["path"]
        item_type = item["type"]
        
        # Buat jalur folder lokal yang sesuai dengan struktur aslinya
        local_path = os.path.join(TARGET_DIR, path)
        
        if item_type == "tree":
            # Jika tipe struktur adalah folder, otomatis buat foldernya
            os.makedirs(local_path, exist_ok=True)
        
        elif item_type == "blob":
            # Jika tipe struktur adalah berkas, siapkan unduhan
            downloaded_count += 1
            
            # FITUR AUTO-RESUME: Jika berkas sudah ada secara lokal, bypass langsung!
            if os.path.exists(local_path):
                print(f"[{downloaded_count}/{total_items}] ⏩ Skipped (Sudah ada): {path}")
                continue
                
            # Pastikan folder pembungkus berkas ini sudah dibuat
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            
            # Konstruksi URL unduhan mentah (Raw file)
            raw_url = f"https://githubusercontent.com{REPO_OWNER}/{REPO_NAME}/main/{path}"
            
            print(f"[{downloaded_count}/{total_items}] 📥 Downloading: {path} ...", end="", flush=True)
            
            success = download_file_stream(raw_url, local_path)
            if success:
                print(" DONE ✅")
            else:
                print(" FAILED ❌")
                
            # Jeda 0.1 detik agar koneksi tetap stabil dan tidak dianggap serangan DDoS
            time.sleep(0.1)

    duration = (time.time() - start_time) / 60
    print("\n=====================================================================")
    print(f"🎉 DOWNLOAD PIPELINE SELESAI DALAM {duration:.2f} MENIT!")
    print(f"Seluruh data disimpan di folder lokal: ./{TARGET_DIR}/")
    print("=====================================================================")

if __name__ == "__main__":
    main()
