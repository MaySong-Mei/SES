import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def fill_datagap(d, intensity=100, report=False, show=True, reorder=True):
    '''
    This function is to fill the gaps for high slope missing data
    :param d: np array
    :param intensity: level of adding miss data
    :param report: print debug
    :param show: graph visualization
    :param reorder: reorder the processed data based on x-axis
    :return: np array that is filled with gaps
    '''
    d_copy = d.copy().T
    d = d.tolist()
    count = 0
    for i in range(len(d[0])):
        if i == len(d[0])-1:
            break
        else:
            deltax = math.fabs(d[0][i] - d[0][i+1])
            deltay = d[1][i + 1] - d[1][i]
            number_tobe_added = int((math.fabs(deltay/deltax)*intensity)**0.4)  # hardcode here
            if not number_tobe_added:
                continue

            count += number_tobe_added
            height = deltay/number_tobe_added
            step = deltax/number_tobe_added

            if report:
                print("Processing the {}th data".format(i))
                print("Data is (%f,%f), (%f,%f)"%(d[0][i], d[1][i], d[0][i+1], d[1][i+1]))
                print("Delta x,y is ", deltax, deltay)
                print("--------------------")
                print("We will added {} new data".format(number_tobe_added))
            for m in range(number_tobe_added):
                if report:
                    print("Increase by ", step * m, height * m)
                    print("Finished with ", d[0][i]+step*m, d[1][i]+height*m)

                d_copy = np.append(d_copy,[[d[0][i]+step*m,d[1][i]+height*m]],axis=0)
    if report:
        print(d_copy.shape)
    if show:
        plt.scatter(d_copy.T[0][:len(d[0])], d_copy.T[1][:len(d[0])], s=1)
        plt.scatter(d_copy.T[0][len(d[0])+1:], d_copy.T[1][len(d[0])+1:], s=0.2)
        plt.show()
    if reorder:
        d_copy = pd.DataFrame(d_copy, columns=['x', 'y']).sort_values(by=['x']).values
    return d_copy.T


def get_prepdata(filename:str, show=False):
    '''
    Just like the name mentioned, this is a data preprocessing function that allow user to
    sort the data, normalize the data
    Notably this one will drop the duplicated data
    :param filename: name of local csv file to be processed
    :param show: draw graph for visualization
    :return: np array that is processed
    '''

    df = pd.read_csv(filename)
    df = df.sort_values(by=['x'])
    df = df.drop_duplicates(subset=['x'])

    # apply normalization techniques
    df['y'] = (df['y'] - df['y'].min())/\
              (df['y'].max() - df['y'].min())
    df = df.values.transpose()

    if show:
        plt.scatter(df[0], df[1], s=1)
        plt.show()

    return df

def batch_fill():
    #TODO
    raise NotImplemented



if __name__ == "__main__":
    #  Test cases
    d_BaMnO3 = get_prepdata("b.csv")
    d = fill_datagap(d_BaMnO3, intensity=100)
    pd.DataFrame(d.T).to_csv('b_2.csv', index=False)