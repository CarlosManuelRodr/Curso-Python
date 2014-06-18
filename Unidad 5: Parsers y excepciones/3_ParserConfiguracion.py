#Encoding: utf-8
import configparser

# Carga parser.
parser = configparser.ConfigParser()
parser.read('config.ini')

# Lee todo el archivo de configuración.
for section_name in parser.sections():
    print('Section:', section_name)
    print('  Options:', parser.options(section_name))
    for name, value in parser.items(section_name):
        print('  %s = %s' % (name, value))
    print('')


# Añade a archivo de configuración.
f = open('config.ini', 'w')
parser.add_section('posible_drogadicto')
parser.set('posible_drogadicto', 'nombre', 'Baldemar')
parser.set('posible_drogadicto', 'sustancia', 'cocaina')
parser.set('posible_drogadicto', 'estado', 'peligro')
parser.write(f)