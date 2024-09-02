<h1 align="center">做e时代的主人</h1>

### 前言

<h6><b><img src="awesomeface.png" alt="welcome" width="29px">[注:这不仅是一份预习文档，也可以当作以后学习期间的长期方向指导]</h6>

​	推荐用手机或者平板，可以躺在床上或者沙发上。在电脑上也可以使用 WIN + ← 将此文档放到屏幕一侧，右边可以用自己的IDE动手做实验。

​	可以按照顺序阅读，也可以直接跳到感兴趣的章节。

**符号约定**：

<img src="question.png" alt="q" width="25px"> 这个用来表示暂时无需完全理解的细节问题，供深入研究和思考所用；

<img src="bulb.png" alt="b" width="25px"> 这个用来表示联想内容或是温馨提示;

<img src="awesomeface.png" alt="a" width="25px"> 这个用来表示下面的内容是一段笑话或是在项目开发过程出现的梗;

<img src="warning.png" alt="w" width="25px"> 这个用来表示下面的内容是容易犯错的地方，特此警告；

**写给读者:**

​	<img src="warning.png" alt="w" width="25px">这只是一份参考文档，并不能作为学习的唯一工具，我们推荐自己动手查阅更多资料，学习如何阅读官方文档，**这对以后的学习开发非常重**要。我们的培训不能覆盖到所有方面，而现实情况下我们遇到的问题和困难却是防不胜防的。本文档也将着力向大家传授部分阅读官方文档的方法。

​	<img src="awesomeface.png" alt="welcome" width="29px">另一方面，我们也不希望读者会对开发项目和写代码这些概念理解的过于沉重，代码只是我们在信息时代的一款语言，我们不需要去死记硬背各种标签或是函数，但是我们需要理解它们是一种什么样的存在，以及为什么而存在。

​	最后一点，在计算机领域虽然看似很抽象，但是却比现实世界要单纯许多。希望我们社团的培训能够使大家产生对计算机的兴趣，进一步学会更多技能。也希望大家正确对待计算机，多多学习和实践，成为e时代的主人。



### 章节列表

<h6><b>入门篇</b></h6>

1. 你好, 0和1的世界
2. 网页是什么(上):元素
3. 开发环境和基础平台配置
4. 进入代码(上):基本类型和逻辑
5. 让函数再次伟大!

<h6><b>进阶篇</b></h6>

1. 进入代码(下):指针和自定义类型，更多特性
2. 编程思想浅谈
3. 网络沉思录
4. 同步与异步

<h6><b>实战篇</b></h6>

1. 网页是什么(下):前端和后端
2. 前后端通用工具简介
3. 前端学习浅谈和开发规范
4. 后端学习浅谈和开发规范





## 施工中





#### 入门篇其3-开发环境和基础平台配置

##### 开发平台选择：

> ​	<img src="awesomeface.png" width="25px">推荐Arch Linux或者Ubuntu作为开发环境，当然我们培训是基于windows开展的。



**编译器，编辑器和IDE**
$$
编译器 \neq IDE！
$$




	编译器是将源代码转换为可执行程序的工具，比如gcc,llvm,go build等。编译器通过多个阶段（如词法分析、语法分析、语义分析、代码⽣成等）将源代码转换成可执⾏⽂件或库。特点是可以⼀次性转换整个源代码。可以进⾏语法和语义检查，提⾼代码质量。⽣成的代码执⾏效率⾼，但编译过程可能耗时较⻓。


	编辑器是程序员⽤于编写和修改源代码的软件⼯具。它提供了⽂本编辑的基本功能，如插⼊、删除、复制和粘贴等，以及针对编程语⾔的特定功能，如语法⾼亮、代码折叠和⾃动完成等。本⾝并不参与代码的执⾏和转换，如vscode，记事本。


	IDE是⼀种集成了多种开发⼯具和功能的软件应⽤程序，旨在提⾼软件开发的效率和质量。它通常包括源代码编辑器、编译器、调试器、构建⼯具、版本控制系统等，为程序员提供了⼀个全⾯的开发环境。集成了多种开发⼯具，⽅便程序员在同⼀个界⾯下完成开发任务。提供了丰富的功能和插件，满⾜不同开发需求。⽀持代码⾃动完成、语法⾼亮、代码重构等，提⾼编程效率和质量。可以⾃动管理代码库、构建⼯具和⽂档等，减少⼿动操作的时间和错误。如Visual Studio，IDEA，Pycharm。

<img src="question.png" width = "25px"> 我们在入门过程中不需要完全理解编译器的原理，而是选择使用合适的编辑器或者IDE来开发项目。我们推荐使用vscode来进行开发工作。



##### 编辑器vscode 配置

使用记事本来写代码显示我们太逊了:innocent:，我们需要一个更酷炫更方便的开发工具。

