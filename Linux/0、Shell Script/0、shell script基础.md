### 不记文档，白忙一场

------

#### 0、常见解释器

> ```python
> 解释器：
> 	是一种'命令解释器'
> 	主要作用是对命令进行运行和解释，将需要执行的操作传递给'操作系统'的'内核'并执行。
> 1> #!/bin/bash (默认)
> 2> #!/bin/ksh
> 3> #!/bin/bsh
> 4> #!/bin/sh
> 注* shell脚本一定要有解释器吗？但是不一定。
> 	测试，将#!/bin/bash删除，执行.sh文件，也可以执行
> 注* SecureCRT --> 选项 --> 会话选项 --> 字符编码 --> 选择UTF-8
> ```

#### 1、权限

> ```python
> 1> 文件和目录权限
> 	文件权限：-rw-r--r--
> 	目录权限：drw-r--r--
> 	注* 每三个一列，分别是所有者（owner），所属组（group），其他（other）
> 		rwx：分别表示可读、可写、可执行。用数字表示为 r:4 w:2 x:1
> 		755：表示所有者权限为7，所属组为5，其他为5。eg.如果权限为7就是rwx，即全部权限都有
> 2> 举例.sh文件没有x可执行权限，用sh命令运行
> 	-rw-r--r-- root root helloworld.sh
> 	执行sh helloworld.sh也可以执行，虽然三个分组都没有执行权限
> 	因为sh是一个命令，会去读取文件内容。而sh这个命令是有执行权限的就可以。
> ```

#### 2、执行shell脚本

> ```python
> 方法1：
> 	1> 赋予执行权限 chmod 744 helloworld.sh
> 	2> 执行./helloworld.sh
> 方法2：
> 	sh helloworld.sh或者bash helloworld.sh
> 方法3：
> 	source helloworld.sh
> ```

#### 3、常见变量

> #### 什么是变量
>
> ```python
> 1> 介绍
>     a=12
>     echo $a
>     输出12，所以a就是自己定义的变量
> 2> ${}的应用
> 	a=b
> 	echo $a #输出b
> 	echo ${a} #输出b
> 	echo $aook #输出空，没有aook这个变量
> 	echo ${a}ook #输出book
> 注* 等号两边一定不能有空格
> ```
>
> #### 常见变量
>
> ```python
> 1> $?
> 	上一次命令是否执行成功：0成功，1失败
> 	随便乱写一个命令：ls，会报错Error，然后执行echo $?，输出的是1
> 	注* 可写为${?}
> 2> $0 $1-$9 $# $*
> 	1、写一个脚本，名称为test.sh
>         #!/bin/bash
>         #by guozi 2019/5/14
>         #测试常见变量
>         echo "文件名称为：$0"
>         echo "第一个参数：$1"
>         echo "第二个参数：$2"
>         echo "一共传入参数的个数：$#"
>         echo "列举所有参数：$*"
> 	2、执行脚本，sh test.sh 12 ABc 123 sun，输出为：
>         文件名称为：test.sh
>         第一个参数：12
>         第二个参数：ABc
>         一共传入参数的个数：4
>         列举所有参数：12 ABc 123 sun
> ```

#### 4、常见符号

> ```python
> 1> > #会覆盖原有的内容
> 	cat >test.sh --> enter --> 输入"第一行内容" --> ctrl + c结束输入
> 	cat >test.sh会发现之前的内容都没有了，只有一行"第一行内容"
> 	如果一行一行增加，则使用：
> 	cat > test1.txt <<EOF
> 	解释来源：https://www.cnblogs.com/zhongjianlong/archive/2013/09/17/linux.html
> 2> >> #追加。不会覆盖原有的内容
> 	cat >>test.sh
> 3> ; #执行多条命令
> 	cat test.sh ; ls
> 	则前后两条命令都会执行，结果都会输出到控制台
> 4> | #管道符
> 5> && #前面的命令执行成功，后面的命令才可以执行
> 	cat test.sh && ls
> 	cat test1.sh && ls  #前面的执行不成功
> 6> || #前面的命令执行成功，则不再执行后面的命令
> 	cat test.sh || ls
> 	cat test1.sh || ls
> 7> "" #会输出变量值	
> 	写一个简单脚本，para.sh：
> 		#!/bin/bash
> 		#by guozi 2019/5/14
> 		echo "第一个参数是：$1"
> 		echo '第一个参数是：$1'
> 	执行sh para.sh abc 123
> 	输出：
> 		第一个参数是：abc
> 		第一个参数是：$1
> 8> '' #输出字符串本身
> 	例子见7>
> 9> `` 或者 $() #输出命令结果
> 	a=`date` 或者 a=$(date)
> 	echo $a
> 10> /dev/null
> 	理解：
> 		垃圾桶，无底洞
> 	分类：
> 		1>/dev/null #正确输出到无底洞
> 		2>/dev/null #错误输出到无底洞
> 	举例：
> 		cat test1.sh  #报错：cat: test1.sh: No such file or directory
> 		cat test1.sh 2>/dev/null #什么都不输出
> 		cat test.sh #输出文件中内容
> 		cat test.sh 1>/dev/null #什么都不输出
> ```

