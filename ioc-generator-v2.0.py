# Include standard modules
import argparse
import time
from pathlib import Path
import hashlib

# //////////////////////////////////////////////
#
# Python Automated IOC Generator v2.0
#
# File Name, MD5 hash value,
# SHA-1 hash value, SHA-256 hash value,
# and File Size in Bytes.
#
# //////////////////////////////////////////////

# Initiate the parser
parser = argparse.ArgumentParser(description="Python Automated IOC Generator v2.0 by Brett Fullam")
parser.add_argument("-f", "--file", help="select file as input")
parser.add_argument("-d", "--directory", help="select directory as input")
parser.add_argument("-V", "--version", help="show program version", action="store_true")


#/////////////  BEGIN -- timestamp

# grab the epoch timestamp at run time and convert to human-readable for the artifact output document footer information
timeStamp = time.time()

# convert epoch timestamp to human-readable date time formatted
report_time = time.strftime('%c', time.localtime(timeStamp))

# create a custom string to be included at the end of the generated output
report_time_footer = str('IOCs generated on: ') + report_time + str('\ncreated by Python Automated IOC Generator') + str('\n\n')

#/////////////  END -- timestamp


#/////////////  BEGIN -- Generate IOCs
#///////////// File Name, MD5 hash, SHA-1 hash, SHA-256 hash, File size in bytes

# create and open a file named 'output.txt' to write our data to
f = open("output.txt", "w")

def iocGrab(arg):

    # store a single entry value from direct user input, or from the directory_as_input() function
    target_file = arg

    # use Path module to access .stat results -- 'name' to grab the file name, and 'st_size' to grab the file size in bytes    
    file_ = Path(target_file)
    fileName = (file_.name)
    fileStats = (file_.stat().st_size)

    # Grab the name of the file, create a custom string, print output to screen, as well as write to 'output.txt'
    fileNameOutput = "\nFile name: " + fileName + "\n\n"
    print(fileNameOutput)
    f.write(fileNameOutput)

    # /// Hashing START

    # Open and read the file contents to create the MD5 hash of the file
    md5_hash = hashlib.md5()
    with open(target_file,"rb") as f4:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f4.read(4096),b""):
            md5_hash.update(byte_block)
        md5hash = (md5_hash.hexdigest())

    # Output the MD5 hash value created by hashlib.md5() as reference
    md5Data = str("MD5: " + md5hash + "\n")
    print(md5Data)
    f.write(md5Data)


    # Open and read the file contents to create the SHA-1 hash of the file
    sha1_hash = hashlib.sha1()
    with open(target_file,"rb") as f3:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f3.read(4096),b""):
            sha1_hash.update(byte_block)
        sha1hash = (sha1_hash.hexdigest())

    # Output the SHA-1 hash value created by hashlib.sha1() as reference
    sha1Data = str("SHA-1: " + sha1hash + "\n")
    print(sha1Data)
    f.write(sha1Data)


    # Open and read the file contents to create the SHA-256 hash of the file
    sha256_hash = hashlib.sha256()
    with open(target_file,"rb") as f2:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f2.read(4096),b""):
            sha256_hash.update(byte_block)
        sha256hash = (sha256_hash.hexdigest())

    # Output the SHA-256 hash value created by hashlib.sha256() as reference
    sha256Data = str("SHA-256: " + sha256hash + "\n")
    print(sha256Data)
    f.write(sha256Data)

    # /// Hashing END

    # Create a custom string to show the file size in bytes
    fileSizeBytes = ("Size in bytes:  " + str(fileStats) + ("\n\n"))

    # Store the 'size' value as fileSizeBytes, create a custom string, print output to screen, as well as write to 'output.txt'
    print(fileSizeBytes)
    f.write(fileSizeBytes)

    return

#/////////////  END -- Generate IOCs
#///////////// File Name, MD5 hash, SHA-1 hash, SHA-256 hash, File size in bytes

#/////////////  BEGIN -- Directory as input

def directory_as_input(arg):

    # store the directory_as_input value in the path_of_the_directory variable
    path_of_the_directory = arg

    # initialize list 'i'
    i = [ ]

    # use Path to get the file paths for each file in the directory
    entries = Path(path_of_the_directory)
    for i in entries.iterdir():
        # send a concatenated value using "i.parent" and "i.name" to create the relative path for each file
        # which will appears as "directory-indicated/filename" as the loop iterates over the list 'i"
        grabPath = (i.parent / i.name)
        # the 'grabPath' value is then passed to the iocGrab() function
        iocGrab(grabPath)

    f.write(report_time_footer)
    f.close()

    print(report_time_footer)

#/////////////  END -- Directory as input


# Read arguments from the command line
args = parser.parse_args()


# Check for --file or -f
if args.file:
    iocGrab(args.file)
    print(report_time_footer)
    f.write(report_time_footer)
    f.close()
# Check for --directory or -d
elif args.directory:
    directory_as_input(args.directory)
# Check for --version or -V
elif args.version:
    print("IOC Generator version 2.0")
# Print usage information if no arguments are provided
else:
    print("usage: ioc-generator-v2.0.py [-h] [-f FILE] [-d DIRECTORY] [-V]")