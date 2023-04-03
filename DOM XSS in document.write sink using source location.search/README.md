# DOM XSS in document.write sink using source location.search

Now, the challenge is kinda different than the first challenge, when we input tag in the search bar like before ``<b>hello</b>``, nothing will happen

![b-tag input](https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20document.write%20sink%20using%20source%20location.search/b-tag%20input.png?raw=true)

But, let's see the source code

![Source Code Analysis](https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20document.write%20sink%20using%20source%20location.search/Source-Code-analysis.png?raw=true)

In the source code, we can see that the query was passed to the function **trackSearch**, then the function will create a new dom of image while the source of th image is coming from our input

To bypass it, we can add a **">** before the tag. So the payload will look like this:
```html
"><img src='x' onerror=alert("XSS")>
"><svg src='x' onload=alert("XSS")>
"><script>alert("XSS")</script>
">document.write("<script>alert("XSS")</script>");

etc...
```
both will works, let's try with svg tag

![svg input](https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20document.write%20sink%20using%20source%20location.search/svg-tag-input.png?raw=input)

Result

![result](https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20document.write%20sink%20using%20source%20location.search/XSS%20result.png?raw=true)

