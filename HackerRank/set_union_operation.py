# Enter your code here. Read input from STDIN. Print output to STDOUT
en_nums = int(input())
en_subs = set(map(int, input().split()))
fr_nums = int(input())
fr_subs = set(map(int, input().split()))

union = en_subs.union(fr_subs)

print(len(union))
