### 不记文档，白忙一场

------

#### 报错

> (1) eclipse修改代码后，Tomcat没有变化
>
> ```python
> 步骤：先把Tomcat停掉，然后选Eclipse导航栏的Project --> Clean，clean会删除项目WebRoot下的classes文件，然后自动重新编译再生成class文件。
> 注意：我的情况，clean出问题这个项目没有作用，clean all之后变好了。而且我的没有变化的不是class文件，而是配置文件.properties
> ```

