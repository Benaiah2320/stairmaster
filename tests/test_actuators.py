import unittest

from actuators import *

class StepAdd(unittest.TestCase):

    def test_init_dir_check_fail(self):
        """
        Tests that adding a step correctly verifies the direction
        """

        values = [2, -5, 'str', '-1', 'cww']
        for i in values:
            self.assertRaises(TypeError, Step, i, 5)

    def test_init_dir_check_pass(self):
        """
        Test that the cw or ccw results in a created step
        """

        values = ['cw', 'ccw']
        for i in values:
            self.assertEqual(i, Step(i, 5).direction)

    def test_init_delay_fail(self):
        """
        Test that delay fails when not 5 or greater
        """

        values = [4.9, 0, -5, -100, "5", "string"]
        for i in values:
            self.assertRaises(TypeError, Step, 'cw', i)

    def test_init_delay_pass(self):
        """
        Tests that delay passes when 5 or greater
        """

        values = [100, 5]
        for i in values:
            self.assertEqual(i, Step('cw', i).delay)


if __name__ == '__main__':
    unittest.main()
