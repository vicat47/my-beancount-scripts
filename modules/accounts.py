import re

import dateparser


def get_eating_account(from_user, description, time=None):
    if time == None or not hasattr(time, 'hour'):
        return 'Expenses:Meal:Snacks'
    elif time.hour <= 3 or time.hour >= 21:
        return 'Expenses:Meal:Snacks'
    elif time.hour <= 10:
        return 'Expenses:Meal:Breakfast'
    elif time.hour <= 16:
        return 'Expenses:Meal:Lunch'
    else:
        return 'Expenses:Meal:Dinner'


def get_credit_return(from_user, description, time=None):
    for key, value in credit_cards.items():
        if key == from_user:
            return value
    return "Unknown"


public_accounts = [
    'Assets:Company:Alipay:StupidAlipay'
]

credit_cards = {
    '中信银行': 'Liabilities:CreditCard:CITIC',
    '招商银行': 'Liabilities:Card:CMB',
}

accounts = {
    '招商银行(2697)': 'Liabilities:Card:CMB',
    '建设银行(6207)': 'Assets:Cash:CCB',
    '零钱': 'Assets:Balances:WeChat',
}

descriptions = {
    #'滴滴打车|滴滴快车': get_didi,
    '余额宝.*收益发放': 'Assets:Company:Alipay:MonetaryFund',
    '转入到余利宝': 'Assets:Bank:MyBank',
    '花呗收钱服务费': 'Expenses:Fee',
    '自动还款-花呗.*账单': 'Liabilities:Company:Huabei',
    '信用卡自动还款|信用卡还款': get_credit_return,
    '外卖订单': get_eating_account,
    '美团订单': get_eating_account,
    '上海交通卡发行及充值': 'Expenses:Transport:Card',
    '地铁出行': 'Expenses:Transport:City',
    '火车票': 'Expenses:Travel:Transport',
}

anothers = {
    '哪吒': get_eating_account,    # 楼下牛拉
    '吉野家美莲广场店': get_eating_account,
    '猴儿炸串': get_eating_account,
    '早点': get_eating_account,    # 小笼包
    '小丽姐姐麻辣烫米线店': get_eating_account,
    '麦当劳': get_eating_account,
    '五爷拌面': get_eating_account,
    '济南高新区大碗聚手擀面馆': get_eating_account,
}

incomes = {
    '余额宝.*收益发放': 'Income:Trade:PnL',
}

description_res = dict([(key, re.compile(key)) for key in descriptions])
another_res = dict([(key, re.compile(key)) for key in anothers])
income_res = dict([(key, re.compile(key)) for key in incomes])
