class Solution:

    def carFleet(
        self,
        target: int,
        position: List[int],
        speed: List[int]
    ) -> int:
        ordered_cars = []
        for p, s in zip(position, speed):
            ordered_cars.append((p, s))
        ordered_cars.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for car in ordered_cars:
            pos, spd = car
            time2target = (target - pos) / spd

            if not stack:
                stack.append(time2target)
            else:
                prev = stack[-1]
                if time2target > prev:
                    stack.append(time2target)
        return len(stack)


