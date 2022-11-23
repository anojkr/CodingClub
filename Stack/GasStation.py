class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        diff = 0
        surPlus = 0
        startIndex = 0
        for i in range(0, len(gas)):
            surPlus += gas[i] - cost[i]
            if surPlus < 0:
                diff += surPlus
                surPlus = 0
                startIndex = i + 1
        if surPlus + diff >= 0:
            return startIndex
        return -1
