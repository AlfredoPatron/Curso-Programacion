dic = {'clave1':100, 'clave2':500}

a = dic.popitem()
print(a)
print(dic)


marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)
