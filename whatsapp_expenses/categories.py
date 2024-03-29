#!/usr/local/bin/python

'''
Categories expenses
'''

def check_category(item):

    '''
    Check and return the category for an expense
    '''

    categories =  {

        'market':
            [
                'mercado',
                'chino',
                'carniceria',
                'friambreria',
                'panaderia',
                'maple',
                'dietetica',
                'bolson',
                'verduleria',
                'verdureira',
                'água',
                'fraldas',
                'fralda',
            ],

        'delivery':
            [
                'delivery',
                'rappi',
                'macdonald',
                'mac',
            ],

        'transport':
            [
                'taxi',
                'táxi',
                'uber',
                'cabify',
                'subte',
            ],

        'home':
            [
                'faxineira',
                'faxina',
                'limpeza',
                'agua',
            ],


        'health':
            [
                'farmacity',
                'farmacia',
                'psico',
                'barbearia',
            ],

        'fun':
            [
                'cafe',
                'café',
                'saida',
                'restaurante',
                'sobremesa',
                'starbucks',
                'propina',
                'gorgeja',
            ],
    }

    # Get list of keys that contains the given value
    category = [
        key for key, categories in categories.items()
            if item in categories
        ]

    if category:
        print(category)
    else:
        print('other')
