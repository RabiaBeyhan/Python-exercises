


girdi=input("bir sayı girin: ")
a=False
while a==False:
    try:
        girdi=float(girdi)
    except:
        print("geçersiz bir veri")
        girdi=input("lütfen geçerli bir sayı girin: ")
    else:
        a=True
    

