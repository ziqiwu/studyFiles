### 不记文档，白忙一场

------

#### 单选框radio

```python
一、实现点击redio后面文字选中redio
	方法1：<input type="radio" id="clickIn"/> <label for="clickIn">点击我选中</label>
    	解释：input标签设置ID，文字添加一个lable标签，设置一个for属性值与ID值相同即可。
	方法2：<label >
                <input type="radio" name="clickIn"  value="clickIn" />点击我选中
            </label>    
        解释：input设置name和value值相同即可。
     方法3：<label>
                <input type="radio" name="refund" value="refund_goods"/> 退货退款
            <label>
            <label>
                <input type="radio" name="refund" value="refund"/> 仅退款
            </label>
		解释：两个redio的name值都设置一个的即可，N个redio实现方式一样。
二、radio和汉字对齐
	字体样式设置为：font-size:12px;
	radio样式设置为：vertical-align:middle; margin-top:-2px; margin-bottom:1px;
```

#### 单位

```python
vh：是view height，代表整个屏幕分为100份，其中的几份
vw：是view width，代表整个屏幕分为100份，其中的几份
%：是占他的父div百分之多少
```

#### 浮动

```python
示例:
<div id="divTop" style="width=100%;border:1px solid #dddd;">
	<div id="divLeft" style="width=40%;height=40%;border:1px solid #ddd"></div>
	<div id="divRight" style="width=40%;height=40%;border:1px solid #ddd"></div>
</div>
divLeft肯定是左浮动 --> float:left
divRight如果是右浮动，则两个div中间有空隙；如果左浮动，则两个div的最右边有空隙
```

#### 隐藏

```python
display:none、visibility:hidden和opacity:0之间的区别
https://blog.csdn.net/github_39673115/article/details/77926351
```





