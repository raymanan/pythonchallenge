'''
Created on 2013-4-12

@author: nan
'''
import string

def run():
    text1 = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.
kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. """
    text2 = "map"
    table = string.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2]) 
    print text1.translate(table)
    pass
