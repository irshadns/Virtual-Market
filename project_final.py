# Project done by IRSHAD NAWAZ
# irshadnaw@gmail.com
# https://linkedin.com/in/irshadns
# https://github.com/irshadns


# Greet User with their name , returns name
def greetings():
    dash = '-' * 40

    print(dash)
    print('\t''\t''Welcome to Virtual Market ')
    print(dash)

    name = input('What is your name ? ')

    while len(name) == 0 or name.isspace():
        name = input('Please provide your name : ')

    print('Hello', name, 'hope you are doing well today')
    print(name, 'today you can buy anything from the following menu : ')

    return name


# Open Text file , Read and Print all it's contents , returns lines ( lines = contents )
def show_menu(filename):
    file_ref = open(filename, 'r')
    lines = file_ref.readlines()

    for line in lines:
        print(line, end='')  # it will print all it's contents one by one

    file_ref.close()
    return lines


# Open sub menu text file , Read and split its contents per line and assign into 3 variables (sno , item & price) ,
# append item(submenu item) into 'item_list'(list variable) and append price(item's price) into
# 'price_list'(list variable)
# Print it's contents in text align format
# return these 2 lists(variables) 'item_list' and 'price_list'
def split_for_submenu(filename):
    item_list = []
    price_list = []

    file_ref = open(filename, 'r')
    lines = file_ref.readlines()
    file_ref.close()

    for line in lines:
        sno, item, price = line.split()  # Splitting contents per line into 3 variables
        item_list.append(item)  # Appending item(submenu items) together
        price_list.append(price)  # Appending price(items prices) together
        print('{:<5s}{:<15s}{:>7s}'.format(sno, item, price))  # Printing all it's content one by one

    return item_list, price_list


# Open and read text file (i.e main menu file) , split it's contents per line and assign into
# 2 variables (sno,submenu_name), append 'submenu_name' to 'submenu'(list variable) , Get input from user to open
# which sub menu (= 'file_choice' variable) , open and returns 'file_choice'(submenu_choice).
def select_menu(filename):
    submenu_list = []
    file_choice = ''
    file_ex = '.txt'
    lines = show_menu(filename)

    for line in lines:
        sno, submenu_name = line.split()  # Splitting contents per line into 2 variables
        submenu_list.append(submenu_name)  # Appending submenu_name together

    submenu_choice = input('\n''Please select the option ''\n')

    while submenu_choice.isalpha() or submenu_choice.isspace() or int(submenu_choice) > len(
            lines) or submenu_choice == '0':
        print('Please select a number from 1 to', len(lines))
        submenu_choice = input('Please select the option ''\n')

    submenu_choice = int(submenu_choice)

    for i in range(1, len(submenu_list) + 1):
        if submenu_choice == i:
            print('You have selected', submenu_list[submenu_choice - 1])
            print('Showing the sub menu of', submenu_list[submenu_choice - 1])
            file_choice = submenu_list[submenu_choice - 1] + file_ex

    return file_choice


