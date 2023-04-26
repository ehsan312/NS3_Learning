import os

# Install ns-3
os.system("git clone https://gitlab.com/nsnam/ns-3-allinone.git")
os.chdir("ns-3-allinone")
os.system("./download.py -n ns-3.33")
os.system("./build.py")

# Run example
os.chdir("../ns-3-allinone/ns-3.33")
os.system("/waf configure")
os.system("./waf --run scratch/wifi-simple-adhoc")



