兴趣点收集示例
=============

这个示例展示了一个简单粗暴的样板（boilerplate），可以直接基于它开始构建你的 Hackathon 作品。

功能
----

### 示例已经实现的功能
* 地图拖动选点，添加名称后存储到 Django 构建的后端里

### 在现有数据库结构下可以实现的功能
* 给地图点增加标签
* 给地图点增加其他相关信息
    * http://service.shmetro.com/czxx/index.htm?id={StationId}, StationId=0254时显示的是金科路站的信息。可以设计一个机制，获取地铁站的id
* 选择一些已经存储的点，根据经纬度坐标，调用高德地图或者其他厂商的 API，做路径规划
* ……

开工
----

不管你是想直接开工，还是想搞明白这个目录里的东西是怎么来的，好让你心里舒服一些，你都需要保证你的电脑上已经装好了这些基础依赖：
* `Python` 及包管理器 `pip`
    * [`Django`](https://www.djangoproject.com/download/)
    * [`Django REST Framework`](http://www.django-rest-framework.org/#installation) 提供各个 Model 的 API 接口
    * [`Django SSL Server`](https://github.com/teddziuba/django-sslserver) 防止浏览器不通过某些非 HTTPS 请求
    * [`Django CORS Headers`](https://github.com/ottoyiu/django-cors-headers) 不再被跨域问题所烦恼
* `Node.js` 及其包管理器 `npm`
    * 切换到 `frontend` 目录下运行命令 `npm install` 即可，或者按照 [Ant Design 快速上手](https://ant.design/docs/react/getting-started-cn) 给出的步骤操作
    * 然后为了使用高德地图 API，需要安装 `react-amap`（`npm install --save react-amap`）

如果你想从零开始构建这个目录，而不是直接 clone 它，那么你需要访问这些网址：
* [Django Builder](mmcardle.github.io/django_builder/)
* [Ant Design 快速上手](https://ant.design/docs/react/getting-started-cn)

为了使用这个例子中的高德地图 API，你需要到[高德开放平台](http://lbs.amap.com/)注册并获取一个用于 Web 端的 API 密钥，并将其填入 `frontend/mapdemo/mapdemo.jsx` 的相应位置中。

例子中没有使用高德官方提供的 JavaScript API，而是使用了由饿了么前端组封装好的 [React AMap](https://elemefe.github.io/react-amap/articles/start) 库。

在实际开工前，我们要明确这个示例的目标不是提供一个完整的工程项目，而是要让所有的东西尽快工作起来。如果你在足够的时间内能有更好的解决方法，请**毫不犹豫**地替换本示例中的相关部分。

示例作者希望你能够通过示例快速掌握的有：

后端快速构建
-----------
* 通过给出的 Django 示例，可以在有一个需求的时候，快速产生想法——我需要哪些数据对象，它们之间各自的关系是什么？
    * https://www.zhihu.com/question/24696366/answer/29189700 有一个比较不错的数据库基本概念科普
    * Django 官网提供的教程也是不错的上手选择
* 有了由 Django Builder 生成的文件后，怎么去除不需要的依赖，并加上我们需要的依赖（如`django-cors-headers`），然后让网站在本地跑起来（`makemigrations [app_name]`，再`migrate`，再`createsuperuser`，再`runsslserver`）
* 由于浏览器的安全策略，你需要先访问一次后端所运行的地址，手动确认你要访问该网址。不然，前端的 `fetch` 请求都不能成功。
* 在示例中我们采取了极不安全的做法，我们允许了所有的跨域请求（`settings.py` 中 cors header 相关设置），也允许了未登录用户通过 REST API 进行读写增删操作（`api.py` 中 `permissions.AllowAny` 等），但是这可以帮助你避免在搭建 demo 时去处理复杂的权限问题。

前端快速构建
-----------
* 想清楚这个例子中的前端和后端是如何配合的，为什么我们可以说前端页面实际上只是静态文件。学会如何通过 `npm build` 打包文件并部署到服务器上。（在没有虚拟主机的情况下，可以尝试使用`python3 -m http.server`在本地提供静态文件的服务器）
* 看懂例子中 `index.js` 的内容编译后是作为什么文件，如何被挂载到 `index.html` 中去的。
* 去掉 `mapdemo.jsx` 文件中 `export default class ...` 中的 `export default`，编译，刷新，打开开发者工具，在 console 欣赏一下 React 中最常见的报错信息之一。
* 去掉 `mapdemo.jsx` 文件头几行 `import { Map, Marker } from 'react-amap'` 中的花括号，编译，刷新，打开开发者工具，在 console 里再欣赏一下报错信息。
* 在 `mapdemo.jsx` 中示范了 `fetch` 的使用。寅岑学长已经师范了如何使用 Python 去发起 HTTP 请求并接受响应。而在这里，你应该注意一下 `.then()` 的用法——这是处理 Promise 的最佳用法。
* 看各个组件的 `onChange` 等 `props` 是如何链接到组件类（`class`）的各个方法上去的，也查阅一下为什么有的时候我们需要`.bind(this)`。

最后，我们需要再次重申，这是 Hackathon 快速上手网页应用开发的做法，而不是以后构建大型项目、在生产环境中应该采取的做法。如果遇到实践上的困难，**不要犹豫**，赶紧在 QQ 群内提问。
