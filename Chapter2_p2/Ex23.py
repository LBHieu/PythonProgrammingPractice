def Check_chan(x):
    if x % 2 == 0:
        print(x, "là số chẵn")
    else:
        print(x, "là số lẻ")


from Kiem_tra import *
if __name__ == "__main__":
    n = int(input("Nhập vào một số để kiểm tra: "))
    Check_chan(n)