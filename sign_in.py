from selenium import webdriver
import time
import csv
import pandas as pd

a = ['','123@qq.com','123@yahoo.com']
b = ['','123456','111111']
#字典中的key值即为csv中列名
dataframe = pd.DataFrame({'username':a,'password':b})
#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("test.csv",index=False,sep=',')
print(dataframe)
# data = pd.read_csv('test.csv')#读取csv文件
# print(data)
# username=pd.read_csv('test.csv',usecols=[1])
# print(username)
c=[0,1,2]
d=[0,1]
password_all=[]
username_all=[]
# 定位csv文件中数据的位置
for i in c:
    for j in d:
        if j==0:
            password1=dataframe.iloc[i,j]
            print(password1)
            password_all.append(password1)
        else:
            username1=dataframe.iloc[i,j]
            print(username1)
            username_all.append(username1)
print(password_all)
print(username_all)
driver=webdriver.Firefox()
driver.get("https://cnodejs.org/")
driver.find_element_by_xpath("/html/body/div[1]/div/div/ul/li[5]/a").click()
for n in range(3):
    username=username_all[n]
    password = password_all[n]
    driver.find_element_by_name("login").clear()
    driver.find_element_by_name("login").send_keys(username)
    time.sleep(2)
    driver.find_element_by_name("password").send_keys(password)
    time.sleep(2)
    driver.find_element_by_name("commit").submit()
    time.sleep(3)
time.sleep(10)
driver.close()


