#!/usr/bin/python
import StringIO
import getopt
import hashlib
import sys
import os
print "  "
print "Python Hash-Cracker"
print "Version 3.0-2 Stable"
more = "config/add.txt"

def info():
  print " "
  print "Information:"
  print "[*]Options:"
  print "[*](-h) Hash"
  print "[*](-t) Type [See supported hashes]"
  print "[*](-w) Wordlist"
  print "[*](-n) Numbers bruteforce"
  print "[*](-v) Verbose [{WARNING}Slows cracking down!]"
  print "[*]Examples:"
  print "[>]./Hash-Cracker.py -h <hash> -t md5 -w DICT.txt"
  print "[>]./Hash-Cracker.py -h <hash> -t sha384 -n -v"
  print "[*]Supported Hashes:"
  print "[>]md5, sha1, sha224, sha256, sha384, sha512"
  print "[*]Thats all folks!\n"

def check_os():
    if os.name == "nt":
        operating_system = "windows"
    if os.name == "posix":
        operating_system = "posix"
    return operating_system

def definepath():
    if check_os() == "posix":
        if os.path.isfile("fake-update"):
            return os.getcwd()
        else:
            return "/opt/Hermies"
    else:
        return os.getcwd() 

def check_config(param):
    fileopen = file("%s/config/config.txt" % (definepath()), "r")
    for line in fileopen:
        line=line.rstrip()
        #print line
        if line.startswith(param) != "#":
           if line.startswith(param):
                line = line.rstrip()
                line = line.replace('"', "")
                line = line.replace("'", "")
                line = line.split("=")
                return line[1]

class hash:
  def iterate(self,hash,mode=0):
	if mode == 0:
		h2 = hashlib.sha256
	else:
		h2 = hashlib.sha512
		#print "Final hash "+hash
	return h2(str(hash)+str(hash)).hexdigest()
  def hashcrack(self, hash, type,salt1,salt2):
    self.num = 0
    if (type == "md5"):
       h = hashlib.md5
    elif (type == "sha1"):
       h = hashlib.sha1
    elif (type == "sha224"):
       h = hashlib.sha224
    elif (type == "sha256"):
       h = hashlib.sha256
    elif (type == "sha384"):
       h = hashlib.sha384
    elif (type == "sha512"):
       h = hashlib.sha512
    else:
       print "[-]Is %s a supported hash type?" % type
       exit()
    wordlist1 = open(wordlist, "r")
    wordlist2 = wordlist1.read()
    buf = StringIO.StringIO(wordlist2)
    while True:
       line = buf.readline().strip()	   
       if (line == ""):
           print "\n[-]Hash not cracked:"
           print "[*]Reached end of wordlist"
           print "[*]Try another wordlist"
           print "[*]Words tryed: %s" % self.num
           break
       part1 = self.iterate(salt1)
       part2 = self.iterate(line)
       part3 = self.iterate(salt2)
       hash3 = self.iterate(part1+part2+part3,1)
       #print "Computed hash " + hash3 + "\nfrom "+part1+"\n"+part2+"\n"+part3 + " for password " + line
       if (ver == "yes"):
           sys.stdout.write('\r' + str(line) + ' ' * 20)
           sys.stdout.flush()
       if (hash3 == hash.lower()):
           print "[+]Hash is: %s" % line
           print "[*]Words tryed: %s" % self.num
           break
       else:
           self.num = self.num + 1


  def hashcracknum(self, hash, type,salt1,salt2):
    self.num = 0
    if (type == "md5"):
       h = hashlib.md5
    elif (type == "sha1"):
       h = hashlib.sha1
    elif (type == "sha224"):
       h = hashlib.sha224
    elif (type == "sha256"):
       h = hashlib.sha256
    elif (type == "sha384"):
       h = hashlib.sha384
    elif (type == "sha512"):
       h = hashlib.sha512
    else:
       print "[-]Is %s a supported hash type?" % type
       exit()
    while True:
       line = "%s" % self.num
       line.strip()
       hash2 = h(line).hexdigest().strip()
       if (ver == "yes"):
           sys.stdout.write('\r' + str(line) + ' ' * 20)
           sys.stdout.flush()
       if (hash2.strip() == hash.strip().lower()):
           print "[+]Hash is: %s" % line
           break
       else:
         self.num = self.num + 1

def main(argv):
  what = check_os()
  print "[Running on %s]\n" % what
  global hash1, type, wordlist, line, ver, numbrute , custom
  hash1 = None
  type = None
  wordlist = None
  line = None
  ver = None
  numbrute = None
  custom = None
  try:
      opts, args = getopt.getopt(argv,"ih:t:w:nv",["ifile=","ofile="])
  except getopt.GetoptError:
      print '[*]./Hash-Cracker.py -t <type> -h <hash> -w <wordlist>'
      print '[*]Type ./Hash-Cracker.py -i for information'
      sys.exit(1)
  for opt, arg in opts:
      if opt == '-i':
          info()
          sys.exit()
      elif opt in ("-t", "--type"):
          type = arg
      elif opt in ("-h", "--hash"):
          hash1 = arg
      elif opt in ("-w", "--wordlist"):
          wordlist = arg
      elif opt in ("-v", "--verbose"):
          ver = "yes"
      elif opt in ("-n", "--numbers"):
          numbrute = "yes"
      elif opt in ("-m", "--mode"):
          custom = "yes"		 
  if not (type and hash1):
      print '[*]./Hash-Cracker.py -t <type> -h <hash> -w <wordlist>'
      sys.exit()
  if (type == "hashbrowns"):
      if (hash1 == "hashbrowns"):
          if (wordlist == "hashbrowns"):
              print "     ______"
              print "^. .^      \~"
              print " (oo)______/"
              print "   WW  WW"
              print " What a pig!!! "
              exit()
  values = hash1.split('$')
  salt1 = values[0]
  salt2 = values[2]
  hash1 = values[1]
  print "Found salt1:"+salt1
  print "Found salt1:"+salt2
  print "[*]Hash: %s" % hash1
  print "[*]Hash type: %s" % type
  print "[*]Wordlist: %s" % wordlist
  print "[+]Cracking..."
  try:
      if (numbrute == "yes"):
         h = hash()
         h.hashcracknum(hash1, type,salt1,salt2)
      else:
         h = hash()
         h.hashcrack(hash1, type,salt1,salt2)

  except IndexError:
        print "\n[-]Hash not cracked:"
        print "[*]Reached end of wordlist"
        print "[*]Try another wordlist"
        print "[*]Words tryed: %s" % h.num
  except KeyboardInterrupt:
        print "\n[Exiting...]"
        print "Words tryed: %s" % h.num
  except IOError:
        print "\n[-]Couldn't find wordlist"
        print "[*]Is this right?"
        print "[>]%s" % wordlist
if __name__ == "__main__":
    main(sys.argv[1:])
