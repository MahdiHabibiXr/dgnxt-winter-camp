def diginext_task1(i=1, s=""):
    # repeat the input text i times
    temp = s * i
    # seprate i chars of the repeated text
    temp = temp[0:i]
    # return the count of char a in the new string
    return temp.count('a'), temp


# set the default values
txt = "aba"
length = 10
# print the input text and integer
print(f"Input: {txt} , length: {length}")
# just print a line
print('=' * 30)
# calculate with the function
a_count, txt = diginext_task1(length, txt)
# print the output
print(f"Output string: {txt} \nRepeat 'a': {a_count}")
