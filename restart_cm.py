#################
#@author maniiyer
#################

import paramiko
import time
import sys
from paramiko.ssh_exception import AuthenticationException, SSHException

print "[logger.info] This will restart the Cloudera Manager"
print "[logger.info] Retrieving the host ip"

#This will extract the hostip from the extract_ip.py
print "[logger.info] Enter the hostname / ip where the cloudera manager is located"
cm_host = raw_input()
print "[logger.info] Extracted the cloud era ip and it is: " + cm_host

#Setting the SSH Credentials and the command to be passed
print "[logger.info] Enter the username for ssh" 
user = raw_input()
print "[logger.info] Enter the password:" 
passwd = raw_input


#SSHing into the system and executing the remote command

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
rm_cmd = "service cloudera-scm-server restart"

try:
	ssh.connect(cm_host, username=user, password=passwd, timeout=10)
	print "[logger.info] Connected to the remote host: " + cm_host
except AuthenticationException:
	print "[logger.critical] Cannot ssh into the system...exiting the script"
	sys.exit(1)

print "[logger.info] Opening Connection to send Remote command...."
remote = ssh.get_transport().open_session()
print "[logger.info] Opened Connection and ready to send remote command"

print "[logger.info] Sending Remote Command..."
remote.exec_command(rm_cmd)
print "[logger.info] Sent Remote Command..."

print "[logger.info] Recieving the exit status of the remote command that is executed"
exit_status = remote.recv_exit_status()

if exit_status == 0:
	print "[logger.info] Recieved exit status is 0. Command executed Successfuully"
	print "[logger.info] Giving the Cloudera Manager some time to restart"
	time.sleep(120)
else: 
	print "[logger.critical] Recieved exit status as 1. Something is wrong"
	sys.exit(1)
ssh.close()

