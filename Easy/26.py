def removeDuplicates(nums):
    cur = None;
    for x in range(len(nums) - 1, -1, -1):
        if cur == None:
            cur = nums[x];
            continue;
        
        if cur == nums[x]:
            del nums[x];
            continue;
        
        cur = None;
        cur = nums[x];

    return len(nums);

res = removeDuplicates([1,1,2]);
print(res);