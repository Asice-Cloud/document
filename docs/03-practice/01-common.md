#### <span id="common">实践篇其 1 - 通用工具介绍</span>

> [!NOTE]
>
> 本章作者：wjj + cgy
>
> 难度：⭐⭐
>
> 涉及语言：shell



##### <img src="../../assets/gitlogo.jpg" width=30> git

在介绍 `git` 之前，我们不妨先从 **代码托管平台** 开始说起。世界上最大最热门的代码托管平台，当然要数 `Github`，你可以从上面下载项目源代码、一些课程资料等等等等。国内也有类似的平台比如 `Gitee (码云，全是广告)`，`Gitcode（'自主研发'的 sb 玩意）` 等。

<img src="../../assets/bulb.png" width=25> 你可以为自己注册 `Github` 账号，并通过平台的学生认证，然后你就可以免费使用一些付费软件或者网站了，比如 `jetbrains` 系列，`overleaf`。  

想要在这些平台上下载资源，我们就需要使用到 `git` 工具。事实上，`git` 是一个版本控制工具，概括起来，就是实现开发者本地仓库与远程仓库之间的文件互传等操作。你可以在 <a href="https://git-scm.com/downloads">这个网址</a> 来下载 `git`，然后按照下面推荐的流程进行安装（仅以 windows 为例）

<img src="../../assets/setup1.png" width=400>

<img src="../../assets/setup2.png" width=400>

<img src="../../assets/setup3.png" width=400>

关于 `git` 的使用教学，我们在这里只举几个简单的例子，深入的学习可以参考 <a href="https://git-scm.com/docs">推荐文档</a> 来进行学习，当然，网上相关的教程也是很多的。

当你想要创建一个新项目的时候，在 `powershell` 中按照如下流程：

```shell
#shell
cd <你的项目文件夹目录>
git init
git config user.name <你的用户名>
git config user.email <你的邮箱>
git remote add <你的仓库url>.git

// 然后你对你的项目进行了更新，想要提交到仓库
git add ./
git commit -m "<你的提交信息>"
git push <remote name> <分支>
```

当你想要下载某个仓库的时候

```shell
#shell
git clone <仓库url>.git
```

<img src="../../assets/awesomeface.png" width=25> 文档看得太累了怎么办，还是打会儿 <a href="https://learngitbranching.js.org/?locale=zh_CN">游戏</a> 吧，一个挺有意思的 git 学习小游戏。

##### <img src="../../assets/apifoxlogo.png" width=30> apifox

`apifox` 是一个国内开发的免费的接口调试工具，非常适合个人和团体使用。前后端都可以使用它来检查接口是否能正常运行，处理返回值。在项目中开发过程中，合适的接口调试工具会让开发轻松很多，类似的工具还有 `postman`，`swagger` 等等。你可以在 <a href="https://apifox.com/">apifox 的官网</a> 来获取

`apifox` 提供了一个示例项目用于学习，同时你也可以参阅 <a href="https://apifox.com/help/">官方文档</a> 获取帮助，~~他们甚至提供了视频~~

##### <img src="../../assets/navicatlogo.png" width=30> Navicat

`Navicat` 是一个可以图形化操作 `MySQL` 的工具，在命令行操作数据库毕竟是一件比较费眼睛的事情，图形化的界面会方便很多。我们在后端的开发和部署时会频繁地用到它。此外 `Navicat` 支持操作多种数据库，比如 `MongoDB`，`SQL Server`，`Redis` 等等。这样强大的工具是需要付费的，所以我们也推荐一些其他的工具，如 <a href="https://dbeaver.io/download/">`DbServer`</a>，它提供了免费的社区版。

你可以在 <a href="https://navicat.com.cn/products">官网</a> 来下载 `Navicat`。

在操纵 `MySQL` 的时候，首先你需要和你的 `MySQL` 建立连接，如图所示：~~请忽略掉我已经建立的连接~~

<img src="../../assets/cat2.png" width=400>

然后你可以在一个连接中建立数据库，如图所示。对于一个独立的项目来说，建立独立的数据库显然是很有必要的

<img src="../../assets/cat1.png" width=400>

如果你要使用 `MySQL` 来进行一些操作，在上方菜单中点击查询，然后新建查询，就可以了，如图所示

<img src="../../assets/cat3.png" width=400>

具体的使用方法，可以参考 <a href="https://www.navicat.com.cn/manual/online_manual/cn/navicat_16/win_manual/">官方文档</a> 获取帮助。

