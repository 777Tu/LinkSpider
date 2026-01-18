from urllib.parse import urlparse 

def UrlPBPaths(Urlpaths):
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
                    parseMtds +="#"+ Paths.fragment
                    PBPaths.append(parseMtds)
            else:
                 PBPaths =[Urlpaths]
            return PBPaths
for i in UrlPBPaths("https://user:pass@example.com/path?query#frag"):
    print(i)            
