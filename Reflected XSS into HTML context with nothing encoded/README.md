# Reflected XSS into HTML context with nothing encoded

In this challenge, there's a search bar. This app will return us back contents we've input before.

Let's try using b-tag ``<b>``

Well, it seems they don;t filter our input, so let's just inject our payload: 
```html
<script>alert()</script>
```

Result:
