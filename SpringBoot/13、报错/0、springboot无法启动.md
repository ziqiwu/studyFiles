### 不记文档，白忙一场

------

#### 0、无任何报错

> #### 0、因application.yml取值导致
>
> ```python
> 0> console输出：
> 	2019-04-23 16:48:22.538 --> INFO  CnafSelfControlApplication - Starting 				CnafSelfControlApplication on R9LOMLJ7ILIFB69 with PID 13136 (H:\desktop\springboot-	applications\cnafSelfControl\target\classes started by 起鹜 in H:\desktop\springboot-		applications\cnafSelfControl)
> 	2019-04-23 16:48:22.543 --> INFO  CnafSelfControlApplication - The following profiles 	  are active: dev
> 	2019-04-23 16:48:22.677 --> INFO  AnnotationConfigApplicationContext - Refreshing 		org.springframework.context.annotation.AnnotationConfigApplicationContext@26132588: 	startup date [Tue Apr 23 16:48:22 CST 2019]; root of context hierarchy
> 
> 	Process finished with exit code 1
>     
> 1> 问题代码
> 	@Component
> 	@PropertySource({"classpath:resources/application.yml"})
> 	public class OpcConnect {
>     	private static final Logger opcConnectLogger = 											LoggerFactory.getLogger(OpcConnect.class);
>     	@Value("${opc.server.uri}")
>     	private static String opcUriStr;
>         /**
>          * 测试某个opc路径是否可以连接成功
>          * @param opcUri
>          * @return
>          */
>         public static int checkOpcConnect(String opcUri){
>             int flag = 0;
>             try {//--将SampleConsoleClient类中的client对象是静态的，属于整个类的
>                 SampleConsoleClient.initialize(new String[]{},opcUri);  //先初始化OPC链接
>                 SampleConsoleClient.connect1();  //链接OPC
>             } catch (Exception e) {
>                 System.out.println("-----------OPC连接失败："+opcUri);
>                 flag = 1;
>             }
>             return flag;
>         }
>     }
> 2> 问题解决：
> 	配置：@PropertySource({"classpath:resources/application.yml"})去掉resources正常
> 		即@PropertySource({"classpath:application.yml"})
> 
> 注* 版本springboot v1.5.20.RELEASE
> ```

