import pandas as pd
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-p", "--path", dest="train_path", help="Path to training data in CSV format from MyVision.ai.")


(options, args) = parser.parse_args()

if not options.train_path:   # if filename is not given
    parser.error('Error: path to training data must be specified. Pass --path to command line')

# Read data
df = pd.read_csv(options.train_path)

# Convert it to teh format required if using the simple option in train_frcnn.py
df2 = df[['filename','xmin','ymin','xmax','ymax','class']]

df2.to_csv("piezas_prueba/train.txt", sep=',', header=None, index=None)
