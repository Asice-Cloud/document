#### <span id="compile">实践篇其 3 - 从零开始的代码编译原理</span>

> [!NOTE]
>
> 本章作者：wjj + syl
>
> 难度：⭐⭐⭐⭐⭐
>
> 涉及语言：shell, Go, javascript



##### 为什么需要编译

并不是所有语言的源代码都可以直接运行，通常我们会把语言分为高级语言、低级语言、机器语言。机器语言由二进制代码组成，计算机可以直接使用，但是让开发者使用这种语言显然是不可能的。我们目前接触到的语言几乎都是高级语言，它们更接近人类的语言，并且能让开发者将精力集中在程序开发上，而不必在程序运行底层的一些细节上纠结。汇编语言是一种低级语言，它比高级语言要更加接近计算机硬件。

高级语言源代码并不能直接运行，而是要转化成某种机器看得懂的代码。对于在操作系统上运行的代码，应该转化为汇编代码，而对于在虚拟机上运行的代码，则应该转化为一些中间代码，比如字节码。编译就是进行这个过程。

比如我们后端使用的 Go 语言，就需要编译成机器码才能运行。Go 语言的工具包里提供了编译的工具，可以使用命令 `go bulid` 来对代码进行编译，也可以在编译的时候添加参数，即 [build flags] 位置上可以填写的参数：

```shell
#shell
go build [build flags] [packages]
```

<img src="assets/bulb.png" width=25px>大家可以自行查阅可以添加的编译相关参数，如 -gcflags=-S 会输出汇编等。 

当然了，在开发过程中，我们也可以使用 `go run <文件名>` 来编译运行了，它会生成一个临时的可执行文件。



##### 编译的过程

想要从源代码生成可执行文件并不是一件容易的事。对于在操作系统运行的程序，比如 C 语言的程序，要经历预处理、编译、汇编、链接四个过程。

<img src="assets/ccom.png">

**预处理**：在这个阶段，预处理器将源代码中的预处理指令（如 `#include`、`#define` 等）替换为实际的内容。预处理器会根据指令展开头文件，处理宏定义，并删除注释等。

**编译**：编译器将预处理后的源代码转换为汇编代码。它会对每个源文件进行词法分析、语法分析和语义分析，生成相应的中间代码，并进行优化。

**汇编**：汇编器将编译生成的中间代码转换为机器可读的汇编代码，也就是机器码的文本表示。这个阶段将源代码转换为机器语言的汇编指令，但还没有生成可执行文件。

**链接**：链接器将汇编生成的目标文件以及可能的库文件链接在一起，生成最终的可执行文件。它会解析各个目标文件之间的符号引用和符号定义关系，将它们合并成一个完整的程序。

对于在虚拟机运行的程序，大致按照下面的流程。这里的前端和后端，当然不再是狭义的网络开发中的前端和后端了。编译过程中，还会对代码进行一些优化，比如乘法一般会被优化成位移，来提高程序的性能。

<img src="assets/compilepro.png">

<img src="assets/compile.png">

你可能暂时不太理解每个细节，没有关系，先通过上面图片的大标题，感受一下编译的过程。<img src="assets/question.png" width=25px>下面我们将会对 Go 以及 javascript 的编译流程进行简单讲述，当然不要求读者完全掌握。



##### Go 语言的编译

​	这是 Go 官方介绍自己的编译器的网址，https://go.dev/src/cmd/compile/README，感兴趣可以看一看。我们下面具体讲一下 Go 编译器是如何工作的。先看几个 <span id="pre">前置知识</span>。



###### 抽象语法树

