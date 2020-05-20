# git学习笔记

## 配置git

~~~linux
配置了用户名和邮箱，修改也用此代码
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
查看已经配置设置
git config --list
~~~

## 传文件过程

本地磁盘目录（工作区）上传到 本地虚拟仓库（暂存区）然后上传到 远程仓库（github码云等）

## git操作 工作区-暂存区

~~~
git init 初始化暂存区
工作区->暂存区
git add 文件名称
git add *提交所有文件
git commit -m "提交描述"
git status 查看当前工作区的状态
git checkout 文件名 从暂存区将文件恢复到工作区
git diff 查看工作区和暂存区版本的不同之处
clear清除屏幕
git log 查看提交版本
git reset --hard 版本号  从暂存区恢复到工作区 

~~~

## git操作 暂存区-远程区

~~~~
授权 生成ssh密匙
ssh-keygen -t rsa -C "github邮箱"
win电脑找隐藏文件：
我的电脑 用户 用户名文件夹 .ssh(隐藏文件夹) xxx.pub（密匙在这里）
github账户配置密匙
settings中的ssh and gpg keys中 粘贴到key中（码云中差不多）

暂存区->远程区
git remote add origin 仓库地址
git push -u origin master
第一次提交会要求你输入用户名密码
刷新仓库 即可看见
origin为github默认的 如果想同时关联两个远程仓库
先删除关联  git remote rm origin然后重新关联
git remote add github(gitee) 仓库地址

git clone 仓库地址 从远程仓库克隆到本地
git pull 从远程仓库更新到本地 大家进度不一样时候使用

~~~~
