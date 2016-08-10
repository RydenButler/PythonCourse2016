
def binarify(num): 
    """convert positive integer to base 2"""
    if num<=0: return '0'
    digits = []
    while num > 0:
		digits.insert(0,str(num%2))
		num /= 2
    return ''.join(digits)
    
def int_to_base(num, base):
    """convert positive integer to a string in any base"""
    if num<=0: return '0'
    digits = []
    while num > 0:
		digits.insert(0,str(num%base))
		num /= base
    return ''.join(digits)

def base_to_int(string, base):
    """take a string-formatted number and its base and return the base-10 integer"""
    if string=="0" or base <= 0 : return 0 
    number = 0
    for i in range(len(string)):
    	number += base ** (len(string) - i - 1) * int(string[i])
    return number
    
def flexibase_add(str1, str2, base1, base2):
	return base_to_int(str1, base1) + base_to_int(str2, base2)
	
def flexibase_multiply(str1, str2, base1, base2):
    """multiply two numbers of different bases and return the product"""
    return base_to_int(str1, base1) * base_to_int(str2, base2) 
    
def romanify(num):
	"""given an integer, return the Roman numeral version"""
	Latin = {0: '', 1: 'I', 2: 'II', 3:'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VII', 
		9: 'IX', 10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX',
		80:'LXXX', 90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
		600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M'}
	Rome = []
	while num > 1000:
		num -= 1000
		Rome.append('M')
	Number = str(num)
	Number = [dec for dec in Number]
	if len(Number) == 3:
		Hundred = int(Number[-3])*100
		Rome.append(Latin[Hundred])
		Ten = int(Number[-2])*10
		Rome.append(Latin[Ten])
		Digit = int(Number[-1])
		Rome.append(Latin[Digit])
	if len(Number) == 2:
		Ten = int(Number[-2])*10
		Rome.append(Latin[Ten])
		Digit = int(Number[-1])
		Rome.append(Latin[Digit])
	elif len(Number) == 1:	
		Digit = int(Number[-1])
		Rome.append(Latin[Digit])
	
	return ''.join(Rome) # or face the wrath of the Legion
  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.