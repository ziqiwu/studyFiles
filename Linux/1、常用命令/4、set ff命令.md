### 不记文档，白忙一场

------



> ```python
> :set ff
> 
> 查看当前文本的模式类型，一般为dos,unix
> 
> 
> 
> :set ff=dos
> 设置为dos模式
> 
> 也可以用一下方式转换为unix模式
> 
> 
> 
> :%s/^M//g
> 等同于:set ff=unix
>     
> 注意：
> 	其他格式，如果utf等编码格式：
> 	https://blog.csdn.net/chengxuyuanyonghu/article/details/51680319
> ```
>
> 





