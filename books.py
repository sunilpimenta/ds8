from datascience import *
from urllib.request import urlopen
import numpy as np
import matplotlib
#% matplotlib inline

huck_finn_url = 'https://www.inferentialthinking.com/data/huck_finn.txt'
huck_finn_chapters = urlopen(huck_finn_url).read().decode().split('CHAPTER ')[44:]

counts = Table().with_columns([
        'Jim', np.char.count(huck_finn_chapters, 'Jim'),
        'Tom', np.char.count(huck_finn_chapters, 'Tom'),
        'Huck', np.char.count(huck_finn_chapters, 'Huck')
    ])

cum_counts = counts.cumsum().with_column('Chapter', np.arange(1, 44, 1))
cum_counts.plot(column_for_xticks=3)
#plots.title('Cumulative Number of Times Each Name Appears', y=1.08);
