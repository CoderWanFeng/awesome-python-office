


![](https://www.python-office.com/api/img-cdn/pandas/read-excel/cover.jpg)
大家好，这里是程序员晚枫。

很多朋友使用Python中的``Pandas这个库进行Excel的数据处理``，数据处理从宏观上分为这么3个阶段：数据读取、数据处理、数据输出。

对于大多数新人来说，在数据读取的这一步就卡住了。

**今天我们就来一起学习一下，``Pandas官方推荐的6种Excel读取方式。``**

>本文一共3部分：下载pandas和生成Excel文件、源码解读、读取Excel的6种方式。
<br/>如果你是一个熟练的Python使用者，你可以直接跳转到第3部分。
<br/>如果你是刚接触Python或者刚接触Pandas，建议你从第1部分开始看。

``下文所有代码，都可以 ←左右→ 滑动查看，也可以直接复制粘贴。``

## 1、准备工作

- 首先，你要下载最新版本的``Pandas``库。这样你才能使用Pandas，这个不难理解吧？

- 其次，你要有一个和本文一样的``Excel``文件。为了确保大家和本文的操作统一，建议大家使用和本文同样的Excel文件。

怎么下载Pandas？怎么获取Excel？``我们都用1行命令来自动搞定``,毕竟我们是自动化办公社区，如果这些操作不能自动化搞定，那岂不是太过分了？


你直接执行下面这行代码，就会生成一个和本文一模一样的Excel文件啦~

#### 1行命令安装：pandas，版本：1.4.0

在你的电脑终端里面，执行下面这行命令，就可以自动安装pandas了~

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-office -U
```


#### 1行命令生成Excel
Excel文件也不需要你四处下载，之前我们不是介绍了一个功能嘛，这里是它的用武之地👉：[1行代码，自动生成带模拟数据的Excel文件](https://mp.weixin.qq.com/s/xVwEjXu58WovgSi4ZTtVQw)

以后我们处理Excel的案例和演示，每次都会使用这种自动生成的方法，你当然也可以手动编辑一个，``但如果未来我们要学习如何处理10w行的Excel文件呢？``不论你是手动生成还是百度云下载，都是一个及其缓慢的过程。

但用下面这个生成方式，模拟一个10w+数据的Excel文件，也是不过是一瞬间的事情，一定要尝试一下哟~你会发现新世界的。📱

```python
import office

office.excel.fake2excel(columns=['name', 'company_prefix','job'], rows=5)

```

在你的PyCharm里面，执行上面这行代码，就可以生成一个如下图所示👇，和本文一模一样的Excel文件啦~
![](https://www.python-office.com/api/img-cdn/pandas/read-excel/excel-water.jpg)


## 2、pandas源代码里说了什么？

其实学习Pandas很简单，不用网上东奔西找，所有的代码功能，``创始人和开发者们都通过注释的方法写在源代码里了。``

如何查找pandas的源代码？

下载好pandas以后，我们就打开pandas的源码，看看pandas推荐的读取方式有哪些。pandas源码的路径：``D:\你的python安装目录\Lib\site-packages\pandas\``

打开源码后，pandas文件夹下有多个目录结构，如下图所示，我们要的读取Excel功能，在``pandas\io\excel\_base.py``文件中的``290行-350行``。如下图所示👇
![](https://www.python-office.com/api/img-cdn/pandas/read-excel/profile-water.jpg)

既然找到了这段源码，那么问题来了👉**源码告诉了我们什么？**

## ３、6种读取Excel的方式

下面我们就根据上文获取到的pandas源码，逐个解析一下这6种读取excel的方式。


### 1、指定索引列读取

这种读取方式，适合Excel里的数据，本身有一列表示序号的情况。
```python
pd.read_excel('fake2excel.xlsx', index_col=0)

# 使用index_col=0，指定第1列作为索引列。
```

结果如下图所示：
- 列名没有对齐，不是代码运行有问题，是因为那么列被当作了索引列。

![](https://www.python-office.com/api/img-cdn/pandas/read-excel/1.jpg)

这种方式不符合我们这个文件的要求，所以我们可以进行以下修改：不要指定索引列。

代码和结果如下：
```python
pd.read_excel('fake2excel.xlsx', index_col=None)
```
![](https://www.python-office.com/api/img-cdn/pandas/read-excel/1-1.jpg)

### 2、指定sheet读取
见名知意。

```python
pd.read_excel(open('fake2excel.xlsx', 'rb'), sheet_name='Sheet2')

# 使用sheet_name=0，指定读取sheet2里面的内容。
```

我们在原表里加入了sheet2，结果如下图所示：
- 这种情况下，不会读取sheet1里面的内容

![](https://www.python-office.com/api/img-cdn/pandas/read-excel/2.jpg)

### 3、取消header读取
读取本身没有列名的数据。

```python
pd.read_excel('fake2excel.xlsx', index_col=None, header=None) 

# 使用header=None，取消header读取。
```

结果如下图所示：
- 这种情况下，适合原Excel表没有列名的情况。
- 我们的文件里有列名的情况下，列名也被当成了数据。

![](https://www.python-office.com/api/img-cdn/pandas/read-excel/3.jpg)

### 4、指定读取格式

这种适合高端玩家，在对数据处理精度要求比较高或者速度要求比较快的情况下。

```python
pd.read_excel('fake2excel.xlsx', index_col=0, dtype={'age': float})  

# 使用dtype，指定某一列的数据类型。
```

结果如下图所示：
- 我们添加了一列：年龄，本来是整数，但是指定float类型之后，读取出来成了小书。
- 这种读取，更适合对数据有特殊要求的情况，例如：金融行业。

![](https://www.python-office.com/api/img-cdn/pandas/read-excel/4.jpg)

### 5、自定义缺失值
这种使用的场景是什么呢？比如在收集信息的时候据时候，发现有人填的年龄是负数，那就自动给他把年龄清空掉，让他重新填写。

```python
pd.read_excel('fake2excel.xlsx', index_col=None,na_values={'name':"庞强"}) 

# 使用na_values，自己定义不显示的数据
```

结果如下图所示：
- 我们的表格里，有个人的名字叫：庞强我们不想显示这个人的名字
- 于是我们就在na_values指定：name这一列是庞强的名字，置为空，在pandas里空值会用NaN表示。

![](https://www.python-office.com/api/img-cdn/pandas/read-excel/5.jpg)


### 6、处理Excel里的注释行

不仅Python是可以写注释的，Excel也是可以写注释的。很多人没有用过，用过的朋友在评论区说一下你为什么给Excel写注释吧~？

pandas提供了处理Excel注释行的方法。
```python
pd.read_excel('fake2excel.xlsx', index_col=None, comment='#') 
```

结果如下图所示：

![](https://www.python-office.com/api/img-cdn/pandas/read-excel/6.jpg)

## ４、写在最后

做为Python程序员，平时需要大家阅读源码，认清楚代码背后的原理和逻辑。

最近使用pandas比较多，正好pandas也可以处理excel，所以近期会持续的更新一些pandas使用的文章。


 >下一篇想看什么，在评论区告诉我吧




