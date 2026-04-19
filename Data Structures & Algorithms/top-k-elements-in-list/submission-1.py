import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict={}
        for i in nums:
            count_dict[i] = count_dict.get(i,0) + 1
        heap = []
        for num, count in count_dict.items():
            heapq.heappush(heap, (count, num))
            if len(heap)>k:
                heapq.heappop(heap)
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans
        