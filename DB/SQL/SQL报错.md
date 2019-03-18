### 不记文档，白忙一场

------

#### 复杂sql写法

> ```python
> 示例：
> 第一步：先列出每个表的基本信息，和相互关系
>     --机场数据
>     select * from CN_BASIC_INFO_STATISTIC where STATISTIC_TIME='20181010'
> 
>     --机场和油库对应关系
>     select * from CN_AIRPORT_WORKING_UNIT where airport_code='2110'
> 
>     --油库数据
>     select * from CN_WORKINGUNIT_STOCK_DAY where unit_code in('Z2102','Z2105') and 					statistic_time='2018-07-15'
> 
> 第二步：把表都关联起来
>     select * from
>     (#对应关系(以该表为基准表)   AIRPORT_CODE机场code，WU_CODE作业单元
>         select * from CN_AIRPORT_WORKING_UNIT where airport_code='2110'
>     ) aa
>         left join 
>     ( #机场数据  UNIT_CODE机场code，UNIT_NAME机场名称，STATISTIC_TIME，STOCK_VIEW_DAY
>         select * from CN_BASIC_INFO_STATISTIC where STATISTIC_TIME='20181010'
>     ) bb
>         on aa.AIRPORT_CODE =bb.UNIT_CODE
>         left join
>     (#油库数据  UNIT_CODE作业单元code,UNIT_NAME作业单元名称，STATISTIC_TIME，STOCK_VIEW_DAY
>         select * from CN_WORKINGUNIT_STOCK_DAY where unit_code in('Z2102','Z2105') and 					statistic_time='2018-07-15'
>     ) cc
>         on aa.WU_CODE = cc.UNIT_CODE
> #注意：一定要先找到基准表，应该有哪些数据，是全的。比如示例中以CN_AIRPORT_WORKING_UNIT为基准表，
> 	#CN_BASIC_INFO_STATISTIC和CN_WORKINGUNIT_STOCK_DAY是大恒跑存储过来的数据。如果查询的时间内没有
> 	#数据。则按基准表left join也一定有数据，只不过对应的值为空而已。
> ```

#### SQL中有''

> (1) 情况一：
>
> ```python
> 概述：    
>     String sql ="select aa.code,'#1' as statistic_time from ( "
>     其中'#1'代表时间，比如'2018-10-10'
> 解决：
> 	sql = String.format(sql.replace("#1", "%s"), "2018-10-10");
> ```
>
> (2) 情况二：
>
> ```python
> 概述：
> 	要用到模糊查询
>     String sql = "select * from ta where airport_name like ? "
> 解决：
> 	ps.setString(1,"%"+airportName+"%")
> 注意：
> 	不用加''，即不用写成ps.setString(1,"'%"+airportName+"%'")，否则查不到结果
> ```

#### SQL的where条件思路

**sql示例**

> ```python
> select *
> FROM
> (
> 	select OIL_TANK_PCODE,oil_tank_code,to_number(max(oil_height))
> 	from CN_HEIGHT_VOLUME_RELATION
> 	where OIL_TANK_PCODE in(
> 		select distinct(pcode) from cn_oil_tank where oil_tank_addr is not null 
> 	) 
> 	group by oil_tank_pcode,oil_tank_code
> 	order by oil_tank_pcode,oil_tank_code
> ) tt1
> 	left join 
> (
> 	select pcode,code from cn_oil_tank where oil_tank_addr is not null group by pcode,code
> ) tt2
> 	on tt1.OIL_TANK_PCODE = tt2.pcode and tt1.oil_tank_code=tt2.code
> 	left join
> (
> 	select code as ttcode,name as ttname from CN_WORKINGUNIT 
> ) tt3
> 	on tt2.pcode=tt3.ttcode 
> where pcode is not null and code is not null
> order by tt1.OIL_TANK_PCODE,tt1.oil_tank_code
> ```

**sql解析**

> ```python
> tt1表中多出来的油罐code，是不需要的，tt2表中多出来的油库code是不需要的。思路是：并不一定要在单表中就写where条件过滤掉 --> 完全可以根据左连接和右连接产生的一方的null值来进行筛选。
> 如上sql所示：以tt1表为基准表，和tt2表关联的条件是两边的油库code相等，油罐code也相等。tt1基准表的字段都留下来了，但是tt2表就会因为油库code多出来关联不上是null，油罐code少出来就更关联不上也是null了。
> ```

#### mysql和oracle子查询

**mysql必须写成**

> ```python
> delete from ganbi_basic
> where id not in(
> 	select ids from
> 	(
> 		select max(id) "ids" from ganbi_basic group by info_url,title order by 					count(info_url) desc
> 	) tt1
> )
> 【注】即必须多一层select ids from
> ```

**oracle直接写成**

> ```python
> delete from ganbi_basic
> where id not in(
>     select max(id) "ids" from ganbi_basic group by info_url,title order by 					count(info_url) desc
> )
> 【注】直接这样写即可
> ```

#### oracle的clob改为varchar2

> ```python
> -------------------修改cn_scada_alarm-------------------
> --新增一个字段，类型为VARCHAR2
> alter table CN_SCADA_ALARM add temp VARCHAR2(120);
> --将字段类型Clob的列数据更新到新增的列
> update CN_SCADA_ALARM set temp=RAW_DATA;
> --删除Clob列
> alter table CN_SCADA_ALARM drop column RAW_DATA;
> --将新增列名更改为原来的列名
> alter table CN_SCADA_ALARM rename column temp to RAW_DATA;
> ```

#### 为空则替换为0函数

> ```python
> 1、mysql为ISNULL(check_expression,replacement_value)
> 	select ISNULL(null,0) from dual --> 输出0
> 	select ISNULL('value',0) from dual --> 输出value字符串
> 2、oracle为NVL(eExpression1, eExpression2)
> 	select NVL(null,0) from dual --> 输出0
> 	select NVL('value',0) from dual --> 输出value字符串
> ```
>









