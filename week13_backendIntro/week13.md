第13周

初识后端：请求、MVC、ORM
=======================

安装 pip 和 Django
------------------
* 安装 pip：https://pip.pypa.io/en/stable/installing/
* 安装 Django：`sudo pip3 -H install django`（从 2.0 起 Django 不支持 Python 2.X）

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

MVC（Model-View-Controller）模型 
--------------------------------

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
