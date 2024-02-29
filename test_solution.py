#!/usr/bin/env python3
#Programmiertask VOITH Unittest
#Author: Valentin Hofrichter
#v0.0.1

import unittest, sys, random, subprocess, pkg_resources
import solution

class TestSolution(unittest.TestCase):
    
    #Testing with picked samples
    def test_Test1(self):
        self.assertEqual(solution.num2word(4), "four")
        self.assertEqual(solution.num2word(33), "thirty-three")
        self.assertEqual(solution.num2word(100), "one hundred")
        
    #Testing against a known solution from the num2words package
    def test_RandomTest(self):
        rand = random.randint(0,100)
        self.assertEqual(solution.num2word(rand), num2words(rand))
        
        rand = random.randint(0,100)
        self.assertEqual(solution.num2word(rand), num2words(rand))
        
        rand = random.randint(0,100)
        self.assertEqual(solution.num2word(rand), num2words(rand))
        
        rand = random.randint(0,100)
        self.assertEqual(solution.num2word(rand), num2words(rand))
        
    #sadly the num2words implementation uses a diffrent scheme to write large numbers, so testing above 1000 is getting false positives in cases where there are no hundreds.
    #without changing the logic in solution.py to a more complicated, but equivalent to num2words, solution is out of the scope of this assignment

if __name__ == "__main__":
    
    required = {"num2words"}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    
    if missing:
        python = sys.executable
        subprocess.check_call([python, "-m", "pip", "install", *missing], stdout=subprocess.DEVNULL)

    from num2words import num2words
    
    unittest.main()