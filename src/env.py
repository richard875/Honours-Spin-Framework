import os
import cgi
from datetime import datetime

from tests import main

print('Content-Type: text/plain; charset=UTF-8')
print('Status: 200')
print()


now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print("Run at:", now)
print('Experiment 1: Benchmark')
print('=======================')
test, total_time = main()