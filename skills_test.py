import io
import unittest
import unittest.mock
from skills import skills

@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
class TestSkills(unittest.TestCase):

    def test_spacing(self, mock_stdout):
        master, selected = skills("example.csv","libre")
        print(*selected, sep=",")
        self.assertEqual(mock_stdout.getvalue(),"Writer,Calc,Impress\n")

if __name__ == '__main__':
    unittest.main()