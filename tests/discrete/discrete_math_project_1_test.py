import unittest
from app.discrete.discrete_math_project_1 import DiscreteMathProject


class DiscreteMathProject1(unittest.TestCase):
    def test_sequence_len_valid(self):
        project = DiscreteMathProject()
        self.assertTrue(len(project.sequence), 50)


if __name__ == '__main__':
    unittest.main()