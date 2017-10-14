第5周

HTML, CSS, JavaScript
=====================

本 Markdown 在 Visual Studio Code 下借助 Markdown+Math（`goessner.mdmath`）插件完成。

课前准备
-------

* 下载/升级到一款如下列出的最新版本的浏览器（本系列小灶将以 Chrome 完成绝大多数的示例）
    * Chrome ([官网](https://www.google.com/chrome/browser/index.html) / [谷歌中国官网](http://www.google.cn/chrome/browser/desktop/index.html) / [太平洋软件站](http://dl.pconline.com.cn/download/51614-1.html))
    * [Firefox](https://www.mozilla.org/zh-CN/firefox/new/)
* 下载一款纯文本编辑器，推荐（本系列将以 Visual Studio Code 完成大多数的示例）
    * [Visual Studio Code](https://code.visualstudio.com/download) from Microsoft
    * [Atom](https://atom.io) from GitHub
    * [Sublime Text 3](https://www.sublimetext.com/3)
    * [Notepad++](https://notepad-plus-plus.org/download/) (仅适用于 Windows)
* （可选）下载相关实时预览插件
    * `hdg.live-html` for Visual Studio Code

前言
----

第一次的小灶活动，我们会接触到3种分工明确的计算机语言。（实际上，HTML和CSS更适合被称为格式标准。而JavaScript则是一种图灵完备的编程语言。）

小灶系列本来的第一讲想介绍的是数据的存储形式，从csv、json和数据库讲起。但为了将开课时间提前到第五周，尽早开讲，同时又不会来不及做较为充足的准备，第一讲最后还是选择了从数据的呈现讲起。

HTML
----

### 数字化信息

对于计算机而言，任何事务最底层的存在形式就是两种互斥的逻辑态。我们定义一个bit能存储一个逻辑态，这个逻辑态要么是“真”，要么就是“假”。在只有一个bit的情况下，我们只能建立2个双射关系。最常见的一个单bit双射关系如下

$$\{\rm{false},\,\rm{true}\} \mapsto \{0,\,1\}$$

当我们用多个逻辑态组成各种唯一的序列时，我们就有了让用逻辑态与现实生活中的各种事物建立双射关系的可能。

当我们有5个bit时，我们就能建立32对双射关系，可以表示24个字母了；有6个bit时，我们就能有64对双射关系，大小写字母都能表示了。

但是单单能表达英语字母是不够的，我们还需要有标点符号，还需要空格、换行符、用来表达数学运算的`+-*/`、删除、回退……。第一个真正具有足够“表达力”的映射集——ASCII（音：ASS-kee）编码，筛选出了128个字符，用7个bit进行表达。ASCII的确定，让人们可以以一种熟悉的形式与计算机进行交互。

### 结构化信息

在日常生活中，我们可以接触到很多的信息。人可以直接处理多种存在形式的信息，比如爱因斯坦的手稿、林肯乐队的一首歌……而对计算机而言，宣纸墨迹、歌曲声音在经过一定处理前，都是没有办法去处理的。

印刷出来的一首古诗一般都是这样的：

>梅花（宋·王安石）\
>墙角数枝梅，凌寒独自开。\
>遥知不是雪，为有暗香来。

如果直接把上面这几行文字这些作为存储形式，电脑处理起来有些麻烦。

```python
'梅花（宋·王安石）\n墙角数枝梅，凌寒独自开。\n遥知不是雪，为有暗香来。'
```

电脑一般会更喜欢如下的形式：

```xml
<ancientPoem type="诗">
    <title>梅花</title>
    <author>
        <authorTime>宋</authorTime>
        <authorName>王安石</authorName>
    </author>
    <content>
        <line>墙角数枝梅，凌寒独自开。</line>
        <line>遥知不是雪，为有暗香来。</line>
    </content>
</ancientPoem>
```

或是如下的形式
```javascript
{
    type: "诗",
    title: "梅花",
    author: {
        time: "宋",
        name: "王安石"
    },
    lines:[
        "墙角数枝梅，凌寒独自开。",
        "遥知不是雪，为有暗香来。"
    ]
}
```
