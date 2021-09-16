import fitz
from bs4 import BeautifulSoup
from difflib import Differ
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
from html.entities import html5
# print(html5)
# soup = BeautifulSoup(open('test.html'), 'html.parser')
# new_div = soup.new_tag('div')

# file = fitz.open('data2.pdf') 
# for pageNumber,page in enumerate(file.pages(),start=1):
#     text=page.getText("html")
#     # tfile=file.get_toc()
#     txt_file=open(f'report_1.txt','w+')
#     txt_file.writelines(text)
#     txt_file.close()


file_html = open(r'report_1.txt', 'r+')
file_xml = open(r'data_xml.xml', 'r+')
file_diff = open(r'file_diff.txt', 'w')

soup_text=[[]]
html_text=[]
soup_starting_tags_array=[]
soup_ending_tag=[]
html_span_text=[]
soup_starting_tags_children=[]
with open('report_1.txt','r+') as file:   
    soup = BeautifulSoup(file, 'html.parser')
    # soup_obj=soup.p
    # soup_array=soup_obj.find_next_siblings("p")
    span_text=soup.find_all('span')
    for span in span_text:
        html_text.append(span.text)
    # print(html_text)
    print(len(html_text))
    # soup_text=soup.get_text()
    # lines = (line.strip() for line in soup_text.splitlines())
    # chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # html_text=[chunk for chunk in chunks if chunk]
    # for data in html_text:
        # print(data)
    # print(html_text)
    soup_div=soup.find("div")
    # soup_para=soup_div.find("p")
    # print(soup_para)
    soup_starting_p=soup_div.findChildren("p", recursive=False)
    # soup_starting_tags=soup_starting_p.findChildren("", recursive=False)
    # i=0
    for k in soup_starting_p:
        temp_k=k.findChildren(recursive=False)
        # print(temp_k[i])
        # i=i+1
        for child_temp_k in temp_k:
            soup_starting_tags_children.append(child_temp_k)

    # print(soup_starting_tags_children)
    # a=np.array(soup_starting_tags_children, dtype=object)
    # b=a.ravel()
    # soup_starting_tags_children_final=sum(soup_starting_tags_children, [])
    # print(soup_starting_tags_children_final)
    for temperorary in soup_starting_tags_children:
        temp_k=str(temperorary)
        # print(k)
        clean = re.compile('>.*?<')
        temp_k=re.sub(clean, '><', temp_k)
        # print(temp_k)
        clean = re.compile('</.*?>')
        clean_span=re.compile('<span.*?>')
        temp_k=re.sub(clean_span, '', temp_k)
        # print(temp_k)
        soup_starting_tags_array.append(re.sub(clean, '', temp_k))
        clean = re.compile('<[a-zA-Z].*?>')
        clean_span=re.compile('</span.*?>')
        temp_k=re.sub(clean_span, '', temp_k)
        soup_ending_tag.append(re.sub(clean, '', temp_k))
    # print(temp_k)
    # soup_starting_tags=[str(x) for x in soup_starting_tags]
    # clean = re.compile('>.*?<')
    # print(re.sub(clean, '><', soup_starting_tags))
    # print(soup_ending_tag)
    # print(len(soup_ending_tag))
    # print(len(soup_starting_tags_array))

    # print(soup_starting_tags_array)



with open('data2_xml.xml','r+') as file_xml:   
    soup_xml = BeautifulSoup(file_xml, 'lxml')
    soup_matter=soup_xml.find("rearmatter")
    soup_xml_p=soup_matter.findChildren(["p","ol","li"], recursive=False)
    # print(soup_xml_p)
    # soup_xml_data=soup_xml.find_all(['p','li','ol'], recursive=False)
    soup_xml_data=[str(x) for x in soup_xml_p]
    # print(soup_xml_data)
    # for r in soup_text:
    #     for c in r:
    #         print(c,end = " ")
    #         print()
    # print(soup_text[])
    # print(soup_array)
    # print(soup_array[0].get_text())
    # print(soup_array[0].contents[0])
    # for child in soup_obj.descendants:
    #     # print(child)
    #     store_child=[]
    #     store_child.append(child)
    


# with open('data_xml.xml','r+') as file_xml:   
#     # for line in file: 
#     soup_xml = BeautifulSoup(file_xml, 'lxml')
#     soup_xml_obj=soup_xml.p
    # print(soup_xml_obj.find_next_siblings("p"))





tree = ET.parse('data_xml.xml')
root = tree.getroot() 
# print("From XML file : "+root[0].text)  
# print(root.tag)

# a,b = re.search(store_child[-1], root[0].text).span()
# print(f'position of \'my\': [{a}:{b}]\n')

# with open ('data_xml.xml', 'w+' ) as f:
#     clean = re.compile(store_child[-1])
#     text = f.read()
#     # a,b = re.search(store_child[-1], text).span()
#     # print(f'position of \'my\': [{a}:{b}]\n')
#     text_sub=ET.fromstring(re.sub(clean, store_child[0], text))
#     f.write(text)
#     print(text_sub)





# for child in root:
#     print(child.tag, child.attrib)

