import random, math, numpy
import unittest
import sys
import itertools

sys.path.append('/home/olohuone/Coding/io8oi/Research/Indifference/')

import lib.readDateVals as rv


class TestMathFunctions(unittest.TestCase):

    def setUp(self):
	self.seq = range(10)
	self.data = [[random.uniform(0,100) for _ in range(10)] for _ in range(10)]
	self.returns = [[random.random()*x for x in range(10)] for _ in range(10)]
	self.sds = [[random.random()*x**2 for x in range(10)] for _ in range(10)]
	self.corrMatrix = numpy.corrcoef(self.returns)
	
    def testRandomChoices(self):
	randomSd = random.choice(self.sds)
	randomRe = random.choice(self.returns)
	aves = rv.aves(self.returns)
	randomAve = random.choice(aves)

	self.assertTrue(randomSd in self.sds)
	self.assertTrue(randomAve in aves)
	self.assertTrue(randomRe in self.returns)
	
    def testOrder(self):
	mySds = rv.sds(self.sds, 365)
	#SDs must be positive (not zero and not negative)
	self.assertTrue(sum([sd <= 0 for sd in mySds])==0)

    def checkSize(self):
	size = size(self.returns)
	self.assertTrue(10 == size)
	
	# Check SDs and returns work correctly


# Provides commandLine interface
if __name__ == '__main__':
    unittest.main()
