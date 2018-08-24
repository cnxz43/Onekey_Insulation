# -*- coding: utf-8 -*-


from urllib import parse,request
import json
from retrying import retry
import requests
import string
from requests.auth import HTTPBasicAuth

@retry(stop_max_attempt_number=7)
def open_url(req):
    print("trying...")
    res = request.urlopen(req)
    res = res.read()
    return res


def connect_commandplat(device = "BADGS3" ,command_list = []):
    '''

    :param device:
    :param commandarr: 指令集 type：list
    :return:
    '''

    # 连接指令平台权限转码
    user = "wg_cmcc_luoxiaoyong"
    pwd = "1qaz@WSX"
    b64_auth = HTTPBasicAuth(user,pwd)

    # device ="BADGS3" #"SJGS10"
    # textmod=["CHECK N7LINK STATUS;"]

    # 指令集list 转码
    btcommands = bytes(json.dumps(command_list), encoding="utf-8")

    #头文件
    header_dict = {"Content-Type": "application/json;charset=UTF-8"}


    #url转码
    url="http://"+ "10.216.6.231/WebApi/mml/"+device+ "/" + "集中操作"
    url = parse.quote(url,safe=string.printable)

    #向平台发送post请求，url：平台地址，data：post携带信息，指令集合， auth：权限信息， headers：头文件
    r = requests.post(url=url,data=btcommands, auth= b64_auth ,headers=header_dict)

    #请求所得信息（解码）
    print ("result:",r.content.decode("utf-8"))



