<template>
  <aside class="aside">
    <div class="wrapper">
      <div class="widget">
        <div class="widget-title">
          <i class="fa fa-folder-o"> Categories</i>
        </div>
        <ul class="category-list">
          <li class="category-list-item" v-for="category in categories" :key="category">
            <nuxt-link class="link" :to="`/categories/${category}`">{{category}}</nuxt-link>
          </li>
        </ul>
      </div>
      <div class="widget">
        <div class="widget-title">
          <i class="fa fa-tags"> Tags</i>
        </div>
        <div class="tag-list">
          <nuxt-link class="tag-item" :to="`/tags/${tag}`" v-for="tag in tags" :key="tag">{{tag}}</nuxt-link>
        </div>
      </div>
      <div class="widget">
        <div class="widget-title">
          <i class="fa fa-file-o"> Recent articles</i>
        </div>
        <ul class="article-list">
          <li class="article-list-item" v-for="article in rencentArticles" :key="article.attributes.title">
            <nuxt-link class="link" :to="article.path">
              {{ article.attributes.title }}
            </nuxt-link>
          </li>
        </ul>
      </div>
    </div>
  </aside>
</template>

<script>
export default {
  data() {
    return {
      categories: [],
      tags: [],
      rencentArticles: []
    }
  },
  methods: {
    getCategories(articles) {
      const categories = [];
      articles.forEach(article => {
        article.attributes.categories.forEach(category => {
          if (categories.filter(item => item === category).length === 0) {
            categories.push(category);
          }
        })
      })
      return categories;
    },
    getTags(articles) {
      const tags = [];
      articles.forEach(article => {
        article.attributes.tags.forEach(tag => {
          if (tags.filter(item => item === tag).length === 0) {
            tags.push(tag);
          }
        })
      })
      return tags;
    }
  },
  async fetch () {
    const context = await require.context('~/content/blog', true, /\.md$/);
    const articles = await context.keys().map(key => ({
      ...context(key),
      path: `/blog/${key.replace('.md', '').replace('./', '')}`
    }))
    articles.sort((a, b) => new Date(b.attributes.date).getTime() - new Date(a.attributes.date).getTime());
    this.rencentArticles = articles.slice(0, 5);
    this.categories = this.getCategories(articles);
    this.tags = this.getTags(articles);
  },
};
</script>

<style lang="scss" scoped>
.aside {
  width: 25%;
  padding-top: 40px;
  .wrapper {
    border-left: 1px solid #ddd;
    padding-left: 35px;
    padding-bottom: 20px;
    word-wrap: break-word;
    .widget {
      margin-bottom: 30px;
      .widget-title {
        color: #6E7173;
        line-height: 2.7;
        margin-top: 0;
        font-size: 16px;
        border-bottom: 1px solid #ddd;
      }
      ul {
        list-style: none;
        padding: 0;
        margin: 14px 0;
        li {
          margin: 5px 0;
          line-height: 1.5;
          /* .link {
            color: #6E7173;
            &:hover {
              color: #444;
            }
          } */
        }
      }
      .tag-list {
        display: flex;
        flex-wrap: wrap;
        margin: 14px 0;
        .tag-item {
          line-height: 26px;
          padding: 0px 5px;
          margin: 3px;
          border: 1px solid #808080;
          border-radius: 5px;
          color: #aaa;
          &:hover {
            color: #fff;
            border: 1px solid #808080;
            background: #afafaf;
          }
        }
      }
    }
  }
}
@media print, screen and (max-width: 48em) {
  .aside {
    display: none;
    .wrapper {
      border-left-width: 0px;
    }
  }
}
@media screen and (prefers-color-scheme: dark) {
  .aside {
    .wrapper {
      border-left: 1px solid #ddd;
      .widget {
        .widget-title {
          color: #c1c3c5;
          border-bottom: 1px solid #ddd;
        }
        .tag-list {
          .tag-item {
            border: 1px solid #d5d3d3;
            color: rgb(227, 227, 227);
            &:hover {
              color: rgb(206, 206, 206);
              border: 1px solid #dfdddd;
              background: #4f4f4f;
            }
          }
        }
      }
    }
  }
}
</style>
