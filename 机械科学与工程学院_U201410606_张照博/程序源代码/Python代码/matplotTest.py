import numpy as np  
import matplotlib.pyplot as plt  



##########################三条曲线对照图##########################
# evenly sampled time at 200ms intervals 
# x = [200,400,800,1000,2000,3000,4000,5000,6000,8000,10000,12000,15000,17500,20000,22500,25000,27500,30000,32500,35000,37500,40000,42500,45000,47500,50000,52500,55000,57500,60000,62500,65000,67500,70000,72500,75000,77500,80000,82500,85000,87500,90000,92500,95000,97500,100000,110000,120000,125000,130000,140000,150000,160000,175000,]
# y1 = [33.0,30.0,36.0,37.2,31.7,34.0,35.5,37.6,36.1,37.8,40.3,42.4,35.7,40.0,46.1,42.1,42.0,45.1,45.6,48.3,45.6,48.3,48.7,46.8,48.0,48.0,46.8,46.9,48.3,49.6,49.2,48.9,49.0,50.0,51.9,48.9,50.4,53.2,53.3,50.7,50.9,51.4,50.1,51.9,51.6,53.2,52.1,51.2,53.6,51.7,54.7,54.4,53.5,54.4,56.3,]
# y2 = [61.1,58.5,51.1,54.3,53.0,56.5,54.3,57.1,52.2,57.3,54.6,54.0,54.5,57.0,56.4,56.6,56.2,56.3,56.2,56.7,55.3,56.3,57.5,55.7,57.0,57.0,56.3,55.2,56.1,57.7,56.7,55.8,58.1,57.6,57.4,57.7,57.8,58.4,57.8,57.4,58.2,58.4,56.5,58.2,57.7,59.7,57.5,57.0,58.0,56.0,58.0,57.7,57.7,59.4,58.3,]
# y3 = [32.4,57.4,49.6,59.5,51.3,51.8,52.7,54.0,51.0,52.7,48.9,49.1,48.6,49.7,49.0,49.6,49.7,50.7,48.6,48.6,48.5,48.7,47.6,48.3,48.5,47.2,47.4,47.2,48.7,46.7,47.6,48.0,46.4,48.0,46.1,47.2,47.1,47.3,48.6,46.2,46.3,45.7,46.1,46.5,46.7,44.9,46.3,47.4,47.2,47.6,47.1,47.8,46.6,45.3,48.5,] 
# plt.plot(x,y1,color = 'red',linestyle = '-',label = 'Accuracy')
# plt.plot(x,y2,color = 'blue',linestyle = '-.',label = 'Precision')
# plt.plot(x,y3,color = 'green',linestyle = ':',label = 'Recall')
# plt.xlabel('Data Amount')
# plt.ylabel('Percentage (%)')
# plt.legend(loc='lowwer right')  
# plt.show()  
##########################三条曲线对照图##########################



##########################查全率、查准率精度变化图##########################
# x = [3000,4000,5000,6000,8000,10000,12000,15000,17500,20000,22500,25000,27500,30000,32500,35000,37500,40000,42500,45000,47500,50000,52500,55000,57500,60000,62500,65000,67500,70000,72500,75000,77500,80000,82500,85000,87500,90000,92500,95000,97500,100000,110000,120000,125000,130000,140000,150000,160000,175000,]
# y2 = [56.5,54.3,57.1,52.2,57.3,54.6,54.0,54.5,57.0,56.4,56.6,56.2,56.3,56.2,56.7,55.3,56.3,57.5,55.7,57.0,57.0,56.3,55.2,56.1,57.7,56.7,55.8,58.1,57.6,57.4,57.7,57.8,58.4,57.8,57.4,58.2,58.4,56.5,58.2,57.7,59.7,57.5,57.0,58.0,56.0,58.0,57.7,57.7,59.4,58.3,]
# y3 = [51.8,52.7,54.0,51.0,52.7,48.9,49.1,48.6,49.7,49.0,49.6,49.7,50.7,48.6,48.6,48.5,48.7,47.6,48.3,48.5,47.2,47.4,47.2,48.7,46.7,47.6,48.0,46.4,48.0,46.1,47.2,47.1,47.3,48.6,46.2,46.3,45.7,46.1,46.5,46.7,44.9,46.3,47.4,47.2,47.6,47.1,47.8,46.6,45.3,48.5,] 
# plt.plot(x,y2,color = 'blue',linestyle = '-.',label = 'Precision')
# plt.plot(x,y3,color = 'green',linestyle = ':',label = 'Recall')
# plt.xlabel('Data Amount')
# plt.ylabel('Percentage (%)')
# plt.legend(loc='upper left')  
# plt.title('Comparative Analysis',color='black') 
# plt.annotate('Precision', xy=(63000, 55.5), xytext=(70000, 53), arrowprops=dict(facecolor='blue', shrink=0.01), )  
# plt.annotate('Recall', xy=(55000, 49), xytext=(70000, 51), arrowprops=dict(facecolor='green', shrink=0.01), )  
# plt.show()
##########################查全率、查准率精度变化图##########################






