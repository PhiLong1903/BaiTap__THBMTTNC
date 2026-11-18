from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while True:
    print("1. Nhập thông tin sinh viên")
    print("2. Hiển thị danh sách sinh viên")
    print("3. Tìm kiếm sinh viên")
    print("4. Cập nhật thông tin sinh viên")
    print("5. Xóa sinh viên")
    print("6. Thoát")
    choice = int(input("Chọn chức năng: "))
    if choice == 1:
        qlsv.nhapSinhVien()
    elif choice == 2:
        qlsv.hienThiDanhSachSinhVien()
    elif choice == 3:
        ID = int(input("Nhập ID sinh viên cần tìm: "))
        sv = qlsv.findByID(ID)
        if sv != None:
            print(f"ID: {sv._id}, Tên: {sv._name}, Giới tính: {sv._sex}, Ngành học: {sv._major}, Chuyên ngành: {sv._chuyenNganh}, Điểm TB: {sv._diemTB}, Học lực: {sv._hocLuc}")
        else:
            print("Không tìm thấy sinh viên có ID:", ID)
    elif choice == 4:
        ID = int(input("Nhập ID sinh viên cần cập nhật: "))
        qlsv.updateSinhVien(ID)
    elif choice == 5:
        ID = int(input("Nhập ID sinh viên cần xóa: "))
        qlsv.deleteById(ID)
    elif choice == 6:
        break
    else:
        print("Lựa chọn không hợp lệ!")