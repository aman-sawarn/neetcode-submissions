class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i] = count.get(i,0) + 1
        print(count)
        count = dict(sorted(count.items(), key=lambda x:x[1]))
        return list(count.keys())[len(count)-k:]
        