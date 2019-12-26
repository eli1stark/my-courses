Hello everybody! Today I want to tell you about my project. I'm working on it for approximately a month. First of all, I would like to tell about the idea of project which I named Mobiplay. As a young men, I prefer to play some games on my phone or laptop sometimes but very often I need to play with some random players who can ruin the gaming process and even if the players are good, I can only add them within the game we play, but what if I want to play with them in other games? In this moment things making more complicated. So I decided it would be nice if this world had some kind of social network for gamers, in which people can meet each other based on their interests in several games. I considered implementing this project on the web, using tech stack which I went through CS50 course, namely Python, Flask, Jinja2, Bootstrap, SQLite 3, HTML5, CSS 3 and a little bit of JavaScript. Unfortunately, Mobiplay (website) is suited only for desktops, laptop and tablets, it's optimized very badly for phones. What about the code part?

I divided Mobiplay into 3 parts (static folder, templates, and application.py with other python files). The main technology which makes things works is Flask as I said before. The main page around which Mobiplay was built is chat which gives an opportunity to gamers to interact with each other. Also, users have page named account in which they can enter their personal info, add a profile photo, change their password + page named games, there are games that are available on Mobiplay which users can add to their profiles. What about page profile, gamers can choose their location, first language, second language, the favorite game from added games to profile, status (online, idle or offline). Further, this information will be used on the search page where people can add new friends. All added friends transfer to the page "chat" and the page "mates" (list of added friends). Using this chat I can communicate with my friends but it's only possible chatting with added mates. If I remove some mate I lost chat history with him, and the opportunity to chat, but if I add him again, all is back. All data of the project is stored in SQlite3 on several tables. The main design of the site is built on Bootstrap.

Thanks for reading this, hope you enjoy! It is possible that Mobiplay can be improved by me in the future and became a real social network. Well, let's see!

