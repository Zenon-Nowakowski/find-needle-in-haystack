haystack = "hello"
needle = "ll"
solution = ""
index = 0
for i,letter in enumerate(haystack): 
    if needle[index % len(needle)] == letter:
        solution += letter
        if(needle == solution):
            print('solved:{}'.format(i-len(needle)+1))
    index+=1
else:
    solution = -1
print(solution)