def count_up_to(max):
 count = 0
 while count <= max:
    yield count
    count += 1
counter = count_up_to(5)
for num in counter:
 num=num+2
 print(num)
