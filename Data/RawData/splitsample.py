# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:16:20 2017

@author: Leshang
"""
import re
import sys
#import os
 
def split_sample(filename = 'release3.samples.xml', directory = 'split'):
    file = open(filename)
    
    #lines = file.readlines()
    all_lines = file.read()
#    title_found = False
    title = ''
#    root_found = False
    root = ''
#    directory = 'split'
    root_end = '</prov:document>'
    
    #print(all_lines)
    
    #find title
    p = re.compile(r'<\?.[^<>]*\?>')
    found = p.findall(all_lines)
    if(len(found) > 0):
        title = found[0]
        print('XML Title: \n', title)
#        title_found = True
    
    p = re.compile(r'<prov:document.[^<>]*>', re.S)
    found = p.findall(all_lines)
    if(len(found) > 0):
        root = found[0]
        print('XML Root: \n', root)
#        root_found = True
        
    
    
    #p = re.compile(r'(<prov:entity.[^<>]*>.[\n\s]*<kimlab-sample:sample-name>.*?)<prov:entity.[^<>]*>.[\n\s]*<kimlab-sample:sample-name>'\
    #             , re.S)
#    p = re.compile(r'<prov:entity.[^<>]*>.[\n\s]*<kimlab-sample:sample-name', re.S)
    p = re.compile(r'<prov:entity.[^<>]*>.[\n\s]*<obo:IAO_0000577', re.S)
    found_first = p.finditer(all_lines)
    #m = re.compile(r'(.*)<prov:entity.[^<>]*>.*?<kimlab-sample:sample-name>'\
    #             , re.S)
    #found = m.findall(found_first[0])
    #print(all_lines[found_first[0].start(0),found_first[0].start(1)-1])
    
    pos_list = []
    for it in found_first:
        pos_list.append(it.start())
        print(it.start())
        
    pos_list.append(len(all_lines) - 16)  
    
    #print ('Contents: \n', found_first[len(found_first)-1])
    
    #i = 1
    #os.mkdir(dir)
    for i in range(len(pos_list)-1):
        print(i)
        new_file = open(directory + '/' + filename + '-' + str(i+1) + '.xml', 'w+')
        new_file.write(title)
        new_file.write('\n')
        new_file.write(root)
        new_file.write('\n\n  ')
        new_file.write(all_lines[pos_list[i]:pos_list[i+1]-1])
        new_file.write('\n')
        new_file.write(root_end)
    #    i += 1
#        print(i)
        new_file.close()
    
    print(range(len(pos_list)-1))
    print('Parse Complete.')
    
    #for line in lines:
    #    if(title_found == False):#title not found
    #        p = re.compile(r'<\?.[^<>]*\?>')
    #        found = p.findall(line)
    #        if(len(found) > 0):
    #            title = found[0]
    #            print('XML Title: ', title)
    #            title_found = True
    #            continue
    #    else:#found title
    #        p = re.compile(r'<(prov:document).[^<>]*>')
    #        found = p.findall(line)
    #        if(len(found) > 0):
    #            root = found[0]
    #            print('XML Root: ', root)
    #            root_found = True
    #            continue
if __name__ == "__main__":
#    if(len(sys.argv)<2):
#        print('No input arguments')
#    else:
#        split_sample(sys.argv[1])
    split_sample('peSTAR.samples.xml')
#    split_sample('samples2.samples.xml')
#    split_sample('release3.samples.xml')
#    split_sample('pipeline12a.samples.xml')