<img src="../../assets/linux.jpg" width=30> **GNU/Linux (仅了解)**

GNU/Linux 是对一系列基于 Linux 内核和 GNU 组件的发行版的统称，一般称作 Linux 即可。现今大多数服务器都运行着免费、稳定的 Linux 操作系统，而且对于开发者而言，Linux 下的工具链往往更为完整，开发环境的配置与 Windows 相比也简单太多。Linux 操作多数基于命令，即你在终端中输入命令，操作系统便能精准地明白你的意思，然后执行你交代的任务。这里只简要介绍一些入门的操作，更深入的了解可参考[中科大 Linux 101](https://101.lug.ustc.edu.cn/)。有些命令不知道是用来干嘛的的不要紧，后续接触的多了就能理解了。

【简单上手：Windows 推荐 WSL】

搜索栏中搜索“启用或关闭 Windows 功能”，打开“适用于 Linux 的 Windows 子系统"和"Hyper-V"，重启后在 powershell 中运行命令

```powershell
wsl --install    # 安装 wsl 的命令，默认会安装 Ubuntu，对新手友好
```

如果连接不上服务器可在 Microsoft Store 中搜索 Ubuntu 安装。

安装好后可在 Powershell 中运行命令 `wsl` 或开始菜单中打开应用 `Ubuntu`，即进入 Linux 命令行（wsl 默认不包含图形界面）。

【常用操作】
- 路径与导航
```bash
pwd                 # print working directory，会打印出你当前所处位置
ls                  # 列出当前位置的文件
cd ..               # change directory 改变当前所处位置
mkdir proj          # 新建目录（文件夹）
```
- 文件与查看
```bash
touch README.md             # 新建一个名为 README.md 的文件，若存在则只 touch 它一下（修改时间更新内容不变）
cp -r src dst               # cp 表示 copy, -r 表示递归（也会复制子目录），复制 src 目录到 dst 目录
mv object destination       # move 移动文件/目录
rm -r danger                # remove，-r 同上表示递归，小心使用，回车前看清路径，删除后很难恢复
cat file | less             # cat 会输出文件所有内容，less 接收这些内容并允许用户翻页查看
```
- 压缩与解压
```bash
# c-compress x-extract
tar -czvf archive.tar.gz dir/        # 将目录压缩为 tar.gz（常用）
tar -xzvf archive.tar.gz             # 解压 tar.gz 到当前目录
tar -xzvf archive.tar.gz -C target/  # 解压到指定目录

tar -cjvf archive.tar.bz2 dir/       # 使用 bzip2 压缩
tar -xjvf archive.tar.bz2            # 解压 tar.bz2

tar -cJvf archive.tar.xz dir/        # 使用 xz 压缩
tar -xJvf archive.tar.xz             # 解压 tar.xz

zip -r archive.zip dir/              # 压缩为 zip（跨平台常见）
unzip archive.zip -d target/         # 解压到指定目录

gzip -k file                         # 单个文件 → file.gz（-k 保留原文件）
gunzip file.gz                       # 解压 .gz
```
- 搜索与定位
```bash
grep -Rni "TODO" .          # 代码里找关键字
find . -name "*.go"         # 按名字找文件
```
- 权限与 sudo
```bash
ls -l               # 列出的同时显示权限（rwx read write execute)
chmod +x run.sh     # change mode，x 表示 execute，给 run.sh 添加可执行权限
sudo <命令>         # 临时以管理员身份执行某命令
```
- 包管理（Ubuntu/Debian）
```bash
sudo apt search docker       # 查找某一软件包
sudo apt install docker.io   # 安装指定软件包
sudo apt remove docker.io    # 删除指定软件包
sudo apt upgrade             # 更新所有软件包
```
- 进程与网络
```bash
ps aux | grep myapp       # 找进程，grep 接收 ps 的输出结果并筛选出含 "myapp" 的信息
kill 12345                # 结束（杀死）进程
curl https://example.com  # 获取一个网站的信息，类似于你用浏览器访问该网站的过程
```

- 编辑器怎么选
  - nano：命令 `nano <filename>` 即可开始编辑，底部有命令提示
  - vim：学习曲线陡峭，基本使用：命令 `vi <filename>` 或 `vim <filename>` 打开文件，打开时会处于 NORMAL 模式，`i` 进入 INSERT 模式来编辑；`Esc` 退出 INSERT 模式，回到 NORMAL 模式， `:wq` 保存退出
  - VS Code：有人称其为宇宙第一编辑器，功能强大且易用，有友好的图形化界面


