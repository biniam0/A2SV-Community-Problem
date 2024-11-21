n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()
 
if k == 0:
    if nums[0] > 1:
        print(1)
    else:
        print(-1)
elif k == n or nums[k-1] != nums[k]:
    print(nums[k-1])
else:
    print(-1)
