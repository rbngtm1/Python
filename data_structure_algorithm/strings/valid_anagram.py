# string1 = "tra"
# string2 = "ratt"

# list1=list(str(string1))
# list2=list(str(string2))
# print(list2)
# newlist=[]
# # def myfunc():
# for i in list1:
#     print(i)
#     if (i not in list2) and (len(list1) != len(list2)):
#         newlist.append(i)
#         print(newlist)
#         print('false') 
#     else:
#         print('True')

# # a=myfunc()
# # print(a)
input_str_1 = "practice makes perfect"
input_str_2 = "perfect makes practice"

input_str_3 = "allergy"
input_str_4 = "allergic"


def is_anagram(str_1, str_2):
    str_1 = str_1.replace(" ", "")
    str_2 = str_2.replace(" ", "")

    if len(str_1) != len(str_2):
        return False

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    dict_1 = dict.fromkeys(list(alphabet), 0)
    dict_2 = dict.fromkeys(list(alphabet), 0)

    for i in range(len(str_1)):
        dict_1[str_1[i]] += 1
        dict_2[str_2[i]] += 1
    return dict_1 == dict_2


# Is an anagram:
print(is_anagram(input_str_1, input_str_2))

# Is not an anagram:
print(is_anagram(input_str_3, input_str_4))

