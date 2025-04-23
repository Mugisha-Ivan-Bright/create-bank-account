from flask import Flask, render_template, render_template, request , session , redirect , url_for

app = Flask(__name__)
app.secret_key ='super_screte_key_123'

customers = [{ 'customer':"Mugisha Ivan Bright",
               'Bank':[{'name':'BK','Transaction_id':'1','Account_no':'100-33-23-2025','password':'bk_password123'},{'name':'Umutanguha Finance','Transaction_id':'1','Account_no':'10-03-43-2006','password':'umutanguha3044_child'},{'name':'Equity bank','Transaction_id':'1','Account_no':'E0D4-004-230-2024','password':'EQUITY-BANK_CHILDREN-BEFORE'}],
               'sponsor':'Twagirayezu Felicien',
               'email':'mugishaivanbright250@gmail.com',
               'password':'password123'
                },
             { 'customer':'Muneza Delphin',
               'Bank':[{'name':'EQUITY Bank','Transaction_id':'2','Account_no':'E0D4-304-043-2024','password':'my_munez123'}],
               'sponsor':'Uwera Donate',
               'email':'mugishaivanbright250@gmail.com',
               'password':'delphin123321'
               },
             { 'customer':'Twahirwa Peter',
               'Bank':[{'name':'EQUITY Bank','Transaction_id':'3','Account_no':'E0D4-004-049-2021','password':'pteTwahi123'}],
               'sponsor':None,
               'email':'mugishaivanbright250@gmail.com',
               'id':'000000000000000000000009999999999',
               'password':'petersonLogin'
               },
             { 'customer':'Uwineza Judth',
               'Bank':[{'name':'Umutanguha Finance','Transaction_id':'2','Account_no':'034-304-023-2024','password':'uwineza_umutanguha234'}],
               'sponsor':None,
               'id':'555555555555555555553333322222222',
               'email':'mugishaivanbright250@gmail.com',
               'password':'uwinezaLogin'
               },
             { 'customer':'William chung',
               'Bank':[{'name':'EQUITY Bank','Transaction_id':'4','Account_no':'E5D4-304-043-2024','password':'willleeez123'}],
               'sponsor':None,
               'id':'0000000234999943043944444444444440',
               'email':'mugishaivanbright250@gmail.com',
               'password':'williamLogin'
               },
                   {
                'customer': "Manzi Patrick",
                'Bank': [{'name': 'BK', 'Transaction_id': '2', 'Account_no': '103-88-55-2025', 'password': 'patrickBK2025'}],
                'sponsor': 'Kabera Claude',
                'email': 'patrick.manzi@example.com',
                'password': 'patrick_pass'
            },
            {
                'customer': "Iradukunda Divine",
                'Bank': [{'name': 'BK', 'Transaction_id': '3', 'Account_no': '104-99-11-2025', 'password': 'divine_bk987'}],
                'sponsor': None,
                'id': '11112222333344445555666677778888',
                'email': 'divine.iradukunda@example.com',
                'password': 'divine2025'
            },
            {
                'customer': "Uwimana Joseph",
                'Bank': [{'name': 'UMUTANGUHA Finance', 'Transaction_id': '3', 'Account_no': '051-101-333-2024', 'password': 'uwimana_umu24'}],
                'sponsor': 'Dusabimana Rose',
                'email': 'uwimana.joseph@example.com',
                'password': 'joseph123'
            },
            {
                'customer': "Munyaneza Claude",
                'Bank': [{'name': 'UMUTANGUHA Finance', 'Transaction_id': '4', 'Account_no': '052-777-888-2024', 'password': 'munya_umu2024'}],
                'sponsor': None,
                'id': '99999999988888888887777777766666',
                'email': 'claude.munyaneza@example.com',
                'password': 'claude_secure'
            },
            {
                'customer': "Niyitegeka Alice",
                'Bank': [{'name': 'EQUITY Bank', 'Transaction_id': '5', 'Account_no': 'E0D4-999-333-2025', 'password': 'alice_equity2025'}],
                'sponsor': 'Nkundwa Ange',
                'email': 'alice.niyitegeka@example.com',
                'password': 'niyalice2025'
            },
            {
                'customer': "Byiringiro Isaac",
                'Bank': [{'name': 'EQUITY Bank', 'Transaction_id': '6', 'Account_no': 'E0D4-456-123-2025', 'password': 'isaacEqty987'}],
                'sponsor': None,
                'id': '22223333444455556666777788889999',
                'email': 'isaac.byiringiro@example.com',
                'password': 'isaac_pass'
            },
            {
                'customer': "Uwase Aline",
                'Bank': [{'name': 'BK', 'Transaction_id': '4', 'Account_no': '105-44-77-2025', 'password': 'alineBK88'}],
                'sponsor': 'Gasasira Elie',
                'email': 'aline.uwase@example.com',
                'password': 'aline_bk2025'
            },
            {
                'customer': "Karangwa Jules",
                'Bank': [{'name': 'UMUTANGUHA Finance', 'Transaction_id': '5', 'Account_no': '053-654-321-2025', 'password': 'karu_umu2025'}],
                'sponsor': None,
                'id': '77788899900011122233344455566677',
                'email': 'karangwa.jules@example.com',
                'password': 'karulesafe'
            },
            {
                'customer': "Ingabire Liliane",
                'Bank': [{'name': 'EQUITY Bank', 'Transaction_id': '7', 'Account_no': 'E0D4-888-777-2025', 'password': 'lily_eqpass'}],
                'sponsor': None,
                'id': '10101010101010101010101010101010',
                'email': 'liliane.ingabire@example.com',
                'password': 'lily_secure'
            },
            {
                'customer': "Kamanzi Theoneste",
                'Bank': [{'name': 'EQUITY Bank', 'Transaction_id': '8', 'Account_no': 'E0D4-222-555-2025', 'password': 'kamanziEQT'}],
                'sponsor': 'Nirere Tracy',
                'email': 'kamanzi.theoneste@example.com',
                'password': 'theo_pass'
            }
              
               ]

