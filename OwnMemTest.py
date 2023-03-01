 #!/usr/bin/env python3
# Copyright (C) 2017, 2018 Vasily Galkin (galkinvv.github.io)
# This file may be used and  redistributed accorindg to GPLv3 licance.
import sys, os, mmap, math, random, datetime, time
import subprocess


os.system("")
random.seed(12111)
passed = []
faultychips = 0

class color():
    RED = '\033[31m'
    GREEN='\033[32m'
    YELLOW='\033[33m'
    WHITE='\033[37m'


amaifost = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(color.GREEN+"Detected AMD GPU card:")
bbb = ""
q = subprocess.call(['sudo',''])
p = subprocess.Popen(['lspci', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
aaa = str(p).split("\\n\\n")

for i in range(len(aaa)):
 if  "VGA" in aaa[i]:
  if "AMD" in aaa[i]:
   bbb=bbb+aaa[i]

ccc=bbb.split("\\n\\t")
vvv=""

for i in range(len(ccc)):
 print(ccc[i])
 if "Memory" and " pref" in ccc[i]:
  qqq=ccc[i].split(" ")
  vvv=vvv+" "+qqq[2]

print()
print()

print(color.YELLOW+"Possible GPU address: "+vvv)
print(color.WHITE)

def run_test():

    # input processing
    if len(sys.argv) < 2: raise Exception("Usage: " + sys.argv[0] + " C8000000 [mb_to_test]")
    offset = int(sys.argv[1], 16)
    if len(sys.argv) > 3:
        nbchips = int(sys.argv[3], 10)
    else:
        nbchips = 8
        print("default 8 chips no value in command line received from user")
    print("number of chips is set to:",nbchips)
    if len(sys.argv) >= 3:
        bytes_to_test = int(1024 * 1024 * float(sys.argv[2]))
    else:
        bytes_to_test = 1024 * 1024 * 32 // 8

    physmem = os.open("/dev/" + os.environ.get("MEM", "mem"), os.O_RDWR, 777)
    phys_arr = mmap.mmap(physmem, bytes_to_test, offset=offset)

    def bin8(byte):
        return "0b{:08b}".format(byte)

    def verify_no_errors_with_data(data, test_name):
        global faultychips
        if len(phys_arr) > len(data):
            data += b'\x00' * (len(phys_arr) - len(data))
        print("This test is working to detect bad chips. Warning it can give wrong faulty chip number ; only the amount of faulty chips will be good")
        print("count the chips counter-clockwise from right to left with pcie near you")
        phys_arr[:] = data
        data_possibly_modified = phys_arr[:]
        time.sleep(0.5)
        bad_addresses = {}
        all_errors = []
        firstbadadress=0
        bad_bits = [0]*8
        print(color.RED)
        for i in range(len(data)):
            xored_error = data[i] ^ data_possibly_modified[i]


        def totals():
             global faultychips
             total_errors =  sum((v[0] for k, v in bad_addresses.items()))

             print("number of faulty chips= ",faultychips)
             print("Total bytes tested: 4*" + str(len(data)//4))
             print("Total errors count: ", total_errors, " - every ", len(data)/(total_errors+1), " OK: ", len(data) - total_errors)

        totals()

    verify_no_errors_with_data(bytes(random.getrandbits(8) for i in range(len(phys_arr))), "rand")

try:
    for i in range(1):
        run_test()
finally:
     print(color.YELLOW+"\n\nUsage:\npython3 ./dmmg.py b0000000 1 16  \nScript file dmmg.py is on root of the USB if you need to edit ; run lspci -v to find address of your ati card default is b0000000 \n 1 is 1MB of memory \n 16 is the number of memory chips from the card")

