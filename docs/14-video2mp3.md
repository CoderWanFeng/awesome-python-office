1行Python代码，拿到周杰伦新歌的MP3文件，终于可以免费听周杰伦了

![](https://www.python-office.com/api/img-cdn/python-office/jayzhou/cover.jpg)

大家好，这里是程序员晚枫。


## 需求说明
杰伦终于出新歌了，可惜只有一个先行版MV的视频版本。

> 如果想听周杰伦的新歌：高音质的《最伟大的作品》``MP3``格式，怎么办呢？

今天给大家分享一下，如何使用1行Python代码，从MV里提取出完整的MP3文件。


## 1行代码实现

我们使用python来完成提取。
#### 安装python-office这个库

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-office -U
```


#### 1行代码进行验证

这个代码，可以从任意常见格式的视频中，提取出MP3文件。
这里以MP4举例：

```
# 导入这个库：python-office，简写为office
import office

#1行代码，提取mp3文件
office.video.video2mp3(path='d://程序员晚枫的文件夹//最伟大的作品.mp4', mp3_name='《最伟大的作品》')

# 参数作用：
# path = 这里填写你本地的MV文件
# mp3_name = 这里填写你生成的mp3文件名，这里不用改
```
运行以上代码，就会出现MP3格式的《最伟大的作品》了。


> 获取MV文件的下载，大家需要百度一下~



## 阅读更多

> 如果有我没说清楚的，或者在使用过程中有问题，欢迎大家在评论区和我交流~

- []()

- []()



