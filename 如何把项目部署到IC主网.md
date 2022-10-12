## 把 MyICBlog 项目部署到 IC 主网

前提条件:
已经电脑安装了 nodejs、dfx（ IC 开发 SDK ）

**关于如何安装 dfx开发工具、如何创建开发者身份、dfx 常用命令、创建cycles钱包、把ICP转cycles、什么是cycles、ICP经济模型 10月13日晚上会更新详细说明，这里暂时跳过**


<br>

先在命令行中转到 MyICBlog 的目录

安装依赖包

```bash
npm install
```

在本地环境测试：

```bash
dfx start --clean
```

```bash
dfx deploy
```

在主网部署项目：

```bash
dfx deploy --network ic
```
