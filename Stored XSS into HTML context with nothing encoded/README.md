# Stored XSS into HTML context with nothing encoded

So basically stored XSS is a kind of vulnerability where we able to input evil command/script to a webiste, and beign stored to the database. Everytime the command shows up in the front end (a user open the page that executing our payload), it will be executed.

In this case, the website is a blog site, where we able to read posts and post comments

![home](https://github.com/DJumanto/Portswigger-XSS/blob/main/Stored%20XSS%20into%20HTML%20context%20with%20nothing%20encoded/Home.png?raw=true)

![comment box](https://github.com/DJumanto/Portswigger-XSS/blob/main/Stored%20XSS%20into%20HTML%20context%20with%20nothing%20encoded/Comment%20Box.png?raw=true)

the possible vulnerability is in the comment post form. If we able to input html tag such as ``<h1>``, then we might able to sent a script tage with evil code inside. Let's try with ``<h1>`` tag first

![h1 trial](https://github.com/DJumanto/Portswigger-XSS/blob/main/Stored%20XSS%20into%20HTML%20context%20with%20nothing%20encoded/Comment%20with%20h1-tag%20trial.png?raw=true)

After we sent it, when we back to the comment section, we can see that the command was succesfully injected

![h1 executed](https://github.com/DJumanto/Portswigger-XSS/blob/main/Stored%20XSS%20into%20HTML%20context%20with%20nothing%20encoded/h1-executed.png?raw=true)

Then let's try with ``<script>`` tag

![xss-inserted](https://github.com/DJumanto/Portswigger-XSS/blob/main/Stored%20XSS%20into%20HTML%20context%20with%20nothing%20encoded/input%20xss%20command.png?raw=true)

The result is

![xss-executed](https://github.com/DJumanto/Portswigger-XSS/blob/main/Stored%20XSS%20into%20HTML%20context%20with%20nothing%20encoded/XSS-Executed.png?raw=true)

voila, it works. Now the command we sent to the databse will always be executed everytime someone visit that page, at least until someone sanitize it or delete it manually from the database. 


