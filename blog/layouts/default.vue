<template>
  <div class="layout">
    <Header />
    <div class="container">
      <Main />
      <Aside />
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from './component/Header'
import Main from './component/Main'
import Aside from './component/Aside'
import Footer from './component/Footer'

export default {
  components: {
    Header,
    Main,
    Aside,
    Footer
  },
  // async fetch () {

  // }
}
</script>

<style lang="scss" scoped>
.layout {
  padding: 0 60px;
  max-width: 1150px;
  margin: 0 auto;
  .container {
    display: flex;
  }
}
@media print, screen and (max-width: 48em) {
  .layout {
    padding: 0 30px;
    .container {
      display: block;
    }
  }
}
@media print, screen and (max-width: 35.5em) {
  .layout {
    padding: 0 20px;
  }
}
</style>
