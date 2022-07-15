全解 | 45个处理字符串的Python方法，内容太干，请自备一桶水

![](https://www.python-office.com/api/img-cdn/pro-python/str-func/str-func.jpg)

大家好，这里是程序员晚枫。

今天给大家整理了字符串的全部45个方法。


## 一、题目解析
先来看一个题目：
> 判断用户输入的内容里是否含有数字。



实现代码
```
str = input('请输入内容>>')
print(str.isalpha())
```
今天我们来一起看一下，Python中str字符串的所有45个内置操作。

## 二、45个方法

我把这45个方法，根据用途的不同，分为了6个类别：
```
# 下文所有的str，都是用的这个变量 👇
str = 'https://www.python-office.com {content}'
```
### 1、拼接
```
print('-'.join(str))  # 用来指定拼接符号，拼接出一个字符串，效率比+高
print(str.center(100, '*'))  # 字符串居中，左右填充指定内容
print(str.ljust(50, '*'))  # 返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
print(str.rjust(50, '*'))  # 它将原字符串右对齐，并使用空格填充至指定长度，并返回新的字符串。如果指定的长度小于原字符串长度，则直接返回原字符串。
print(str.zfill(50))  # 返回指定长度的字符串，原字符串右对齐，前面填充0。
```


### 2、查找
```
print(str.count('p'))  # 指定内容，在原str中出现了多少次

print(str.find('pip'))  # 包含pip,则返回开始的索引值，否则返回-1。
print(str.index('pip'))  # 包含pip,则返回开始的索引值，否则返回Exception。

print(str.rfind(' '))  # 返回参数字符串在字符串中最后一次出现的位置。没有查询到则返回-1.
print(str.rindex(' '))  # 返回参数字符串在字符串中最后一次出现的位置。没有查询到则返回Exception.
```
### 3、分割和替换
```
print(str.replace(' ', '-'))  # 替换操作，str.replace()函数并不对原有的字符串进行改变。



print(str.partition(' '))  # 如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
print(str.rpartition(' '))  # 类似于 partition() 方法，只是该方法是从目标字符串的末尾也就是右边开始搜索分割符。

print(str.rsplit(' '))  # 如果给出了 maxsplit，则最多进行 maxsplit 次拆分，从 最右边 开始。
print(str.split(' '))  # 分割字符串
print(str.splitlines())  # 按照行界符('\r', '\r\n', \n'等)分隔，返回一个包含各行作为元素的列表，默认不包含行界符。

print(str.lstrip('p'))  # 删除从开头开始指定的字符串，然后返回结果字符串。注意：只能从开头开始
print(str.rstrip('p'))  # 删除 string 字符串末尾的指定字符，默认为空白符，包括空格、换行符、回车符、制表符。
print(str.strip())  # 删除前后的指定字符，默认是空格
```



### 4、大小写操作
```
print(str.capitalize())  # 第一个字母大写，对中文无效
print(str.lower())  # 字母转为小写，只对英语有效
print(str.casefold())  # 字母转为小写，所有语言都有效，例如：德语
print(str.upper())  # 字母全部转为大写，英语有效
print(str.swapcase())  # 将字符串中的英文字母大小写互换，并返回修改后的字符串。
print(str.title())  # 将字符串中的每个单词首字母大写，其余字母小写，并返回新的字符串。
```




### 5、判断内容
```
print(str.startswith('pip'))  # 判断是否以pip为开头
print(str.endswith('office'))  # 判断str是否以office结尾
print(str.isalnum())  # 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
print(str.isalpha())  # 如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
print(str.isascii())  # 如果字符串为空或字符串中的所有字符都是 ASCII，则返回 True，否则返回 False。
print(str.isdecimal())  # 如果字符串中的所有字符都是十进制字符，则返回True
print(str.isdigit())  # isdigit函数检测字符串中是否只包含数字字符。若全部是由数字字符组成的字符串，则返回True，否则返回False。isdigit函数没有参数。
print(str.isidentifier())  # 如果字符串是Python中的有效标识符，返回True。如果不是，则返回False。
print(str.islower())  # islower() 方法检测字符串是否由小写字母组成.
print(str.isupper())  # 检测字符串中所有的字母是否都为大写。
print(str.isnumeric())  # 检查字符串中是否只包含数值字符。此方法只适用于Unicode的对象。

print(str.isprintable())  # 如果字符串中的所有字符都可打印或字符串为空，则返回 True，否则返回 False。
print(str.isspace())  # 检测字符串是否只由空白字符组成。
print(str.istitle())  # 检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
```

### 6、不常用
```
print(str.maketrans())#此静态方法返回一个 可供 str.translate() 使用的转换对照表。
print(str.translate())
print(str.encode(encoding='utf8', errors='strict'))  # 返回字符串编码后的数据，默认的编码是当前的字符串编码。errors为给定的不同错误处理方法。
print(str.expandtabs())  # 用空格替换\t符号
print(str.format(content='yyds'))

format_map_dict = {'content': 'yyds'}
print(str.format_map(format_map_dict))  # str.format_map(mapping) 方法仅适用于字符串格式中可变数据参数来源于字典等映射关系数据时。mapping 会被直接使用而不是复制到一个 dict。
```

## 三、注意事项

上一篇我们分享了：12种Python里正则表达式的用法

同样是处理字符串的操作，str和正则方法的区别是什么呢？

- 你可以简单理解为：str内置方法用来处理简单字符串；正则用来处理复杂的字符串。
- 尽量使用str方法或者正则，因为这样比自己写代码更方便，而且代码运行效率也更快。


---
