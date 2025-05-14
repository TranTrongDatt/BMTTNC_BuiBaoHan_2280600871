def tao_tuple_tu_list(lst):
    return tuple(lst)

#Nhập ds từ ng dùng và xử lý chuỗi
nhap_list = input("\nNhập ds các số, cách nhau bằng dấU phẩy: ")
so = list(map(int, nhap_list.split(',')))

my_tuple = tao_tuple_tu_list(so)
print("List: ", so)
print("Tuple từ LIST: ", my_tuple)