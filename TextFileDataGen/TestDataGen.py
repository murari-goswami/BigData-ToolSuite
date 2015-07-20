#!/usr/bin/python

__author__ = 'MGoswam1'

import random, csv, sys, os
from random import randrange
from collections import deque     ## Importing the queue to upload the metadata in the memory
import logging

msisdnlist = deque()
DataDirFile= list()
delimiter=','
reader=""
writer=""

# A function definition which taken input as file name and file selector to load the data into memory
# as per the criteria
def getdata(filename, fileselector):
    if fileselector == 'M':
        fHandle=open(filename,'r')     # File operation to extrat the metadata from the file
        for rec in fHandle:
            msisdnlist.append(rec.rstrip('\n'))
    elif fileselector=='C':
        None

# A function call to spilt the records from the file as per the delimiter passed in the argument
def splitlines(line,delimiter):
    for splits in line.split(delimiter):
        DataDirFile.append(splits)


############################################## Main Programme starts here#######################################
logging.basicConfig(filename='TestDataGen_execution.log',filemode='w', level=logging.INFO)

logging.info("The configuration file is FileReplaceConfig.cfg")
logging.info("Reading the configuration file to extract the metadata file")

fHandleM=open("FileReplaceConfig.cfg",'r')
splitlines(fHandleM.read(),delimiter)
fHandleM.close()

logging.info("The landing directory is :%s" %DataDirFile[0]) # .rstrip('\n')
logging.info("The data file name is : %s" % DataDirFile[1]) # .rstrip('\n')

# Load metadata in a list
getdata("metadata.dat",'M')

# Iterate over the list to print the records from the list
logging.info("The current path is : %s"% os.getcwd()) #.rstrip('\n')
logging.info("The path to change to : %s"% DataDirFile[0]) #.rstrip('\n')
os.chdir(DataDirFile[0])
try:
    logging.info("The Reader file is %s"% DataDirFile[1]) #.rstrip('\n')
    logging.info("datafile is %s"% DataDirFile[1]) #.rstrip('\n')
    reader = csv.reader(open(DataDirFile[1].rstrip('\n'),'rb'))
    logging.info("The writer file is new_%s"%DataDirFile[1])
    fwriter=open("new_"+DataDirFile[1].rstrip('\n'),'wb')
    writer = csv.writer(fwriter)

    for row in reader:
    # print [row[0],row[1],row[2],str(random.choice(msisdnlist)),
    #                  row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],
    #                  row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],row[33],
    #                  row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41],row[42],row[43],row[44],row[45],row[46],row[47],row[48],
    #                  row[49]]
        writer.writerow([row[0],row[1],row[2],str(random.choice(msisdnlist)),
                     row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],
                     row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],row[33],
                     row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41],row[42],row[43],row[44],row[45],row[46],row[47],row[48],
                     row[49]])

    logging.info("The replacement File generation is completed")
except Exception:
    print "File Read / Write error"

logging.info("The programme finished")
