class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # binary search solution space, sum of the entire thing is the upper bound
        # if the weight can be completed in less than required days, then move right pointer
        # if it takes longer, then we need to increase the weight limit

        def check_weight(shipCapacity):
            num_days = 1
            capacity = 0
            for weight in weights:
                if capacity + weight > shipCapacity:
                    num_days += 1
                    capacity = 0
                capacity += weight
            return num_days <= days

        l, r = max(weights), sum(weights)

        while l < r:
            m = (l + r) // 2
            if check_weight(m):
                r = m
            else:
                l = m + 1

        return l
