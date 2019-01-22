### 不记文档，白忙一场

------

#### new一个package

> ```python
> 弹框出来是：
> 	Source folder --> cnafSelfControl/src
> 	Name --> selfControl.hbase
> 现在需求是心在hbase包下新建一个hbaseInter包：
> 	直接把Name后面的值改为selfControl.hbase.hbaseInter，即直接加了一个.hbaseInter
> ```

#### 只有src，没有src/main/java

> ```python
> 方法一：点击src包下面的package，右键build path --> Use As Source Folder即可
> 注意：比如在src下创建了main，在main下又分别创建了java和resource包，则应该在最里面的java和resource包上右键build path
> 
> 方法二：直接在项目上右键，new --> source folder --> src/main/java
> ```

