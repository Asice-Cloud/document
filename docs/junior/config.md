#### <span id="config">入门篇其3-开发环境和基础平台配置</span>

> [!NOTE]
>
> 本章作者：syl+wjj
>
> 难度：⭐
>
> 涉及语言：无



##### 开发平台选择：

> ​	<img src="assets/awesomeface.png" width="25px">推荐Arch Linux或者Ubuntu作为开发环境，当然我们培训是基于windows开展的。



**编辑器和IDE**
$$
编辑器 \neq IDE！
$$

    编辑器是程序员⽤于编写和修改源代码的软件⼯具。它提供了⽂本编辑的基本功能，如插⼊、删除、复制和粘贴等，以及针对编程语⾔的特定功能，如语法⾼亮、代码折叠和⾃动完成等。本⾝并不参与代码的执⾏和转换，如vscode，记事本。


    IDE是⼀种集成了多种开发⼯具和功能的软件应⽤程序，旨在提⾼软件开发的效率和质量。它通常包括源代码编辑器、编译器、调试器、构建⼯具、版本控制系统等，为程序员提供了⼀个全⾯的开发环境。集成了多种开发⼯具，⽅便程序员在同⼀个界⾯下完成开发任务。提供了丰富的功能和插件，满⾜不同开发需求。⽀持代码⾃动完成、语法⾼亮、代码重构等，提⾼编程效率和质量。可以⾃动管理代码库、构建⼯具和⽂档等，减少⼿动操作的时间和错误。如Visual Studio，IDEA，Pycharm。

<img src="assets/question.png" width = "25px"> 我们在入门过程中不需要完全理解编译器的原理，而是选择使用合适的编辑器或者IDE来开发项目。我们推荐使用vscode来进行开发工作。



##### 编辑器vscode 配置

使用记事本来写代码显示我们太逊了:innocent:，我们需要一个更酷炫更方便的开发工具。

这里推荐大家使用 `Visual Studio Code` 编辑器，先到其[官网下载](https://code.visualstudio.com/)安装。选择适合自己电脑的发行版进行安装。windows就一条龙到底就行了。记得选择添加到PATH中，这样方便以后在终端直接 `code .`打开这个项目文件夹。桌面快捷方式可以自行选择是否创建。

<img src="assets/vsc1.png" width = 500px>

> <img src="assets/awesomeface.png" width="25px">有关 vscode 可以看我们B站的一个视频了解一下。为什么 Visual Studio Code 被誉为 IDE 中最强的男人：https://www.bilibili.com/video/BV13v411w7Fb

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

**简单的配置启动HTML**

在插件市场搜索并下载一些插件，下面是一些常用的开发html的插件，当然你也可以自行下载：

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

<img src="assets/sys1.png" width=800px>

点击“环境变量”选项后，可以设置变量名和值。

<img src="assets/sys2.png" width=800px> 

完成以后点击确定，就可以保存到环境变量了:blush:



##### 更多的开发工具

我们上网冲浪的时候，经常会看到好多人在吵用什么工具写程序是最好的。下面是全网统计的编译器/IDE受欢迎图：

<img src="assets/rank.png">

​	但是 :cold_sweat: `visual studio`太重了！！而且vs主要经营.Net的开发和调试，也不是我们的主力语言。相比之下`vscode`便捷而且拥有海量插件，配置的好的话也不会比vs差到哪去。

​	<img src="assets/bulb.png" width=25px>不过市场上其他的编译器和IDE同样值得推荐，比如Jetbrains全家桶中的idea(收费，建议使用学信网去申请个教育包)，vim(门槛较高)，用起来也是很爽的。IDE的好处是开盖即用，不需要再过多配置，但是可能比较重而且不够自由。
