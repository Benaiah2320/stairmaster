"""
File for classes related to instantiating stepper motor objects
"""


class Step:
    """
    Step object, just enforces structure of step
    """

    def __init__(self, direction: str, delay: int):

        # check direction value is 1 or -1
        if direction == 'ccw' or direction == 'cw':
            self.direction = direction
        else:
            raise ValueError('Must be "ccw" or "cw"')

        # check delay is positive and over 5us
        if type(delay) == int:
            if delay >= 5:
                self.delay = delay
            else:
                raise ValueError('Must be greater than 5us')
        else:
            raise TypeError('Must be an integer')


class Motor:

    def __init__(
            self,
            enable_pin,
            direction_pin,
            step_pin,
            steps_per_rev,
            min_delay=5,
            max_delay=500,
            max_delta_delay=5,
    ):
        valid_steps_per_rev = [
            400,
            800,
            1600,
            3200,
            6400,
            12800,
            25600,
            1000,
            2000,
            4000,
            5000,
            8000,
            10000,
            20000,
            25000,
        ]

        # save init values
        # pins must all be different, and must be strings or ints
        pins = [enable_pin, direction_pin, step_pin]
        if all((isinstance(pin, str) or isinstance(pin, int)) for pin in pins):
            if len(pins) == len(set(pins)):
                self.enable_pin = enable_pin
                self.direction_pin = direction_pin
                self.step_pin = step_pin
            else:
                raise ValueError('All pins must be different')
        else:
            raise TypeError

        # min_delay must be int and greater than 5us
        if type(min_delay) == int:
            if min_delay >= 5:
                self.min_delay = min_delay
            else:
                raise ValueError('Must be greater than 5us')
        else:
            raise TypeError('Must be an integer')

        # max_delay must be int and greater than 5us
        if type(max_delay) == int:
            if max_delay >= 5:
                self.max_delay = max_delay
            else:
                raise ValueError('Must be greater than 5us')
        else:
            raise TypeError('Must be an integer')

        # delay must be int and greater than 5us
        if type(max_delta_delay) == int:
            if max_delta_delay >= 5:
                self.max_delta_delay = max_delta_delay
            else:
                raise ValueError('Must be greater than 5us')
        else:
            raise TypeError('Must be an integer')

        # steps per rev must be int and from list
        if type(steps_per_rev) == int:
            if steps_per_rev in valid_steps_per_rev:
                self.steps_per_rev = steps_per_rev
            else:
                raise ValueError('Must be valid steps per rev from DM542T driver')
        else:
            raise TypeError('Must be an integer')

