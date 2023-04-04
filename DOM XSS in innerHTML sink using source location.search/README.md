# DOM XSS in innerHTML sink using source location.search

In this challenge, we need to perform an XSS attack when the code is applying **innerHTML** sink to show up user input query.

if we attempt using ``<b>`` tag in the text-area the result will be like this:
<div style="text-align: center;margin-bottom:10px;margin-top:10px;">
    <img src="https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20innerHTML%20sink%20using%20source%20location.search/b-tag%20result.png?raw=true">
</div>

Does it mean we able to inject ``<script>`` tag in the query? let's try it out
```html
<script>alert()</script>
```
<div style="text-align: center;margin-bottom:10px;margin-top:10px;">
    <img src="https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20innerHTML%20sink%20using%20source%20location.search/script-tag%20attempt.png?raw=true">
</div>

well it doesn't work, let's see the source code

<div style="text-align: center;margin-bottom:10px;margin-top:10px;">
    <img src="https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20innerHTML%20sink%20using%20source%20location.search/js-function.png?raw=true">
</div>

Well, the code tell us that it will insert our query to innerHTML of an element with id **searchMessage**, and insert the result inside a span tag. Maybe you think that we able to add the close ``</span>`` tags before inject our main payload, so our paylaod might be like this: 
```html
</span><script>alert()</script>
```
Yet, it still doesn't work, because however **innerHTML** sink will refuse all ``<script>`` tags in most modern website. So the solution is using another tags such ``<img>`` tags
```html
<img src=x onerror='alert("xss with image tag")'>
```
<div style="text-align: center;margin-bottom:10px;margin-top:10px;">
    <img src="https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20innerHTML%20sink%20using%20source%20location.search/img-tag%20trial.png?raw=true">
</div>

The Result will be like this:

<div style="text-align: center;margin-bottom:10px;margin-top:10px;">
    <img src="https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20innerHTML%20sink%20using%20source%20location.search/result.png?raw=true">
</div>





