# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 08:56:00 2018

@author: Tianyi Xia
"""  
import jieba
import re

#指标文件列表
def txtflist():
    txtfilelist=['一发动机.txt','一内饰.txt','一零部件.txt','一变速箱与传动.txt','中文标点.txt'
                           ,'一车身外观.txt','一驾驶操控和视野.txt','程度级别.txt',
                           '一车内空间.txt','一安全.txt','一座椅.txt','一电子设备.txt'
                           ,'一空调.txt','一油耗.txt','总体评价.txt','正面评价词语.txt'
                           ,'负面情感词语.txt','判断词语.txt','争议词语.txt']
    return txtfilelist

#读取全部的指标文件    
def filelist(txtfilelist):
    map = []
    for num in range(0, 19):
      map += [[]]
    i=0
    for txtlist in map:
        filetxt=open('C:\\pythondata\\cars\\指标txt\\new\\new\\'+txtfilelist[i],'r')  
        i+=1
        for txt in filetxt:
            txtlist.append(txt.strip().strip("\n"))
    map[4].append(" ")
    return map



#发动机标题文件：testengine.csv
#变速箱标题文件：testtransm.csv
#发动机正文文件：testengine2.txt
#变速箱正文文件：testtransm2.txt

#读取文章内容
def get_word():
    result=[]
    file_objectt=open('C:\\pythondata\\cars\\指标txt\\new\\new\\content10.txt').read().split('\n')  
    #一行行的读取内容  
    for it in range(len(file_objectt)):  
        resultp=[] 
        tem_list = jieba.cut(re.sub('[A-Za-z0-9]','',file_objectt[it])) 
        #读取每一行分词 
        for wt in tem_list :            
            resultp.append(wt)  
        result.append(resultp)   
    print(result)
    return result

#处理数据，对分过词的文章内容和词库做匹对，并准确的返回“类别+形容词”的格式    
def get_result(map,result):              
    final=[]
    b=""
    a=""
    ai=0
    bi=0
    p=0
    at=[]
    for content in result:
        i=0
        test=[]
        for word in content:
            if i == 0:
                previous_word=""
            else:
                previous_word=content[i-1]
            if word in map[0]:
                a = "发动机"
                ai = 1
            elif word in map[1]:
                a = "内饰"
                ai = 1
            elif word in map[2]:
                a = "零部件"
                ai = 1
            elif word in map[3]:
                a = "变速箱"
                ai = 1
            elif word in map[5]:
                a = "车身外观"
                ai = 1
            elif word in map[6]:
                a = "操控和视野"
                ai = 1
            elif word in map[8]:
                a = "车内空间"
                ai = 1
            elif word in map[9]:
                a = "安全"
                ai = 1
            elif word in map[10]:
                a = "座椅"    
                ai = 1
            elif word in map[11]:
                a = "电子设备"
                ai = 1
            elif word in map[12]:
                a = "空调"
                ai = 1
            elif word in map[13]:
                a = "油耗"
                ai = 1
            elif word in map[14]:
                a = "总体评价"
                ai = 1
            elif word in map[15]:
                if word in map[18]:
                    if previous_word in map[17]:
                        b = str(previous_word)+str(word)
                        bi = 1
                    else:
                        b = str(word)
                        bi = 1
                else:
                    b = str(word)
                    bi = 1
            elif word in map[16]:
                if word in map[18]:
                    if previous_word in map[17]:
                        b = str(previous_word)+str(word)
                        bi = 1
                    else:
                        b = str(word)
                        bi = 1
                else:
                    b = str(word)
                    bi = 1
            elif word in map[4]:
                if ai == 1 and bi == 1 and p == 0:
                    c = a + "--" + b
                    test.append(c)
                    ai=0
                    bi=0
                    a=""
                    b=""
                elif ai == 1 and bi == 1 and p ==1:
                    if a not in at:
                        at.append(a)
                    for ae in at:
                        c = ae + "--" + b
                        test.append(c)
                    ai = 0
                    bi = 0
                    p = 0
                    at =[]
                    a=""
                    b=""
                elif ai == 0 and bi == 1 and p==0:
                    b = ""
                    bi = 0
                elif ai == 1 and bi == 0:
                    p = 1
                    ai = 0
                    if a not in at:
                        at.append(a)
                elif ai == 0 and bi == 1 and p == 0:
                    bi == 0
                    b =""
                elif ai == 1 and p == 1:
                    ai = 0
                    if a not in at:
                        at.append(a)
                elif p == 1 and bi == 1:
                    for ae in at:
                        c = ae + "--" + b
                        test.append(c)
                    at=[]
                    a=""
                    b = ""
                    ai = 0
                    bi = 0
                    p = 0
            else:
                a = a
                b = b
            print(i)
            i+=1
            print("ai"+str(ai))
            print(a)
            print("bi"+str(bi))
            print(b)
            print("p"+str(p))
        if ai == 1 and bi == 1:
            c = a + "--" + b
            test.append(c)
        final.append(test)
    return final

#将输出的结果按照文章中每条的评论顺序输出到txt文件
def writetotxt(final):
    number=0
    print(final)
    for ele in final:
        number+=1
        file=open('C:\\pythondata\\cars\\指标txt\\new\\new\\结果集\\'+str(number)+'.txt','w')  
        for p in ele:
            file.write(p)
            file.write("\n") 
    return ele
    
if __name__=="__main__":
    a=get_result(filelist(txtflist()),get_word())
    writetotxt(a)
