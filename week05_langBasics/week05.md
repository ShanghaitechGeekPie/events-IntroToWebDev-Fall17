第5周

HTML, CSS, JavaScript
=====================

本 Markdown 在 Visual Studio Code 下借助 `goessner.mdmath` 插件完成。

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

> 本讲讲的只是一切的基础，一般来说，制作相应内容会用到更进阶的工具。

第一次的小灶活动，我们会接触到3种分工明确的计算机语言。（实际上，HTML和CSS更适合被称为格式标准。而JavaScript则是一种图灵完备的编程语言。）

小灶系列本来的第一讲想介绍的是数据的存储形式，从csv、json和数据库讲起。但为了将开课时间提前到第五周，尽早开讲，同时又不会来不及做较为充足的准备，第一讲最后还是选择了从数据的呈现讲起。

为什么不能比HTML更简单
----

[W3C HTML 5 标准文档](https://www.w3.org/TR/html5/)

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
    line: [
        "墙角数枝梅，凌寒独自开。",
        "遥知不是雪，为有暗香来。"
    ]
}
```

> #### 示例1：
> [`examples/sec01_html/00_plain.html`](http://htmlpreview.github.io/?https://github.com/ShanghaitechGeekPie/events-IntroToWebDev-Fall17/blob/master/week05_langBasics/examples/sec01_html/00_plain.html) 是一个简单的 HTML 5 页面，它展现了
> * 纯HTML文件的基本结构
>    * `<!DOCTYPE html>` 声明
>    * `<head>`（头部）
>    * `<body>`（主干）
> * [采用 Base 64 硬编码](https://en.wikipedia.org/wiki/Data_URI_scheme)的图片文件
>    * 作为收藏夹图标（favicon）
>    * 作为图片元素（`<img>`）
> * 列表元素 `<ul>`、`<ol>`、`<dl>`
> * 换行符元素`<br>`

> #### 示例：表单
> [`examples/sec01_html/01_form.html`](http://htmlpreview.github.io/?https://github.com/ShanghaitechGeekPie/events-IntroToWebDev-Fall17/blob/master/week05_langBasics/examples/sec01_html/01_form.html) 演示了一个基本的表单示例，现在很少有应用会直接使用这种最原始的表单。更多的应用选择直接通过 JavaScript 来负责表单的交互。同时，包括`React`在内的各类前端框架，也都有很多组件库内置了组件化设计的表单元素。

> #### 示例：表格
> [`examples/sec01_html/02_table.html`](http://htmlpreview.github.io/?https://github.com/ShanghaitechGeekPie/events-IntroToWebDev-Fall17/blob/master/week05_langBasics/examples/sec01_html/02_table.html) 演示了几个基本的表格。尽管在网站设计中已经很少见了，但表格依旧是用于实现电子邮件复杂布局的一个主流选择。

> #### TODO 示例：`<div>` 与 `<span>`
> [`examples/sec01_html/03_div.html`](http://htmlpreview.github.io/?https://github.com/ShanghaitechGeekPie/events-IntroToWebDev-Fall17/blob/master/week05_langBasics/examples/sec01_html/03_div.html) 演示了 `<div>` 块布局元素与 `<span>` 行内布局元素的基本特性。

穿上 CSS 好逛街
--------------
CSS 的全名叫 Cascaded Stylesheet，即“层叠样式表”。一般而言，记录结构化内容的任务全都交由 HTML 完成，而对于内容的外观部分，则是由 CSS 来完成的。

CSS 的各个语句块可以对 DOM 中的元素赋予各种外观参数。包括定位信息、颜色信息、阴影信息、边框信息……在高版本的 CSS 中，也可以指定过渡效果、关键帧动画等信息。

CSS 入门的2个关键点是**选择器**（指定方法、属性继承）、**盒模型**（`padding`-`border`-`margin`），对这两个关键点有所了解后，就能完成很多事情了。

早期版本的 CSS 只能将所有数据直接指定，而没有设计变量、循环等表达机制。因此产生了一些专门用来编译 CSS 文件的工具，其中 SaSS（基于 Ruby）和 LESS（基于 JavaScript）最为流行。在新的标准草案中，已经加入了原生实现的变量机制。

> #### 示例：选择器
> `examples/sec02_css/00_selector.html` 演示了选择器对应语句的效果

> #### 示例：盒模型
> `examples/sec02_css/01_box_model.html` 演示了盒模型对应语句的视觉效果

> #### 示例：响应式布局
> `examples/sec02_css/02_responsive.html` 演示了响应式布局的一种实现

> #### 示例：过渡动画
> `examples/sec02_css/03_transition.html` 演示了过渡动画

> #### 关键帧动画
> `examples/sec02_css/04_key_frame.html` 演示了关键帧动画

> #### 布局技巧
> `examples/sec02_css/05_positioning.html` 跳转到的[学习 CSS 布局](http://zh.learnlayout.com/index.html)演示了各类布局示例，如固定在页面顶端、在页面中垂直居中等

JavaScript：浏览器不再只是“浏览”器
--------------------------------
在 JavaScript 出现之前，浏览器的用户互动基本上都要通过表单和服务器发生互动，然后从服务器获取新页面来实现。

设想你要制作一个和电脑对战的五子棋，在 JavaScript 出现之前，用户可能在 9 个单选框中点击一个标上`X`，然后点击提交，用户的选择被发送到服务器端，然后服务器选择一个`O`，发送回客户端。

但当有了 JavaScript 之后，你可以让用户浏览器内执行的 JavaScript 脚本来决定到底选哪个格子标上`O`，而不再需要向服务器进行通信了。

当然，早些时候，有好几个流行度不输 JavaScript 的页内交互解决方案，比如来自微软的 ActiveX、半死不活的 Silverlight。还有来自 Adobe 的 Shockwave Flash，也曾借助设计师能快速上手的 Flash 而红遍大江南北。

在网页应用中的 JavaScript，主要操作的是 DOM 中的各个元素。浏览器的开发者在浏览器的 JavaScript 引擎中，提供了操作 HTML 和 CSS 的各类 API，以及进行 HTTP 通信的各类 API。

> #### TODO 示例：定时
> `examples/sec03_js/TODO_00_settimeout.html` 演示了`setTimeOut`实现的定时功能，类似的函数还有`setInterval`

> #### TODO 示例：操作页面元素
> `examples/sec03_js/TODO_01_dom_manipulation.html` 演示了使用 JS 完成的 DOM 操作

> #### TODO 示例：jQuery
> `examples/sec03_js/TODO_02_jquery.html` 演示了经典的基于`jQuery`的 DOM 操作

开发者工具：不再苦烹无米之炊！
---------------------------
不管是 Chrome，还是 Firefox，还是 Edge……大多数的现代浏览器，都提供了功能丰富的开发者工具。

开发者工具中，一般提供了以下的基本工具
* DOM 元素查看器
* JavaScript Console
* 页面资源查看器
* 网络请求瀑布流
* 安全信息查看器