​	[抽象语法树](https://en.wikipedia.org/wiki/Abstract_syntax_tree)（Abstract Syntax Tree、AST），是源代码语法的结构的一种抽象表示，它用树状的方式表示编程语言的语法结构 [1](https://draveness.me/golang/docs/part1-prerequisite/ch02-compile/golang-compile-intro/#fn:1)。抽象语法树中的每一个节点都表示源代码中的一个元素，每一棵子树都表示一个语法元素，以表达式 `2 * 3 + 7` 为例，编译器的语法分析阶段会生成如下图所示的抽象语法树（<img src="assets/awesomeface.png" width=25px>看起来很像中缀树...）。下面是一个简单表达式的抽象语法树。

![abstract-syntax-tree](https://img.draveness.me/2019-12-20-15768548776645-abstract-syntax-tree.png)

作为编译器常用的数据结构，抽象语法树抹去了源代码中不重要的一些字符 - 空格、分号或者括号等等。编译器在执行完语法分析之后会输出一个抽象语法树，这个抽象语法树会辅助编译器进行语义分析，我们可以用它来确定语法正确的程序是否存在一些类型不匹配的问题。



###### 静态单赋值

[静态单赋值](https://en.wikipedia.org/wiki/Static_single_assignment_form)（Static Single Assignment、SSA）是中间代码的特性，如果中间代码具有静态单赋值的特性，那么每个变量就只会被赋值一次。在实践中，我们通常会用下标实现静态单赋值，这里以下面的 Go 代码举个例子：

```go
x := 1
x := 2
y := x
```

经过简单的分析，我们就能够发现上述的代码第一行的赋值语句 `x := 1` 不会起到任何作用。下面是具有 SSA 特性的中间代码，我们可以清晰地发现变量 `y_1` 和 `x_1` 是没有任何关系的，所以在机器码生成时就可以省去 `x := 1` 的赋值，通过减少需要执行的指令优化这段代码。

```go
x_1 := 1
x_2 := 2
y_1 := x_2
```

因为 SSA 的主要作用是对代码进行优化，所以它是编译器后端的一部分；当然代码编译领域除了 SSA 还有很多中间代码的优化方法，编译器生成代码的优化也是一个古老并且复杂的领域（俗称编程界的黑魔法），这里就不会展开介绍了。



###### 指令集

最后要介绍的一个前置知识就是指令集了，很多开发者在都会遇到在本地开发环境编译和运行正常的代码，在生产环境却无法正常工作，这种问题背后会有多种原因，而不同机器使用的不同指令集可能是原因之一。

我们大多数开发者都会使用 x86_64 的 linux 作为工作上主要使用的设备，在命令行中输入 `uname -m` 就能获得当前机器的硬件信息：

```bash
$ uname -m
x86_64
```

x86 是目前比较常见的指令集，除了 x86 之外，还有 arm 等指令集，不同的处理器使用了不同的架构和机器语言，所以很多编程语言为了在不同的机器上运行需要将源代码根据架构翻译成不同的机器代码。

复杂指令集计算机（CISC）和精简指令集计算机（RISC）是两种遵循不同设计理念的指令集，从名字我们就可以推测出这两种指令集的区别：

- 复杂指令集：通过增加指令的类型减少需要执行的指令数；
- 精简指令集：使用更少的指令类型完成目标的计算任务；

早期的 CPU 为了减少机器语言指令的数量一般使用复杂指令集完成计算任务，这两者并没有绝对的优劣，它们只是在一些设计上的选择不同以达到不同的目的。



###### Go 编译原理

Go 语言编译器的源代码在 [`src/cmd/compile`](https://github.com/golang/go/tree/master/src/cmd/compile) 目录中，目录下的文件共同组成了 Go 语言的编译器，学过编译原理的人可能听说过编译器的前端和后端，编译器的前端一般承担着词法分析、语法分析、类型检查和中间代码生成几部分工作，而编译器后端主要负责目标代码的生成和优化，也就是将中间代码翻译成目标机器能够运行的二进制机器码。 编译原理的核心过程如下所示。

![complication-process](https://img.draveness.me/2019-12-20-15768548776662-complication-process.png)

Go 的编译器在逻辑上可以被分成**四个阶段**：**词法与语法分析**、**类型检查**和 **AST 转换**、**通用 SSA 生成**和最后的**机器码生成**。



###### 词法与语法分析 

所有的编译过程其实都是从解析代码的源文件开始的，词法分析的作用就是解析源代码文件，它将文件中的字符串序列转换成 Token 序列，方便后面的处理和解析，我们一般会把执行词法分析的程序称为词法解析器（lexer）。

而语法分析的输入是词法分析器输出的 Token 序列，语法分析器会按照顺序解析 Token 序列，该过程会将词法分析生成的 Token 按照编程语言定义好的文法（Grammar）自下而上或者自上而下的规约，每一个 Go 的源代码文件最终会被归纳成一个 [SourceFile](https://golang.org/ref/spec#Source_file_organization) 结构：

```go
SourceFile = PackageClause ";" { ImportDecl ";" } { TopLevelDecl ";" } .
```

词法分析会返回一个不包含空格、换行等字符的 Token 序列，例如：`package`, `json`, `import`, `(`, `io`, `)`, …，而语法分析会把 Token 序列转换成有意义的结构体，即语法树：

```go
"json.go": SourceFile {
    PackageName: "json",
    ImportDecl: []Import{
        "io",
    },
    TopLevelDecl: ...
}
```



Token 到上述抽象语法树（AST）的转换过程会用到语法解析器，每一个 AST 都对应着一个单独的 Go 语言文件，这个抽象语法树中包括当前文件属于的包名、定义的常量、结构体和函数等。

> Go 语言的语法解析器使用的是 LALR(1) 的文法，对解析器文法感兴趣的读者可以在推荐阅读中找到编译器文法的相关资料。

![golang-files-and-ast](https://img.draveness.me/2019-12-20-15768548776670-golang-files-and-ast.png)

<img src="assets/bulb.png" width=25px>值得注意的是，语法解析的过程中发生的任何语法错误都会被语法解析器发现并将消息打印到标准输出上，整个编译过程也会随着错误的出现而被中止。



###### 类型检查 

当拿到一组文件的抽象语法树之后，Go 语言的编译器会对语法树中定义和使用的类型进行检查，类型检查会按照以下的顺序分别验证和处理不同类型的节点：

1. 常量、类型和函数名及类型；
2. 变量的赋值和初始化；
3. 函数和闭包的主体；
4. 哈希键值对的类型；
5. 导入函数体；
6. 外部的声明；

通过对整棵抽象语法树的遍历，我们在每个节点上都会对当前子树的类型进行验证，以保证节点不存在类型错误，所有的类型错误和不匹配都会在这一个阶段被暴露出来，其中包括：结构体对接口的实现。

类型检查阶段不止会对节点的类型进行验证，还会展开和改写一些内建的函数，例如 make 关键字在这个阶段会根据子树的结构被替换成 [`runtime.makeslice`](https://draveness.me/golang/tree/runtime.makeslice) 或者 [`runtime.makechan`](https://draveness.me/golang/tree/runtime.makechan) 等函数。下图为类型检查阶段对 make 进行改写。

![golang-keyword-make](https://img.draveness.me/2019-12-20-15768548776677-golang-keyword-make.png)

<img src="assets/bulb.png" width=25px>类型检查这一过程在整个编译流程中还是非常重要的，Go 语言的很多关键字都依赖类型检查期间的展开和改写。



###### 中间代码生成

当我们将源文件转换成了抽象语法树、对整棵树的语法进行解析并进行类型检查之后，就可以认为当前文件中的代码不存在语法错误和类型错误的问题了，Go 语言的编译器就会将输入的抽象语法树转换成中间代码。

在类型检查之后，编译器会通过 [`cmd/compile/internal/gc.compileFunctions`](https://draveness.me/golang/tree/cmd/compile/internal/gc.compileFunctions) 编译整个 Go 语言项目中的全部函数，这些函数会在一个编译队列中等待几个 Goroutine 的消费，并发执行的 Goroutine 会将所有函数对应的抽象语法树转换成中间代码。下图为并发编译过程

![concurrency-compiling](https://img.draveness.me/2019-12-20-15768548776685-concurrency-compiling.png)

<img src="assets/bulb.png" width=25px>由于 Go 语言编译器的中间代码使用了 SSA 的特性，所以在这一阶段我们能够分析出代码中的无用变量和片段并对代码进行优化



###### 机器码生成

Go 语言源代码的 [`src/cmd/compile/internal`](https://github.com/golang/go/tree/master/src/cmd/compile/internal) 目录中包含了很多机器码生成相关的包，不同类型的 CPU 分别使用了不同的包生成机器码，其中包括 amd64、arm、arm64、mips、mips64、ppc64、s390x、x86 和 wasm，其中比较有趣的就是 WebAssembly（Wasm）了。

作为一种在栈虚拟机上使用的二进制指令格式，它的设计的主要目标就是在 Web 浏览器上提供一种具有高可移植性的目标语言。Go 语言的编译器既然能够生成 Wasm 格式的指令，那么就能够运行在常见的主流浏览器中。

```bash
$ GOARCH=wasm GOOS=js go build -o lib.wasm main.go
```

我们可以使用上述的命令将 Go 的源代码编译成能够在浏览器上运行 WebAssembly 文件，当然除了这种新兴的二进制指令格式之外，Go 语言经过编译还可以运行在几乎全部的主流机器上，不过它的兼容性在除 Linux 和 Darwin 之外的机器上可能还有一些问题，例如：Go Plugin 至今仍然不支持 Windows。下图为 Go 语言支持的架构。

![supported-hardware](https://img.draveness.me/2019-12-20-15768548776695-supported-hardware.png)



###### 编译器入口

Go 语言的编译器入口在 [`src/cmd/compile/internal/gc/main.go`](https://github.com/golang/go/blob/master/src/cmd/compile/internal/gc/main.go) 文件中，其中 600 多行的 [`cmd/compile/internal/gc.Main`](https://draveness.me/golang/tree/cmd/compile/internal/gc.Main) 就是 Go 语言编译器的主程序，该函数会先获取命令行传入的参数并更新编译选项和配置，随后会调用 [`cmd/compile/internal/gc.parseFiles`](https://draveness.me/golang/tree/cmd/compile/internal/gc.parseFiles) 对输入的文件进行词法与语法分析得到对应的抽象语法树：

```go
func Main(archInit func(*Arch)) {
    ...

    lines := parseFiles(flag.Args())
```

得到抽象语法树后会分九个阶段对抽象语法树进行更新和编译，就像我们在上面介绍的，抽象语法树会经历类型检查、SSA 中间代码生成以及机器码生成三个阶段：

1. 检查常量、类型和函数的类型；
2. 处理变量的赋值；
3. 对函数的主体进行类型检查；
4. 决定如何捕获变量；
5. 检查内联函数的类型；
6. 进行逃逸分析；
7. 将闭包的主体转换成引用的捕获变量；
8. 编译顶层函数；
9. 检查外部依赖的声明；

对整个编译过程有一个顶层的认识之后，我们重新回到词法和语法分析后的具体流程，在这里编译器会对生成语法树中的节点执行类型检查，除了常量、类型和函数这些顶层声明之外，它还会检查变量的赋值语句、函数主体等结构：

```go
    for i := 0; i < len(xtop); i++ {
        n := xtop[i]
        if op := n.Op; op != ODCL && op != OAS && op != OAS2 && (op != ODCLTYPE || !n.Left.Name.Param.Alias) {
            xtop[i] = typecheck(n, ctxStmt)
        }
    }

    for i := 0; i < len(xtop); i++ {
        n := xtop[i]
        if op := n.Op; op == ODCL || op == OAS || op == OAS2 || op == ODCLTYPE && n.Left.Name.Param.Alias {
            xtop[i] = typecheck(n, ctxStmt)
        }
    }
    ...
```

类型检查会遍历传入节点的全部子节点，这个过程会展开和重写 `make` 等关键字，在类型检查会改变语法树中的一些节点，不会生成新的变量或者语法树，这个过程的结束也意味着源代码中已经不存在语法和类型错误，中间代码和机器码都可以根据抽象语法树正常生成。

```go
    initssaconfig()

    peekitabs()

    for i := 0; i < len(xtop); i++ {
        n := xtop[i]
        if n.Op == ODCLFUNC {
            funccompile(n)
        }
    }

    compileFunctions()

    for i, n := range externdcl {
        if n.Op == ONAME {
            externdcl[i] = typecheck(externdcl[i], ctxExpr)
        }
    }

    checkMapKeys()
}
```

<img src="assets/bulb.png" width=25px>在主程序运行的最后，编译器会将顶层的函数编译成中间代码并根据目标的 CPU 架构生成机器码，不过在这一阶段也有可能会再次对外部依赖进行类型检查以验证其正确性。



##### javascript 语言的编译

虽然我们常说 js 是动态类型语言，但是其实 js 也是一门编译语言。与传统编译不同的地方在于，js 并非提前编译，编译结果也不能在分布式系统上移植。这一部分内容相较于 Go 编译较少，而且大部分内容是相似的，这里就使用流程图简单概括了。

js 的编译主要工具有：

- **引擎**
  从头到尾负责整个 JavaScript 程序的编译和执行过程。

- **编译器**
  引擎的好朋友之一，负责**语法分析**及**代码生成**等一系列脏活累活

- **作用域**
  引擎的另一个好朋友，负责收集并维护由所有声明的变量组成的一系列的查询，并实施一套非常严格的规则，确定当前所执行的代码对这些变量的访问权限。

  

###### V8 引擎编译流程

在不考虑优化的前提下，编译流程可见下图：（其中 AST等内容可见[上文](#pre)）

<img src="assets/jsengine3.png">

###### 词法作用域

​	这其中我们着重关注词法作用域的规则，包括 var/let 的区别，提升，闭包等概念。

<img src="assets/js2.png">
