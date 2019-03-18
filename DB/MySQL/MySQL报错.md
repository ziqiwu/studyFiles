### 不记文档，白忙一场

------

#### 替换，字符串变数字

**sql示例**

> ```python
> select cast(replace(see,',','') as UNSIGNED) from ganbi_basic limit 10;
> ```

**应用场景**

> ```python
> 字段see的值为'1,385 观看次数'，想把它转换为纯数字1385
> 可以用cast(see as UNSIGNED)函数，但是结果是1，如果是'1385观看人次'，则可以准确取出人数。
> 思路为把','去掉，使用replace(see,',','')
> ```

#### 字符串操作

**sql示例**

> ```python
> select *,cast(replace(see,',','') as UNSIGNED) from ganbi_basic where length(duration)<8 and left(duration, 1)<3 order by length(duration) desc,duration desc 
> ```

**应用场景**

> ```python
> 1、字符串长度：length(duration)
> 2、字符串以什么开头：left(duration, 1)<3或者where left(info_url,4)!='http'。第二个参数是截取长度
> ```

