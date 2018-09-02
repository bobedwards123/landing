from htmlgen import webgen
from headline import headline 
from benefits import benefits
from areyou import areyou
list = [['click here to find out more', '#moreinfo'], ['sign up now', '#signup']]

pronoun = input('our, this, the, my what is the prooun of the product?')
product = input('what is your product?')
achieve = input('what do your customers want to achieve?')
challenge = input('what is their primary challenge?')

benefit  = benefits('0', pronoun, product)
ben1 = benefits('1', pronoun, product)
ben2 = benefits('2', pronoun, product)
ben3 = benefits('3', pronoun, product)
areyou = areyou(achieve, challenge)
selection = int(input('would you like to choose 1 or more sentences?'))
sentences = headline(selection)
print(sentences)
name = product
for x in sentences:
    text_file = open('{}{}.html'.format(name, x), 'w')

    text_file.write(webgen(name, list, x, benefits, ben1, ben2, ben3, areyou))
text_file.close()