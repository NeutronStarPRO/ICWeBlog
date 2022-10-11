<template>
  <footer class="footer">
    <div class="wrapper">
      Copyright © 2022 <a href="/">Nash Zheng</a>
    </div>
  </footer>
</template>

<script>
export default {}
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
</style>
