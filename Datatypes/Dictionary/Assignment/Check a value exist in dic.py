#7..Check if a value exists in dictionary
colour={
    1:"red",
    2:"blue",
    3:"Orange",
    4:"yellow",
    5:"Green"
}
val=input("Enter the value to be checked:")
if val in colour.values():
    print(val," exists in dictionary")
else:print(val," doesn't exists in dictionary")