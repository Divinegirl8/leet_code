class Solution(object):
    def group_anagrams(self, strs):
        mapValue = {}
        for value in strs:
            sorted_array = tuple(sorted(value))

            if sorted_array not in mapValue:
                mapValue[sorted_array] = []

            mapValue.get(sorted_array).append(value)
        return list(mapValue.values())