#### 5、运算符

> #### 运算符
>
> ```python
> 1> 整数：
> 	1、加：
> 		方法1：expr 1 + 2  注* 加号两边必须要有空格
> 		方法2：echo $((1+2))
> 		方法3：echo $[1+2]
> 	2、减
> 		方法1：expr 1 - 2
> 		其余同加
> 	3、乘
> 		方法1：expr 1 \* 2    注* 乘必须转义字符，转一下\*，否则的话，*代表的是通配符
> 		其余同加
> 	4、除
> 		方法1：expr 1 / 2
> 		其余同加
> 	5、取余
> 		方法1：expr 1 % 2
> 		其余同加
> 	注* 对于整数的'变量'运算
> 		a=12;b=6;expr $a + $b
> 		a=12;b=6;echo $((a + b))
> 		a=12;b=6;echo $[a + b]
> 2> 小数
> 	方法1：命令输入bc，进入linux自带的计算器交互界面，进行计算
> 	方法2：使用管道符
> 		echo "1.264+3.456" | bc
> 3> 小数的精度
> 	echo "scale=2;1.264+3.456" | bc #scale对于加号是没有作用的，只对乘除取余
> 	所以转换一下
> 	echo "scale=2;(1.264+3.456)/1" | bc
> 	注* bc运算scale=2;0.2+0.3结果是.50，小数点之前的0不显示
> ```
>
> #### 注意记录
>
> ```python
> 1> expr命令
> 	注* expr 1 + 2 运算符两边必须要有空格
> 2> 乘必须转义字符，转一下\*
> 	否则的话，*代表的是通配符
> 3> a=12;b=6;expr $a + $b 注意分号的作用，就是可以执行多条命令
> 	a=12;b=6;echo $(a+b)
> 4> 小数的运算，使用linux自带的bc计算器
> 	方法1：输入命令bc，直接在界面进行交互处理
> 	方法2：列出表达式，使用管道符传递给bc计算器
> 5> 小数的运算，保留几位小数
> 	echo "scale=2;1.264+3.456" | bc
> 	注* scale对于加号是没有作用的echo "scale=2;(1.264+3.456)/1" | bc
> 6> bc运算scale=2;0.2+0.3结果是.50，小数点之前的0不显示
>     
> ```

#### 6、常见的条件判断

> #### 常见的***条件判断***
>
> ```python
> 1> 表达式
> 	格式：[ 表达式 ]
> 	注意：表达式两边必须要有空格
> 2> 文件（夹）或路径
> 	-e #目标是否存在（exist）
> 		eg1:[ -e test.sh ] && echo "存在"  #输出存在
> 		eg2:[ -e test1.sh ] || echo "不存在"  #输出不存在
> 	-d #是否为路径（directory）
> 		mkdir guozi
> 		eg1:[ -d guozi ] && echo "是"   #输出是
> 		eg2:[ -d test.sh ] || echo "不是"   #输出不是
> 	-f #是否为文件（file）
> 		eg:[ -f test.sh ] && echo "是"   #输出是
> 3> 权限
> 	-r #是否有读取权限（read）
> 	-w #是否有写权限（write）
> 	-e #是否有执行取权限（execute）
> 	eg:[ -r test.sh ] && echo "有可读权限"
> 4> 比较
> 	整数
> 		1、-eq 等于
> 		2、-ne 不等于
> 		3、-gt 大于
> 		4、-lt 小于
> 		5、-ge 大于等于
> 		6、-le 小于等于
> 	小数
> 		注* 小数的比较，必须用到bc计算器
> 		因为：
> 			bc命令
> 			执行输入4>5
> 			成立返回1，不成立返回0
> 		所以：
> 			[ $(echo '1.4>1.3' | bc) -eq 1 ] && echo "成立"
> 			注* echo $(echo "1>2" | bc)是输出`$(echo "1>2" | bc)`的执行结果
> 5> 字符串
> 	1、= 等于
> 		[ 'kkkk' = 'kkkk' ] && echo "等于"
> 	2、!= 不等于
> 		[ 'kkkk' = 'aaaa' ] || echo "不等于"
> ```
>
> #### 注意记录
>
> ```python
> 1> [ 表达式 ]
> 	注意： 表达式两边必须要有空格
> 	[ -e test.sh ] && echo "存在"
> 	[ -e test1.sh ] && touch test1.sh
> 2> -d是判断路径
> 	[ -d /user/local/nginx ]
> 3> 是否有权限
> 	[ -x test.sh ] && echo "有执行权限"
> 4> 整数的比较
> 	[ 9 -eq 9 ] && echo "相等"
> 	注* 列举的判断（-eq/-ne/-lt/-gt/-ge/-le等）都必须是应用于整数值的表达式
> 5> 小数的比较
> 	注* 也还是需要使用到bc计算器
> 	bc命令
> 	执行输入4>5
> 	成立返回1，不成立返回0
> 	所以：[ $(echo '1.4>1.3' | bc) -eq 1 ] && echo "成立"
> ```
>
> #### 小脚本
>
> ```python
> 1>判断输入的两个数的是否相等
> 	写脚本
>         #!/bin/bash
>         #判断输入的两个数的是否相等
>         #by guozi 2019/5/14
>         if [ $1 -eq $2 ]
>         then
>         echo "$1等于$2"
>         else
>         echo "$1不等于$2"
>         fi
> 	执行脚本
> 		cat > compare.sh --> enter --> ctrl + v  #注意会自动创建compare.sh文件
> 		sh compare.sh 12 43
> 		输出：12不等于43
> 2> 以输入的名称创建文件
> 	#!/bin/bash
> 	#以输入的名称创建文件
> 	#by guozi 2019/5/14
> 	touch $1
> 	if [ $? -eq 0 ];then
> 	echo "$1创建成功"
> 	fi
> 	注* ";"使用来执行多条命令
> ```

