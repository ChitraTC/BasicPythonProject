#6 Delete a list of keys from dictionary
colour={
    1:"red",
    2:"blue",
    3:"Orange",
    4:"yellow",
    5:"Green"
}
r_keys=[4,5]
for i in r_keys:
    colour.pop(i)
print(colour)