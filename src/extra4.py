import subprocess
import sys
import pandas as pd

# run different number of threads and delta
T = [0, 1, 4]
N = [100, 1000, 5000, 10000, 50000, 100000]


data = dict()
index = []

print("\nRun extra2 exper\n")
for n in N:
    cur_array = []
    for t in T:
        cur = subprocess.run(["java", "SSSP", "-a", "0", "-n", f"{n}", "-t", f"{t}"], capture_output=True)
        cur_array.append(cur.stdout.decode('utf-8'))
        print(f"node: {n}, t: {t}, time: {cur.stdout.decode('utf-8')}\n")
    data[n] = cur_array

final = pd.DataFrame(data, index=T)
final.to_csv("./results/extra4.csv")