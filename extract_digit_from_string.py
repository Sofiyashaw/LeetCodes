# Write a Python program to extract digits from a given string

test_string="t3y5hy4hgv3h4b2nj2"
print("The original string is"+test_string)
res = "".join(filter(lambda i : i.isdigit(),test_string))
print("The digit string is" +str(res))