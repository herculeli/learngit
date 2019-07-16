import numpy as np
import os
#os.chdir('/home/brown/code/liblinear-1.96/python')

from liblinearutil import *
#import liblinearutil



cc = [-1wdqqjnd0, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sdahsdb
sjhbdajhsbdj

#def calCorrcoef(x,y):
#    x=x.reshape((1,x.size))
    y=y.reshape((1,y.size))
    m=np.concatenate((x,y),axis=0)
    res=np.corrcoef(m)
    return res

def liblinearclassify(train_feature, test_feature, train_label, test_label):
    '''
    使用liblinear进行分类的函数，
    函数输入:train_feature, test_feature, train_label，test_label
    函数输出：预测的label信息，分类的准确率。
    进行了参数的选择，范围可以改变，目前的范围 s = 0 or 1, c = np.arange(1.5,10.5,0.5)
    '''
    train_new = train_feature.tolist()
    test_new = test_feature.tolist()
    train_label_new = train_label.T[0].tolist()
    test_label_new = test_label.T[0].tolist()
    corr_max = -2
    best_s = 0
    best_c = 0
    predicted_label = 0
    for s in np.arange(1):
#        for c in np.arange(1.5,10.5,0.5):
#            para = '-s %d -c %f -q'%(s,c)
#            # print(para)
#            model = train(train_label_new, train_new, para)
#            p_label, p, p_val = predict(test_label_new, test_new,model)
#            if p[0] > accmax:
#                accmax = p[0]
#                best_s = s
#                best_c = c
#                predicted_label = p_label
        for c in cc:
            para ='-s 11 -c %f -q'%(2**c)
            model = train(train_label_new, train_new, para)
            p_label, p,p_val = predict(test_label_new, test_new, model)
            cor_matrix=calCorrcoef(np.array(p_label), test_label)
        
        if cor_matrix[0][1] > corr_max:
                corr_max = p[0]
                best_s = s
                best_c = 2 ** c
                predicted_label = p_label
    return predicted_label,corr_max, best_c, best_s
