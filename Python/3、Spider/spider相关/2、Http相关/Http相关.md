### 不记文档，白忙一场

------

#### Http详细介绍

> ```python
> http协议这一篇就够了：https://www.cnblogs.com/ranyonsue/p/5984001.html
> ```

#### Https是什么

> ```python
> http就是应用层的协议，https， s代表secure，比http安全。ssl
> ```

#### 常见端口

> ```python
> http：明文传输   80
> https：加密传输  443 
> ftp：21
> ssh：22
> mysql：3306
> redis：6379
> MongoDB：27017
> ```

#### Http工作原理简单介绍

> ```python
> url详解：
> 	http://www.taobao.com:80/index.html?username=goudan&password=123#anchor
> 	协议   主机           端口号  路径  query-string（参数）         锚点
> 原理：
> 	一张网页的程序有至少10-20个请求，每一个css、js、图片都是一个http请求
> 	浏览器就会将html、css、js、img翻译成图文并茂的形式
> http请求和响应：
> 	请求行、请求头、请求体
> 	get、post
> 	响应行、响应头、响应体
> 请求头
> 官方说明：https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html
> 表格整理：https://kb.cnblogs.com/page/92320/
> ```

#### 常见的Http状态码

> ```python
> 常见的http状态码
> 
> 100：继续 客户端应当继续发送请求。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。
> 
> 101： 转换协议 在发送完这个响应最后的空行后，服务器将会切换到在Upgrade 消息头中定义的那些协议。只有在切换新的协议更有好处的时候才应该采取类似措施。
> 
> 102：继续处理 由WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。
> 
> 200：请求成功 处理方式：获得响应的内容，进行处理
> 
> 201：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到 处理方式：爬虫中不会遇到
> 
> 202：请求被接受，但处理尚未完成 处理方式：阻塞等待
> 
> 204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。 处理方式：丢弃
> 
> 300：该状态码不被HTTP/1.0的应用程序直接使用， 只是作为3XX类型回应的默认解释。存在多个可用的被请求资源。 处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃
> 301：请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL来访问此资源 处理方式：重定向到分配的URL
> 
> 302：请求到的资源在一个不同的URL处临时保存 处理方式：重定向到临时的URL
> 
> 304：请求的资源未更新 处理方式：丢弃，使用本地缓存文件
> 
> 400：非法请求 处理方式：丢弃
> 
> 401：未授权 处理方式：丢弃
> 
> 403：禁止 处理方式：丢弃
> 
> 404：没有找到 处理方式：丢弃
> 
> 500：服务器内部错误 服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般来说，这个问题都会在服务器端的源代码出现错误时出现。
> 
> 501：服务器无法识别 服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。
> 
> 502：错误网关 作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。
> 
> 503：服务出错 由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复。
> 
> -------------------------------------------------------------------------------------------常见的http状态码
> 1xx：指示信息--表示请求已接收，继续处理
> 2xx：成功--表示请求已被成功接收、理解、接受
> 3xx：重定向--要完成请求必须进行更进一步的操作
> 4xx：客户端错误--请求有语法错误或请求无法实现
> 5xx：服务器端错误--服务器未能实现合法的请求
> 
> 200 OK                        //客户端请求成功
> 400 Bad Request               //客户端请求有语法错误，不能被服务器所理解
> 401 Unauthorized              //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用 
> 403 Forbidden                 //服务器收到请求，但是拒绝提供服务
> 404 Not Found                 //请求资源不存在，eg：输入了错误的URL
> 500 Internal Server Error     //服务器发生不可预期的错误
> 503 Server Unavailable        //服务器当前不能处理客户端的请求，一段时间后可能恢复正常
> ```

#### 请求头信息详解

