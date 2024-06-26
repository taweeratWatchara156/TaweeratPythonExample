# พื้นที่สามเหลี่ยมใดๆ ที่มีด้านทั้งสาม (a,b และ c) ยาวไม่เท่ากัน สามารถคำนวณได้จากสูตร 
# พื้นที่สามเหลี่ยมใดๆ = รากที่สองของ(s(s-a)(s-b)(s-c))
# โดย s = (a+b+c)/2 

# จงเขียนโปรแกรมรับค่าความยาวด้านทั้งสามของสามเหลี่ยมใดๆ (เป็นจำนวนเต็ม) และคำนวณพื้นที่จากสูตรข้างต้น แสดงผลเป็นทศนิยม 2 ตำแหน่ง
import math

i1, i2, i3 = 0,0,0

i1 = int(input("ด้าน 1 : "))
i2 = int(input("ด้าน 2 : "))
i3 = int(input("ด้าน 3 : "))

s = (i1 + i2 + i3) / 2
area = math.sqrt(s * (s - i1) * (s - i2) * (s - i3))
print("พื้นที่สามเหลี่ยมเท่ากับ : ", "{:.2f}" .format(area))