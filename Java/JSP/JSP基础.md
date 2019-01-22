### 不记文档，白忙一场

------

#### EL表达式逻辑运算符

> ```python
> 示例：
> 	$("#topFrame").attr("src","salesSortieRankController.do?salesSortieRankList
>      &unitCode=${(empty unitCode) ? LOCAL_CLINET_USER.currentDepart.stockCode:unitCode}
>      &timeStart=${timeStart}&timeEnd=${timeEnd}&rankRange=${rankRange}")
> 解释：
> 	JS中获取URL中的参数，不一定要写JS，EL表达式中就可以进行三目运算符的判断。
> 	示例中的对应java代码为：
> 	//开始时间
> 	request.setAttribute("timeStart",timeStart);
> 	//结束时间
> 	request.setAttribute("timeEnd",timeEnd);
> 	//查看本年数据
> 	request.setAttribute("rankRange", rankRange);
> 	//公司code
> 	request.setAttribute("unitCode",unitCode);
> 	return new ModelAndView("com/jeecg/statisticsquery/salesSortieRank/salesSortieRankTree");
> ```

#### for循环 + if判断

> ```python
> <table width="100%" border="0" cellspacing="0" cellpadding="0" class="main">
> 	<c:forEach items="${realStockList}" var="item" varStatus="status">
> 		<c:choose>
> 			<c:when test="${type == '4'}"><!-- 如果 -->
> 				<tr style="height:25px;width: 100%;cursor: pointer;background-color: 									green;"  onclick="showOrHide('Z2102');">
> 					<td class="unitNameCls">200</td>
> 					<td class="realStockCls">200</td>
> 					<td>200</td>
> 					<td class="timeCls">200</td>
> 				</tr>
> 			</c:when>
> 			<c:otherwise> <!-- 否则 -->
> 				<tr style="height:25px;width: 100%;display: none;display:none;" 									class="Z2102">
> 					<td class="unitNameCls">&nbsp;&nbsp;&nbsp;200</td>
> 					<td class="realStockCls">200</td>
> 					<td>200</td>
> 					<td class="timeCls">200</td>
> 				</tr>
> 			</c:otherwise>
> 		</c:choose>
> 	</c:forEach>
> </table>
> ```

