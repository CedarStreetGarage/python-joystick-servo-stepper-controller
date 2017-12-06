import time
from   threading import Timer


class Loop():

   def __init__(self, rate):
      self.rate = rate

   def _fun(self):
      t = time.time()
      self.fun()
      elapsed = time.time() - t
      self.timer = Timer(self.rate - elapsed, self._fun)
      self.timer.start()

   def fun(self, fun):
      self.fun = fun
      return self

   def start(self):
      self.timer = Timer(self.rate, self._fun)
      self.timer.start()

   def stop(self):
      self.timer.cancel()

