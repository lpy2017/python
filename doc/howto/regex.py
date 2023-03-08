import re
import os
import sys


def f1():
    p = re.compile("ab*")
    p = re.compile("ab*", re.IGNORECASE)
    p = re.compile(r"\w")  # 字符串前加r 反斜杠不以任何特殊的方式处理前缀为 'r' 的字符串字面

def f2():
    p2 = re.compile("[a-z]+")
    print(p2.match(""))  # None
    m = p2.match("ab")
    print(m)  # <re.Match object; span=(0, 2), match='ab'>
    if m:
        print("match", m.group())
    else:
        print("not match")
    print(m.group())  # str ab
    print(m.start())  # int  0
    print(m.end())   # int  2
    print(m.span())  # tuple[int,int]  (0, 2)
    # 匹配 包含start 不包含 end


def f3():
    p = re.compile(r"\d+")
    list = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')  #list
    print(list)       # ['12', '11', '10']
    print(list[0])
    iterator = p.finditer('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
    for m in iterator:
        print(m)  # <re.Match object; span=(0, 2), match='12'>


def f4():
    m = re.search("^from", "from here ot eternity")
    print(m)   # <re.Match object; span=(0, 4), match='from'>


def f5():
    p = re.compile("(a(b)c)d")
    m = p.match("abcd")
    print(m.group(0))   # abcd    (a(b)c)d
    print(m.group(1))   # abc      (a(b)c)
    print(m.group(2))   # b       (b)


def f6():
    p = re.compile(r"\W+")
    sl = p.split("This is a test, short and sweet, of split()")
    print(sl)     # ['This', 'is', 'a', 'test', 'short', 'and', 'sweet', 'of', 'split', '']
    sl = p.split("This is a test, short and sweet, of split()", 2)
    print(sl)   # ['This', 'is', 'a test, short and sweet, of split()']  只分割2个\W+
    re.split(r"\W+", "This is a test, short and sweet, of split()")  # 等价于上面 compile+split


def f7():
    p = re.compile('(blue|white|red)')
    str = p.sub('colour', 'blue socks and red shoes')
    print(str)   # colour socks and colour shoes
    str2 = p.sub('colour', 'blue socks and red shoes', count=1)
    print(str2)  # colour socks and red shoes   count=1 只替换一个
    print(re.sub('(blue|white|red)', 'colour', 'blue socks and red shoes'))   # 等等价于  re.compile+ p.sub


def f8():
    # match 开头匹配  search 会0开始到最后
    print(re.match('super', 'superstition').span())   # (0, 5)
    print(re.match('super', 'insuperable'))  #None

    s = '<html><head><title>Title</title>'
    len(s)  # 32
    # match 会贪婪 （匹配到最多的）
    print(re.match('<.*>', s).span())  # (0, 32)
    #  *?, +?, ??, or {m,n}? 非贪婪的，匹配到第一个结束
    print(re.match('<.*?>', s).group())  # <html>


if __name__ == '__main__':
    if len(sys.argv) > 1:
        params = sys.argv[1:]
        print(params)
    # f1()
    # f2()
    # f3()
    # f4()
    # f5()
    # f6()
    # f7()
    f8()
