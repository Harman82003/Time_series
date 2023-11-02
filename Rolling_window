def make_windows1(y_train,horizonnn,windowww):
    grouped_values=[]
    horizon1=[]
    y_train=np.array(y_train)
    y_train1=np.array(y_train)

    for i in range(0, len(y_train)-(horizonnn)-windowww+1):     #assume horizon to be 7):
            window = y_train[i:i + horizonnn]
    
            grouped_values.append(window)
       

           #     for i in range(0, len(y_train)-(horizonnn)):
            horizon = y_train1[i + horizonnn:i+horizonnn+windowww]
            horizon1.append(horizon)


         
                 
        
    grouped_values=np.array(grouped_values)
    horizon1=np.array(horizon1)
    return (grouped_values,horizon1)
