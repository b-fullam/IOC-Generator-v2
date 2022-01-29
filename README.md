# IOC-Generator-v2
Quickly generate common Indicators of Compromise (IOCs) from files with Python.

### Quickly generate common Indicators of Compromise (IOCs) from files with Python.

An analyst can quickly generate common Indicators of Compromise (IOCs) from a single file or directory that can then be incorporated into tools like Mandiant's IOCe.

``` noLineNumbers
usage: ioc-generator-v2.0.py [-h] [-f FILE] [-d DIRECTORY] [-V]

Python Automated IOC Generator v2.0 by Brett Fullam

options:
  -h, --help                show this help message and exit
  -f FILE, --file FILE      select file as input
  -d DIRECTORY, --directory DIRECTORY
                            select directory as input
  -V, --version             show program version
```

The file is processed and each of the IOCs are generated and output to the screen, as well as to a text file called "output.txt" which is located in the same directory the python script resides.

``` noLineNumbers
File name: 2innocent.pdf


MD5: 2942bfabb3d05332b66eb128e0842cff

SHA-1: 90ffd2359008d82298821d16b21778c5c39aec36

SHA-256: 3df79d34abbca99308e79cb94461c1893582604d68329a41fd4bec1885e6adb4

Size in bytes:  13264


IOCs generated on: Sat Jan 29 08:41:22 2022
created by Python Automated IOC Generator
```

For more information about this script, check out my article on "[Security Automation with Python — Quickly generate common IOCs from files with Python](https://www.brettfullam.com/security-automation-with-python-quickly-generate-common-io-cs-from-files-with-python  "Quickly generate common IOCs from files with Python")." 

## Getting Started

1. Download the script or use git to clone the repository

2. No extra dependencies needed.  This script was created using Python3, and all of the necessary dependencies are already included in the standard Python installation.

3. The repository includes the following:

* The finished version of the script using only using standard Python libraries (file name ending in ".py")
* License
* README.md file
* 2innocent.pdf sample file for testing
* ioc-samples directory that contains 2 sample files for testing

``` nolinenumbers
.
├── 2innocent.pdf
├── LICENSE
├── README.md
├── ioc-generator-v2.0.py
└── ioc-samples

1 directory, 4 files
```
The directory, which contains 2innocent.pdf and highly_malicious.txt, are harmless sample files for you to test the "directory_as_input" functionality included in the script to see first hand how multiple files are processed.