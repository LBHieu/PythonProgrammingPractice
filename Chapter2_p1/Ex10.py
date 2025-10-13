import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

length = float(input("Nhập chiều dài: "))
width = float(input("Nhập chiều rộng: "))
# height = float(input("Nhập chiều cao: "))

# x = [0, length, length, 0, 0]
# y = [0, 0, width, width, 0]
# z = [0, 0, 0, 0, height]

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot3D(x, y, z, 'b-')  

# ax.set_xlabel('Chiều dài')
# ax.set_ylabel('Chiều rộng')
# ax.set_zlabel('Chiều cao')
# plt.title('Đường nối các điểm trong không gian 3D')

# plt.show()

print(f"Diện tích hình chữ nhật là: {length * width:.2f}")