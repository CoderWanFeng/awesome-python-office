
![](https://www.python-office.com/api/img-cdn//wanfeng/opensource-img/open-cover.jpg)


大家好，这里是全网同名的``程序员晚枫``。

2019年从法学院毕业后就从事了程序员的工作，因为业务需要或者自己感兴趣，先后使用的开发语言有：Java、Python、JS。


**今天整理一下这3年开发的私人项目，全部开源给大家，并且写明使用的步骤和命令。**

``每一个项目都是我正在使用的，有一些项目的访问人数超过了10w+，大家赶紧去领取吧~``

如果有任何使用问题，欢迎在评论区和我讨论~

> 以下内容，按照访问的用户数量排序。

## 1、自动化办公

关注我的读者都知道，这3年我一直关注``Python自动化办公``这个方向，做了一个方便小白使用的Github开源项目python-office。

1行代码即可实现自动化办公，不需要非程序员学习复杂的编程知识。

如下图所示，截止今日发文，该项目在GitHub获得了``150+ star，10+ contributors``，感谢大家的参与和认可~！
![](https://www.python-office.com/api/img-cdn//wanfeng/opensource-img/python-office.jpg)
>这个网站的技术框架：python-office
<br/>源码下载和使用命令如下：
```python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-office -U

# 因为功能很多，各个功能的使用，请大家移步官方文档。
# 全部免费开源。
 官网链接：https://www.python-office.com/
```


## 2、开源项目的官网


这个项目和上一个息息相关，为了更好的介绍python-office这个项目，我买了``服务器 + 域名 + DNS解析 + CDN``服务等一堆应用，然后用``vuepress``开发了一个配套的网站：https://www.python-office.com。

``这个网站，用电脑打开的主页效果是这样的``👇
![](https://www.python-office.com/api/img-cdn//wanfeng/opensource-img/python-office.com.jpg)



>这个网站的技术框架：vuepress
<br/>源码下载和使用命令如下：

```shell
git clone https://github.com/CoderWanFeng/python-office.com # 把项目clone到本地

cd python-office.com/docs-pages #进入主目录

npm run dev #运行项目，需要你本地有node环境，node环境的下载和安装，我这里就不罗嗦了，百度大量有。
# npm run build
```

## 3、适合手机观看的个人网站

最近我一直在更新知识星球：Python读者圈。

但是发布到其它平台的文章，为了配合平台政策，我可能要做各种各样的内容阉割。

所以有了个人网站以后，在把文章发布到自媒体平台的同时，我也会把``更加完整版内容``发布到自己的网站上。

``手机上的效果是这样的``👇
![](https://www.python-office.com/api/img-cdn//wanfeng/opensource-img/hexo.jpg)


>这个网站的技术框架：hexo
<br/>源码下载和使用命令如下：

```shell
git clone https://github.com/CoderWanFeng/python4office.cn.git #把项目clone到本地

cd hexo/hexo # 进入启动目录

hexo c # 清除残留打包文件

hexo g # 项目打包

hexo s # 本地运行项目

```

## 4、微信机器人

因为自己的``技术群``实在是太多了(100+)，我就给自己开发了一个``微信自动回复机器人``。

``这个机器人不仅可以个人微信号使用，还可以放在公众号后台，给公众号使用。``

>这个网站的技术框架：wxpy（机器人）、flask（回复内容）
<br/>一定注意：微信机器人的使用，必须确保你的微信能登录``网页版微信``，请务必事先确认一下，否则你是用不了的，据我所知无解；公众号使用没有任何限制，所有人的公众号都可以。
<br/>源码下载和使用命令如下：

```shell
git clone https://github.com/CoderWanFeng/weixin-robot.git # 把项目clone到本地

pip install wxpy # 下载依赖

pip install flask # 下载依赖

cd weixin-robot/wechat-robot/code/ # 进入主程序目录

python3 wechat_flask.py # 启动接口

python3 wechat_robot.py # 启动机器人
```

## 5、彩虹屁小程序

这是我最早的有用户的一个项目：彩虹屁小程序，2019年的时候非常流行彩虹屁，我就花了一周的时间，写了一个小程序给我的读者玩。到现在，这个小程序还在正常开通使用，欢迎大家体验。

``效果如下图所示👇``
![](https://www.python-office.com/api/img-cdn//wanfeng/opensource-img/mini.png)

>这个网站的技术框架：微信小程序 · 云开发
<br/>源码下载和使用命令如下：

```shell
浏览器打开：https://github.com/CoderWanFeng/rainbow-miniprogram

# 非常遗憾，因为我之前的操作失误，这个项目的代码全部被删除了。
# 如果你需要的话，请在这个项目的GitHub里提交issues，如果有需要，我会尽力恢复。
```

## 写在最后

从决定从事程序员的第一天起，我就想做一个对别人有用的东西出来，这几年也是一直在探索中。

我做得还不够好，如果``上面的项目有你喜欢的，或者你看过后有更好的创意``，欢迎你来联系我，我们一起把它做得更好~


---

