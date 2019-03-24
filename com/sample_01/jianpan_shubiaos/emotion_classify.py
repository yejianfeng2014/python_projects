#-*- coding :utf-8 -*-

from keras.preprocessing import sequence

from keras.models import  Sequential

from  keras.layers import  Dense ,Embedding

from keras.layers import  LSTM


from  keras.datasets import  imdb


#最多使用的单词数

max_features = 20000

# 循环网络的截断长度

maxlen = 80


batch_size = 32

(train_x,train_y),(text_x,text_y) = imdb.load_data(num_words=maxlen)


print(len(train_x))

print(len(train_y))

print('>>>>>>>')

print(len(text_x))
print(len(text_y))

import  tensorflow as tf


# 截断处理

train_pad_x = sequence.pad_sequences(train_x,maxlen)


text_pad_x = sequence.pad_sequences(text_x,maxlen=maxlen)


print(train_pad_x.shape)
print(text_pad_x.shape)


#数据预处理结束，开始建模


print(train_pad_x[0])

print(train_x[0]) #输出的是第一个数据


print(train_x) # 大小是25000


model = Sequential()

# embedding 向量维度是 128
model.add(Embedding(max_features,128))


#构建lstm

model.add(LSTM(128,dropout= 0.2,recurrent_dropout= 0.2))


model.add(Dense(1,activation='sigmoid'))


model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])


model.fit(x=train_pad_x,y = train_y,batch_size=batch_size,
          epochs= 2,
          validation_data=(text_pad_x,text_y))

score = model.evaluate(text_pad_x,y= text_y,batch_size=batch_size)

print('test loss :',score[0])
print('test accuracy: ',score[1])

#
# 对于网络结构，我们采用3层全向连接的，输入层有4个节点，隐含层有10个节点，输出层有3个节点的网络。其中，隐含层的激活函数为relu（rectifier），输出层的激活函数为softmax。损失函数则相应的选择categorical_crossentropy(此函数来着theano或tensorflow，具体可以参见这里)（二分类的话一般选择activation=‘sigmoid’， loss=‘binary_crossentropy’）。
# PS：





