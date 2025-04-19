#     for (let currentIndex = 1; currentIndex < nums.length; currentIndex++) {
#         if (nums[uniqueIndex] < nums[currentIndex]) {
#             uniqueIndex++;
#             nums[uniqueIndex] = nums[currentIndex];
#         }
#     }
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            uniqueIndex = 0

            for i in range(1, len(nums)):
                if nums[uniqueIndex] < nums[i]:
                    uniqueIndex += 1
                    nums[uniqueIndex] = nums[i]

            return uniqueIndex + 1        