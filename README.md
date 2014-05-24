#django_werobot

###关于项目
使用werobot作为微信后端,使werobot能存取django中的数据.

该项目稍加修改便可用于:需要在django之外使用django orm 的场合.

###quick guide
我们先让它跑起来看看效果.

```
pip install -r requirements.txt
python werobot_demo.py
```

###设计思路
*  以数据为中心,将werobot作为django与微信的中间人.
*  将werobot与django尽可能隔离

###使用场景
*  用户使用django admin增删数据,可反映到微信中.如此一来实际相当于微信的第三方后台.本质上是共用数据库
*  在django中建立存储正则规则的model,如此一来,用户可以直接在admin里写正则规则(关键字匹配等).
*  更多用法,发挥你的想象.你甚至可以把数据当做代码来用.如此一来用户在admin里拥有很高的自由度.
