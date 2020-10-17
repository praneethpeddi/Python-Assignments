student_data = [
    {
        "student_name": "Vachan ram",
        "marks": [25, 25, 51, 5, 18, 80, 31, 80, 83, 25, 38, 55, 88, 64, 91]
    },
    {
        "student_name": "Saketh ram",
        "marks": [32, 19, 33, 54, 42, 14, 73, 40, 7, 51, 10, 91, 9, 29, 11]
    },
    {
        "student_name": "Sanketh",
        "marks": [93, 82, 28, 91, 99, 45, 47, 13, 1, 89, 91, 65, 100, 3, 47]
    },
    {
        "student_name": "Hruday",
        "marks": [99, 8, 1, 18, 10, 20, 30, 8, 46, 83, 27, 18, 50, 34, 10]
    },
    {
        "student_name": "Samvad",
        "marks": [11, 19, 100, 85, 95, 58, 41, 67, 12, 22, 81, 30, 71, 5, 50]
    },
    {
        "student_name": "Knowledge",
        "marks": [95, 72, 72, 42, 3, 18, 13, 23, 25, 44, 63, 70, 94, 71, 24]
    },
    {
        "student_name": "Saketh ram",
        "marks": [33, 6, 13, 32, 78, 27, 100, 17, 71, 56, 68, 52, 65, 82, 67]
    }
]

book_index = [
    {
        "book_id": 5678923,
        "marks": [25, 25, 51, 5, 18, 80, 31, 80,
                  83, 25, 38, 55, 88, 64, 91]
    },
    {
        "book_id": 9876532579,
        "marks": [32, 19, 33, 54, 42, 14, 73, 40, 7,
                  51, 11, 91, 9, 29, 11]
    },
    {
        "book_id": 91278364,
        "marks": [93, 82, 28, 91, 99, 45, 47, 13,
                  1, 89, 91, 65, 100, 3, 47]
    },
    {
        "book_id": 12369863,
        "marks": [99, 8, 1, 18, 10, 20, 30, 8, 46,
                  83, 27, 18, 50, 34, 10]
    },
    {
        "book_id": 32578934,
        "marks": [11, 19, 100, 85, 95, 58, 41, 67,
                  12, 22, 81, 30, 71, 5, 50]
    },
    {
        "book_id": 35782345,
        "marks": [95, 72, 72, 42, 3, 18, 13, 23,
                  25, 44, 63, 70, 94, 71, 24]
    },
    {
        "book_id": 87512321,
        "marks": [33, 6, 13, 32, 78, 27, 100, 17,
                  71, 56, 68, 52, 65, 82, 67]
    }
]


def get_all_decimal_val():
    list_of_marks_from_stu = [i['marks'] for i in student_data]
    list_of_marks_from_book_ids = [j['marks'] for j in book_index]
    list_of_book_ids = [j['book_id'] for j in book_index]
    return list_of_marks_from_stu, list_of_marks_from_book_ids, list_of_book_ids


def get_all_hex_val(del_marks):
    li_of_hex_val = []
    for i in del_marks:
        for j in i:
            hex_val = hex(j)
            li_of_hex_val.append(hex_val)
    return li_of_hex_val


def get_all_hex_val_of_book_id(book_ids):
    list_of_hex_val_of_book_id = []
    for i in book_ids:
        hex_value = hex(i)
        list_of_hex_val_of_book_id.append(hex_value)
    return list_of_hex_val_of_book_id


def validation_hex(input1, input2, input3):
    lis_to_verify1 = ['0x19', '0x19', '0x33', '0x5', '0x12', '0x50', '0x1f', '0x50', '0x53', '0x19', '0x26', '0x37',
                      '0x58', '0x40', '0x5b', '0x20', '0x13', '0x21', '0x36', '0x2a', '0xe', '0x49', '0x28', '0x7',
                      '0x33', '0xa', '0x5b', '0x9', '0x1d', '0xb', '0x5d', '0x52', '0x1c', '0x5b', '0x63', '0x2d',
                      '0x2f', '0xd', '0x1', '0x59', '0x5b', '0x41', '0x64', '0x3', '0x2f', '0x63', '0x8', '0x1', '0x12',
                      '0xa', '0x14', '0x1e', '0x8', '0x2e', '0x53', '0x1b', '0x12', '0x32', '0x22', '0xa', '0xb',
                      '0x13', '0x64', '0x55', '0x5f', '0x3a', '0x29', '0x43', '0xc', '0x16', '0x51', '0x1e', '0x47',
                      '0x5', '0x32', '0x5f', '0x48', '0x48', '0x2a', '0x3', '0x12', '0xd', '0x17', '0x19', '0x2c',
                      '0x3f', '0x46', '0x5e', '0x47', '0x18', '0x21', '0x6', '0xd', '0x20', '0x4e', '0x1b', '0x64',
                      '0x11', '0x47', '0x38', '0x44', '0x34', '0x41', '0x52', '0x43']
    lis_to_verify2 = ['0x19', '0x19', '0x33', '0x5', '0x12', '0x50', '0x1f', '0x50', '0x53', '0x19', '0x26', '0x37',
                      '0x58', '0x40', '0x5b', '0x20', '0x13', '0x21', '0x36', '0x2a', '0xe', '0x49', '0x28', '0x7',
                      '0x33', '0xb', '0x5b', '0x9', '0x1d', '0xb', '0x5d', '0x52', '0x1c', '0x5b', '0x63', '0x2d',
                      '0x2f', '0xd', '0x1', '0x59', '0x5b', '0x41', '0x64', '0x3', '0x2f', '0x63', '0x8', '0x1', '0x12',
                      '0xa', '0x14', '0x1e', '0x8', '0x2e', '0x53', '0x1b', '0x12', '0x32', '0x22', '0xa', '0xb',
                      '0x13', '0x64', '0x55', '0x5f', '0x3a', '0x29', '0x43', '0xc', '0x16', '0x51', '0x1e', '0x47',
                      '0x5', '0x32', '0x5f', '0x48', '0x48', '0x2a', '0x3', '0x12', '0xd', '0x17', '0x19', '0x2c',
                      '0x3f', '0x46', '0x5e', '0x47', '0x18', '0x21', '0x6', '0xd', '0x20', '0x4e', '0x1b', '0x64',
                      '0x11', '0x47', '0x38', '0x44', '0x34', '0x41', '0x52', '0x43']
    lis_to_verify3 = ['0x56a74b', '0x24cafed63', '0x570cc1c', '0xbcbfc7', '0x1f11d76', '0x221fec9', '0x5375501']

    if input1 == lis_to_verify1:
        print(f'validation successful : expected and actual results are same')
    else:
        print(f'validation failed : expected and actual results are not same')

    if input2 == lis_to_verify2:
        print(f'validation successful : expected and actual results are same')
    else:
        print(f'validation failed : expected and actual results are not same')

    if input3 == lis_to_verify3:
        print(f'validation successful : expected and actual results are same')
    else:
        print(f'validation failed : expected and actual results are not same')


def main():
    stu_marks, books_marks, book_ids = get_all_decimal_val()
    hex_stu_marks = get_all_hex_val(stu_marks)
    hex_book_marks = get_all_hex_val(books_marks)
    hex_book_id = get_all_hex_val_of_book_id(book_ids)
    validation_hex(hex_stu_marks, hex_book_marks, hex_book_id)


if __name__ == "__main__":
    main()