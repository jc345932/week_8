def pricess_string():
    string_1 ="Hello world"
    print("The whole string:", string_1)
    print("The first letter:", string_1[0])
    print("The lase letter:", string_1[-1])
    print("slicing from left:", string_1[:3])
    print("slicing from middle:", string_1[1:4])

def split_string():
    print("*" * 20)
    str_1 = "A stitch in time saves nine"
    half = int(len(str_1)/2)
    print(str_1[:half])
    print(str_1[half:])
    print("*" * 20)
split_string()