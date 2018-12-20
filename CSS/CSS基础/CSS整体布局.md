### 不记文档，白忙一场

------

#### div之间相互遮挡

```python
第一步：示例
<div class="total">
    <%-- 左侧总体 --%>
    <div style="width:20%;float:left;margin-top:10px;"></div>

    <%--右侧总体--%>
    <div style="border: 1px solid #ddd;width: 78%;float: right;margin-top:1vh;">
        <%--标题--%>
        <div class="panel-header" style="border-right: none;border-left: none;"></div>
        <%--选择框--%>
        <div style="margin-top: 10px;margin-left: 33px;"></div>
        <%--表格--%>
        <div style="margin-top:1vh;" id="tblDiv"></div>
        <%--趋势图--%>
        <div style="margin-top:1vh;" id="echartsDiv"></div>
    </div>
</div>
```

```python
第二步：问题
	有的按钮被遮住了，只能点一半。有的因为宽度被挤，浮动到了其他地方
```

```python
第三步：解决
	1、最外层class="total"的div包含两个div，分别是左侧总体和右侧总体的div。在width样式属性上，分别是
		20%和80%，保证它们在100%左右，因为div自带外边距。
	2、如果div是上下关系，则要保证每个div要有margin-top="1vh"的设置，保证和上一个div之间有间隔
	3、如果div是左右关系，则要保证每个div要有float:"left"或者float:"right"的设置，保证和相邻的div浮动		  分开
	4、如果想要有div外面的浅色框，使页面看起来更层次分明，则设置border:1px solid #ddd。使div显现出来
```

```python
第一步：示例
	<div style="border: 1px solid #ddd;width:100%;height:70vh;margin-top:1vh;" id="echartsDiv" 		id="echartsDiv"></div>
```

```python
第二步：问题
	echarts显示不出来，F12看到div高度是0
```

```python
第三步：解决
	div不给高度的话，是position的，必须给高度
```











