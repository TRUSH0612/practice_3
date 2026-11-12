x=0
while x==0:
    try:
        pred_val=int(input("Введите показатели счётчика за прошлый месяц:  "))
        tek_val=int(input("Введите показатели счётчика за текущий месяц: "))
        if pred_val>9999 or tek_val>9999:
            print("Введите значение меньше 9999")
            x=0
        else:
         if pred_val>tek_val:#если обнуляется счётчик 
            tek_val+=10000
        x+=1
           
    except:#если ввели строку
        print("Напиши  ЦИФРЫ")
used=tek_val-pred_val
chast=0 #между 300 и 600
chast1=0 #между 600 и 800
chast2=0 #после 800
if used>300:
    chast=used-300
    if used>600:
        chast1=used-600
        chast=300
        if used>800:
            chast2=used-800
            chast1=200
cen = 21 + chast*0.06 + chast1*0.04 + chast2*0.025 #зафиксированная цена за кадый избыток по частям
if used!=0:#средняя цена 
    avg=cen/used
    avg=round(avg, 2)
else:
    avg="Зафиксированная цена"
print("Предыдущее: ", pred_val, "Текущее: ", tek_val, "Исполльзованно: ", used, "К оплате: ", cen, "Ср. цена за m^3: ", avg)

            





