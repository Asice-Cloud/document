<h1 align="center">做e时代的主人</h1>

#### 前言

###### <img src="awesomeface.png" alt="welcome" width="29px">[注:这不仅是一份预习文档，也可以当作以后学习期间的长期方向指导]

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



#### 章节列表

<h6><b>入门篇</b></h6>

1. 你好, 0和1的世界
2. 网页是什么(上):元素
3. 开发环境(IDE editor environment)和基础平台配置(windows PATH)
4. 变量与类型(上):基本类型
5. 何为函数

<h6><b>进阶篇</b></h6>

1. 变量与类型(下):指针和自定义类型
2. 编程思想浅谈
3. 了解网络协议和应用
4. 同步与异步

<h6><b>实战篇</b></h6>

1. 网页是什么(下):前端和后端
2. 前后端通用工具简介
3. 前端学习浅谈和开发规范
4. 后端学习浅谈和开发规范





<h4>入门篇其3 开发环境和基础平台配置</h4>



1. ###### **开发平台选择：**

> ​	<img src="awesomeface.png" width="25px">推荐Arch Linux或者Ubuntu作为开发环境，当然我们培训是基于windows开展的。



<h5>编译器，编辑器和IDE</h5>


$$ {<img src="warning.png}
编译器 \neq IDE！
$$




	编译器是将源代码转换为可执行程序的工具，比如gcc,llvm,go build等。编译器通过多个阶段（如词法分析、语法分析、语义分析、代码⽣成等）将源代码转换成可执⾏⽂件或库。特点是可以⼀次性转换整个源代码。可以进⾏语法和语义检查，提⾼代码质量。⽣成的代码执⾏效率⾼，但编译过程可能耗时较⻓。


	s编辑器是程序员⽤于编写和修改源代码的软件⼯具。它提供了⽂本编辑的基本功能，如插⼊、删除、复制和粘贴等，以及针对编程语⾔的特定功能，如语法⾼亮、代码折叠和⾃动完成等。本⾝并不参与代码的执⾏和转换，如vscode，记事本。


	IDE是⼀种集成了多种开发⼯具和功能的软件应⽤程序，旨在提⾼软件开发的效率和质量。它通常包括源代码编辑器、编译器、调试器、构建⼯具、版本控制系统等，为程序员提供了⼀个全⾯的开发环境。集成了多种开发⼯具，⽅便程序员在同⼀个界⾯下完成开发任务。提供了丰富的功能和插件，满⾜不同开发需求。⽀持代码⾃动完成、语法⾼亮、代码重构等，提⾼编程效率和质量。可以⾃动管理代码库、构建⼯具和⽂档等，减少⼿动操作的时间和错误。如Visual Studio，IDEA，Pycharm。

<img src="question.png" width = "25px"> 我们在入门过程中不需要完全理解编译器的原理，而是选择使用合适的编辑器或者IDE来开发项目。我们推荐使用vscode来进行开发工作。



2. ###### **vscode 配置**

使用记事本来写代码显示我们太逊了:innocent:，我们需要一个更酷炫更方便的开发工具。

这里推荐大家使用 `Visual Studio Code` 编辑器，先到其[官网下载](https://code.visualstudio.com/)安装。选择适合自己电脑的发行版进行安装。windows就一条龙到底就行了。记得选择添加到PATH中，这样方便以后在终端直接 `code .`打开这个项目文件夹。桌面快捷方式可以自行选择是否创建。

<img src="file:////home/asice-cloud/.config/QQ/nt_qq_84aeb657cd7aefe6cae59ed118656127/nt_data/Pic/2024-08/Ori/4db79ce448bbc7ce6be65e148495387c.png" width = 500px>

> <img src="awesomeface.png" width="25px">有关 vscode 可以看我们B站的一个视频了解一下。为什么 Visual Studio Code 被誉为 IDE 中最强的男人：https://www.bilibili.com/video/BV13v411w7Fb

现在我们已经完成了软件的安装。但是打开vscode的话里面还是空空的，因为它本身只是一个文本编辑器，我们需要安装一些插件来让它变得强大(:yum:vscode补全计划)



下面我们以配置html开发环境为例，其他语言如何配置可以查阅相关文档。先介绍vscode上几个常用组件。

##### 插件市场

vscode 自身的产品思路就是一个轻量级的开发工具加上繁荣开放的插件市场组成。因此很多强大的功能需要通过安装插件来实现，目前 vscode 的插件市场中已经有着几万个插件。通过 `侧边栏上的按钮` 或快捷键 `Ctrl + Shift + X` 打开 vscode 的插件市场。

<img src="https://qiniu.3yya.com/ca3a892f5d5cca90adaaf101a0504e0a/ca3a892f5d5cca90adaaf101a0504e0a.png" width=500px>

##### 命令面板

vscode 的命令面板能让我们快速方便地执行很多功能与命令，包括自身的设置和插件提供的功能等。

通过 `View -> Command Palette` 或者快捷键 `Ctrl + Shift + P` 可以打开命令面板。

<img src="https://qiniu.3yya.com/085039b5ebd66fa5b0e927d5ff803707/085039b5ebd66fa5b0e927d5ff803707.png" width = 500px>

##### 配置面板

通过 `File -> Preferences -> Settings` 或 `Ctrl + ,` 打开配置面板。

<img src="https://qiniu.3yya.com/230cb699debabe62f5a05afc42077fbc/230cb699debabe62f5a05afc42077fbc.png" width=500px>

##### 简单的配置

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



###### **3.系统变量设置**

我们经常需要将某些路径添加到系统变量中，这样方便我们可以快速调用它们。下面以windows平台为例，演示如何添加环境变量。

<img src="file:////home/asice-cloud/.config/QQ/nt_qq_84aeb657cd7aefe6cae59ed118656127/nt_data/Pic/2024-08/Thumb/441719610a5ce4dd844e9068e047b31e_720.png" width=800px>

点击“环境变量”选项后，可以设置变量名和值。

<img src="file:////home/asice-cloud/.config/QQ/nt_qq_84aeb657cd7aefe6cae59ed118656127/nt_data/Pic/2024-08/Ori/65875d7c2a0a4b09d8f3a482d7afdc48.png" width=800px> 

完成以后点击确定，就可以保存到环境变量了:blush: