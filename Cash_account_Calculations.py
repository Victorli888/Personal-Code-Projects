def format_rounded(num):
    return "{:.2f}".format(round(num, 2))


def findBalance(starting_amount, interest_percent, deposit, num_years):
    # Interest rate is compounded every day, and paid out monthly
    daily_interest = (interest_percent / (100*365))

    compounded_amount = starting_amount
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul",
              "Aug","Sep","Oct","Nov","Dec"]
    last_compounded = compounded_amount
    curr_year = 2023

    for year in range(num_years):
        for day in range(365):
            compounded_amount = compounded_amount * (1 + daily_interest)

            # bi-weekly Paychecks
            if day % 15 == 0 and day != 0:
                compounded_amount += deposit


            # Monthly
            if day % 30 == 0 and day != 0:
                month = (day // 30) - 1  # 0th Index
                monthly_payout = compounded_amount - last_compounded - 2*deposit
                rounded_formated_payout = format_rounded(monthly_payout)

                print(f"As of {months[month]} {curr_year}, Current balance: ${format_rounded(compounded_amount)}, Payout this month was:"
                       f"${rounded_formated_payout}")

                last_compounded = compounded_amount
        curr_year += 1
    return format_rounded(compounded_amount)
