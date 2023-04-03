# Reflected XSS into HTML context with nothing encoded

In this challenge, there's a search bar. This app will return us back contents we've input before.

![result](https://github.com/DJumanto/Portswigger-XSS/blob/main/Reflected%20XSS%20into%20HTML%20context%20with%20nothing%20encoded/Result.png?raw=true)

Let's try using b-tag ``<b>``

![result b-tag](https://github.com/DJumanto/Portswigger-XSS/blob/main/Reflected%20XSS%20into%20HTML%20context%20with%20nothing%20encoded/Result%20b-tag.png?raw=true)

Well, it seems they don;t filter our input, so let's just inject our payload: 
```html
<script>alert()</script>
```
![inject script-tag](https://github.com/DJumanto/Portswigger-XSS/blob/main/Reflected%20XSS%20into%20HTML%20context%20with%20nothing%20encoded/inject%20with%20script-tag.png?raw=true)

Result:

![XSS Result](https://github.com/DJumanto/Portswigger-XSS/blob/main/Reflected%20XSS%20into%20HTML%20context%20with%20nothing%20encoded/xss%20result.png?raw=true)

if we able to insert script tag, then attacker could inject command like XmlHTTPRequest to send user data to attacker.

