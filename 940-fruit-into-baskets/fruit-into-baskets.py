class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l , res, tot=0,0,0
        count=collections.defaultdict(int)
        for r in range(len(fruits)):
            count[fruits[r]]+=1
            tot+=1
            while len(count)>2:
                f=fruits[l]
                count[f]-=1
                tot-=1
                l+=1
                if not count[f]:
                    count.pop(f)
            res=max(res,tot)
        return res            

        # left = 0
        # count = {}
        # max_len = 0

        # for right in range(len(fruits)):
        #     count[fruits[right]] = count.get(fruits[right], 0) + 1

        #     while len(count) > 2:
        #         count[fruits[left]] -= 1
        #         if count[fruits[left]] == 0:
        #             del count[fruits[left]]
        #         left += 1

        #     max_len = max(max_len, right - left + 1)

        # return max_len
