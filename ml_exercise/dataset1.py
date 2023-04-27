import unittest
import numpy as np
from matplotlib import pyplot

class TestStringMethods(unittest.TestCase):
    def test_true_func(self):
        value = 0
        expected = 0
        actual = true_function(value)
        self.assertEqual(expected, actual)
    
def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10 


x = np.linspace(-1, 1)
y = true_function(x)

pyplot.xlabel("x")
pyplot.ylabel("y")

pyplot.plot(x,y,label="sin")
pyplot.legend()
pyplot.savefig("ex1.1.png", format="png")

pyplot.show()
    
if __name__ == "__main__":
    unittest.main()
