# This code starter
# This is an update

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
# from sklearn.impute import IterativeImputer

def fill_data_1(d,hyper):
    d_copy = d.copy().T
    # print(d_copy.shape)
    # range_coeff = (d[1][len(d[0])] - d[1][0])/10000
    d = d.tolist()
    # d2 = d.copy()
    # length = len(d[0])
    count = 0
    for i in range(len(d[0])):
        if i == len(d[0])-1:
            # print(i)
            break
        else:
            deltax = math.fabs(d[0][i] - d[0][i+1])
            deltay = d[1][i + 1] - d[1][i]

            if deltax:
                print("!!!!!!!")
                print(deltax, deltay, deltay/deltax)
                number_tobe_added = int((math.fabs(deltay/deltax)*hyper)**0.4) # hardcode here
                print("Processing the {}th data".format(i))

            else:
                number_tobe_added = 0
            if number_tobe_added>0:
                count+=number_tobe_added
                height = deltay/number_tobe_added
                step = deltax/number_tobe_added
                print("Data is (%f,%f), (%f,%f)"%(d[0][i],d[1][i],d[0][i+1],d[1][i+1]))
                print("Delta x,y is ", deltax, deltay)
                print("--------------------")
                print("We will added {} new data".format(number_tobe_added))
                for m in range(number_tobe_added):
                    print("Increase by ", step * m, height * m)
                    print("Finished with ", d[0][i]+step*m, d[1][i]+height*m)

                    d_copy = np.append(d_copy,[[d[0][i]+step*m,d[1][i]+height*m]],axis=0)
            else:
                pass
                # print("No new data added")
            # print("{} data added".format(number_tobe_added))
            # print(len(d[0]))
    print(d_copy.shape)
    return d_copy.T






if __name__ == "__main__":
    # print("Hello World")
    df = pd.read_csv("b.csv")
    # df = pd.DataFrame(df, columns=['index','x','y'])
    df = df.sort_values(by=['x'])
    df = df.drop_duplicates(subset=['x'])

    # copy the data
    df_min_max_scaled = df.copy()

    # apply normalization techniques
    df_min_max_scaled['y'] = (df_min_max_scaled['y'] - df_min_max_scaled['y'].min()) / \
                             (df_min_max_scaled['y'].max() - df_min_max_scaled['y'].min())

    d_BaMnO3 = df_min_max_scaled.values.transpose()
    # d_BaMnO3 = df.values.transpose()

    # plt.plot(d_BaMnO3)
    plt.scatter(d_BaMnO3[0], d_BaMnO3[1], s=1)
    plt.show()
    # print(d_BaMnO3.values.transpose())
    d = fill_data_1(d_BaMnO3,100)

    plt.scatter(d[0][:269],d[1][:269],s=1)
    plt.scatter(d[0][270:], d[1][270:], s=0.1)

    # plt.scatter(d[0][:269],d[1][:269],s=1)
    # plt.scatter(d[0][270:], d[1][270:], s=0.1)
    plt.show()

    pd.DataFrame(d.T).to_csv('b_2.csv', index=False)

#TODO
#增点以后，定步长取点

#TODO
#Normalization DONE


