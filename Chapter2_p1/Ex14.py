import math

a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

if a <= 0 or b <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong = a / b if b != 0 else "Không thể chia cho 0"
    phan_con_lai = a % b if b != 0 else "Không thể chia cho 0"
    log10_a = math.log10(a)
    luy_thua = pow(a, b)

    print(f"Tổng của a và b: {tong}")
    print(f"Hiệu của a và b: {hieu}")
    print(f"Tích của a và b: {tich}")
    print(f"Thương của a chia cho b: {thuong}")
    print(f"Phần còn lại khi a dư chia cho b: {phan_con_lai}")
    print(f"Kết quả log10(a): {log10_a:.2f}")
    print(f"Kết quả a^b: {luy_thua}")