这里推荐大家使用 `Visual Studio Code` 编辑器，先到其[官网下载](https://code.visualstudio.com/)安装。选择适合自己电脑的发行版进行安装。windows就一条龙到底就行了。记得选择添加到PATH中，这样方便以后在终端直接 `code .`打开这个项目文件夹。桌面快捷方式可以自行选择是否创建。

<img src="vsc1.png" width = 500px>

> <img src="awesomeface.png" width="25px">有关 vscode 可以看我们B站的一个视频了解一下。为什么 Visual Studio Code 被誉为 IDE 中最强的男人：https://www.bilibili.com/video/BV13v411w7Fb

现在我们已经完成了软件的安装。但是打开vscode的话里面还是空空的，因为它本身只是一个文本编辑器，我们需要安装一些插件来让它变得强大(:yum:vscode补全计划)



下面我们以配置html开发环境为例，其他语言如何配置可以查阅相关文档。先介绍vscode上几个常用组件。

**插件市场**

vscode 自身的产品思路就是一个轻量级的开发工具加上繁荣开放的插件市场组成。因此很多强大的功能需要通过安装插件来实现，目前 vscode 的插件市场中已经有着几万个插件。通过 `侧边栏上的按钮` 或快捷键 `Ctrl + Shift + X` 打开 vscode 的插件市场。

<img src="https://qiniu.3yya.com/ca3a892f5d5cca90adaaf101a0504e0a/ca3a892f5d5cca90adaaf101a0504e0a.png" width=500px>

**命令面板**

vscode 的命令面板能让我们快速方便地执行很多功能与命令，包括自身的设置和插件提供的功能等。

通过 `View -> Command Palette` 或者快捷键 `Ctrl + Shift + P` 可以打开命令面板。

<img src="https://qiniu.3yya.com/085039b5ebd66fa5b0e927d5ff803707/085039b5ebd66fa5b0e927d5ff803707.png" width = 500px>

**配置面板**

通过 `File -> Preferences -> Settings` 或 `Ctrl + ,` 打开配置面板。

<img src="https://qiniu.3yya.com/230cb699debabe62f5a05afc42077fbc/230cb699debabe62f5a05afc42077fbc.png" width=500px>

**简单的配置**

在插件市场搜索并下载一些插件，下面是一些常用的，当然你也可以自行下载：

1.中文插件

2.`Live Server` 可以将当前项目映射到本地的 IP 的端口，通过这个端口就可以像访问网站一样访问项目文件，对我们前端项目开发中的实时预览很有帮助。

3.`Prettier` 是一款强大的格式化插件，支持多种前端语言。

安装插件后还要配置一下，按下 `Ctrl + ,` 打开配置面板，输入 format 过滤配置项。将 `Default Formatter （默认格式化工具）` 选择为 `Prettier`，我个人还习惯将 `Format On Save （保存时格式化）` 勾选上。

4.`CSS Peek` 能够帮助我们快速地定位、预览样式的定义。

5.`JavaScript (ES6) code snippets` 可以帮助我们快速地插入代码块，支持以下多个前端语言。

- JavaScript (.js)
- TypeScript (.ts)
- JavaScript React (.jsx)
- TypeScript React (.tsx)
- Html (.html)
- Vue (.vue)

下载了一些插件之后，就可以进行简单的html网页开发了。

新建一个 HTML 文件，输入代码保存。右键 `Open with Live Server` 便会打开一个浏览器实时显示我们的页面

<img src="https://qiniu.3yya.com/aa3f6c4bc5b6ca7bb49680fea86df1a8/aa3f6c4bc5b6ca7bb49680fea86df1a8.png" width=700px>



##### 系统变量设置

我们经常需要将某些路径添加到系统变量中，这样方便我们可以快速调用它们。下面以windows平台为例，演示如何添加环境变量。

<img src="sys1.png" width=800px>

点击“环境变量”选项后，可以设置变量名和值。

<img src="sys2.png" width=800px> 

完成以后点击确定，就可以保存到环境变量了:blush:



##### 更多的开发工具

我们上网冲浪的时候，经常会看到好多人在吵用什么工具写程序是最好的。下面是全网统计的编译器/IDE受欢迎图：

<img src="rank.png">

​	但是 :cold_sweat: `visual studio`太重了！！而且vs主要经营.Net的开发和调试，也不是我们的主力语言。相比之下`vscode`便捷而且拥有海量插件，配置的好的话也不会比vs差到哪去。

​	不过市场上其他的编译器和IDE同样值得推荐，比如Jetbrains全家桶中的idea(收费，建议使用学信网去申请个教育包)，vim(门槛较高)，用起来也是很爽的。IDE的好处是开盖即用，不需要再过多配置，但是可能比较重而且不够自由。



#### 入门篇其4-进入代码(上):基本类型和逻辑

##### 走入代码的世界

正如同现实世界中将物质分成了各种类型一样，计算机世界里也将数据存储为了各种类型。相对的，也存在这最小的存储单元：位(bit，或者缩写为b)，也就是一个0或者1。我们通常的信息计量单位是字节(byte，缩写为B)，**一个字节是8个位**。同样的，数据的不同类型也有着不同的大小(size)。下图列举了一些常见的类型和其大小。

| 类型         | 占用存储空间               | 表示范围                         |
| ------------ | -------------------------- | -------------------------------- |
| byte         | 1字节                      | true或者false                    |
| 单精度float  | 4字节                      | -3.403e38 ~ 3.403e38             |
| 双精度double | 8字节                      | -1.798e308~1.798e308             |
| int          | 32位系统4字节64位系统8字节 | -2^31 ~ 2^31-1 或 -2^63 ~ 2^63-1 |
| uint         | 32位系统4字节64位系统8字节 | 0~2^32-1 或 0 ~ 2^64-1           |
| char         | 1字节                      | 存储ASCII字符                    |

<img src="bulb.png" width=25px>另外还有类似int8，int64，string等类型，大家可以自行搜索做了解。

当我们知道了如何表示数据后，就可以来尝试来一段代码了：这里就用c语言来演示
定义变量的方式： [变量类型] 变量名 = 某个值或者表达式

```c
#include<stdio.h>
int main(void){
    int integer = 1;
    bool condition = false;
    char letter = 'a';
    
    printf("my first variable: %d",integer); // 输出 my first variable: 1
    // ... 其他也可以自行尝试查看如何输出
}
   
```

<img src="question.png" width=25px> 我们也可能会遇到定义的变量类型和我们需要的类型不一致的情况，这时我们需要转换这个变量。一般情况下有隐式转换和显示转换两种方式，读者可以自行查阅了解相关内容，如何转换以及什么情形下可以转换。



<img src="warning.png" width=25px>**注意：有些符号我们称之为“关键字”，这是语言本身提供的，用来编写代码的元素。比如上面的int, bool等。我们给变量起名时不可以和关键字重名。大家可以自行查阅常用关键字。**



##### 表达式

将变量通过某些运算符号连接起来，就是表达式了。比如：

```c
int v1 = 100;
float v2 = 200;
// 表达式举例
float expression_1 = v1+v2;
float expression_2 = v2-v1;
bool equal = v1==v2;

//表达式也可以连接起来：使用()来改变运算顺序
float expression_3 = 3*(expression_1+expression_2)
// 更多可以自行探索
```

##### 基本运算符
+，-， *， / ：这是表示四则运算的符号。使用%取余。

##### 逻辑运算和逻辑运算符
逻辑运算会返回真，假两个值其中之一，判断规则是第二列所示
| 符号 | 含义                         |
| ---- | ---------------------------- |
| ==   | 左右两个元素是否相等         |
| !=   | 左右两个是否不相等           |
| >    | 左边是否大于右边             |
| <    | 左边是否小于右边             |
| >=   | 左边是否不小于右边           |
| <=   | 左边是否不大于右边           |
| &&   | 左边和右边同时成立           |
| \|\| | 左边或者右边成立             |
| !    | 逻辑非，将真变为假，假变为真 |

> <img src="awesomeface.png" width=25px>[注：不同语言中可能有更多的逻辑运算符，可自行查找]



##### 简单语句

一般情况下，编程语言中都是在 if 关键字语句中使用逻辑运算，也称"控制语句"，例如：

```
//格式： if(condition){
// 	herein code will run if condition is true
// }else{
//	herein code will run if condition is false
// }
int a=10;
int b=20;
if(a>=0 && b<=30){ //判断如果a不小于0，同时b不大于30，如果成立则执行if语句内部的代码
	printf("right!");
}
if(a!=b){ //判断如果a不等于b，成立则执行内部代码
	//...
}else if(a<b){ // 继续判断，如果a小于b,执行内部代码
	printf("a is smaller!");
}else{ //如果之前的判断都不成立，执行这个内部的代码
	pritnf("b is smaller!");
}
```

另一方面，我们也有所谓的“循环语句”，以 for 关键字为例，

```
//全写格式是： for(initial;final;operation)
int i=0;
for(;i<10;){
	printf("%d",i);
	i=i+1;
}
// 这个等价于
for(int j=0;j<10;j++){
	printf("%d",j);
}
```

<img src="question.png" width=25px>可以自行查询 switch, while等控制、循环语句关键字的作用



##### <img src="question.png" width=25px>位运算和位运算符

(这一部分建议自行了解)

| 符号 | 描述     | 运算规则                                    |
| :--- | :------- | :------------------------------------------ |
| &    | 与       | 两个位都为1时，结果才为1                    |
| \|   | 或       | 两个位都为0时，结果才为0                    |
| ^    | 异或     | 两个位相同为0，相异为1                      |
| ~    | 取反(非) | 0变1，1变0                                  |
| <<   | 左移     | 各二进位全部左移若干位，高位丢弃，低位补0   |
| >>   | 右移     | 各二进位全部右移若干位，高位补0或符号位补齐 |

位运算我们一般用的不多，不过可能有时候会出现左移和右移的代码，通俗来讲，左移后移就是乘以2的某次幂：

``` c
int a =1;
a<<2; // = a*(2^2)
a>>1; // = a/(2^1)
```



##### 运算顺序

<img src ="warning.png" width=25px> 在开发过程中往往会有多个运算符出现在一起，和数学上的运算一样，这时候需要规定运算顺序，以及如何改变运算顺序。

这里是一份以c语言为例的运算符优先级排序，其他语言可以自行查阅了解。<img src="question.png" width=25px>有些运算符我们现在还没有提到，可以搜索看看都是什么。

| 优先级 | 操作符             | 描述                   |
| :----- | :----------------- | :--------------------- |
| 1      | `++` `--`          | 后缀自增自减运算符     |
|        | `()`               | 函数调用               |
|        | `[]`               | 数组下标               |
|        | `.`                | 类成员变量             |
|        | `−>`               | 类成员变量（指针访问） |
|        | `(*type*){*list*}` | 复合字面量             |
| 2      | `++` `--`          | 前缀自增自减运算符     |
|        | `+` `−`            | 一元加减法             |
|        | `!` `~`            | 逻辑非和位运算非       |
|        | `(*type*)`         | 显式类型转换           |
|        | `*`                | 解引用                 |
|        | `&`                | 取地址                 |
|        | `sizeof`           | Size-of                |
|        | `_Alignof`         | 对齐                   |
| 3      | `*` `/` `%`        | 乘法，除法，取余       |
| 4      | `+` `−`            | 加法和减法             |
| 5      | `<<` `>>`          | 左移和右移             |
| 6      | `<` `<=`           | 小于和不大于           |
|        | `>` `>=`           | 大于和不小于           |
| 7      | `==` `!=`          | 等于和不等于           |
| 8      | `&`                | 位运算与               |
| 9      | `^`                | 位运算异或             |
| 10     | \|                 | 位运算或               |
| 11     | `&&`               | 逻辑运算与             |
| 12     | \|\|           | 逻辑运算或             |
| 13     | `?:`               | 三元条件判断符         |
| 14     | `=`                | 赋值运算               |
|        | `+=` `−=`          | 加、减到左边           |
|        | `*=` `/=` `%=`     | 乘、除、取余到左边     |
|        | `<<=` `>>=`        | 左移、右移到左边       |
|        | `&=` `^=` `|=`     | 位运算到左边           |
| 15     | `,`                | 逗号                   |



#### 进阶篇其3-网络沉思录

##### 什么是计算机网络

```
计算机网络包括两个或更多个通过电缆（有线）或WiFi（无线）连接的计算机，用于传输、交换或共享数据及资源。可以使用硬件（例如，路由器、交换机、接入点和电缆）和软件（例如，操作系统或业务应用程序）来构建计算机网络。

通常按地理位置来定义计算机网络。例如，局域网(LAN)可连接特定物理空间（例如办公大楼）中的计算机，而广域网(WAN)可连接各大洲的计算机。互联网是最大的WAN，它连接了全球数十亿台计算机。
```

常见网络类型是：

```
    • 局域网(LAN)：LAN可在相对短的距离内连接计算机，以便它们可以共享数据、文件和资源。例如，LAN可以连接办公大楼、学校或医院中的所有计算机。通常，LAN由私人拥有和管理。

    • 无线局域网(WLAN)：WLAN类似于LAN，但以无线方式连接网络上的设备。

    • 广域网(WAN)：顾名思义，WAN可以连接一个广阔区域（例如跨地区或跨大洲）内的计算机。互联网是最大的WAN，它连接了全球数十亿台计算机。集体所有权模型或分布式所有权模型都是常见的WAN管理模型。

    • 城域网(MAN)：MAN通常比LAN大，但比WAN小。MAN通常由城市和政府单位拥有和管理。

    • 个人区域网(PAN)：一个PAN为一个人提供服务。例如，如果您同时拥有iPhone和Mac，那么您很有可能已经建立了一个PAN，可以在两个设备之间共享和同步内容（短信、电子邮件、照片等）。

    • 校园网(CAN)：CAN也可表示企业区域网。CAN比LAN大，但比WAN小。CAN可以为学院、大学和商业园区等场所提供服务。

    • 虚拟专用网(VPN)：VPN是两个网络终端之间安全的点到点连接。VPN建立了一个加密通道，该通道将保留黑客都无法访问的用户身份和访问凭证以及所传输的所有数据。
```



##### 常用术语

```
    • IP地址：IP地址是为使用互联网协议进行通信的网络中连接的每个设备分配的唯一编号。每个IP地址都会标识设备的主机网络以及设备在主机网络上的位置。当一个设备向另一个设备发送数据时，数据包含一个"标头"，其中包含发送设备的IP地址和目标设备的IP地址。

    • 节点：节点是网络内可以接收、发送、创建或存储数据的连接点。每个节点都要求您提供某种形式的身份来接收访问权限，例如IP地址。节点的一些例子包括计算机、打印机、调制解调器、网桥和交换机。节点实质上是可以识别和处理信息并将信息传输到任何其他网络节点的任何网络设备。

    • 路由器：路由器是用于在网络之间发送数据包中包含的信息的物理或虚拟设备。路由器会分析数据包中的数据，以确定将信息传输到最终目的地的最佳方式。路由器会转发数据包，直至其到达目标节点。

    • 交换机：交换机是一种设备，它可以连接其他设备并管理网络内节点间通信以确保数据包到达最终目的地。路由器是在网络之间发送信息，而交换机是在单个网络中的节点之间发送信息。在讨论计算机网络时，"交换"是指在网络中的设备之间传输数据的方式。

    • 端口：端口将标识网络设备之间的特定连接。每个端口均由一个编号标识。如果将IP地址比作酒店的地址，那么端口就是该酒店内的套房或房间号。计算机使用端口号确定哪个应用、服务或进程应接收特定报文。（扩展知识：端口转发，一个端口承担多个作用）

    • 网络电缆类型：最常见的网络电缆类型包括以太网双绞线、同轴电缆和光纤。电缆类型的选择取决于网络的规模、网络元素的排列以及设备间的物理距离。
```



##### 网络如何工作

<img src="question.png" width=25px> 这些东西阅读了解即可，具体的TCP/IP协议内容很多，今后将会逐步学习

```
计算机网络使用电缆、光纤或无线信号来连接计算机、路由器和交换机等节点。利用这些连接，网络中的设备便可以进行通信并共享信息和资源。
网络需要遵循协议，而协议定义了发送和接收通信内容的方式。协议是规则的集合，在网络中要做到有条不紊地交换数据，就必须遵循一些事先约定好的规则。这些规则明确规定了所交换的数据的格式以及相关的同步问题。为进行网络中的数据交换而建立的规则、标准或约定称为网络协议（Network Protocol），它是控制两个（或多个）对等实体进行通信的规则的集合。设备可使用这些协议进行通信。例如，网络上的每个设备都会使用TCP协议或IP协议来进行通讯。
路由器是可使不同网络进行通信的虚拟或物理设备。路由器会分析信息，以确定数据到达最终目的地的最佳方法。交换机可连接设备并管理网络内的节点间通信，从而确保信息包通过网络到达最终目的地。

最顶层的是一些应用层协议，这些协议定义了一些用于通用应用的数据报结构，包括FTP及HTTP等。中间层是UDP协议和TCP协议，它们用于控制数据流的传输。UDP是一种不可靠的数据流传输协议，仅为网络层和应用层之间提供简单的接口。而TCP协议则具有高的可靠性，通过为数据报加入额外信息，并提供重发机制，它能够保证数据不丢包、没有冗余包以及保证数据包的顺序。对于一些需要高可靠性的应用，可以选择TCP协议；而相反，对于性能优先考虑的应用如流媒体等，则可以选择UDP协议。

最底层的是网际网络协定，是用于报文交换网络的一种面向数据的协议，这一协议定义了数据包在网际传送时的格式。目前使用最多的是IPv4版本，这一版本中用32位定义IP地址，尽管地址总数达到43亿，但是仍然不能满足现今全球网络飞速发展的需求，因此IPv6版本应运而生。在IPv6版本中，IP地址共有128位，“几乎可以为地球上每一粒沙子分配一个IPv6地址”。IPv6目前并没有普及，许多网际网络服务提供商并不支持IPv6协议的连接。但是，可以预见，将来在IPv6的帮助下，任何家用电器都有可能连入网际网络。
```

<img src="question.png" width=25px>如果学习大学计算机课程的话，会接触到网络体系结构，也就是下图所示的

<img src="https://img-blog.csdnimg.cn/img_convert/afe9b94ee66ddc880668dfef2c607d39.png" width=800px>







#### 实践篇其4-后端学习浅谈和开发规范

##### go语言基础


```go
package main

import "fmt"

func main(){
    fmt.Println("Hello World!")
}
```

上面是go语言的Hello World示例，在学习过程中遇到问题可以参阅<a href="https://golang.google.cn/doc/">go语言的官方文档</a>

###### go语言的代码结构

一个go语言项目的代码由不同的包组成，其中`main`包中包含主函数，即程序运行的起点

go语言的文件后缀是`.go`，每个文件必须在开头声明包，比如上例`Hello World`中，必须先声明此文件在`main`包中

然后需要引用此文件依赖的包，这部分vscode会帮你自动补全，比如，你只要在`main`函数中写`fmt.Println`，然后Ctrl+S保存此文件，那么`import`部分就会自动生成。一个文件有可能不依赖任何包，也有可能依赖于标准库（比如`fmt`），或者一些第三方包（比如`gin`）

###### 定义变量
使用`var`关键字定义变量

`var`关键字既可以在函数内又可以在函数外定义变量，在函数外定义的变量为全局变量，可以在此包内或者包外使用在函数内定义的变量为局部变量，只能在函数内部使用
```go
package main

var GlobalVar string = "global"

var intVar int = 5

func main(){
    var localVar string
    localVar = "local"
}
```
> go语言对变量的命名有较严格的要求。在函数外定义的变量，若变量名首字母为大写，则可以既可以在包内使用，也可以在包外使用，比如上例中的`GlobalVar`，若首字母为小写，那么只能在包内使用，比如上例中的`intVar`，

> 为了规范和合法，请遵循以下的命名规范
> + 大驼峰命名法：变量名中每个单词的首字母大写，比如`UserName`,`InterviewTime`
> + 小驼峰命名法：变量名中第一个单词的首字母小写，其他单词的首字母大写，比如`accessToken`,`timeLimit`
> + 变量名不以数字开头，不使用中文
> + 变量名不和go语言的关键字冲突，比如`for`,`func`




使用`:=`符号定义变量

`:=`只能在函数内定义变量，这种定义方法不需要声明类型。请使用和上面相同的命名规范
```go
package main

func main(){
    num := 25
}
```


###### go语言的基本数据类型
**`int`**:用来存储整数，可以进行基本数学运算，在64位的电脑上，其长度为64位，在32位的电脑上，其长度为32位，以64位电脑为例，其存储范围为
$$
-2^{63} \sim 2^{63}-1
$$
其他长度的`int`如下：`int8`,`int16`,`int32`,`int64`，长度分别为：8位，16位，32位，64位，其存储范围仿照上例

相应的，不存储符号的整数类型如下：`uint`,`uint8`,`uint16`,`uint32`,`uint64`以`uint64`为例，其存储范围是
$$
0 \sim 2^{64}
$$

**`float32`和`float64`**:用来存储浮点数类型，显然`float64`会比`float32`更加精确

```go
var percent float32 = 0.11253
```

**`string`**:用来存储字符串，定义字符串时，内容请使用双引号`"`或者反引号 ` 括起来。字符串可以进行加法操作，如下

```go

var a = "hello"
b := "world"
fmt.Println(a+b)
// 输出
// Hello World

```
可以进行索引查询操作来获取字符串中的某一个字符，如下（注意，计算机中的索引都是从0开始）

```go
str := "Hello World"
char := string(str[6])
fmt.Println(char)
// 输出
// W

```
**`bool`**:表示真和假，只有`true`,`false`，go语言中不能使用0和1来作为布尔值
```go
condition1 := true
condition2 := false
```

**`切片`** go语言支持动态数组，并且提供了一些常用方法。
```go
a := []int{1,2,3,4,5}
type Stu struct{
    Name string
    Age int
}
stus := []Stu{}

stus = append(stus,Stu{
    Name:"wjj",
    Age:80,
})
// 向切片追加值
```

**`map`**:映射，用来存储键值对，可以将一个类型映射到另一个类型，如下：

```go
MyMap := map[string]string{
    "name":"wjj",
    "password":"123456",
}

delete(MyMap,"name")
// 删除映射中的某个键值对
```
根据键查值的用法，如果键在map中存储了，那么value会被赋值，`ok`为`true`
如果键不存在，则value不会被赋值，`ok`为`false`

```go
value,ok := MyMap["name"]
```

###### **fmt**

fmt包为我们提供了几个非常常用的输出函数
```go
fmt.Println("Why?")
```
`fmt.Println`接受多个参数，将它们都输出出来，参数之间用空格分开，输出的末尾会自动切换到下一行
```go
name := "wjj"
age := 80
fmt.Printf("My name is %s,and my age is %d",name,age)
// 输出结果是
// My name is wjj,and my age is 80
```
`fmt.Printf`接受多个参数，第一个参数中的`%s``%d`为占位符，后面的`name``age`会去填充前面的占位符。显然，你前面有多少占位符，后面就应该有多少参数

```go
status := "on going"
info := fmt.Sprintf("Our project is %s",status)
```
`fmt.Sprintf` 和 `fmt.Printf`的用法一样，但是会把本来应该的输出作为`string`类型返回出来

> 不同的类型有不同的占位符，请为每个类型使用正确的占位符，常用占位符如下

> + 十进制整数  `%d`
> + 字符串 `%s`
> + 浮点数（小数） `%f`
> + 通配符 `%v`

###### 运算符
|运算符|意义|
|--|--|
|`+`|加法|
|`-`|减法|
|`*`|乘法|
|`/`|除法|
|`%`|取余|
|`|`|或，按位或|
|`&`|与，按位与|
|`^`|按位异或|

 <img src="warning.png" width="25px">go语言的运算符要求两个变量的类型相同，比如下面这个例子 

```go
a := 10
b := 2.2
c := float64(a) + b
// 那么c是float64类型，值为12.2

d := float(a) / b
e := a / int(b)
// d是float64类型，值为4.5454.....
// e是int类型，值为5
```

###### 分支结构
使用`if`关键字来进行分支结构，`if`的主要用法如下
```go
a := 100
if a < 100{
    fmt.Println("Hello World")
} else if a < 50 {
    fmt.Println("Hello Tenzor")
} else {
    fmt.Println("Ahhhhhh")
}
```
> 不同于其他语言，条件语句不需要加括号，但是`else`关键字必须紧跟在 `}` 所在的行

```go
var a int = 100
if a += 80;a < 200{
    fmt.Println(a)
}
```
> `if`关键字之后可以跟一个需要执行的语句，然后再跟上布尔值

使用`switch`关键字进行分支结构
```go
func main(){
    a := "技术部"
    switch a{
        case "技术部":{
            fmt.Println("tz-gin,vue")
        }
        case "美工部":{
            fmt.Println("ps,xd")
        }
        case "视频部":{
            fmt.Println("pr,ae")
        }
        default :{
            fmt.Println("你是什么部")
        }
    }
}
```


###### 循环结构
go语言使用`for`关键字进行循环结构，值得注意的是，go语言并没有`while`关键字，常见用法如下
```go
sum := 0
for i := 0;i<50;i++{
    sum += i
}
// 分号前第一个语句可以省略，中间是结束条件，后面是每次循环结束之后执行的语句

