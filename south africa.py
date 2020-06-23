# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:37:52 2020

@author: SEDMQ
"""

# Create a list of the BRICS countries
country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"
                    ]
           }

# Print the list and dictionary
print( "country" )
print( "capitals" )
"""
What response did you get?
Why did the list and dictionary contents not print?
Fix the code and run the script again.
"""

print( capitals["South Africa"] [2] )
"""
Why did you get an error for the 2nd capital of South Africa?
Hint: Check the syntax for the index value.
"""