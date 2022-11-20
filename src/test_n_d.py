import sys
import subprocess
import pandas as pd

T = [0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48]

data = dict()
index = []

print("\nRun deep_largeN exper\n")
# for d in [500]:
cur_array = []
d = 500
n = 100000
for t in T:
    cur = subprocess.run(["java", "SSSP", "-a", "0", "-n", f"{n}", "-t", f"{t}", "-d", f"{d}"], capture_output=True)
    cur_array.append(cur.stdout.decode('utf-8'))
    print(f"node: {n}, t: {t}, d: {d}, time: {cur.stdout.decode('utf-8')}\n")
data[5] = cur_array

final = pd.DataFrame(data, index=T).T
final.to_csv(f"./results/n_{n}_d_{d}.csv")
