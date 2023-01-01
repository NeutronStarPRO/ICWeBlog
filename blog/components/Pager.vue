<template>
  <div class="pager" :class="{hide: hideIfOnePage && totalPage <= 1}">
    <span class="pager-item prev-nav" @click="onClickPage(currentPage - 1)" :class="{hidden: currentPage === 1}">
      Previous page
    </span>
    <template v-for="(page, index) in pages">
      <template v-if="page === currentPage">
        <span :key="index" class="pager-item current">{{page}}</span>
      </template>
      <template v-else-if="page === '···'">
        <span class="pager-item separator" :key="index">···</span>
      </template>
      <template v-else>
        <span :key="index" class="pager-item other" @click="onClickPage(page)">{{page}}</span>
      </template>
    </template>
    <span class="pager-item next-nav" @click="onClickPage(currentPage + 1)" :class="{hidden: currentPage === totalPage}">
      Next page
    </span>
  </div>
</template>

<script>
export default {
  name: 'Pager',
  props: {
    totalPage: {
      type: Number,
      required: true
    },
    currentPage: {
      type: Number,
      required: true
    },
    hideIfOnePage: {
      type: Boolean,
      default: true
    }
  },
  computed: {
    pages () {
      let pages = [
        1,
        this.totalPage,
        this.currentPage,
        this.currentPage - 1,
        this.currentPage - 2,
        this.currentPage + 1,
        this.currentPage + 2
      ];
      let u = unique(pages.filter((n) => n >= 1 && n <= this.totalPage).sort((a, b) => a - b));
      let u2 = u.reduce((prev, current, index, array) => {
        prev.push(current);
        if (
          array[index + 1] !== undefined &&
          array[index + 1] - array[index] > 1
        ) {
          prev.push('···');
        }
        return prev;
      }, [])
      return u2;
    }
  },
  methods: {
    onClickPage (n) {
      if (n >= 1 && n <= this.totalPage) {
        this.$emit('update:currentPage', n);
      }
    }
  }
}

function unique (array) {
  // return [...new Set(array)];
  const object = [];
  array.map(number => {
    object[number] = true;
  })
  return Object.keys(object).map(s => parseInt(s, 10));
}
</script>

<style lang="scss" scoped>
.pager {
  /* display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap; */
  user-select: none;
  &.hide {
    display: none;
  }
  .pager-item {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    background-color: #fff;
    font-size: 14px;
    height: 36px;
    line-height: 36px;
    padding: 6px 10px;
    color: #444;
    margin: 0 3px;
    cursor: pointer;
    border: 1px solid #ddd;
    &:not(.separator):hover {
      background-color: #f8f8f8;
      border-color: #999;
    }
    &:not(.separator).current {
      cursor: default;
      background-color: #f8f8f8;
      border-color: #999;
    }
    &.separator {
      font-weight: bold;
      cursor: default;
      border: none;
    }
    &.prev-nav {
      float: left;
      margin: 0;
      &::before {
        font-family: "FontAwesome";
        content: "\f100";
        padding-right: 0.3em;
      }
      &.hidden {
        display: none;
      }
    }
    &.next-nav {
      float: right;
      margin: 0;
      &::after {
        font-family: "FontAwesome";
        content: "\f101";
        padding-left: 0.3em;
      }
      &.hidden {
        display: none;
      }
    }
  }
}
@media screen and (prefers-color-scheme: dark) {
  .pager-item {
    background-color: rgb(49, 48, 48) !important;
    color: rgb(215, 213, 213) !important;
    border: 1px solid #ddd !important;
    &:not(.separator):hover {
      background-color: #a7a3a3 !important;
      border-color: rgb(104, 107, 107) !important;
    }
    &:not(.separator).current {
      background-color: #a9a8a8 !important;
      border-color: rgb(118, 112, 112) !important;
    }
  }
}
</style>
