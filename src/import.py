import os
import sqlite3
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

DB_FILE = "kas_takmir.db"
PDF_FILE = "Laporan_Kas_Takmir.pdf"

#==========================
# Format & Input Rupiah
#==========================
def format_rupiah(angka):
    return f"Rp {angka:,}".replace(","",")

def input_rupiah(prompt):
    while True:
        try:
            nilai = input(prompt).strip()

            if not nilai:
                print("❌ Input tidak boleh kosong!")
                continue


            nilai_bersih = (
                nilai.replace("Rp", "")
                    .replace("rp", "")
                    .replace(".", "")
                    .replace(",", "")
                    .strip()
            )
            return int(nilai_bersih)
        except ValueError:
            print("❌ Masukkan angka yang benar! Contoh: 100.000")

#=========================
#DATABASE
#=========================
def get_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS kas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal TEXT,
            petugas TEXT,
            jenis TEXT,
            keterangan TEXT,
            jumlah INTEGER
        )
    """)
    conn.commit()
    conn.close()

#=======================
# Ambil UserName OS
#=======================
def get_petugas():
    try:
        user =  os.getlogin()
    except:
        user = os.environ.get("USERNAME") or os.environ.get("USER")
    
    return user.strip() if user else "Unknown"

def get_tanggal_sekarang():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")