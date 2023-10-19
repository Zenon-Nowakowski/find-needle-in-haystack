#The class which finds the needle
def find_needle_in_haystack(haystack, needle):   
    #var declarations to make the function work
    needle_index = 0 
    solution = ""
    index = 0
    #this is functioning almost identically the same as a for loop with the acception that we can manipulate index at any point of the execution 
    while(index < len(haystack)): 
        #print('letter value: {}, needle value: {}, at needle_index: {}'.format(haystack[index], needle[needle_index % len(needle)], needle_index))
        #if a char belonging to the needle is found, then add it to the solution string and increment the index of needle, modulus is used to prevent overflow
        if needle[needle_index % len(needle)] == haystack[index]:
            solution += haystack[index]
            needle_index+=1
            #print('solution: {} needle_index of heystack: {} needle_index of needle: {}'.format(solution, index, needle_index))
        #reset the index if needle index and solution vars if solution is not found
        else:
            index -= needle_index
            needle_index = 0
            solution = ""
            #print('correct char not found, solution: {} needle_index of heystack: {} needle_index of needle: {}'.format(solution, index, needle_index))
        if(needle == solution):
            #print(solution)
            return index-len(needle)+1
        index+=1
    return -1
# test cases commonly failed: 
value = find_needle_in_haystack("leetcode", "leeto")
print('returned value:{}'.format(value))
value = find_needle_in_haystack("hello", "ll")
print('returned value:{}'.format(value))
value = find_needle_in_haystack("mississipi", "issi")
print('returned value:{}'.format(value))
#error with this test is that it compares to p, does not find it and resets however the way the logic currently works it compares to the 'ipi' as it has already looped through the solution 
value = find_needle_in_haystack("mississipi", "issip")
print('returned value:{}'.format(value))
