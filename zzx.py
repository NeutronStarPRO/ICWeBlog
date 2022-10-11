import os
import shutil

# 获取目录
src_path = os.path.abspath("blog/dist")  # dist文件所在目录
src = src_path + "/"

nuxt_path = os.path.abspath("blog/dist/_nuxt")  # 获取_nuxt文件夹的目录
about_path = os.path.abspath("blog/dist/about")
archives_path = os.path.abspath("blog/dist/archives")
blog_path = os.path.abspath("blog/dist/blog")
categories_path = os.path.abspath("blog/dist/categories")
tags_path = os.path.abspath("blog/dist/tags")
guestbook_path = os.path.abspath("blog/dist/guestbook")

assets_target_path = os.path.abspath("MyICBlog/src/MyICBlog_assets/assets")  # 移动到assets目录
assets_tar = assets_target_path + "/"

src_target_path = os.path.abspath("MyICBlog/src/MyICBlog_assets/src")  # 移动到src目录
src_tar = src_target_path + "/"


# 移动文件到IC项目目录的src里
while True:
    file_list = os.listdir(src)  # 获取到当前目录下所有文件

    if len(file_list) > 0:  # 如果目录不为空，那么进行移动

        if os.path.exists(src_tar):
            shutil.rmtree(src_tar)  # 删掉旧文件

        if os.path.exists(assets_tar):
            shutil.rmtree(assets_tar)

        os.mkdir(src_tar)  # 创建新文件夹
        os.mkdir(assets_tar)

        if os.path.exists(assets_tar):
            shutil.move(nuxt_path, assets_tar)  # 移动_nuxt到assets文件夹里
        else:
            print("文件夹不存在")

        if os.path.exists(src_tar):
            shutil.move(about_path, src_tar)
            shutil.move(archives_path, src_tar)
            shutil.move(blog_path, src_tar)
            shutil.move(categories_path, src_tar)
            shutil.move(tags_path, src_tar)
            shutil.move(guestbook_path, src_tar)
        else:
            print("文件夹不存在")

        for file in file_list:  # 遍历目录
            file_end_name = file.split(".")[-1]  
            if file_end_name == "ico":  # 判断我们需要移动的文件，这里移动的是后缀.ico文件
                shutil.move(src + file, assets_tar + file)  # 移动到IC项目的assets文件夹里
            if file_end_name == "nojekyll":  
                shutil.move(src + file, assets_tar + file)  # 移动到IC项目的assets文件夹里
            if file_end_name == "html":  
                shutil.move(src + file, src_tar + file)  # 移动到IC项目的src文件夹里
        
        # 把index.js文件移动到MyICBlog_assets/src里
        # srcfile 需要复制、移动的文件
        # dstpath 目的地址
        def mycopyfile(srcfile, dstpath):  # 复制函数
            if not os.path.isfile(srcfile):
                print ("%s 文件不存在"%(srcfile))
            else:
                fpath,fname = os.path.split(srcfile)  # 分离文件名和路径
                if not os.path.exists(dstpath):
                    os.makedirs(dstpath)  # 创建路径
                shutil.copy(srcfile, dstpath + fname)  # 复制文件

        src_dir = './index.js'
        dst_dir = './MyICBlog/src/MyICBlog_assets/src/'  # 目的路径记得加斜杠
        mycopyfile(src_dir, dst_dir)  # 复制文件
        
    exit(0)  # 移动完毕，进行退出
