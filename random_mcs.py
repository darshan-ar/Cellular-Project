import numpy as np
import random

def calculate(B,M):
    '''
    Method to calculate the Number of RBs required to achieve the required data rate using random MCS level
    :param B: numpy list :: Single list containing all the BS's RB's channel conditions
    :param M: numpy list :: List containing data rate requirement for each MVNO
    :return: int,int :: number of allocated RBs and number of unserved MVNOs
    '''
    print("RB allocation through random MCS selection")
    count=0
    M.sort(reverse=True)
    random_mcs= random.choice(B)
    new_B=[i for i in B if i>=random_mcs]
    B_status= np.zeros(len(new_B),dtype='int32')
    B_status=B_status.tolist()
    m_marked = np.zeros(len(M), dtype='int32')
    m_marked = m_marked.tolist()
    for k,m in enumerate(M):
        if random_mcs*len(new_B)<=m:
            print("MVNO data rate of {} cannot be achieved with this mcs selection policy".format(m))
        else:
            for n in range(len(new_B)):
                if n*random_mcs>=m and n<=B_status.count(0):
                    print("{} RB's with mcs {} was used to achieve data rate of {}".format(n,random_mcs,m))
                    count+=n
                    m_marked[k] = 1
                    for p in range(n):
                        B_status[p] = 1
                    break

    return count,m_marked.count(0)




