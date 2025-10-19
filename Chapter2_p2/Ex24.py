def printValue(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
       print("chuỗi dài hơn:", s1)
    elif len2 > len1:
       print("Chuỗi dài hơn:",s2)
    else:
       print(s1)
       print(s2)
from So_Sanh_Chuoi import *
st1 = input("Nhập vào chuỗi thứ nhất:")
st2 = input("Nhập vào chuỗi thứ hai:")
printValue(st1, st2)
