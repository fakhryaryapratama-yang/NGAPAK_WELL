#  ==================
# Export PDF
# ===================
def export_pdf():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT tanggal, jenis, jumlah, keterangan, petugas  FROM kas")
    rows = cur.fetchall()
    conn.close()
    
    if note rows:
        print("❌ Tidak ada data untuk diekspor.")
        return
    
    c = canvas.Canvas(FILE_PDF, pagesize=A4)
    width, height = A4
    y = height - 50