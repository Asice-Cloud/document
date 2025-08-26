#### <span id="run">入门篇其 6 - 程序，启动！</span>

> [!NOTE]
>
> 本章作者：wjj
>
> 难度：⭐⭐⭐
>
> 涉及语言：C/C++

经过上面的简单介绍，你应该已经了解了简单的代码知识。现在我们就来实践一下，如何写出一个简单的程序。

```c
// C
#include "stdio.h"

void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void output(int arr[],int len) {
    for (int i = 0; i < len; i++) {
        printf("%d ",arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {454, 7, 16, 644, 76, 78, 13};
    int len = 7;
    printf("排序前的数组:");
    output(arr, len);
    insertionSort(arr, len);
    printf("排序后的数组:");
    output(arr, len);
    
}
```

这是一个插入排序的例子，将一个 `int` 数组按从小到大的顺序排序。<img src="assets/bulb.png" width=25px> 在安装了 `Code Runner` 插件的前提下你可以在 vscode 代码区右键，然后点击 `RunCode` 即可运行。顺便一提，`Code Runner` 可以支持多种语言的运行与调试，也可以手动配置编译选项（我们会在编译章节介绍编译参数选项），大家可以自行尝试更多功能。如下图所示，vscode 中右键后出现在最上面的 Run Code 选项就是这个插件的效果之一。

> 插入排序：维护一个已经排序好的数组，依次将后面的元素按大小顺序插入到合适的位置。将第一个元素看作已经排序好的数组，然后将后面的元素依次插入，时间复杂度是 $O(n^{2})$

<img src="assets/runcode.png" width=500>
