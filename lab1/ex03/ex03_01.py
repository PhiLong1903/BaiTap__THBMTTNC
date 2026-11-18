def tinh_tong_chan (n):
    tong = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            tong += i
    return tong
input_list =        input("Nhập một danh sách các số nguyên, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(",")))

tong_chan = sum(tinh_tong_chan(num) for num in numbers)
print("Tổng các số chẵn trong danh sách là:", tong_chan)
