import os
import cgi
# from benchmarkPolybench.index import main

print('Content-Type: text/plain; charset=UTF-8')
print('Status: 404')
print()

print('Hello, from Python!')

print(1+1)

# compile_file = "gcc -O3 -I src/utilities -I src/linear-algebra/kernels/atax src/utilities/polybench.c src/linear-algebra/kernels/atax/atax.c -DPOLYBENCH_TIME -o atax_time"
# print(compile_file)
# os.system(compile_file)
# cwd = os.name
# print(cwd)
# os.mkdir("123")
# main()

# os.popen("./atax_time")
# print(so)

compile_file = "gcc -O3 -I utilities -I linear-algebra/kernels/atax utilities/polybench.c linear-algebra/kernels/atax/atax.c -DPOLYBENCH_TIME -o atax_time"
execute_file = "./atax_time"
os.system(compile_file)
# so = os.popen(execute_file).read().strip()

# print(os.path.isdir("src"))

# params = cgi.parse()
# print(params)


