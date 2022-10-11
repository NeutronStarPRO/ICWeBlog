---
title: NS——一种匿名兑换比特币的方法
date: 2022-09-22
tags:
 - 未来梦想家
categories:
 - ICP
 - 产品设计
---

如何才能完全匿名的交易比特币？

我发现很难，几乎不可能做到。因为不管怎样，比特币网络总会公开交易记录。导致比特币最终还是得通过一个账户发送到交易所。

所以，我们不如换一种思路设计匿名的过程：**大家都把比特币扔掉，换成一种没有交易记录的币，然后变现就完全匿名了！**

我给这个新币起了一个代号 “ NS ” ，是中子星的英文首字母缩写。

<!-- more -->

<br>

我在 IC 网络上设计了一个方法，黑洞 canister 是一个不受任何人控制的“ 智能合约 ”，不过可以让别人给黑洞容器充值 Cycles 来维持容器运行。

发 1 个比特币和一点 “ Gas ” ，黑洞 canister 就会创建 1 个 NS 钱包 canister ，然后发 1 个 NS 给钱包，再把钱包 canister 的控制权交给用户。拿着 NS 去交易所卖钱就无法溯源了，因为 NS 就没有 “ 源 ” ！

<br>

所有 NS 都是由 BTC 兑换来的！

![img](https://github.com/NeutronStarPRO/NeutronStarPROBolgPicOnIC/blob/main/NS%E2%80%94%E2%80%94%E5%A6%82%E4%BD%95%E5%8C%BF%E5%90%8D%E4%BA%A4%E6%98%93%E6%AF%94%E7%89%B9%E5%B8%81/2.jpg?raw=true)

<br>

这里有四个问题需要解决：

1. NS 必须绝对可信。

2. 比特币是 “ 黄金 ”，NS 需要与比特币实现价值绑定，让大家认为 NS 和比特币一样值钱。

3. NS 不能与比特币网络有任何关联。

4. 既然已经没有交易记录了，如果我觉得 NS 和比特币一样值钱，是一种匿名的比特币，想买点 NS ，怎么验证这个 NS 是真的 NS ，而不是别人随意伪造的币呢。

   <br>

答案很简单：

1. 我通过黑洞 canister 让大家信任 NS 。没人能控制黑洞 canister 所以它会像一个自动售货机一样在 IC 上一直工作。
2. 让大家把 BTC 和 ICP 发送进黑洞 canister ，发多少 BTC 就会获得多少 NS 。因为 NS 是用 BTC 换到的，所以虽然 NS 没有与 BTC 实现算法锚定，但是 NS 的价值仍然等于 BTC。(当然有人愿意 1 个 NS 卖 1 块钱也不是不行)
3. NS 是运行在 IC 网络上的 Token ，与比特币网络没有任何关联。
4. NS 没有交易记录，但是一个 canister 向另一个 canister 发送 NS 时，需要先互相**确认身份**。确认双方都来自母 canister 之后才会交易。也就是说，钱包只能由那个黑洞 canister 创建，第三方创建的钱包无法通过验证。

<br>

两个 canister 之间**确认身份**的过程也很简单，就是用非对称加密算法验证双方的 Root word 是否相同：

<br>

黑洞 canister 创建钱包 canister 时通过端到端加密发送 Root word 到钱包里。收到 Root word 后立即用 AES 256 把 Root word 保护起来。🔒

![img](https://github.com/NeutronStarPRO/NeutronStarPROBolgPicOnIC/blob/main/NS%E2%80%94%E2%80%94%E5%A6%82%E4%BD%95%E5%8C%BF%E5%90%8D%E4%BA%A4%E6%98%93%E6%AF%94%E7%89%B9%E5%B8%81/2.jpg?raw=true)

钱包发送 NS 前，互发公钥给对方。

<br>

双方用公钥加密自己的 Root word 的哈希再发给对方。

<br>

用私钥解密后，对比自己的 Root word 的哈希，一样就通过认证。

<br>

假如 A 钱包要给 B 钱包发送 NS ：

![image-20221011144829550](https://github.com/NeutronStarPRO/NeutronStarPROBolgPicOnIC/blob/main/NS%E2%80%94%E2%80%94%E5%A6%82%E4%BD%95%E5%8C%BF%E5%90%8D%E4%BA%A4%E6%98%93%E6%AF%94%E7%89%B9%E5%B8%81/1.png?raw=true)

<br>

确认之后就可以进行交易了。

<br>