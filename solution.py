#!/usr/bin/env python3
#Programmiertask VOITH
#Author: Valentin Hofrichter
#v0.0.2

import sys

def main(args):
    """The main() function will validate the input and can be used to change the range of the accepted numbers.

    Args:
        args (list): if provided with a list with two items that can be interpreted as numbers, the lower bound of accepted numbers will be set
        to the first and the upperBound to the second.
    """
    
    if len(args) == 2:
        try:
            lowerBound = int(args[0])
            upperBound = int(args[1])
        except (ValueError):
            print("Usage: solution.py lowerBound upperBound")
            exit()
    else:
        lowerBound = 0
        upperBound = 100000
    
    try:
        num = int(input("Please enter a Number: "))
    except (ValueError):
        print("Not a Number!")
        exit()
        
    
    if num >= lowerBound and num <= upperBound:
        print(f"The Number is {num2word(num)}.\n")
    else:
        print(f"Number {num} is out of range ({lowerBound}, {upperBound}).")

def num2word(num):
    """This function will convert any positive integer between 0 and 9999 into an equivalent english numeral.

    Args:
        num (int): number

    Returns:
        str: string representation of the provided number
    """
    
    lowerNumbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]
    upperNumbers = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    magnitudes = ["thousand", "million"]
    
    #edge case
    if num == 0:
        return "zero"
        
    #splitting the number into useful digits
    digits = list()
    
    while num > 0:
        digits.append(num % 1000)
        num //= 1000
    
    #construction of the numerals
    t = 0
    res = ""
    for n in digits:
        if t == 0:
            if n <= 15:
                res = res + lowerNumbers[n]
        
            elif n > 15 and n <= 19:
                res = res + f"{lowerNumbers[n % 10]}teen"
            
            else:
                if n // 100 == 0:
                    if n % 10 == 0:
                        res = res + f"{upperNumbers[(n // 10) - 2]}"
                    else:
                        res = res + f"{upperNumbers[(n // 10) - 2]}-{lowerNumbers[n % 10]}"
                else:
                    if n % 100 != 0:
                        res = res + f"{lowerNumbers[n // 100]} hundred and {num2word(n % 100)}"
                    else:
                        res = res + f"{lowerNumbers[n // 100]} hundred"
            t += 1
        else:
            res = f"{num2word(n)} {magnitudes[t-1]} and " + res
            t += 1
                
    return res


if __name__ == "__main__": 
    main(sys.argv[1:])