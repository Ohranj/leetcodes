def removeElement(nums, val):
    for x in range(len(nums) - 1, -1, -1):
        if nums[x] == val:
            del nums[x];
    return len(nums);

res = removeElement([0,1,2,2,3,0,4,2], 2);
print(res);