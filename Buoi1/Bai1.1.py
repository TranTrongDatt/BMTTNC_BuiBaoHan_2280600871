def tinh_tong_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

#Nhập ds từ ng dùng và xử lý chuỗi
nhap_list = input("\nNhập ds các số, cách nhau bằng dấU phẩy: ")
so = list(map(int, nhap_list.split(',')))

# Sử dụng hàm và in kết quả
tong_chan = tinh_tong_chan(so)
print("\n\t   TỔNG CÁC SỐ CHẴN TRONG DANH SÁCH   \n", tong_chan)