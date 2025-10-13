import math

r = float(input("Nhập bán kính (r): "))
h = float(input("Nhập chiều cao (h): "))

V = math.pi * r**2 * h

print(f"Thể tích của hình trụ là: {V:.2f}")