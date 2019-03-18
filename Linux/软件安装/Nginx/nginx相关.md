### 不记文档，白忙一场

------

#### 安装

> ```python
> 【注1】安装c++编译环境yum install -y gcc gcc-c++
> 	检查是否安装：rpm -qa | grep gcc*
> 【注2】执行./configure命令的时候，提示需要perl5。
> 	https://blog.csdn.net/wtwshui/article/details/79415799
> 第一步：下载所有的tar包
> 	(1)nginx-1.12.0.tar.gz
> 		http://nginx.org/en/download.html
> 	(2)pcre-8.32.tar.gz
> 		http://www.pcre.org/
> 	(3)openssl-fips-2.0.16.tar.gz
> 		http://www.openssl.org/
> 	(4)zlib-1.2.11.tar.gz
> 		http://www.zlib.net/
> 	【注】nginx的模块依赖库是：pcre库、openssl库、zlib库
> 	【注】或者用第二种方法，直接用yum命令安装
> 		yum install pcre*
> 		yum install openssl*
> 		yum install zlib*
> 第二步：安装
> 	上面4个tar包安装流程都是一样的
> 	解压：tar -zxvf openssl-fips-2.0.16.tar.gz
> 	配置：./configure
> 	编译：make	
> 	安装：make install
> 	【注】4个模块安装顺序是openssl、pcre、zlib、nginx
> 第三步：开放80端口
> 	vi /etc/sysconfig/iptables
> 	增加一行
> 	-A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT
> 第四步：测试
> 	直接在浏览器地址栏输入：ip地址，端口默认是80，不需要写
> 	成功则出现nginx欢迎页面
> ```

