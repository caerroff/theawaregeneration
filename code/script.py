class Article:
    def __init__(self, title, content, author, topic):
        self.code = self.createArticle(title, content, author, topic)



    def createArticle(self,title:str, content:str, author:str, topic:int):
        retour = ""
        retour+= f"""       <div class="article">
            <div class="topic{topic}">
                <h2 class="title">{title}</h2>
                <p class="content">{content}<p>
                <h3 class="author">{author}<h3>
            </div>
        </div>"""
        return retour

    def addToHTML(self,nameOfIndex:str):
        html = open(f"../{nameOfIndex}", "r")
        count = 1
        for i in html:
            if "<!--Here-->" in i:
                print(count)
                break
            count += 1
        newHtml = open("newindex.html", "w")
        newCode = ""
        count2 = 1
        html = open(f"../{nameOfIndex}", "r")
        for i in html:
            print(i)
            if count2 == count+1:
                newCode += self.code
                newCode += """
"""
            newCode += i
            count2+=1
        newHtml.write(newCode)
        newHtml.close()
        if str(input("type y if it seems okay\n")) == "y":
            final = open(f"../{nameOfIndex}", "w")
            final.write(newCode)
            


title = "Coucou kerrouche"
content = "This is a really cool article, everyone should read it, it has definitely not been made to test this script and it of course contains a lot of stuff."
author = "Hahaha"

#print(createArticle(title, content, author, 1))

myArticle = Article(title, content, author, 3)
myArticle.addToHTML("index.html")