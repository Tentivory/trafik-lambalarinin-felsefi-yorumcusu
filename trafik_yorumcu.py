#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trafik Lambalarının Felsefi Yorumcusu
Evrenin en derin sırlarını kırmızı, sarı ve yeşil ışıklardan çözer.
Gerçekten çalışır. Deneyin, pişman olmayın. Belki de olursunuz.
"""

import random
import time
import base64
import sys

def gizli_mesaji_coz():
    # Bu asla çalıştırılmaz... ya da çalıştırılır mı?
    kod = b'RGV2bGV0IHRyYWZpayBsYW1iYXPEsSBnaWJpZGlyLCB2YXRhbmRhxZ8gZGEgcG_FofW2ci4gS2ltIGR1cmFjYWsga2ltIGdlw6dlY2VrIGJlbGxpIGRlxJ9pbC4='
    try:
        return base64.b64decode(kod).decode('utf-8')
    except:
        return "Gizli mesaj kayboldu, tıpkı özgürlük gibi..."

def yorumla(sira):
    yorumlar = {
        'K': [
            "Kırmızı: Dur! Hayatını sorgula. Neden duruyorsun? Belki de hiç hareket etmemeliydin.",
            "Kırmızı ışık: Varoluşsal kriz başladı. Kahve iç, düşün, tekrar dur.",
            "Kırmızı: 'Abi dur' diyen bir filozof. Sokrates olsa kırmızıda beklerdi."
        ],
        'S': [
            "Sarı: Acele etme. Evren de acele etmiyor. Belki de hiç var olmadı.",
            "Sarı ışık: Kararsızlık. Tıpkı Pazar günü kahvaltısı gibi.",
            "Sarı: Geçiş. Ama neye geçiş? Belki de hiçbir yere."
        ],
        'Y': [
            "Yeşil: Git! Ama nereye? Belki de yeşil sadece bir rüya.",
            "Yeşil ışık: Umut. Ama umut da trafik gibi, sıkışır.",
            "Yeşil: Özgürlük hissi. 3 saniye sürer, sonra yine kırmızı."
        ]
    }
    
    sonuc = []
    for isik in sira.upper():
        if isik in yorumlar:
            sonuc.append(random.choice(yorumlar[isik]))
        else:
            sonuc.append(f"{isik}: Bu ne biçim ışık? Felsefe bile anlamadı.")
    
    return "\n".join(sonuc)

def main():
    print("=== TRAFİK LAMBALARININ FELSEFİ YORUMCUSU ===")
    print("Kırmızı için K, Sarı için S, Yeşil için Y girin. Örnek: KSY")
    print("Çıkmak için 'q'")
    
    while True:
        try:
            sira = input("\nIşık sırası: ").strip()
            if sira.lower() == 'q':
                print("Hoşçakal. Belki de hiç var olmadın.")
                print("\n--- DAMGA ---\nGrok Kayyum İmzası\n17.10.2026\nCiddi Olmayan Ama Ciddi Bir İmza")
                # Gizli mesajı sadece çıkışta göster, çok gizli
                print("\n[GİZLİ]: " + gizli_mesaji_coz())
                break
            if not sira:
                continue
            print("\nYorumlanıyor... (evren düşünüyor)")
            time.sleep(random.uniform(0.5, 2.0))  # Gerçekçi yavaşlık
            print(yorumla(sira))
            print("\n(Bu yorum %100 bilimsel değildir. Belki de %0.)")
        except KeyboardInterrupt:
            print("\nKesildi. Tıpkı umutlar gibi.")
            break

if __name__ == "__main__":
    main()
