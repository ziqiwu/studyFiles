### 不记文档，白忙一场

------

#### 0、简介

> #### 前言
>
> ```python
> 	inux'编译安装'中configure、make和make install各自的作用
> 	
>     ./configure是用来'检测你的安装平台'的目标特征的。比如它会检测你是不是有CC或GCC，并不是需要CC或	GCC，它是个shell脚本。这一步一般用来生成 Makefile，为下一步的编译做准备。
> 	
>     make是用来'编译'的，它从Makefile中读取指令，然后编译。
> 	
>     make install是用来'安装'的，它也从Makefile中读取指令，安装到指定的位置。
> 	
>     AUTOMAKE和AUTOCONF是非常有用的用来发布C程序的东西。
> ```
>
> #### 1、configure
>
> ```python
> 	这一步一般用来生成 Makefile，为下一步的编译做准备，你可以通过在 configure 后加上参数来对安装进行控制，比如代码:./configure --prefix=/usr
> 	
>     上面的意思是将该软件安装在 /usr 下面，执行文件就会安装在 /usr/bin （而不是默认的 /usr/local/
> bin)，资源文件就会安装在 /usr/share（而不是默认的/usr/local/share）。同时一些软件的配置文件你可以通过指定 --sys-config= 参数进行设定。有一些软件还可以加上 --with、--enable、--without、--disable 等等参数对编译加以控制，你可以通过允许 ./configure --help 察看详细的说明帮助。
> ```
>
> #### 2、make
>
> ```python
> 	这一步就是编译，大多数的源代码包都经过这一步进行编译（当然有些perl或Python编写的软件需要调用perl或python来进行编译）。
> 	
>     如果 在 make 过程中出现 error ，你就要记下错误代码（注意不仅仅是最后一行），然后你可以向开发者提交 bugreport（一般在 INSTALL 里有提交地址），或者你的系统少了一些依赖库等，这些需要自己仔细研究错误代码。
> 	
>     make 的作用是开始进行源代码编译，以及一些功能的提供，这些功能由他的 Makefile 设置文件提供相关的功能，比如 make install 一般表示进行安装，make uninstall 是卸载，不加参数就是默认的进行源代码编译。
> 
>     make 是 Linux 开发套件里面自动化编译的一个控制程序，他通过借助 Makefile 里面编写的编译规范进行自动化的调用 gcc 、ld 以及运行某些需要的程序进行编译的程序。一般情况下，他所使用的 Makefile 控制代码，由 configure 这个设置脚本根据给定的参数和系统环境生成。
> ```
>
> #### 3、make install
>
> ```python
> 	这条命令来进行安装（当然有些软件需要先运行 make check 或 make test来进行一些测试），这一步一般需要你有 root 权限（因为要向系统写入文件）
> 
>     linux编译安装中configure、make和make install各自的作用
> ```
>





