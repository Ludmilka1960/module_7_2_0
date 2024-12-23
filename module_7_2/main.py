
def custom_write(file_name,strings):
    strings_positions = {}
    file = open(file_name,'w',encoding='utf-8')
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(0,len(strings)):
            byte_position = file.tell()
            file.write(f"{strings[i]}" '\n')
            strings_positions [(i+1,byte_position)] = strings[i]
        file.close()
        return strings_positions


info = [
    'Sun of the sleepless ',
'Melancholy star ',
'Whose tearful beam ',
'glows tremulously far ']
result = custom_write('Записать и запомнить.txt', info)
for elem in result.items():
    print(elem)