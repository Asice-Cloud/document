#### <span id="pointer">进阶篇其 1-进入代码(下): 指针和自定义类型，更多特性</span>

> [!NOTE]
>
> 本章作者：syl
>
> 难度：⭐⭐⭐⭐⭐
>
> 涉及语言：C/C++，Go

<img src="assets/awesomeface.png" width=25px> 你可能早就听闻了指针的大名。2024 年的全球 Windows 蓝屏的原因就是一个经典的野指针访问。（图片来自 b 站 epcdiy）

<img src="assets/pointer1.png" width=700px >

另一个臭名昭著的叫调用空指针，同样是程序爆炸的典中典了。

##### **所以，什么是指针，指针又为什么这么重要？**

下面是摘自维基百科的定义：

在计算机科学中，指针是一种最简单形式的 [引用](https://zh.wikipedia.org/wiki/參照)（reference）。

指针有两种含义，一是作为数据类型，二是作为实体。前者如字符指针、浮点数指针等等；后者如指针对象、指针变量等。

**指针引用（reference）了存储器中一个地址**。通过被称为指针解引用（dereference）的动作，可以取出在那个地址中存储的 [值](https://zh.wikipedia.org/wiki/值_(電腦科學))。保存在指针指向的地址中的 [值](https://zh.wikipedia.org/wiki/值_(電腦科學))，可能代表另一个 [变量](https://zh.wikipedia.org/wiki/變數_(程式設計))、[结构](https://zh.wikipedia.org/wiki/資料結構)、[对象](https://zh.wikipedia.org/wiki/对象_(计算机科学)) 或 [函数](https://zh.wikipedia.org/wiki/函數)。但是从指针值是无法得知它所引用的存储器中存储了什么资料类型的信息。可以打个比方，假设将存储器当成一本书，那么一张记录了某个页码加上行号的 [便利贴](https://zh.wikipedia.org/wiki/便利貼)，可以被当成是一个指向特定页面的指针；根据便利粘贴面的页码与行号，翻到那个页面，把那个页面的那一行文字读出来，就相当于是对这个指针进行解引用的动作。可做一模拟以增强对指针的理解：整数（integer）也是一类数据类型及其对象或 [变量](https://zh.wikipedia.org/wiki/變數_(程式設計))，可定义具体的数据类型如短整数（short）、长整数（long）、超长整数（long long）、无符号整数（unsigned）等等；也可以用于称呼整数值、整数对象、整数变量等。又如，一个浮点数指针（float *），可称作指向了一个浮点数类型的对象。

**这一段话初看可能很迷惑，但是重点就在于，指针存储的信息，是内存中某一变量的地址，而不是直接存储变量的值。**

这里解释一下值和引用的区别：如果我想知道你在家里做什么，值相当于你告诉我在做什么，是一个给出了一个副本的过程；引用就是相当于指针找到了你家的门牌号，通过指针就可以直接找到你在哪里、在家里做什么。<img src="assets/awesomeface.png" width=25px> 我们可以参考这个图片：

<img src="assets/pointer.avif" width=400px>

在 C 语言中，指针和引用的使用方式是这样的：

```c
//C
//取出某个变量地址，用 &
int a = 1;
printf("address of a is %p", &a);
//定义指针使用 [类型]*指针名 = 变量地址
int *p = &a;
// 使用指针需要解引用，使用 * 
int b = *p + 1;
printf("b is %d",b); //2
```

##### 内存结构

在了解了指针的概念后，我们可以深入探讨以下前面写过的变量生命周期的问题。先来了解一下编程语言的内存结构（不同语言可能有不同的标准内存结构），我们以 **C 语言内存结构** 为例介绍变量是如何存储的（实际上这就是 **linux x86_64 gnu** 的内存结构）

<img src="assets/memory4.png" >

我们主要描述堆和栈，其他大家自行了解即可。

我们在上面提到过，**栈区** 是编译器 **自动管理的部分**，我们用户不能也不需要干涉。这里主要是存储 **局部变量、函数以及返回值**，它们有时候也被称为 **自动生命周期变量**。而 **堆区** 就是我们用户手动管理的区域。下面是 C 语言申请堆区内存的例子：

```c
//C
// 需要头文件 #include<stdlib.h>

int *arr = (int*)malloc(10*sizeof(int)); //申请了10个int大小的空间
free(arr); //记得释放这个空间，要不然会撑爆内存的（重启电脑除外）
```

<img src="assets/awesomeface.png" width=25px> 是不是感觉这和数组很像？没错，**数组是一坨连续的内存组成的结构，它的数组名就是指向这一串变量的第一个的指针，也就是数组名就是指向索引为 0 的那个元素的指针**。

```c
//C
//所以数组也可以写做：
int *array = {1,2,3,4,5};
//可以输出 *array，发现就是array[0]
```

**这一部分大家知道概念即可，因为更先进的语言已经不需要我们再这么深入底层研究了，有很多方便的方式来分配内存，比如 Go 语言中，使用 make：**

```go
//Go
slice := make([]int, 10)
for i := 0; i < 10; i++{
    slice[i] = i;
}
fmt.Println(slice) // 会输出 0 1 2 3 4 ... 9
```

##### 自定义数据类型

有时候基本类型没有办法满足我们的使用需求，比如下面这个场景：统计全班的年龄 (char*)、身高 (int)、体重 (double) 等数据。

如果我们在 C 语言中还是每种类型的数据都定义一个数组，可能是这样的：

```c
//C
char* names[] = {"程锦鑫", "孙源隆", "王俊杰"};
int height[] = {xxx, xxx, xxx};
double weight[] = {xx.xx, xx.xx, xx.xx};
```

然后我们还需要记住每个数组中变量的顺序和对应其他数组的同一个人的数据，很麻烦。所以，我们可以考虑把数据放到一个整体中去。

我们通常称这种聚合的结构是结构体，C 语言中结构体可以如下方式定义：

```c
//C
struct Student{
    char* name;
    int height;
    double weight;
};

//结构体数组，也可以用指针表示
struct Student[] students = {
    {"程锦鑫", xxx, xx.xx},
    //...更多了例子
} 
```

结构体中可以放入多种不同类型，一个结构体的大小也等于其中所有类型的总和。

> <img src="assets/bulb.png" width=25> 我们知道类型大小可能不是 4 的倍数，而计算机访问时都是按 4 作为单元的。所以如果能将不是倍数的进行调整为 4 的倍数（称为对齐）将会提高性能。这一点在嵌入式开发中尤其重要。
>
> 另一方面，我们知道函数是一种类型，所以结构体中也可以放入函数，这也是面向对象的一个重要的实现方式。我们会在下面章节接触面向对象的内容。

##### 再谈形参

我们继续探讨 C 语言中向函数传递参数的问题。现在可以解释之前 swap 函数的问题了，我们使用指针，是直接找到了变量 a,b 的地址，将存储在这个地址上的值进行了交换，而 a，b 指针的生命周期在函数 swap 之外，所以它们交换成功。同样的，使用数组也是一个道理。

```c
//C
void swap(int *a,int *b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
int main(){
    int a = 1,b = 2;
    swap(&a, &b);
    printf("a=%d,b=%d", a, b); //现在就是a=2 b=1了
}
```

<img src="assets/question.png" width=25px> 我们有提到过函数存储在栈上，其函数名也是指向函数的指针，大家可以自行了解是什么作用，我们只写一个例子演示：函数指针两个主要用途：第一个是 **回调函数**，这个概念我们也会在实际开发中经常用到，会在 **异步编程** 的章节详细讲述。

```c
//C
int add(int a, int b){
    return a + b;
}

int substract(int a, int b){
    return a - b;
}

//回调函数
//定义方式： [返回类型](*指针名)(形参列表)
//调用方式： 函数名(实参列表)
void operation(int a, int b, int (*func) (int a, int b)){
    printf("result is %d", func(a, b));
}

int main(){
    operation(10, 5, add);
    operation(10, 5, substract);
    return 0;
}
```

第二种用途：通过函数指针也可以实现 **结构体中的函数**（一般称这种函数为方法），这是面向对象的重要内容：

```c
//C
struct Student{
    char* name;
    int* scores;
    //计算总分：假设scores是 {1，2，3，4，5}
    int (*f)(int *arr);
}

int sum(int *arr){
    int res = 0;
    for(int* i=arr;i<=arr+5;i++){
        res+=*i;
    }
    return res
}

int main(){
    struct Student *s = (struct Student) malloc(sizeof(struct Student));
    s->name = "函数指针";
    s->scores = (int*) malloc(sizeof(int) * 5);
    for(int i = 0; i <= 5; i++){
        s->scores[i] = i;
    }
    s->f = sum;
    printf("%d: ", s->f(s->scores));
}
```

##### 指针的威力

<img src="assets/awesomeface.png" width=25px> C/C++ 已经被白宫列为了危险的东西，那群老登现在都在鼓吹 rust。Linux 系统也委员会也因为是否使用 rust 开发内核处于几乎内战的状态了。说到 C/C++ 内存问题，99% 都是因为指针的破坏力太大了。我们举一个例子：

```c
//C
int a = 1;
int *p = &a;
printf("p is %p, p+1 is %p", (void*) p, (void*) (p+1); // 加减法会将地址值加减一个此类型的大小
```

WC，指针居然也能做加减运算，但如果你不小心运算到了某个没有存储数据的随机地址，然后你又去尝试取它的数据，便会触发一个叫脏内存的东西。顾名思义，这就是随机的数据，可能导致你的程序崩溃退出。

<img src="assets/awesomeface.png" width=25px>另一方面，如果你已经使用 free 手动释放了指针，指针将变为野指针，顾名思义这将指向不可访问/不可预测的区域，如果你不小心又访问或者释放了一次，寄寄。

上面就是野指针的危害，相对的，空指针就是指向没有存储数据的地址，即 0 地址处，称为 NULL 或者 nil, 这里是没有东西的。我们就不演示空指针和野指针了，大家可以自行了解。
