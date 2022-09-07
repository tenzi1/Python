# import unittest
from fibanacci import fib

# class FibonacciTest(unittest.TestCase):

#     def testCalculation(self):
#         self.assertEqual (fib(0), 1)
#         self.assertEqual (fib(1), 1)
#         self.assertEqual (fib(5), 8)
#         self.assertEqual (fib(10), 89)

# if __name__ == '__main__':
#     unittest.main()

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55

