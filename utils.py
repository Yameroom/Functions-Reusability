#rumus konversi suhu
def ctof(c):
    return (c * 9/5) + 32
def ctok(c):
    return c + 273.15
def ftoc(f):    
    return (f - 32) * 5/9   
def ftok(f):
    return (f - 32) * 5/9 + 273.15 
def ktoc(k):
    return k - 273.15   
def ktof(k):
    return (k - 273.15) * 9/5 + 32

#ini nih wak fungsi utamanya
def konversi_suhu(nilai, dari, ke):
    if dari not in ['c', 'f', 'k'] or ke not in ['c', 'f', 'k']:
        return "Satuan suhu tidak valid. Gunakan C, F, atau K."
    
    if nilai < 0 and dari == 'k':
        return "Nilai suhu Kelvin tidak boleh bernilai negatif."
    
    if dari == "c" and ke == "f":
        return ctof(nilai)
    elif dari == "c" and ke == "k":
        return ctok(nilai)
    elif dari == "f" and ke == "c":
        return ftoc(nilai)
    elif dari == "f" and ke == "k":
        return ftok(nilai)
    elif dari == "k" and ke == "c":
        return ktoc(nilai)
    elif dari == "k" and ke == "f":
        return ktof(nilai)
    elif dari == ke:
        return nilai
    else:
        return "Terjadi kesalahan dalam konversi suhu."
    