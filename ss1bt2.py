print("--- HỆ THỐNG NHẬP CHỈ SỐ SỨC KHỎE ---")

name_patient = input("Nhập tên bệnh nhân: ")

# Ép kiểu dữ liệu sang float
weight = float(input("Nhập cân nặng bệnh nhân: "))

print("--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")

print("Bệnh nhân:", name_patient)
print("Cân nặng:", weight)

# Kiểm tra kiểu dữ liệu
print("Kiểu dữ liệu của cân nặng là:", type(weight))

#Hàm input() trong Python luôn trả về dữ liệu kiểu chuỗi (str).
#Người dùng nhập 65.5 nhưng chương trình lưu thành "65.5".
#Vì không ép kiểu sang float nên biến weight có kiểu:
#<class 'str'>
#Dữ liệu dạng chuỗi không dùng được cho các phép tính y khoa như BMI hoặc tính toán số học.