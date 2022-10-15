import os
import cgi

from tests import main

print('Content-Type: text/plain; charset=UTF-8')
print('Status: 200')
print()


print('Experiment 1: Benchmark')
print('=======================')
test, total_time = main()