class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        def getVal(arr, i):
            if i == -1:
                return float('-inf')
            if i == len(arr):
                return float('inf')
            return arr[i]

        # return (lShort, rShort, lLong, rLong)
        def getIndices(rShort, aShort, aLong):
            midIndex = (len(aShort) + len(aLong)) / 2
            rLong = midIndex - rShort
            return (rShort - 1, rShort, rLong - 1, rLong)

        # determine whether to go left or right
        def getDirection(lShort, rShort, lLong, rLong, aShort, aLong):
            if getVal(aShort, lShort) > getVal(aLong, rLong):
                return -1
            elif getVal(aLong, lLong) > getVal(aShort, rShort):
                return 1
            else:
                return 0

        # calculate median
        def getResult(lShort, rShort, lLong, rLong, aShort, aLong):
            odd = (len(aShort) + len(aLong)) % 2
            if odd:
                return min(getVal(aLong, rLong), getVal(aShort, rShort))
            else:
                return (max(getVal(aShort, lShort), getVal(aLong, lLong))
                        + min(getVal(aShort, rShort), getVal(aLong, rLong))) / 2.0

        # determine long and short arrays
        aShort = nums1
        aLong = nums2
        if len(nums1) > len(nums2):
            aShort = nums2
            aLong = nums1

        # temporary variables
        lShort = rShort = lLong = rLong = d = 1

        # binary search
        l = 0
        r = len(aShort)
        while d != 0:
            m = (l + r) / 2
            # getting indices from our m
            lShort, rShort, lLong, rLong = getIndices(m, aShort, aLong)
            # get out d (direction)
            d = getDirection(lShort, rShort, lLong, rLong, aShort, aLong)
            if d < 0:
                r = m - 1
            elif d > 0:
                l = m + 1

        # calculate median
        return getResult(lShort, rShort, lLong, rLong, aShort, aLong)