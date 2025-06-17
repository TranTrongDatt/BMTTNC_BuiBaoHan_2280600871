#Nhập số từ người dùng
so = int(input("\nVui lòng nhập 1 số nguyên: "))

#Kiểm tra xem số đó có phải số chẵn hay không
if so % 2 == 0:
    print(so, "LÀ SỐ CHẴN !!!")
else:
    print(so, "KHÔNG PHẢI LÀ SỐ CHẴN !!!")