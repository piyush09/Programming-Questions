# Print even numbers and their indexes in the array
nums_dict = {}
nums = [2,9,7,5,4,13,111,15,16]
index = 0

for i in range(0,len(nums)):
    if nums[i]%2 == 0:
        nums_dict[nums[i]] = index

    else:
        index += 1

for key, value in nums_dict.items():
    print (key, value)

