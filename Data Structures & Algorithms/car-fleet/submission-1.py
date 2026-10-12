import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # questions: is there guaranteed to be a single car/
        # do we need to check for valid target?
        # can there be negative positions?
        # can speed be a double?


        # brute force:
        # sort it by position
        # for every pair of cars, calculate how many cycles it takes to reach the target. if the car behind has a cycle equal or less than the car in front, this mean the car behind caught up

        # ex) car 1 takes 3 cycles. car 4 takes 3 cycles
            # car 1 caught up to car 4

            # car 3 takes 10 cycles. car 2 takes 5 cycles
                # car 3 does not catch up catch up to car 2

        # keep track of cars based on cycles it takes
        # car 3: 10 - 0 / 1 = 10
        # car 4: 10 - 1 / 2 = math.ceil(9/2)

        # car 1: 3
        # car 2: 5
        # car 3: 10
        # car 4: 3

        # 10 5 3 

        # need to sort the cars based on position
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars, key=lambda c: c[0])
        # print(cars)

        # given a and b, where b is in front, a catches up if a's cycle <= b's cycle

        # stack of cycles
        stack = []
        for car in cars:
            cycle = (target - car[0]) / car[1]

            while stack and stack[-1] <= cycle:
                stack.pop()

            stack.append(cycle)
            

        return len(stack)

        