# Ask user to select items and their quantity in loop until user put 'no' to continue...
# appending selected item(s) , selected quantity(ies) , unit price of selected item(s) , price for quantity of
# selected item(s) into (list variables) = item_bought , item_bought_quantity , item_bought_unit_price ,
# item_quantity_price_list.
def add_item(item_list, price_list, item_bought, item_bought_quantity, item_quantity_price_list, item_bought_unit_price,
             file_choice):
    while True:
        print('Which item would you like to buy ? from 1 to', len(item_list) - 1)
        choice_item = input()

        while not choice_item.isdigit():
            print('Enter Correct Choice')
            print('Which item would you like to buy ? from 1 to', len(item_list) - 1)
            choice_item = input()

        while choice_item == '0' or int(choice_item) >= len(item_list):
            print('Please select from 1 to', len(item_list) - 1)
            print('Which item would you like to buy ? from 1 to', len(item_list) - 1)
            choice_item = input()

        choice_item = int(choice_item)
        item_bought.append(item_list[choice_item])
        print('You have selected the Item', item_bought[-1])
        item_quantity = input('How much items you want to buy ? (Numeric Quantity) ')

        while not item_quantity.isdigit() and not item_quantity.replace('.', '1').isdigit():
            print('Please Enter Quantity in numbers')
            item_quantity = input('How much items you want to buy ? [Numeric Quantity] ')

        item_quantity = float(item_quantity)
        item_bought_quantity.append(item_quantity)
        item_quantity_price = float(price_list[choice_item]) * float(item_quantity)
        print(item_quantity, item_bought[-1], 'will cost you', item_quantity_price)
        item_quantity_price_list.append(item_quantity_price)
        item_bought_unit_price.append(price_list[choice_item])

        choice = input('Would you like to buy more items from this menu ? yes/no ')
        choice = choice.lower()

        while choice != 'yes' and choice != 'no':
            print('Enter Valid choice')
            choice = input('Would you like to buy more items this menu ? yes/no ')
            choice = choice.lower()

        if choice == 'yes':
            split_for_submenu(file_choice)
            continue

        elif choice == 'no':
            return item_bought, item_bought_quantity, item_quantity_price_list, item_bought_unit_price


# Print Purchased items(item_bought) , their quantity(item_bought_quantity) , and
# their prices for quantities(item_quantity_price_list) in a bill format
def show_basket(item_bought, item_bought_quantity, item_quantity_price_list):
    dash = '-' * 49
    print(dash)
    print(' ''S.no''\t''Items''\t''\t''\t''  ''Quantity''\t''  ''Total price')
    print(dash)
    for i in range(0, len(item_bought)):
        print(
            '{:^8d}{:<17s}{:>6.1f}{:>14.2f}'.format(i + 1, item_bought[i], item_bought_quantity[i],
                                                    item_quantity_price_list[i]))
    print(dash)


