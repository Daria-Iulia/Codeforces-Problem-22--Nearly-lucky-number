n = str(input())
lucky = n.count('4') + n.count('7')

if set(str(lucky)) <= {'4', '7'}:
    print("YES")
else:
    print("NO")