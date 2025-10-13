import math

price = float(input("Nhập giá trị món ăn: "))
tax = price*(18/100)
tip = price*(5/100)
total = price + tax + tip

print(f"Giá trị món ăn: {price:.2f}")
print(f"Thuế: {tax:.2f}")
print(f"Tiền boa: {tip:.2f}")
print(f"Tổng cộng: {total:.2f}")

