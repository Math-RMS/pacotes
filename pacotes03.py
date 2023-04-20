while True:
    try:
        numero = int(input("Entre com um número: "))
        print(numero/5)
        break
    except ValueError:                                   
        print('Valor Errado.')
    except ZeroDivisionError:
        print("Desculpe. Não posso divivdir por zero.")
    except:
        print("Nâo sei o que fazer...")
    
'''
    except ValueError:                                                                      
        print('Valor Errado.')
    except ZeroDivisionError:                             poderia ser escrito em uma linha    except (ValueError, ZeroDivisionError):
        print("Desculpe. Não posso divivdir por zero.")                                             print("Valor errado ou Não é possível dividir por zero.)
'''