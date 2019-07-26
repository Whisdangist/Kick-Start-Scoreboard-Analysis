# Kick Start Scoreboard Analysis

## 简介
早(zhong)上(wu)起床刷知乎，刷到了一个问题，叫“在谷歌中国实习是种什么样的体验？”。看到众多实习大佬的回答，顿生羡慕，于是找了谷歌实习的公众号，发现了这个谷歌举办的比赛: Kick Start. 看到了上轮比赛排行榜上众多大佬，想了解下国内占比是否很多，高分段低分段国家占比是否有差异，以便开始入手刷题之前了解一下敌情。于是乎就写了两个脚本，一个爬数据，另一个做简单的数据分析。

## 数据源
[Kick Start Round C 2019](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff2)

## 代码环境
python2  
matplotlib==2.1.2  # 这个我直接安装的2.2.4版本会报错: Matplotlib support failed, 所以降到了这个版本

## 补充说明
1. 这里附的json文件并不是爬虫脚本生成的。原始生成的json文本不含空白字符，为了看起来舒服一些，我在Sublime Text 3中用[Sublime-HTMLPrettify](https://github.com/victorporof/Sublime-HTMLPrettify)这个插件做了下处理。
2. 爬虫脚本里对base64的处理采用的是URL安全版的，和标准base64有点区别，一开始坑了我好久，就像这样一直报错：
```
>>> import base64
>>> base64.b64decode('IueOi-eQmyIs')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "D:\Python27\lib\base64.py", line 78, in b64decode
    raise TypeError(msg)
TypeError: Incorrect padding
```
后来我发现：
```
>>> base64.b64encode('"王琛",')
'IueOi+eQmyIs'
>>> base64.urlsafe_b64encode('"王琛",')
'IueOi-eQmyIs'
```
