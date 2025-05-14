def dao_nguoc_list(lst):
    return lst[::-1]

#Nhập ds từ ng dùng và xử lý chuỗi
nhap_list = input("\nNhập ds các số, cách nhau bằng dấU phẩy: ")
so = list(map(int, nhap_list.split(',')))

# Sử dụng hàm và in kết quả
list_dao_nguoc = dao_nguoc_list(so)
print("\n\t   LIST SAU KHI ĐẢO NGƯỢC   \n", list_dao_nguoc)