# ##########################P-R图##########################
# y2 = [61.1,58.5,51.1,54.3,53.0,56.5,54.3,57.1,52.2,57.3,54.6,54.0,54.5,57.0,56.4,56.6,56.2,56.3,56.2,56.7,55.3,56.3,57.5,55.7,57.0,57.0,56.3,55.2,56.1,57.7,56.7,55.8,58.1,57.6,57.4,57.7,57.8,58.4,57.8,57.4,58.2,58.4,56.5,58.2,57.7,59.7,57.5,57.0,58.0,56.0,58.0,57.7,57.7,59.4,58.3,]
# y3 = [32.4,57.4,49.6,59.5,51.3,51.8,52.7,54.0,51.0,52.7,48.9,49.1,48.6,49.7,49.0,49.6,49.7,50.7,48.6,48.6,48.5,48.7,47.6,48.3,48.5,47.2,47.4,47.2,48.7,46.7,47.6,48.0,46.4,48.0,46.1,47.2,47.1,47.3,48.6,46.2,46.3,45.7,46.1,46.5,46.7,44.9,46.3,47.4,47.2,47.6,47.1,47.8,46.6,45.3,48.5,] 
# y2=y2[20:]
# y3=y3[20:]
# plt.plot(y2,y3,color = 'blue',linestyle = ':')
# plt.xlabel('Precision')
# plt.ylabel('Recall')
# plt.legend(loc='lowwer right')  
# plt.show()  
##########################P-R图##########################


##########################决策树精度变化图##########################
# x = [200,400,800,1000,2000,3000,4000,5000,6000,8000,10000,12000,15000,17500,20000,22500,25000,27500,30000,32500,35000,37500,40000,42500,45000,47500,50000,52500,55000,57500,60000,62500,65000,67500,70000,72500,75000,77500,80000,82500,85000,87500,90000,92500,95000,97500,100000,110000,120000,125000,130000,140000,150000,160000,175000,]
# y1 = [33.0,30.0,36.0,37.2,31.7,34.0,35.5,37.6,36.1,37.8,40.3,42.4,35.7,40.0,46.1,42.1,42.0,45.1,45.6,48.3,45.6,48.3,48.7,46.8,48.0,48.0,46.8,46.9,48.3,49.6,49.2,48.9,49.0,50.0,51.9,48.9,50.4,53.2,53.3,50.7,50.9,51.4,50.1,51.9,51.6,53.2,52.1,51.2,53.6,51.7,54.7,54.4,53.5,54.4,56.3,]
# y2 = [61.1,58.5,51.1,54.3,53.0,56.5,54.3,57.1,52.2,57.3,54.6,54.0,54.5,57.0,56.4,56.6,56.2,56.3,56.2,56.7,55.3,56.3,57.5,55.7,57.0,57.0,56.3,55.2,56.1,57.7,56.7,55.8,58.1,57.6,57.4,57.7,57.8,58.4,57.8,57.4,58.2,58.4,56.5,58.2,57.7,59.7,57.5,57.0,58.0,56.0,58.0,57.7,57.7,59.4,58.3,]
# y3 = [32.4,57.4,49.6,59.5,51.3,51.8,52.7,54.0,51.0,52.7,48.9,49.1,48.6,49.7,49.0,49.6,49.7,50.7,48.6,48.6,48.5,48.7,47.6,48.3,48.5,47.2,47.4,47.2,48.7,46.7,47.6,48.0,46.4,48.0,46.1,47.2,47.1,47.3,48.6,46.2,46.3,45.7,46.1,46.5,46.7,44.9,46.3,47.4,47.2,47.6,47.1,47.8,46.6,45.3,48.5,] 
# plt.plot(x,y1,'rs')
# plt.title('DecisionTree',color='black')
# plt.xlabel('Data Amount')
# plt.ylabel('Accuracy (%)')
# plt.show()  
##########################决策树精度变化图##########################


