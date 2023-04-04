# DOM XSS in jQuery anchor href attribute sink using location.search source
So here, we have feedback form where we able to submit form, going back to home, etc.

<div style="text-align: center; margin-top: 10px">
    <img src="https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20jQuery%20anchor%20href%20attribute%20sink%20using%20location.search%20source/submit-feedback-page.png?raw=true" alt="submit form page">
</div>

The vulnerability is in the href attribute. If you look closely in the url params <span style="color:green;">**returnPath**</span>, it will return to a spesific page.

<div style="text-align: center; margin-top: 10px">
    <img src="https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20jQuery%20anchor%20href%20attribute%20sink%20using%20location.search%20source/Attack-target.png?raw=true" alt="submit form page">
</div>

the jquery function will set the **href** of back button target based on url <span style="color:green;">**returnPath**</span> value. So, instead of redirect it to a **/post or /**, we can set it to execute javascript code <span style="color:yellow;"><b>
javascript:alert()</b></span>. The payload going to be like this:
```html
https://example.com/feedback?returnPath=javascript:alert()
```
Therefore, the href tag target will be like this:
<div style="text-align: center; margin-top: 10px">
    <img src="https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20jQuery%20anchor%20href%20attribute%20sink%20using%20location.search%20source/payload-insert.png?raw=true" alt="submit form page">
</div>
If we click the back button, it will execute the arbitary javascript code
<div style="text-align: center; margin-top: 10px">
    <img src="https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20jQuery%20anchor%20href%20attribute%20sink%20using%20location.search%20source/Result.png?raw=true" alt="submit form page">
</div>

