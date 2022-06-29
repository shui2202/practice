def threesum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return [i, j, k]
                return None
num = [1, 2, 3, 4, 5]
sum = 6
print(threesum(num, sum))