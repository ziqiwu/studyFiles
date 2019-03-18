### 不记文档，白忙一场

------

#### JavaScript

> ```python
> JavaScript 是网络上最常用也是支持者最多的客户端脚本语言。它可以收集用户的跟踪数据,不需要重载页面直接提交表单，在页面嵌入多媒体文件，甚至运行网页游戏。
> 
> 我们可以在网页源代码的<script>标签里看到，比如：
> <script type="text/javascript" src="https://statics.huxiu.com/w/mini/static_2015/js/sea.js?v=201601150944"></script>
> 
> 
> 示例：
> <html>
> <body>
> 
> <script type="text/javascript">
> var r=Math.random()
> if (r>0.5) 
> {
> document.write("<a href='http://www.w3school.com.cn'>学习 Web 开发！</a>")
> }
> else
> {
> document.write("<a href='http://www.microsoft.com'>访问微软！</a>")
> }
> </script>
> 
> </body>
> </html>
> ```

#### jQuery

> ​	阅读
>
> ```python
> https://www.cnblogs.com/suoning/p/5683047.html#autoid-0-11-0
> ```
>
> ​	详情
>
> ```python
> jQuery 是一个十分常见的库,70% 最流行的网站(约 200 万)和约 30% 的其他网站(约 2 亿)都在使用。一个网站使用 jQuery 的特征,就是源代码里包含了 jQuery 入口,比如:
> <script type="text/javascript" src="https://statics.huxiu.com/w/mini/static_2015/js/jquery-1.11.1.min.js?v=201512181512"></script>
> 
> 
> 代码实例：
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <title>Title</title>
> </head>
> <body>
> 
>     <p>人生的命运必然是你一生做出选择的总结</p>
>     <button id="hide">隐藏</button>
>     <button id="show">显示</button>
>     <button id="toggle">隐藏/显示</button>
> 
>     <script src="/jquery/jquery-1.11.1.min.js"></script>
>     <script>
> 
>         $(document).ready(function(){
>             $("#hide").click(function(){
>                 $("p").hide(1000);
>             });
>             $("#show").click(function(){
>                 $("p").show(1000);
>             });
> 
>         //用于切换被选元素的 hide() 与 show() 方法。
>             $("#toggle").click(function(){
>                 $("p").toggle(2000);
>             });
>         });
> 
>     </script>
> </body>
> </html>
> ```
>
> ​	注意
>
> ```python
> 如果你在一个网站上看到了 jQuery，那么采集这个网站数据的时候要格外小心。jQuery 可以动态地创建 HTML 内容,只有在 JavaScript 代码执行之后才会显示。如果你用传统的方法采集页面内容,就只能获得 JavaScript 代码执行之前页面上的内容
> ```

#### Ajax

> ​	阅读
>
> ```python
> http://www.runoob.com/ajax/ajax-examples.html
> ```
>
> ​	详情
>
> ```python
> 我们与网站服务器通信的唯一方式，就是发出 HTTP 请求获取新页面。如果提交表单之后，或从服务器获取信息之后，网站的页面不需要重新刷新，那么你访问的网站就在用Ajax 技术。
> 
> Ajax 其实并不是一门语言,而是用来完成网络任务(可以认为 它与网络数据采集差不多)的一系列技术。Ajax 全称是 Asynchronous JavaScript and XML(异步 JavaScript 和 XML)，网站不需要使用单独的页面请求就可以和网络服务器进行交互 (收发信息)。
> ```

#### DHTML

> ​	阅读
>
> ```python
> http://www.w3school.com.cn/example/dhtm_examples.asp
> ```
>
> ​	详情
>
> ```python
> Ajax 一样，动态 HTML(Dynamic HTML, DHTML)也是一系列用于解决网络问题的 技术集合。DHTML 是用客户端语言改变页面的 HTML 元素(HTML、CSS，或者二者皆 被改变)。比如页面上的按钮只有当用户移动鼠标之后才出现,背景色可能每次点击都会改变，或者用一个 Ajax 请求触发页面加载一段新内容，网页是否属于DHTML，关键要看有没有用 JavaScript 控制 HTML 和 CSS 元素
> ```

#### 道高一尺魔高一丈

> ```python
> 那些使用了 Ajax 或 DHTML 技术改变 / 加载内容的页面，可能有一些采集手段。但是用 Python 解决这个问题有两种途径
> 1、直接从 JavaScript 代码里采集内容，时间成本高可操作性差
> 2、用 Python 的 第三方库运行 JavaScript，直接采集你在浏览器里看到的页面（么么哒） -- selenium
> ```



