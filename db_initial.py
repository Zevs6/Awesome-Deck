from db_initial.json_to_mysql import *
import configparser

# Conf Parser
config = configparser.ConfigParser()
config.read('conf.ini')
db_conf = config['DATABASE']

host = db_conf['Host']
user = db_conf['User']
passwd = db_conf['Password']
db_name = db_conf['Database']
table_name = db_conf['TableName']

jsonToMySQL(host, user, passwd, db_name, table_name)

key = input('Press any key to quit')
quit()
