### 不记文档，白忙一场

------

#### 复杂sql写法

```python
示例：
第一步：先列出每个表的基本信息，和相互关系
    --机场数据
    select * from CN_BASIC_INFO_STATISTIC where STATISTIC_TIME='20181010'

    --机场和油库对应关系
    select * from CN_AIRPORT_WORKING_UNIT where airport_code='2110'

    --油库数据
    select * from CN_WORKINGUNIT_STOCK_DAY where unit_code in('Z2102','Z2105') and 					statistic_time='2018-07-15'

第二步：把表都关联起来
    select * from
    (--对应关系
        select * from CN_AIRPORT_WORKING_UNIT where airport_code='2110'
    ) aa
        left join 
    ( --机场数据
        select * from CN_BASIC_INFO_STATISTIC where STATISTIC_TIME='20181010'
    ) bb
        on aa.AIRPORT_CODE =bb.UNIT_CODE
        left join
    (--油库数据
        select * from CN_WORKINGUNIT_STOCK_DAY where unit_code in('Z2102','Z2105') and 					statistic_time='2018-07-15'
    ) cc
        on aa.WU_CODE = cc.UNIT_CODE
```





