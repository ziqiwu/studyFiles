### 不记文档，白忙一场

#### 1、问题

> ```python
> 1> tomcat8安装到aliyun上，启动./startup，然后访问xiaoguozi.com.cn:8080，显示网络不可达
>     分析：aliyun的安全组端口肯定开放了。那就可能是防火墙的端口没有开放
> 	解决：systemctl stop firewalld，关闭防火墙，访问tom猫出来了。
> 		firewall-cmd --add-port=8080/tcp --permanent
> 		firewall-cmd --reload
> 		开放了端口，启动防火墙访问，SUCCESS
> ```