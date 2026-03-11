def two_sum(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        complete = target - num
        if complete in seen:
            return [seen[complete], i]
        seen[num] = i
numbers=[1,4,2,7,3,4,2,8,9]
print(two_sum(numbers, 9))
