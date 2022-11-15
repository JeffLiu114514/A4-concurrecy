import subprocess
import sys

# run different number of threads and delta
T = [1, 2, 4, 8, 16, 32, 48]
N = 10000
D = [2000000000, 300000000, 100000000, 100000, 5000]

data = dict()
index = []

for d in D:
    cur_array = []
    for t in T:
        cur = subprocess.run(["java", "SSSP_extra", "-a", "0", "-n", f"{N}", "-t", f"{t}", "-D", f"{d}"], capture_output=True)
        cur_array.append(float(cur.stdout.decode('utf-8')))
    data[d] = cur_array

final = pd.DataFrame(data, index=T)
final.to_csv("log_extra2.csv")