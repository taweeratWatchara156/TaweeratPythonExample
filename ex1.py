# จงเขียนโปรแกรมรับค่าปี ค.ศ. จากนั้นให้แสดงผลปี พ.ศ.
# และผลรวมของตัวเลขแต่ละหลักของปี ค.ศ. และ พ.ศ. ดังตัวอย่างต่อไปนี้


yeark = input("ใส่ปี คศ : ")
yearp = int(yeark) + 543

sum1, sum2 =  0, 0

print("พศ ", yeark, " = คศ ", yearp)

for i in range(len(yeark)) :
    sum1 += int(yeark[i])

print("ผลรวมเลขของปี คส : ", sum1)

yearp = str(yearp)
for i in range(len(str(yearp))) :
    sum2 += int(yearp[i])

print("ผลรวมเลขของปี พศ : ", sum2)