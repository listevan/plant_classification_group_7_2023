import os
data_dir = "/Users/stevenli/SigAida/data/images/"

for f in os.listdir(data_dir):
    h = list(f)
    print(h)
    if h[3] == "9" or h[2] == "9":
        print(f)
        os.remove(data_dir + f)