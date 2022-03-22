# -*- coding: utf-8 -*-
'''
Author: Yang Sixue
Date: 2022-03-22 10:56:06
LastEditors: Yang Sixue
LastEditTime: 2022-03-22 11:22:41
Description: file content
'''
import fitz  
import os

dirname = '副高级'

img_path = '/Users/ysx/Downloads/扫描件/'+ dirname +'/'
doc = fitz.open()
i = 0

def addimg(img_file):
	global i
	print(img_file)
	imgdoc = fitz.open(img_file)
	pdfbytes = imgdoc.convertToPDF()
	pdf_name = str(i) + '.pdf'
	imgpdf = fitz.open(pdf_name, pdfbytes)
	doc.insertPDF(imgpdf)
	i+=1

addimg(img_path+'毕业证.jpg')
img_list=sorted(os.listdir(img_path+'1/'))
for img in img_list:
    addimg(img_path+'1/'+img)

img_list=sorted(os.listdir(img_path+'2/'))
for img in img_list:
    addimg(img_path+'2/'+img)

# 循环path中的文件，可import os 然后用 for img in os.listdir(img_path)实现
# 这里为了让文件以1，2，3的形式进行拼接，就偷懒循环文件名中的数字。
# for i in range(1,4):
# 	img = str(i) + '.jpg'
# 	img_file = img_path + '/' + img
# 	imgdoc = fitz.open(img_file)
# 	pdfbytes = imgdoc.convertToPDF()
# 	pdf_name = str(i) + '.pdf'
# 	imgpdf = fitz.open(pdf_name, pdfbytes)
# 	doc.insertPDF(imgpdf)
doc.save(dirname + '.pdf')
doc.close()