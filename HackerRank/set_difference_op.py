# Enter your code here. Read input from STDIN. Print output to STDOUT
en_num = int(input())
en_set = map(int, input().split())
fr_num = int(input())
fr_set = list(map(int, input().split()))

count = 0

for num in en_set:
    if num not in fr_set:
        count += 1

print(count)
