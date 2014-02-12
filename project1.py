import os

dict = {}
found={}

#retrieves the terms in the corpus along with the number of documents the terms appear in
# and places them in the dictionary "dict"
for a in os.listdir("corpus"):
    f = open("corpus/"+a)
    y = a.split(".")
    y=y[0]
    
    for b in f:
         c=b.strip(" ").split()
         if len(c)>0 and c[0] in dict:
             list = found[c[0]].split()
             if  y not in list:
                dict[c[0]]=dict[c[0]]+1
                found[c[0]] = found[c[0]]+" "+str(y)
         elif len(c)>0 and c[0] not in dict:
            found[c[0]]=str(y)
            dict[c[0]]=1

         
             
#places the content of the dictionary in a file
g= open("Dictionary.txt","w")
for k,v in sorted(dict.items()):
    g.write(str(k)+" : "+ str(v)+"\n")

g.close()


#opens the dictionary.txt and retrieves the terms and then constructs a postings list for each term in the
#dictionary
h = open("Dictionary.txt","r")
list = open("PostingsList.txt","a")
for j in h:
    terms_dict={}
    count=0
    terms = j.split(":")
    for l in os.listdir("corpus"):
        count = l.split(".")
        count = count[0]
        f = open("corpus/"+l)
        for z in f:
           m = z.split()
           if len(m)>0:
                terms[0]=terms[0].strip(" ")
                m[0]=m[0].strip(" ")
                if  int(count) not in terms_dict and m[0]==terms[0]:
                    terms_dict[int(count)] = int(m[1])
                elif len(m)>0 and int(count) in terms_dict and m[0]==terms[0]:
                    terms_dict[int(count)] = terms_dict[int(count)] + int(m[1])

     
    list.write(terms[0]+" - ")             
    counter=0
    print(len(terms_dict)== int(terms[1]))
    for y,z in sorted(terms_dict.items()):
         counter+=1
         if counter==len(sorted(terms_dict)):
            list.write("("+str(y)+"|"+ str(z)+") ")
         else:
            list.write("("+str(y)+"|"+ str(z)+"), ")

    list.write("\n")
    
     
    
list.close()
