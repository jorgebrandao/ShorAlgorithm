Version: Python 3.5.4



Example 1: (Shor for N=15 and a=4)

$ python
>>> from shor import *
>>> #for 25 iterations
>>> sh(25)
>>> 
>>> exit()
$

Example 2: QFT3,4,5 and all inverses(all for 100 iterations)

$ python
>>> from adder import *
>>> 
>>> qft3(100)
>>> invqft3(100)
>>> qft4(100)
>>> invqft4(100)
>>> qft5(100)
>>> 
>>> exit()
$

Example 3: (a+b) and (a+b)mod N (all for 100 iterations)
$ python
>>> from adder import *
>>> 
>>> adder33(100)#all parameters for a and b can be changed in the file
>>> addmod(100)#only b can be changed in the file
>>>
>>> exit()
$
