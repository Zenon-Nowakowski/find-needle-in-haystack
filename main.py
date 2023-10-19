def find_needle_in_haystack(haystack, needle):   
    index = 0 
    solution = ""
    for i,letter in enumerate(haystack): 
        if needle[index % len(needle)] == letter:
            solution += letter
            index+=1
        else:
            #print('correct char not found')
            index = 0
            solution = ""
        if(needle == solution):
            print(solution)
            return i-len(needle)+1
    return -1
# value = find_needle_in_haystack("leetcode", "leeto")
# print('returned value:{}'.format(value))
# value = find_needle_in_haystack("hello", "ll")
# print('returned value:{}'.format(value))
# value = find_needle_in_haystack("mississipi", "issi")
# print('returned value:{}'.format(value))
value = find_needle_in_haystack("mississipi", "issip")
print('returned value:{}'.format(value))