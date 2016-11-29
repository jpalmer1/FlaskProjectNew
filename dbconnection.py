import pymysql
pymysql.install_as_MySQLdb()

import MySQLdb

def connection():
    conn = pymysql.connect(host='sql8.freemysqlhosting.net', port=3306, user='sql8146091', passwd='gLs1fMyhhT', db='sql8146091')
    c = conn.cursor()

    return c, conn