import json
import random
import threading

class Simulator(threading.Thread):

    def __init__(self, name="Simulation", callback=None):
        self.data = None
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        self.initial_start = True
        self.hour = 1
        self.time_waiting = 5
        self.callback = callback

        threading.Thread.__init__(self, name=name)


    def run(self):
        """ main control loop """
        print("%s starts" % (self.getName(),))

        count = 0
        while not self._stopevent.isSet():
            with open('data.json', 'r') as outfile:
                self.data = json.loads(outfile.read())
            count += 1
            self._stopevent.wait(self._sleepperiod)
            if count % self.time_waiting == 0:
                if self.initial_start:
                    cold = random.randint(0, 1) + random.random()
                    hot = random.randint(0, 1) + random.random()
                    total_val = hot + cold
                    total = [{'hour': "0{}:00".format(self.hour), 'cold': cold, 'hot': hot, 'total': total_val}]
                    print(total)
                    self.initial_start = False
                else:

                    total = self.data['04']['6']
                    if 6 < self.hour <= 9 or 14 < self.hour <= 18:
                        cold = random.randint(1, 2) + random.random()
                        hot = random.randint(3, 5) + random.random()
                    elif 18 < self.hour <= 21:
                        cold = random.randint(1, 2) + random.random()
                        hot = random.randint(4, 9) + random.random()
                    else:
                        cold = random.randint(0, 1) + random.random()
                        hot = random.randint(0, 1) + random.random()
                    total_val = hot + cold
                    if self.hour < 10:
                        strhour = "0" + str(self.hour)
                    else:
                        strhour = "0" + str(self.hour)
                    df = {'hour': "{}:00".format(strhour), 'cold': cold, 'hot': hot, 'total': total_val}
                    print(df)
                    total.append(df)

                self.data['04']['6'] = total
                with open('data.json', 'w') as outfile:
                    json.dump(self.data, outfile)
                self.hour += 1
                if self.hour % 25 == 0:
                    break

        print("%s ends" % self.getName())
        self.callback()

    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
        self.callback()
