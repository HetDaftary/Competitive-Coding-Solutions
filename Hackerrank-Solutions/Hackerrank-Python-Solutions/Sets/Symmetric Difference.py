# Enter your code here. Read input from STDIN. Print output to STDOUT

n, set1, m, set2 = int(input()), set(list(map(int, input().strip().split()))), int(input()), set(list(map(int, input().strip().split())))

print('\n'.join(list(map(str, sorted(list(set1.union(set2).difference(set1.intersection(set2))))))))
