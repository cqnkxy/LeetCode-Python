"""
给定下面的interface
interface Iterator<T> {
  boolean hasNext();
  T next();
}.

interface predicate<T> {
  boolean apply(T item)
}.

要求implement一个filter function如下：
Iterator<T> filter(Iterator<T> in, predicate<T> pred);
predicate里的apply就是起到check的作用，比如说T是Integer，然后当一个integer
是偶数的时候apply function返回True，否则返回False，那么filter function
就是实现一个偶数的iterator
例如如果不断call next()的话，Iterator<T> in返回的是0,1,2,3,4,5,6,...，
那么filter function返回的那个iterator应该能输出0,2,4,6...
"""

class Filter(object):
    def __init__(self, iterator, pred):
        self.iterator = iterator
        self.pred = pred
        self.val = 0
        self.used = True

    def hasNext(self):
        while self.used:
            if self.iterator.hasNext():
                self.val = self.iterator.next()
                if self.pred(self.val):
                    self.used = False
                    break
            else:
                break
        return not self.used

    def next(self):
        self.used = True
        return self.val
