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


# list_of_marks_from_stu = [i['marks'] for i in student_data]
# print(list_of_marks_from_stu)
# list_of_marks_from_book_ids = [j['marks'] for j in book_index]
# print(list_of_marks_from_book_ids)
# list_of_book_ids = [j['book_id'] for j in book_index]
# print(list_of_book_ids)


def convert_to_hex_data(marks, name):
    hex_data_dict = []
    for each_mark in marks:
        dict_type = {name: each_mark[name]}
        marks = []
        for number in each_mark['marks']:
            hex_val = hex(number)
            if len(hex_val) <= 3:
                hex_list = list(hex_val)
                hex_list.insert(2, '0')
                hex_val = ''.join(hex_list)
            marks.append(hex_val)
        dict_type['marks'] = marks
        hex_data_dict.append(dict_type)
    return hex_data_dict


def convert_to_hex_each_book_id(id, name):
    hex_data_dict = []
    for each_id in id:
        dict_type = {name: each_id[name]}
        id_s = []
        val = dict_type['book_id']
        hex_val = hex(val)
        if len(hex_val) <= 3:
            hex_li = list(hex_val)
            hex_li.insert(2, '0')
            hex_val = ''.join(hex_li)
        id_s.append(hex_val)
        dict_type['book_id'] = id_s
        hex_data_dict.append(dict_type)
    return hex_data_dict


def printing_converted_data(hex_data):
    counter = 0
    print('\n')
    print('[')
    for each_item in hex_data:
        print('{')
        for key, value in each_item.items():
            if key == 'student_name':
                print(f"\t'{key}' : '{value}'")
            elif key == 'book_id':
                print(f"\t'{key}' : {value}")
            else:
                print(f"\t'{key}' : {value}")
        counter = counter + 1
        if counter < len(hex_data):
            print('}')
        else:
            print('}')
    print(']')


def main():
    hex_data_of_stu_marks = convert_to_hex_data(student_data, 'student_name')
    # print(hex_data_of_stu_marks)
    hex_data_of_book_id_marks = convert_to_hex_data(book_index, 'book_id')
    # print(hex_data_of_book_id_marks)
    hex_data_of_book_id = convert_to_hex_each_book_id(book_index, 'book_id')
    # print(hex_data_of_book_id)
    printing_converted_data(hex_data_of_stu_marks)
    printing_converted_data(hex_data_of_book_id_marks)


if __name__ == '__main__':
    main()
