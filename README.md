# InstructData

## 1. 简介
InstructData是一个用于数据标注的工具，是个人在工作中的一个小工具。目前主要用于评分模型数据的标注，后续会逐渐支持更多的数据类型。

## 2. 使用
安装pyside6
```shell
pip install pyside6
```
运行
```shell
python main.py
```

## 3. 功能
目前仅支持评分模型数据的标注，接受指定格式的数据，请参考data文件夹下的示例数据。
图形化操作，将评分写入json文件中。
- 需要更换数据格式请参考utils中的handler类型