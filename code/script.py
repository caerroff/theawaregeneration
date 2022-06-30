class Article:
    def __init__(self, title, content, author, topic):
        self.codeHomePage = self.createArticleHomePage(title, content, author, topic)
        self.codeArticle = self.createArticleCode(title, content, author)
        self.createArticlePage()


    def createArticleHomePage(self,title:str, content:str, author:str, topic:int):
        retour = ""
        retour+= f"""       <a href="articles/article-1.html">
            <div class="article">
                <div class="topic{topic}">
                    <h2 class="title">{title}</h2>
                    <p class="content">{content}<p>
                    <h3 class="author">- {author}<h3>
                </div>
            </div>
        </a>"""
        return retour

    def createArticleCode(self, title:str, content:str, author:str):
        retour = ""
        newContent = ""
        for i in content:
            if "\n" in i:
                newContent += i+"<br>"
            else:
                newContent += i
        retour += f"""      <h1>{title}</h1>
       <p>{newContent}</p>
       <h3>{author}<p>
        
        """
        return retour

    def createArticlePage(self):
        newPage = open("article.html", "w")
        code = ""
        skeleton = open("articleSkeleton.html", "r")
        for i in skeleton:
            if "<!--Start-->" not in i:
                code += i
            else:
                code += self.codeArticle
        
        newPage.write(code)

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
                newCode += self.codeHomePage
                newCode += """
"""
            newCode += i
            count2+=1
        newHtml.write(newCode)
        newHtml.close()
        
        final = open(f"../{nameOfIndex}", "w")
        final.write(newCode)
            


title = "Feminism and what it means to us"
content = """There are many topics and issues close to our heart, and we'll get to all of them, but launching this during Women's History Month, we decided to start it off with feminism.




There are many misconceptions and untrue stereotypes about what feminism is and what feminists are like, but these are important to debunk. The Merriam-Webster dictionary defines feminism as “belief in and advocacy of the political, economic, and social equality of the sexes expressed especially through organized activity on behalf of women's rights and interests”. To put it simply, feminists believe that women and men are equal. Equal, not the same as many like to misinterpret it, but equal. This also includes gender-nonconforming and genderfluid folks as well as trans people.

            The difference in treatment, salary, representation and, in cases, rights changes from country to country, from community to community, but full equality hasn’t yet been achieved. You might notice the differences in healthcare, housing, abuse, education, and many other places. Therefore, we believe that feminism is a super important topic to talk and educate about as well as becoming active change-makers.

            I’ve been brought up in a family where my parents share household chores, both of them work and they treated me as equal to my brothers. This is what I’ve seen my whole life and what I deem normal, however not every place and not every person is like that. Listening to the stereotypes my grandmas still have, watching documentaries about women being harassed, treated as second class citizens, and seeing all the stories just in Hungary alone gives me a reality check and inspires me to work on a better future for all women. (Anna)

Feminism means a lot to me. I started feeling and thinking like a feminist even when I didn’t know that there’s a movement that focus on that. It all started with little things like getting frustrated when boys were asked to carry the chairs in school, or when someone said I was sitting like a boy. I, a little girl, thought to myself: “Why am I treated differenty than boys?” The anger grew as I became older. I saw men, some of them being my relatives, being sexist towards women, not doing the chores at home, telling sexist jokes and being offended when a woman rejects them. I started to do research and learnt that women get paid less and that they’re less likely to get hired due to the fact that they could get pregnant in the future; I learnt that women are more frequent victims of abuse and sexual harassment; I learnt that women are still seen as objects and beautiful throphies for men. But I am so much more than that. We are so much more than that. We are intelligent, curious, imaginative, strong, independent and just as great as men are. My belief is that to prove this to the rest of the world, we must embrace the sisterhood and loudly share our voices. Will you join us on this hard yet amazing journey? (Gabrielė)

"""
author = "Gabrielė Petruokaitė"

#print(createArticle(title, content, author, 1))

myArticle = Article(title, content, author, 3)
myArticle.addToHTML("index.html")