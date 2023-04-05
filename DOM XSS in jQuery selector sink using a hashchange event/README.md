# DOM XSS in jQuery selector sink using a hashchange event

In this challenge, we do an XSS attack using vulnerability on hashchange event in jquery.

<div style="margin-top: 10px; margin-bottom: 10px;"
alt="Home">
    <img src="https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20jQuery%20selector%20sink%20using%20a%20hashchange%20event/Home%20page.png/?raw=true">
</div>

<div style="margin-top: 10px; margin-bottom: 10px;"
alt="Home">
    <img src="https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20jQuery%20selector%20sink%20using%20a%20hashchange%20event/jquery%20function.png/?raw=true">
</div>

here we can see that the jquery perform autoscrolling based on **location.hash** value in the url param such as Fake News, Proscatinating, etc. But, instead of set it's value to existing post, we can inject javascript code, let's do it in the reserved exploit server, and make response such like this:

<div style="margin-top: 10px; margin-bottom: 10px;"
alt="Home">
    <img src="https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20jQuery%20selector%20sink%20using%20a%20hashchange%20event/payload.png/?raw=true">
</div>

It will create an iframe from our lab source, and when it's content is loading, we'll add ``<img src=x onerror=print()>`` code in the url. Automatically, the jquery will execute and instead of change our position to available post, it will check an image from unavailable source image and execute print() javascript function.

The result will be like this:
<div style="margin-top: 10px; margin-bottom: 10px;"
alt="Home">
    <img src="https://github.com/DJumanto/Portswigger-XSS/blob/main/DOM%20XSS%20in%20jQuery%20selector%20sink%20using%20a%20hashchange%20event/result.png/?raw=true">
</div>

