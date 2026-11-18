def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'
result = xoa_phan_tu(my_dict, key_to_remove)
if result: 
    print("Từ điển sau khi xóa phần tử có khóa", key_to_remove, "là:", result)
else:
    print("Không tìm thấy khóa", key_to_remove, "trong từ điển.")