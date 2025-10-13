n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    sum_result = n * (n + 1) / 2

    print(f"Tổng của các số nguyên dương từ 1 đến {n} là: {sum_result:.2f}")