# def prettify(elem):
#     rs = ET.tostring(elem,encoding='utf-8')
#     rp = minidom.parseString(rs)
#     return rp.toprettyxml(indent="  ")


# for rank in root.iter('p'):
#     b = ET.SubElement(rank, 'b')
#     new_rank = prettify(soup_array[0].contents[0])
#     rank.text = new_rank
#     rank.set('style', 'yes')

# tree.write('output.xml')





    # for element in soup_obj[0].findChildren('b'):
    #     print(element)

    # print(soup_obj.find_next_siblings("p"))

    # print(soup)

        # clean = re.compile('>.*?<')
        # print(re.sub(clean, '><', line))



# lookup="CHIMNEYS AND VENTS"
# for num, line in enumerate(file_xml, 1):
#         # if lookup in line:
#         # print('found at line:', num)
#         clean = re.compile('<.*?>')
        # print(re.search(clean,line))
        # for next_word in line:
            






# file_new.re.search("CHIMNEYS AND VENTS")



# for line in file_new:
#     if line.strip() not in old_lines:
#         file_diff.write(line)
# file_new.close()
# file_diff.close()



# differ = Differ()
# for line in file_new:
#     if line.strip() not in old_lines:
#         file_diff.write(line)
# file_new.close()
# file_diff.close()


# new_div=text
# soup.body.append(new_div)   
# with open("test.html", "w") as file:
#     file.write(str(soup))


# old_lines = open(r'report_1.txt', 'r+')
# for line in differ.compare(old_lines.readlines(), file_new.readlines()):
#         print(line)



def computeLPSArray(pat, M, lps):
    len = 0 
    lps[0] = 0
    i = 1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1

def run_kmp(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    j = 0 
    computeLPSArray(pat, M, lps)
    i = 0 
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            return i - j
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1

# html = ["Hi", "Shree", "Hi"]
# starting_tags = ["<span> <b>", "<span> <b>", "<span>"]
# ending_tags = ["</b> </span>", "</b> </span>", "</span>"]
# xml = ["<p>Hi Shree</p>", "<p>Hi</p>"]

n = len(html_text)
m = len(soup_xml_data)

# traverse needed html indices for each xml index

i = int(0)  # index for html track

new_xml = []

# print (html_text[1])

html_text_main = []
for x in html_text:
    html_text_main.append(x)

for data in soup_xml_data:
    ndata = ""
    for ii in range(len(data)):
        if data[ii] == '\n' or data[ii] == '\t':
            ndata += ' '
        else: 
            ndata += data[ii]
    data = ndata
    ndata = ""
    for ii in range(len(data)):
        if data[ii] == ' ':
            if len(ndata) == 0 or ndata[-1] != ' ':
                # print(ii)
                ndata += ' '
            continue
        ndata += data[ii]
    data = ndata
    pos = int (0)  # index till traversal
    # print(data)
    start = []
    end = []
    temp_starting_tags = []
    temp_ending_tags = []
    for ii in range(len(data)):
        start.append(0)
        end.append(0)
        temp_ending_tags.append("")
        temp_starting_tags.append("")
    tries=10
    # print (data)
    # html_text_old = html_text
    # print(html_text[1])
    # print(html_text_old[])

    changed = []
    err = -1

    while i < len (html_text):
        pattern = html_text[i]
        if pattern[-1] == '-' or pattern[-1]=='.':
            pattern = pattern[:-1]
        text = ""
        for ii in range(pos, min(len(pattern) + 500 + pos, len(data))):
            text += data[ii]
        # print(pattern)
        # print(text)
        # if data == '<p>\\nCHIMNEYS AND VENTS</p>':
        #     print (pattern, text)
        index_found = run_kmp(pattern, text)
        if index_found == -1:
            if tries!=0 and len(html_text[i])>1:
                changed.append(i)
                html_text[i]=html_text[i][1:]
                tries-=1
                continue
            err = i
            print ("--> Error at index ", i, "in HTML Array")
            break
        else:
            print (pattern)
            start[index_found + pos] = 1
            # print (index_found + pos)
            # print (pos + index_found + len(pattern) - 1)
            end[pos + index_found + len(pattern) - 1] = 1
            temp_starting_tags[index_found + pos] = soup_starting_tags_array[i]
            temp_ending_tags[pos + index_found + len(pattern) - 1] = soup_ending_tag[i]
            pos = index_found + pos + len(pattern)
        i += 1

    # print(html_text_old[1])
    # html_text = html_text_old
    # print(html_text[1])

    for x in changed:
        html_text[x] = html_text_main[x]
    if err != -1:
        print ("** Error Text: ", html_text[err], '\n')
    new_data = ""
    for ii in range(len(data)):
        if start[ii] == 1:
            new_data += temp_starting_tags[ii]
        new_data += data[ii]
        if end[ii] == 1:
            new_data += temp_ending_tags[ii]
    new_xml.append(new_data)


with open ('output.xml', 'w+' ) as f:
    f.write('<rearmatter>')
    f.write("\n")
    for data in new_xml:
        f.write(data)
        f.write("\n")
        # print (data)
    f.write('</rearmatter>')