for {
    // infinite loop
}
// 可以用这个来执行无限循环
a := map[string]string{
    "name":"wjj",
    "password":"123456"
}

for key,value := range a{
    // code
}
// 使用range关键字遍历map或者数组
```

###### 定义函数
使用`func`关键字来定义函数，函数的传入值和传出值得类型可以是任意的，甚至连函数本身都可以作为参数传递给另一个函数。定义函数的范式如下：
```go
func UserInfo(name,password string,id int)string{
    // code
}

func Register(infos map[string]string,vip bool)(data string,ok bool){
    // code
}
```
当返回值只有一个值的时候，你可以不打括号，比如`UserInfo`函数，如果返回值有多个值，需要为返回值打括号，你可以为返回值命名，比如`Register`函数

go语言提供函数匿名函数，这使得在某些函数接受或者返回的类型也是函数时，能够很方便地编写，如下
```go
Anony := func(id int)string
```

###### 定义结构体
结构体可以将多个字段放在一个类型下方便使用，就像面向对象中的类一样，使用`struct`关键字创建结构体实例
```go
userInfo := struct{
    Name string
    College string
    Age int
}{
    Name:"wjj",
    College:"LZ",
    Age:80,
}
```
但是在大部分情况下，我们定义一个结构体类型都是会在多次使用的，所以可以使用`type`和`struct`关键字来定义结构体，然后可以像前面定义变量那样来实例化结构体
```go
type UserInfo struct{
    Name string
    College string
    Age int
}

