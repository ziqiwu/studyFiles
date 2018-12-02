### 一、表

#### 1、机场、公司的对应关系表

​	CN_COMPANY_AIRPORT

--中国航空油料有限责任公司  S0003
select * from cn_company where pid='S0003'

--华北公司  S0029
select * from cn_company where pid='S0029'

--华北公司本部  S0030
select * 
from CN_AIRPORT
where code in(select AIRPORT_CODE from CN_COMPANY_AIRPORT where BRANCH_OFFICE_CODE='S0030')

#### 2、所有组织机构的信息

​	T_S_Depart

​	注意：independentornot=0是独立实体  ；isdel=0  没有删除

​		    CN_COMPANY_AIRPORT机场和公司的对应关系

#### 3、公司的库存/加油架次相关信息

​	Cn_Company_Stock_View 一条

​	Cn_Company_Sales_EveryDay 历史所有

#### 4、机场的库存/加油架次相关信息

​	Cn_Airport_Stock_RealTime 一条

​	CN_AIRPORT_STOCK_HISTORY 历史所有

#### 5、机场和作业单元关系表

​	CN_AIRPORT_WORKING_UNIT

​	



