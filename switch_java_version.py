import os
import sys

print '''
   _____         _ _       _       
  / ____|       (_) |     | |      
 | (_____      ___| |_ ___| |__    
  \___ \ \ /\ / / | __/ __| '_ \   
  ____) \ V  V /| | || (__| | | |  
 |_____/ \_/\_/ |_|\__\___|_| |_|  
       _                           
      | |                          
      | | __ ___   ____ _          
  _   | |/ _` \ \ / / _` |         
 | |__| | (_| |\ V / (_| |         
  \____/ \__,_| \_/ \__,_|         
                                   
                    (_)            
 __   _____ _ __ ___ _  ___  _ __  
 \ \ / / _ \ '__/ __| |/ _ \| '_ \ 
  \ V /  __/ |  \__ \ | (_) | | | |
   \_/ \___|_|  |___/_|\___/|_| |_|
                                   
                                   
                                   
>>>>>>press 1   Swtich to java 8 
>>>>>>press 2   Swtich to java 11
'''

selection = int(input("> "))

if selection == 1:
    os.system('setx /m JAVA_HOME "C:/Program Files/Java/jdk1.8.0_211"')
elif selection == 2:
    os.system('setx /m JAVA_HOME "C:/Program Files/Java/jdk-11.0.6"')
else:
    print "wrong option!"
