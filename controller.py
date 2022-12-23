import view
import model


def start_spav():
    iam = ''
    spr = []
    iam = view.privet()
    while True:
        select = view.menu(iam)
        if select == '9': 
            break
        elif select == '1': 
            spr = model.load_spr()
            print('Справочник успешно считан из файла \n')
        elif select == '2': 
            if spr != []:
                view.view_spr_loader(spr)
            else:
                print(f'{iam}, сначало необходимо загрузить справочник \n')
        elif select == '3': 
            sprav = model.read_spr_file()
            view.view_read_spr(sprav)
        elif select == '4': 
            data = view.employee(iam)
            model.add_employee(data)
        elif select == '5': 
            sprav = model.read_spr_file()
            view.view_read_spr(sprav)
            number = view.nom_employee(iam)
            if number != 0:
                data = view.employee(iam)
                model.change_employee(number,data)
            else:
                print(f'{iam}, необходимо ввести правильный номер сотрудника \n')
                            
        elif select == '6': 
            sprav = model.read_spr_file()
            view.view_read_spr(sprav)
            number = view.nom_employee(iam)
            if number != 0:
                model.delete_employee(number)
            else:
                print(f'{iam}, необходимо ввести правильный номер сотрудника \n')

        elif select == '7': 
            spr = model.load_spr()
            model.export_csv(spr, iam)
            
        elif select == '8': 
            spr = model.load_spr()
            model.export_txt(spr, iam)
            
        else:
            continue