#### 7、shell脚本的输入

> #### shell脚本输入之read命令
>
> ```python
> 1> 语法：
> 	read -参数
> 2> 参数：
> 	-p: 给出提示符，默认不支持"\n"换行
> 	-s: 隐藏输入的内容
> 	-t: 给出等待的时间，超时会退出read
> 	-n: 限制读取字符的个数，超出个数会自动执行脚本
> 	注* 这只是最基本的一部分，用man read命令了解更多参数
> 	注* 其余参数一定要加在-p参数的前面，即-p参数是写在最后面的
> 3> 示例：
> 	写脚本：
>         #!/bin/bash
>         #测试脚本的输入
>         #by guozi 2019/5/15
>         read -s -t 10 -n 6 -p "请您输入密码：" password
>         echo "您输入的密码为：$password"
> 	脚本解释：
> 		-s隐藏输入，-t 10是10s不输入自动退出，-n是最多输入6个字符，-p是把输入的内容赋值为password		变量
> 	执行脚本：
>         vi readtest.sh --> ctrl + v将脚本粘进入  #注意会自动创建readtest.sh文件
>         sh readtest.sh
> 	效果为：
>         请您输入密码：您输入的密码为：123  
>         注* 因为-p默认不支持"\n"换行，所以可以手动加一行，如下：
> 	加入换行
>         read -s -t 10 -n 6 -p "请您输入密码：" password
>         echo -e "\n"
>         echo "您输入的密码为：$password"
> 	效果为：
>         请您输入密码：
>         您输入的密码为：123424
> ```
>
> #### 注意记录
>
> ```python
> 1> vi 123.sh  注* 会自动创建123.sh文件并启动编辑模式
> 2> -n如果是5，则输入第6个字符的时候，就会自动执行脚本，并没有按回车
> 3> 输入的内容，会自动赋值给password变量
> 4> 注* 其余参数一定要加在-p参数的前面，即-p参数是写在最后面的
> ```

#### 8、shell脚本的输出

> #### 脚本输出
>
> ```python
> 语法：echo -e "\033[字背景颜色;字体颜色;特效m字符串\033[0m"
> 	注* 
> 		"\033["和"\033[0m"是开启属性和关闭属性的固定格式；
> 		m是属性和字符串之间的分隔，固定格式；
> 		-e是激活echo对特殊脚本的解析；
> 		不同属性用分号分隔。
> 	注* 
> 		1 开启属性是"\033["，记得"["，不是"\033"
> 		2 "\033["和后面的字符串之间，不能有空格。因为你看结束属性"\033[0m"在[和0之间也没有空格。
> #字背景颜色范围： 40-47
> 	echo -e "\033[40;37m 黑底白字 \033[0m"
> 	echo -e "\033[41;37m 红底白字 \033[0m"
> 	echo -e "\033[42;37m 绿底白字 \033[0m"
> 	echo -e "\033[43;37m 黄底白字 \033[0m"
> 	echo -e "\033[44;37m 蓝底白字 \033[0m"
> 	echo -e "\033[45;37m 紫底白字 \033[0m"
> 	echo -e "\033[46;37m 天蓝底白字 \033[0m"
> 	echo -e "\033[47;37m 白底白字 \033[0m"
>         
> #字体色范围：30-37
> 	echo -e "\033[30m 黑色字体 \033[0m"
> 	echo -e "\033[31m 红色字体 \033[0m"
> 	echo -e "\033[32m 绿色字体 \033[0m"
> 	echo -e "\033[33m 黄色字体 \033[0m"
> 	echo -e "\033[34m 蓝色字体 \033[0m"
> 	echo -e "\033[35m 紫色字体 \033[0m"
> 	echo -e "\033[36m 天蓝字体 \033[0m"
> 	echo -e "\033[37m 白色字体 \033[0m"
> 
> #特效范围：
> 	echo -e "\033[0m 无任何特效 \033[0m"
> 	echo -e "\033[1m 高亮度 \033[0m"
> 	echo -e "\033[4m 下划线 \033[0m"
> 	echo -e "\033[5m 闪烁 \033[0m"
>     
> 示例：
> 	改上一个脚本输入的文件
>         #!/bin/bash
>         #输出属性测试
>         #by guozi 2019/5/15
>         read -s -t 10 -n 6 -p "$(echo -e "\033[41;37;5m 请您输入密码：\033[0m")" password
>         echo "您输入的密码为：$password"
> 	注* $(echo -e "\033[41;37;5m 请您输入密码：\033[0m")的两边，一定要加双引号，否则语法报错
> 		认为没有结束，之后的所有命令都是加了闪烁红底
> 	注* 当然特效还可以接着往后加，比如41;37;5;1;4m，就会再增加下划线和高亮两个特性
> 	注* shell中可以在双引号中嵌套使用双引号
> ```
>
> #### 注意记录
>
> ```python
> 1> -e是'激活'echo对特殊脚本的解析
> 2> 不同属性用分号分割
> 3> \033[是固定格式
> ```

