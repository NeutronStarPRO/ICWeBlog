<template>
  <main class="main">
    <Nuxt />
  </main>
</template>

<script>
export default {}
</script>

<style lang="scss" scoped>
.main {
  width: 75%;
  padding-right: 50px;
  padding-top: 20px;
}
@media print, screen and (max-width: 48em) {
  .main {
    width: 100%;
    padding-right: 15px;
  }
}
@media print, screen and (max-width: 35.5em) {
  .main {
    padding-right: 0;
  }
}
</style>
