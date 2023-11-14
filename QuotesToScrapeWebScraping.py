import requests 


unwanted_chars=['“','>','”','<”','”']

def scraping_specific_area(desired_file,appending_writing,class_name):
    with open(desired_file,appending_writing,encoding='utf-8')   as f: 
        for line in response.text.split('\n'):
            if f'class="{class_name}" ' in line :
                line.strip()
                new_line=line.split(f'itemprop="{class_name}"')[1]
                remove_html=new_line.split('<')[0]
                for char in unwanted_chars :
                    if char in remove_html :
                        almost_cleaned_line  = remove_html.replace(char,'')
                finally_cleaned_line = almost_cleaned_line.replace('>“','')
                cleaned_line= finally_cleaned_line.replace('&#39;','')
                f.write(cleaned_line)
                f.write('\n')





for i in range(1,11) :
    response = requests.get(f'https://quotes.toscrape.com/page/{i}/')
    print(response.status_code)
    scraping_specific_area('cleaned_quotes.txt','a','text')
    scraping_specific_area('cleaned_authors.txt','a','author')


    


            


