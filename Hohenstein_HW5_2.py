#Tyler Hohenstein HW5.2
accession = []
seqList = []
seq = ""
accessionNumList = []
seqLengthList = []
gcList = []

fileName = input("Enter fasta file name and path:  ")
#C:/Users/Tyler/Desktop/Graduate School/VCU/BNFO 600/Python/5.2_SampleData.fasta

infile = open(fileName, "r")
for line in infile:
    print(line)
    if line[0] == ">":
        if seq != "":
            seqList.append(seq)
        seq = ""
        filestr = line
        accession.append(filestr)
    else:
        seqLine = line
        seq += seqLine
seqList.append(seq)
infile.close()

for i in range(0, len(accession)):
    accessionSplit = accession[i].split(sep = '|')
    accessionNum = accessionSplit[3]
    accessionNumList.append(accessionNum)

for i in range(0, len(seqList)):
    seqLength = len(seqList[i])
    seqLengthList.append(seqLength)

for i in range(0, len(seqList)):
    gc = 0
    for j in seqList[i]:
        if j == "G" or j == "C":
            gc += 1
    gcContent = gc / len(seqList[i]) * 100
    gcList.append(gcContent)

print("\n\n\nAccession-Number", "      Sequence-Length", "     GC-Content (%)")
for i in range(0, len(accession)):
    print(format(accessionNumList[i], "<22s"), format(seqLengthList[i], "<20d")\
          , format(gcList[i], "<.4f"))
        
numSeq = len(seqList)
print("\nTotal number of sequences: ", numSeq)

avgLength = sum(seqLengthList) / len(seqList)
print("\nAverage sequence length: ", format(avgLength, ".4f"))

avgGC = sum(gcList) / len(gcList)
print("\nAverage GC content (%): ", format(avgGC, ".4f"))

        
