# ปีอธิกสุรทิน (leap year) เป็นปีที่มีการเพิ่มหนึ่งวัน ซึ่งสามารถคำนวณปีอธิกสุกรทินได้จากปีที่หารด้วย 4 ลงตัวเป็นส่วนมาก 

# ในปีอธิกสุรทินแต่ละปีนั้น เดือนกุมภาพันธ์มี 29 วัน แทนที่จะมี 28 วัน ซึ่งการเพิ่มวันเข้าไปในปฏิทินทุกสี่ปีเพื่อชดเชยตามข้อเท็จจริงที่ว่าระยะเวลา 365 วันนั้นสั้นกว่าปีสุริยคติเกือบ 1/4 วัน หรือ 6 ชั่วโมง

# ข้อยกเว้นบางประการต่อกฎนี้มีว่า เนื่องจากระยะเวลาของปีสุริยคติน้อยกว่า 365.25 วันเล็กน้อย จึงกำหนดให้ปีที่หารด้วย 100 ลงตัวมิใช่ปีอธิกสุรทิน แต่ยกเว้นปีที่หารด้วย 400 ลงตัว

# ตัวอย่างเช่น ค.ศ. 1600 และ 2000 เป็นปีอธิกสุรทิน แต่ ค.ศ. 1700, 1800 และ 1900 ไม่ใช่ 

# จงเขียนโปรแกรมรับเลขปี ค.ศ. เข้าไปเรื่อยๆ แล้วบอกว่าปีนั้นเป็นปีอธิกสุรทิน (leap year) หรือไม่ โดยโปรแกรมจะหยุดทำงานเมื่อผู้ใช้ป้อนเลข 0 หรือเลขจำนวนเต็มลบ


while(True) :
    year = int(input("Please enter a year! : "))
    if(year <= 0) : break;

    if(year % 4 == 0) : print("It's leap year!")
    else : print("It's not a leap year")