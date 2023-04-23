import os
import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if error:
        print(f"Error: {error.decode('utf-8')}")
    else:
        print(f"Output: {output.decode('utf-8')}")

def install_ns3():
    # Update the system
    print("Updating the system...")
    run_command("sudo apt-get update")

    # Install prerequisites
    print("Installing prerequisites...")
    run_command("sudo apt-get install -y build-essential autoconf automake libxmu-dev python3-pygraphviz cvs mercurial bzr git cmake p7zip-full python3-matplotlib python-tk python3-dev qt5-default gnuplot-x11 wireshark")

    # Download ns-3
    print("Downloading ns-3...")
    run_command("wget https://www.nsnam.org/release/ns-allinone-3.33.tar.bz2")

    # Extract ns-3
    print("Extracting ns-3...")
    run_command("tar xjf ns-allinone-3.33.tar.bz2")

    # Change directory to ns-allinone-3.33
    os.chdir("ns-allinone-3.33")

    # Build ns-3
    print("Building ns-3...")
    run_command("./build.py --enable-examples --enable-tests")

    # Configure waf
    print("Configuring waf...")
    run_command("cd ns-3.33 && ./waf configure --enable-examples --enable-tests")

    # Build ns-3 using waf
    print("Building ns-3 using waf...")
    run_command("cd ns-3.33 && ./waf")

    print("ns-3 installation completed.")

if name == "__main__":
    install_ns3()
