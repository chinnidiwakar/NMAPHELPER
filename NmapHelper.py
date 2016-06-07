#!/usr/bin/python
import subprocess
print "\033[1;31mCCCCCCCC H      H IIIIIII N      N N      N IIIIIII\033[1;m"
print "\033[1;31mC	 H	H    I	  NN	 N NN	  N    I   \033[1;m"
print "\033[1;37mC	 H	H    I	  NNNN	 N NNNN	  N    I   \033[1;m"
print "\033[1;37mC	 HHHHHHHH    I	  N  NN	 N N  NN  N    I   \033[1;m"
print "\033[1;37mC	 H	H    I	  N   NNNN N   NNNN    I   \033[1;m"
print "\033[1;32mC	 H	H    I	  N	NN N	 NN    I   \033[1;m"
print "\033[1;32mCCCCCCCC H	H IIIIIII N      N N	  N IIIIIII\033[1;m\n"

def prog():
	userinput = raw_input("Enter Ip or Domain You want to Scan: ")
	print "\nOS_detection      = 1"
	print "TCP_connect_scan  = 2"
	print "Syn_scan          = 3"
	print "Fin_scan          = 4"
	print "Xmas_scan         = 5"
	print "Null_scan         = 6"
	print "Version_detection = 7"
	print "Fast_scan         = 8"
	print "Ack_scan          = 9"
	print "UDP_scan          = 10\n"
	scan_type = raw_input("\nEnter the Scan Type you want to perform on the target, Please enter a number[ex:1] : ")
	
	if scan_type == "1":
		subprocess.call(["nmap", "-O", userinput])
	elif scan_type == "2":
		subprocess.call(["nmap", "-sT", userinput])
	elif scan_type == "3":
		subprocess.call(["nmap", "-sS", userinput])
	elif scan_type == "4":
		subprocess.call(["nmap", "-sF", userinput])
	elif scan_type == "5":
		subprocess.call(["nmap", "-sX", userinput])
	elif scan_type == "6":
		subprocess.call(["nmap", "-sN", userinput])
	elif scan_type == "7":
		subprocess.call(["nmap", "-sV", userinput])
	elif scan_type == "8":
		subprocess.call(["nmap", "-F", userinput])
	elif scan_type == "9":
		subprocess.call(["nmap", "-sA", userinput])
	elif scan_type == "10":
		subprocess.call(["nmap", "-sU", userinput])
	else:
		print "An Invalid Option"
	return;
	
def redo():
	redo = raw_input("Do you want to Scan Again? Give Y to Continue any other to Quit: ")
	while redo == "Y":
		prog()
	else:
		print "Good Bye"
		quit()

prompt = raw_input("\nWelcome to Nmap Help. Give Y to Continue or any other key to Quit: ")
if prompt == "Y":
	prog()
	redo()
else:
	print "Good Bye"
	quit()
