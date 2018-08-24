#-*- coding: utf-8 -*-

import jpype as jp
import os.path


device ="BADGS3"
# device = "BADMME09BHW"#
commandarr=["CHECK BOARD STATUS;","CHECK N7LINK STATUS;","CHECK HDC STATUS;","SHOW SYSTEM TIME;"]

jar_path = os.path.join(os.path.abspath('.'), 'libs/onekey-1.0-SNAPSHOT.jar')
jp.startJVM(jp.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % jar_path)
Test = jp.JClass('Mycommand')
# 或者通过JPackage引用Test类
# com = jpype.JPackage('com')
# Test = com.Test
t = Mycommand()
res = t.excCommand(device, commandarr)
jp.shutdownJVM()
print (res)


