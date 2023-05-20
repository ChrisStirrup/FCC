class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.cumulative_total = 0
        self.funds_in_out = []
        self.descriptions = []
        self.print_ledger = ''
        self.sum_of_withdrawals = 0

    def __str__(self):
        star_amount = (30 - int(len(self.name)))/2
        star = ''
        while star_amount > 0:
            star_amount -= 1
            star = star + '*'
        build_print_ledger = len(self.ledger)
        select_part = 0
        while build_print_ledger > 0:
            self.print_ledger = self.print_ledger + self.descriptions[select_part] + self.funds_in_out[select_part]
            select_part += 1
            build_print_ledger -= 1

        return """{}{}{}
{}
Total: {}""".format(star, self.name, star, self.print_ledger, self.cumulative_total)

    def deposit(self, amount, description=""):
        deposit_result = {"description": description, "amount:": amount}
        self.cumulative_total = self.cumulative_total + amount
        self.ledger.append([deposit_result])
        amount = "{:> .2f}".format(amount)
        amount = amount[:7]
        self.funds_in_out.append('{} \n'.format(amount))
        if description:
            description = description + "                       "
            description = description[:23]
            self.descriptions.append('{}'.format(description))
        else:
            self.descriptions.append("                       ")


    def withdraw(self, amount, description=""):
        if self.check_funds(self, amount):
            self.cumulative_total = self.cumulative_total - amount
            amount = amount * -1
            withdraw_result = {"description": description, "amount:": amount}
            self.ledger.append([withdraw_result])
            self.sum_of_withdrawals += amount
            amount = "{:> .2f}".format(amount)
            amount = str(amount) + "       "
            amount = amount[:7]
            self.funds_in_out.append('{} \n'.format(amount))
            if description:
                description = description + "                       "
                description = description[:23]
                self.descriptions.append('{}'.format(description))
            else:
                self.descriptions.append("                       ")
            return True
        else:
            return False

    def get_balance(self):
        return "{}, has {}".format(self.name, self.cumulative_total)

    def transfer(self, transfer_amount, destination):
        if self.check_funds(self, transfer_amount):
            self.withdraw(transfer_amount, "transfer to {}".format(destination.name))
            destination.deposit(transfer_amount, "transfer from {}".format(self.name))
            return True
        else:
            return False

    def check_funds(self, list_to_check, amount):
        if list_to_check.cumulative_total >= amount:
            return True
        else:
            return False


