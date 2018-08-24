# -*- coding: utf-8 -*-

from urllib import parse
import json
import requests
import string
from requests.auth import HTTPBasicAuth
# from ..models import Commands


# def get_command_list(ne_type, vendor):
#     qs = Commands.objects.filter(ne_type=ne_type).filter(vendor=vendor)
#     command_list = qs[0].command_list.split('+')
#     return command_list


def connect_commandplat(ne, command_list):
    """
    :param ne:
    :param command_list: 指令集 type：list
    :return:
    """

    # url转码
    url = "http://" + "10.216.6.231/WebApi/mml/" + ne + "/" + "集中操作"
    url = parse.quote(url, safe=string.printable)

    # 指令集list 转码
    btcommands = bytes(json.dumps(command_list), encoding="utf-8")

    # 连接指令平台权限转码
    user = "wg_cmcc_luoxiaoyong"
    pwd = "1qaz@WSX"
    b64_auth = HTTPBasicAuth(user, pwd)

    # 头文件
    header_dict = {"Content-Type": "application/json;charset=UTF-8"}

    # 向平台发送post请求
    # url：平台地址；
    # data：post携带信息，即指令集合；
    # auth：权限信息；
    # headers：头文件
    r = requests.post(url=url,
                      data=btcommands,
                      auth=b64_auth,
                      headers=header_dict)

    # 请求所得信息（解码）
    return r.content.decode()

def organize_result(ret):
    ret = ret[1:-1]
    ret = ret.split(',')
    result = ''
    for r in ret:
        result += "\n\n**********************指令结果***********************\n\n"+r[1:-1].replace('\\r\\n','\n')
    return result

if __name__ == '__main__':
    ne = {}
    command_list = {}
    tag = 'SJ'

    ne['BA'] = 'BADGS3'
    command_list['BA'] = ["CHECK BOARD STATUS;",
                          "CHECK N7LINK STATUS;",
                          "CHECK HDC STATUS;",
                          "SHOW SYSTEM TIME;"]

    ne['SJ'] = 'SJGS10'
    command_list['SJ']= ["LST POOLBKPCTRL:;",
                         "DSP BKPSTATUS:;",
                         "DSP N7LNK:;",
                         "DSP MGW:;",
                         "LST OFI: QR=LOCAL;"]

    ne['TS'] = 'TSGS11'
    command_list['TS'] = ["mml",
                          "ioexp;",
                          "allip:acl=a1;",
                          "saaep:sae=36;",
                          "nrgwp:mg=all;",
                          "exit;"]
    ret = connect_commandplat(ne[tag], command_list[tag])
    organize_result(ret)