bk_transactions =[{'Transaction_id':'1','deposit':10000,'Balance':2300 ,'message':['You currently have no message available']},{'Transaction_id': '2', 'deposit': 5000, 'Balance': 4000, 'message': ['SMS alert activated']},{'Transaction_id': '3', 'deposit': 12000, 'Balance': 9000, 'message': ['BK transfer completed']},{'Transaction_id': '4', 'deposit': 7000, 'Balance': 3200, 'message': ['Loan interest deducted']}]
umtangh_transactions =[{'Transaction_id':'1','deposit':10000,'Balance':2034, 'message':['You currently have no message available']},{'Transaction_id':'2','deposit':10000,'Balance':5000, 'message':['You currently have no message available']} , {'Transaction_id': '3', 'deposit': 6000, 'Balance': 3000, 'message': ['Mini-statement generated']},{'Transaction_id': '4', 'deposit': 7500, 'Balance': 5100, 'message': ['Welcome to UMUTANGUHA!']},{'Transaction_id': '5', 'deposit': 8000, 'Balance': 6600, 'message': ['Your savings increased']}]
equity_transactions = [{'Transaction_id':'1','deposit':10000, 'Balance':3000, 'message':['You currently have no message available']},{'Transaction_id':'2' ,'deposit':10000, 'Balance':4000, 'message':['You currently have no message available']},{'Transaction_id':'3' ,'deposit':10000, 'Balance':5000, 'message':['You currently have no message available']},{'Transaction_id':'4' ,'deposit':10000, 'Balance':6000, 'message':['You currently have no message available']},{'Transaction_id': '5', 'deposit': 13000, 'Balance': 8900, 'message': ['Equity: Your PIN was changed']},{'Transaction_id': '6', 'deposit': 11000, 'Balance': 7200, 'message': ['Airtime purchased']},{'Transaction_id': '7', 'deposit': 10000, 'Balance': 4500, 'message': ['Equity loan interest paid']}, {'Transaction_id': '8', 'deposit': 14000, 'Balance': 9900, 'message': ['Cash sent to BK']}]

allowed_bank_info =[{'Bank':'BK','security':'2%' , 'insurance':'$50'} ,{'Bank':'EQUITY Bank','security':'3%','insurance':'$40'},{'Bank':'UMUTANGUHA Finance','security':'1%','insurance':20}]



@app.route("/" , methods =['GET','POST'])
def index():
    return render_template('index.html')
def make_deposit():
    pass
