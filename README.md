# kayotin-vote
本案例将结合Django和Mysql，实现一个投票项目。
### 项目介绍

本项目源于以下链接，主要参考了这个100天学习Python。

原文链接：[https://github.com/jackfrued/Python-100-Days/blob/master/Day41-55/42.深入模型.md](https://github.com/jackfrued/Python-100-Days/blob/master/Day41-55/42.%E6%B7%B1%E5%85%A5%E6%A8%A1%E5%9E%8B.md)

但是呢，原文并没有上传本项目的源码，而且有的地方也说的很不清楚，导致学习的时候走了很多弯路。所以这里把项目源码上传上来，希望后面学习的同学可以少走一点弯路。

### 项目功能

本案例将结合Django和Mysql，实现一个投票项目。

- 投票项目的首页会展示某在线教育平台所有的学科；
- 点击学科可以查看到该学科的老师及其信息；
- 用户登录后在查看老师的页面为老师投票，可以投赞成票和反对票；
- 未登录的用户可以通过登录页进行登录；
- 尚未注册的用户可以通过注册页输入个人信息进行注册。
- ### 创建项目

在cmd输入以下命令创建项目vote

```python
django-admin startproject vote
```

用pycharm打开项目，指定虚拟环境，然后在终端中输入以下命令新建一个应用polls

```python
python manage.py startapp polls
```

在主目录新建一个保存模板页的文件夹`tempaltes`，包含4个静态页面。分别是展示学科的页面`subjects.html`，显示学科老师的页面`teachers.html`，登录页面`login.html`，注册页面`register.html`

修改配置文件settings.py，指定模版文件路径，也就是Templates中的DIRS项
