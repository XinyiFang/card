#!/usr/bin/env python
'''
This file is a tool to parse json file and generate voc format xml file.
'''
import json
import xml.etree.ElementTree as ET
import cv2
import os


json_file = open("to62090.txt",'r')


while True:

    im_height = 640
    im_width = 360
    im_ch = 3

    jpg_name,others=json_file.readline().split(':')
    jpg_name=jpg_name[2:-1]
    stack=[]
    items=[]
    for i in range(len(others)-3):
        t=others[i]
        if t=="[":
            stack.append((t,i))
        elif t=="]" and stack!=[]:
            tt=stack[-1]
            if tt[0]=="[":
                stack.pop()
                items.append(others[tt[1]+1:i])

    print jpg_name
    for item in items:
        print item

    #create a xml
    out = ET.Element('annotation')
    #folder
    folder = ET.SubElement(out,"folder")
    folder.text = "VOC2007"
    #filename
    filename = ET.SubElement(out,"filename")
    filename.text = jpg_name

    #file size
    file_size = ET.SubElement(out,"size")
    file_width = ET.SubElement(file_size,"width")
    file_width.text = str(im_height)
    file_height = ET.SubElement(file_size,"height")
    file_height.text = str(im_width)
    file_depth = ET.SubElement(file_size,"depth")
    file_depth.text = str(im_ch)

    for item in items:

        #create a car obj
        obj = ET.SubElement(out,'object')
        obj_name = ET.SubElement(obj,"name")
        obj_name.text = str(item[4])

        #create boundingbox
        bndbox = ET.SubElement(obj,"bndbox")
        xmin = ET.SubElement(bndbox,'xmin')
        xmin.text = str(item[0])

        ymin = ET.SubElement(bndbox,'ymin')
        ymin.text = str(item[1])

        xmax = ET.SubElement(bndbox,'xmax')
        xmax.text = str(item[2])

        ymax = ET.SubElement(bndbox,'ymax')
        ymax.text = str(item[3])

    out_tree = ET.ElementTree(out)

    out_xml_path = "Annotations/"
    xml_file_name = jpg_name
    #out_tree.write(out_xml_path + xml_file_name + ".xml")


