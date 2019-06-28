### 不记文档，白忙一场

------

#### 0、thymeleaf模板不能找到

> #### 简介
>
> ```python
> 我的controller路径是：
> 	http://localhost:8888/api/v1/activemq/common?username=guozi&msg=11111
> 描述：
> 	虽然是api开头的，但是我加了参数username=guozi
> 备注：
> 	因为有过滤器，以api开头的路径，都会过滤，过滤条件就是username=guozi
> 解决：
> 	是因为我Controller类上加的注解是@Component，而不是@Controller，更不是@RestController。
> 	因为不是返回json数据，所以controller去找模板，返回html了。
> 教训：
> 	以后，dao层的就加@Repository，service的就加@Service，Controller的就加@Controller。
> 	不要都是@Component，容易混乱。
> ```

