import sys
import subprocess
import pandas as pd

N = int(sys.argv[1])
T = [0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48]

data = dict()
index = []


for n in range(N, N + 1, 500):
    cur_array = []
    for t in T:
        cur = subprocess.run(["java", "SSSP", "-a", "0", "-n", f"{N}", "-t", f"{t}"], capture_output=True)
        cur_array.append(float(cur.stdout.decode('utf-8')))
    data[n] = cur_array

final = pd.DataFrame(data, index=T).T
final.to_csv("log.csv")