#### 9、处理海量数据之grep

> #### grep使用
>
> ```python
> 简介：对数据进行"行"的提取
> 语法：grep [参数] [内容] [file]
> 使用：grep [参数] [内容] [file] 或者 cat /etc/passwd | grep [参数] [内容]
> 参数：
> 	-v #显示除去匹配成功之外的行。比如-v user则是含有user的行不显示，显示剩下的
> 	-n #对提取的内容进行行号显示
> 	-w #精确匹配
> 	-i #忽略大小写
> 	^ #匹配以什么开头的行
> 	-E #匹配符合正则表达式的行
> 示例：
> 	grep "^user" /etc/passwd   #显示/etc/password文件中以user开头的行
> 	grep -ivn "user" /etc/passwd   #显示忽略大小写匹配到user之外的行
> ```
>
> #### 注意记录
>
> ```python
> 注* grep和sed是处理行，awk是处理列，cut的功能完全可以由awk替代。cut只用于截取字符串。
> 1> ^是放在提取内容的左边，而不是作为一个选项
> ```

#### 10、处理海量数据之sed

> #### sed使用
>
> ```python
> 简介：主要对数据进行处理（新增，替换，删除，搜索）
> 语法：sed [选项] [动作] 文件名
> 参数与选项：
> 	1> 不对源文件修改
> 		注* 下面列举的几个，都是只改输出，不会对原文件造成影响的。
> 		
> 		1、-n #把'匹配'到的行输出打印到屏幕
> 		2、p #以行位单位进行查询，通常与-n一起使用
> 			df -h | sed -n '2p'	
> 			解释：输出df -h结果的第二行
> 		3、d #删除
> 			df -h | sed '2d'
> 			解释：输出df -h中删除了第二行剩下的内容
> 		4、a #在行的下面插入新的内容
> 			df -h | sed '2a 123456789'
> 			解释：输出在df -h中第二行下插入"123456789"字符串之后的内容
> 		5、i #在行的上面插入新的内容
> 			df -h | sed '2i 123456789'
> 			解释：输出在df -h中第二行上方插入"123456789"字符串之后的内容
> 		6、c #替换
> 			df -h | sed '2c 123456789'
> 			解释：输出将df -h中第二行替换为"123456789"字符串之后的内容
> 		7、s/要被取代的内容/新的字符串/g #指定内容进行替换
> 			df -h | sed 's/0%/100%/g'  
> 			或者  
> 			df -h >df.txt
> 			sed 's/0%/100%/g' 
> 	2> 修改源文件
> 		1、-i #对源文件进行修改（高危操作，使用之前必须备份）
> 			sed -i 's/0%/100%/g' df.txt
> 			解释：将df.txt文件中的0%都替换为100%
> 		2、搜索：在文件中搜索内容
> 			sed -n '/100%/p' df.txt
> 			解释：将df.txt文件中含有100%的内容查询出来，对比-p和n结合使用的df -h | sed -n '2p'
> 			注* -n是打印匹配到的内容。可以去掉-n再执行查看结果。
> 		3、-e #表示可以执行多条内容
> 			cat -n df.txt | sed -n -e 's/100%/满分/g' -e '/满分/p'
> 			解释：前后两个动作，都必须要有-e。先将100%都替换为满分，再将匹配到满分的输出打印
> 			注* 命令行解释
> 				-n是打印匹配到的内容，-e是指有多个匹配条件。p是以行位单位匹配
> ```
>
> #### 注意记录
>
> ```python
> 注* grep和sed是处理行，awk是处理列，cut的功能完全可以由awk替代。cut只用于截取字符串。
> 1> df -h | sed "2d"
> 	只是对查询出来的内容进行一部分不显示，而不会对原文件造成影响
> 2> df -h >df.txt
> 	sed "2d" df.txt
> 	同样是不会对原文件造成影响的。只是一部分不会打印到屏幕上。
> 3> 列举的几个，都是只改输出，不会对原文件造成影响的。	
> ```

#### 11、处理海量数据之awk

