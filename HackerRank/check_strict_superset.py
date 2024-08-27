# Enter your code here. Read input from STDIN. Print output to STDOUT
super_set = set(map(int, input().split()))
n = int(input())
is_superset = True

for i in range(n):
    other_set = set(map(int, input().split()))
    if not super_set.issuperset(other_set):
        is_superset = False
        break

print(is_superset)
