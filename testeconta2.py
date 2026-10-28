import testeconta1
conta1 = testeconta1.conta()
conta2 = testeconta1.conta()
conta1.info(nome="carlos")
conta2.info(nome="pedro")
contas = {1:conta1, 2:conta2}

print (contas[1].nome)