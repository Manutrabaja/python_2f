import sys
# print (sys.path)

import re
text = 'Mi numero de telefono es 56-00-258, el codigo de pais +58, mi de la suerte es 7'

result = re.findall('[0-9]+',text) 
print(result)

import time
timestamp = time.time()
print(timestamp)
local = time.localtime()
result_1 = time.asctime(local) 
print(result_1)

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]

counter = collections.Counter(numbers)
print(counter)