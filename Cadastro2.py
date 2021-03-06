import pandas as pd
import os
import csv
 
class Cadastro():
    def __init__(self):
      
        self.matricula = input('Digite a sua matrícula: ')
        self.nome = input('Digite o seu nome: ')
        print('\nBem vindo,{}'.format(self.nome))
        self.email = input('Digite o seu email: ')
        assert '@' in self.email,'Email inválido' # @ assert
        assert '.com' in self.email,'Email inválido.' # .com assert
        self.celular = input('Digite o seu celular: ')
        assert len(self.celular) == 8, 'Número invalido. Comece novamente' # len assert
        self.endereço = input('Digite o seu endereço: ')
        self.numero = input('Digite o número da sua residência: ')
        self.bairro = input('Agora digite o bairro: ')
        self.cidade = input('Digite a sua cidade: ')
        self.complemento = input('Complemento: ')
        self.cargo = input('Qual cargo você ocupa atualmente: ')
        self.salario = int(input('Qual o seu salário atual? : '))
        self.setor = input('Em qual setor você atua? : ')
        

    def calc_inss(self):
        if self.salario <= 1045:
            self.desconto_inss = self.salario * 0.075
        elif self.salario <= 2089.60:
            self.desconto_inss = self.salario * 0.09
        elif self.salario <= 3134.40:
            self.desconto_inss = self.salario * 0.12
        else:
            self.desconto_inss = self.salario * 0.14
        
        return(self.desconto_inss)
        print('Desconto INSS: ', self.desconto_inss)

    def calc_irrs(self):
        if self.salario <= 1659.38:
            self.desconto_irrs = self.salario * 0.08
        elif self.salario <= 2765.66:
            self.desconto_irrs = self.salario * 0.09
        elif self.salario <= 5531.31:
            self.desconto_irrs = self.salario * 0.11
        else:
            self.desconto_irrs = 604.44
        
        return(self.desconto_irrs)
        print('Desconto IRRS: ', self.desconto_irrs)


    def mostrar(self):
        
        
        return('\nNome: {}'.format(self.nome) + '\nMatrícula: {}'.format(self.matricula)
                 + '\nCelular: {}'.format(self.celular) + '\nEndereço: {}'.format(self.endereço) + '\nNúmero da casa: {}'.format(self.numero)
               + '\nBairro: {}'.format(self.bairro) + '\nCidade: {}'.format(self.cidade) + '\nComplemento: {}'.format(self.complemento)
              + '\nCargo: {}'.format(self.cargo) + '\nSalário: {}'.format(self.salario) + '\nSetor: {}'.format(self.setor) +
             '\nEmail: {}'.format(self.email))
        print('\n Confira os dados que foram digitados: ' + '\n Nome: {}'.format(self.nome) + '\n Matrícula: {}'.format(self.matricula)
                 + '\n Celular: {}'.format(self.celular) + '\n Endereço: {}'.format(self.endereço) + '\n Número da casa: {}'.format(self.numero)
               + '\n Bairro: {}'.format(self.bairro) + '\n Cidade: {}'.format(self.cidade) + '\n Complemento: {}'.format(self.complemento)
              + '\n Cargo: {}'.format(self.cargo) + '\n Salário: {}'.format(self.salario) + '\n Setor: {}'.format(self.setor) +
             '\n Email: {}'.format(self.email))
        
    def dataframe(self):
                
        descontado_inss = self.calc_inss()
        descontado_irrs = self.calc_irrs()
        salario_liquido = self.salario - descontado_inss - descontado_irrs
        
        data1 = {'Nome':self.nome,'Matricula':self.matricula,'Cidade':self.cidade,'Setor':self.setor,'Cargo':self.cargo,'Salario Bruto':self.salario,'Desconto Inss':descontado_inss,'Desconto Irrs':descontado_irrs,'Salário Liquido':salario_liquido}
        df = pd.DataFrame(data=data1,index=[0])
        
        perg = input('Salvar? (s/n)')
        if perg == 's' or 'S':
            if os.path.exists(caminho):
                df.to_csv(caminho,mode='a',header=False)
            else:
                df.to_csv(caminho)
                df.append(df)


            
       
                
            
class Listar():
    def listar_por_setor(self):
        df_list = pd.read_csv(caminho)  
        grupo_setor = df_list.groupby(['Setor'])

        for key, item in grupo_setor:
            print(grupo_setor.get_group(key), "\n")
    

            

    def listar_df(self):
        df_full = pd.read_csv(caminho)
        print(df_full)



def perg_inicial():
    perg_init = input('Olá. \n Insira o número correspondente : 1 - Cadastrar Funcionário /// 2 - Listar Funcionários /// 3 - Listar Custo Por Setor : ') 
    if perg_init == '1':
        cad = Cadastro()
        cad.mostrar()
        cad.calc_inss()
        cad.calc_irrs()
        cad.dataframe()
    elif perg_init == '2':
        lista= Listar()
        lista.listar_df()
    else:
        lista = Listar()
        lista.listar_por_setor()
        

    perg_final = input('Deseja realizar outra operação? (s/n) : ')
    if perg_final == 's':
        perg_inicial()
    else:
        pass

qst = input('É a primeira vez usando o programa? (s/n) :')
if qst == 's':
    caminho = input('Bem vindo,Aonde você deseja salvar o arquivo? Ex: C:/       :')
else:
    p = input('Já possui um arquivo Cadastro criado? (s/n) : ')
    if p == 's':
        caminho = input('Especifique o caminho do arquivo : ')
    else:
        caminho = input('Aonde você deseja salvar o arquivo? Ex: C:/       :')

perg_inicial()

#cad = Cadastro()
#cad.mostrar()
#cad.calc_inss()
#cad.calc_irrs()
#cad.dataframe()

#lista = Listar()
#lista.listar_por_setor()
#lista.listar_df()    
       
    
 