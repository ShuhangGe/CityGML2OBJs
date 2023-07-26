# import markup3dmodule
# import polygon3dmodule
# from lxml import etree
# import os
# import argparse
# import glob
# import numpy as np
# import itertools
import logging
from xml.etree.ElementTree import ElementTree
logging.basicConfig(filename='/mnt/sda/CityGML/CityGML2OBJs-master/getdata.log', level=logging.DEBUG)

FULLPATH = '/mnt/sda/CityGML/tokyo/CityGML_Buildings/CityGML_Buildings/tile_0_1/Tokyo_Buildings.gml'
tree = ElementTree()
tree.parse(FULLPATH)
root = tree.getroot()
a = tree.find('core:cityObjectMember')
print(a)
# for el in root.iter('srsDimension'):
#     attrib = el.attrib
#     if len(attrib) > 1:
#         # adjust attribute order, e.g. by sorting
#         print('attrib.items(): ',attrib.items())

# data = root.findall("{http://www.opengis.net/gml}MultiSurface")
# print(data)
save_path = '/mnt/sda/CityGML/tokyo/CityGML_Buildings_tokyo_object'
for child in root:
    # 第二层节点的标签名称和属性
    #print(child.tag,":", child.attrib) 
    # 遍历xml文档的第三层
    for children in child:
        #logging.info('\n')
        # 第三层节点的标签名称和属性
        #logging.info(f'children: {children.tag} : {children.attrib}, {children.text}')
        

        for children4 in children:
            #logging.info(f'children4: ,{children4.tag} : {children4.attrib}, {children4.text}')
            for children5 in children4:
                #logging.info(f'children5: ,{children5.tag} : {children5.attrib}, {children5.text}')
                for children6 in children5:
                    #logging.info(f'children6: ,{children6.tag} : {children6.attrib}, {children6.text}')
                    for children7 in children6:
                        #logging.info(f'children7: ,{children7.tag} : {children7.attrib}, {children7.text}')
                        for children8 in children7:
                            #logging.info(f'children8: ,{children8.tag} : {children8.attrib}, {children8.text}')
                            for children9 in children8:
                                #logging.info(f'children9: ,{children9.tag} : {children9.attrib}, {children9.text}')
                                for children10 in children9:
                                    #logging.info(f'children10: ,{children10.tag} : {children10.attrib}, {children10.text}')
                                    for children11 in children10:
                                        #logging.info(f'children11: ,{children11.tag} : {children11.attrib}, {children11.text}')
                                        for children12 in children11:
                                            #logging.info(f'children12: ,{children12.tag} : {children12.attrib}, {children12.text}')
                                            
                                            obj = children12.text
                                            
                                            #print('obj: ',obj)
                                            # print(obj.split(' ')[:3])
                                            # print(obj.split(' ')[3:6])
                                            # print(obj.split(' ')[6:9])
                                            # print(obj.split(' ')[9:12])
                                            # print(obj.split(' ')[12:15])
                                            # print(obj.split(' ')[15:18])
                                            if  obj.split(' ')[:3] != []:
                                                with open(save_path + '/tokyo_v' + ".obj", "a") as obj_file:
                                                    obj_file.write('v ')
                                                    for i in obj.split(' ')[:3]:
                                                        obj_file.write(i+' ')
                                                    obj_file.write('\n')
                                            if  obj.split(' ')[3:6] != []:
                                                with open(save_path + '/tokyo_v' + ".obj", "a") as obj_file:
                                                    obj_file.write('v ')
                                                    for i in obj.split(' ')[3:6]:
                                                        obj_file.write(i+' ')
                                                    obj_file.write('\n')
                                            if  obj.split(' ')[6:9] != []:
                                                with open(save_path + '/tokyo_v' + ".obj", "a") as obj_file:
                                                    obj_file.write('v ')
                                                    for i in obj.split(' ')[6:9]:
                                                        obj_file.write(i+' ')
                                                    obj_file.write('\n')
                                            if  obj.split(' ')[9:12] != []:
                                                with open(save_path + '/tokyo_v' + ".obj", "a") as obj_file:
                                                    obj_file.write('v ')
                                                    for i in obj.split(' ')[9:12]:
                                                        obj_file.write(i+' ')
                                                    obj_file.write('\n')
                                            if  obj.split(' ')[12:15] != []:
                                                with open(save_path + '/tokyo_v' + ".obj", "a") as obj_file:
                                                    obj_file.write('v ')
                                                    for i in obj.split(' ')[12:15]:
                                                        obj_file.write(i+' ')
                                                    obj_file.write('\n')
                                            if  obj.split(' ')[15:18] != []:
                                                with open(save_path + '/tokyo_v' + ".obj", "a") as obj_file:
                                                    obj_file.write('v ')
                                                    for i in obj.split(' ')[15:18]:
                                                        obj_file.write(i+' ')
                                                    obj_file.write('\n')
                                            if  obj.split(' ')[18:21] != []:
                                                with open(save_path + '/tokyo_v' + ".obj", "a") as obj_file:
                                                    obj_file.write('v ')
                                                    for i in obj.split(' ')[18:21]:
                                                        obj_file.write(i+' ')
                                                    obj_file.write('\n')


