data = input("Enter your email and something: ")
Start_position = data.find("@")                
End_position = data.find(" ", Start_position)  
host = data[Start_position +1 : End_position]
print(host)
