快来白嫖动漫头像！Python调用百度AI接口，1行代码免费转换200张。
![](https://files.mdnice.com/user/26656/e85f9535-c3f0-4fff-9823-8a117d833a50.jpg)

大家好，这里是程序员晚枫。
> Python自动化办公官网发布啦：**[https://www.python-office.com/](https://www.python-office.com/)**

上一次给大家分享了：**前文链接**

## 0. 问题说明

大家太喜欢这个功能了，没一会就把这个功能的200次试用用完了。


如果你出现下面这个报错，说明你的程序本身没有问题，只是试用次数用完了。
![](https://files.mdnice.com/user/26656/c9e78022-40d4-4a44-9dd9-e78172420e6d.jpg)


今天给大家补充一个进阶版本，保证每个人都可以使用~

## 1. 安装python-office
安装很简单，在有python环境的电脑上，只需要执行下面这一行命令。
> 如果你之前使用过python-office这个库，也需要执行一下，可以下载到最新版本~

安装
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-office -U
```




## 2. 生成动漫头像
直接上代码！

代码
```
# 导入这个库：python-office，简写为office
import office

office.image.img2Cartoon(path='',client_api='你的api key', client_secret='你的secret key')

# 参数说明：
# path: 存放自己真人照片的位置 + PDF的文件名，例如：d://image//程序员晚枫.jpg
# client_api: '你的api key'
# client_secret: '你的secret key'
```
直接运行以上代码，就会得到一张转化后的动漫头像了。

>程序可能需要运行20秒左右。

## 3. 免费开通自己的动漫头像账号
相信细心的朋友发现了，这个最新的版本和上次的区别就是：多了``clinet_api和client_secret``这2个参数。

这2个参数就是百度AI平台提供的，每人200次免费调用机会。
> 这也就是大家在上一个版本使用会报错的原因：因为我给大家提供了自己的200次试用，已经用完了。

**开通免费试用很简单**，打开百度AI平台，找到：人像动漫化这个功能，然后创建自己的应用，复制下图中的2个信息到你自己的代码里就可以了。**如果不知道百度AI平台的链接，大家可以评论区提问（文章里不能放链接，容易审核不通过🐕）**。
![](https://files.mdnice.com/user/26656/b351231e-1436-4452-947c-d62e03b003c4.jpg)


## 4.全部功能
1行代码实现复杂功能，是不是使用起来很方便？


> 项目已被收录进【开源中国】、【Python官网】等平台，所有功能，免费给大家使用：[https://github.com/CoderWanFeng/python-office](https://github.com/CoderWanFeng/python-office)
