# 10分钟入门HTML、CSS和JavaScript

Copyright &copy; Yuehao Wang. All Rights Reserved.

---
## HTML入门

简单来讲，HTML是一个用于写网页的标记语言。写法如下：

```html
<!DOCTYPE html>
<html>
<head></head>
<body></body>
</html>
```

代码分析：

第一行：声明html版本，这里的写法代表使用html5。

第二行：`<html>`标签代表html开始。html中处了`<html>`标签，还有各种各样的标签，标签的格式基本都是`<标签名字>标签中的内容</标签名字>`，对于特殊的表情可以没有`标签中的内容</标签名字>`部分。不同的标签有不同的用途。

第三行：`<head>`标签里可以放入一些类似用于配置网页的东西，比如设置网页标题，引入JavaScript脚本和css样式表。

第四行：`<body>`标签中放置网页内容。比如放入`<p>`，`<div>`这些标签。

以下，用html写一个Hello, world：

```html
<!DOCTYPE html>
<html>
<head></head>
<body>
<p>Hello, world!</p>
</body>
</html>
```

编写+运行html，通常情况下，我们不需要安装额外的开发工具，直接创建一个`你喜欢的文件名.html`，然后向其中加入html代码，最后用浏览器打开这个html文件即可。

之所以html采用了`<xxx>abc</xxx>`的语法形式，可能和网页设计中需要用到标签间的层级关系有关，也就是说，一个标签下面可能有很多子标签，子标签一同组成了父标签。这种层级关系可以大大简化网页设计。以下是一个更为复杂的网页：

```html
<!DOCTYPE html>
<html>
<head>
	<title>Html demo</title>
</head>
<body>
<p>Hello, html!</p>
<button>Click me!</button>
<ul>
	<li>todo 1</li>
	<li>todo 2</li>
	<li>todo 3</li>
</ul>
<a href="https://geekpie.org">Go to GeekPie</a>
</body>
</html>
```

Html使用`<!--code-->`的方式进行注释，读者可以将上面代码部分注释掉，观察网页上少了什么，这样就能清楚地知道每个标签的实际意义。除此之外，html中的每一个标签也可以被称为一个元素。元素可以添加很多的属性，如添加id属性：`<p id="text">just a text</p>`。


---
## CSS入门

CSS是用于修饰html元素的样式表语言。基本语法如下：

```css
/** 所有p标签用以下样式 */
p {
	font-size: 20px;    /** 文字大小设为20像素 */
	color: #FF0000;     /** 字体颜色设为红色 */
}


/** id属性为abc的标签用以下样式 */
#abc {
	font-family: Arial; /** 字体设置为Arial */
}

/** class属性为cls的标签用以下样式 */
.cls {
	background: #000000; /** 背景色设置为黑色 */
}
```

CSS代码不能单独地用浏览器打开运行，需要在.html文件引入。引入方式有两种：

- 方式一

直接在.html文件的`<style>`标签中写入css代码：

```html
<!DOCTYPE html>
<html>
<head>

<!-- 引入css -->
<style>
p {
	color: red;
}
</style>

</head>
<body>
<p>Hello, world!</p>
</body>
</html>
```

运行上面代码，你就可以看到我们的Hello, world文本变色了。

- 方式二

首先创建一个.css文件（这里假设名为abc.css，且在.html文件的同级目录下），向abc.css写入代码，然后在.html文件写入如下代码：

```html
<!DOCTYPE html>
<html>
<head>

<!-- 引入css -->
<link rel="stylesheet" type="text/css" href="./abc.css">

</head>
<body>
<p>Hello, world!</p>
</body>
</html>
```


---
## JavaScript入门

JavaScript（简称js）通常作为浏览器中的网页脚本语言（然而JavaScript的使用途径远不止这一个），它可以使原本“静止”的网页“动起来”。举个例子，前面我们的Hello, world例子中，呈现的界面是“静止”的，也就是说你看到的网页永远都是同一个位置同一种样式的同一行文本，要让这个文本“动起来”，比如动态地改变它的位置和字体大小，就需要用到JavaScript。首先来学习JavaScript的基本语法：

```javascript
// 注释用 // 或者 /**/


// 定义变量，开头使用var关键字
var n = 1;
var s = "string";
var b = true, a = [1, 2, 3];


// 定义含有3个参数的函数
function func_name(param1, param2, param3) {
	// 函数内容
}
// 调用函数
func_name(value1, value2, value3);


// 条件判断
if (n > 2) {
	// 当n > 2时，运行这里
} else if (n > 0) {
	// 当 2 > n > 0时，运行这里
} else {
	// 其他情况，运行这里
}


// for循环，和C语言类似
for (var i = 0; i < 10; i++) {
	// 循环内容
}


// 弹窗
alert("我是弹窗");
```

JavaScript代码不能单独地用浏览器打开运行，需要在.html文件引入。引入方式有两种：

- 方式一

直接在.html文件的`<script>`标签中写入JavaScript代码：

```html
<!DOCTYPE html>
<html>
<head>

<!-- 引入JavaScript脚本 -->
<script>
// 这里添加JavaScript代码
</script>

</head>
<body>
<p>Hello, world!</p>
</body>
</html>
```

- 方式二

首先创建一个.js文件（这里假设名为xxx.js，且在.html文件的同级目录下），向xxx.js写入脚本代码，然后在.html文件写入如下代码：

```html
<!DOCTYPE html>
<html>
<head>

<!-- 引入JavaScript脚本 -->
<script type="text/javascript" src="xxx.js"></script>

</head>
<body>
<p>Hello, world!</p>
</body>
</html>
```

JavaScript脚本被引入后，就可以使用脚本对网页进行操作了。具体怎么操作html里的元素呢？看下面的例子：

```html
<!DOCTYPE html>
<html>
<head>

<!-- 引入JavaScript脚本 -->
<script>
window.onload = function () {
	var pTag = document.getElementById("text");
	pTag.innerHTML = "Hello, ";
};
</script>

</head>
<body>
<p id="text">Hello, world!</p>
</body>
</html>
```

首先，在JavaScript脚本中，`window.onload`被赋值成为了一个函数，这个函数在页面加载完成后会被调用，这样做的目的是为了防止页面未加载完成就进行后续操作所带来的问题。

接下来，我们用到了`document.getElementById`，这个函数是浏览器中的内置的，它可以根据id属性获取指定的元素，上述代码表示获取id为"text"的元素。

获得了html元素之后，我们就可以对其进行操作了，上面的代码更改了元素的`innerHTML`属性，也就是更改了`<p>`中的内容部分。


### 更多JavaScript例子

#### var关键字
`var`是用于声明变量的关键字。`var`无奇不能，几乎所有的JavaScript中的对象（包括函数）都可以存放在`var`中。

```javascript
var i = 0;
var j = 3.1415926;
var s = "Hi, Js";
var a = ["abc", "hhh", 123];
var f = function() {alert("function!");};
```

#### 使用数组Array
```javascript
// 定义数组
var a = [1, 2, 3];

// 遍历数组
for (var i = 0; i < a.length; i++) {
	alert(a[i]);
}

// 定义空数组
var b = [];
var c = new Array();
```

#### 函数使用
```javascript
// 用于y = x * x的函数
function y(x) {
	return x * x;
}
// 或者写为
var y = function(x) {
	return x * x;
};

// 调用函数
y(3);
```

---
> 本教程到此为止，仅作为Web前端最基本入门教程。全面的学习大家还是得看看详尽的教程。
> 
> 参考：http://www.w3school.com.cn/index.html
