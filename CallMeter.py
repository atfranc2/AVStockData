from time import time, sleep

class CallMeter:
    def __init__(self, call_limit_per_minute = 5, call_limit_per_day = 500):
        self.call_limit_per_minute = call_limit_per_minute
        self.call_limit_per_day = call_limit_per_day
        self.total_calls = 0
        self.calls_within_limit = 0
        self.call_time = time()
        self.last_call_time = time()

    def incrementCalls(self):
        self.total_calls += 1
        self.calls_within_limit += 1

    def __meterCalls(self):
        self.call_time = time()
        time_delta = self.call_time - self.last_call_time
        self.__incrementcalls()

        print(time_delta)
        print(self.calls_within_limit)
        print(self.call_limit_per_minute)

        if (time_delta < 60) and (self.calls_within_limit > self.call_limit_per_minute):
            print(f"Calls per minute exceeded. Pausing operations for {time_delta} seconds.")
            sleep(60 - time_delta)
            self.total_calls = 1
            self.last_call_time = time()
