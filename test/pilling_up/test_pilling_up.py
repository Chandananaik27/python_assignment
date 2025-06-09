import unittest

from src.pilling_up.util import main,can_stack_cubes

class TestCanStackCubes(unittest.TestCase):
    def test_can_stack_cubes_yes(self):
        cubes = [1, 2, 3]
        self.assertEqual(can_stack_cubes(3, cubes), "Yes")

    def test_can_stack_cubes_no(self):
        cubes = [3, 2, 1, 4]
        self.assertEqual(can_stack_cubes(4, cubes), "No")

    def test_can_stack_cubes_empty(self):
        cubes = []
        self.assertEqual(can_stack_cubes(0, cubes), "Yes")

if __name__ == '__main__':
    unittest.main()