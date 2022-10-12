<template>
  <header class="header">
    <div class="site-name">
      <h1 class="hidden">NeutronStarPRO</h1>
      <nuxt-link class="logo" to="/">NeutronStarPRO</nuxt-link>
      <p class="description">
        欢迎来到我的个人博客，我会在这里记录下关于学习和生活的点点滴滴
      </p>
    </div>
    <div class="nav-menu">
      <nuxt-link to="/" class="nav-link" exact-active-class="current">
        <i class="fa fa-home"> 首页</i>
      </nuxt-link>
      <nuxt-link to="/archives" class="nav-link" exact-active-class="current">
        <i class="fa fa-archive"> 归档</i>
      </nuxt-link>
      <!-- <nuxt-link to="/tags" class="nav-link" exact-active-class="current">
        <i class="fa fa-tag"> 标签</i>
      </nuxt-link> -->
      <nuxt-link to="/about" class="nav-link" exact-active-class="current">
        <i class="fa fa-user"> 关于</i>
      </nuxt-link>
      <!-- <nuxt-link to="/history" class="nav-link" exact-active-class="current">
        <i class="fa fa-book"> 历史</i>
      </nuxt-link> -->
      <!-- <nuxt-link to="/guestbook" class="nav-link" exact-active-class="current">
        <i class="fa fa-comments"> 留言</i>
      </nuxt-link> -->
    </div>
  </header>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.header {
  padding: 58px 0 0;
  text-align: left;
  border-bottom: 1px solid #ddd;
  position: relative;
  .site-name {
    margin-bottom: 40px;
    .hidden {
      padding: 0;
      margin: 0;
      height: 0;
      overflow: hidden;
      display: none;
    }
    .logo {
      font: bold 38px/1.12 "Times New Roman", Georgia, Times, sans-serif;
      color: #555;
      word-break: break-all;
      &:hover {
        color: #777;
      }
    }
    .description {
      margin: 0.2em 0 0;
      color: #999;
    }
  }
  .nav-menu {
    display: flex;
    margin: 10px 0 -1px;
    padding: 0;
    position: absolute;
    right: 0;
    bottom: 0;
    .nav-link {
      padding: 3px 20px 3px;
      line-height: 30px;
      color: #444;
      font-size: 13px;
      border: 1px solid transparent;
      &:hover {
        border-bottom-color: #444;
      }
      &.current {
        border: 1px solid #ddd;
        border-bottom-color: #fff;
      }
    }
  }
}
@media print, screen and (max-width: 48em) {
  .header {
    .site-name {
      margin-bottom: 20px;
      text-align: center;
    }
    .nav-menu {
      position: relative;
      text-align: center;
      justify-content: center;
      flex-wrap: wrap;
      .nav-link {
        padding: 0 15px;
        line-height: 27px;
        height: 27px;
        font-size: 13px;
      }
    }
  }
}
</style>
