# YouTube converter 

## Description 
This is online converter for youtube videos,
that allows you to convert video file to mp3 format.
Project works in asynchronous manner using celery and redis. 

## Installation
```
$ git clone https://github.com/nadyrbek97/youtube_converter
$ virtualenv venv -p python3
$ source venv/bin/activate
$ cd converter
$ pip install -r requirements.txt

```


## Theoretical Part 
### Redis 
**What is Redis?**
``` 
Redis (REmote DIctionary Server) is an in-memory, key-value database,
commonly referred to as a data structure server. One of the key differences
between Redis and other key-value databases is Redis’s ability to store
and manipulate high-level data types. These data types are fundamental
data structures (lists, maps, sets, and sorted sets) that most developers
are familiar with. Redis’s exceptional performance, simplicity, and atomic
manipulation of data structures lends itself to solving problems that are
difficult or perform poorly when implemented with traditional relational
databases.
```




### Celery 
**What is Celery?**
```
Celery is a distributed task queue that can process vast amounts of
messages. It does real-time processing but also supports task
scheduling. Using Celery, not only can you create asynchronous
tasks easily and let them be executed by workers as soon as
possible, but you can also schedule them to run at a specific time.
```
**Why do we need Celery?**
```
Everything you execute in a view affects response times. In many
situations, you might want to return a response to the user as
quickly as possible and let the server execute some process
asynchronously. This is especially relevant for time-consuming
processes or processes subject to failure, which might need a retry
policy. For example, a video sharing platform allows users to upload
videos but requires a long time to transcode uploaded videos. The
site might return a response to users to inform them that the
transcoding will start soon, and start transcoding the video
asynchronously. Another example is sending emails to users. If your
site sends email notifications from a view, the SMTP connection
might fail or slow down the response. Launching asynchronous
tasks is essential to avoid blocking the code execution.
    Ru
Не используйте базу данных в качестве broker/backend
Брокер отвечает за передачу сообщений (задач) между так называемыми
исполнителями (workers). Проблема использования базы данных заключается
в её ограничениях - она просто не предназначена для этого.
Дело в том, что с ростом количества исполнителей, нагрузка на базу будет
только возрастать, а учитывая тот факт, что каждый worker имеет ещё ряд потоков, ситуация может стать катастрофической даже при малых нагрузках.
Всё это приведёт к бутылочному горлышку в виде затыка на I/O, потере задач,
а возможно и неоднократному их исполнению (два воркера могут получить одну и ту же задачу на исполнение).
Отличным production-ready решением является использование RabbitMQ или Redis для этой роли.

```

**How does Celery work?**
``` 
Celery works as a queue
```

**How does Celery work with Redis?**
```

```

**What are workers in celery?**
```
Celery workers, which process tasks as they receive them. Let's
install a message broker.
```

**In which data types Data is passed in workers?**
```

Ru
Worker celery должны быть перезапущены каждый раз,
когда производится изменение кода, связанного с задачей celery.

```