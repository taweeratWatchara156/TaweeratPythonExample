# ลิฟท์โกลาหล

# โรงแรมแห่งหนึ่งมีลิฟธ์อยู่ 5 ตัว ลิฟท์แต่ละตัวจะอยู่ชั้นต่างๆ ตั้งแต่ 1 - 25 ต่างกันไปที่เกิดจากการสุ่ม

# คำสั่งสุ่ม import random เรียกใช้โดย random.randint(x,y)

# ผู้ใช้ลิฟต์จะกดลิฟต์ด้วยการระบุชั้นที่ผู้ใช้ลิฟท์กด เช่น กด 20 แสดงว่าอยู่ชั้น 20
# จากนั้นลิฟท์ตัวที่อยู่ใกล้ชั้นนั้นที่สุดจะเคลื่อนที่มารับผู้กด ดังตัวอย่าง

# จงเขียนโปรแกรมสุ่มเลขที่อยู่ของลิฟท์ทั้ง 5 ตัว และให้ผู้ใช้ป้อนชั้นที่กด แล้วแสดงผลลัพธ์เป็นลิฟท์ตัวที่ใกล้ที่สุดที่จะเคลื่อนที่มารับ
# หากลิฟท์ตัวที่ใกล้ที่สุดมีเหมือนกันหลายตัวให้เลือกตัวที่มีค่าน้อยที่สุด

import random

min = 9999
result = 0
elavator = {'1':0, '2':0, '3':0, '4':0, '5':0}

for i in range(len(elavator)) :
    i += 1
    elavator[str(i)] = random.randint(1, 25)

print(elavator)
level = int(input("Please enter level u want to go : "))

for i in range(len(elavator)) :
    i += 1
    if(elavator[str(i)] >= level) :
        result = elavator[str(i)] - level;
    else : result = level - result;
    if(result < min) : min = i;


print("elavator number ",min , " is coming to you!")

    


