### 不记文档，白忙一场

------

#### 双纵坐标

```python
第一步：示例(折线图)：
	waveOption = {
		grid : {
	        top : 40,    //距离容器上边界40像素
	        bottom: 80   //距离容器下边界30像素
	    },
		legend: {
			data:['销售量','加油架次'],
		},
	    xAxis: {
	        type: 'category',
	        data: timeArr,
            axisLabel: {  
			   interval:0,  
			   rotate:40  
			}
	    },
	    yAxis: [{
				name: '销售量',
	        	type: 'value',
				position: 'left',
				axisLabel: {
					formatter: '{value} (万吨)'
				}
	    	},
			{
				name: '加油架次',
				type: 'value',
				position: 'right',
				axisLabel: {
					formatter: '{value} (万架)'
				}
			}
		],
	    series: [{
				name: '销售量',
	        	data: yAxisArrSales,
				tooltip: {
					trigger: 'axis'
				},
	        	type: 'line',
	        	smooth: true
	    	},
			{
				name: '加油架次',
				data: yAxisArrSorties,
				tooltip: {
					trigger: 'axis'
				},
				type: 'line',
				yAxisIndex: 1,
				smooth: true
			}
	    ]
	};
	waveChart = echarts.init($("#echartsDiv").get(0));
	waveChart.setOption(waveOption);
	waveChart.resize();
第二步：必不可少
	1、legend --> 两个纵坐标的图例
    2、yAxis --> 两个纵坐标的样式
    3、series --> 两个纵坐标的数据
第三步：报错
	1、两条折线，把左边的图例点关掉，另一条折线不再以右边纵坐标为准，开始以左边为准了
    	解决 --> 在series的另一条折线中加yAxisIndex: 1
```



