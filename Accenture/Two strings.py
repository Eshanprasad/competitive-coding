"""
Two strings s and t, where length of s and t are between 1 and 1000 characters.

Output:
Return True if it's possible to create s by rearranging the characters of t and False oherwise.

Example:
Input:
s = "listen"
t = "silent"

output: True
"""


s = input()
t = input()
s_dict, t_dict = {}, {}
for i in s:
    s_dict[i] = 1+s_dict.get(i, 0)
for i in t:
    t_dict[i] = 1+t_dict.get(i, 0)
for i in s_dict:
    if i in t_dict and t_dict[i]>=s_dict[i]:
        continue
    else:
        print(False)
        break
else:
    print(True)