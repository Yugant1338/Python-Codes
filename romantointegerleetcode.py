class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l1 = []
        num = 0
        for i in s:
            if i == "I":
                l1.append(1)
            if i == "V":
                l1.append(5)
            if i == "X":
                l1.append(10)
            if i == "L":
                l1.append(50)
            if i == "C":
                l1.append(100)
            if i == "D":
                l1.append(500)
            if i == "M":
                l1.append(1000)
        for j in range(0, len(l1) - 1):
            if l1[j] > l1[j + 1]:
                num = num + int(l1[j])
            if l1[j] < l1[j + 1]:
                num = num - int(l1[j])
            if l1[j] == l1[j + 1]:
                num = num + int(l1[j])
        return (num + int(l1[-1]))
