### 不记文档，白忙一场

------

#### 简介

> ```python
> 1、导入url:https://blog.csdn.net/sinat_32133675/article/details/78019092
> 2、不同excel版本，导致问题：https://blog.csdn.net/it_wangxiangpan/article/details/42778167
> ```

#### 报错

> ```python
> 1、Cannot get a text value from a numeric cell
> 	解决：
> 	POI操作Excel时偶尔会出现Cannot get a text value from a numeric cell的异常错误。
> 
> 	异常原因：Excel数据Cell有不同的类型，当我们试图从一个数字类型的Cell读取出一个字符串并写入数据	 库时，就会出现Cannot get a text value from a numeric cell的异常错误。
> 
> 	此异常常见于类似如下代码中：row.getCell(0).getStringCellValue()；
> 
> 	解决办法：先设置Cell的类型，然后就可以把纯数字作为String类型读进来了：
> 
> 	if(row.getCell(0)!=null){
>           row.getCell(0).setCellType(Cell.CELL_TYPE_STRING);
>           stuUser.setPhone(row.getCell(0).getStringCellValue());
> 	}
> 	来源：https://blog.csdn.net/ysughw/article/details/9288307
> 2、导入数字时,在获取cell时精度丢失问题
> 	问题如下：
> 		导入的excel表格中数据为数字时，excel中值为23.4，java中获取到为23.399999943
> 	解决如下：
> 		import java.text.NumberFormat;
> 		private static NumberFormat numberFormat = NumberFormat.getInstance();
> 		static {
> 			numberFormat.setGroupingUsed(false);
> 		}
> 		if (cell.getCellType() == Cell.CELL_TYPE_NUMERIC) {
> 			value = numberFormat.format(cell.getNumericCellValue());
> 		}else{
> 			cell.setCellType(Cell.CELL_TYPE_STRING);
> 			String value = cell.getStringCellValue();
> 		}
> 	来源如下：
> 		https://blog.csdn.net/qq_34531925/article/details/76735345
> ```
>

#### API

> ```python
> 1、CellRangeAddress（int firstRow, int lastRow, int firstCol, int lastCol）
> 	在用poi在EXECL报表设计的时候，遇到单元格合并问题，用到一个重要的函数：
>     参数：起始行号，终止行号， 起始列号，终止列号
> ```

#### 导出实战

> ```python
> https://blog.csdn.net/fight_man8866/article/details/82189446
> ```

#### 导入实战

> ```python
> https://blog.csdn.net/sinat_32133675/article/details/78019092
> ```

```
//@ sourceMappingURL=jquery-2.0.3.min.map
```

