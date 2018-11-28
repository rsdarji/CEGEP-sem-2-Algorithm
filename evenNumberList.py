# def evenNumbers(list):
#     evenList = []
#
#     for i in list:
#         if i%2==0:
#             evenList.append(i)
#     return evenList
#
# print(evenNumbers([0,1,2,3,4,5,6,7]))

def numberOfVowels(str):
    counter = 0
    for i in str:
        if i in ('a','e','i','o','u','A','E','I','O','U'):
            counter+=1
    return counter
print(numberOfVowels("afgfgfgefAIghfi"))