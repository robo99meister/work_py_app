import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect('192.168.0.10', username='root', password='toshibatec1048')

client.exec_command('touch /tmp/classification_output_detaillog')

client.close()