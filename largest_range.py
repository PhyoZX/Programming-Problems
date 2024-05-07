# the array  [1, 5, 3, 2, 0, 4]
def largestRange(array) :
    numbers = {x:0 for x in array} # {1: 0, 5: 0, 3: 0, 2: 0, 0: 0, 4: 0}
    left = right = 0

    for number in array :
        if numbers[number] == 0 :
            left_count = number - 1
            right_count = number + 1

            while left_count in numbers :
                numbers[left_count] = 1
                left_count -= 1
            left_count += 1

            while right_count in numbers :
                numbers[right_count] = 1
                right_count += 1           
            right_count -= 1

            if (right - left) <= (right_count - left_count) :
                right = right_count
                left = left_count

    return [left, right]

print(largestRange([11,7,3,4,2,1,0]))