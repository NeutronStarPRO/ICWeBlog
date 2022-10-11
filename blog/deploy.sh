#!/usr/bin/env sh

# 当发生错误时中止脚本
set -e

# 构建
npm run generate

# cd 到构建输出的目录下
cd dist

cd -
