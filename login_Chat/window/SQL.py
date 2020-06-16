import pymssql




def common(cn, sql):
    cursor = cn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    information = []
    for row in results:
        information.append(row)
    return information


def Judge_account(account):
    """用于判断账号是否存在"""
    cn = pymssql.connect("DESKTOP-AT2JRG0", "gyp", "gaoyupeng", "test")
    sql = '''select distinct name
            from name_account
            '''

    aacount = common(cn, sql)
    for acc in aacount:
        if acc[0] == account:
            return 1
    return 0


def Judge_ac_and_pw(account, password):
    """用于判断账号和密码是否匹配"""
    cn = pymssql.connect("DESKTOP-AT2JRG0", "gyp", "gaoyupeng", "test")
    sql = '''select name, password
                    from name_account
                    '''
    aaccount = common(cn, sql)
    for acpw in aaccount:
        if acpw[0] == account and acpw[1] == password:
            return 1
    return 0
# class Ab():
#     def C(self):
#         sql = '''select name,password
#                 from name_account
#                 '''
#         account = common(cn, sql)
#         for row in account:
#             if row[1] == "gaoyupeng11":
#                 print('ok')
#
# Tom = Ab()
# Tom.C()
