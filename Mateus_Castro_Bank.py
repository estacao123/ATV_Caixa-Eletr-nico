from datetime import datetime
SPACE = ('===========================================================')
class User:
    def __init__(self,name: str, agency: int, account: int, password: int, key: int = None, balance: int = 1500,limit: int = 0 ):
        self.name = name 
        self.agency = agency
        self.account = account
        self.password = password
        self.key = key 
        self.balance = balance 
        self.limit = limit
        self.statement = []


    def exhibit(self):
        print(f"Nome: {self.name}")
        print(f"Agencia: {self.agency}")
        print(f"Conta: {self.account}")
        print(f"Senha: {self.password}")
        

    def balanceExhibit(self):
        print(f"Saldo: {self.balance}")  
         
    
    def limitExhibit(self):
        print(f"Limite: R$ {self.limit}")
        
    
    def statementExhibit(self):
        print("\n--- Extrato ---")

        if not self.statement:
            print("Nenhuma transção registrada")
        else:
            for movement in self.statement:
                print(movement)


    @classmethod
    def NewUserCreator(cls):
        name = input("Digite o nome do usuario: ")
        agency = int(input("Digite a agencia do usuario: "))
        account = int(input("Digite a conta do usuario: "))
        password = int(input("Digite a senha do usiario: "))
        return cls(name, agency, account, password)
    
testUser = User(name = "Arlindo Orlando",agency = 2233, account = 446677, password = 280985)

users = [testUser]

def login():
    while True:
        print(SPACE)
        print("\n--- LOGIN ---")
        agencyLogin = int(input("Digite sua agência: "))
        accountLogin = int(input("Digite sua conta: "))
        passwordLogin = int(input("Digite sua senha: "))

        
        user = None
        for u in users:
            if u.agency == agencyLogin and u.account == accountLogin and u.password == passwordLogin:
                user = u
                break

        if user is None:
            print("Dados incorretos! Tente novamente.\n")
            continue 

        return user
                
def panel():           
    while True:
        print("\n" + SPACE)
        print("digite 1 para login")
        print("digite 2 para criar conta")
        print("digite 3 para sair")
        print("\n" + SPACE)

        choice = int(input("O que deseja fazer?: "))

        if choice == 1:
            user = login()
            while True:
                print(SPACE)
                print("\n--- Painel do Usuário ---")
                print(f"\n Bem Vindo {user.name}")
                print(" 1 - Conferir saldo")
                print(" 2 - Conferir chave")
                print(" 3 - Fazer PIX")
                print(" 4 - Consultar limite")
                print(" 5 - Alterar limite")
                print(" 6 - Conferir Extato")
                print(" 7 - Depósito")
                print(" 8 - Saque")
                print(" 0 - Sair do Painel do Usuário")
                print(SPACE)

                choice1 = int(input("O que deseja fazer ?: "))

                if choice1 == 0:
                    print(SPACE)
                    print("Saindo do painel...")
                    print(SPACE)
                    break 

                if choice1 == 1:
                    print("\n---Saldo---")
                    user.balanceExhibit()
                
                elif choice1 == 2:
                    print("\n --- Chave PIX ---")
                    if user.key != None:
                        print(f"Esta é sua chave {user.key}")
                        
                    else:
                        print(SPACE)
                        print("Chave não criada")
                        user.key = int(input("Digite sua chave :"))
                        print("Chave criada")
                        
                
                elif choice1 == 3:
                    print("\n--- PIX ---")
                    k = int(input("Digite a chave PIX do destinatario: "))
                    value = int(input("Digite o valor do PIX: "))
                    password = int(input("Digite sua senha: "))

                    if k != user.key :
                        if user.key != None:
                            if user.balance - value >= -user.limit:
                                if password == user.password :
                                    user.balance -= value
                                    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                                    user.statement.append (f"PIX de R${value} Para {k} no dia {data}")
                                    print ("\nPix efetuado com sucesso!")
                                else:
                                    print("Senha incorreta tente novemante!")
                            else:
                                print("Saldo insuficiente!")
                        else:
                            print("Você ainda nao possui chave pix") 
                            print("Você pode criar outra chave na opção 2 no painel")   
                    else:
                        print("Essa é a sua chave, tente outra chave")
                    
                elif choice1 == 4:
                    print("\n --- Limite ---")
                    user.limitExhibit()
                
                elif choice1 == 5:
                    print("\n --- Alterando Limite ---")
                    agreement = input("Você tem certeza que quer alterar seu limite ? s/n:").lower()
                    if agreement == "s":
                        user.limitExhibit()
                        user.limit = int(input("Para quanto você deseja alterar seu limite ?: "))
                        print(f"Limite alterado para R$ {user.limit}.")
                    elif agreement == "n":
                        print("Muito bem! ")
                    else:
                        print("Opção inválida digite s ou n ")
                
                elif choice1 == 6:
                    user.statementExhibit()
                    user.balanceExhibit()
                
                elif choice1 == 7:
                   print("\n---Depósito---")
                   deposit = int(input("Valor do depósito: "))
                   data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                   user.balance += deposit
                   user.statement.append (f"Depósito de R${deposit} no dia {data}")
                   print("Depósito realizado com sucesso!")

                elif choice1 == 8:
                    print("\n---Saque---")
                    sake = int(input("Valor do saque: "))
                    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    if user.balance - sake >= -user.limit:
                        user.balance -= sake
                        user.statement.append (f"Saque de R${sake} no dia {data}")
                        print("Saque realizado com sucesso!")
                    else:
                        print("Saldo insuficiente")
                     
        elif choice == 2:
            new_user = User.NewUserCreator()
            users.append(new_user)
            print("\nUsuário criado com sucesso!")
        elif choice == 3:
            print(SPACE)
            print("encerrando o sistema...")
            print(SPACE)
            break
        else:
            print("Opcao invalida")

 
    
panel() 