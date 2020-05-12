# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:44:01 2020

@author: Moeed
"""

import csv
import json
import glob    
import os
import pandas as pd

#importing libaries
def psv_to_json(pathname,firstindex,lastindex):
    path=pathname+'\p0'
    path1=pathname+'\CSV\p0'
    path2=pathname+'\JSON\p0'
    pathpsv=r''
    pathcsv=r''
    pathjson=r''
    #intiating custom paths
    os.makedirs(r"E:\training\CSV")
    os.makedirs(r"E:\training\JSON")    
    #making new directory
    for i in range (firstindex,lastindex): #main loop
        if  len(str(i))==1:       #judging and making custom path name               
            pathpsv=path+'0000'+str(i)+'.psv'
            pathcsv=path1+'0000'+str(i)+'.csv'
            pathjson=path2+'0000'+str(i)+'.json'
        if  len(str(i))==2:    
            pathpsv=path+'000'+str(i)+'.psv'
            pathcsv=path1+'000'+str(i)+'.csv'
            pathjson=path2+'000'+str(i)+'.json'
        if  len(str(i))==3:    
            pathpsv=path+'00'+str(i)+'.psv'
            pathcsv=path1+'00'+str(i)+'.csv'
            pathjson=path2+'00'+str(i)+'.json'
        if  len(str(i))==4:    
            pathpsv=path+'0'+str(i)+'.psv'
            pathcsv=path1+'0'+str(i)+'.csv'
            pathjson=path2+'0'+str(i)+'.json'
        if  len(str(i))==5:    
            pathpsv=path+str(i)+'.psv'
            pathcsv=path1+str(i)+'.csv'
            pathjson=path2+str(i)+'.json'
        with open(pathpsv, "r") as file_pipe: # reading and converting psv files to csv
            reader_pipe = csv.reader(file_pipe, delimiter='|')
            with open(pathcsv, 'w') as file_comma:
                writer_comma = csv.writer(file_comma, delimiter=',')
                writer_comma.writerows(reader_pipe)
        df = pd.read_csv(pathcsv, usecols=[0,1,2,3,5,6,34,35,39,40], header=0) #filter csv to first six columns
        #print (pathcsv)
        df.to_csv(pathcsv, encoding='utf-8', index=False) # writing it again
        with open(pathcsv) as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            with open(pathjson, 'w') as f:
                json.dump(rows, f,indent=4)
    os.chdir(pathname+'\CSV')
    extension = 'csv'
    print ('csv')
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
    
    os.chdir(pathname+'\JSON')
    extension1 = 'json'
    print ('json')
    all_filenames = [i for i in glob.glob('*.{}'.format(extension1))]
    combined_json = pd.concat([pd.read_json(f) for f in all_filenames ])
    combined_json.to_json( "combined_json.json",orient='records')
psv_to_json(r'E:\training',1,20001)
print ('Finished')

