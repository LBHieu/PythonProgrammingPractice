import math

a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))
angle_A = float(input("Nhập góc A (radian): "))
angle_B = float(input("Nhập góc B (radian): "))
angle_C = float(input("Nhập góc C (radian): "))

S1 = 0.5 * a * b * math.sin(angle_C)
S2 = 0.5 * a * c * math.sin(angle_B)
S3 = 0.5 * b * c * math.sin(angle_A)

print(f"Diện tích tam giác (theo ab sin C): {S1:.2f}")
print(f"Diện tích tam giác (theo ac sin B): {S2:.2f}")
print(f"Diện tích tam giác (theo bc sin A): {S3:.2f}")