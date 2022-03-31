'''
@author neelkant newra
date: 28.03.22

Program to execute varying temperature according to time

'''
import time

def TempChange(initial:int, final:int, value:int ,sleep_time:float,decrement = True):
    '''
    Parameter
    ---------
    initial : initial value of temperature
    final : final value of temperature
    value : value of temperature to be increase or decrease
    sleep_time : Time after which value changes(second)
    decrement : True --> decrement; False --> increment
    
    return
    ------
    generator : representing the temperature increase/decrease
    
    '''
    
    if decrement == True:
        while initial>final:
            time.sleep(sleep_time) #sleep
            initial-=value
            yield 'Current Temperature is: {}'.format(initial)
    else:
        while initial<final:
            time.sleep(sleep_time) #sleep
            initial+=value
            yield 'Current Temperature is: {}'.format(initial)


# demo for output
#for _ in TempChange(initial=10,final=55,value=10,sleep_time=2,flag=False):
#    print(_)
