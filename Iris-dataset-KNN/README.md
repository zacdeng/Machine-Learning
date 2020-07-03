# KNN分类在Iris Dataset中的应用

* Question1

Iris 也称鸢尾花卉数据集,包含 150 个数据,每个数据包含 4 个属性花 萼⻓度、花萼宽度、花瓣⻓度、花瓣宽度 (sepal_length,sepal_width,petal_length,petal_width) ,可通过这 4 个 属性预测鸢尾花卉属于( Setosa , Versicolour , Virginica )三个种类 中的哪⼀类。 加载数据集的⽅式为

from sklearn.datasets import load_iris 

iris = load_iris() 

X = iris.data 

# 

y = iris.target

(1)在同⼀图中，以花萼⻓度，花萼宽度为横纵坐标，画出三种类别 的分布散点图 

![1](https://github.com/zacdeng/Image-hosting-service/raw/master/Machine%20Learning/I2.png)

(2)使⽤散点图绘制不同种类之间花萼与花瓣(⻓乘以宽)的关系。使⽤ 不同颜⾊标记不同种类,并添加相应的坐标轴标记和图例。 

![2](https://github.com/zacdeng/Image-hosting-service/raw/master/Machine%20Learning/I3.png)

* Question2

鸢尾花数据集分类 鸢尾花数据集简介，加载⽅法如题6，⾃⼰编写KNN算法对数据进⾏ 分类，打印分类准确率。

![result](https://github.com/zacdeng/Image-hosting-service/raw/master/Machine%20Learning/I1.png)