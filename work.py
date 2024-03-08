#Вариант 24.
#Шеснадцатиричные числа, не превышающие 102410 расположенные в порядке убывания. Для каждой такой последовательности максимальное число вывести прописью.

nums = {'0':"ноль",'1':'один','2':"два",
        '3':"три",'4':"четыре",'5':"пять",
        '6':"шесть",'7':"семь",'8':"восемь",
        '9':"девять", 'A':'десять','B':'одиннадцать',
        'C':'двенадцать','D':'тринадцать','E':'четырнадцать', 'F':'пятнадцать','-':'минус'}


max_number = 1024
max_number_hex = int(hex(max_number)[2:])
buf_len = 1
work_buffer = ''
work_buffer1 = 0
value = 1
max_s = 0
with open("work.txt", 'r') as file:
    buffer = file.read(buf_len)
    while buffer:
        if buffer == '-':
            work_buffer += buffer
            buffer = file.read(buf_len)
        while '0' <= buffer <= 'F':
            work_buffer += buffer
            buffer = file.read(buf_len)
        if value:  # Вывод максимального числа первой последовательности
            for x in str(work_buffer):
                print(nums[str(x)], end=" ")
            print(" ")
        value = 0
        if len(work_buffer) > 0 and abs(int(work_buffer, 16)) <= max_number_hex:
            if int(work_buffer, 16) >= work_buffer1 and (work_buffer1 != 0 and int(work_buffer, 16) != 0):
                max_s = work_buffer
                for x in str(max_s):
                    print(nums[str(x)], end=" ")
                print(" ")
        work_buffer1 = int(work_buffer, 16)
        work_buffer = ''
        buffer = file.read(buf_len)