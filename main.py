def find_needle_in_haystack(haystack, needle):   
    index = 0 
    solution = ""
    for i,letter in enumerate(haystack): 
        print('letter value: {}, needle value: {}, at index: {}'.format(haystack[i], needle[index % len(needle)], index))
        if needle[index % len(needle)] == haystack[i]:
            solution += haystack[i]
            index+=1
            print('solution: {} index of heystack: {} index of needle: {}'.format(solution, i, index))
        else:
            i -= index
            index = 0
            solution = ""
            print('correct char not found, solution: {} index of heystack: {} index of needle: {}'.format(solution, i, index))
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
#error with this test is that it compares to p, does not find it and resets however the way the logic currently works it compares to the 'ipi' as it has already looped through the solution 
value = find_needle_in_haystack("mississipi", "issip")
print('returned value:{}'.format(value))