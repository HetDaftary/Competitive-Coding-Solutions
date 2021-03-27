# cook your dish here
n, h, x = list(map(int, input().rstrip().split()))
in1 = list(map(int, input().rstrip().split()))

if max(in1) + x >= h:
    print("YES")
else:
    print("NO")