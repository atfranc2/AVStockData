from time import time, sleep

class CallMeter:
    def __init__(self, call_limit_per_minute = 5, call_limit_per_day = 500):
        self.call_limit_per_minute = call_limit_per_minute
        self.call_limit_per_day = call_limit_per_day
        self.total_calls = 0
        self.calls_within_limit = 0
        self.call_time = time()
        self.last_call_time = time()

        self.second_basis = 60

    def incrementCalls(self):
        self.total_calls += 1
        self.calls_within_limit += 1

    def timeSinceLastCall(self):
        return self.call_time - self.last_call_time

    def isConsecutiveCall(self):
        return self.timeSinceLastCall() < self.second_basis

    def meterCalls(self):
        self.incrementCalls()
        self.call_time = time()
        self.calls_within_limit = self.calls_within_limit if self.isConsecutiveCall() else 1
        self.last_call_time = self.last_call_time if self.isConsecutiveCall() else time()
        time_delta = self.call_time - self.last_call_time

        # print('Call Time', self.call_time)
        # print('Last Call Time', self.last_call_time)
        # print('Time Delta', time_delta)
        # print('Calls Within Limit', self.calls_within_limit)
        # print('-------------------------------------------')

        if (time_delta < self.second_basis) and (self.calls_within_limit > self.call_limit_per_minute):
            print(f"Calls per minute exceeded. Pausing operations for {self.second_basis - time_delta} seconds.")
            sleep(self.second_basis - time_delta)
            self.calls_within_limit = 0
            self.last_call_time = time()
