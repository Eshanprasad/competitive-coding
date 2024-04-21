k = 10.1
x = 20.0
#normal
print("{:.4f}".format(k))
print("{:.4f}".format(x))

"""
here in "{0:.4f}"
0 is the index of the values mentioned in format().
"""
print("{0:.4f}".format(k))
print("{0:.4f}".format(x))

"""
In format() we can include multiple variables like format(a, b, c).
So we use index to select a value from them.
example:
print("first variable {0:.2f}, second variable {1:.2f}".format(k, x))
here 0 is index of k in format(k, x)
1 is index of x in format(k, x)
"""

print("first variable {0:.2f}, second variable {1:.2f}".format(k, x))