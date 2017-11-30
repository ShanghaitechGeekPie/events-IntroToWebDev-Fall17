第11周 LAB

React Router 和 Fetch API
=========================

有哪些步骤
---------
按照 [第9周 第一个 ReactJS 应用](https://github.com/ShanghaitechGeekPie/events-IntroToWebDev-Fall17/blob/master/week09_firstReactJsApp/week09.md) 的内容，搭建好开发环境。然后利用 [`wk11example`](https://github.com/ShanghaitechGeekPie/events-IntroToWebDev-Fall17/tree/master/week11_reactRouter_fetch/wk11example) 内的内容，尝试以下操作。

关键点
------
* 前端路由（UI 与 URL 同步）：[React Router](https://reacttraining.com/react-router/)
* 前后端通信：原生 [Fetch API](https://developer.mozilla.org/zh-CN/docs/Web/API/Fetch_API)（也可以考虑用 [axios](https://github.com/axios/axios)，或是 GitHub 维护的 [github/fetch](https://github.github.io/fetch/) 等库）

React Router
------------

传统的网站中，各个不同功能的执行经常要涉及从后端获取新的 HTML 文件。比如传统的电商购物车，涉及如下步骤

| 用户界面（前端） | 服务器（后端） |
|----------------|---------------|
| 进入商品页面，`GET /productDetail?id=65530` | 从数据库调取 `65530` 商品的信息，生成完整的 HTML 响应 |
| 点击添加进购物车，`GET /addToCart?id=65530&qty=1` | 写入数据库信息，返回添加成功确认页的 HTML 响应 |

传统的网站与现代网站应用最显著的差异是完整的 HTML 响应越来越少，而 JSON 响应越来越多。因为的确，最关键的信息就在这些 JSON 里了，每次都做完整的 HTML 响应有些买椟还珠的感觉。但是，我们也想保留 `/productDetail`、`/addToCart` 这样以不同路径切换内容的体验，从开发角度来说，功能状态不会混作一团，debug 也更明晰；对用户而言，路径变化也使具体行为感知更加明晰。

在引入 React Router 之前，我们可以看看原生 JavaScript 能如何操作浏览器的地址栏。随便打开一个网页，然后在 console 里输入下面的代码，就能够看到地址栏的变化。

```javascript
history.pushState(
  {},
  '',
  'some/other/url'
)
```

关键点就在于，虽然地址栏内容变了，但没有产生新的 HTTP 请求。在 React 构建的应用中，我们希望不同的路径对应不同的组件，但组件其实都已经在本地，无需向后端请求了。说起来有点抽象和拗口，但是跑完例子你就应该有所领会了。
