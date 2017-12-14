第13周

初识后端：请求、MVC、ORM
=======================

安装 pip 和 Django
------------------
* 安装 pip：https://pip.pypa.io/en/stable/installing/
* 安装 Django：`sudo -H pip3 install django`（从 2.0 起 Django **不**支持 Python 2.X）
* 更新 Django：`sudo -H pip install django --upgrade`

HTTP 请求
---------
<pre>
Request       = Request-Line
                *(( general-header
                    | request-header
                    | entity-header ) CRLF)
                CRLF
                [ message-body ]
</pre>

* 请求行
* 头部信息
  * 一行或多行
  * 尾随 CRLF
* 空行，标志头部结束
* 主干信息

MVC（Model-View-Controller）
---------------------------

[Django appears to be a MVC framework, but you call the Controller the “view”, and the View the “template”. How come you don’t use the standard names?](https://docs.djangoproject.com/en/2.0/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names)


由 `urls.py` 决定请求路由

ORM（Object-relational Mapping，关系对象映射） 
--------------------------------------------

```python
class Person(models.Model):
    first_name = models.CharField(...)
    last_name = models.CharField(...)
    birth_date = models.DateField(...)
```

```python
>>> for p in Person.objects.raw('SELECT * FROM applabel_person'):
...     print(p)
```
上述代码运行后，我们能够得到
<pre>
John Smith
Jane Jones
</pre>

而有 ORM 的情况下，我们一般写
```python
people = Person.objects.all()
```

Tutorial Walkthrough
--------------------
[Writing your first Django app, part 1](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)

部分示例代码在 [`wk13example`](https://github.com/ShanghaitechGeekPie/events-IntroToWebDev-Fall17/tree/master/week13_backendIntro/wk13example) 文件夹下

### 基本概念

* project
* app

### 本次 Lab 步骤

* `django-admin startproject [project_name]`
* `cd [project_name]/`
* `python3 manage.py startapp [app_name]`
* 修改 `models.py`
* 修改 `./[app_name]/urls.py`
* 修改 `./[project_name]/urls.py`，增加导向 `[app_name].urls` 的 `urlpattern`
  * `from django.urls import include`
  * `urlpatterns += path('[app_url]/', include('[app_name].urls'))`
* 在 `[project_name]/settings.py` 中，`INSTALLED_APPS += '[app_name].apps.[AppName]Config'`
* `python3 manage.py makemigrations [app_name[]]`
* `python3 manage.py migrate`
* 数据库基础建设到此完成
* 为了使用自带后台管理界面，
  * 在 `[app_name]/admin.py` 内注册 `model`
  * `python3 manage.py createsuperuser`
  * `python3 manage.py runserver`
  * 访问对应路径，登陆管理界面
  * 使用管理界面，试着添加 dummy 数据
* 通过改写 `urls.py` 和 `views.py` 对接路由与响应
* 在 `views.py` 中实现各类功能

> demo 中 `/polls/<int:q_id>/` 返回的 `JsonResponse` 是 `unicode-escaped` 处理后的内容。在 JavaScript 中使用 `JSON.dump()` 配合其他函数可以变回正常的中文显示。

发布前注意事项
-------------

### `SECRET_KEY`
这个变量内的随机字符串会被用来给各类 hash 加盐，也有其他安全目的的作用。为了保证安全，发布前要将其去除，以其他方式提供给最终用户。比如，设置环境变量等。

### `.gitignore`
不要将 `.sqlite3` 文件、`.pyc` 等文件计入 Git 历史中，也尽量不要包括 `migration` 这类可以通过命令自动生成的文件。

### pip: `requirement.txt`
一般正式作品可能会包含 Django 以外的各类依赖，最好编写 `requirement.txt` 放在项目目录下。

### 改用 `virtualenv`
Virtualenv 能构造隔离开的开发环境，具体安装过程可以参考 [Getting a copy of Django’s development version](https://docs.djangoproject.com/en/2.0/intro/contributing/#getting-a-copy-of-django-s-development-version)

