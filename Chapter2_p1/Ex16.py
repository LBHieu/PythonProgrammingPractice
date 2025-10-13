import math

d = float(input("Nhập độ cao (m): "))

v_i = 0  
a = 9.8  

v_f = math.sqrt(v_i**2 + 2 * a * d)

print(f"Vận tốc khi chạm đất: {v_f:.2f} m/s")