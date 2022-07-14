

![](https://www.python-office.com/api/img-cdn/python-office/only-win/cover.jpg)

python-office自动化办公这个开源项目是2022.5.13号上线，至今1个多月的时间分别在GitHub获得了150+ star，在Gitee获得了250+ star。

![](https://www.python-office.com/api/img-cdn/python-office/only-win/star.jpg)

> 从项目创建的第一天，就有朋友反馈：这个库支持Mac和Linux吗？

> 我一般都是直接回复：想支持，但是我做不到。有一个不太完美的替代方案。

今天【知识星球：Python读者圈】里也有了提问，我就详细给大家解释一下我做不到的原因，如果你有解决思路，欢迎大家在评论区和我交流~

## 1、技术上，很难解决

根据我的python开发经验来说，很多流行的第三方库，比如：redis、supervisor等常用的专业开发工具，都不能做到windows系统和Mac系统、Linux系统完美兼容，甚至根本无法兼容。再加上Office软件本身不能兼容的问题。

客观地讲，这些著名第三方库、以及微软Office的程序员的开发水平比大多数的程序员都要高，他们都没解决兼容问题，我有点怂。

我和一些开源小伙伴也曾经想过顶住这种压力，相信自己的研发能力，把这个难题给攻克。``然后仔细看了看代码，python-office里面，不兼容的问题主要是来自win32com，而win32com是只能适配win系统的。``

然而因为我自己目前资源和精力有限，如果现在花时间去研发底层兼容的技术（先假如我们能做到），最近3、5年（往乐观了说），我们这个python-office都没法往前开发新的功能，也没法使用了。

``对于一个新项目来说，完成更重要，还是完美更重要？我选择的是先完成，等做大了，有时间有资源了，再考虑解决可能是整个行业都在面临的问题（假如我们的项目能活到那时候）。``

## 2、用户用什么操作系统？

生产一台笔记本电脑和开发一个开源项目的共同点是什么？我觉得是有人用。

python-office项目，目前主要面向的是非程序员的办公群体。

市场上主流的``办公用``操作系统有：Win、Mac、Linux。最近的一次百度发布的调查显示，它们之间的占比分别约为89%、3.7%、0.79%。

![](https://www.python-office.com/api/img-cdn/python-office/only-win/xitong.png)

说实话，我作为一个开发者，更喜欢用Mac和Linux，我甚至可以完全不打开Windows的电脑。但是python-office不只是我一个人用。

在第1个问题，技术上无法解决导致的面对多个操作系统只能选择一个进行开发的情况下，``如果你是开发者，你会选择哪一个？我选择了使用人数最多的Windows系统。``

## 3、放弃了，但没完全放弃。

虽然从宏观上看，技术上是这样、整个市场是这样，但是微观上，对使用这个项目的Mac、Linux用户来说，如果就是想试试怎么办？

> 我同步发布了：python-office-mac 和 python-office-linux。直接使用pip就可以安装。

功能上，相对于原版本的python-office有所阉割。目前源代码和python-office在同一个github仓库，分别是：mac分支和linux分支。也欢迎有兴趣的同学，参与到这2个分支的开发中。


![](https://www.python-office.com/api/img-cdn/python-office/only-win/github.jpg)


## 4、小结

综上所述，目前python-office因为技术上、市场使用率上的考虑，最完整的版本是windows系统的开发，其它系统的朋友，比如：Mac、Linux，可以考虑使用对应的python-office-mac、python-office-linux这些第三方库。

----
> 如果你有疑问或者创意，请在评论区和我交流哟~








