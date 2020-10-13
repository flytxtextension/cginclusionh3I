import os, time
from ftplib import FTP
import MTNNigeria_Properties
import random
import time
from time import gmtime, strftime
import datetime
import numpy as np
import MySQLdb

Previous_Date = datetime.datetime.today() - datetime.timedelta(days=MTNNigeria_Properties.Days_To_Subtract)
Previous_Date_Formatted = Previous_Date.strftime('%Y%m%d')  # format the date to yymmdd
previousdate=str(Previous_Date_Formatted)
print previousdate

Previous_Date = datetime.datetime.today() - datetime.timedelta(days=MTNNigeria_Properties.Days_To_Subtract)
Previous_Date_Formatted = Previous_Date.strftime('%d%m%Y')  # format the date to ddmmyy
columndate=str(Previous_Date_Formatted)
print columndate

filenamesearch=strftime(previousdate+"_CLM_FLT_RPT01_SUBS_PROFILE"+".csv", time.localtime())
# filenamesearch=strftime("PROFILE_ADAIL_"+previousdate+".csv", time.localtime())
print "File name ", filenamesearch

for root, dirs, files in os.walk(MTNNigeria_Properties.SourceFile_Path):
    for filename in files:
        print(filename)

        ActualFileName=filenamesearch
        if filename==ActualFileName:
            print 'File Found with date: '+previousdate+', File name: '+ActualFileName+' '

            FileDirectory = MTNNigeria_Properties.SourceFile_Path
            b = np.loadtxt(r'' + FileDirectory + filename + '', dtype=str, delimiter=',',
                           usecols=(MTNNigeria_Properties.Columns_Taken))
            print b
            listx = []

            print "file name starts with date is", previousdate
            prepaid= "Prepaid"
            print (prepaid)

            for i in b:
                for x in i:
                    # print ("asd")
                    if previousdate and prepaid in x:
                        listx.append(i[0])

            print "list is ", listx
            totallen = len(listx)
            print "Total Length: ", totallen

            percent = (int(totallen) * int(MTNNigeria_Properties.PercentageGeneration)) / 100
            print "percentage", percent
            if percent == 0:
                newpercentageround = percent + 1
                num_to_select = newpercentageround
                randomshuffle = random.sample(listx, num_to_select)
                print "random no.", randomshuffle
            else:
                num_to_select = percent
                randomshuffle = random.sample(listx, num_to_select)
                print "random no.", randomshuffle

            db = MySQLdb.connect(host='192.168.151.126', user='neon', passwd='NeonDxPass123!',
                                 db='neon', port=3306)
            sql_select_Query_NonTrigger_Updates = MTNNigeria_Properties.sql_select_Query_NonTrigger_Updates
            sql_select_Query = sql_select_Query_NonTrigger_Updates
            cursor = db.cursor()
            cursor.execute(sql_select_Query)
            results = cursor.fetchall()
            print results
            if not results:
                print("Entity Id is Null")
            for r in results:
                print "Entity ID From Query: ", r[0]
            cursor.close()

            # entity id (for testing purpose replace 'r[0]' with any numeric values like 12345 )
            valfromdbentityid = 32434
            print valfromdbentityid

            timee = strftime(",1,%d%m%Y %H:%M:%S,0+0000", time.localtime())
            print "time ", timee
            OutputFile = MTNNigeria_Properties.OstrichUplod_Path

            data = open(OutputFile + strftime("%Y%m%d") + "_DAILY_CG_SUBS" + ".csv", "w")

            for elem in randomshuffle:
                data.write("%s\n" % (elem + "," + (str(valfromdbentityid)) + timee))

    else:
        print 'File not Found with date: '+previousdate



