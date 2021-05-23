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


if __name__ == '__main__':
    unittest.main()
