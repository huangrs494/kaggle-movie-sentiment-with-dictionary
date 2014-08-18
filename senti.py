from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#from senti_classifier import senti_classifier
def run(instance) :
	#sentences = ['The movie was the worst movie', 'It was the worst acting by the actors']
	#pos_score, neg_score = senti_classifier.polarity_scores(sentences)
	#print pos_score, neg_score
	sf = open('senti_dict')
	sl = sf.readlines()
	senti = {}
	for s in sl :
		sp = s.split('\t')
		senti[sp[0].strip()] = float(sp[1].strip())
	#print(senti) 
	in_file ='train.tsv'
	f = open(in_file)
	lines = f.readlines()
	X = []
	Y = []
	head = 'true'
	output = open('./output-test.csv', 'w')
	output.write("PhraseId")
	output.write(",")
	output.write("Sentiment")
	output.write("\n")
	n_match = 0
	for line in lines :
	
	  if(head=='true') :
		head = 'false'
	  else :
		l = line.strip().split('\t')
		score = 0
		if(len(l)>2) :
			score = getsentiment(senti,l[2])

		#print('\n'+l[2]+'='+str(score))	
		output.write(l[0])
		output.write(",")
		#output.write(l[1])
		#output.write("\t")
		if(len(l)>2) :
			output.write(l[2])
			output.write(",")
	
		output.write(str(score))
		output.write("$")
		ss =2
		if(score<0):
			if(score<-3) :		
				ss = 0
			else :
				ss = 1
		elif(score==0) :
			ss = 2
		else :
			if(score>3) :		
				ss = 4
			else :
				ss = 3
		if(in_file == 'train.tsv') :
			if(str(ss) == l[3]) :
				n_match += 1
			output.write(l[3])
			output.write('#')
		output.write(str(ss))
		output.write("\n")

	#	output.write(l[2])
	#	output.write("\t")
	#	output.write(score)		
	#	output.write("\n")

	#for val in range(len(t_x)):
	#	output.write(t_x[val])
	#	output.write("\t")
	#	output.write(clf.predict(t_x_t[val]))		
	#	output.write("\n")		
	output.close()
	print(float(n_match)/float((len(lines)-1)))
	print('==========END============')

def getsentiment(senti, line) :
	score = 0.0
	words = line.rsplit(' ')
	last_word =''
	for word in words :	
		if(word in senti) :
			score += float(senti[word])
					
	score = score/len(words)
	return score		
instance =50
run(instance)



