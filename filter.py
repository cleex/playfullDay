import csv
# awk -F'/' '{ if (length($1)>2) print $1 }' en_US_dict.txt >en_US_dict_gt2.txt
# cat en_US_dict_gt2.txt 20k_and_stopw.txt |sort|uniq >common.txt
# run: python  filter.py  <input_file> <filter_file>

ifn = str(sys.argv[1])
ffn = str(sys.argv[2])

def words(text): return re.findall('[a-z]+', text.lower())

wlist = words(file(ffn).read())
#print(wlist)

ofp = open(ifn + ".filtered.csv" , 'w')
with open(ifn, 'r') as csvfile:
    csvLines = csv.reader(csvfile)
    # csv reader return list of list of columns
    for line in csvLines:
        # remove punctuation and split into seperate words
        w_to_chk = re.findall('[a-z]+', line[1].lower())
        #print(line[0] + ", " + line[1] + ">>>" + " ".join(w_to_chk) )

        # if the list w_to_chk has more than one elem, not to chk; just print
        if len(w_to_chk) > 1:
            ofp.write(line[0] + ", " + line[1] + "\n")
            print(line[0] + ", " + line[1] + " => not filtered: " + " ".join(w_to_chk) )
        # not to print single letter
        elif len(w_to_chk) > 0 and len(w_to_chk[0]) > 1 and ( not w_to_chk[0] in wlist):
            ofp.write(line[0] + ", " + w_to_chk[0] + "\n")
ofp.close()
