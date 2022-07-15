![](https://www.python-office.com/api/img-cdn/python-office/sheet2excel/cover.jpg)

大家好，这里是程序员晚枫。

❤先说一个好消息，``python-office自动化办公``的官网上线了，点击直达👉[https://www.python-office.com](https://mp.weixin.qq.com/s/RKTP1Q_DQxyPDaLTT0AC2g)
![](https://www.python-office.com/api/img-cdn//wanfeng/opensource-img/python-office.com.jpg)


今天开源项目[python-office](https://mp.weixin.qq.com/s/d2m7xYCLXF8QUlr-5sSuPA)发布了一个新功能:

> 1行代码，拆分你指定的Excel文件为多个Excel文件，以sheet命名。

本文给大家详细介绍一下~


## 需求说明

上文给大家讲了excel的合并，是把多个excel合并为一个excel里的多个sheet。详情见👉[上文回顾](https://mp.weixin.qq.com/s/3ZhZZfGlpNhszCWnOBeklg)

今天这个是反向操作：把1个文件里的多个sheet，拆分为不同的excel文件。如下图所示。

![](https://www.python-office.com/api/img-cdn/python-office/sheet2excel/profile.jpg)

有一位老师，现在有全校1年级12个班级所有同学都在一起的``一个成绩单Excel文件``，现在老师想把它们拆分为12个文件，每个文件用sheet的名字命名，例如：``一年级1班.xlsx、一年级2班.xlsx、一年级3班.xlsx``等等。

> 这里大可放心，哪怕每个表的格式、内容不同，也完全可以无损拆分。这里用班级成绩合并举例，只是为了大家更好的理解。



## 1行代码实现

下面我们用一行代码，实现上面这个功能。
#### 安装python-office这个库

- 这行命令的作用：下载 + 更新；
- 如果你之前用过这个库，也要运行一下这行命令，进行一下更新。否则没有本文功能。

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-office -U
```


#### 1行代码
```
# 导入这个库：python-office，简写为office
import office

#1行代码，验证是否绑定成功
office.excel.sheet2excel(file_path='d://程序员晚枫的文件夹/class.xlsx')

#参数作用：
# file_path = 将要拆分的Excel文件的位置，只能拆分xlsx后缀的Excel文件。
```
直接运行以上代码，就可以得到一个拆分后的excel文件啦~

**快去试试吧~**

> 如果有我没说清楚的，或者在使用过程中有问题，欢迎大家在评论区和我交流~

## 阅读更多

- [1行Python代码，拿到周杰伦新歌的MP3文件，终于可以免费听周杰伦了](https://mp.weixin.qq.com/s/cT8lcUwd3UayTfLGddjfJw)
- [1.2-1.0=0.19？Python中不可思议的错误，原来是浮点数计算的陷阱。](https://mp.weixin.qq.com/s/8lTqXmub1YAdEQmHGITL8Q)
- [3年开发了5个私人项目：自动化办公、网站、机器人、小程序...免费开源，拿走不谢~](https://mp.weixin.qq.com/s/2Nkxd4sjhheRwseK-MUQ2A)

----