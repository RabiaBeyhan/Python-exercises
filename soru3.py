import random
sayı=random.randint(0,100)

tahmin=int(input("0 ile 100 arasında bir sayı tahmin edin: "))
while (tahmin!=sayı):
    if(tahmin>sayı):
        tahmin=int(input("Aşağı in: "))
        continue
    else:
        tahmin=int(input("Yukarı çık: "))
print(f"doğru tahmin, sayı= {tahmin}")