> #### awk使用
>
> ```python
> 简介：是一门编程语言，支持条件判断，数组，循环等功能，与grep、sed共称为'linux三剑客'。
> 	AWK是一种处理文本文件的语言，是一个强大的文本分析工具。之所以叫AWK是因为其取了三位创始人 		Alfred Aho，Peter Weinberger, 和 Brian Kernighan 的Family Name的首字符。
> 	对数据进行"列"的提取
> 语法：
> 	awk '条件{执行动作}'文件名
> 	awk '条件1 {执行动作} 条件2 {执行动作}...' 文件名
> 	awk [选项] '条件1 {执行动作} 条件2 {执行动作}...' 文件名
> 特殊要点：
> 	1> printf
> 		#格式化输出，不会自动换行
> 		#%ns：字符串型，n代表有多少个字符;
> 		#%ni：整型，n代表输出几个数字；
> 		#%.nf：浮点型，n代表小数点后有多少个小数
> 		注* 如果用两个参数的形式，则第一个参数，即格式，需要加双引号。eg:'{printf "%s\n",$1}'
> 		注* \t 制表符   \n  换行符
> 	2> print
> 		#打印出内容，默认会自动换行
> 示例：
> 	1> df -h | grep /dev/vda1 | awk '{printf "/dev/vda1的使用率是："}{print $5}'
> 		注* 不能写成{printf "/dev/vda1的使用率是：$5"}
> 		特殊字符：
> 			1> $1 #代表第一列
> 			2> $2 #代表第二列
> 			3> $0 #代表一整行
> 	2> （练习）echo "scale=2;0.13+0.1" | bc | awk '{printf "%.2f",$0}'
> 		注* 换行则加\n --> awk '{printf "%.2f\n",$0}'
> 选项
> 	1> -F #指定分隔符
> 		cat /etc/passwd | awk -F ":" '{print $1}'
> 		解释：等同于cut -d ":" -f 1 /etc/passwd
> 	2> BEGIN #在读取所有行内容前就开始执行，常被用于修改内置变量的值
> 	3> FS #BEGIN时定义分隔符
> 		cat /etc/passwd | awk 'BEGIN{FS=":"}{print $1}'
> 		解释：等同于-F的选项，和cut指定分隔符
> 	4> END #结束的时候执行
> 		awk 'BEGIN {printf "开始\n"} {FS=":"} (NR>=2 && NR <= 10) {print $1} END {print 			"结束"}' /etc/passwd
> 		解释：
> 			开始 --> 输出开始两个字并用冒号分割
> 			中间 --> 输出第二行到第十行的第一列
> 			结束 --> 输出结束两个字
> 	5> NR #行号
> 		df -h | awk 'NR==2 {print $5}'
> 		解释：提取第二行，第五列的值
> 		awk 'BEGIN {FS=":"} (NR>=2 && NR<=10){print $1}' /etc/passwd
> 		解释：使用第二种语法  awk '条件1 {执行动作} 条件2 {执行动作}...' 文件名
> ```
>
> #### 注意记录
>
> ```python
> 注* grep和sed是处理行，awk是处理列，cut的功能完全可以由awk替代，之后碰到就用awk替代。
> ```

#### 12、处理海量数据之cut

> #### cut使用
>
> ```python
> 简介：对数据进行"列"的提取
> 语法：cut [选项] [file]
> 使用：cut [选项] [file] 或者 cat /etc/passwd | cut [选项]
> 参数：
> 	-d #指定分隔符
> 	-f #指定截取区域
> 	-c #以'字符'为单位进行分割
> 	注意：cut 如果不加-d，默认是以制表符为分隔符
> 	注意：/etc/passwd文件的最后一列，/bin/bash代表可以登录用户，/sbin/nologin代表不可登录用户
> 示例：
> 	-d和-f
> 		以":"为分隔符，截取第一列和第三列
> 			cut -d ":" -f 1,3 /etc/passwd
> 		以":"为分隔符，截取第一列到第三列
> 			cut -d ":" -f 1-3 /etc/passwd
> 		以":"为分隔符，截取第二列到最后一列
> 			cut -d ":" -f 2- /etc/passwd
> 	-c
> 		以":"为分隔符，截取第二个字符到第九个字符
> 			cut -d ":" -f 1-3 /etc/passwd | cut -c 2-9 
> 应用：
> 	领导想让你查询linux上面可登录的普通用户
> 	grep '/bin/bash' /etc/passwd | cut -d ":" -f 1 | grep -v "root"
> 	解释：先查出所有包含/bin/bash的行，然后传递给cut以分号切割取第一列，然后传递给grep取反去掉root
> 		这个超级用户
> 	注1* grep /bin/bash /etc/passwd | awk -F ":" '{printf "%s\n",$1}' | grep -v "root"
> 		也可以
> 	注2* grep /bin/bash /etc/passwd | awk -F ":" '{print $1}' | grep -v "root"
> 		也可以
> 	注* grep /bin/bash /etc/passwd | awk -F ":" '{printf $1}' | grep -v "root"
> 		不可以，因为查出来的是rootmysqlqiwu，是一个整体，所以grep -v "root"不起作用
> 	注* '{printf "%s\n",$1}'中printf的第一个参数代表格式，是需要加双引号的。
> ```
>
> #### 注意记录
>
> ```python
> 注* grep和sed是处理行，awk是处理列，cut的功能完全可以由awk替代。cut只用于截取字符串。
> 1> cut 如果不加-d，默认是以制表符为分隔符
> 2> 两种写法cat /etc/passwd | cut -d ":" -f 1-3
> 	或者
>     cut -d ":" -f 1-3 /etc/passwd
> 3> tab键分割的文件，如下：
> 	姓名	得分	评级
> 	小红	89	A
> 	小明	67	C
> 4> 截取字符串，cut很好用，对比如下：
> 	cat /etc/passwd | awk -F ':' '{print $1$2:$3}'
> cat /etc/passwd | cut -d ":" -f 1-3
> ```

