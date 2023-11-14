import requests 

response = requests.get('https://quotes.toscrape.com')

print(response.status_code)


with open('cleaned_quotes.txt' ,'w') as file :

    for line in  response.text.split('\n'):
        if '<span class="text" itemprop="text">' in line :

            only_text = line.replace( '<span class="text" itemprop="text">','')
            only_text_only=only_text.replace('</span>','')
            cleaning_apostroph=only_text_only.replace('&#39;',"'")
            cleaned_first_quotation_mark= cleaning_apostroph.replace('”','')
            cleaned_text= cleaned_first_quotation_mark.replace('“','')

            file.write(cleaned_text.strip()) 
            file.write('\n')        
            
with open('cleaned_authors.txt','w')   as f: 
     for line in response.text.split('\n'):
        if '<span>by <small class="author" ' in line :
        
            cleaned_left_place=line.replace('<span>by <small class="author" itemprop="author">','')
            cleaned_right_place=cleaned_left_place.replace('</small>','')
        

            f.write(cleaned_right_place.strip())
            f.write('\n')


            
        


