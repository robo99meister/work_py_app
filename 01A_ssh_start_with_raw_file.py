#Loops 起動時初期設定
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect('192.168.0.10', username='root', password='toshibatec1048')

#詳細ログを保存するよう設定ファイルを作成
client.exec_command('touch /tmp/classification_output_detaillog')
client.exec_command('touch /tmp/classification_output_raw')

client.close()