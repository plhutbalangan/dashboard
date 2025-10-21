import subprocess, os, datetime

print("🔄 Mengambil data terbaru dari Kemenag...")
subprocess.run(['python', 'ambil_data_balangan_final.py'], check=True)

print("📤 Mengunggah ke GitHub...")
os.system('git add static/data_balangan.json')
os.system(f'git commit -m "Auto update data Balangan {datetime.datetime.now()}"')
os.system('git push origin main')

print("✅ Data berhasil diupdate dan dikirim ke GitHub!")
