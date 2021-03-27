T = int(input())

for _ in range(T):
    print(len(list(filter(lambda x: x != '', input().strip().split('0')))))