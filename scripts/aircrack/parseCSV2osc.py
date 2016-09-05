import subprocess, glob, time, csv, random

# airodump-ng is running and logging the results into a csv file
# with the following command: sudo airodump-ng -o csv -w manuf mon0
# subprocess looks for the last edited csv file in current folder
# this file is parsed by the csv module to find the number of data packets that have passed through the network since the last check

csvs=subprocess.Popen("ls -t1 *csv | head -1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
csv_last=csvs.communicate()[0].strip()

key_value=(' # IV') # look up this value in the scan dump

def lookup(dump):
    datas=[]
    results=[]
    scan=open(dump, "rU")
    next(scan)
    scanDict=csv.DictReader((line.replace('\0','') for line in scan), delimiter=',')
    #return scanDict
    for aDict in scanDict:
        print aDict
    # for adict in scanDict:
    #     if adict.has_key(key_value) and adict.get(key_value)!=None:
    #         try:
    #             datas.append(int(adict.get(key_value)))
    #         except:
    #             pass
    #datas.sort(reverse=True)
    # for i in range(4):
    #     results.append(datas[i])
    # return results

new_packet_list=lookup(csv_last)

print new_packet_list