#### 13、循环控制语句if

> ```python
> 1> 单个判断（单分支循环）
> 	if [ 条件判断 ];then
> 	fi
>     
> 	if [ 条件判断 ];then
> 	else
> 	fi
> 2> 多个判断（多分支循环）
> 	if [ 条件判断 ];then
> 	elif [ 条件判断 ];then
> 	elif [ 条件判断 ];then
> 	fi
> 注* then就相当于java中的if{}的大括号
> 示例：
> 	#!/bin/bash
> 	#测试多分支循环判断
> 	#by guozi 2019/5/15
> 	echo '请输入一个数值：'
> 	read number
> 	if [ $number -eq 10 ];then
> 		echo '等于10'
> 	elif [ $number -lt 10 ];then
> 		echo '小于10'
> 	elif [ $number -gt 10 ];then
> 		echo '大于10'
> 	fi
> ```

#### 14、循环控制语句for

> #### for使用
>
> ```python
> 1> 使用1：
> 	语法：
> 		for 变量名 in 值1 值2 值3
> 			do
> 			执行动作
> 			done
> 	示例：
> 		#!/bin/bash
> 		#循环打印出1到10
> 		#by guozi 2019/5/15
> 		for i in 1 2 3 4 5 6 7 8 9 10
> 			do
> 			echo "$i"
> 			sleep 1 #睡1s
> 			done
> 2> 使用2：
> 	语法：
> 		for 变量名 in `命令`
> 			do
> 			执行动作
> 			done
> 	示例1：
> 		#!/bin/bash
> 		#循环打印出1到10
> 		#by guozi 2019/5/15
> 		for i in $(seq 1 10)
> 			do
> 			echo "$i"
> 			sleep 1 #睡1s
> 			done
> 	示例2：
> 		#!/bin/bash
> 		#循环ping列表中的主机
> 		#by guozi 2019/5/15
> 		for i in $(cat server.txt)
> 			do
> 			ping -c 2 $i 1>/dev/null  #如果正确的ping通了，输出到无底洞，错误才输出
> 			echo -e "\n"
> 			done
> 		注* -c count	ping指定次数后停止ping；
> 			linux不像window，如果我们不加参数，它会一直ping下去
> 		注* server.txt
> 			www.baidu.com
> 			www.afasdfks.com
> 			xiaoguozi.com.cn
> 			www.xiaoguozi.com.cn
> 			www.nsflkjsad.com
> 			
> 3> 使用3
> 	语法：
> 		for ((条件))
> 			do
> 			执行动作
> 			done
> 	示例：
> 		#!/bin/bash
> 		#循环打印出1到10
> 		#by guozi 2019/5/15
> 		for ((i=1;i<11;i++))
> 			do
> 			echo "$i"
> 			sleep 1 #睡1s
> 			done
> ```
>
> #### 注意记录
>
> ```python
> 1> ping -c 2 www.baidu.com
> 	ping两次，两次之后，自动断开
> 	linux不像window，如果我们不加参数，它会一直ping下去
> ```

#### 15、循环控制语句case

> ```python
> 简介：类似于java中的switch case
> 语法：
> 	case 变量 in
> 		值1)
> 		执行动作
> 		;;
> 		值2)
> 		执行动作
> 		;;
> 		值3)
> 		执行动作
> 		;;
> 		*)
> 		执行动作
> 		;;
> 	esac
> 示例：
> 	#!/bin/bash
> 	#测试case循环语句
> 	#by guozi 2019/5/15
> 	echo "请输出查询天气的城市："
> 	read city
> 	case $city in
> 		北京)
> 		echo "晴天"
> 		;;
> 		上海)
> 		echo "小雨"
> 		;;
> 		广州)
> 		echo "多云"
> 		;;
> 		*)
> 		echo "输入城市有误"
> 		;;
> 	esac
> ```

#### 16、循环控制语句while

> ```python
> 简介：while循环是条件循环也是不定循环，只要条件判断式成立，循环就会一直进行着。
> 语法：
> 	while [ 条件判断式 ]
> 	do
> 		执行动作
> 	done
> 示例：
>     #!/bin/bash
>     #计算从0到输入数字的累加和
>     #by guozi 2019/5/15
>     echo "请输出数字："
>     read number
>     i=0
>     sum=0
>     while [ $i -lt $number ]
>     do
>             sum=$((sum + i))
>             i=$((i + 1))
>             echo "当前i为：$i，当前总数为$sum"
>     done
> 注* 实现和for ((i=0;i<$number;i++))
> 注* 死循环：while [ 1 ]
> 注意：
> 	1> 变量赋值，等号两边一定不能有空格
> 	2> sum=$((sum + i))是给变量sum赋值，不能写成$sum=$((sum + i))
> 	3> sum=$((sum + i))是对的，sum=$(($sum + $i))也可以。
> 		详见运算符，a=12;b=6;echo $((a + b))
> ```

