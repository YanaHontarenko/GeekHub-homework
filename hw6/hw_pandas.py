
# coding: utf-8

# <center>
# <img src="../../img/ods_stickers.jpg">
# ## Открытый курс по машинному обучению
# <center>
# Автор материала: Юрий Кашницкий, программист-исследователь Mail.Ru Group <br> 
# 
# Материал распространяется на условиях лицензии [Creative Commons CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Можно использовать в любых целях (редактировать, поправлять и брать за основу), кроме коммерческих, но с обязательным упоминанием автора материала.

# # <center>Домашнее задание № 1 (демо).<br> Анализ данных по доходу населения UCI Adult</center>

# **В задании предлагается с помощью Pandas ответить на несколько вопросов по данным репозитория UCI [Adult](https://archive.ics.uci.edu/ml/datasets/Adult) (качать данные не надо – они уже есть в репозитории).**

# Уникальные значения признаков (больше информации по ссылке выше):
# - age: continuous.
# - workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
# - fnlwgt: continuous.
# - education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
# - education-num: continuous.
# - marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
# - occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
# - relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
# - race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
# - sex: Female, Male.
# - capital-gain: continuous.
# - capital-loss: continuous.
# - hours-per-week: continuous.
# - native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.   
# - salary: >50K,<=50K

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('adult.csv')
data.head()


# **1. Сколько мужчин и женщин (признак *sex*) представлено в этом наборе данных?**

# In[ ]:


print(data[data['sex']=='Male']['sex'].count())
print(data[data['sex']=='Female']['sex'].count())


# **Ответ: 21790 мужчин и 10771 женщина.**

# **2. Каков средний возраст (признак *age*) женщин?**

# In[ ]:


print(data[data['sex']=='Female']['age'].mean())


# **Ответ: средний возраст женщин 36.85823043357163.**

# **3. Какова доля граждан Германии (признак *native-country*)?**

# In[ ]:


count_all = data.shape[0]
count_german = data[data['native-country']=='Germany']['sex'].count()
print(count_german/count_all*100)


# **Ответ:доля немцев в нашем наборе данных приблизительно 0.42%**

# **4-5. Каковы средние значения и среднеквадратичные отклонения возраста тех, кто получает более 50K в год (признак *salary*) и тех, кто получает менее 50K в год? **

# In[ ]:


less_50 = data[data['salary']=='<=50K']
greater_50 = data[data['salary']=='>50K']


# In[ ]:


print(less_50['age'].mean())
print(less_50['age'].std())


# In[ ]:


print(greater_50['age'].mean())
print(greater_50['age'].std())


# **Ответ:средние значение и среднеквадратичные отклонения возраста тех, кто получает более 50K в год равно 44.24984058155847 и 10.51902771985177 соответственно.
# Средние значение и среднеквадратичные отклонения возраста тех, кто получает менее 50K в год равно 36.78373786407767 и 14.020088490824813 соответственно.**

# **6. Правда ли, что люди, которые получают больше 50k, имеют как минимум высшее образование? (признак *education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters* или *Doctorate*)**

# In[ ]:


greater_50['age'].count()


# In[ ]:


greater_50_with_education = greater_50[((greater_50['education']=='Bachelors') | 
                                       (greater_50['education']=='Prof-school') | 
                                       (greater_50['education']=='Assoc-acdm') | 
                                       (greater_50['education']=='Assoc-voc') | 
                                       (greater_50['education']=='Masters') | 
                                       (greater_50['education']=='Doctorate'))]
greater_50_with_education['age'].count()


# **Ответ: как видно, количество людей с высшим образованием, которые получают больше 50К намного меньше, чем просто людей, которые получают больше 50К.**

# **7. Выведите статистику возраста для каждой расы (признак *race*) и каждого пола. Используйте *groupby* и *describe*. Найдите таким образом максимальный возраст мужчин расы *Amer-Indian-Eskimo*.**

# In[ ]:


data.groupby(['sex', 'race'])['age'].describe()


# **Ответ: максимальный возраст мужчин расы Amer-Indian-Eskimo 82 года**

# **8. Среди кого больше доля зарабатывающих много (>50K): среди женатых или холостых мужчин (признак *marital-status*)? Женатыми считаем тех, у кого *marital-status* начинается с *Married* (Married-civ-spouse, Married-spouse-absent или Married-AF-spouse), остальных считаем холостыми.**

# In[ ]:


greater_count = greater_50[greater_50['sex']=='Male']['age'].count()
greater_50_tmp = greater_50[greater_50['marital-status'].apply(lambda status: status[:7] == 'Married')]
greater_50_married_count = greater_50_tmp[greater_50_tmp['sex']=='Male']['age'].count()
greater_50_not_married_count = greater_count - greater_50_married_count


# In[ ]:


print(greater_50_married_count/greater_count*100)
print(greater_50_not_married_count/greater_count*100)


# **Ответ: доля зарабатывающих много(>50K) больше среди женатых мужчин**

# **9. Какое максимальное число часов человек работает в неделю (признак *hours-per-week*)? Сколько людей работают такое количество часов и каков среди них процент зарабатывающих много?**

# In[ ]:


data['hours-per-week'].max()


# In[ ]:


max_work_count = data[data['hours-per-week']==99]['age'].count()
max_work_count


# In[ ]:


max_work_50_count = data[((data['hours-per-week']==99) & (data['salary']=='>50K'))]['age'].count()
max_work_50_count


# In[ ]:


print(max_work_50_count/max_work_count*100)


# **Ответ: максимальное число часов работы человека 99. Такое число часов работают 85 человек, среди них 25 зарабатывают много(>50K) - 29.41%. **

# **10. Посчитайте среднее время работы (*hours-per-week*) зарабатывающих мало и много (*salary*) для каждой страны (*native-country*).**

# In[ ]:


import numpy as np


# In[ ]:


data.groupby(['salary', 'native-country'])['hours-per-week'].agg([np.mean])


# In[ ]:


get_ipython().system('jupyter nbconvert --to script hw_pandas.ipynb')

