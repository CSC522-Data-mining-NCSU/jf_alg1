import mysql.connector
import pdb
import csv

cnx = mysql.connector.connect(user='root', password = 'QsBq_lqsym_1010', host = '127.0.0.1', database = 'Netflix')
cursor = cnx.cursor()

def getRate(userid):
    query = 'select user_id, movie_id, datediff(date,\'1999-01-01\') as date, rating from ratings where user_id = '+ str(userid)

    cursor.execute(query)
    rows = cursor.fetchall()
    fp = open('./userRate/'+str(userid)+'.rate','w')
    myFile = csv.writer(fp)
    myFile.writerows(rows)
    fp.close()

all_u = []
userfp = open('user_attr.csv','r')
u = csv.reader(userfp)
u.next()
for i in u:
    all_u.append(int(i[0]))


for i in all_u[0:1000]:
    getRate(i)

cursor.close()
cnx.close()
