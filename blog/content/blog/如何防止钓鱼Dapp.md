---
title: 如何防止钓鱼Dapp
date: 2022-11-04
categories:
 - Computer technology
tags:
 - Chinese & 中文
 - IC
---
如果我想骗别人的 ICP ，我该怎么做？

做个像模像样的 dapp 网站，然后在上面放一些 NFT 、小说之类的东西钓鱼。

那么如何防止这种情况呢，我觉得引入第三方来保障交易比较好。

<!-- more -->

## IC 上如何进行安全支付

如果用户不确定这个 Dapp 是否安全，是不是钓鱼网站。**可以选择安全支付通道，牺牲便宜的 Gas 费，获得安全支付保障。**

<br/>

用户用不用无所谓，dapp 接入就行，让安全支付成为 dapp 标配。

<br/>

**重点在于威慑钓鱼、增强用户信心。**

**如果 dapp 接入了安全支付，就已经代表了这个 dapp 是可信的。当用户看到可以 “ 安全支付 ” 时，就类似是一种认证，就可以放心支付了。**

<br/>

支付过程很简单：

那 NFT 商城来说，如果用户不确定发送 token 后对方是否会 “ 发货 ” ，就可以选择**安全支付**。

<img src="https://s1.imagehub.cc/images/2022/12/13/1b62009ba889a94086d6b35110718489.png" style="zoom: 33%;" />

**1**：点击安全支付，dapp 调用接口。浏览器弹出风控 canister 的页面、显示 dapp 地址信息。**先发给风控 canister 要支付的 token** ，同时风控 canister 为这笔交易生成一个订单 id 。（风控 canister 开源，controller 是开发团队也可以设为黑洞）只有收 token 、退还 token 和支付给 dapp 地址 3 种交易方法，没有转给别人的方法。

**2**：**风控 canister 把收到的 token 、付款人身份发给 dapp** ，dapp 需要在 2 分钟内发 NFT 。

**3**：**dapp 发 NFT 给钱包，如果超时风控 canister 就会退回 token 。**

**4**：钱包收到 NFT 后，弹出提示框告诉用户是否确认收货。确认后就用私钥签名 “ 确认已收货 + 订单 id ” 的信息，发送给风控 canister 。风控 canister 验证后再付给商家 token 。

<br/>

如果是个钓鱼 dapp ，商家 2 分钟内还不发货，token 就会退回，只损失了 2 次 Gas 费。之后上报给 “ 黑名单 ” 公布给大家防范。

<br/>

用户收货后不满意也可以退货退款，只要不点 “ 确认收货 ” ，token 就在风控 canister 里。然后在 NFT list 里点退款，钱包自动退回 NFT 并向风控 canister 发送 “ 退款 + 订单 id ” 的签名。没点 “ 确认收货 ” 时 NFT 被锁在钱包里任何人都没法动。

如果超过 3 天没点确认收货，风控 canister 自动放行 token ，订单更新为 “ 已收货 ” ，用户打开钱包后更新状态信息。

<br/>
<br/>

付款方和收货方都在钱包里才支持安全支付。

~~如果想购买 dapp 里的电子书怎么办？我觉得让用户手动 “ 确认收货 ” 比较好。如果用户收货后，点了未收货，dapp~~

~~风控 canister 内置一个认证 dapp 的默克尔树。记录 dapp 前端 canister id ，在用户选择安全支付时，先从默克尔树验证前端页面。验证后开放安全支付功能，否则风控 canister 拒绝请求。~~

<br/>
