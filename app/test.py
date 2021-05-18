from typing import List
from memory_profiler import profile
from app.myStringSearch import StringSearch
#from StringSearch import StringSearch
def stringSearch(spam_words: List[str], test_post: str):
    # 5490 test words
    # 575 spam words

    search = StringSearch()
    search.SetKeywords(spam_words)
    f = search.FindFirst(test_post)
    #print(f)
    # b = search.ContainsAny(test_post)

#@profile
def test():
    with  open('./sample_post') as f:
        test_post = f.read()
    with open('./app/SpamWordsCN.min.txt') as f:
        span_words = [line.rstrip() for line in f]
    times = 100
    while times > 0:
        stringSearch(span_words, test_post)
        times -= 1

if __name__=='__main__':
    import time

    start = time.time()
    test()
    end = time.time()
    print('程序运行时间:%s毫秒' % ((end - start) * 1000))

# 我的mac上一次100篇耗时1096.024990081787毫秒
