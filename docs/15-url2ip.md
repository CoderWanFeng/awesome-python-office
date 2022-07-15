1行Python代码，获取对方的IP地址

大家好，这里是程序员晚枫。


## 需求说明

上次我们讲过[使用腾讯云DNS解析 + Github Pages，免费搭建个人网站 （给小白的保姆级教程）](https://cloud.tencent.com/developer/article/2019284)，有一些进阶的小伙伴可能有自己的云服务器，想把域名绑定到云服务器上。
> 如何验证域名和服务器IP是否绑定成功呢？



## 1行代码实现

我们使用python来进行验证。
#### 安装python-office这个库

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-office -U
```


#### 1行代码进行验证
```
# 导入这个库：python-office，简写为office
import office

#1行代码，验证是否绑定成功
office.tools.url2ip(url='www.python4office.cn')

#参数作用：
# url = 填写你的域名
```
运行以上代码，就会出现你的域名对应的IP地址信息，如果和你配置的一样，就说明安装成功了~
如果不一样，程序会报错、或者返回其它IP地址，你再返回第一步进行修改即可~

> 如果有我没说清楚的，或者在使用过程中有问题，欢迎大家在评论区和我交流~

## 阅读更多
- []()
- []()
- 