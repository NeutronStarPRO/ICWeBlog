<template>
  <div class="wrapper">
    <h1 class="title">Viewing articles under {{keyword}} category</h1>
    <div class="archive">
      <div class="archive-list">
        <div class="archive-item" v-for="archive in archives" :key="archive.date">
          <h2 class="archive-time">{{archive.date}}</h2>
          <ul class="article-list" v-for="article in archive.articles" :key="article.attributes.title">
            <li class=".article-item">
              <span class="article-date">{{ formatDate(article.attributes.date) }}</span>
              <nuxt-link class="article-link" :to="article.path" :title="article.attributes.title">{{ article.attributes.title }}</nuxt-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { formatArticles, formatDate } from '@/util'
export default {
  async asyncData({isDev, route, store, env, params, query, req, res, redirect, error}) {
    const context = await require.context('~/content/blog', true, /\.md$/);
    let articles = await context.keys().map(key => ({
      ...context(key),
      date: context(key).attributes.date,
      path: `/blog/${key.replace('.md', '').replace('./', '')}`
    }))
    const keyword = route.params.slug;
    articles = articles.filter(article => {
      return article.attributes.categories.indexOf(keyword) !== -1;
    })
    return { archives: formatArticles(articles, articles.length), keyword };
  },
  methods: {
    formatDate(date) {
      return formatDate(date);
    }
  }
}
</script>

<style lang="scss" scoped>
.title {
  margin-top: 1.1em;
  margin-bottom: .67em;
  font-size: 20px;
  font-weight: normal;
  color: #888;
}
.archive {
  padding: 25px 0 15px;
  .archive-list {
    font-size: 17px;
    line-height: 2;
    padding-bottom: .8em;
    .archive-item {
      .archive-time {
        margin: 0;
        font: bold 25px / 1.1 "ff-tisa-web-pro", Cambria, "Times New Roman", Georgia, Times, sans-serif;
      }
      .article-list {
        margin: 15px 0;
        padding-left: 40px;
        .article-item {
          .article-date {
            padding-right: .7em;
          }
        }
      }
    }
  }
}
@media screen and (prefers-color-scheme: dark) {
  .title {
    color: rgb(217, 217, 217);
  }
}
</style>
