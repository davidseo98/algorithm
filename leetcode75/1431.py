class Solution(object):

    # Beats 100 (100% runtime)
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        cutoff = max(candies) - extraCandies
        return [candy >= cutoff for candy in candies]
        