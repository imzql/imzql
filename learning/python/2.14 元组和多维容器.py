#元组 tuple
#特性：有序；元素可重复；可存放多种数据类型
#不支持元素的修改
tuplea=("张三","李四","王五","赵六")

#索引操作
# print(tuplea[1])
# print(tuplea[-3])
# print(tuplea[1:3])

#元组用在对安全性有一定需求的数据上
# 2 5 7 3 


#多维容器
lista=[213,2432,43,545,46]
listb=[1212,234,35,45,"你好",(1,23,2,"北京",535,4,),68,12]
listc=[44,67,67,8798,64,646,5,345]
listx=[lista,listb,listc,[21,322,343,5,4,6,6]] #多维容器

print(listx[1][5][3])