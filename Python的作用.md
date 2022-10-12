## Python文件的作用

生成的静态网页都在 `blog/dist` 文件夹里

这个 zzx.py 的作用就是把 `blog/dist` 里的文件移动到 IC 项目的对应位置里

因为每次运行脚本时会清空 `MyICBlog/src/MyCBlog_assets/` 下的所有文件，所以也需要复制一份 index.js 文件放在 `MyICBlog/src/MyCBlog_assets/src` 里。而这个 index.js 文件就放在最外面，在 ICWeBlog 目录下。
把旧文件清空后，再把新生成的文件移进 MyICBlog 项目里。

<br>

如果不想运行 Python 文件，可以手动移动：

所有前端的文件都放在 `MyICBlog/src/MyCBlog_assets/` 里；

* 所有 html 文件都移动到 `MyICBlog/src/MyCBlog_assets/src` 里；             
 （注意：这个目录下原有的 index.js 文件要保留下来；原有的 html 文件可以删掉）

* ` _nuxt`、`favicon.ico`、`.nojekyll` 这 3 个都移动到 `MyICBlog/src/MyCBlog_assets/assets` 里，即可。
