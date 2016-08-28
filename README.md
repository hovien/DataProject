# DataProject
This is a school project that aims to analyze interview data using Python for preprocessing and Weka for text mining.
the folders contain linux bash scripts, python code and tools I used that were created by others. All bash scripts are to be run from the main folder, directories are changed automatically by the script. Analysis can only be done on UTF-8 encoded text. Description of the contents of folders:

Tools:
Here are the programs that need to be installed to use my solutions. These programs are not my work and I don't take credit for them, I just have them in one place for convenience. 





English - python code is found here for preprocessing the English text files to be used in Weka. The steps of use are as follows (however, the bash scripts will conduct the same steps except number 1):
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
11) clustering_arff_creator.py will create the ARFF file format for clustering in Weka. Inputs are the stemmed file from step 3) and the attribute list from step 9).

ENG_bash:
- basic_bash_script_ENG: goes through the process described above. First promts for the name of the file to be processed   (assumes it is in the folder data/English), then creates the association rule tester ARFF and the clustering ARFF in the folder data/English/results. The stemmed file is saved in the folder data/English/results/stemmed, the attribute list is saved in data/English/results/attributes.
- bash_adj-noun-assoc_ENG: same as the basic bash script, except it uses nouns and adjectives too for creating the association rule testing file and skips the clusterer creation
- bash_adj-noun-cluster_ENG: this is a clustering file creator that takes the adjectives as attributes and the nouns as instances, so the frequency numbers can be interpreted as "how many times does this adjective occur within 4 words distance of this noun in the stemmed file?"
- bash_noun-attr-all-inst-cluster_ENG: attempts to create a clustering file that has nouns as attributes and all stemmed words as instances, but it doesn't function properly
- bash_verb-cluster_ENG: creates a file for clustering using verbs as attributes and instances
- bash_verb-noun-assoc_ENG: creates an association rule tester file using nouns and verbs as attributes






Finnish - python code is found here for preprocessing the Finnish text files to be used in Weka. The steps of use are similar to the English, with some changes:
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
11) clustering_arff_creator.py will create the ARFF file format for clustering in Weka. Inputs are the stemmed file from step 3) and the attribute list from step 9)

FIN_bash:
- basic_bash_script_FIN: just like the English version, it goes through the process described above. First promts for the name of the file to be processed   (assumes it is in the folder data/Finnish), then creates the association rule tester ARFF and the clustering ARFF in the folder data/Finnish/results. The stemmed file is saved in the folder data/Finnish/results/stemmed, the attribute list is saved in data/Finnish/results/attributes.
- bash_adj-noun-assoc_FIN: same as the basic bash script, except it uses nouns and adjectives too for creating the association rule testing file and skips the clusterer creation
- bash_adj-noun-cluster_FIN: this is a clustering file creator that takes the adjectives as attributes and the nouns as instances, so the frequency numbers can be interpreted as "how many times does this adjective occur within 4 words distance of this noun in the stemmed file?"
- bash_verb-cluster_FIN: creates a file for clustering using verbs as attributes and instances
- bash_verb-noun-assoc_FIN: creates an association rule tester file using nouns and verbs as attributes







freq - this folder has the python and bash code for creating frequency lists.

1) For making the English frequency list, run freq/ENG/freq_bash. It will prompt for the name of the file you want to process (path not needed, only file name). The output files (word frequency and noun frequency list excluding stop words)  will appear in data/English/results/freq (the folders have to exist already).

2) For making the Finnish files, repeat the process with the freq/FIN/freq_bash. The Finnish version doesn't remove the stop words. The output is data/Finnish/results/freq (the folders have to exist already).

3) freq_sums.py in both folders (ENG and FIN) creates a file that contains all words from all input files with their corresponding frequencies as columns next to each other. The inputs are either the word frequencies or the noun frequencies. It is saved as csv file and the format is like this: word, frequency in text A, frequency in text B, etc. I used this file to make visualisations using Tools/raw. The file names are hard coded, no prompting happens, so the python file needs to be changed directly before running. Comments with capital letters inside the file help with it.

4)freq_sums_for_raw.py creates a csv file for raw analysis. In this analysis the top 15 words altogether are listed and their individual frequencies are shown by interview. The columns are: word, frequency, interview number. Inputs and output is to be adjusted just like in the freq_sums.py, they are marked with comments in capital letters. The length of the frequency list can be adjusted too, now it's top 15 words, but it can be a lower or higher number.


