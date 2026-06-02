print("\n" + "="*50)
print("🎨  SELAMAT DATANG DI COLORUN  🎨")
print("="*50)
print("Temukan personal color (Winter, Summer, Autumn, Spring)\n")

print("1️⃣ Lihat warna pembuluh darah di pergelangan tangan:")
print("   [1] Biru / Ungu (cool tone)")
print("   [2] Hijau / Zaitun (warm tone)")
print("   [3] Campuran biru-hijau (neutral)")
pilihan1 = input("Pilih nomor (1/2/3): ").strip()
if pilihan1 == "1":
    undertone = "cool"
elif pilihan1 == "2":
    undertone = "warm"
else:
    undertone = "neutral"

print("\n2️⃣ Kontras antara rambut, kulit, dan mata:")
print("   [1] Tinggi (rambut gelap, kulit cerah)")
print("   [2] Sedang (cukup beda)")
print("   [3] Rendah (warna senada)")
pilihan2 = input("Pilih nomor (1/2/3): ").strip()
if pilihan2 == "1":
    kontras = "high"
elif pilihan2 == "2":
    kontras = "medium"
else:
    kontras = "low"

print("\n3️⃣ Warna mata dominan:")
print("   [1] Coklat tua / Hitam")
print("   [2] Biru / Hijau muda / Hazel terang")
print("   [3] Coklat madu / Keemasan")
pilihan3 = input("Pilih nomor (1/2/3): ").strip()
if pilihan3 == "1":
    warna_mata = "dark"
elif pilihan3 == "2":
    warna_mata = "light"
else:
    warna_mata = "warmBrown"

print("\n4️⃣ Reaksi kulit terhadap sinar matahari:")
print("   [1] Mudah terbakar (merah, susah coklat)")
print("   [2] Mudah kecoklatan (tan)")
print("   [3] Kadang terbakar, kadang coklat")
pilihan4 = input("Pilih nomor (1/2/3): ").strip()
if pilihan4 == "1":
    reaksi = "burn"
elif pilihan4 == "2":
    reaksi = "tan"
else:
    reaksi = "both"

def hitung_season(u, k, m, r):
    if u == "cool" and k == "high" and (m in ["dark","light"]) and r == "burn":
        return "Winter", "Dingin & Kontras Tinggi", "Elegan, tegas", "❄️"
    if u == "cool" and k in ["medium","low"] and m == "light" and r in ["burn","both"]:
        return "Summer", "Dingin & Lembut", "Kalem, romantis", "🌼"
    if u in ["warm","neutral"] and k in ["low","medium"] and m in ["warmBrown","dark"] and r in ["tan","both"]:
        return "Autumn", "Hangat & Natural", "Bumi, hangat", "🍂"
    if u in ["warm","neutral"] and k in ["high","medium"] and m in ["light","warmBrown"] and r in ["tan","both"]:
        return "Spring", "Hangat & Cerah", "Segar, ceria", "🌸"
    if u == "cool":
        return "Summer", "Cool tone (default)", "Lembut", "🌼"
    if u == "warm":
        return "Spring", "Warm tone (default)", "Cerah", "🌸"
    return "Autumn", "Netral hangat", "Alami", "🍂"

season, tipe, vibe, emoji = hitung_season(undertone, kontras, warna_mata, reaksi)

palet_nama_warna = {
    "Winter": ["Hitam pekat", "Putih bersih", "Merah darah", "Biru dongker", "Fuchsia"],
    "Summer": ["Lavender", "Dusty pink", "Baby blue", "Abu-abu mutiara", "Mint"],
    "Autumn": ["Coklat tua", "Hijau zaitun", "Mustard", "Bata merah", "Krem hangat"],
    "Spring": ["Coral", "Peach", "Hijau apel", "Kuning mentega", "Salmon"]
}

rekom_outfit = {
    "Winter": "Blazer hitam, kemeja putih, gaun merah marun, tas biru dongker.",
    "Summer": "Cardigan lavender, blus dusty pink, rok baby blue, aksesori perak.",
    "Autumn": "Jaket coklat suede, sweater hijau zaitun, scarf mustard.",
    "Spring": "Blazer coral, blus peach, dress hijau apel, sepatu kuning."
}

rekom_makeup = {
    "Winter": "Lipstik merah berry, eyeliner hitam tegas, blush pink dingin.",
    "Summer": "Lipstik pink muda, eyeshadow abu keunguan, blush peach lembut.",
    "Autumn": "Lipstik warna bata, blush oranye tua, highlighter emas.",
    "Spring": "Lipstik coral, eyeshadow emas muda, blush peach segar."
}

print("\n" + "="*50)
print("✨ HASIL ANALISIS PERSONAL COLOR ✨")
print("="*50)
print(f"🌈 Season Anda     : {season} {emoji}")
print(f"📝 Karakteristik   : {tipe} — {vibe}")
print("\n🎨 Rekomendasi warna:")
for warna in palet_nama_warna[season]:
    print(f"   • {warna}")
print(f"\n👗 Outfit yang cocok : {rekom_outfit[season]}")
print(f"💄 Makeup yang cocok : {rekom_makeup[season]}")
print("\n🌟 Gunakan warna-warna di atas untuk tampil maksimal!")
print("="*50)
