class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer = 0
        rightPointer = len(numbers) - 1

        while True:
            # two values sum to target

            # sum > target -> move rightPointer

            # sum < target -> move leftPointer

            sumVal = numbers[leftPointer] + numbers[rightPointer]

            if sumVal == target:
                return [leftPointer + 1, rightPointer + 1]

            if sumVal > target:
                rightPointer -= 1

            else:
                leftPointer += 1

        return None