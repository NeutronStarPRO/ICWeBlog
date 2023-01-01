<template>
  <footer class="footer">
    <div class="wrapper">
      <a href="/About">Nash Zheng</a> 2023
    </div>
  </footer>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.footer {
  width: 75%;
  margin-top: 1.8em;
  .wrapper {
    line-height: 2.5;
    color: #6E7173;
    padding: .8em 0 3.6em;
    text-align: center;
  }
}
@media print, screen and (max-width: 48em) {
  .footer {
    width: 100%;
  }
}
@media screen and (prefers-color-scheme: dark) {
  .footer {
    .wrapper {
      color: #a7b1b7;
    }
  }
}
</style>
