# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:38:07 2018

@author: Tianyi Xia
"""
import jieba
import re

Ts2=[]
#发动机标题文件：testengine.csv
#变速箱标题文件：testtransm.csv
#发动机正文文件：testengine2.txt
#变速箱正文文件：testtransm2.txt
file_objectt=open('C:\\pythondata\\cars\\csv\\testengine2.txt', encoding='utf-8').read().split('\n')  #一行行的读取内容  
for it in range(len(file_objectt)):  
    result=[] 
    tem_list = jieba.cut(re.sub('[A-Za-z0-9\!\%\[\]]','',file_objectt[it])) 
    for wt in tem_list :#读取每一行分词  
        if wt not in result:
            result.append(wt)  
    Ts2.append(result)
   
txt1=[]                    
filetxt=open('C:\\pythondata\\cars\\指标txt\\一发动机.txt','r')  
for txt in filetxt:
    txt1.append(txt.strip("\n"))

txt2=[]                    
filetxt=open('C:\\pythondata\\cars\\指标txt\\汽车品牌.txt','r')  
for txt in filetxt:
    txt2.append(txt.strip("\n"))

txt3=[]                    
filetxt=open('C:\\pythondata\\cars\\指标txt\\一零部件.txt','r')  
for txt in filetxt:
    txt3.append(txt.strip("\n"))
    
txt4=[]                    
filetxt=open('C:\\pythondata\\cars\\指标txt\\一变速箱与传动.txt','r')  
for txt in filetxt:
    txt4.append(txt.strip("\n")) 

txt5=[]                    
filetxt=open('C:\\pythondata\\cars\\指标txt\\stopwords.txt','r',encoding='utf-8')  
for txt in filetxt:
    txt5.append(txt.strip("\n")) 

txt6=[]                    
filetxt=open('C:\\pythondata\\cars\\指标txt\\中文标点.txt','r')  
for txt in filetxt:
    txt6.append(txt.strip("\n")) 

txt7=[]                    
filetxt=open('C:\\pythondata\\cars\\指标txt\\一车身外观.txt','r')  
for txt in filetxt:
    txt7.append(txt.strip("\n")) 

txt8=[]                    
filetxt=open('C:\\pythondata\\cars\\指标txt\\一驾驶操控和视野.txt','r')  
for txt in filetxt:
    txt8.append(txt.strip("\n")) 
    
txt9=[]                    
filetxt=open('C:\\pythondata\\cars\\指标txt\\程度级别.txt','r')  
for txt in filetxt:
    txt9.append(txt.strip("\n")) 
 
txt10=[]                    
filetxt=open('C:\\pythondata\\cars\\指标txt\\地名.txt','r',encoding='utf-8')  
for txt in filetxt:
    txt10.append(txt.strip("\n")) 
    
final0=[]    
for aa in Ts2:
    for bb in aa:
        final0.append(bb)

for dc in final0:
    print(len(final0))
    if len(dc)==1:
        final0.remove(dc)
        
final=[]
for fc in final0:
    if fc not in final:
        if len(fc) > 1:
            final.append(fc)

#num = 1
#while num < 10:      
#    for cc in final:
#        print(len(final))
#        if cc in 'txt%s' % num:
#            final.remove(cc)
#    num+=1
for loop in range(1,5):
    for cc in final:
        print(len(final))
        if cc in txt1:
            final.remove(cc)
    for cc in final:
        print(len(final))
        if cc in txt2:
            final.remove(cc)
    for cc in final:
        print(len(final))
        if cc in txt3:
            final.remove(cc)
    for cc in final:
        print(len(final))
        if cc in txt4:
            final.remove(cc)  
    for cc in final:
        print(len(final))
        if cc in txt5:
            final.remove(cc) 
    for cc in final:
        print(len(final))
        if cc in txt6:
            final.remove(cc)
    for cc in final:
        print(len(final))
        if cc in txt7:
            final.remove(cc)
    for cc in final:
        print(len(final))
        if cc in txt8:
            final.remove(cc)
    for cc in final:
        print(len(final))
        if cc in txt9:
            final.remove(cc)
    for cc in final:
        print(len(final))
        if cc in txt10:
            final.remove(cc)
    for cc in final:
        print(len(final))
        if len(cc) == 1:
            final.remove(cc)        
for ec in final:
    if ec in txt2:
        final.remove(ec)

#txt000=[]                    
#filetxt=open('C:\\pythondata\\cars\\指标txt\\123.txt','r')  
#for txt in filetxt:
#    txt000.append(txt.strip("\n"))        
#
#for dd in txt000:
#    if dd in txt2:
#        txt000.remove(dd)
#
filetxt1=open('C:\\pythondata\\cars\\指标txt\\testtransm2a.txt','w')  
for dd in final:
        filetxt1.write(dd)
        filetxt1.write("\n")
        
#for e in txt2:        
#    if "迈腾" == e:
#        print("1")
#for f in final:        
#    if "蒙迪欧" == f:
#        print("1")        
################################yzyzyzyzyzyzyzyzyz##############################
txtyz=[]                    
filetxt=open('C:\\pythondata\\cars\\指标txt\\三负面词汇.txt','r')  
for txt in filetxt:
    txtyz.append(txt.strip("\n")) 
    
Ts2yz=[]
Ts2yzpinpai=[]
Ts2yzbujian=[]
Ts2yzguzhang=[]
file_yanzheng=open('C:\\pythondata\\cars\\csv\\testengine.csv', encoding='gbk').read().split('\n')  #一行行的读取内容  
#for yanzheng in range(len(file_yanzheng)):  
##    resultyz=[] 
#    tem_yzlist = jieba.cut(re.sub('[A-Za-z0-9\!\%\[\]]','',file_yanzheng[yanzheng])) 
#    for yz in tem_yzlist :#读取每一行分词  
#        if yz in txtyz:
##            resultyz.append(yz)  
#            Ts2yz.append(file_yanzheng[yanzheng])   
##            Ts2yzguzhang.append(yz)
abc=[]
abci=0
c=[]
b=[]
for yanzheng in range(len(file_yanzheng)):  
#    resultyz=[] 
    p = re.sub('[A-Za-z0-9\!\%\[\]]','',file_yanzheng[yanzheng])
    tem_yzlist = jieba.cut(re.sub('[A-Za-z0-9\!\%\[\]]','',p))     
    for yz in tem_yzlist:#读取每一行分词 
        if yz in txtyz: 
            c.append(yz)
        if yz in txt2: 
            b.append(yz)
    if len(c)==0:
        c.append("___")
#    for yz in tem_yzlist:#读取每一行分词 

    if len(b)==0:
        b.append("___")
    d =str(b[0])+"---"+str(c[0])
    abc.append(d)
    abci+=1
    b=[]
    c=[]
#        if a == " " and c == " ":
#            h=0
#        else:
#        d = str(a.strip('\n') + "+" + c.strip('\n'))
#        print(d)
#        Ts2yz.append(c)

finalyz=[]    
for aa in Ts2yz:
    if aa not in finalyz:
        finalyz.append(aa)        

for ele in finalyz:
    if len(ele)<6:
        finalyz.remove(ele)        
            
del(it,loop,result,ele,fc,txt,wt,yanzheng,yz,aa,bb,cc,dc,dd,ec)


for kkkk in file_objectt:
    if kkkk=="_-. (. , 下载次数: )":
        file_objectt.remove(kkkk)