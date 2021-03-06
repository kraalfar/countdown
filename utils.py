import numpy as np

rules = """Во-первых, Вова питух.
Во-вторых, правила.\n
-Чтобы начать игру напишите `/буквы n m l`. n, m, l это количество гласных, согласных и специальных (ъ, ь) букв в раунде. Всего должно быть 9 букв. Гласных (n) хотя бы три должно быть, согласных (m) хотя бы 4, 
а специальных (l) не больше одного. После этого вы должны составить одно слово из этих букв, использовать букву можно столько раз сколько она встретилась. Имена собственные и слова с дефисами использовать нельзя. Но любые формы слов подходят.\n
-Чтобы проверить ваше слово напишите `/проверь слово`. 
"""

vowels = ['а',
          'е',
          'и',
          'о',
          'у',
          'э',
          'ю',
          'ы',
          'я',
          'ё']

vowels_weights = np.array([0.1894197, 0.19973214, 0.1738221, 0.25925833, 0.06197047,
                           0.00753293, 0.01506821, 0.0448949, 0.04743602, 0.00086519])
# vowels_weights = [40487008,
#                   42691213,
#                   37153142,
#                   55414481,
#                   13245712,
#                   1610107,
#                   3220715,
#                   9595941,
#                   10139085,
#                   184928]

consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м',
              'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

consonants_weights = np.array([0.02849634, 0.08115504, 0.03031147, 0.05327157, 0.0168,
                               0.0294807, 0.02161092, 0.06247811, 0.07867572, 0.05734491,
                               0.11976056, 0.05026136, 0.08464501, 0.09777598, 0.11191107,
                               0.0047274, 0.01735657, 0.00863128, 0.02583641, 0.01301957,
                               0.00645])
# consonants_weights = [8051767,
#                       22930719,
#                       8564640,
#                       15052118,
#                       4746916,
#                       8329904,
#                       6106262,
#                       17653469,
#                       22230174,
#                       16203060,
#                       33838881,
#                       14201572,
#                       23916825,
#                       27627040,
#                       31620970,
#                       1335747,
#                       4904176,
#                       2438807,
#                       7300193,
#                       3678738,
#                       1822476]

specials = ['ь', 'ъ']

specials_weights = np.array([0.97932546, 0.02067454])
# specials_weights = [8784613,
#                     185452]
