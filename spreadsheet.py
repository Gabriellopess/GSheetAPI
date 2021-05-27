import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1w-mgy_DsnAaw6lFnV9xmeDfzQy2_iWIzUYjLUhX6SxA')
worksheet = sh.sheet1

def spreadsheet(value):
    #inicializa a primeira linha para definir cada coluna caso a planilha esteja em branco.
    values_list = worksheet.get('A1:F1')
    if values_list == []:
        worksheet.update('A1:F1', value)
    else:
        print('já existe')

columns = [['Nome', 'CPF', 'Idade', 'User SignIn Date', 'Product SignIn Date', 'Produtos Totais']]
spreadsheet(columns)

# print(worksheet.get_all_records()[2].get('CPF'))
# print(worksheet.get('B2:B7'))
# print(worksheet.col_values(2)[1])
# worksheet.update('A7', '02066639435')


def createUser(json):
    #Criar usuário
    if type(json) == list and len(json) <= 4:
        worksheet.append_row(json)      
    else:
        print('not now')

# def get_rowindex(string):
#     #Identifica em qual linha se encontra o usuário a partir do seu cpf
#     if type(string) == str:
#         index = 0
#         list = worksheet.get_all_records()
#         for i in range(len(list)):
#             if list[i].get('CPF') == string:
#                 obj = list[i]
#                 index = i
#                 print(obj, index, i) 
#         row = index + 2
#         print(row)
#         return row

def get_rowindex(string):
    #Identifica em qual linha se encontra o usuário a partir do seu cpf
    if type(string) == str:
        index = 0
        row = 0
        list = worksheet.col_values(2) #na coluna 2 se encontram os CPFs
        for i in range(len(list)):
            if list[i] == string:
                obj = list[i]
                index = i
                row = index + 1
        return row

def updateUser(cpf, json):
    if type(json) == list and type(cpf) == str and len(json) <= 4: 
        row = get_rowindex(cpf)
        cell_range = str('A'+str(row)+':F'+str(row))
        json_list = [json]
        worksheet.update(cell_range, json_list)
    else:
        print('not now')


def deleteUser(cpf):
    if type(cpf) == str:
        row = get_rowindex(cpf)
        worksheet.delete_rows(row)
    else:
        print('not now')


def updateProdutoDate(cpf, value):
    if type(cpf) == str:
        row = get_rowindex(cpf)
        cell = str('E'+str(row))
        worksheet.update(cell, value)


def updateTotalProduto(cpf, value):
    if type(cpf) == str:
        row = get_rowindex(cpf)
        cell = str('F'+str(row))
        worksheet.update(cell, value)
        print(cpf + " e " + cell)
