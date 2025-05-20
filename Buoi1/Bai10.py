def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

# Sử dụng hàm và in kết quả
input_string = input("\nMời nhập chuỗi cần đảo ngược: ")
print("\n\t   --- Chuỗi đảo ngược --- \n", dao_nguoc_chuoi(input_string))