@app.route("/submit" , methods =['POST'])
def submit():

    name = request.form.get('name')
    email =request.form.get('email')
    bank =request.form.get('radio')
    password = request.form.get('password')
    balance =""
    deposit =""
    message =""

    if name and email and bank and password:
        def authenticate_customer(name,email,bank,password):
                matched_customer = next((c for c in customers if c['customer'].lower()==name.lower() and c['email'] ==email and c['password']==password),None)
                if matched_customer:
                    bank_selected = next((b for b in matched_customer['Bank'] if bank.lower()==b['name'].lower()),None)
                    if bank_selected:
                        bank_info = next((sec for sec in allowed_bank_info if sec['Bank'].lower()==bank_selected['name'].lower()),None)
                        transaction_id = bank_selected['Transaction_id']

                        if bank_selected['name'].lower() =='bk':
                            deposit = next((depos['deposit'] for depos in bk_transactions if depos['Transaction_id'] ==transaction_id))
                            balance = ((int(deposit) * 2) / 100) - 50
                            message = next((depos['message'] for depos in bk_transactions if depos['Transaction_id'] ==transaction_id))
                            balance = int(deposit) - (((int(deposit) * 2) / 100) + 50)
                        elif bank_selected['name'].lower() =='umutanguha finance':
                            deposit = next((depos['deposit'] for depos in umtangh_transactions if depos['Transaction_id'] ==transaction_id))
                            balance = int(deposit) - (((int(deposit) *1) / 100) + 20)
                            message = next((depos['message'] for depos in umtangh_transactions if depos['Transaction_id'] ==transaction_id))
                        elif bank_selected['name'].lower() =='equity bank':
                            deposit = next((depos['deposit'] for depos in equity_transactions if depos['Transaction_id'] ==transaction_id))
                            balance = int(deposit) - (((int(deposit) *3) / 100) + 40)
                            message = next((depos['message'] for depos in equity_transactions if depos['Transaction_id'] ==transaction_id))                            

                        session['transaction'] ={'name':name,'bank_selected':bank_selected['name'],'deposit':deposit,'balance':balance , 'message':message} 
                       
                        mes = session['transaction']
                        return  render_template("transaction.html" ,message = message , customer = request.form.get('name'), bank_info = bank_info,balance =balance , deposit = deposit  )
                    else:
                        return render_template(
                                "Error-page.html",
                                error_code="Bank Not Registered",
                                error_message="The selected bank is not associated with your account.",
                                error_details="Try registering that bank account so we can manage your transactions. Thank you!"
                            )
                else:

                    return render_template(
                            "Error-page.html",
                            error_code="Authentication Failed",
                            error_message="Incorrect name, email, or password.",
                            error_details="Please make sure your details are correct."
                        )
        return authenticate_customer(name,email,bank,password)
    
              

@app.route('/transaction' , methods =['POST'])

