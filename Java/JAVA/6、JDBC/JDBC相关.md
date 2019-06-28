### 不记文档，白忙一场

------

#### ResultSet中列值为null

> ```python
> 前提：
> 	oilTankObj.setTankStorage(rs.getObject("NOW_STORAGE")==null?							null:String.valueOf(rs.getDouble("NOW_STORAGE")));  //如果是null或者空
> 	因为rs.getDouble("NOW_STORAGE")得到的不是null，而是0
>     
> 	数据库里面的int，decimal等类型的字段值为null， 通过jdbc的ResultSet的getInt("x")或者			getDouble("x")取出来之后是null吗，并不是，之前并没有太在意，一直以为取出来应该是null，后来偶然	  发现居然不是null，是0。。 然后就好奇，查了下为什么会是0。
> 来源：
> 	https://men4661273.iteye.com/blog/2360579
> 方法一：使用rs.getObject(String paramString)方法
> 	Object object = rs.getObject("xx");  
>     if (object == null) {  
>         o.setXx(null);  
>     }else{  
>         ……  
>     }  
> 方法二：wasNull（）方法可以判断最后一次get到的数据是否是null的，但是一定要紧跟在需要判断的那个列的	get后面!!
> 	o.setA(rs.getInt("xx"));  
>     if (rs.wasNull()) {  
>          o.setA(null);  
>     }  
> ```

