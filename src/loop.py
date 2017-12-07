import time
from   threading import Timer


class Loop():

   def __init__(self, rate):
      self.time_step = 1.0 / rate

   def fun(self, fun):
      self.fun = fun
      return self

   def start(self):
      start_time = time.time()
      self.fun()
      elapsed = time.time() - start_time
      self.timer = Timer(self.time_step - elapsed, self.start)
      self.timer.start()