# Ask user to select from 2 options :
# 1. Remove Item Completely ( to remove bought item along it's whole quantity)
# 2. Remove Item Partially ( to remove number of items from quantity of bought item)
def remove_item(item_bought, item_bought_quantity, item_quantity_price_list, item_bought_unit_price):
    while True:
        show_basket(item_bought, item_bought_quantity, item_quantity_price_list)

        remove_choice = input(
            '\n''Select the remove mode: ''\n''1. Remove Item Completely ''\n'
            "2. Remove Item Partially (Edit Quantity) "'\n''\n''0. Return to Shopping Menu''\n')
        while remove_choice != '1' and remove_choice != '2' and remove_choice != '0':
            print('Invalid Option')
            remove_choice = input('\n''Select the remove mode: ''\n''1. Remove Item Completely ''\n'
                                  "2. Remove Item Partially (Edit Quantity)  "'\n''\n''0. Return to Shopping Menu''\n')

        if remove_choice == '0':
            print('Returning to Main Menu''\n')
            return item_bought, item_bought_quantity, item_quantity_price_list, item_bought_unit_price
            # break

        if remove_choice == '1':
            while True:
                delete_item = input(
                    'Select the item you want to completely remove it from the Basket ? for e.g 1,2,3..... ')

                while not delete_item.isdigit() or delete_item.isspace() or int(delete_item) > len(item_bought) or delete_item == '0':
                    print('No item found , Please Enter from 1 to', len(item_bought))
                    delete_item = input(
                        'Select the item you want to completely remove it from the Basket ? for e.g 1,2,3..... ')
                delete_item = int(delete_item)
                print('Your selected item', item_bought[delete_item - 1], 'has been completely removed')

                del item_bought[delete_item - 1]
                del item_bought_quantity[delete_item - 1]
                del item_quantity_price_list[delete_item - 1]
                del item_bought_unit_price[delete_item - 1]

                choice_del = input('Do you want to completely remove more items ? yes/no ')
                choice_del = choice_del.lower()

                while choice_del != 'yes' and choice_del != 'no':
                    print('Enter Valid Choice : yes or no ')
                    choice_del = input('Do you want to completely remove more items ? yes/no ')
                    choice_del = choice_del.lower()

                if choice_del == 'yes':
                    if len(item_bought) == 0:
                        print('Basket is empty''\n''buy some items ! ')
                        return item_bought, item_bought_quantity, item_quantity_price_list, item_bought_unit_price
                    else:
                        show_basket(item_bought, item_bought_quantity, item_quantity_price_list)
                    continue

                elif choice_del == 'no':
                    return item_bought, item_bought_quantity, item_quantity_price_list, item_bought_unit_price
                    # break

        elif remove_choice == '2':
            while True:

                ch_item = input("Select the item you want to edit it's quantity ! for e.g 1,2,3..... ")
                while not ch_item.isdigit() or ch_item.isspace() or int(ch_item) > len(item_bought) or ch_item == '0':
                    print('No item found , Please Enter from 1 to', len(item_bought))
                    ch_item = input("Select the item you want to edit it's quantity ! for e.g 1,2,3..... ")

                ch_item = int(ch_item)
                print('Your selected item is', item_bought[ch_item - 1])
                quantity_remove_items = input(
                    'How many items you want to remove from its quantity ! for e.g 1,2,3..... ')

                while not quantity_remove_items.isdigit() or quantity_remove_items.isspace() or not quantity_remove_items.replace(
                        '.', '1').isdigit():
                    print('Please provide Valid Quantity')
                    quantity_remove_items = input(
                        'How many items you want to remove from its quantity ! for e.g 1,2,3..... ')

                while float(quantity_remove_items) > item_bought_quantity[ch_item - 1]:
                    print('Error ! Your provided quantity is greater than actual quantity of item ')
                    quantity_remove_items = input(
                        'How many items you want to remove from its quantity ! for e.g 1,2,3..... ')

                if float(quantity_remove_items) == item_bought_quantity[ch_item - 1]:
                    print(quantity_remove_items, item_bought[ch_item - 1], 'have been removed from ',
                          item_bought_quantity[ch_item - 1], item_bought[ch_item - 1])
                    del item_bought[ch_item - 1]
                    del item_bought_quantity[ch_item - 1]
                    del item_quantity_price_list[ch_item - 1]
                    del item_bought_unit_price[ch_item - 1]

                elif float(quantity_remove_items) < item_bought_quantity[ch_item - 1]:
                    print(quantity_remove_items, item_bought[ch_item - 1], 'have been removed from ',
                          item_bought_quantity[ch_item - 1], item_bought[ch_item - 1])
                    deducted_amount = float(item_bought_unit_price[ch_item - 1]) * float(quantity_remove_items)
                    item_quantity_price_list[ch_item - 1] -= float(deducted_amount)
                    item_bought_quantity[ch_item - 1] -= float(quantity_remove_items)

                ch_edit = input('Do you want to Edit quantity of more Items ? yes/no ')
                ch_edit = ch_edit.lower()

                while ch_edit != 'yes' and ch_edit != 'no':
                    print('Enter Valid Choice : yes or no')
                    ch_edit = input('Do you want to Edit quantity of more Items ? yes/no ')
                    ch_edit = ch_edit.lower()

                if ch_edit == 'yes':
                    if len(item_bought) == 0:
                        print('Basket is empty''\n''buy some items ! ')
                        return item_bought, item_bought_quantity, item_quantity_price_list, item_bought_unit_price
                    else:
                        show_basket(item_bought, item_bought_quantity, item_quantity_price_list)
                    continue

                elif ch_edit == 'no':
                    return item_bought, item_bought_quantity, item_quantity_price_list, item_bought_unit_price
                    # break


