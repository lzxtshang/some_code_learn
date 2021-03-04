def process(pattern, put):
    patterns = list(pattern)
    puts = put.split(" ")
    info = {}
    if len(puts) != len(patterns):
        return False
    for i in range(0, len(puts)):
        val = info.get(patterns[i])
        if val:
            return val == puts[i]
        if puts[i] not in info.values():
            info[patterns[i]] = puts[i]
        else:
            return False
    return True

if __name__ == "__main__":
    """
    字符匹配，比如输入"abba"  "北京 杭州 杭州 北京" 输出 false
    """
    pattern = "abbc"
    put = "北京 杭州 杭州 北京"
    print(process(pattern, put))
    
 #https://blog.csdn.net/qq447995687/article/details/102807096
#//有一个字符串它的构成是词+空格的组合，如“北京 杭州 杭州 北京”，
# //要求输入一个匹配模式（简单的以字符来写）， 比如 aabb, 来判断该字符串是否符合该模式， 举个例子：
# //1. pattern = “abba”, str=“北京 杭州 杭州 北京” 返回 ture
# //2. pattern = “aabb”, str=“北京 杭州 杭州 北京” 返回 false
# //3. pattern = “baab”, str=“北京 杭州 杭州 北京” 返回 ture
# 这道题还是比较简单的，pattern并不是正则表达式，str也不是说根据pattern的某种规律来推算，就是实打实的匹配。

# 思路：

# 首先要将pattern和str进行对应，不同的字母对应不同的词
# 其次，字母的出现的顺序应该和词出现的顺序一致
# 如果上述条件，任何一个不满足就匹配不成功
# 可以用map将对应关系进行保存下来，key=字母，val=词，挨个遍历pattern对应位置上的值，如果在map中存在，则比较val是否相等；如果不存在则将对应关系放入map中
# 但是有个漏洞：如果此时map中不存在，但是val中存在会返回true，这时需要在val中判断，之前是否有这个val，如果有则字母与词不匹配。
