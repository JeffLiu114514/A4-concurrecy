import subprocess
import sys
import pandas as pd

# run different number of threads and delta
T = [0, 1, 2, 4, 8, 16]
N = 1000000
D = [100000000, 50000000, 10000000, 5000000, 1000000]

data = dict()
index = []

print("\nRun extra2 exper\n")
for d in D:
    cur_array = []
    for t in T:
        cur = subprocess.run(["java", "SSSP", "-a", "0", "-n", f"{N}", "-t", f"{t}", "-D", f"{d}"], capture_output=True)
        cur_array.append(cur.stdout.decode('utf-8'))
        print(f"node: {N}, delta: {d}, t: {t}, time: {cur.stdout.decode('utf-8')}\n")
    data[d] = cur_array

final = pd.DataFrame(data, index=T).T
final.to_csv("extra2_experiment.csv")