k = int(input("Key: "))
text = input("Enter value: ")
list1 = [c for c in text]
list2 = [ord(c) + k for c in text]
list3 = [chr(x) for x in list2]
print(list1)
print(list3)

