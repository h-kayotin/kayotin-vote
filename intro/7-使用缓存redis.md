# 7-缓存

当一个网站的访问量很大时，制约访问速度的往往是关系型数据库的存取速度。优化web性能的一个主要手段就是使用缓存，将访问量大但数据量不大的数据存储在缓存服务器中。缓存服务器通常是采用hash存储直接将数据存储在内存中，比如可以使用redis来达到这样的目的。

### 接入Redis

Redis的安装不再赘述，如果需要在Django项目中接入Redis，可以使用三方库`django-redis`

```python
pip install django-redis==4.7.0
```

修改settings.py里的cache配置

```python
CACHES = {
    'default': {
        # 指定通过django-redis接入Redis服务
        'BACKEND': 'django_redis.cache.RedisCache',
        # Redis服务器的URL
        'LOCATION': ['redis://192.168.32.11:6379/0', ],
        # Redis中键的前缀（解决命名冲突）
        'KEY_PREFIX': 'vote',
        # 其他的配置选项
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            # 连接池（预置若干备用的Redis连接）参数
            'CONNECTION_POOL_KWARGS': {
                # 最大连接数
                'max_connections': 512,
            },
            # 连接Redis的用户口令
            'PASSWORD': 'abc@1234',
        }
    },
}
```

### 使用缓存（编程式缓存

通过`django-redis`提供的`get_redis_connection`函数直接获取Redis连接来操作Redis。

在views.py中增加如下方法：

```python
from django_redis import get_redis_connection
from django_redis.serializers import json

def show_subjects_red(request):
    """获取学科数据"""
    redis_cli = get_redis_connection()
    # 先尝试从缓存中获取学科数据
    data = redis_cli.get('vote:polls:subjects')
    if data:
        # 如果获取到学科数据就进行反序列化操作
        data = json.loads(data)
    else:
        # 如果缓存中没有获取到学科数据就查询数据库
        queryset = Subject.objects.all()
        data = SubjectSerializer(queryset, many=True).data
        # 将查到的学科数据序列化后放到缓存中
        redis_cli.set('vote:polls:subjects', json.dumps(data), ex=86400)
    return Response({'code': 20000, 'subjects': data})
```

我们在urls.py中加一条映射：

```python
urlpatterns = [
    path('api/sub_redis/', views.show_subjects_red),
]
```

> 我们可以访问api/sub_redis/测试是否可以拿到Json数据。注意启动服务器上的redis。
> 

### 缓存的更新(以下知识点请自行了解，这里仅简述)

当数据更新时，如何更新缓存中的数据，目前有以下几种方式

1. Cache Aside Pattern 当数据更新时，先更新数据库，再删除缓存
2. Read/Write Through Pattern Read Through指在查询操作中更新缓存，也就是说，当缓存失效的时候，由缓存服务自己负责对数据的加载，从而对应用方是透明的；而Write Through是指在更新数据时，如果没有命中缓存，直接更新数据库，然后返回。如果命中了缓存，则更新缓存，然后再由缓存服务自己更新数据库（同步更新）
3. Write Behind Caching Pattern 只更新缓存，不更新数据库。数据库的更新异步进行。可以大幅提升性能，但是会牺牲强一致性。

### 缓存的几个问题

由于缓存过期或请求缓存中没有的数据，大量并发直接访问数据库的问题。

1. 缓存穿透 
2. 缓存击穿
3. 缓存雪崩