func MyFunc(){
    info := UserInfo{
        Name:"syl".
        College:"Qian",
        Age:79,
    }
    fmt.Println(info)
}
```
结构体的字段我们也称之为结构体的属性。此外，我们可以像定义函数那样为结构体定义一些方法，这也是面向对象的思想。结构体的字段和方法可以继承，下面`Student`继承了`UserInfo`的属性

```go
type Student struct{
    UserInfo
    Name string
    password string
    Hometon string
}

func (s Student) Login(password string)bool{
    if password == s.password{
        return true
    }    
    return false
}

func (s Student) Say(){
    fmt.Printf("Hello,my name is %s",s.Name)
}
```
<img src="warning.png" width="25px">请注意结构体字段的命名，像变量的命名那样，小写字母开头的字段只能在结构体内部的方法中使用，比如上例中的`password`；而大写字母开头的字段可以在外部使用，比如`Name`

###### 指针

go语言的指针比较自由，向C语言一样，使用`&`来取变量的地址，使用`*`来对指针变量解引用，空指针的值为`nil`

<img src="warning.png" width=25>请尽可能避免空指针的出现，这个错误在结构体的字段为切片或者`map`类型的时候尤其容易出现

```go
type MyType struct{
    Info map[string]string
    Id int
}

func main(){
    data := MyType{}
    data.Info = make(map[string]string,0)
}
```

##### go语言进阶

###### panic和recover

**`defer`关键字**

`defer`关键字后面紧跟的代码，会在当前函数的其他部分执行完后最后执行。多个`defer`关键字时，按照先进后出原则，即越早出现的`defer`越晚执行

```go
func main(){
    fmt.Println(1)
    defer fmt.Println(2)
	defer fmt.Println(3)
}
```

> 会先输出1，再输出3，最后输出2

**`panic`和`recover`**

`panic`用于触发一个错误，`recover`用于捕获和恢复一个错误，当一个函数执行到`panic`时，会立刻终止，并逐层向上返回，知道程序退出运行或者被`recover`捕获，<img src="warning.png" width=25>值得注意的是，`recover`只在`defer`关键字中使用有效，并且这个`defer`定义在`panic`之前

`panic`接受和`recover`返回都是`interface{}`类型，所以可以向其中传入任意类型的参数

```go
func Sub() {
	fmt.Println("Hello World")
	panic("AN ERROR")
    fmt.Println("Ahhhhhhhhh")
}

