from datetime import datetime
yıl,ay,gün,saat=map(int,input("sınav tarihinizi yıl ay gün saat formatında yazın: ").split(" "))

tarih=datetime(yıl,ay,gün,saat)

bugün=datetime.today()
fark=tarih-bugün
print(f"sınavınıza {fark.days} gün, {fark.seconds/3600} saat kaldı.")