> ```python
> 官方说明：https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html
> 表格整理：https://kb.cnblogs.com/page/92320/
> 
> 浏览器端可以接受的媒体类型 ，MIME
> Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8
> 
> 浏览器申明自己接收的编码方法，通常指定压缩方法，是否支持压缩，支持什么压缩方法（gzip，deflate），（注意：这不是指字符编码）;
> Accept-Encoding:gzip, deflate, br
> 
> 浏览器申明自己接收的语言。其中 en-US 的权重最高 ( q 最高为1，最低为 0)，服务器优先返回 en-US 语言
> Accept-Language:en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
> 
> 和缓存相关
> Cache-Control:max-age=0
> 
> 连接方式，保持长连接
> 例如：　
> Connection: keep-alive   
> 当一个网页打开完成后，客户端和服务器之间用于传输HTTP数据的TCP连接不会关闭，如果客户端再次访问这个服务器上的网页，会继续使用这一条已经建立的连接
> 例如：  
> Connection: close  代表一个Request完成后，客户端和服务器之间用于传输HTTP数据的TCP连接会关闭， 当客户端再次发送Request，需要重新建立TCP连接。
> 
> 会话相关
> Cookie:BIDUPSID=9F5816DD3088F4291EA4C12FFC2ABCDE; BAIDUID=78AF1CE91C8F84BD601F6E2778C618DA:FG=1; PSTM=1513827071; BD_UPN=12314353; H_PS_PSSID=1454_21125_18559_25177; BD_CK_SAM=1; PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; pgv_pvi=769396736; pgv_si=s5038345216; BD_HOME=0; H_PS_645EC=3ff96rRFDTjHDZ%2BqFcj5%2FYOP6KISjZyhvnS1a%2B1q4A19NgE%2FSjllKIn8ejA
> 
> 主机
> Host:www.baidu.com
> 
> 申明浏览器支持从 http 请求自动升级为 https 请求，并且在以后发送请求的时候都使用 https。
> 当页面中包含大量的 http 资源的时候（图片、iframe），如果服务器发现一旦存在上述的响应头的时候，会在加载 http 资源的时候自动替换为 https 请求。
> Upgrade-Insecure-Requests:1
> 
> 向服务器发送浏览器的版本、系统、应用程序的信息。
> Chrome 浏览器的版本信息为 63.0.3239.132，并将自己伪装成 Safari，使用的是 WebKit 引擎，WebKit伪装成 KHTML，KHTML伪装成Gecko（伪装是为了接收那些为Mozilla、safari、gecko编写的界面）
> User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36
> 
> 如果是ajax请求，一般都带这个
> X-Requested-With: XMLHttpRequest
> 
> 上一个页面，你从哪个页面过来的
> Referer: https://www.baidu.com/?tn=57095150_6_oem_dg
> 图片防盗链
> ```
>

#### 响应头信息详解

> ```python
> 响应头信息
> Connection:Keep-Alive
> 	
> 控制浏览器的缓存，常见值为 private、no-cache、max-age、alidate，默认为 private，根据浏览器查看页面不同的方式来进行区别。
> 浏览器在访问了该页面后，不再会访问服务器。max-page=0表示关闭浏览器过期。
> Cache-control: max-age=0
> 	
> 内容编码格式
> Content-Encoding:gzip
> 
> 内容类型
> Content-Type:text/html; charset=utf-8
> 
> 时间
> Date:Sun, 24 Dec 2017 04:21:28 GMT
> 	
> 过期时间
> Expires:Sun, 24 Dec 2017 04:20:29 GMT
> 	
> 服务器版本
> Server:BWS/1.1
> 	
> 给客户端保存的cookie值
> Set-Cookie:BDSVRTM=0; path=/
> Set-Cookie:BD_HOME=0; path=/
> Set-Cookie:H_PS_PSSID=1454_21125_18559_25177; path=/; domain=.baidu.com
> 
> 内容是否分块传输
> Transfer-Encoding:chunked
> 
> 常见的http状态码
> 1xx：指示信息--表示请求已接收，继续处理
> 2xx：成功--表示请求已被成功接收、理解、接受
> 3xx：重定向--要完成请求必须进行更进一步的操作
> 4xx：客户端错误--请求有语法错误或请求无法实现
> 5xx：服务器端错误--服务器未能实现合法的请求
> 
> 200 OK                        //客户端请求成功
> 400 Bad Request               //客户端请求有语法错误，不能被服务器所理解
> 401 Unauthorized              //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用 
> 403 Forbidden                 //服务器收到请求，但是拒绝提供服务
> 404 Not Found                 //请求资源不存在，eg：输入了错误的URL
> 500 Internal Server Error     //服务器发生不可预期的错误
> 503 Server Unavailable        //服务器当前不能处理客户端的请求，一段时间后可能恢复正常
> ```