func main() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered:", r)
		}
	}()
	Sub()
}
```

> `Sub`函数中触发的`panic`会向上返回，被主函数中定义的`defer`中的`recover`捕获，然后被恢复，所以这个程序输出是：
>
> Hello World
>
> Recovered:AN ERROR

###### 文件操作

**`byte`和`[]byte`类型**

`byte`是字节类型，一个`byte`类型的变量空间大小就是一个字节，也即8位。在特定的编码方式下，每个字符都有自己的字节码，在`UTF-8`编码中，一个英文字符占一个字节，一个汉字通常占3个字节，在不同的编码方式中则会有所差别。

<img src="warning.png" width=25> 一个文件使用什么编码方式保存，就应使用什么编码方式打开，否则就会出现乱码。现在大部分文件的编码方式都是`UTF-8`，你可以尝试用其他的编码方式打开你电脑中的文件，看看会出现什么结果

`[]byte`类型即`byte`的切片，在go语言中，`string`和 `[]byte`之间可以互相转换。go语言存储和打开文件都是通过字节码。

 <img src="question.png" width=25> go语言还提供了`rune`类型，可自行查阅

**文件的打开和关闭**

`os`包为我们提供了打开和关闭文件的方法

```go
func main(){
    f, err := os.Open("./hello.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()
	body, err := io.ReadAll(f)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(body))
}
```

> `os.Open`会返回一个`os.File`的指针类型，同时返回一个错误，`os.File` 可以作为`io.Reader`和`io.Writer`类型，于是我们使用`io.ReadAll`来读取文件的全部字节，这里以`.txt`类型为例，将它的全部字节转化为字符串输出出来。使用`Close`方法来关闭文件，请及时关闭文件

<img src="warning.png" width=25> `io.ReadAll`会把文件一次性读取出来，如果文件很大的话，将整个文件加载到内存当中可能会导致内存不足或者性能下降问题。对于较大的文件，更推荐使用`bufio`包来逐步读取文件

```go
func main(){
    f, err := os.Open("./hello.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()
	r := bufio.NewReader(f)
	buf := make([]byte, 1024)
	for {
		n, err := r.Read(buf)
		if err != nil && err.Error() != "EOF" {
			panic(err)
		}
		if n == 0 {
			break
		}
		fmt.Println(buf[:n])
	}
}
```

> `n`表示每次读取文件读出来的字节数，如果读取数量为0，那么说明文件读取完毕，可以退出循环

<img src="question.png" width=25>  `os`包提供了一种更一般性的打开文件的方式：`os.OpenFile`，可自行查阅

**文件和目录的创建**

`os`包为我们提供了创建文件和目录的方法，其中，在前缀目录不存在的时候`Mkdir`会报错，`MkdirAll`则会将不存在的前缀目录全部创建，`os.ModeDir`的类型请自行参阅官方文档

```go
func CreateAFile() {
	f, err := os.Create("./dir/test.go")
	defer f.Close()
	if err != nil {
		panic(err)
	}
}

func CreateADir() {
	err := os.Mkdir("./test", os.ModeDir)
	if err != nil {
		panic(err)
	}
}

func CreateAllDir() {
	err := os.MkdirAll("./dir/hello", os.ModeDir)
	if err != nil {
		panic(err)
	}
}

```

###### 接口

go语言提供了`interface`类型用来实现空接口，我们可以在接口中声明一些方法，然后实现了这些方法的结构体都可以称为这个接口。在函数中传入或者传出参数的时候，使用合适的接口类型可以让参数的类型更加多样化，因此，如果一个参数想要接受任意类型的参数，我们既可以使用`any`类型，也可以使用空接口`interface{}`

接口类型使得go语言能够更好的面向对象编程，这种编程思想在后端的开发中有很重要的指导意义

<img src="question.png" width="25px"> 可以在一些社区文档或者教程中看到面向对象的思想，这种思想能让你更好得理解一些源代码

```go
type Human interface {
	Say(msg string)
	Eat(food string) (ok bool)
}

type Student struct {
	Name string
}

func (s Student) Say(msg string) {
	fmt.Printf("My name is %s,I want to say %s\n", s.Name, msg)
}

func (s Student) Eat(food string) (ok bool) {
	if food == "apple" {
		fmt.Println("delicious")
		return true
	}
	fmt.Println("Ahhhhhhhh No!!!")
	return false
}

func (s Student) Sleep(){
    fmt.Println("I'm sleeping")
}

func Do(human Human) {
	human.Say("hello")
	human.Eat("U-235")
}

func main() {
	a := Student{Name: "wjj"}
	Do(a)
}
```
> 如上例，我们把能`Say`和`Eat`的对象成为`Human`，对于`Student`结构体来说，它实现了这两个方法，此外它还有自己独特的方法`Sleep`，所以它可以作为一个`Human`，因此可以作为参数传递给`Do`函数

接口可以继承，我们可以继承上面的`Human`接口来定义一个`Child`接口。于是，实现了`Say`,`Eat`,`Cry`方法的结构体都可以称为`Child`，显然`Student`由于没有实现`Cry`方法，所以不能称为`Child`
```go
type Child interface{
    Human
    Cry()
}
```
接口类型的变量可以承接任意类型的变量，这在后面的开发中会非常使用。我们可以对接口类型的变量进行类型断言，进而使用它的一些属性和方法

```go
var stu interface{}
data,ok := stu.(Student)
if ok{
    fmt.Println("It's a student")
} else {
    fmt.Println("It's not a student")
}
```

> 这里的`stu`变量显然是一个空接口，不能作为`student`类型，所以`ok`的值是`false`，如果类型断言成功，`ok`的值为`true` ，那么就可以使用`student`类型的属性和方法

<img src="question.png" width="25px"> 在go语言中有两个接口很重要`io.Reader`和`io.Writer`，建议查资料了解一下，对于后面 `gin` 框架的编写很有帮助 

######   并发编程

**<img src="question.png" width=25>进程，线程和协程** 

进程的定义如下

> 进程是一个具有一定独立功能的程序在一个数据集合上依次动态执行的**过程**。进程是一个正在执行的程序的实例，包括程序计数器、寄存器和程序变量的当前值。

进程是操作系统资源分配的基本单位，拥有独立的地址空间，你可以在任务管理器中查看自己的电脑正在运行的进程。通常情况下一个进程崩溃后，并不会影响到其他进程

线程是进程的一部分，一个进程至少拥有一个线程，线程是处理器任务调度和执行的基本单位。一个进程的线程之间共享它们的进程的地址空间，一个线程的崩溃有可能导致整个进程的崩溃

go语言天然支持并发编程。值得注意的是，go语言的进程是一种轻量级的goroutine，并且在go语言中进行协程管理非常便捷，这使得`gin`框架在后端的并发情景处理中有着独特的优势

**`go func`**

go语言提供的go关键字可以很方便的开协程，配合匿名函数，完成一些并发编程就变得十分容易

```go
func main(){
    go func(){
        for i := 0;i<5;i++{
        	fmt.Println("Hello World")
        }
    }()
    time.Sleep(5*time.Second)
}
```

<img src="warning.png" width=25> `time.Sleep(5*time.Second)`指让程序休眠5秒，因为`main`包中的`main`函数所在的协程为主协程，主协程结束运行之后，其他的协程也会立即结束，所以在这里我们通过让程序休眠的方式来让`go`关键字开的协程执行完毕，在后面我们有一些其他方法来达到这个目的

这种开启协程的方式常用且方便，比如在后端程序运行的过程中想要定时发送消息，就可以通过开一个协程来实现

**`sync`包**

`sync`包是一个go的标准库，它包含的一些类型和函数可以让我们很方便的进行协程管理

```go
func main() {
	wg := sync.WaitGroup{}
	wg.Add(2)
	go func() {
		for i := 0; i < 100; i++ {
			fmt.Println("Hello")

		}
		wg.Done()
	}()
	go func() {
		for i := 0; i < 100; i++ {
			fmt.Println("World")
		}
		wg.Done()
	}()
	wg.Wait()
}
```

> 使用`sync.WaitGroup`类型及其方法可以让主协程等待子协程执行完毕之后在结束主协程，可以看到输出结果是`Hello`和`World`加菩提出现，但是它们并没有一个明确的顺序，这说明这两个循环是同时执行的
>
> <img src="warning.png" width=25> 请务必保证`wg.Add` 增加的数量和`wg.Done`的数量相同，否则会导致线程阻塞

##### net/http包

##### gin框架基础

gin框架是在`net/http`包的基础上搭建起来的，简单易上手，支持中间件，下面是一个简单的示例代码

```go
func main() {
	r := gin.Default()
	r.GET("/example", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"msg": "hello gin!",
		})
	})
	r.Run("127.0.0.1:8080")
}
```

> 变量`r`是一个路由处理器，我们定义了一个`GET`方式的接口，通过匿名函数的方式为它分配了路由处理函数。gin框架中的路由处理函数是`func(*gin.Context)`类型，`gin,Context`是上下文，后面会讲到。这个应用运行在`127.0.0.1:8080`上，可以通过Apifox或者其他调试工具来进行测试

##### 数据库，SQL和gorm基础

##### 使用tz-gin开发

##### gorm进阶 

##### 其他的常用包 

**`errors`**
