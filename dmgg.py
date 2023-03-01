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

#sys.argv[1]=vvv  #activate this line for autodetection (not sure it is working ok)

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
            if xored_error:
                for a in range(nbchips):
                 if i>=a*256*(1+int(i/(256*nbchips))) and i<(a+1)*256*(1+int(i/(256*nbchips))):  # knowing the chipsize could fix this
                  if nbchips>8:
                   if a==0 and amaifost[0]==0:
                    amaifost[0]=1
                    faultychips=faultychips+1
                    print("chip 5 is faulty at address: ",i)
                    break
                   if a==1 and amaifost[1]==0:
                    amaifost[1]=1
                    faultychips=faultychips+1
                    print("chip 7 is faulty at address: ",i)
                    break
                   if a==2 and amaifost[2]==0:
                    amaifost[2]=1
                    faultychips=faultychips+1
                    print("chip 6 is faulty at address: ",i)
                    break
                   if a==3 and amaifost[3]==0:
                    amaifost[3]=1
                    faultychips=faultychips+1
                    print("chip 8 is faulty at address: ",i)
                    break
                   if a==4 and amaifost[4]==0:
                    amaifost[4]=1
                    faultychips=faultychips+1
                    print("chip 3 is faulty at address: ",i)
                    break
                   if a==5 and amaifost[5]==0:
                    amaifost[5]=1
                    faultychips=faultychips+1
                    print("chip 1 is faulty at address: ",i)
                    break
                   if a==6 and amaifost[6]==0:
                    amaifost[6]=1
                    faultychips=faultychips+1
                    print("chip 4 is faulty at address: ",i)
                    break
                   if a==7 and amaifost[7]==0:
                    amaifost[7]=1
                    faultychips=faultychips+1
                    print("chip 2 is faulty at address: ",i)
                    break
                   if a==8 and amaifost[8]==0:
                    amaifost[8]=1
                    faultychips=faultychips+1
                    print("chip 11 is faulty at address: ",i)
                    break
                   if a==9 and amaifost[9]==0:
                    amaifost[9]=1
                    faultychips=faultychips+1
                    print("chip 9 is faulty at address: ",i)
                    break
                   if a==10 and amaifost[10]==0:
                    amaifost[10]=1
                    faultychips=faultychips+1
                    print("chip 12 is faulty at address: ",i)
                    break
                   if a==11 and amaifost[11]==0:
                    amaifost[11]=1
                    faultychips=faultychips+1
                    print("chip 10 is faulty at address: ",i)
                    break
                   if a==12 and amaifost[12]==0:
                    amaifost[12]=1
                    faultychips=faultychips+1
                    print("chip 13 is faulty at address: ",i)
                    break
                   if a==13 and amaifost[13]==0:
                    amaifost[13]=1
                    faultychips=faultychips+1
                    print("chip 15 is faulty at address: ",i)
                    break
                   if a==14 and amaifost[14]==0:
                    amaifost[14]=1
                    faultychips=faultychips+1
                    print("chip 14 is faulty at address: ",i)
                    break
                   if a==15 and amaifost[15]==0:
                    amaifost[15]=1
                    faultychips=faultychips+1
                    print("chip 16 is faulty at address: ",i)
                    break
                  if nbchips==8:
                   if (a==0  and amaifost[0]==0) or (a==1 and amaifost[1]==0):
                    amaifost[0]=1
                    amaifost[1]=1
                    faultychips=faultychips+1
                    print("chip 3 and/or 4 is faulty at address: ",i)
                    break
                   if (a==2  and amaifost[2]==0) or (a==3 and amaifost[3]==0):
                    amaifost[2]=1
                    amaifost[3]=1
                    faultychips=faultychips+1
                    print("chip 1 and/or 2 is faulty at address: ",i)
                    break
                   if (a==4  and amaifost[4]==0) or (a==5 and amaifost[5]==0):
                    amaifost[4]=1
                    amaifost[5]=1
                    faultychips=faultychips+1
                    print("chip 5 and/or 6 is faulty at address: ",i)
                    break
                   if (a==6  and amaifost[6]==0) or (a==7 and amaifost[7]==0):
                    amaifost[6]=1
                    amaifost[7]=1
                    faultychips=faultychips+1
                    print("chip 7 and/or 8 is faulty at address: ",i)
                    break
                if not bad_addresses:
                    firstbadadress=hex(i)
                if xored_error not in bad_addresses:
                    bad_addresses[xored_error] = [0, []]
                bad_addresses[xored_error][0] += 1
                all_addresses = bad_addresses[xored_error][1]
                if 1:
                    for b in range(8):
                        if xored_error & (1<<b): bad_bits[b] += 1
                if 1:    
                    if len(all_addresses) < 0x4000:
                        all_addresses.append(i)
                    if len(all_errors) < 0x4000:
                        all_errors.append(i)
        if not bad_addresses:
            passed.append(test_name)
            print(color.GREEN+"No faulty chips found")
            print(color.WHITE)

        print(color.WHITE)

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

