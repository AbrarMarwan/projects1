import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from tensorflow.python.ops.gen_math_ops import xlogy

# تحميل بيانات Iris
iris = load_iris()

print(iris)
X = iris.data
y = iris.target
#+
# تقسيم البيانات إلى مجموعات تدريب وتحقق واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=42)
# توسيع نطاق الميزات
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)
print(X_test)
# تصميم بنية MLP بسيطة
model = models.Sequential()
#
# # إضافة طبقة مخفية مع 10 خلايا عصبية ودالة تنشيط ReLU
model.add(layers.Dense(10, activation='relu', input_shape=(X_train.shape[1],)))
#
# # إضافة طبقة إخراج مع 3 خلايا عصبية (عدد الفئات) ودالة تنشيط Softmax
model.add(layers.Dense(3, activation='softmax'))
#
# # تهيئة النموذج باستخدام خوارزمية Adam ودالة خسارة فئة التصنيف
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#
# # تدريب النموذج
history = model.fit(X_train, y_train, epochs=115, batch_size=2, validation_data=(X_val, y_val))
#
# # تقييم النموذج على مجموعة الاختبار
test_loss, test_acc = model.evaluate(X_train, y_train, verbose=2)
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)

print(f"Test accuracy: {test_acc:.4f}")
