#coding=utf-8

import urllib.request
from bs4 import BeautifulSoup
from urllib import error
import re
ls = ['zhenrenxiu','meinv',"lianglichemo",'rentiyishu','xiaohua','lianglichemo']
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

for j in range(56195,90000):
	url_origin = "http://www.7160.com/meinv/"+str(j)
	try:
		page_obj = urllib.request.urlopen(url_origin)
		page_soup = BeautifulSoup(page_obj,'lxml')
		total_page_obj = page_soup.find(text=re.compile('共')).string
		pattern = re.compile(r'\d+')
		match = pattern.search(total_page_obj)

		if match == None:
			total_page = 0;
		else:
			total_page = match.group();

		for i in range(1,int(total_page)+1):
			if i == 1 :
				url = url_origin+"/index.html"
			else:
				url = url_origin+"/index_"+str(i)+".html"
			request = urllib.request.Request(url)
			try:
				res = urllib.request.urlopen(request)

				soup = BeautifulSoup(res,'lxml')
				title_obj = soup.find(attrs={"class":"picmainer"})

				if title_obj is not None:
					print(url)
					title = title_obj.h1.string
					content = soup.find('img')
					src = content.get("src")

					file_name = validateTitle(title)+".jpg"
					urllib.request.urlretrieve(src, "D://img5/"+file_name)
					print(file_name+"保存成功")
			except Exception  as e:
				print("异常"+str(j))
	except Exception  as e:
				print("异常"+str(j))