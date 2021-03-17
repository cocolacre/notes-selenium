#http://suninjuly.github.io/blog_example.html

selector1 = "#post2 .title" #whitespace here means we need one of the descendant element
selector2 = "#posts .title" #all posts' child elements with class "title"
selector3 = "#post2.title" #child element of post2 of class "title"
selector4 = "#post2 > div.title" #child of post2 of class title with tag "div"
selector5 = "#post2 div.title" #any descendant div.title
selector6 = "#post2>div.title" #same as selector4 