![image-20230319221719219](C:\Users\Tiny\AppData\Roaming\Typora\typora-user-images\image-20230319221719219.png)

https://docker.easydoc.net/doc/81170005/cCewZWoN/N9VtYIIi  docker入门



 docker run -it -p 9000:8000 --name mysite2 -v F:\mytest\mytest/app -d django_docker_img:v1

这里不能带/app，挂载目录会报错

docker exec -it mysite4 /bin/bash