# Open and read coupons from text file(i.e COUPONS.txt) , Give 2 options to user :
# 1. Get Free Coupon (to get discount next time)  2. Enter Coupon to get discount(this time),
# this function print(show) + writes(in text file i.e FINAL_BILL.txt) the remaining bill after coupon
def coupon(coupon_filename, bill_filename, total_amount, name):
    file_ref = open(bill_filename, 'a')  # Open Bill text file(created by program) in 'Append mode'
    file_c = open(coupon_filename, 'r')
    contents = file_c.readlines()
    coupons = []

    for line in contents:
        c = line.split()
        coupons.append(c[-1])

    file_c.close()

    dash = '-' * 49
    dash_for_txt_file = '-' * 52

    print('\n')
    file_ref.write('\n')

    choice = input('Select the Option : ''\n''1. Get Free Coupon''\n''2. Enter Coupon to get discount''\n')
    while choice != '1' and choice != '2' and choice.isspace():
        print('Invalid choice')
        choice = input('Select the Option : ''\n''1. Get Free Coupon''\n''2. Enter Coupon to get discount''\n')

    if choice == '1':
        # print coupon next to middle term of all coupons " [len(coupons) / 2]
        print('free coupon to use next time to avail discount : ''"', coupons[int(len(coupons) / 2)], '"')
        print('No discount , as no coupon was inserted')
        file_ref.write('No discount , as no coupon was inserted' + '\n')
        print(dash)
        file_ref.write(dash_for_txt_file + '\n')

        print('Total Amount = {:>30.2f}'.format(total_amount))
        file_ref.write('Total Amount = {:>33.2f}'.format(total_amount) + '\n')
        print(dash)
        file_ref.write(dash_for_txt_file + '\n')

        print('Thanks for Shopping', name)
        file_ref.write('Thanks for Shopping ' + str(name))

    elif choice == '2':
        while True:
            choice = input('Do you have any Coupon ? yes/no ')
            choice = choice.lower()

            while choice != 'yes' and choice != 'no':
                print('Invalid choice')
                choice = input('Do you have any Coupon ? yes/no ')
                choice = choice.lower()

            if choice == 'yes':
                user_coupon = input('Enter Coupon to get 5% discount: ')
                user_coupon = user_coupon.upper()
                for z in range(0, len(coupons)):
                    if user_coupon == coupons[z]:
                        discount = int(0.05) * float(total_amount)
                        total_amount -= float(discount)
                        discount = 0.05 * float(total_amount)
                        total_amount -= float(discount)

                        print('\n')

                        print('Coupon :', user_coupon, 'Applied')
                        file_ref.write('Coupon :' + str(user_coupon) + ' Applied' + '\n')

                        print('You got 5% discount')
                        file_ref.write('You got 5% discount''\n')

                        print('After 5% discount :')
                        file_ref.write('After 5% discount : ''\n')
                        print(dash)
                        file_ref.write(dash_for_txt_file + '\n')

                        print('Total Amount = {:>30.2f}'.format(total_amount))
                        file_ref.write('Total Amount = {:>33.2f}'.format(total_amount) + '\n')
                        print(dash)
                        file_ref.write(dash_for_txt_file + '\n')

                        print('Thanks for Shopping', name)
                        file_ref.write('Thanks for Shopping ' + str(name))
                        file_ref.close()
                        exit()

                print('Invalid Coupon !')

            elif choice == 'no':
                print('\n')
                print('No discount , as no coupon was inserted')
                file_ref.write('No discount , as no coupon was inserted' + '\n')
                print(dash)
                file_ref.write(dash_for_txt_file + '\n')

                print('Total Amount = {:>30.2f}'.format(total_amount))
                file_ref.write('Total Amount = {:>33.2f}'.format(total_amount) + '\n')

                print(dash)
                file_ref.write(dash_for_txt_file + '\n')

                print('Thanks for Shopping', name)
                file_ref.write('Thanks for Shopping ' + str(name))
                file_ref.close()
                break


