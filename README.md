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
        
         It has a 'Class' "Category", with the following functions:
        
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
             
              
            
              
