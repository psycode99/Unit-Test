import test_my_math
import unittest

def my_suite():
    suite = unittest.TestSuite()
    results = unittest.TestResult()
    suite.addTest(unittest.makeSuite(test_my_math.TestAdd))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()