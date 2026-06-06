'''Question: Good Day
Given a time string in "HH:MM" format (24-hour clock), return:

"Good morning" for times 05:00 to 11:59
"Good afternoon" for times 12:00 to 17:59
"Good evening" for times 18:00 to 21:59
"Good night" for times 22:00 to 04:59
Tests:
Passed:1. get_greeting("06:30") should return "Good morning".
Passed:2. get_greeting("12:00") should return "Good afternoon".
Passed:3. get_greeting("21:59") should return "Good evening".
Passed:4. get_greeting("00:01") should return "Good night".
Passed:5. get_greeting("11:30") should return "Good morning".'''def get_greeting(s):
    x = float(s[0]) * 10 + float(s[1])
    y = float(s[3]) / 10 + float(s[4]) / 100
    z = x + y

    if 5.00 <= z <= 11.59:
        return 'Good morning'
    elif 12.00 <= z <= 17.59:
        return 'Good afternoon'
    elif 18.00 <= z <= 21.59:
        return 'Good evening'
    else:
        return 'Good night'