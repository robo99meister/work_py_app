#read raw file
import struct

fid = open("C:\python\libtdtr_toppage_20190731102500_reuse_1652x2338.raw", 'rb')   # 'r'は読み込み専用、'b'はバイナリモードで読み込みを表す

a = struct.unpack('B', fid.read(1))   # 'f'はfloat32の場合、doubleは'd', int8は'b', int16は'h'
print(a)