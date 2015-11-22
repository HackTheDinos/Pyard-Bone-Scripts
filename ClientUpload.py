import os,sys, getopt,pysftp, uuid,urllib

host = "pyradact.cloudapp.net"
username="azureuser"
pwd = "HackTheDinos01"
destpath = "/home/azureuser/tmpdata"
checkURL = "http://pyradact.cloudapp.net:8080/check/"

def main(argv):
    inputpath = ''
    specimenid = ''
    try:
        opts, args = getopt.getopt(argv,"hi:s:",["ifile=","specimenid="])
    except getopt.GetoptError:
        print ('ClientUpload.py -i <inputdir> -s <specimenid>')
        sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
	        print('ClientUpload.py -i <inputdir> -s <specimen>')
	        sys.exit()
      elif opt in ("-i", "--ifile"):
	        inputpath = arg
      elif opt in ("-s", "--specimenid"):
	        specimenid = arg
    upload(inputpath,specimenid)

def upload(inputpath,specimenid):
    guid = uuid.uuid4()
    if(not os.path.isdir(inputpath)):
        print(inputpath, "not directory, exiting")
        sys.exit(2)
    if(len(specimenid) >0):
        idfp = open (inputpath+"/id.txt","w")
        idfp.write(specimenid)
        idfp.close()
        try:
            with urllib.request.urlopen(checkURL + specimenid) as response:
                return "OK"
        except urllib.error.HTTPError as e:
            print("ID already exists")
            sys.exit(2)
    with  pysftp.Connection(host,username=username,password=pwd) as sftp:
        print(destpath+"/"+guid.hex+"/")
        sftp.put_r(inputpath,destpath+"/"+guid.hex +"/")
        
if(__name__ == "__main__"):
   main(sys.argv[1:])
