import re
import json
import os
import pandas as pd

def cleansing_kronologi(text):
    pattern_spasi_ekstra = "\\s+"
    pattern_utama_lanjutan = f"{pattern_spasi_ekstra}"
    cleaned_text = re.sub(pattern_utama_lanjutan, ' ', text)
    return cleaned_text

def cleansing(text):
    pattern_angka = "[0-9]"
    pattern_new_line = "\\n"
    pattern_bukan_kata = "[^ \w]"
    pattern_tambahan = "(S/D |DARI |TANGGAL |JANUARI |FEBRUARI |\w*BER |HARI |SENIN|SELASA|RABU|KAMIS|JUMAT|SABTU|MINGGU|SEKITAR |JAM|PUKUL|PADA )"
    pattern_spasi = " "
    pattern_spasi_lebih = "* "
    pattern_utama = f"{pattern_new_line}|({pattern_spasi}({pattern_bukan_kata}|{pattern_angka}){pattern_spasi_lebih})|({pattern_bukan_kata}|{pattern_angka})|{pattern_tambahan}"
    # pattern = r'\\n|( (\\n|[^ \w]|[0-9])* )|([^ \w]|[0-9])|(S/D |DARI |TANGGAL |JANUARI |FEBRUARI |\w*BER |HARI |SENIN|SELASA|RABU|KAMIS|JUMAT|SABTU|MINGGU|SEKITAR |JAM|PUKUL|PADA )'
    # [!@#$%^&*()_+{}\[\]:;"\'<>,.?/\|\\`~-]|[0-9]
    
    cleaned_text = re.sub(pattern_utama, ' ', text)
    cleaned_text = cleansing_kronologi(cleaned_text)
    cleaned_text = cleaned_text.lower()

    return cleaned_text

def informal_to_formal_indo(text):
    with open('data\combined_slang_words.txt') as f:
        data0 = f.read() 
    # print("Data type before reconstruction : ", type(data0))
    formal_indo = json.loads(data0)
    # print("Data type after reconstruction : ", type(formal_indo))
    res = " ".join(formal_indo.get(ele, ele) for ele in text.split())
    return res