for i in range(-10, 10):
    for k in range(-10, 10):
        #print('x^2 + ' + str(i + k) + 'x + ' + str(i * k) + ': constants are (' + str(i) + ', ' + str(k) + ')')
        if (abs(i * k) < abs(i + k)):
            print('x^2 + ' + str(i + k) + 'x + ' + str(i * k) + ': constants are (' + str(i) + ', ' + str(k) + ')')
        #if (abs(i * k) == abs(i + k)):
            #print('x^2 + ' + str(i + k) + 'x + ' + str(i * k) + ': constants are (' + str(i) + ', ' + str(k) + ')')
