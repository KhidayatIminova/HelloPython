# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов

path1 = 'tsk4-51.txt'
path2 = 'tsk4-52.txt'
path_sum = 'tsk4-53.txt'

# def ReadData(path):
#     with open(str(path), 'r') as data:
#         pol = data.read()
#     return pol


s = open(path1, 'r')
print(s)

# for line in s:
#     print(line)
s.close()

# s = ReadData(path1)
# print(s)
# print(len(s))
# print(type(s))
# s.replace(" ","")
# print(s)


# def convert_pol(pol):
#     pol = pol.replace(" ","???")

#     return pol

# print(convert_pol(s))

# def convert_pol(pol):
#     pol = pol.replace('= 0', '')
#     pol = re.sub("[*|^| ]", " ", pol).split('+')
#     pol = [char.split(' ') for char in pol]
#     pol = [[x for x in list if x] for list in pol]
#     for i in pol:
#         if i[0] == 'x': i.insert(0, 1)
#         if i[-1] == 'x': i.append(1)
#         if len(i) == 1: i.append(0)
#     pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
#     return pol