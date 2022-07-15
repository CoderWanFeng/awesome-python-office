1行Python代码下载图片，爬虫从未如此简单，百度看了都害怕

![](https://www.python-office.com/api/img-cdn/python-office/down4img/cover.jpg)

大家好，这里是Python程序员晚枫。



今天，给大家介绍python-office近期更新的功能之一：**1行代码，实现图片的下载**。


真的很实用！

## 1. 安装python-office
安装很简单，在有python环境的电脑上，只需要执行下面这一行命令。
> 如果你之前使用过python-office这个库，也需要执行一下，可以下载到最新版本~

安装
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-office -U
```


## 2. 1行代码，下载图片
直接上代码！

代码
```
# 导入这个库：python-office，简写为office
import office

office.image.down4img(
    url='https://www.python-office.com/api/img-cdn/test/spider/4.jpg',
    output_name='程序员晚枫',
    type='jpg')
# 参数说明：
# url：你要下载的图片链接
# output_name：下载后的图片名称，可以不填，默认：down4img
# type：下载后的图片类型，可以不填，默认：jpg
```




## 3.关联阅读
1行代码实现复杂功能，是不是很简单？

但目前这个1次只能下载1张图片，如何1次下载更多图片呢？

**上一篇，我们讲过：如何1次下载多张图片。并且深入讲解如何加快速度。**
有兴趣的同学，可以去翻一翻，标题：Python爬虫如何加速？异步、协程还是多进程？萌新也能看懂

> 欢迎大家在评论区和我交流哟~
---