
# python3 create_ngrams.py
R --slave --no-save --vanilla < som.R

timestamp=$(date '+%Y%m%d')
mv -v Rplots.pdf output_data/Rplots_${timestamp}.pdf
