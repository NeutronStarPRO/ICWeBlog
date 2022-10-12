# ICWeBlog
欢迎使用 ICWeBlog 博客部署工具！

你可以使用这个工具在区块链上部署自己的博客网站，不需要依赖第三方的去中心化博客网站！

部署在区块链上的网页响应速度依然非常快，体验极佳！

自己可以控制自己的所有数据，自由创建网站，抗审查的 IC 云端博客网站。

价格非常便宜，只要大约 70 元人民币就可以部署很多年。

可以自己修改前端页面，做不同风格的主页，欢迎 pr 。

## 项目目录结构
* blog 文件夹用于生成静态博客网页
* MyICBlog 文件夹是要部署在 IC 主网的项目文件
* zzx.py 脚本，把生成的静态网站转移到 IC 项目里

## 博客说明
只要把 md 文章放进指定目录里就可以生成静态网站了！
### md文件格式
只要按如下格式写好 markdown 文件，然后把 markdown 文件放进 `blog/content/blog/` 里：
```
---
title: 后知后觉
date: 2021-12-27
tags:
 - 未来梦想家
categories:
 - 随笔
---
想象一下，假设现在的机器人技术非常发达了。
那么机器人可以代替人力去做基础性劳动了：由机器人负责种地、浇水，机器人用饲料喂猪，机器人杀猪，机器人做饭、烹饪猪肉等等。
这时候就会有很多普通人将会因为没事干而把大多数时间花在短视频、电影、游戏上（虚拟世界）。
实际上，人们更愿意把时间放在网络上、在游戏里、在虚拟空间里，而不是去乡下锄地或者喂猪。
<!-- more -->
<br>
如果除了睡觉，所有醒着的时间都花在虚拟世界里，真实世界与虚拟世界的界限将越来越模糊。（有VR、MR等等技术）
虚拟世界里有种资产叫 “ Token ” ，人们都喜欢虚拟世界里赚钱，赚到的钱大多数也花在了虚拟世界。
人们愿意把钱存在虚拟世界的银行里。
```
就可以了。

效果如下：

![image-20221011193721863](assets/README/image-20221011193721863.png)

title 是文件标题，date 是文章的时间，tags 是文件的标签（一篇文章可以有好几个标签），categories 是文章分类。<br>
`<!-- more -->` : 放在文章第一段用于首页预览。<br>
`<br>` : 换行的意思，需要空几行就写几个`<br>`。<br>

### 为文章加入图片

为了让网站打开速度更快，请把文章中的图片上传到 Github 仓库，然后在文章中加入 `<img src="这里放图片链接">` 标签即可。<br>
例如：
`<img src="https://github.com/NeutronStarPRO/NeutronStarPROBolgPicOnIC/blob/main/NS%E2%80%94%E2%80%94%E5%A6%82%E4%BD%95%E5%8C%BF%E5%90%8D%E4%BA%A4%E6%98%93%E6%AF%94%E7%89%B9%E5%B8%81/1.png?raw=true"> `

### 修改网站的标题

打开 `blog/nuxt.config.js` 文件。
找到如下代码：（在文件的第 23 行）这个是我自己的配置：

```
 head: {
    title: 'NeutronStar的博客',
    meta: [
      { charset: 'utf-8' },
      { name: 'apple-mobile-web-app-capable', content: 'yes' },
      { name: 'apple-mobile-web-app-status-bar-style', content: 'black-translucent' },
      { name: 'format-detection', content: 'telephone=no' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover' },
      { hid: 'description', name: 'description', content: '个人博客 | Blog | Markdown | Vue | Nuxt' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
```
把 title 改成自己的，例如：`title: '小王的博客',` 。

打开 `blog/layouts/component/Header.vue` ，把第 4、5、7 行的文字替换为你想要的：这个是我的配置
```vue
<template>
  <header class="header">
    <div class="site-name">
      <h1 class="hidden">NeutronStarPRO</h1>
      <nuxt-link class="logo" to="/">NeutronStarPRO</nuxt-link>
      <p class="description">
        欢迎来到我的个人博客，我会在这里记录下关于学习和生活的点点滴滴
      </p>
    </div>
```
你可以换成，例如：
```
<template>
  <header class="header">
    <div class="site-name">
      <h1 class="hidden">小王</h1>
      <nuxt-link class="logo" to="/">小王</nuxt-link>
      <p class="description">
        欢迎来到我的个人博客，我会在这里记录下关于学习和生活的点点滴滴
      </p>
    </div>
```

### 修改关于页

打开 `blog/pages/about.vue` 文件，修改文件中 6 ~ 20 行的对应汉字内容即可。

```vue
<template>
  <div class="wrapper">
    <h2>关于</h2>
    <br/><br/>

      正在学习: <br/><br/>
      HTML、CSS、JavaScript、React、Vue、Flutter、Motoko、Rust、Svelte、Python<br/><br/>
      产品设计、IC、web3、架构、区块链、智能合约<br/><br/>
      经济学、英语、哲学、博弈论<br/><br/>

    <br/>

      <strong>联系我：</strong><br/><br/>

      Email:&nbsp;&nbsp; nashzhengpro@gmail.com / 15383620197@qq.com<br/><br/>
      WeChat:&nbsp;&nbsp; NeutronStarPRO<br/><br/>
      Twitter:&nbsp;&nbsp; <a href="https://twitter.com/NeutronStar_PRO">@NeutronStar_PRO</a><br/><br/>
      Github:&nbsp;&nbsp; <a href="https://github.com/NeutronStarPRO">NeutronStarPRO</a><br/><br/>
      Bilibili:&nbsp;&nbsp; <a href="https://space.bilibili.com/627399227">中子星PRO</a><br/><br/>
      Discord: NeutronStarPRO#2925

      <br/><br/><br/><br/><br/><br/><br/>
      <p>
        Powered by Dfinity Internet Computer blockchain.
      </p>
  </div>
</template>
```

效果如下：

![image-20221011213635568](assets/README/image-20221011213635568.png)



## 部署博客文章

1. 使用电脑的命令行进入 blog 文件夹，然后输入 `npm run generate` 命令  [这里查看详细教程 ](如何生成网站.md) 
2. 运行 zzx.py 脚本  [这里查看详细教程](Python的作用) 
3. 进入 MyICBlog 目录部署，把 MyICBlog 部署到 IC 主网  [这里查看详细教程](如何把项目部署到IC主网) 





