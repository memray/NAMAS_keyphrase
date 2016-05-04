# -*- coding: utf-8 -*-
from keyphrase.MySQLConnector import MySQLConnector

__author__ = 'Memray'

import json;
import os;
import pymysql;

# Mysql Singleton CLass with pymysql
# class mysql_test(object):



if __name__ == '__main__':
    output_file = '/data/sci.json'
    if(not os.path.exists(output_file)):
        os.makedirs(output_file)

    conn = MySQLConnector("localhost", "root", "123456", "cs_academy", True)
    sql = 'SELECT abd,ded FROM sci_scie_computer_paper'
    articles = conn.queryrows(sql)
    # print(len(articles))
    file = open(output_file)
    for article in articles:
        dict = {}
        dict['abstract']=article[0]
        dict['keyword']=article[1]
        json_text = json.JSONEncoder.encode(dict)
        file.write(json_text)
    file.close()