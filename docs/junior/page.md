#### <span id="page">入门篇其 2 - 网页简介: 元素</span>

> [!NOTE]
>
> 本章作者：cjx
>
> 难度：⭐
>
> 涉及语言：html, css

网页是构成网站的基本元素，是承载各种网站应用的平台。通俗地说，网站就是由网页组成的。网页是一个包含 HTML 标签的纯文本文件，它可以存放在世界某个角落的某一台计算机中，是万维网中的一“页”，是超文本标记语言格式（标准通用标记语言的一个应用，文件扩展名为 `.html` 或 `.htm`）。

网页由多个元素构成，每个元素都有其独特的功能和作用。

##### 文本

一般情况下，网页中最多的内容是文本，可以根据需要对其字体、大小、颜色、底纹、边框等属性进行设置。

##### 图像

丰富多彩的图像是美化网页必不可少的元素，用于网页上的图像一般为 JPG 格式和 GIF 格式（当然还有无限缩放而不失去清晰度的 SVG 格式）。网页中的图像主要用于点缀标题的小图片，介绍性的图片，代表企业形象或栏目内容的标志性图片，用于宣传广告等多种形式。

<img src="assets/tenzor.svg" alt="img" width="18px"> 这个挑战 logo 就是由以下代码导入的

```html
<!-- .html文件 -->
<img src="assets/tenzor.svg" alt="img" width="25px">
```

<img src="assets/question.png" alt="q" width="25px"> 上面的一串代码中，img 标签被添加了三个属性，其中 src 属性规定了图像的路径、alt 属性规定了图像无法显示时的替代文本、width 属性规定了图像的宽度。除此之外，img 标签还有 height、draggable 等属性，大家在后续学习中会逐渐接触到。

##### 超链接

超级链接是 Web 网页的主要特色，是指从一个网页指向另一个目的端的链接。这个“目的端”通常是另一个网页，也可以是下列情况之一：相同网页上的不同位置、一个下载的文件、一副图片、一个 E-mail地址等。超级链接可以是文本、按钮或图片，鼠标指针指向超级链接位置时，会变成小手形状。

<a href='https://www.tiaozhan.com/'>跳转至挑战网首页</a>

```html
<!-- .html文件 -->
<a href='https://www.tiaozhan.com/'>跳转至挑战网首页</a>
```

##### 动画

动画是网页中最活跃的元素，创意出众、制作精致的动画是吸引浏览者眼球的最有效方法之一。但是如果网页动画太多，也会物极必反，使人眼花缭乱，进而产生视觉疲劳。

<img src="assets/question.png" alt="q" width="25px"> 下面的代码定义了一个动画，实现了一个元素颜色的变化。

```css
/* .css文件 */
@keyframes animation {
  from {
    color: red;
  }
  to {
    color: green;
  }
}
```

##### 表单

表单是用来收集访问者信息或实现一些交互作用的网页，浏览者填写表单的方式是输入文本、选中单选按钮或复选框、从下拉菜单中选择选项等。

姓名：<input placeholder="请输入你的姓名" style="background-color:white">
性别：<input type='radio' name="gender" style="background-color:white"> 男 <input type='radio' name="gender" style="background-color:white"> 女

```html
<!-- .html文件 -->
<input placeholder="请输入你的姓名" style="background-color:white">
<input type='radio' name="gender" style="background-color:white">男
<input type='radio' name="gender" style="background-color:white">女
```


