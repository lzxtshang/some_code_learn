def getSum(a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0X7fffffff
        MIN = 0X80000000
        while b != 0 :
          a,b = a^b,(a&b)<<1
          print(" a = {0:b},b =  {1:b}".format(a,b))
        return a
def getSum_(a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            print(type(a))
            print(" a = {0:b},b =  {1:b}".format(a,b))
        return a if a <= MAX else ~(a^mask)
print(getSum(-1,-1))
print(getSum_(-1,-1))
