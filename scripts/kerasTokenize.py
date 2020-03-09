from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
#from keras.utils import to_categorical
from keras.utils.np_utils import to_categorical
import numpy as np


#phrases = ['gemeente TESSENDERLO , vertegenwoordigd', 'TESSENDERLO , vertegenwoordigd door', ', vertegenwoordigd door het', 'vertegenwoordigd door het college', 'door het college van', 'de gemeente TESSENDERLO , vertegenwoordigd', 'gemeente TESSENDERLO , vertegenwoordigd door', 'TESSENDERLO , vertegenwoordigd door het', ', vertegenwoordigd door het college', 'vertegenwoordigd door het college van', 'de gemeente TESSENDERLO , vertegenwoordigd door', 'gemeente TESSENDERLO , vertegenwoordigd door het', 'TESSENDERLO , vertegenwoordigd door het college', ', vertegenwoordigd door het college van', 'de gemeente TESSENDERLO , vertegenwoordigd door het', 'gemeente TESSENDERLO , vertegenwoordigd door het college', 'TESSENDERLO , vertegenwoordigd door het college van', 'de gemeente TESSENDERLO , vertegenwoordigd door het college', 'gemeente TESSENDERLO , vertegenwoordigd door het college van', 'de gemeente TESSENDERLO , vertegenwoordigd door het college van', 'burgemeester en schepenen \n', ' \n', 'verwerende partij \n', ' \n', '\n', ' \n', '\n', ' \n', '\n', ' \n', ' \n', 'In zake: \n', ' \n', ' \n', ' \n', ' \n', ' \n', ' \n', ' \n', ' \n', ' \n', ' \n', ' \n', ' \n', ' \n', ' \n', ' \n', ' \n', '\n', 'I. \n', '\n', 'VOORWERP VAN DE VORDERING \n', '\n', ' \n', 'De vordering ingesteld bij', 'vordering ingesteld bij aangetekende', 'ingesteld bij aangetekende brief', 'bij aangetekende brief van', 'aangetekende brief van 19', 'brief van 19 december', 'van 19 december 2010', '19 december 2010 strekt', 'december 2010 strekt tot', '2010 strekt tot de', 'strekt tot de vernietiging', 'De vordering ingesteld bij aangetekende', 'vordering ingesteld bij aangetekende brief', 'ingesteld bij aangetekende brief van', 'bij aangetekende brief van 19', 'aangetekende brief van 19 december', 'brief van 19 december 2010', 'van 19 december 2010 strekt', '19 december 2010 strekt tot', 'december 2010 strekt tot de', '2010 strekt tot de vernietiging', 'De vordering ingesteld bij aangetekende brief', 'vordering ingesteld bij aangetekende brief van', 'ingesteld bij aangetekende brief van 19', 'bij aangetekende brief van 19 december', 'aangetekende brief van 19 december 2010', 'brief van 19 december 2010 strekt', 'van 19 december 2010 strekt tot', '19 december 2010 strekt tot de', 'december 2010 strekt tot de vernietiging', 'De vordering ingesteld bij aangetekende brief van', 'vordering ingesteld bij aangetekende brief van 19', 'ingesteld bij aangetekende brief van 19 december', 'bij aangetekende brief van 19 december 2010', 'aangetekende brief van 19 december 2010 strekt', 'brief van 19 december 2010 strekt tot', 'van 19 december 2010 strekt tot de', '19 december 2010 strekt tot de vernietiging', 'De vordering ingesteld bij aangetekende brief van 19', 'vordering ingesteld bij aangetekende brief van 19 december', 'ingesteld bij aangetekende brief van 19 december 2010', 'bij aangetekende brief van 19 december 2010 strekt', 'aangetekende brief van 19 december 2010 strekt tot', 'brief van 19 december 2010 strekt tot de', 'van 19 december 2010 strekt tot de vernietiging', 'De vordering ingesteld bij aangetekende brief van 19 december', 'vordering ingesteld bij aangetekende brief van 19 december 2010', 'ingesteld bij aangetekende brief van 19 december 2010 strekt', 'bij aangetekende brief van 19 december 2010 strekt tot', 'aangetekende brief van 19 december 2010 strekt tot de', 'brief van 19 december 2010 strekt tot de vernietiging', 'De vordering ingesteld bij aangetekende brief van 19 december 2010', 'vordering ingesteld bij aangetekende brief van 19 december 2010 strekt', 'ingesteld bij aangetekende brief van 19 december 2010 strekt tot', 'bij aangetekende brief van 19 december 2010 strekt tot de', 'aangetekende brief van 19 december 2010 strekt tot de vernietiging', 'van de beslissing van', 'de beslissing van het', 'beslissing van het college', 'van 'schepenen van de gemeente', 'van de beslissing van het', 'de beslissing van het college', 'beslissing van het college van', 'van het college van burgemeester', 'het college van burgemeester en', 'college van burgemeester en schepenen', 'van burgemeester en schepenen van', 'burgemeester en schepenen van de', 'en schepenen van de gemeente', 'van de beslissing van het college', 'de beslissing van het college van', 'beslissing van het college van burgemeester', 'van het college van burgemeester en', 'het college van burgemeester en schepenen', 'college van burgemeester en schepenen van', 'van burgemeester en schepenen van de', 'burgemeester en schepenen van de gemeente', 'van de beslissing van het college van', 'de beslissing van het college van burgemeester', 'beslissing van het college van burgemeester en', 'van het college van burgemeester en schepenen', 'het college van burgemeester en schepenen van', 'college van burgemeester en schepenen van de', 'van burgemeester en schepenen van de gemeente', 'van de beslissing van het college van burgemeester', 'de beslissing van het college van burgemeester en', 'beslissing van het college van burgemeester en schepenen', 'van het college van burgemeester en schepenen van', 'het college van burgemeester en schepenen van de', 'college van burgemeester en schepenen van de gemeente', 'van de beslissing van het college van burgemeester en', 'de beslissing van het college van burgemeester en schepenen', 'beslissing van het college van burgemeester en schepenen van', 'van het college van burgemeester en schepenen van de', 'het college van burgemeester en schepenen van de gemeente', 'van de beslissing van het college van burgemeester en schepenen', 'de beslissing van het college van burgemeester en schepenen van', 'beslissing van het college van burgemeester en schepenen van de', 'van het college van burgemeester en schepenen van de gemeente', 'Tessenderlo op datum van 7 december 2009. \n', ' \n', ' \n', '\n', 'II. \n', '\n', 'VERLOOP VAN DE RECHTSPLEGING \n', '\n', ' \n', 'Het verzoekschrift van 19', 'verzoekschrift van 19 december', 'van 19 december 2009', '19 december 2009 is', 'december 2009 is op', '2009 is op 23', 'is op 23 december', 'op 23 december 2009', '23 december 2009 ingeschreven', 'december 2009 ingeschreven in', '2009 ingeschreven in het', 'ingeschreven in het register', 'Het verzoekschrift van 19 december', 'verzoekschrift van 19 december 2009', 'van 19 december 2009 is', '19 december 2009 is op', 'december 2009 is op 23', '2009 is op 23 december', 'is op 23 december 2009', 'op 23 december 2009 ingeschreven', '23 december 2009 ingeschreven in', 'december 2009 ingeschreven in het', '2009 ingeschreven in het register', 'Het verzoekschrift van 19 december 2009', 'verzoekschrift van 19 december 2009 is', 'van 19 december 2009 is op', '19 december 2009 is op 23', 'december 2009 is op 23 december', '2009 is op 23 december 2009', 'is op 23 december 2009 ingeschreven', 'op 23 december 2009 ingeschreven in', '23 december 2009 ingeschreven in het', 'december 2009 ingeschreven in het register', 'Het verzoekschrift van 19 december 2009 is', 'verzoekschrift van 19 december 2009 is op', 'van 19 december 2009 is op 23', '19 december 2009 is op 23 december', 'december 2009 is op 23 december 2009', '2009 is op 23 december 2009 ingeschreven', 'is op 23 december 2009 ingeschreven in', 'op 23 december 2009 ingeschreven in het', '23 december 2009 ingeschreven in het register', 'Het verzoekschrift van 19 december 2009 is op', 'verzoekschrift van 19 december 2009 is op 23', 'van 19 december 2009 is op 23 december', '19 december 2009 is op 23 december 2009', 'december 2009 is op 23 december 2009 ingeschreven', '2009 is op 23 december 2009 ingeschreven in', 'is op 23 december 2009 ingeschreven in het', 'op 23 december 2009 ingeschreven in het register', 'Het verzoekschrift van 19 december 2009 is op 23', 'verzoekschrift van 19 december 2009 is op 23 december', 'van 19 december 2009 is op 23 december 2009', '19 december 2009 is op 23 december 2009 ingeschreven', 'december 2009 is op 23 december 2009 ingeschreven in', '2009 is op 23 december 2009 ingeschreven in het', 'is op 23 december 2009 ingeschreven in het register', 'Het verzoekschrift van 19 december 2009 is op 23 december', 'verzoekschrift van 19 december 2009 is op 23 december 2009', 'van 19 december 2009 is op 23 december 2009 ingeschreven', '19 december 2009 is op 23 december 2009 ingeschreven in', 'december 2009 is op 23 december 2009 ingeschreven in het', '2009 is op 23 december 2009 ingeschreven in het register', 'van de Raad. \n', ' \n', 'De voorzitter van de', 'voorzitter van de Raad', 'van de Raad heeft', 'de Raad heeft met', 'Raad heeft met een', 'heeft met een beschikking']
phrases = ['gemeente TESSENDERLO' , 'vertegenwoordigd', 'TESSENDERLO  vertegenwoordigd door', 'vertegenwoordigd door het', 'vertegenwoordigd door het college', 'door het college van']

MAX_NUM_WORDS = 1000
MAX_SEQUENCE_LENGTH = 100
tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
tokenizer.fit_on_texts(phrases)
sequences = tokenizer.texts_to_sequences(phrases)

word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))
print(word_index)


data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

#labels = to_categorical(np.asarray(phrases))
print(data.shape)
#print(labels.shape)