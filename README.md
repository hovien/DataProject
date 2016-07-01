# DataProject
This is a school project that aims to analyze interview data using Python for preprocessing and Weka for text mining.
The processing flow is as follows:

ENGLISH TEXT:
1) converting rtf into utf-8 text format
2) preproc_India.py will preprocess the text file
3) english_stemmer.py will stem the preprocessed text
4) using linux command to make a word frequency list: tr ' ' '\n' < stemmed_file_name | sort | uniq -c > output_file_name
5) wordfreq_sorter.py will sort the frequency list starting with the most frequent
6) using the word frequency list to extend the stopword list and repeat step 2) and 3)
7) using stanford POS tagger tagging the original text file
8) nounfreq.py will make a noun frequncy list from the tagged text
9) attribute_lister.py will make an attribute list for the association rule data file 
10) arff_transformer_with_attributes_list.py will create the ARFF file format for association rule finding in Weka. Inputs are the attribute list file from step 9) and the preprocessed, stemmed file from step 3)

FINNISH TEXT:
1) converting rtf into utf-8 text format
2) preproc_Finland.py will preprocess the text file
3) finnish_stemmer.py will stem the preprocessed text
4) using linux command to make a word frequency list: tr ' ' '\n' < stemmed_file_name | sort | uniq -c > output_file_name
5) using the word frequency list to extend the stopword list and repeat step 2) and 3)
6) Finntagger_preproc.py will preprocess the original text file for the Finnish POS tagger
7) FinnTreeBank tagger is used to tag the text preprocessed for tagging
8) Finnish_nounfreq.py will extract the stemmed nouns from the tagged text file and calculate frequencies
9) Finnish_attr_lister.py will create the attribute list for the association rule data file
10) arff_transformer_with_attributes_list.py will create the ARFF file format for association rule finding in Weka. Inputs are the attribute list file from step 9) and the preprocessed, stemmed file from step 3)

