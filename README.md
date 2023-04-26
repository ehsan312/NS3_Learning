# NS3 Learning

_Learn NS3 for simulation & impelementation network project's_

## What is NS3:

"***ns-3*** is a discrete-event network simulator for Internet systems, targeted primarily for research and educational use. ns-3 is free, open-source software, licensed under the GNU GPLv2 license, and maintained by a worldwide community."

official website: [Click To See](https://www.nsnam.org/) 

[comment]: # (The best way to learn is read official Docs.)


### Propertise

- ability to simulate a wide range of network technologies and protocols (wireless , Internet protocols, and routing protocols)
-  NS3 supports both IPv4 and IPv6 protocols 
-  models for various wireless technologies (WiFi, WiMAX, and LTE)
-  scalability (NS3 can simulate networks with thousands of nodes, making it suitable for large-scale network simulations)
-  The ability to simulate different types of traffic and network topologies, which makes it useful for evaluating the performance of complex networks under different conditions.
-  NS3 is an open-source tool, which means that its source code is available to the public, and users can modify it to suit their needs. This property allows researchers and developers to customize NS3 to meet their specific requirements and add new features and models to the simulator.

### Prerequisite for lrearning NS3

To learn NS-3 (Network Simulator 3), you should consider the following prerequisites:

- C++ programming language: NS-3 is written in C++, and to work with it, you need to be proficient in this language.

- Python programming language: Some scripts and auxiliary tools in NS-3 are written in Python. Therefore, basic Python knowledge can be helpful.

- Computer networking concepts: To make the most of NS-3, you should be familiar with fundamental computer networking concepts such as the OSI model, various protocols, routing, etc.

- Telecommunications engineering concepts: Understanding basic telecommunication concepts like modulation, encoding, data transmission, etc., can be helpful when working with NS-3.

- Data analysis skills: To analyze the results of NS-3 simulations, you should be familiar with data analysis tools such as charts, statistics, and probability.

- Research skills: To use NS-3 in research projects, you need to be familiar with research methods and scientific paper writing.

With the above prerequisites in mind, you can study relevant resources and practice to learn NS-3 effectively.

### 1. Instalation

To install NS3, you can follow these steps:

* Open a terminal window on your Linux machine.

* At first update your linux system:

<pre>
<code id="my-code-block" data-clipboard-target="#my-code-block">
sudo apt-get install update && apt-get install upgarde -y 
</pre>

>    Install the required dependencies by running the following command:

<pre>
<code id="my-code-block" data-clipboard-target="#my-code-block">
sudo apt-get install build-essential autoconf automake libxmu-dev libxml2-dev python3-pygraphviz cvs mercurial bzr git cmake p7zip-full python3-matplotlib python-tk python3-dev qtbase5-dev qtchooser gnuplot-x11 wireshark
</code>
</pre>


* Download the NS3 source code from the official website: https://www.nsnam.org/releases/ns-3-38/
    Extract the downloaded file to a directory of your choice.
    Navigate to the extracted directory in the terminal.
    
>>    First WAY  >> Run the following commands to configure and build NS3:

<pre>
<code id="my-code-block" data-clipboard-target="#my-code-block">
cd ~
wget https://www.nsnam.org/release/ns-allinone-3.33.tar.bz2

tar xjf ns-allinone-3.33.tar.bz2

cd ns-allinone-3.33

./build.py --enable-examples --enable-tests

</code>
</pre>

* Run the following commands to configure and build NS3:

<pre>
<code id="my-code-block" data-clipboard-target="#my-code-block">
cd ns-3.33
./waf configure --enable-examples --enable-tests
./waf

</code>
</pre>

>>    Scound WAY  >> Run the following commands to configure and build NS3:

<pre>
<code id="my-code-block" data-clipboard-target="#my-code-block">

sudo apt-get update

sudo apt-get install build-essential autoconf automake libxmu-dev python3-pygraphviz cvs mercurial bzr git cmake p7zip-full python3-matplotlib python3-tk python3-dev qt5-default gnuplot-x11 wireshark

cd ns-3-dev
./ns3 configure --enable-examples --enable-tests
./ns3

</code>
</pre>

* Run the following commands to configure and build NS3:

<pre>
<code id="my-code-block" data-clipboard-target="#my-code-block">

./ns3 --run hello-simulator

</code>
</pre>

 
 * Once the build process is complete, you can run the examples provided in the examples/ directory.

Note: NS3 requires several dependencies to be installed on your system, such as Python, GCC, and Boost. Make sure to install these dependencies before attempting to build NS3.


### 2. Implemetation 



### Install script 

You can setup Ns3 on ubuntu by script ***setup.py***


<pre>
<code id="my-code-block" data-clipboard-target="#my-code-block">
git clone https://github.com/ehsan312/NS3_Learning.git
python3 python_script.py
</code>
</pre>



