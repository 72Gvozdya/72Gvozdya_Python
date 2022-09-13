import glob
import re
import csv
sh_version_files = glob.glob("sh_cdp_n*")
for x in sh_version_files:
    l_dev = re.search(r'sh_cdp_n_(\S+)\.', x).group(1)
    print(l_dev)