def send_money():
    if request.method =='POST':

        new_transactions = session['transaction']
        receiver_account = request.form.get('account')        
        sending_amount = request.form.get('amount')
        receivers_bank = request.form.get('bank')
        message = request.form.get('message')
        my_account_code = request.form.get('account_code')

        match_of_bank = next((b['Bank'] for b in customers if b['customer'].lower()==new_transactions.get('name').lower()),None)
        if match_of_bank:
            match_of_account = next((ac['Account_no'] for ac in match_of_bank if ac['Account_no']==my_account_code and ac['name'].lower()==new_transactions.get('bank_selected').lower()),None)
            if match_of_account:
                get_balance = int(new_transactions.get('balance'))
                if get_balance < int(sending_amount):
                  return render_template('Error-page.html',error_code=400,error_message='The funds are insuffient',error_details=f'Sorry your balance is not enough to send $ {sending_amount}')
                else:
                    get_receiver_name =None
                    receiver_bank_account_info = None

                    for customer in customers:
                        for ba in customer['Bank']:
                          if ba['name'].lower() == receivers_bank.lower() and ba['Account_no']==str(receiver_account):
                            receiver_bank_account_info = ba
                            get_receiver_name =customer['customer']
                            break
                    if receiver_bank_account_info:
                        receiver_transaction_id = receiver_bank_account_info['Transaction_id']
                        receiver_transaction = None

                        if receiver_bank_account_info['name'].lower() =='bk':
                            receiver_transaction= next((depos for depos in bk_transactions if depos['Transaction_id'] ==receiver_transaction_id),None)

                        elif receiver_bank_account_info['name'].lower() =='equity bank':  
                            receiver_transaction = next((depos  for depos in equity_transactions if depos['Transaction_id'] ==receiver_transaction_id),None)
                        elif receiver_bank_account_info['name'].lower() =='umutanguha finance':
                            receiver_transaction = next((depos  for depos in umtangh_transactions if depos['Transaction_id'] ==receiver_transaction_id),None)
                        if receiver_transaction:
                            receiver_transaction['deposit'] +=int(sending_amount)

                        message_to_sender_required_info =None
                        message_to_sender =None
                        new_balance = None
                        
                        for customer in customers:
                            for b in customer['Bank']:
                                if b['Account_no'] ==my_account_code and customer['customer'] ==  new_transactions.get('name'):
                                    message_to_sender_required_info = b
                                    break
                        if message_to_sender_required_info:
                              if message_to_sender_required_info['name'].lower() =='bk':
                                  message_to_sender = next((messg['message'] for messg in bk_transactions if messg['Transaction_id'] ==message_to_sender_required_info['Transaction_id']),None)
                                  new_balance = next((bal for bal in bk_transactions if bal['Transaction_id']==message_to_sender_required_info['Transaction_id']),None)
                              elif message_to_sender_required_info['name'].lower() =='equity bank':
                                  message_to_sender = next((messg['message'] for messg in equity_transactions if messg['Transaction_id'] ==message_to_sender_required_info['Transaction_id']),None)
                                  new_balance = next((bal for bal in equity_transactions if bal['Transaction_id']==message_to_sender_required_info['Transaction_id']),None)                            
                              elif message_to_sender_required_info['name'].lower() =='umutanguha finance':
                                  message_to_sender = next((messg['message'] for messg in umtangh_transactions if messg['Transaction_id'] ==message_to_sender_required_info['Transaction_id']),None)
                                  new_balance = next((bal  for bal in umtangh_transactions if bal['Transaction_id']==message_to_sender_required_info['Transaction_id']),None)  
      
                              new_balance['deposit'] = int(new_balance['deposit']) - int(sending_amount)
                            
                              message_to_sender.append(f"You have sent ${sending_amount} to {get_receiver_name}")
      
                              message_to_receiver = receiver_transaction['message']
                              message_to_receiver.append(f"You have received {sending_amount} from {new_transactions['name']} ")
      
      
                              return render_template("transaction_summary.html", 
                              
                                  receiver = get_receiver_name,
                                  send_amount=sending_amount,
                                  receivers_bank=receivers_bank,
                                 
                              )

                    else:
                         return render_template('Error-page.html',error_code=400,error_message='Invalid Receiver\'s credentials',error_details='pLease check your receiver\'s account number or user name.and try again')



           




                    # new_transactions['deposit'] =  int(new_transactions['deposit']) - int(sending_amount)
                    



            else:
                return render_template('Error-page.html',error_code=400,error_message='Invalid account number',error_details='pLease check your account number very well')

    else:
        return render_template('Error-page.html',error_code = 400,error_message="Bad request",error_details="Please.recheck your submission details")   

@app.route("/deposit" , methods =['GET','POST'])
def make_a_deposit():
    form_data = request.form
    user_session_info = session['transaction']
    for customer in customers:
        for b in customer['Bank']:
            if b['name'].lower() == user_session_info.get('bank_selected').lower() and customer['customer'].lower() == user_session_info.get('name').lower():
                user_bank_info = b
                break
    if user_bank_info:

        update_deposit = None
        if user_bank_info['name'].lower() =='bk':
            update_deposit = next((depos for depos in bk_transactions if user_bank_info['Transaction_id']==depos['Transaction_id']),None)
            and_add_message = next((mes for mes in bk_transactions if user_bank_info['Transaction_id'] == mes['Transaction_id']),None)
        
        elif user_bank_info['name'].lower() =='equity bank':
            update_deposit = next((depos for depos in equity_transactions if user_bank_info['Transaction_id']==depos['Transaction_id']),None)
            and_add_message = next((mes for mes in equity_transactions if user_bank_info['Transaction_id'] == mes['Transaction_id']),None)
        
        elif user_bank_info['name'].lower() =='umutanguha finance':
            update_deposit = next((depos for depos in umtangh_transactions if user_bank_info['Transaction_id']==depos['Transaction_id']),None)
            and_add_message = next((mes for mes in umtangh_transactions if user_bank_info['Transaction_id'] == mes['Transaction_id']),None)

        update_deposit['deposit'] +=int(form_data.get('amount'))
        and_add_message['message'].append(f"You have deposited ${form_data.get('amount')}")
        
        return render_template('make_a_deposit.html')
    else:
        return render_template('Error-page.html',error_code=500,error_message="Internal server error",error_details = "Sorry.Something went wrong")


if __name__ =="__main__":
    app.run(debug=True)
