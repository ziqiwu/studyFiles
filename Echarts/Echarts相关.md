### 不记文档，白忙一场

------

#### 纵轴坐标自适应

> ```python
> 按照官网说法，不设置max,min值即可自动设置刻度值
> 示例：
>     yAxis: [
>         {
>             name: '存量(t)',
>             type: 'value',
>             //max: 10000
>         }
>     ],
> 	注释掉max:10000即可自适应
> 	注：这儿只有一个纵轴，多条折线
> ```

#### 多条折线默认只选中一条

> ```python
> legend中增加selected属性，需要把每条折线是否默认显示都定义出来。
> 如果添加了selectedMode:'sigle'则每次都只能显示一条，切换一条则上一条会消失。
> 示例：
>     legend: {
>         x: 'left',
>         data: ['油库库存','G1#罐存量','G2#罐存量','G3#罐存量','G4#罐存量','G5#罐存量','G6#罐存				量','G11#罐存量','G12#罐存量','G13#罐存量','G14#罐存量','G15#罐存量','G16#罐存			 量'],
>         inactiveColor: '#999',
>         //selectedMode: 'single',
>         selected: {
>             '油库库存': true,
>             'G1#罐存量':false,
>             'G2#罐存量':false,
>             'G3#罐存量':false,
>             'G4#罐存量':false,
>             'G5#罐存量':false,
>             'G6#罐存量':false,
>             'G11#罐存量':false,
>             'G12#罐存量':false,
>             'G13#罐存量':false,
>             'G14#罐存量':false,
>             'G15#罐存量':false,
>             'G16#罐存量':false,
>         },
>         orient: 'vertical',
>         width: 150,
>         top: 50,
>         borderWidth: 1,
>         borderColor: 'blue',
>         textStyle: {
>             color: '#000'
>         },
>     },
> ```

#### 定义横轴纵轴的位置

> ```python
> 测试一下就能看到效果
> 示例：
>     grid: {
>         bottom: 80,
>         left:160,
>     },
> ```

#### 示例纵向排布

> ```python
> 增加orient: 'vertical',
> 示例：    
>     legend: {
>         x: 'left',
>         data: ['油库库存','G1#罐存量','G2#罐存量','G3#罐存量','G4#罐存量','G5#罐存量','G6#罐存			量','G11#罐存量','G12#罐存量','G13#罐存量','G14#罐存量','G15#罐存量','G16#罐存量'],
>     	inactiveColor: '#999',
>     	//selectedMode: 'single',
>     	selected: {
>             '油库库存': true,
>             'G1#罐存量':false,
>             'G2#罐存量':false,
>             'G3#罐存量':false,
>             'G4#罐存量':false,
>             'G5#罐存量':false,
>             'G6#罐存量':false,
>             'G11#罐存量':false,
>             'G12#罐存量':false,
>             'G13#罐存量':false,
>             'G14#罐存量':false,
>             'G15#罐存量':false,
>             'G16#罐存量':false,
>         },
>     	orient: 'vertical',
>     	width: 150,
>     	top: 50,
>     	borderWidth: 1,
>     	borderColor: 'blue',
>     	textStyle: {
>     		color: '#000'
>     	},
>     },
> ```

#### 显示多条折线图

> ```python
> 第一步：
> 	legend: {
>         x: 'left',
>         data: ['油库库存','G1#罐存量','G2#罐存量','G3#罐存量','G4#罐存量','G5#罐存量','G6#罐存			量','G11#罐存量','G12#罐存量','G13#罐存量','G14#罐存量','G15#罐存量','G16#罐存量'],
>     }
> 第二步：
> 	在series中要增加几条曲线，就增加几个大括号。
> 	series中放的是真实的每条曲线的相关数据，其中一个大括号里面的就是一条曲线图。
> ```

#### 折线变为光滑曲线

> ```python
> series中放的是真实的每条曲线的相关数据，其中一个大括号里面的就是一条曲线图。
> 在该调曲线相关数据的大括号中，增加smooth:true属性，即可变为光滑曲线。
> 如果想增加动画效果，即折线动画出现，则增加animation:true
> 示例：
>     series: [
>         {
>             name:'实时库存',
>             type:'line',
>             animation: false,
>             smooth:true,
>             areaStyle: {
>             },
>             lineStyle: {
>                 width: 1
>             },
>             markArea: {
>                 silent: true,
>                 data: [[{
>                     xAxis: '2009/9/12\n7:00'
>                 }, {
>                     xAxis: '2009/9/22\n7:00'
>                 }]]
>             },
>             data:[ ...]
>         }
>     ]
> ```

