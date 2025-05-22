from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\n\t\t\t\t~~~ CHUONG TRINH QUAN LY SINH VIEN ~~~")
    print("\n\t\t************************** MENU ***************************")
    print("\t\t**      1. Them sinh vien.                               **")
    print("\t\t**      2. Cap nhat thong tin sinh vien boi ID.          **")
    print("\t\t**      3. Xoa sinh vien boi ID.                         **")
    print("\t\t**      4. Tim kiem sinh vien theo ten.                  **")
    print("\t\t**      5. Sap xep sinh vien theo diem tb.               **")
    print("\t\t**      6. Sap xep sinh vien theo ten chuyen nganh.      **")
    print("\t\t**      7. Hien thi danh sach sinh vien.                 **")
    print("\t\t**      0. Thoat chuong trinh.                           **")
    print("\n\t\t***********************************************************")
    
    key = int(input("\n->Nhap lua chon: "))
    if (key == 1):
        print("\n\t\t\t\t~~~ NHAP SINH VIEN MOI ~~~ ")
        qlsv.nhapSinhVien()
        print("\n\t\t\t\t!!! Da them sinh vien thanh cong !!!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n\t\t\t\t~~~ CAP NHAT THONG TIN SINH VIEN ~~~ ")
            print("\n->Nhap ID sinh vien can cap nhat: ")
            try:
                ID = int(input())
                qlsv.updateSinhVien(ID)
            except ValueError:
                print("\n\t\t!!! Vui long nhap ID la so nguyen !!!")
        else:
            print("\n\t\t!!! DANH SACH SINH VIEN TRONG !!!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n\t\t\t\t~~~ XOA SINH VIEN ~~~ ")
            print("\n->Nhap ID sinh vien can xoa: ")
            try:
                ID = int(input())
                if (qlsv.deleteById(ID)):
                    print("\n\t\t\t\t Sinh vien co ID = ", ID, " da bi xoa !!!")
                else:
                    print("\n\t\t!!! Sinh vien co ID = ", ID, "khong ton tai !!!")
            except ValueError:
                print("\n\t\t!!! Vui long nhap ID la so nguyen !!!")
        else:
            print("\n\t\t!!! DANH SACH SINH VIEN TRONG !!!")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n\t\t\t\t~~~ TIM KIEM SINH VIEN THEO TEN ~~~ ")
            name = input("\n->Nhap ten sinh vien can tim: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\n\t\t!!! DANH SACH SINH VIEN TRONG !!!")
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n\t\t\t\t~~~ SAP XEP SINH VIEN THEO DIEM TB (GPA) ~~~ ")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\n\t\t!!! DANH SACH SINH VIEN TRONG !!!")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n\t\t\t\t~~~ SAP XEP SINH VIEN THEO TEN CHUYEN NGANH ~~~ ")
            qlsv.sortByMajor()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\n\t\t!!! DANH SACH SINH VIEN TRONG !!!")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n\t\t\t\t~~~ HIEN THI DANH SACH SINH VIEN ~~~ ")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\n\t\t!!! DANH SACH SINH VIEN TRONG !!!")
    elif (key == 0):
        print("\n\t\t\t\t!!! Cam on ban da su dung chuong trinh !!!")
        break
    else:
        print("\n\t\t!!! Lua chon khong hop le !!!")
        print("\n\t\t!!! Vui long nhap lai !!!")