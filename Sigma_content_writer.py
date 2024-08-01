# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 07:01:33 2024

@author: Aye Hein Zayar

Development - v02

"""

import os
import re
import yaml


def read_yaml_external():
    fcomplete = bool()
#    rest:
#        url: ""
#        port: ""
    return fcomplete


def write_yaml():
    fname = input('Enter the file name to save: ')
    fhandler = open(fname)
    count = 0
    for line in fhandler:
        if line.startswitch('Subject:'):
            count = count + 1
    fhandler.close()
    

def open_yaml():
    fopen = bool
    
    with open("","w") as file:
        yaml_write = yaml.safe_load(file)
    return fopen
    

def write_sigma(): 
    
    datas = datas
    pls = "Please choose "
    
    for data in datas:
       title = input(pls, "the title of rule file : ")
       id = input(pls, "the rule ID : ")
       related = input(pls, "the related : ")
       sub_related_id = input(pls, "related id :")
       sub_related_type = input(pls, "related type : ")
       status = input(pls, "the status : ")
       description = input(pls, "description : ")
       references = input(pls, "references : ")
       author = input("Author :")
       date = input("Date (MM/DD/YYYY): ")
       tags = input("Rule tag : ")
       logsource = input(pls, "log source : ")
       logsource_product = input(pls, "product : ")
       logsource_category = input(pls, "category : ")
       detection = input(pls, "detection : ")
       detection_selection = input(pls, "selection : ")
       detection_selection_targetfilename_re = input(pls, "target file regular expression : ")
       detection_selection_targetfilename_endswitch = input (pls, 'target file endswitch : ')
       detection_condition = input (pls, "in condition to : ")
       falsepositive = input("falsepositive description : ")
       level = input (pls, "detection level (Example, high/medium/low : ")
       
       external_link = "https://github.com/SigmaHQ/sigma"


def update_sigma():
    

    
