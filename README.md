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

>    Install the required dependencies by running the following command:

<pre> sudo apt-get install gcc g++ python python-dev mercurial bzr gdb valgrind gsl-bin libgsl-dev libgslcblas0 libgslcblas0-dev flex bison tcpdump sqlite sqlite3 libsqlite3-dev libxml2 libxml2-dev libgtk2.0-0 libgtk2.0-dev uncrustify doxygen graphviz imagemagick texlive texlive-latex-extra texlive-generic-extra texlive-generic-recommended texinfo dia texlive-font-utils python-pygraphviz python-kiwi python-pygoocanvas libgoocanvas-dev python-pygccxml </pre>

* Download the NS3 source code from the official website: https://www.nsnam.org/releases/ns-3-38/
    Extract the downloaded file to a directory of your choice.
    Navigate to the extracted directory in the terminal.
    Run the following commands to configure and build NS3:

' ./waf configure
./waf build'

 
 * Once the build process is complete, you can run the examples provided in the examples/ directory.

Note: NS3 requires several dependencies to be installed on your system, such as Python, GCC, and Boost. Make sure to install these dependencies before attempting to build NS3.

<pre>
<code id="my-code-block" data-clipboard-target="#my-code-block">
// Your code here
</code>
</pre>

### 2. Implemetation 

### Install script 

You can setup Ns3 on ubuntu by script ***setup.py***

<pre> To run the setup script, use the following command:
s`python3 setup.py` </pre>


