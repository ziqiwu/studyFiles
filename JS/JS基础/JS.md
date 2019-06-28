### 不记文档，白忙一场

------

#### 页面查询/导出/提交

> ```python
> 1、面临问题：比如页面选择框有开始时间、结束时间、选择类型等，点击查询按钮后，页面显示检索条件后的数据表-     格，这时候，随便选了选择框，但是没有点击查询按钮 --> 这时候点击导出按钮 --> 从页面选择框拿值作为参
>     数得到的数据，就是错误的
>   以前的解决方法：写很多的隐藏域，只有在点击了查询按钮之后，才把选择框内的值放在隐藏域中，点击导出的时	候，是去隐藏域拿值，而不是页面选择框拿值
>   更好的办法：去掉选择按钮，在选择框数值一旦改变的时候 ，就自动触发查询，这个时候，导出也完全可以从页面拿         值。即使是有本年、本月的按钮，也可以在点击后，从css等方面，加状态。导出的时候，获取状态拿值，而		不需要写入隐藏域中
> ```
>

#### radio触发事件

> #### 来源
>
> ```python
> http://www.cnblogs.com/rose1324/p/8513650.html
> ```
>
> #### 示例
>
> ```python
> <label>第一个</label>
> <input name="radio1" type="radio" id="input1">
> <label>第二个</label>
> <input name="radio1" type="radio" id="input2">
> 
> <script>
>     $("#input1").attr("checked","checked");//默认第一个选中
>     #注意：下拉选的选中为：$("#echartsOpt").attr("selected","selected")
>     $('input:radio[name="radio1"]').change(function () {
>         if($("#input1").is(":checked")){
>             alert("选中第一个！")
>         }
>         if($("#input2").is(":checked")){
>             alert("选中第二个！")
>         }
>         #注意JS中选择器is函数的用法
>     })
> </script>
> 或者JS为:
> <script>
> 	var showTypeValue = $('input:radio[name="radio1"]:checked').val();
>     viewModeChoose(showTypeValue);  #自定义的函数
> </script>
> ```
>

#### 父页面子页面交互

> ```python
> 
> ```
>

#### JSP中JS获取URL参数值

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
>

