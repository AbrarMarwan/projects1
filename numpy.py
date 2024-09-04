
import numpy as np
print("E1")
ls=[[1,2,3,4],[5,6,7,8],[7,8,9,10]]
array=np.array(ls)
print(ls)
print(array)
#
# print("\n\n\n")
# print("E2")
# arange=np.arange(1,15)#هنا يطبع ماداخل الرنج بدون for
# print(arange)
# a=range(0,10)#هنا يطبع الرنج نفسها بدون الاعداد الي داخل
# print(a)
# arange=np.arange(1,15,3)
# print(arange)
#
# print("\n\n\n")
# print("E3")
# z=np.zeros(3)#هنا الصف يعتبر واحد والاعمدة 3
# print(z)
# z=np.zeros((3,4))#هنا بيكون 3 صفوف و4 اعمدة
# print(z)
#
# print("\n\n\n")
# print("E4")
# r=np.random.rand(3)#randomفيها العديد من الدوال منها rand وكلها يكون الهدف منهم رقم عشوائي
# #ارقام عشوائية تترواح مابين الواحد والصفر ورقم 3 يعني انه يعطيني 3 ارقام  rand
# print(r)
# r=np.random.rand(2,4)#حددنا ك ماتركس مصفوفة من صفوف واعمدة
# print(r)
#
# print("\n\n\n")
# print("E5")
# r=np.random.randint(50)#  يطبع لك عدد صحيح وليس عدد عشري زي rand ويكون العدد موجب
# print(r)
# r=np.random.randint(5,15)
# print(r)
# #من قبل كان يطلع  لك رقم واحد ولكن لو تشتي اكثر من واحد لازم احدد بالاخير
# r=np.random.randint(5,15,3)
# print(r)
# r=np.random.randint(5,15,(3,2))
# print(r)
#
# print("\n\n\n")
# print("E6")
# no_shape=np.random.randint(100,200,10)
# shape=no_shape.reshape(5,2)
#              #row*colum=10 ولاااازم يكون 10 على حجم الاعداد الذي اخترتهم من قبل
#
# print(no_shape)
# print("\n")
# print(shape)
# shape=no_shape.reshape(10,1)
# #المهم انه اذ ضربت الصفوف في الاعمدة بيطلع الحجم للمصفوفة تبعك
# print("\n")
# print(shape)
#
# print("\n\n\n")
# print("E7")
# numbers = np.arange(1,10)
# print(numbers)
# print("\n")
# np.random.shuffle(numbers)#ماخزنته في متغير عشانه التغير حصل في الارقام ف صارت العملية عليه على طول ووظيفتها انه تلخبط الترتيب
# print(numbers)
#
# print("E8")
# # نسوي كود كذا يجمع بالعمليات الاولى
# print("\n")
# numbers = np.arange(1,11)
# print(numbers)
# print("\n")
# numbers_reshape=numbers.reshape(5,2)
# print(numbers_reshape)
# print("\n")
# np.random.shuffle(numbers_reshape)#ماخزنته في متغير عشانه التغير حصل في الارقام ف صارت العملية عليه على طول ووظيفتها انه تلخبط الترتيب
# print(numbers_reshape)
#
# print("\n\n\n")
# print("E9")
# #معرفة بيانات داخل المصفوفة
# numbers=np.random.randint(1,20,(5,2))
# print(numbers)
# ma=numbers.max()
# mi=numbers.min()
# print(ma)
# print(mi)
# list=[1,2,8,66]
# print(max(list))
# print(min(list))
# max_index=numbers.argmax()
# print(max_index)
# min_index=numbers.argmin()
# print(min_index)
# shape=numbers.shape
# print(shape)
# shape=numbers.shape[0]#rows just
# print(shape)
# shape=numbers.shape[1]#colum
# print(shape)
#
# print("\n\n\n")
#
# print("E10")
# c=np.ceil(2.3)
# print(c)
# #3.0
# c=np.floor(2.3)
# print(c)
# #2.0
# r1=np.round(2.3)
# print(r1)
# #2.0
# r2=np.round(2.6)
# print(r2)
# #3.0
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# add=np.add(matrix,2)
# print(add)
# #تزود للمصفوفة اثنين
