# coding:utf-8
import json
import re
import argparse
def convert(domain,file):
    data=[]
    domain='.'+domain
    base={"name":"","value":"","domain":""}
    with open(file,'r+') as f:
        string=f.read()
    string1=string+';'
    key=re.findall(r"[\w-]+(?==\w)",string1)
    values=re.findall(r"=(.*?);",string1)
    for i in range(len(key)):
        base["name"]=key[i]
        base['value']=values[i]
        base['domain']=domain
        data.append(base.copy())
    print(json.dumps(data))
if __name__=='__main__':
    parser=argparse.ArgumentParser(usage='python3 convert.py -d github.com -f cookie.txt')
    parser.add_argument("-f",dest='file',help='set cookie file')
    parser.add_argument("-d",dest='domain',help='set Second-level domain; example:github.com')
    args=parser.parse_args()
    try:
        convert(args.domain,args.file)
    except:
        print("Error!! \nusage:python3 convert.py -d github.com -f cookie.txt\nPlease set Second-level domain")
