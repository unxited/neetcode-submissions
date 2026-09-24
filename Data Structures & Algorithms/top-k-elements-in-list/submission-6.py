class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        ans = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans
    