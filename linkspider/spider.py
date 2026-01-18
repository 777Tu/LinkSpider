import requests as re
from urllib.parse import urlparse


class Spider:
    def __init__(self, RawUrl):
        self.RawUrl = RawUrl
        self.Visited = set()
        self.queue = [RawUrl]
        
    def HtmlFile(self, PUrl):
        try:
            Ftch = re.get(PUrl, timeout = 5)
            if Ftch.status_code == 200:
                return Ftch.text
            return ""
        except:
            return ""
            
    def LinkSearcher(self, FHtml):
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
    
    def UrlPBPaths(self, Urlpaths):
            Paths = urlparse(Urlpaths)
            PBPaths: list=[]
            parseMtds = Paths.scheme
            if Paths.scheme and Paths.netloc:
                if Paths.netloc:
                    parseMtds += "://" + Paths.netloc
                    PBPaths.append(parseMtds)    
                if Paths.path:
                    parseMtds  +=Paths.path
                    PBPaths.append(parseMtds)
                if Paths.params:
                    parseMtds += Paths.params
                    PBPaths.append(parseMtds)
                if Paths.query:
                    parseMtds +="?"+Paths.query
                    PBPaths.append(parseMtds)
                if Paths.fragment:
                    parseMtds +="#"+Paths.fragment
                    PBPaths.append(parseMtds)
            else:
                 PBPaths =[Urlpaths]
            return PBPaths
           
        
    def SpiderCrawl(self, MxCrawl=10_000_000):
        while self.queue and len(self.Visited) <=MxCrawl:
              CurrLink = self.queue.pop(0)
              if CurrLink in self.Visited:
                  continue
              print(f"SPIDER CRAWLING: {CurrLink}")
              PHtml = self.HtmlFile(CurrLink)
              self.Visited.add(CurrLink)
              for LOPLinks in self.LinkSearcher(PHtml):
                  for LList in self.UrlPBPaths(LOPLinks):
                      if LList not in self.Visited:
                          self.queue.append(LList)
                          print(f"FOUND: {LList}")
                  
                     
                  


if __name__== "__main__":
    LinkList = [
    "https://github.com/dashboard",
    "https://stackoverflow.com/questions",
    "https://www.wikipedia.org/",
    "https://www.google.com/search?q=hello+world&oq=hello+world+&gs_lcrp=EgZjaHJvbWUqCggAEAAYsQMYgAQyCggAEAAYsQMYgAQyBwgBEC4YgAQyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEAAYgAQyBwgHEAAYgAQyBwgIEC4YgAQyBwgJEAAYgAQyBwgKEAAYgAQyBwgLEAAYgAQyBwgMEAAYgAQyBwgNEAAYgAQyBwgOEAAYgATSAQg3OTg2ajBqNKgCDrACAfEFiaIjKWAsAlM&client=ms-android-transsion&sourceid=chrome-mobile&ie=UTF-8"]
    
    for links in LinkList:
        spider = Spider(links)
        spider.SpiderCrawl(MxCrawl=5)
        #spider.SpiderCrawl(MxCrawl=20)            
