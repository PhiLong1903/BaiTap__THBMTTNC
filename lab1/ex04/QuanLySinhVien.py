from SinhVien import SinhVien


class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (sv._id > maxId):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        id = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập ngành học sinh viên: ")
        chuyenNganh = input("Nhập chuyên ngành: ")
        diemTB = float(input("Nhập điểm trung bình: "))
        sv = SinhVien(id, name, sex, major, chuyenNganh, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if (sv != None):
            sv._name = input("Nhập tên sinh viên: ")
            sv._sex = input("Nhập giới tính sinh viên: ")
            sv._major = input("Nhập ngành học sinh viên: ")
            sv._chuyenNganh = input("Nhập chuyên ngành: ")
            sv._diemTB = float(input("Nhập điểm trung bình: "))
            self.xepLoaiHocLuc(sv)
        else:
            print("Không tìm thấy sinh viên có ID:", ID)

    def softById(self):
        self.listSinhVien.sort(key=lambda sv: sv._id, reverse=False)

    def softByName(self):
        self.listSinhVien.sort(key=lambda sv: sv._name, reverse=False)

    def softByDiemTB(self):
        self.listSinhVien.sort(key=lambda sv: sv._diemTB, reverse=True)

    def xepLoaiHocLuc(self, sv):
        if (sv._diemTB >= 9.0):
            sv._hocLuc = "Xuất sắc"
        elif (sv._diemTB >= 8.0):
            sv._hocLuc = "Giỏi"
        elif (sv._diemTB >= 7.0):
            sv._hocLuc = "Khá"
        elif (sv._diemTB >= 5.0):
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if (sv._id == ID):
                return sv
        return None

    def findByName(self, name):
        for sv in self.listSinhVien:
            if (sv._name.lower() == name.lower()):
                return sv
        return None

    def deleteById(self, ID):
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            print("Đã xóa sinh viên có ID:", ID)
        else:
            print("Không tìm thấy sinh viên có ID:", ID)

    def hienThiDanhSachSinhVien(self):
        print("Danh sách sinh viên:")
        for sv in self.listSinhVien:
            print(f"ID: {sv._id}, Tên: {sv._name}, Giới tính: {sv._sex}, Ngành học: {sv._major}, Chuyên ngành: {sv._chuyenNganh}, Điểm TB: {sv._diemTB}, Học lực: {sv._hocLuc}")

    def getListSinhVien(self):
        return self.listSinhVien
