# -*- coding: utf-8 -*-
from keyphrase.MySQLConnector import MySQLConnector

__author__ = 'Memray'

import json;
import os;
# import pymysql;

# Mysql Singleton CLass with pymysql
# class mysql_test(object):



if __name__ == '__main__':
    parent_path = r"H:/NetDrive/WorkSpace/Pitts/NAMAS_keyphrase/"
    output_file = parent_path + r'data/sci_computer.json'
    # if(not os.path.exists(output_file)):
    #     os.makedirs(output_file)

    conn = MySQLConnector("localhost", "root", "123456", "cs_academy", True)
    sql = 'SELECT tid,abd,ded FROM sci_scie_computer_paper;'
    articles = conn.queryrows(sql)
    # print(len(articles))
    file = open(output_file, 'w')
    for article in articles:
        dict = {}
        dict['title']=article[0]
        dict['abstract']=article[1]
        dict['keyword']=article[2]
        json_text = json.dumps(dict)+'\n'
        file.write(json_text)
    file.close()