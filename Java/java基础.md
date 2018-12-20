### 不记文档，白忙一场

------

#### URL编码解码

```python
后端：   
    import java.net.URLDecoder;
    import java.net.URLEncoder;
    URLEncoder.encode((String)obj --> 编码
    URLDecoder.decode((String)obj --> 解码
前端：
	encodeURIComponent(encodeURIComponent(obj)) --> 编码
	decodeURIComponent(decodeURIComponent(obj)) --> 解码
注意：decodeURI()与decodeURIComponent() 使用与区别
```



