# coding:utf-8
import json
import argparse
def convert(domain,file):
    data=[]
    domain='.'+domain
    base={"name":"","value":"","domain":""}
    with open(file,'r+') as f:
        string=f.read()
    string=string.strip('\n')
    count=string.count(';')+1
    string=string.split(';')
    for i in range(count):
        name=string[i].split('=')[0].lstrip()
        value=string[i].split('=')[1].lstrip()
        base['value']=value
        base['name']=name
        base['domain']=domain
        data.append(base.copy())
    print(json.dumps(data))
if __name__=='__main__':
    parser=argparse.ArgumentParser(usage='python3 convert.py -d github.com -f cookie.txt')
    parser.add_argument("-f",dest='file',help='set cookie file')
    parser.add_argument("-d",dest='domain',help='set Second-level domain; example:github.com')
    args=parser.parse_args()
    convert(args.domain,args.file)
