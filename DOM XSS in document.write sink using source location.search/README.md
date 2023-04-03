# DOM XSS in document.write sink using source location.search

Now, the challenge is kinda different than the first challenge, when we input tag in the search bar like before ``<b>hello</b>``, nothing will happen



But, let's see the source code


In the source code, we can see that the query was passed to the function **trackSearch**, then the function will create a new dom of image while the source of th eimage is coming from our input



To bypass it, we can add a **">** before the tag. So the payload will look like this:
```html
"><img src='x' onerror=alert("XSS")>
"><svg src='x' onload=alert("XSS")>
"><script>alert("XSS")</script>
">document.write("<script>alert("XSS")</script>");

etc...
```


Result


