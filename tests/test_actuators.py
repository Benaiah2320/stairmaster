import unittest

from actuators import *


class TestStep(unittest.TestCase):

    def test_init_dir_check_fail(self):
        """
        Tests that adding a step correctly verifies the direction
        """

        values = [2, -5, 'str', '-1', 'cww']
        for i in values:
            self.assertRaises(ValueError, Step, i, 5)

    def test_init_dir_check_pass(self):
        """
        Test that the cw or ccw results in a created step
        """

        values = ['cw', 'ccw']
        for i in values:
            self.assertEqual(i, Step(i, 5).direction)

    def test_init_delay_int_fail(self):
        """
        Test that delay fails when not int
        """

        values = ["5", "string"]
        for i in values:
            self.assertRaises(TypeError, Step, 'cw', i)

    def test_init_delay_min_fail(self):
        """
        Test that delay fails when not greater than 5us
        """

        values = [2, -5, -100, 4]
        for i in values:
            self.assertRaises(ValueError, Step, 'cw', i)

    def test_init_delay_pass(self):
        """
        Tests that delay passes when 5 or greater
        """

        values = [100, 5]
        for i in values:
            self.assertEqual(i, Step('cw', i).delay)


class TestMotor(unittest.TestCase):

    def test_init_min_delay_int_fail(self):
        """
        Test that delay fails when not int
        """

        values = ["5", "string"]
        for i in values:
            self.assertRaises(TypeError, Motor, 1, 2, 3, 400, i)

    def test_init_min_delay_min_fail(self):
        """
        Test that delay fails when not greater than 5us
        """

        values = [2, -5, -100, 4]
        for i in values:
            self.assertRaises(ValueError, Motor, 1, 2, 3, 400, i)

    def test_init_min_delay_pass(self):
        """
        Tests that delay passes when 5 or greater
        """

        values = [100, 5]
        for i in values:
            self.assertEqual(i, Motor(1, 2, 3, 400, min_delay=i).min_delay)

    def test_init_default_max_delay_int_fail(self):
        """
        Test that delay fails when not int
        """

        values = ["5", "string"]
        for i in values:
            self.assertRaises(TypeError, Motor, 1, 2, 3, 400, 5, i)

    def test_init_default_max_delay_min_fail(self):
        """
        Test that delay fails when not greater than 5us
        """

        values = [2, -5, -100, 4]
        for i in values:
            self.assertRaises(ValueError, Motor, 1, 2, 3, 400, 5, i)

    def test_init_default_max_delay_pass(self):
        """
        Tests that delay passes when 5 or greater
        """

        values = [100, 5]
        for i in values:
            self.assertEqual(
                i,
                Motor(1, 2, 3, 400, default_max_delay=i).default_max_delay
            )

    def test_init_pin_str_int_fail(self):
        """
        Test that init fails when any pin value isn't an int or a string
        """

        values = {
            'enable_pin': [1, Step('cw', 10)],
            'direction_pin': [1, "GPIO 2"],
            'step_pin': [[1, 1], "GPIO 2"],
        }

        for i in range(0, 2):
            self.assertRaises(
                TypeError,
                Motor,
                values['enable_pin'][i],
                values['direction_pin'][i],
                values['step_pin'][i],
                400,
            )

    def test_init_pin_unequal_fail(self):
        """
        Tests that init fails when any pin values are the same
        """

        values = {
            'enable_pin':    [1, "GPIO 2", 2, 4],
            'direction_pin': [1, "GPIO 2", 3, 3],
            'step_pin':      [1, 1, 3, 4],
        }

        for i in range(0, 4):
            self.assertRaises(
                ValueError,
                Motor,
                values['enable_pin'][i],
                values['direction_pin'][i],
                values['step_pin'][i],
                400,
            )

    def test_init_pin_pass(self):
        """
        Tests that init passes when all pins are strings or ints and unique
        """

        values = {
            'enable_pin': [1, "GPIO 2"],
            'direction_pin': [2, "GPIO 3"],
            'step_pin': [3, "GPIO 4"],
        }

        for i in range(0, 2):
            test_motor = Motor(
                values['enable_pin'][i],
                values['direction_pin'][i],
                values['step_pin'][i],
                400,
            )
            self.assertEqual(values['enable_pin'][i], test_motor.enable_pin)
            self.assertEqual(values['direction_pin'][i], test_motor.direction_pin)
            self.assertEqual(values['step_pin'][i], test_motor.step_pin)

    def test_init_max_delta_delay_int_fail(self):
        """
        Test that delay fails when not int
        """

        values = ["5", "string"]
        for i in values:
            self.assertRaises(TypeError, Motor, 1, 2, 3, 400, 10, 500, i)

    def test_init_max_delta_delay_min_fail(self):
        """
        Test that delay fails when not greater than 5us
        """

        values = [2, -5, -100, 4]
        for i in values:
            self.assertRaises(ValueError, Motor, 1, 2, 3, 400, 10, 500, i)

    def test_init_max_delta_delay_pass(self):
        """
        Tests that delay passes when 5 or greater
        """

        values = [100, 5]
        for i in values:
            self.assertEqual(i, Motor(1, 2, 3, 400, max_delta_delay=i).max_delta_delay)

    def test_init_steps_int_fail(self):
        """
        Tests that init fails when steps_per_rev not int
        """

        values = ['100', [100, 200], 'string']
        for i in values:
            self.assertRaises(TypeError, Motor, 1, 2, 3, i)

    def test_init_steps_valid_fail(self):
        """
        Tests that init fails when steps_per_rev not from list
        of valid values on DM542T driver
        """

        values = [100, 900, 1000000]
        for i in values:
            self.assertRaises(ValueError, Motor, 1, 2, 3, i)

    def test_init_steps_valid_pass(self):
        """
        Tests that init passes with a valid steps_per_rev value
        """

        values = [400, 6400, 8000]
        for i in values:
            self.assertEqual(i, Motor(1, 2, 3, i).steps_per_rev)


if __name__ == '__main__':
    unittest.main()
