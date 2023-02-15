# Django-web

## 概述

为生产环境部署的一些准备：

* Mysql 8.0+ 

  > * Navicat 数据库可视化操作软件

* [Apache](https://cloud.tencent.com/developer/article/1698069)

  > * 服务端部署

* [WSGI](https://www.cnblogs.com/aaron-agu/p/16376079.html)

* Postman

  > * Postman 可以用来发送请求，从而调用和调试接口。
  > * 可以从它的官网下载并进行安装，然后阅读 [Gettting Started](https://learning.postman.com/docs/getting-started/introduction/) 来学习 Postman 的使用。

然后跟着[官方](https://docs.djangoproject.com/zh-hans/4.1/intro/tutorial01/)熟悉使用方法，最终部署一个自己的项目来。

# TODO
win-Apache 配置存在问题



# Django-Note（一）初始化

## 初始化项目配置

cmd.exe

```shell
django-admin startproject mysite
```

生成的目录结构：

> 外层名字`mysite`可以修改

```markdown
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

## 效果测试

```shell
 python manage.py runserver
```

> 忽略有关未应用最新数据库迁移的警告，稍后我们处理数据库。

服务器现在正在运行，通过浏览器访问 http://127.0.0.1:8000/ 。你将看到一个“祝贺”页面，有一只火箭正在发射。你成功了！

# Django-Note（二）投票应用

## “应用”定义

> 项目 VS 应用
>
> 项目和应用有什么区别？
>
> 应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者小型的投票程序。项目则是一个网站使用的配置和应用的集合。
>
> 项目可以包含很多个应用。应用可以被很多个项目使用。
>
> 在 Django 中，每一个应用都是一个 Python 包，并且遵循着相同的约定。

## 编写应用

在`views.py`编写视图，同时配置`urls`.

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

建立路由

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

还需要建立根目录和对应子应用目录的`url`映射

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```



> 设计了 [`include()`](https://docs.djangoproject.com/zh-hans/4.1/ref/urls/#django.urls.include) ，理念是使`url`可以即插即用。
>
> 当包括其它 URL 模式时使用 `include()` ， `admin.site.urls` 是唯一例外。

## [配置 MySQL 数据库](https://zhuanlan.zhihu.com/p/105717817)

### 安装 mysqlclient

```shell
pip install mysqlclient
```

### 将数据库配置信息存到一个文件中，在settings.py文件中将其引入

创建 MySQL 数据库的配置文件 `my.cnf `

```
[client]
host = 服务器地址
database = 所选数据库
user = 用户名
password = 密码
port = 端口
default-character-set = 字符集，这里推荐 utf8mb4
```

修改`settings.py `

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        'OPTIONS':{
            'read_default_file': 'my.cnf'
        }
    }
}
```



# Django+Nginx + uWSGI生产部署

## 服务器配置python

> python/miniconda的配置见python-notebook

* 新建虚拟环境使 python==3.10 

* ```shell
  pip install django pymysql
  conda install -c conda-forge uwsgi
  ```

## Nginx代理

### [反向代理](https://www.zhihu.com/question/24723688)



# 资源链接

【1】[官方文档](https://docs.djangoproject.com/zh-hans/4.1/)

【2】 [Windows下搭建apache+mod-wsgi+python django环境【全过程】](https://www.cnblogs.com/cmzchxj/p/13794411.html)

