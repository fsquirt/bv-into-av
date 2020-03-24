import re
from urllib import request

BV = input('请输入BV号:')
BVH = str(BV)

url = 'https://api.bilibili.com/x/web-interface/view?bvid='+BVH
req = request.Request(url)
page = request.urlopen(req).read()
page = page.decode('utf-8')
string = page

print("=====分====割====线=====")
print('你要查询的BV号是:',BVH)

aidnum = re.findall('"aid":([0-9]*)',string,flags=0)
av = int(aidnum[0])
print('此视频AV号为:' + "AV",av)
print("")
print("程序制作者:fsquirt,UID:349511867")
print("感谢你的使用")

input()
