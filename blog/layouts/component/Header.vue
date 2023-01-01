<template>
  <header class="header">
    <div class="site-name">
      <h1 class="hidden">NeutronStarPRO</h1>
      <nuxt-link class="logo" to="/">NeutronStarPRO</nuxt-link>
      <p class="description">
        Welcome to my blog, where I will record bits and pieces about my study and life!
      </p>
    </div>
    <div class="nav-menu">
      <nuxt-link to="/" class="nav-link" exact-active-class="current">
        <i class="fa fa-home"> Home</i>
      </nuxt-link>
      <nuxt-link to="/archives" class="nav-link" exact-active-class="current">
        <i class="fa fa-archive"> Archives</i>
      </nuxt-link>
      <nuxt-link to="/about" class="nav-link" exact-active-class="current">
        <i class="fa fa-user"> About</i>
      </nuxt-link>
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
@media screen and (prefers-color-scheme: dark) {
  .header {
    border-bottom: 1px solid #ddd;
    .site-name {
      .logo {
        color: rgb(229, 226, 226);
        &:hover {
          color: rgb(113, 112, 112);
        }
      }
      .description {
        color: rgb(233, 232, 232);
      }
    }
    .nav-menu {
      .nav-link {
        color: rgb(204, 203, 203);
        &:hover {
          border-bottom-color: #252525;
        }
        &.current {
          border: 1px solid #ddd;
          border-bottom-color: #fff;
        }
      }
    }
  }
}
</style>
