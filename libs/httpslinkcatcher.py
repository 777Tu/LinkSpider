def LinkSearcher(FHtml):
        custHtml = " ".join(FHtml.split())
        startZero: int = 0;FDDLinks: list = []
        
        while True:
            FBHttp = custHtml.find("https://", startZero)
            if FBHttp == -1:
                break
            FDTag = custHtml.find(">", FBHttp)
            FDSpace = custHtml.find(" ", FBHttp)
            FDDQuote = custHtml.find('"', FBHttp)
            FDSQuote = custHtml.find("'", FBHttp)
            FDBSlashe = custHtml.find("\\", FBHttp)
            FDAnd = custHtml.find("&", FBHttp)
            
            FDChar = min([FDIdx for FDIdx in [FDTag,FDSpace, FDDQuote,FDSQuote,FDBSlashe,FDAnd] if FDIdx != -1])
            if FDChar:
                FDDUrl = custHtml[FBHttp: FDChar]
            else:
                FDDUrl = custHtml[FBHttp:]
        
            FDDLinks.append(FDDUrl)
            startZero = FDChar +1
        return FDDLinks

if __name__ == "__main__":
    htmlfile =  """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Ultimate Link Trap</title>
</head>
<body>

    <h1>Oya, Track Me If You Can!</h1>

    <p>Check out the <a href="https://www.google.com">Search Giant</a>.</p>

    <nav>
        <a href="/about-us">About</a>
        <a href="contact.html">Contact</a>
    </nav>

    <div id="crazy-links">
        <a 
            HREF  =   "https://vimeo.com/trending" 
            target="_blank">
            Vimeo (with space)
        </a>
        
        <a href='http://github.com/trending' title="Dev Tools">Github (Single Quotes)</a>
    </div>

    <button onclick="window.location.href='https://www.reactjs.org'">React Docs</button>
    
    <span data-url="https://www.tesla.com">This looks like text but get URL for body</span>

    <footer>
        <p>Follow us for more: <a href="https://twitter.com/ai_expert">Twitter/X</a></p>
        <p>Back to top: <a href="#top">Anchor link (Not external!)</a></p>
    </footer>

</body>
</html>

"""
    for links in LinkSearcher(htmlfile):
        print(links)                
