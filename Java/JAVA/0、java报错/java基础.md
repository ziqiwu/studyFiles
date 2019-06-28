### 不记文档，白忙一场

------

#### URL编码解码

> (1) 示例：
>
> ```python
> 后端：   
>     import java.net.URLDecoder;
>     import java.net.URLEncoder;
>     URLEncoder.encode((String)obj --> 编码
>     URLDecoder.decode((String)obj --> 解码
> 前端：
> 	encodeURIComponent(encodeURIComponent(obj)) --> 编码
> 	decodeURIComponent(decodeURIComponent(obj)) --> 解码
> 注意：decodeURI()与decodeURIComponent() 使用与区别
> ```
>
> (2) 大麻烦
>
> ```python
> 之前用的是：
> 	前端(编码) --> encodeURIComponent(encodeURIComponent(obj))
>    	中间网址来回跳转，都不进行编解码，只有到最后一步到后端了
>     后端(解码) --> URLDecoder.decode((String)obj
> 	结果 --> 一直都是好使的，后来突然不能用，后端解码之后获取到的也是???
> 最后解决：
> 	前端(编码) --> 不变
> 	中间(来回跳转) --> 不变
> 	后端(解码) --> new String(req.getParameter("xxx").getBytes("ISO8859-1"), "UTF-8"));
> 	结果 --> 好使了
> ```

#### 日期加减 + 时间戳

```python
Date now = new Date();
System.out.println("---当前时间戳："+dt.getTime());

Calendar calendar = Calendar.getInstance();
calendar.setTime(now);
calendar.add(Calendar.DAY_OF_YEAR,-3);//日期减3天
Date ago=calendar.getTime();
System.out.println("---三天前时间戳："+ago.getTime());
```