#### 17、实战-嵌套循环框架

> ```python
> 1> 外层循环 -- 死循环
>     #!/bin/bash
>     #脚本实战之运维工具
>     #by guozi 2019/5/15
>     while [ 1 ]
>     do
>     cat <<EOF
>     *************************
>     *************************
>     *************************
>     *************************
> 
>     EOF
>     done
> 	注* 在shell中，cat <<EOF位置可以随便写，前面可以有空格。但是EOF前面必须不能有空格。否则报错。
> 2> 外层循环 + 内层循环
>     #!/bin/bash
>     #脚本实战之运维工具
>     #by guozi 2019/5/15
>     while [ 1 ]
>     do
>     cat <<EOF
>     *************************
>     *************************
>     *************************
>     *************************
> 
>     EOF
>     echo "请输入选项"
>     read option
>     case $option in
>             1)
>             clear
>             echo "执行1.sh"
>             ;;
>             2)
>             clear
>             echo "执行2.sh"
>             ;;
>             q)
>             clear
>             echo "拜拜"
>             exit
>             ;;
>             *)
>             clear
>             echo "输入有误"
>             ;;
>     esac
>     done
> 注1：格式是内外层嵌套循环，外层为死循环，但是内层每一次都需要输入参数，在read执行时，会卡住，所以避	免了死循环耗费资源。
> 注2：cat <<EOF
> 	---------
> 	EOF
> 	作用是把中间的内容完整输出，EOF只是一个标识，只要前后字符一样即可，比如cat <<KKK ----- KKK
> ```
>

#### 18、实战之巡检内存使用率

> ```python
> 前提：
> 	巡检的不只是内存使用率，还有CPU、文件系统、数据库表空间，
> 	而且告警方式不是打印出来，还有短信和linux邮箱
> 1> 内存使用值
> 	mem_total=$(free -m | sed -n "2p" | awk '{printf $2}')
> 	mem_used=$(free -m | sed -n "2p" | awk '{printf $3}')
> 	mem_free=$(free -m | sed -n "2p" | awk '{printf $4}')
> 	或者
> 	free -m | grep -i mem | awk '{printf $2"\n"}'
> 	grep和sed都是去取行的
> 2> 内存使用百分比
> 	percent_mem_used=$(echo "scale=2;$mem_used/$mem_total*100" | bc)
> 	percent_free_used=$(echo "scale=2;$mem_free/$mem_total*100" | bc)
> 3> 当前时间格式化
> 	now_time=$(date +"%Y-%m-%d %H:%M:%S 星期%w")
> 4> 判断内存使用并告警
> 	if [ $(echo "percent_free_used<10" | bc) -eq 1 ];then
>         echo -e "\033[43;31;5m告警：\n\033[0m"
>         echo -e "\033[43;31;5m当前内存使用率：$percent_mem_used%；内存剩余：						$percent_mem_free%\033[0m"
>     else
>         echo "当前内存使用率正常"
> 汇总脚本：
>     #!/bin/bash
>     #巡检内存使用率
>     #by guozi 2019/5/15
>     mem_total=$(free -m | sed -n "2p" | awk '{printf $2}')
>     mem_used=$(free -m | sed -n "2p" | awk '{printf $3}')
>     mem_free=$(free -m | sed -n "2p" | awk '{printf $4}')
>     percent_mem_used=$(echo "scale=2;$mem_used/$mem_total*100" | bc)
>     percent_mem_free=$(echo "scale=2;$mem_free/$mem_total*100" | bc)
>     echo -e "\n"
>     now_time=$(date +"%Y-%m-%d %H:%M:%S 星期%w")
>     if [ $(echo "percent_free_used<10" | bc) -eq 1 ];then
>         echo -e "\033[43;31;5m告警：\n\033[0m"
>         echo -e "\033[43;31;5m当前内存使用率：$percent_mem_used%；内存剩余：						$percent_mem_free%\033[0m"
>     else
>         echo "当前内存使用率正常"
>     fi
> 注意1：
> 	小数的比较
> 		[ $(echo '1.4>1.3' | bc) -eq 1 ] && echo "成立"
> 	小数和整数的比较
> 		[ $(echo "12.23>10" | bc) -eq 1 ] && echo "正确"
> 	都需要使用到bc计算器
> 注意2：
> 	$(echo "percent_free_used<10" | bc)
> 	$()括起来之后，里面的变量可以不加$符号，加上也可以$(echo "$percent_free_used<10" | bc)
> ```

#### 19、实战-批量创建用户

