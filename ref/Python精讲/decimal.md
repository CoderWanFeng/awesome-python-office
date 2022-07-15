1.2-1.0=0.19？Python中不可思议的错误，原来是浮点数计算的陷阱。

![](https://www.python-office.com/api/img-cdn/pro-python/float-error/cover.jpg)


我们先来看一个不可思议的错误：``1.2-1.0=0.19999999999999996``

![](https://www.python-office.com/api/img-cdn/pro-python/float-error/error.jpg)


这是一个常见的错误，你遇到过吗？今天我们就一起来分析一下：
- 原因是什么？
- 如何得到正确的运算？
- python中还有哪些意想不到的错误？

## 先说原因
如果你对计算机毫无了解，你可以跳过这部分，直接去看下一小节：如何得到正确的运算。

**这是因为浮点数运算的特殊性决定的，其它编程语言也有这个问题。**

Python的官方解释器CPython（也就是你下载到电脑上的Python安装包的源码） 中的 float 类型使用C语言的 double 类型进行存储。float 对象的值是以固定的精度（通常为 53 位）存储的二进制浮点数，由于 Python 使用 C 操作，而后者依赖于处理器中的硬件实现来执行浮点运算。

**简单来说，许多可以轻松地用十进制表示的数字不能用二进制浮点表示。**1.2在电脑上存储的值实际值是：``1.1999999999999999555910790149937383830547332763671875``

## 怎么解决？

知道了原因，如何得到正确的结果呢？

不然语法知道一大堆，还是写不好代码；就像道理明白一大堆，依然过不好这一生一样悲哀。

> 解决方法：使用python内置的decimal模块
```python
from decimal import Decimal

a = Decimal('1.2')
b = Decimal('1.0')
print(a - b)  # Decimal('0.2')

# 输出结果：0.2
```

这种方法的好处是精确计算，但也有一个坏处：影响计算速度。适用于你认为精度大于效率的时候，例如：金融行业。
![](https://www.python-office.com/api/img-cdn/pro-python/float-error/get.gif)

## 还有哪些常见错误？

之前给大家整理过2期：
- [【Python新人】常见报错及解决方案，看完少走3个月的弯路，建议收藏！](https://mp.weixin.qq.com/s/jsSRfvBnK97EMuVf-yoSgA)
- [Python官方整理的27个历史遗留问题。](https://mp.weixin.qq.com/s/Wwh7uIXvxFoIQBZBfo04iQ)

> 欢迎大家把你遇到的错误，在评论区和我讨论哟~
---