# Open Bill text file in write mode , writes bill in a text file i.e purchased items along with their quantity and
# quantity prices in a text file
# print(show) total amount too.
def write_bill(bill_filename, item_bought, item_bought_quantity, item_quantity_price_list):
    dash = '-' * 49
    dash_for_txt_file = '-' * 52

    file_ref = open(bill_filename, 'w')
    file_ref.write(dash_for_txt_file + '\n')
    file_ref.write(' ''S.no''\t''Items''\t''\t''  ''  ''Quantity''\t''Total price''\n')
    file_ref.write(dash_for_txt_file + '\n')

    total_amount = 0.0

    for i in range(0, len(item_bought)):
        file_ref.write('{:^8d}{:<17s}{:>8.1f}{:>15.2f}'.format(i + 1, item_bought[i], item_bought_quantity[i],
                                                               item_quantity_price_list[i]))
        file_ref.write('\n')
        total_amount += float(item_quantity_price_list[i])

    file_ref.write(dash_for_txt_file + '\n')

    print('Total Amount = {:>30.2f}'.format(total_amount))
    print(dash)

    file_ref.write('Total Amount = {:>33.2f}'.format(total_amount) + '\n')
    file_ref.write(dash_for_txt_file + '\n')
    file_ref.close()

    return total_amount


# Taking main_menu filename , bill filename , coupons file name as argument
# Ask user to select from different Shopping options:
# Add Item , View Basket , Remove Item , Checkout ( show Final Bill & Exit)
def market(main_menu_filename, bill_filename, coupon_filename):  # main function ,which is being executed
    name = greetings()
    show_menu(main_menu_filename)

    item_bought = []
    item_quantity_price_list = []
    item_bought_unit_price = []
    item_bought_quantity = []

    choice_basket = 0

    while True:
        if len(item_bought) == 0:
            print('\n''Shopping Options :''\n')
            choice_basket = input(
                '1. Add Item''\n''0. Exit Program''\n')
            while choice_basket != '1' and choice_basket != '0':
                print('Invalid Option')
                print('\n''Shopping Options :''\n')
                choice_basket = input(
                    '1. Add Item''\n''0. Exit Program''\n')

        elif len(item_bought) >= 1:

            print('\n''Shopping Basket Options :''\n')
            choice_basket = input(
                '1. Add Item''\n''2. View Basket''\n''3. Remove Item''\n''4. Checkout''\n')

            while choice_basket != '1' and choice_basket != '2' and choice_basket != '3' and choice_basket != '4' and \
                    choice_basket != '5':
                print('Enter Valid Option')
                choice_basket = input(
                    '1. Add Item''\n''2. View Basket''\n''3. Remove Item''\n''4. Checkout''\n')
        if choice_basket == '0':

            print('Exiting Program !')
            break

        elif choice_basket == '1':

            file_choice = select_menu(main_menu_filename)
            item_list, price_list = split_for_submenu(file_choice)

            ch_buy_or_return = input('\n''Options : ''\n''1. Buy from this menu ''\n''2. Return to main_menu ''\n')

            while ch_buy_or_return != '1' and ch_buy_or_return != '2':
                print('Invalid Option')
                ch_buy_or_return = input('\n''Options : ''\n''1. Buy from this menu ''\n'''
                                         '2. Return to main_menu''\n')

            if ch_buy_or_return == '1':

                # Calling Add_item function
                item_bought, item_bought_quantity, item_quantity_price_list, item_bought_unit_price = add_item(
                    item_list, price_list, item_bought, item_bought_quantity, item_quantity_price_list,
                    item_bought_unit_price, file_choice)

            elif ch_buy_or_return == '2':

                print('Returning to main menu''\n')
                show_menu(main_menu_filename)

        elif choice_basket == '2':

            print('Basket:')
            # Calling show_basket function
            show_basket(item_bought, item_bought_quantity, item_quantity_price_list)

            continue

        elif choice_basket == '3':

            print('Basket:')
            # Calling Remove_item function
            item_bought, item_bought_quantity, item_quantity_price_list, item_bought_unit_price = remove_item(
                item_bought, item_bought_quantity, item_quantity_price_list, item_bought_unit_price)

        elif choice_basket == '4':
            # 1. show_basket function
            # 2. write_bill function
            # 3. coupon function
            show_basket(item_bought, item_bought_quantity, item_quantity_price_list)
            total_amount = write_bill(bill_filename, item_bought, item_bought_quantity, item_quantity_price_list)
            coupon(coupon_filename, bill_filename, total_amount, name)

            break


market('MAIN_MENU.txt', 'FINAL_BILL.txt', 'COUPONS.TXT')
