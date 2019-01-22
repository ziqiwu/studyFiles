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







