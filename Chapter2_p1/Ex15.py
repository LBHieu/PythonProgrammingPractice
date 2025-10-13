M = float(input("Nhập khối lượng nước (gram): "))
delta_T = float(input("Nhập sự thay đổi nhiệt độ (độ Celsius): "))

if delta_T <= 0:
    print("Sự thay đổi nhiệt độ phải lớn hơn 0!")
else:
    C = 4.186  
    
    Q = M * C * delta_T
    
    Q_kWh = Q * 2.777e-7
    
    cost_per_kWh = 8.9  
    cost = Q_kWh * cost_per_kWh
    
    print(f"Tổng lượng nhiệt cần thiết: {Q:.2f} Joules")
    print(f"Chi phí để làm nóng nước: {cost:.2f} cent")