def create_spend_chart(classes):
    # The program I was using (pycharm) lets me hide statments putting the if here allowed me to scroll past easier, its kept here as I just uploaded my project as is when it passed the FCC checks. 
    hide_circles = 1
    if hide_circles == 1:
        category_one_circle_1 = ''
        category_one_circle_2 = ''
        category_one_circle_3 = ''
        category_one_circle_4 = ''
        category_one_circle_5 = ''
        category_one_circle_6 = ''
        category_one_circle_7 = ''
        category_one_circle_8 = ''
        category_one_circle_9 = ''
        category_one_circle_10 = ''
        category_two_circle_1 = ''
        category_two_circle_2 = ''
        category_two_circle_3 = ''
        category_two_circle_4 = ''
        category_two_circle_5 = ''
        category_two_circle_6 = ''
        category_two_circle_7 = ''
        category_two_circle_8 = ''
        category_two_circle_9 = ''
        category_two_circle_10 = ''
        category_three_circle_1 = ''
        category_three_circle_2 = ''
        category_three_circle_3 = ''
        category_three_circle_4 = ''
        category_three_circle_5 = ''
        category_three_circle_6 = ''
        category_three_circle_7 = ''
        category_three_circle_8 = ''
        category_three_circle_9 = ''
        category_three_circle_10 = ''
        category_four_circle_1 = ''
        category_four_circle_2 = ''
        category_four_circle_3 = ''
        category_four_circle_4 = ''
        category_four_circle_5 = ''
        category_four_circle_6 = ''
        category_four_circle_7 = ''
        category_four_circle_8 = ''
        category_four_circle_9 = ''
        category_four_circle_10 = ''

    hide_category_names = 1
        # The program I was using (pycharm) lets me hide statments putting the if here allowed me to scroll past easier, its kept here as I just uploaded my project as is when it passed the FCC checks. 
    if hide_category_names == 1:
        category_one_name_1 = ''
        category_two_name_1 = ''
        category_three_name_1 = ''
        category_four_name_1 = ''
        category_one_name_2 = ''
        category_two_name_2 = ''
        category_three_name_2 = ''
        category_four_name_2 = ''
        category_one_name_3 = ''
        category_two_name_3 = ''
        category_three_name_3 = ''
        category_four_name_3 = ''
        category_one_name_4 = ''
        category_two_name_4 = ''
        category_three_name_4 = ''
        category_four_name_4 = ''
        category_one_name_5 = ''
        category_two_name_5 = ''
        category_three_name_5 = ''
        category_four_name_5 = ''
        category_one_name_6 = ''
        category_two_name_6 = ''
        category_three_name_6 = ''
        category_four_name_6 = ''
        category_one_name_7 = ''
        category_two_name_7 = ''
        category_three_name_7 = ''
        category_four_name_7 = ''
        category_one_name_8 = ''
        category_two_name_8 = ''
        category_three_name_8 = ''
        category_four_name_8 = ''
        category_one_name_9 = ''
        category_two_name_9 = ''
        category_three_name_9 = ''
        category_four_name_9 = ''
        category_one_name_10 = ''
        category_two_name_10 = ''
        category_three_name_10 = ''
        category_four_name_10 = ''
        category_one_name_11 = ''
        category_two_name_11 = ''
        category_three_name_11 = ''
        category_four_name_11 = ''
        category_one_name_12 = ''
        category_two_name_12 = ''
        category_three_name_12 = ''
        category_four_name_12 = ''
        category_one_name_13 = ''
        category_two_name_13 = ''
        category_three_name_13 = ''
        category_four_name_13 = ''
        category_one_name_14 = ''
        category_two_name_14 = ''
        category_three_name_14 = ''
        category_four_name_14 = ''
        category_one_name_15 = ''
        category_two_name_15 = ''
        category_three_name_15 = ''
        category_four_name_15 = ''

    hide_splitting = 1
        # The program I was using (pycharm) lets me hide statments putting the if here allowed me to scroll past easier, its kept here as I just uploaded my project as is when it passed the FCC checks. 
    if hide_splitting == 1:
        try:
            if classes[0]:
                category_one = classes[0]
        except IndexError:
            category_one = ''
        try:
            if classes[1]:
                category_two = classes[1]
        except IndexError:
            category_two = ''
        try:
            if classes[2]:
                category_three = classes[2]
        except IndexError:
            category_three = ''
        try:
            if classes[3]:
                category_four = classes[3]
        except IndexError:
            category_four = ''

    if category_one:
        category_one_dashes = "---"
        category_one_cost = category_one.sum_of_withdrawals
        category_one_name = category_one.name + '               '
        category_one_name = category_one_name[:15]
        category_one_circle_0 = 'o'
    else:
        category_one_dashes = ""
        category_one_cost = 0
        category_two_name_vert = ''
        category_one_circle_0 = ''

    if category_two:
        category_two_dashes = "---"
        category_two_cost = category_two.sum_of_withdrawals
        category_two_name = category_two.name + '               '
        category_two_name = category_two_name[:15]
        category_two_circle_0 = 'o'
    else:
        category_two_dashes = ""
        category_two_cost = 0
        category_two_name_vert = ''
        category_two_circle_0 = ''

    if category_three:
        category_three_dashes = "---"
        category_three_cost = category_three.sum_of_withdrawals
        category_three_name = category_three.name + '               '
        category_three_name = category_three_name[:15]
        category_three_circle_0 = 'o'
    else:
        category_three_dashes = ""
        category_three_cost = 0
        category_three_name_vert = ''
        category_three_circle_0 = ''

    if category_four:
        category_four_dashes = "---"
        category_four_cost = category_four.sum_of_withdrawals
        category_four_name = category_four.name + '               '
        category_four_name = category_four_name[:15]
        category_four_circle_0 = 'o'
    else:
        category_four_dashes = ""
        category_four_cost = 0
        category_four_name_vert = ''
        category_four_circle_0 = ''

    total_withdraw_cost = category_one_cost + category_two_cost + category_three_cost + category_four_cost

    if category_one:
        category_one_cost_percent = (category_one_cost/total_withdraw_cost * 100)//10
        category_one_loop = 0
        category_one_loop_assignment = []
        category_one_anti_loop = 10
        while category_one_cost_percent > 0:
            category_one_loop += 1
            category_one_anti_loop -= 1
            category_one_cost_percent -= 1
            category_one_loop_assignment.append('o')
        while category_one_anti_loop > 0:
            category_one_anti_loop -= 1
            category_one_loop_assignment.append('')
        if hide_circles == 1:
                # The program I was using (pycharm) lets me hide statments putting the if here allowed me to scroll past easier, its kept here as I just uploaded my project as is when it passed the FCC checks. 
            category_one_circle_1 = category_one_loop_assignment[0]
            category_one_circle_2 = category_one_loop_assignment[1]
            category_one_circle_3 = category_one_loop_assignment[2]
            category_one_circle_4 = category_one_loop_assignment[3]
            category_one_circle_5 = category_one_loop_assignment[4]
            category_one_circle_6 = category_one_loop_assignment[5]
            category_one_circle_7 = category_one_loop_assignment[6]
            category_one_circle_8 = category_one_loop_assignment[7]
            category_one_circle_9 = category_one_loop_assignment[8]
            category_one_circle_10 = category_one_loop_assignment[9]
        if hide_category_names == 1:
                # The program I was using (pycharm) lets me hide statments putting the if here allowed me to scroll past easier, its kept here as I just uploaded my project as is when it passed the FCC checks. 
            category_one_name_1 = category_one_name[0]
            category_one_name_2 = category_one_name[1]
            category_one_name_3 = category_one_name[2]
            category_one_name_4 = category_one_name[3]
            category_one_name_5 = category_one_name[4]
            category_one_name_6 = category_one_name[5]
            category_one_name_7 = category_one_name[6]
            category_one_name_8 = category_one_name[7]
            category_one_name_9 = category_one_name[8]
            category_one_name_10 = category_one_name[9]
            category_one_name_11 = category_one_name[10]
            category_one_name_12 = category_one_name[11]
            category_one_name_13 = category_one_name[12]
            category_one_name_14 = category_one_name[13]
            category_one_name_15 = category_one_name[14]




    if category_two:
        category_two_cost_percent = (category_two_cost/total_withdraw_cost * 100)//10
        category_two_loop = 0
        category_two_loop_assignment = []
        category_two_anti_loop = 10
        while category_two_cost_percent > 0:
            category_two_loop += 1
            category_two_anti_loop -= 1
            category_two_cost_percent -= 1
            category_two_loop_assignment.append('o')
        while category_two_anti_loop > 0:
            category_two_anti_loop -= 1
            category_two_loop_assignment.append('')
        if hide_circles == 1:
                # The program I was using (pycharm) lets me hide statments putting the if here allowed me to scroll past easier, its kept here as I just uploaded my project as is when it passed the FCC checks. 
            category_two_circle_1 = category_two_loop_assignment[0]
            category_two_circle_2 = category_two_loop_assignment[1]
            category_two_circle_3 = category_two_loop_assignment[2]
            category_two_circle_4 = category_two_loop_assignment[3]
            category_two_circle_5 = category_two_loop_assignment[4]
            category_two_circle_6 = category_two_loop_assignment[5]
            category_two_circle_7 = category_two_loop_assignment[6]
            category_two_circle_8 = category_two_loop_assignment[7]
            category_two_circle_9 = category_two_loop_assignment[8]
            category_two_circle_10 = category_two_loop_assignment[9]
        if hide_category_names == 1:
                # The program I was using (pycharm) lets me hide statments putting the if here allowed me to scroll past easier, its kept here as I just uploaded my project as is when it passed the FCC checks. 
            category_two_name_1 = category_two_name[0]
            category_two_name_2 = category_two_name[1]
            category_two_name_3 = category_two_name[2]
            category_two_name_4 = category_two_name[3]
            category_two_name_5 = category_two_name[4]
            category_two_name_6 = category_two_name[5]
            category_two_name_7 = category_two_name[6]
            category_two_name_8 = category_two_name[7]
            category_two_name_9 = category_two_name[8]
            category_two_name_10 = category_two_name[9]
            category_two_name_11 = category_two_name[10]
            category_two_name_12 = category_two_name[11]
            category_two_name_13 = category_two_name[12]
            category_two_name_14 = category_two_name[13]
            category_two_name_15 = category_two_name[14]

    if category_three:
        category_three_cost_percent = (category_three_cost/total_withdraw_cost * 100)//10
        category_three_loop = 0
        category_three_loop_assignment = []
        category_three_anti_loop = 10
        while category_three_cost_percent > 0:
            category_three_loop += 1
            category_three_anti_loop -= 1
            category_three_cost_percent -= 1
            category_three_loop_assignment.append('o')
        while category_three_anti_loop > 0:
            category_three_anti_loop -= 1
            category_three_loop_assignment.append('')
        if hide_circles == 1:
                # The program I was using (pycharm) lets me hide statments putting the if here allowed me to scroll past easier, its kept here as I just uploaded my project as is when it passed the FCC checks. 
            category_three_circle_1 = category_three_loop_assignment[0]
            category_three_circle_2 = category_three_loop_assignment[1]
            category_three_circle_3 = category_three_loop_assignment[2]
            category_three_circle_4 = category_three_loop_assignment[3]
            category_three_circle_5 = category_three_loop_assignment[4]
            category_three_circle_6 = category_three_loop_assignment[5]
            category_three_circle_7 = category_three_loop_assignment[6]
            category_three_circle_8 = category_three_loop_assignment[7]
            category_three_circle_9 = category_three_loop_assignment[8]
            category_three_circle_10 = category_three_loop_assignment[9]
        if hide_category_names == 1:
                # The program I was using (pycharm) lets me hide statments putting the if here allowed me to scroll past easier, its kept here as I just uploaded my project as is when it passed the FCC checks. 
            category_three_name_1 = category_three_name[0]
            category_three_name_2 = category_three_name[1]
            category_three_name_3 = category_three_name[2]
            category_three_name_4 = category_three_name[3]
            category_three_name_5 = category_three_name[4]
            category_three_name_6 = category_three_name[5]
            category_three_name_7 = category_three_name[6]
            category_three_name_8 = category_three_name[7]
            category_three_name_9 = category_three_name[8]
            category_three_name_10 = category_three_name[9]
            category_three_name_11 = category_three_name[10]
            category_three_name_12 = category_three_name[11]
            category_three_name_13 = category_three_name[12]
            category_three_name_14 = category_three_name[13]
            category_three_name_15 = category_three_name[14]


    if category_four:
        category_four_cost_percent = (category_four_cost/total_withdraw_cost * 100)//10
        category_four_loop = 0
        category_four_loop_assignment = []
        category_four_anti_loop = 10
        while category_four_cost_percent > 0:
            category_four_loop += 1
            category_four_anti_loop -= 1
            category_four_cost_percent -= 1
            category_four_loop_assignment.append('o')
        while category_four_anti_loop > 0:
            category_four_anti_loop -= 1
            category_four_loop_assignment.append('')
        if hide_circles == 1:
                # The program I was using (pycharm) lets me hide statments putting the if here allowed me to scroll past easier, its kept here as I just uploaded my project as is when it passed the FCC checks. 
            category_four_circle_1 = category_four_loop_assignment[0]
            category_four_circle_2 = category_four_loop_assignment[1]
            category_four_circle_3 = category_four_loop_assignment[2]
            category_four_circle_4 = category_four_loop_assignment[3]
            category_four_circle_5 = category_four_loop_assignment[4]
            category_four_circle_6 = category_four_loop_assignment[5]
            category_four_circle_7 = category_four_loop_assignment[6]
            category_four_circle_8 = category_four_loop_assignment[7]
            category_four_circle_9 = category_four_loop_assignment[8]
            category_four_circle_10 = category_four_loop_assignment[9]
        if hide_category_names == 1:
                # The program I was using (pycharm) lets me hide statments putting the if here allowed me to scroll past easier, its kept here as I just uploaded my project as is when it passed the FCC checks. 
            category_four_name_1 = category_four_name[0]
            category_four_name_2 = category_four_name[1]
            category_four_name_3 = category_four_name[2]
            category_four_name_4 = category_four_name[3]
            category_four_name_5 = category_four_name[4]
            category_four_name_6 = category_four_name[5]
            category_four_name_7 = category_four_name[6]
            category_four_name_8 = category_four_name[7]
            category_four_name_9 = category_four_name[8]
            category_four_name_10 = category_four_name[9]
            category_four_name_11 = category_four_name[10]
            category_four_name_12 = category_four_name[11]
            category_four_name_13 = category_four_name[12]
            category_four_name_14 = category_four_name[13]
            category_four_name_15 = category_four_name[14]


    return (f'''
    Percentage spent by category
    100| {category_one_circle_10}  {category_two_circle_10}  {category_three_circle_10}  {category_four_circle_10}   
     90| {category_one_circle_9}  {category_two_circle_9}  {category_three_circle_9}  {category_four_circle_9}   
     80| {category_one_circle_8}  {category_two_circle_8}  {category_three_circle_8}  {category_four_circle_8}   
     70| {category_one_circle_7}  {category_two_circle_7}  {category_three_circle_7}  {category_four_circle_7}  
     60| {category_one_circle_6}  {category_two_circle_6}  {category_three_circle_6}  {category_four_circle_6}  
     50| {category_one_circle_5}  {category_two_circle_5}  {category_three_circle_5}  {category_four_circle_5}  
     40| {category_one_circle_4}  {category_two_circle_4}  {category_three_circle_4}  {category_four_circle_4}  
     30| {category_one_circle_3}  {category_two_circle_3}  {category_three_circle_3}  {category_four_circle_3}  
     20| {category_one_circle_2}  {category_two_circle_2}  {category_three_circle_2}  {category_four_circle_2}   
     10| {category_one_circle_1}  {category_two_circle_1}  {category_three_circle_1}  {category_four_circle_1}   
      0| {category_one_circle_0}  {category_two_circle_0}  {category_three_circle_0}  {category_four_circle_0}   
       {category_one_dashes}{category_two_dashes}{category_three_dashes}{category_four_dashes}-
         {category_one_name_1}  {category_two_name_1}  {category_three_name_1}  {category_four_name_1}
         {category_one_name_2}  {category_two_name_2}  {category_three_name_2}  {category_four_name_2}
         {category_one_name_3}  {category_two_name_3}  {category_three_name_3}  {category_four_name_3}
         {category_one_name_4}  {category_two_name_4}  {category_three_name_4}  {category_four_name_4}
         {category_one_name_5}  {category_two_name_5}  {category_three_name_5}  {category_four_name_5}
         {category_one_name_6}  {category_two_name_6}  {category_three_name_6}  {category_four_name_6}
         {category_one_name_7}  {category_two_name_7}  {category_three_name_7}  {category_four_name_7}
         {category_one_name_8}  {category_two_name_8}  {category_three_name_8}  {category_four_name_8}
         {category_one_name_9}  {category_two_name_9}  {category_three_name_9}  {category_four_name_9}
         {category_one_name_10}  {category_two_name_10}  {category_three_name_10}  {category_four_name_10} 
         {category_one_name_11}  {category_two_name_11}  {category_three_name_11}  {category_four_name_11}
         {category_one_name_12}  {category_two_name_12}  {category_three_name_12}  {category_four_name_12}
         {category_one_name_13}  {category_two_name_13}  {category_three_name_13}  {category_four_name_13}
         {category_one_name_14}  {category_two_name_14}  {category_three_name_14}  {category_four_name_14}
         {category_one_name_15}  {category_two_name_15}  {category_three_name_15}  {category_four_name_15} 
    ''')

