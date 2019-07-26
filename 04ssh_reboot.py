#ログを消去して再起動
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect('192.168.0.10', username='root', password='toshibatec1048')

#ログを削除、ログが5MBを超えると、ファイル名が変更されるため、毎回削除する。
client.exec_command('rm /opt/work/log/al/JobExecute.1.txt')
client.exec_command('reboot')

client.close()