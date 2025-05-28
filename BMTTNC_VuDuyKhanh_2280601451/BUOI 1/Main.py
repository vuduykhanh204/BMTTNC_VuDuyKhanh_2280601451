from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while ( 1 == 1) :
    print("\n CHUONG TRINH QUAN LY SINH VIEN")
    print(******************************MENU***********************************)
    print(*****  1.Them sinh vien .                                    ********)
    print(*****  2.Cap nhat thong tin sinh vien boi ID************************ )
    print(*****  3.Xoa sinh vien boi ID                                        )
    print(****** 4. Tim kiem sinh vien theo ten *******************************)
    print(*****  5. Sap xep sinh vien theo diem trung diem ********************)
    print(****** 6. Sap xep sinh vien theo ten chuyen nganh *******************)
    print(****** 7.Hien thi danh sach sinh vien .***************************** )
    printf(***** 0.Thoat ******************************************************)
    print(*********************************************************************)
    key = int(intput("Nhap tuy chon:"))
    if (key == 1):
        print("\n1.Them sinh vien .")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong !")