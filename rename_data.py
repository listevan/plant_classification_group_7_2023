data_dir = "/Users/stevenli/SigAida/data/images/" #change to data directory
import os
ov = []
v = []
for f in os.listdir(data_dir):
    h = list(f)
    a = [[]]
    j = 0
    if (h[0].isnumeric()):
        for i in range(len(h)):
            if (h[i].isnumeric()):
                if (i == 0):
                    a[0].append(h[i])
                elif (h[i - 1].isnumeric() == False):
                    j += 1
                    a.append([])
                    a[j].append(h[i])
                else:
                    a[j].append(h[i])
        ov.append(a)
        v.append(f)

i = 99999                
for a,b in zip(ov, v):
    filename = "l" + ''.join(a[2]) + str(i) + ".tif"
    i -= 1
    os.rename(data_dir + b, data_dir + filename)
