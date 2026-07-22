class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers)
        for i in range(len(numbers)):
            value = target - numbers[i]
            for j in range(low + 1, high):
                if numbers[j] == value:
                    return [i+1, j+1]
            low += 1

                