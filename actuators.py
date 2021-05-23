"""
File for classes related to instantiating stepper motor objects
"""

import queue

class Step:
    """
    Step object, just enforces structure of step
    """

    def __init__(self, direction, delay):

        # check direction value is 1 or -1
        if direction == 'ccw' or direction == 'cw':
            self.direction = direction
        else:
            raise TypeError('Must be "ccw" or "cw"')

        # check
        if delay > 0:
            self.delay = delay


class Motor:

    def __init__(
            self,
            enable_pin,
            direction_pin,
            step_pin,
            steps_per_rev,
            min_delay=5,
            max_delta_delay=5,
    ):

        # save init values
        self.enable_pin = enable_pin
        self.direction_pin = direction_pin
        self.step_pin = step_pin
        self.min_delay = min_delay
        self.max_delta_delay = max_delta_delay
        self.steps_per_rev = steps_per_rev


