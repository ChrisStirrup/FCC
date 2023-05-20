# FCC
FCC contains the Free Code Camp projects that I have completed, in all of these I am given a breif and have to solve it myself.

Arithmatic formatter 

  Takes 
     A list of upto five addition or subtraction problems 
     Optitionaly a "True" statement
     
  Returns 
     A formatted addition subtraction 
     If True a correct solution
   EG
   
      Arithmatic_formatter("3+7", "True")   returns 3/+7/10
      
      
 Time Calculator
 
  Takes 
     A start time in 12hour notation (AM/PM)
     How many hours and minutes you want to add (hours:minutes)
     optionally a day of the week case insensitive (WedNesDay)
   
   Returns 
      A end time in 12 hour notation
      A weekday
      How many days it has been 
    
    EG
      add_time("3:00 PM", "3:10", "wednesday") returns "6:10 PM, Wednesday"
     
     
  Budget App 
    
        This has been the most difficult so far, it does a few things.
        
         It has a Class - "Category", with the following functions:
        
         Deposit, and Withdraw
           Takes
              A number
              An optional description
           Returns
              A stored Deposit or Withdrawal
              If insufficiant funds are present the Withdrawal simply does not take place 
         
         Transfer
           Takes
              A number
              An optional description
              A destionation
              
           Returns
              A stored Deposit in the destination, with the description "Transfer from '   ' "
              Withdrawal in the target.  with the description "Transfer to '   ' "
              if insufficant funds in the target the whole transfer does not take place
              
         get_balance 
           Returns 
              The current balance of the budget category 
                
         create_spend_chart
           Takes
              Upto four categorys
           Returns
              A bar chart showing the percentage spent by each category

Polygon Area Calc
        
            This has two classes; a Rectangle class and a Square class as a subset.
            
            Rectangles 
                
                Can set width and height with set_width and set_height respectivly.
                
                Can tell you their area, perimiter, and diagonal with get_area, get_perimeter, and get_diagonal.
                
                Can print a depiction of themselves using '*' with get_picture
                
                Can return how often another square or rectangle can fit inside them
            
            Squares 
                
                have a set_side function to set their side, additionally the set_width and set_height work to set sides 
             
              
            
Probable Hats

            Has a hat class that containes baals, the balls can be drawn out of the hat with the 'draw' function, this draws x balls without replacment
            
            another function the 'experement' allows n balls to be drawn from a hat x times and a minimum value statment to be given (eg 2 red 1 whhite), it then return the chance of draw containg the minimum value from the sammples drawn