##########################SVM精度变化图##########################
# x = [200,400,800,1000,2000,3000,4000,5000,6000,8000,10000,12000,15000,17500,20000,22500,25000,27500,30000,32500,35000,37500,40000,42500,45000,]
# y1 = [55.0,49.5,51.0,56.0,54.3,53.9,54.2,55.4,56.8,55.9,56.1,55.2,56.1,56.8,56.4,57.4,56.8,56.8,57.4,57.6,56.7,58.1,57.6,57.2,58.4,]
# plt.plot(x,y1,'rs')
# plt.title('Support Vector Machine',color='black')
# plt.xlabel('Data Amount')
# plt.ylabel('Accuracy (%)')
# # plt.plot(x,y1,color = 'red',linestyle = '-',label = 'Accuracy')
# plt.show() 
##########################SVM精度变化图##########################



##########################精度变化对比分析图##########################
# x = [200,400,800,1000,2000,3000,4000,5000,6000,8000,10000,12000,15000,17500,20000,22500,25000,27500,30000,32500,35000,37500,40000,42500,45000,]
# y1 = [55.0,49.5,51.0,56.0,54.3,53.9,54.2,55.4,56.8,55.9,56.1,55.2,56.1,56.8,56.4,57.4,56.8,56.8,57.4,57.6,56.7,58.1,57.6,57.2,58.4,]
# x1 = [200,400,800,1000,2000,3000,4000,5000,6000,8000,10000,12000,15000,17500,20000,22500,25000,27500,30000,32500,35000,37500,40000,42500,45000,47500,50000,52500,55000,57500,60000,62500,65000,67500,70000,72500,75000,77500,80000,82500,85000,87500,90000,92500,95000,97500,100000,110000,120000,125000,130000,140000,150000,160000,175000,]
# y2 = [33.0,30.0,36.0,37.2,31.7,34.0,35.5,37.6,36.1,37.8,40.3,42.4,35.7,40.0,46.1,42.1,42.0,45.1,45.6,48.3,45.6,48.3,48.7,46.8,48.0,48.0,46.8,46.9,48.3,49.6,49.2,48.9,49.0,50.0,51.9,48.9,50.4,53.2,53.3,50.7,50.9,51.4,50.1,51.9,51.6,53.2,52.1,51.2,53.6,51.7,54.7,54.4,53.5,54.4,56.3,]
# s1 = []
# count = 0
# sy1 = []
# while count<len(x):
#     s1.append(x1[count])
#     sy1.append(y2[count])
#     count+=1
# plt.plot(x,y1,'r',s1,sy1,'b')
# plt.title('Comparative Analysis',color='black') 
# plt.annotate('SVM', xy=(12000, 54.5), xytext=(15000, 50), arrowprops=dict(facecolor='red', shrink=0.01), )  
# plt.annotate('DecisionTree', xy=(17000, 38), xytext=(20000, 33), arrowprops=dict(facecolor='blue', shrink=0.01), )  
# plt.xlabel('Data Amount')
# plt.ylabel('Accuracy (%)')
# # plt.plot(x,y1,color = 'red',linestyle = '-',label = 'Accuracy')
# plt.show()  
##########################精度变化对比分析图##########################
