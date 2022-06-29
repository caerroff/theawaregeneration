def addArticle(title:str, content:str, author:str, topic:int):
    retour = ""
    retour+= f"""<div class="article">
    <div class="topic{topic}">
        <h2 class="title">{title}</h2>
        <p class="content">{content}<p>
        <h3 class="author">{author}<h3>
    </div>
</div>"""
    return retour

title = "The Super Article"
content = "This is a really cool article, everyone should read it, it has definitely not been made to test this script and it of course contains a lot of stuff."
author = "me"

print(addArticle(title, content, author, 1))