##soru1
"""
name=input("isminizi girin:")
surname=input("soyadınızı girin:")
city=input("yaşadığınız şehri girin:")
print(f"{name} {surname}, {city} şehrinde yaşıyorsunuz.")
"""
##soru2
"""
def indirim_hesapla(original,discount):
    return original*(100-discount)/100

ilktutar=int(input("ilk utarı girin:"))
indirim=int(input("indirim yüzdesini girin:"))
print(f"son tutar:{indirim_hesapla(ilktutar,indirim)}")
"""
##soru3
"""
dyılı=int(input("doğum yılınızı girin:"))
age=2026-dyılı
print(f"{age} yaşındasınız")
if(age >= 18):
    print("B sınıfı ehliyet alabilirsiniz")
else:
    print("B sınıfı ehliyet alamazsınız")
"""
##soru4

def harf_notu_hesapla(vize,final):
    ortalama=vize*0.4+final*0.6

    if ortalama >= 80:
        return "AA"
    elif ortalama >= 65:
        return "BA"
    elif ortalama >= 60:
        return "BB"
    elif ortalama >= 54:
        return "CB"
    elif ortalama >= 46:
        return "CC"
    elif ortalama >= 40:
        return "DC"
    elif ortalama >= 33:
        return "DD"
    else:
        return "FF"       
        
vize=int(input("vize notunuzu girin:"))
final=int(input("final notunuzu girin:"))   
print(f"harf notunuz: {harf_notu_hesapla(vize,final)}")       
        
