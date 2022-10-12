<template>
  <div class="wrapper">
    <article class="article">
      <h1 class="article-title">
        {{ article.attributes.title }}
      </h1>
      <div class="article-meta">
        <div class="article-date">
          {{ formatDate(article.attributes.date) }}
        </div>
        <div class="article-category">
          <nuxt-link class="link" :to="`/categories/${category}`" v-for="category in article.attributes.categories" :key="category">
            {{category}}
          </nuxt-link>
        </div>
      </div>
      <div class="article-content markdown-body" v-html="article.html"></div>
      <div class="article-copyright"></div>
      <div class="article-tags">
        <nuxt-link class="link" :to="`/tags/${tag}`" v-for="tag in article.attributes.tags" :key="tag">
          {{tag}}
        </nuxt-link>
      </div>
      <div class="article-nav">
        <nuxt-link class="link" to="/">
          上一篇文章
        </nuxt-link>
        <nuxt-link class="link" to="/">
          下一篇文章
        </nuxt-link>
      </div>
    </article>
  </div>
</template>

<script>
import { getArticles, getPagerCount, formatDate } from '@/util'

export default {
  async asyncData({ params }) {
    // TODO 路径错误跳转到404页
    const article = await import(`~/content/blog/${params.slug}.md`);
    // console.log(article);
    return {
      article
    };
  },
  methods: {
    formatDate(date) {
      return formatDate(date)
    }
  },
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
      margin-right: 12px;
      &::before {
        font-family: "FontAwesome";
        content: "\f073";
        padding-right: 0.3em;
      }
    }
    .article-category {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      .link {
        margin-right: 6px;
      }
      &::before {
        font-family: "FontAwesome";
        content: "\f07c";
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
  .article-tags {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    margin-top: 2em;
    .link {
      margin-right: 1em;
      &::before {
        font-family: "FontAwesome";
        content: "\f02b";
      }
    }
  }
  .article-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    overflow: hidden;
    margin-top: 15px;
    margin-bottom: 20px;
    padding: 10px;
    white-space: nowrap;
    border-top: 1px solid #eee;
    .link {
      line-height: 25px;
      font-size: 15px;
      color: #555;
      &:first-child::before {
        font-family: "FontAwesome";
        content: "\f0d9";
        padding-right: 0.3em;
      }
      &:last-child::after {
        font-family: "FontAwesome";
        content: "\f0da";
        padding-left: 0.3em;
      }
    }
  }
}
</style>
