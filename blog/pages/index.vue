<template>
  <div class="wrapper">
    <article class="article" v-for="article in articles" :key="article.attributes.title">
      <h1 class="article-title">
        <nuxt-link class="link" :to="article.path">
          {{ article.attributes.title }}
        </nuxt-link>
      </h1>
      <div class="article-meta">
        <div class="article-date">
          {{ formatDate(article.attributes.date) }}
        </div>
      </div>
      <div class="article-content markdown-body" v-html="article.summary"></div>
      <div class="article-more">
        <nuxt-link class="link" :to="article.path">
          阅读全文
        </nuxt-link>
      </div>
    </article>
    <nav class="navigator">
      <pager :hide-if-one-page="false" :total-page="pagerCount" :current-page.sync="currentPage" @update:currentPage="updatePage" />
    </nav>
  </div>
</template>

<script>
import Pager from '@/components/Pager'
import { perHomeCount } from '@/config'
import { getArticles, getPagerCount, formatDate } from '@/util'

export default {
  async asyncData () {
    const context = await require.context('~/content/blog', true, /\.md$/)
    // console.log(context(context.keys()[0]))
    const articles = await context.keys().map(key => ({
      ...context(key),
      summary: context(key).html.split('<!-- more -->')[0],
      path: `/blog/${key.replace('.md', '').replace('./', '')}`
    }))
    // TODO 使用脚本来生成文章，默认添加标题和时间，根据生成时的创建时间来排序
    articles.sort((a, b) => new Date(b.attributes.date).getTime() - new Date(a.attributes.date).getTime())
    return { articles: getArticles(1, perHomeCount, articles), allArticles: articles }
  },
  components: {
    Pager
  },
  data () {
    return {
      currentPage: 1,
    }
  },
  computed: {
    pagerCount() {
      return getPagerCount(this.allArticles.length, perHomeCount)
    },
  },
  methods: {
    updatePage(page) {
      this.currentPage = page
      this.articles = getArticles(page, perHomeCount, this.allArticles)
    },
    formatDate(date) {
      return formatDate(date)
    }
  }
};
</script>

<style lang="scss" scoped>
.article {
  padding: 25px 0 15px;
  .article-title {
    margin: 0;
    color: #555;
    text-align: left;
    font: bold 25px/1.1 "ff-tisa-web-pro", Cambria, "Times New Roman", Georgia, Times, sans-serif;
    .link {
      color: #555;
    }
  }
  .article-meta {
    padding: 0;
    margin: 15px 0 0;
    color: #6E7173;
    text-indent: .15em;
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    .article-date {
      &::before {
        font-family: "FontAwesome";
        content: "\f073";
        padding-right: 0.3em;
      }
    }
  }
  .article-content {
    font-size: 15px;
    line-height: 1.77;
    color: #444;
    padding-top: 15px;
    text-align: justify;
    text-justify: distribute;
    word-break: normal;
  }
  .article-more {
    display: flex;
    justify-content: flex-end;
    margin-top: 10px;
    .link {
      font-size: 14px;
      color: #444;
      padding: 5px 10px;
      border: 1px solid #ddd;
      border-radius: 5px;
      &::after {
        font-family: "FontAwesome";
        content: "\f101";
        padding-left: 0.3em;
      }
      &:hover {
        background: #F8F8F8;
      }
    }
  }
}
.navigator {
  border-top: 1px solid #ddd;
  list-style: none;
  margin-top: 25px;
  padding: 25px 0 0;
  font-size: 14px;
  text-align: center;
}
</style>
