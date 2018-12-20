### 不记文档，白忙一场

------

#### EL表达式逻辑运算符

```python
示例：
	$("#topFrame").attr("src","salesSortieRankController.do?salesSortieRankList
     &unitCode=${(empty unitCode) ? LOCAL_CLINET_USER.currentDepart.stockCode:unitCode}
     &timeStart=${timeStart}&timeEnd=${timeEnd}&rankRange=${rankRange}")
解释：
	JS中获取URL中的参数，不一定要写JS，EL表达式中就可以进行三目运算符的判断。
	示例中的对应java代码为：
	//开始时间
	request.setAttribute("timeStart",timeStart);
	//结束时间
	request.setAttribute("timeEnd",timeEnd);
	//查看本年数据
	request.setAttribute("rankRange", rankRange);
	//公司code
	request.setAttribute("unitCode",unitCode);
	return new ModelAndView("com/jeecg/statisticsquery/salesSortieRank/salesSortieRankTree");
```



