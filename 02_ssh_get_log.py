import paramiko

fw = open('C:\python\JobExecute.1.txt','w')

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect('192.168.0.10', username='root', password='toshibatec1048')

stdin, stdout, stderr = client.exec_command('grep tdtr /opt/work/log/al/JobExecute.1.txt')
for line in stdout:
    fw.writelines(line)

client.close()
