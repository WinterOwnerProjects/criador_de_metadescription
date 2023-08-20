def str_to_list(string):
    list = string.replace(" ", "-")
    list = list.split()
    return list
def metas_generator(list, gender):
    gender = gender.lower()
    list = str_to_list(list)
    for i in range(len(list)):
        item_da_lista = list[i]
        nome_produto = item_da_lista.replace("-", " ")
        if gender == "m":
            metadescription = "Conheça agora o {} da Bocchi Suprimentos! As melhores lonas plásticas, filmes para estufas e cordas do mercado!".format(nome_produto)
        elif gender == "f":
            metadescription = "Conheça agora a {} da Bocchi Suprimentos! As melhores lonas plásticas, filmes para estufas e cordas do mercado!".format(nome_produto)
        else:
            print("Erro, tente novamente dessa vez com M ou F! ")
            break
        with open(".\programa_de_criacao_de_metadescription\metas_descriptions.txt", "a" , encoding = "utf-8") as arquivo:
            arquivo.write(metadescription)
            arquivo.write("\n"+"\n")
def metas_generator_cat(list):
    list = str_to_list(list)
    for i in range(len(list)):
        item_da_lista = list[i]
        nome_produto = item_da_lista.replace("-", " ")  
        metadescription = "Confira agora nossos produtos da categoria {}! Bocchi Suprimentos, as melhores lonas plásticas, filmes para estufas e cordas do mercado!".format(nome_produto)
        with open(".\programa_de_criacao_de_metadescription\metas_descriptions.txt", "a" , encoding = "utf-8") as arquivo:
            arquivo.write(metadescription)
            arquivo.write("\n"+"\n")
            