> ```python
> 前提：
>     1 grep如果没有查找到匹配行，接下来用$?返回的是1。如果找到了，返回的是0。
>     2 stdin是passwd的一个选项，意思是把管道之前传过来的值设置到某一个用户上。
>     3 cat /etc/passwd | grep user如果找到了匹配到的行，是会输出打印出来的。
>         如果不想打印出来，就输出到无底洞里面。1>/dev/null
>     4 密码保存起来，一定是>>，代表追加的意思，不能用>，这个是覆盖
>     5 密码赋值成功，也会提示信息输出打印，如果不想打印出来，也是输出到无底洞
>     6 脚本写完之后，进行检测，一个是密码文档中是否完整，一个是挑选一个用户进行登录，id命令验证。
>     7 最后再写一个进行删除用户的脚本。
> 1> 查看系统是否存在用户
> 	cat /etc/passwd | grep user1
> 	exist=echo $? #存在则exit为0，不存在则为1
> 2> 创建用户
> 	useradd user1 2>/dev/null && echo "创建用户user1成功"  #创建用户的错误信息输到无底洞不必须
> 3> 生成随机密码
> 	password=$(head -2 /dev/urandom | md5sum | cut -c 1-8)
>         head -2 取/dev/urandom文件的前2行 （/dev/urandom是linux下一个生成随机数的文件）
>         md5sum 是加密生成随机字符串
>         cut -c 1-8 是剪切字符串，-c是按字符剪切
> 4> 设置密码
> 	echo $password | passwd --stdin user1
> 	注* stdin是passwd的一个参数选项，意思是把管道之前传过来的值设置到某一个用户上。
> 5> 记录密码	
> 	echo $password | passwd --stdin user1 && echo "用户名user1，密码							$password">>/user/local/shell-script/new_passwd.txt
> 	注* 密码保存起来，一定是>>，代表追加的意思，不能用>，这个是覆盖
> 汇总脚本：
>     #!/bin/bash
>     #批量创建用户
>     #by guozi 2019/5/15
>     read -p "请输入创建用户名" username
>     read -p "请输入创建用户个数" sum
>     for ((i=1;i<=$sum;i++))
>     do
>         cat /etc/passwd | grep "${username}${i}"  #这儿是${}取值变量的用法，"${username}$i"
>         if [ $? -eq 1 ];then #不存在
>             #创建用户
>             useradd ${username}${i} 2>/dev/null && echo "创建用户${username}${i}成功"
>             #生成密码
>             password=$(head -2 /dev/urandom | md5sum | cut -c 1-8)
>             #设置记录密码
>             echo $password | passwd --stdin ${username}${i} && echo "用户名${username}${i}，			密码$password">>/usr/local/shell-script/new_passwd.txt
>         else
>             echo "用户${username}${i}已经存在，不需要重复创建"
>         fi
>     done
> ```

#### 20、实战-操作数据库

> #### 步骤
>
> ```python
> 前提：
> 	mysql -uroot -p -e其中-e就是非交互界面的意思
> 1> 上面输入一次mysql的用户名和密码，下面可以多次用这个用户执行sql。
> 2> 执行语句为：mysql -u${user} -p ${password} -e ${sql}
> 	其中-e就是非交互界面的意思
> 汇总脚本：
> 	注* 下面是视频的代码，在我电脑不适用，我的Mysql5.7。正确详见"各种报错解决"
> 	#!/bin/bash
> 	#操作数据库
> 	#by guozi 2019/5/15
> 	read -p "请输入要查询学生的姓名" username
> 	read -p "请输入mysql账号" loginname
> 	echo -e "\n"
> 	read -p "请输入mysql密码" password
> 	sql="select * from student.userinfo where username=${username}"
> 	mysql -u${loginname} -p ${password} -e ${sql}
> 	exit
> ```
>
> #### 各种报错解决
>
> ```python
> 吐槽：
> 	一开始就没有搞定，过了半个月，人到了上海，有搞了一个小时，终于搞定了。mmp
> 1> 正确示范
> 	mysql -uroot -p123456 -e "select * from student.userinfo where username='guozi'";
> 	你在linux的shell中直接输入上面命令，即可查询到student库中的userinfo表中的信息。
> 	其他有任何一点错误，运行shell脚本，都会输出一堆mysql的用法参数。
> 2> -p和密码之间必须没有空格，有空格就报错，只是有一个警告，直接输密码不安全：
> 	mysql: [Warning] Using a password on the command line interface can be insecure.
> 3> -e是执行的意思execute，后面的sql语句，必须要用双引号括起来
> 4> 'guozi'必须用单引号括起来，否则将被当做是字段名。
> 5> shell中字符串拼接
> 	直接${name1}${name2}"字符串"连着写就可以
> 	来源：https://www.jb51.net/article/44207.htm
> 6> 正确代码
>         #!/bin/bash
>         #操作数据库
>         #by guozi 2019/5/15
>         read -p "请输入要查询学生的姓名：" username
>         read -p "请输入mysql账号：" loginname
>         echo -e "\n"
>         read -p "请输入mysql密码：" password
>         sql="select * from student.userinfo where username=""'"${username}"'"
>         echo "mysql -u${loginname} -p${password} -e ${sql}"  #这儿时输出调试的，直接cmd运行
>         mysql -u${loginname} -p${password} -e """${sql}"""
>         exit
> ```