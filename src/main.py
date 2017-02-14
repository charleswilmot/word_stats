from pylab import *
from string import *
from collections import Counter, OrderedDict
import powerlaw as pl
import ipdb

main_data_file = 'test3.txt'
new_data_file = main_data_file[:-4] + '_pp.txt'

with open(main_data_file, "rt") as fin:
    with open(new_data_file, "wt") as fout:
        for line in fin:
            
            new_line = line.replace('a', 'a')
            new_line = new_line.replace('?', '')
            new_line = new_line.replace('!', '')
            
            fout.write(new_line)

# characters stuff
print 'Working on the characters stuff...'
with open(new_data_file) as fin:
    charcount =  Counter(letter for line in fin 
                  for letter in line.lower() if letter in lowercase)
                  
figure(1)
char_freqs = OrderedDict(sorted(charcount.items(), key=lambda t: -t[1])) # t[0] sorts by key; t[1] by value
plot(char_freqs.values())
yscale('log')
xticks(np.arange(len(char_freqs.keys())), char_freqs.keys())
xlabel('# Letters')
ylabel('Frequency')

pl_fit = pl.Fit(char_freqs.values(), discrete=True)
c_alpha = pl_fit.alpha
pl.plot_pdf(char_freqs.values())
print 'c_alpha = ', c_alpha

# words stuff
print 'Working on the words stuff...'
with open(new_data_file) as fin:  
    wordcount = Counter(fin.read().split())
				
figure(2)					              
word_freqs = np.array(wordcount.values())
hist(word_freqs, bins=10 ** np.linspace(\
             np.log10(word_freqs.min()), np.log10(word_freqs.max()),100))
xscale('log')
yscale('log')
xlabel('# Words')
ylabel('Frequency')

pl_fit = pl.Fit(word_freqs, discrete=True)
w_alpha = pl_fit.alpha
pl.plot_pdf(word_freqs)
print 'w_alpha = ', w_alpha
 
show()
