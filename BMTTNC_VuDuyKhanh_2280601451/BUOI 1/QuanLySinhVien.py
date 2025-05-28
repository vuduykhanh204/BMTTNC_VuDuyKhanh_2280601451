from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien()> 0):
            maxId = self.listSinhVien[0].id
            for sv in self.listSinhVien:
                if (maxId < sv.id):
                    maxId = sv._id
            maxId = maxId + 1
            return maxId
        def soLuongSinhVien(self) :
            return self .listSinhVien._len_()
        def nhapSinhVien(self):
            svId = self.generateID()
            name = input("Nhap ten sinh vien:")
            sex = input ("Nhap gioi tinh sinh vien :")
            major = input("Nhap chuyen nganh cua sinh vien :")
            diemTB = float(input("Nhap diem cua sinh vien : "))
            self.xepLoaiHocLuc(sv)
            self.listSinhVien.append(sv)
            def updateSinhVien (self ,ID): 
                sv : SinhVien = self.findByID(ID)
                if (sv != None):
                    name = input("Nhap ten sinh vien :")
                    sex = input("Nhap gioi tinh sinh vien")
                    major = int (input("Nhap gioi tinh sinh vien "))
                    diemTB = float(input("Nhap diem cua sinh vien:"))
                    sv._name = name
                    sv._sex = sex
                    sv.major = major
                    sv._diemTB = diemTB
                    self.xepLoaiHocLuc(sv)   
                     