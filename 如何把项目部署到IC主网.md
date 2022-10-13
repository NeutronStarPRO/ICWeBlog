## 把 MyICBlog 项目部署到 IC 主网

前提条件:
已经电脑安装了 nodejs、dfx（ IC 开发 SDK ）

**关于如何安装 dfx开发工具、如何创建开发者身份、dfx 常用命令、创建cycles钱包、把ICP转cycles、什么是cycles、ICP经济模型 10月14日晚上会更新详细说明，这里暂时跳过**


<br>

先在命令行中转到 MyICBlog 的目录 （注意：是在 MyICBlog 目录下操作，不是在 ICWeBlog 下）

安装依赖包

```bash
npm install
```

#### 本地部署测试

先在本地环境测试一下效果：

打开 2 个命令行窗口，一个输入：

```bash
dfx start --clean
```

在另一个命令行里输入：

```bash
dfx deploy
```



#### 主网部署项目

```bash
dfx ping ic
```

```bash
dfx deploy --network ic
```
