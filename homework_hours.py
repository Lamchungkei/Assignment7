# Created by: Kay Lin 
# Created on: 1st-Dec-2017
# Created for: ICS3U
# This program displays finding your maximum homework hours and minimum homework hours
# in last five days

import ui

#your_hours = 0
homework_hours = []

def check_button_touch_up_inside(sender):
    #input your homework hours and send to array
    #global your_hours
    
    your_hours = str(view['hours_textfield'].text)
    if your_hours.isdigit():
       #print('Yes a digit: ' + your_hours)
       
       if len(homework_hours) == 5:
          view['check_button'].enabled = False
       elif your_hours < 0:
          view['result_label'].text = 'Please input valid number.'
          view['hours_textfield'].text = ''
       else:
          homework_hours.append(your_hours)
          view['hours_textfield'].text = ''
          view['hours_textview'].text = 'List of hours in last five days: ' + str(homework_hours)
    else:
      view['hours_textview'].text = 'Please input valid number.'
      view['check_button'].enabled = False
      
def find_the_maximum_hour(array):
    # find your maximum homework hours
    
    array_max = array[0]
    
    for a_value in homework_hours:
      if array_max == 0 or array_max < a_value:
         array_max = a_value
      else:
         array_max = array_max
          
    return array_max
    
def find_the_minimum_hour(array):
    # find your minimum homework hours
    
    array_min = array[0]
    
    for a_value in homework_hours:
      if array_min == 0 or array_min > a_value:
         array_min = a_value
      else:
          array_min = array_min
          
    return array_min
    
def result_button_touch_up_inside(sender):
    # show your maximum hours and minimum hours
    
    maximum = find_the_maximum_hour(homework_hours)
    minimum = find_the_minimum_hour(homework_hours)
    view['maximum_label'].text = 'The maximum hour is: ' + str(maximum)
    view['minimum_label'].text = 'The minimum hour is: ' + str(minimum)
    
view = ui.load_view()
view.present('full_screen')
