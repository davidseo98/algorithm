class Solution(object):

    # beats 82.55% (runtime)
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        length = len(flowerbed)
        for i in range(length):

            if flowerbed[i]: continue
            if (i-1 < 0 or flowerbed[i-1] == 0) and (i+1 >= length or flowerbed[i+1] == 0):
                flowerbed[i]=1
                n -=1

        if n > 0: return False
        else : return True 
        