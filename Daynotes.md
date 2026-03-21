## March 2026

### March 1
- Welcome to the first day of meteorological spring!

## February 2026

### February 28
- The finance addition to the Pixel At-A-Glance widget is now available on my phone. It displays the top movers of my watch list and I wish it had more customization options. I would prefer to always display specific items to which I have the most shares in my portfolio.
- Decided to move the links to other sites to the top of this outline for faster access.

### February 26
- Google is starting to roll out <a href="https://9to5google.com/2026/02/25/pixel-at-a-glance-sports-finance/">the Sports and Finance customizations to the Pixel At A Glance widget</a>. I have the Sports setting on my Pixel 10 but the Finance setting has not yet appeared.

### February 23
- Dave posted on micro.blog about posting to micro.blog from Drummer, and I added to <a href="https://lillihub.com/timeline/84808535#84808535">the thread</a> my experience of a lag between the ping and the post that Anton stated he also experiences. It has Manton's attention.
- Yesterday I successfully tested HTTP network access to Feedland after receiving instruction on <a href="https://oldschool.scripting.com/frank.mcpherson@gmail.com/2026/02/23/164822.html">config.json changes</a> to make it work.

### February 21
- Spent time today testing Scott's Docker Compose for Feedland. I got Feedland up and running with the ability to signup and signon on my Macbook via localhost as instructed by Scott. My attempts to get this running on a Debian or Ubuntu server does not work. It looks like the app is not able to write to mysql because there is no records added to pendingConfirmations. Posted <a href="https://github.com/scotthansonde/feedlandDockerCompose/issues/8">an issue</a>.

### February 20
- <a href="https://linkblog.scotthanson.de/2026/02/20/feedland-docker-compose-for-localhost/">Scott has released</a> the updated version of his <a href="https://github.com/scotthansonde/feedlandDockerCompose">Docker Compose for Feedland</a> that supports localhost and it provides a scripted way to produce the magicString for login.
- Here is <a href="https://lwindolf.github.io/rss-feed-index/blogroll.htm">an index to blogrolls</a>. By definition, a blogroll is a OPML file that lists RSS feeds. To test, I click on an entry and copy the URL to the clipboard, switch to Feedland and click Menu, Subscribe, From an OPML File URL. I first tried one of the awesomerss feeds and Feedland generated an error, then I tried another and the subscription worked. It doesn't appear as though the indexing validates the OPML file or the feeds.
- A flaw in the process of subscribing in Feedland file OPML URL is that there isn't a step to categorize the new feeds.

### February 19
- I've noticed that my linkblog feed created and provided by Wordland has changed when viewed as a river in that it doesn't show links. It looks ok in <a href="https://feedland.duckdns.org/?mailbox=https://wordland.social/fjmnotes/246129403/rss.xml">mailbox view</a>.

### February 18
- I think I've known about <a href="https://www.wired.com/story/pixel-10-can-now-share-files-with-apples-airdrop/">Android's Quick Share</a> option on my Pixel 10 that works with Apple's Airdrop but I had not tried it until today. Works as advertised.
- Seems like every day I am reading about another, new, RSS reader. I find the appearance of energy around RSS interesting, but note that many sites don't provide RSS feeds and I think that is mostly due to the desire to make money off one's site.

### February 17
- <a href="https://vincode.io/2026/02/16/building-zavala.html">Zavala 4.0</a> is not backwards compatible with prior versions, so looks like one needs to somehow manually export outlines from prior versions? I don't see any documentation about an upgrade path, so not sure whether one has to manually export files and re-import or if Version 4 helps in that process.
- Scott Hanson has made <a href="https://oldschool.scripting.com/frank.mcpherson@gmail.com/2026/02/17.html#a164207">a localhost version</a> for his Docker compose file for Feedland. Thinking about the best way for me to test this.

### February 16
- The <a href="https://store.huion.com/products/huion-ink-eb1011?irclickid=wCjX:R0xPxyZRJBwYdxX6UhNUkuxtey9w2KyWU0&sharedid=&irpid=3568835&irgwc=1&afsrc=1">Huion Eink Tablet</a> looks interesting given it's $329 price that includes the tablet, case, and stylus. I get the impression from watching <a href="https://youtu.be/_IzhYX3hp-c?si=gecxuGd8sSbzSYfK">this video</a> that Huion is a known competitor to Wacom, I have not heard of them. Even though the tablet supports EMR, I wonder whether my other styluses will work? I don't see this tablet available for purchase on Amazon.
- Manton added an RSS feed for replies/mentions to micro.blog user posts. I don't think <a href="https://micro.blog/feeds/frankm/mentions.xml">this feed</a> is useful to anyone other than myself. I've added it to the "frank" category in my instance of Feedland. A problem is that because this is a separate feed there is no sequencing of the appearance of a reply and the original post in my river, so it is not obvious what is the context of the reply.
- For some reason, the edit I made to the title of a post on my blog that I wrote yesterday is not taking affect and therefore the only way I can think to correct is to delete the post and then re-publish it today.

### February 15
- Air quality alerts today, at present Google is reporting the AQI is 151.

### February 13
- I spent the afternoon working on and testing <a href="https://wordland.shanson.de/2026/02/11/feedland-docker-compose/">Scott Hanson's dockerized version of Feedland</a>. I've written notes but I don't have the time now to edit and post them, which I will do this weekend. The net is that like the other time I installed Feedland in my home lab, I could not get browser access via HTTP to work. The web browser just simply refuses to load the site and displays an SSL error message. The good news is that I did get access to work via <a href="https://notthebe.ee/blog/easy-ssl-in-homelab-dns01/">my Nginx and duckdns.org configuration</a> in the same manner as I have done with other apps hosted in my home network.

### February 12
- <a href="https://wordland.shanson.de/2026/02/11/feedland-docker-compose/">Feedland has been dockerized</a>. I'll probably try this out in the home lab.

### February 10
- Found out that the default max number of feeds one can subscribe to in Feedland is 250, set by maxNewFeedSubscriptions in config.json. I assume that is to throttle the amount of records in the MySQL database. I increased this number to 500, which I expect to not be a problem because I am the only user.
- Just realized that there is no RSS feed for this outline file being served by PagePark, so a reason to keep using the "Old School" version is to have a RSS feed of my day notes. I just confirmed via Feedland that the HTTPS access to <a href="https://oldschool.scripting.com/frank.mcpherson@gmail.com/rss.xml">the RSS feed of that site</a> works.
- I took <a href="https://frankmcpherson.blog/2026/02/10/today-for-the-first-time.html">a long 30 minute walk</a> this morning because it is warm and sunny outside.
- I got HTTPS working for <a href="https://oldschool.scripting.com/frank.mcpherson@gmail.com/">the Old School version of my Daynotes</a>. For now I am going to keep writing my day notes here and I am not sure how or whether I will continue to use the old site. Details about how I got it working is <a href="https://oldschool.scripting.com/frank.mcpherson@gmail.com/2026/02/09/205300.html">here</a> and I shared <a href="https://github.com/scripting/drummerCms/issues/4#issuecomment-3873457630">my results in the Github thread</a>.

### February 9
- As I have been blogging more about tablets, particularly e-ink tablets, I added <a href="https://frankmcpherson.blog/categories/tablets/">a Tablets category</a> here and today I spent some time adding that category to related posts I have written during the last year.
- Managed to wget download a copy of the minimal template from github. Used VS Code to do a Find and Replace, it found only one entry in which the change needs to be made. Added to my shared github repo from which Digital Ocean apps pulls to https://shared.frankmcpherson.net. Right now the deployment is failing because Github is running a 500. Need to wait for Github's issues to resolve and then initiate a deploy.
- Appears that <a href="http://scripting.com/2026/02/09.html#a151426">Dave is now aware of the problem with the Old School blogs</a>. He says the real issue is that the blogs are now served by https and the template they are based on does not enable that. He provides <a href="https://github.com/scripting/drummerCms/issues/4">instruction for how to fix</a>, which starts by downloading a minimal template, editing it, putting the template html file on a public server, and then adding a header variable to the blog outline. Unfortunately at the moment Github is down so I cannot work on the fix.

### February 8
- Downloading and installing V3.12.12 of the software on my Viwoods AI Paper Mini. Update went smooth and I like the new Quick Refresh mode.
- I am not sure about how long this page is becoming given that I am writing here nearly every day. Feel like at some point I may want to start collapsing days.
- <a href="https://www.manton.org/2026/02/07/really-happy-with-the-new.html">Manton says</a> that he has been working on a new editor for micro.blog and will be releasing it on Monday. I am looking forward to trying it out, although since I am now primarily using my Macbook I find that most of my blog posts are being written in Drafts. I think I would prefer to continue writing posts in Drummer but I am probably the only person who wishes to do so and therefore not worth Manton's time to fix.

### February 6
- <a href="https://github.com/hepplerj/claude-transcribe/blob/main/QUICKSTART_CLAUDE.md">Claude Transcribe</a> is a Python app that uses Claude API to perform OCR on batches of PDF files. The developer claims it does a decent job at handwriting recognition. Curious about whether this is something that could be used in my Viwoods to Obsidian work flow.

### February 4
- <a href="https://lists.opml.org/#1770245942000">Dave made a reading list</a> for the Hacker News "stars" from 2025. I opened my instance of Feedland and clicked Tools, Reading Lists, Subscribe to reading list. I then clicked on the link to view the list as a news page and then added it to the bookmarks so that I can open it easily. I notice that there is a new category called hackernewsstars. Finally, I added this category to the news home page tabs.
- Looks like posting to micro.blog from Drummer is completely broken. I need to stop trying to do this.
- <a href="https://blogbook.my/">Blogbook</a> is an app in development that one can use to make PDF and EPUB files by exporting from WordPress, Micro.blog, or Ghost blog to a single Markdown file. Filter by categories, authors, tags, and dates—then open in Marked 3 for PDF, EPUB, and more. I can create a physical book from an export of my micro.blog to Day One, but that takes all posts in a date range while what I really wanted to do was only publish in book format essays.
- I am 60% done walking the equivalent of the Pacific Crest Trail, tracked using the <a href="https://walkthedistanceapp.com/">Walk The Distance app</a>.

### February 3
- <a href="https://zavala.vincode.io/">Zavala</a> is an outliner for Mac, iOS, and iPadOS. You can import OPML files but it doesn't read/write them. All outlines are stored in a database. I have not found an obvious way to delete an outline and I find that the fact that I cannot read/write OPML files to be disappointing. Fortunately, I still have a copy of Electric Drummer installed on my Mac.

### February 2
- Yesterday I played with Docker Sandbox and the Claude Code agent, which was my first hands on experience with a AI coding agent. Today I learned about <a href="https://buildwithpi.ai/">another coding agent called Pi</a>.
- Created the outline for <a href="https://info.frankmcpherson.net/2026booksread.opml">the books that I read in 2026</a>
- Decided to keep archiving monthly OPML files to Github

### February 1
- One thing that I wish pagePark would do is provide users with ways to collapse and expand all in an outline.
- The calendar has turned over to February and it is still friggin' cold out!

## January 2026

### January 31
- <b>Notes About Hosting This Site</b>
  - Basically, what I need is to be able to store a copy of this outline to another server that can be accessed via a proper URL.
  - FWIW, I notice that <a href="https://daveverse.org">https://daveverse.org</a>, which is where Dave is publishing to Wordpress has the same template as the OldSchool sites, which means there is at least one other way to get a date drive blog running.
  - A concern is that the public URL for this outline is https://drummer.land/frank.mcpherson@gmail.com/Daynotes.opml so whatever is the cause of the breakage at http://oldschool.scripting.com can also appear with the server hosting Drummer, although if that happens it might affect more people than myself and in particular Dave.
  - I took a quick look at <a href="https://github.com/scripting/oldSchoolBlog/tree/master">Dave's oldSchoolBlog app</a> and quickly decided that there is not much chance of my building my own instance of the app to keep this going the way it used to go.
  - Do I want to collapse each day after it passes? I think for now I am going to keep them expanded.
  - Last thing that I have done is to change the forwarding url <a href="http://daynotes.frankm.info">http://daynotes.frankm.info</a> to forward to this page rather than the OldSchool blog page. Looks like I have to wait for DNS to update.
  - Going forward I will use this one outline for my daily notes. I am going to keep each month in the outline but I am going to collapse the month header after the month has past. I think this will provide an easy archive of my day notes. I need to decide whether I am going to continue creating the monthly OPML files that I have been storing in Github.
  - I have added an icon to the icon bar in Drummer to replace the plus icon that calls op.insertInCalendar (), which when invoked either creates the calendar headers if they don't exist or creates a new blank node without setting a type attribute. The result is that pagePark renders this outline as I desire.
  - I've been thinking about what to do if Dave doesn't fix the hosting of the Old School blogs. My decision is to create this second outline of which I think pagePark will do a better job of rendering.
  - I did not realize this, but it seems that for some reason pagePark has a problem rendering nodes that have a type value. For whatever reason some time it renders the entire node as a link.

### January 30
- I have created a redirect to this public OPML file to provide an alternate way to get to it than Dave's OldSchool server. The url is <a href="https://info.frankmcpherson.net/daynotes.opml">https://info.frankmcpherson.net/daynotes.opml</a>. There is something really weird going on with serving this file that is causing an entire node to be a URL like this one.
- Getting an error when building <a href="http://oldschool.scripting.com/frank.mcpherson@gmail.com/">my blog</a>, the file name contains illegal characters. I have been curious about how this url: http://oldschool.scripting.com/frank.mcpherson@gmail.com/ has been working given the 'at' sign because Dave chose to use email addresses for the home site.
- <a href="https://github.com/andrew-waters/orchard">Orchard</a> is a native (swift) application to manage containers on macOS using the new Containerization framework.

### January 27
- To me the answer to <a href="https://micro.blog/ReaderJohn/82907830">the question in this thread</a> is so obvious, because I think the natural outcome of religion is idolatry. When you consider that a group of people worship and idol, whether that be a religion, a bible, or even a name then it is easy to understand how those people don't know what is real so much so they don't even care because the idol reinforces their beliefs.

### January 20
- <a href="https://github.com/rcarmo/agentbox">Agentbox</a> is a simple Docker-based coding agent sandbox, originally inspired by running Batrachian Toad as a general-purpose coding assistant TUI and now generalized to more tools.
- Rui Carmo has published <a href="https://taoofmac.com/space/blog/2026/01/17/2130?utm_content=atom">an overview</a> of his RSS summarization and reading pipeline.

### January 13
- Leo Laporte has vibe coded <a href="https://github.com/leolaporte/rss-reader">a terminal RSS reader app</a> that uses Claude API for summarization. This might provide me with a way to test AI summarization of RSS feeds. And here is <a href="https://github.com/travisred/rss-local-storage">another RSS reader that uses local storage</a>. It does feel like RSS is making a come back given the number of people making apps for it.
- I am thinking of paying for a monthly subscription to Claude in order to learn more about AI and what it can do for me.
- <a href="https://privatellm.app/en">PrivateLLM</a> is a iOS/iPadOS/MacOS app that runs open source LLMs on the device and costs $4.99. The LLMs are not from Hugging Face and optimized for the app.

### January 12
- I haven't upgraded to Tahoe yet, and <a href="https://noheger.at/blog/2026/01/11/the-struggle-of-resizing-windows-on-macos-tahoe/">this is a reason why</a>.

### January 9
- <a href="https://www.touch-portal.com/">Touch Portal</a> enables one to turn an Android or iOS device in to a stream deck.
- Found an app, <a href="https://zetabitapps.com/standbymodepro">Standby Pro</a>, that turns my Pixel 10 in to a smart display when I have it on the wireless charger. What I like about it is, I can configure the manner in which the app auto launches. Right now it is configured to only launch when I put the Pixel 10 on the charger in landscape and its connected to Wifi. If I put the phone on the charger in portrait the app does not launch and in my case the phone stays on the lock screen. The app comes with a number of preset configurations but also can display standard Android app widgets, which means that I can have the Windy radar display to show the current weather. I tried Radarscope but that widget doesn't want to work in landscape.
- I have <a href="https://www.belkin.com/p/2-in-1-foldable-magnetic-charger-with-qi2-25w/BBB010-BL.html">this Belkin Qi 2.5 wireless charger</a> that I am really happy with, it charges my phone and ear buds wirelessly at the same time and has a USB-C port to plug in my watch charger. Funny that it wasn't until I tried Standby Pro that I even considered putting the phone on the charger in landscape.

### January 8
- <a href="https://docs.tropy.org/">Tropy</a> is free open-source software that allows you to organize and describe photographs of research material.

### January 6
- I have not yet upgraded my Macbook Pro to Tahoe. I guess the main reason why is that I haven't seen a compelling reason why I should run toward it. And yet, I do want to keep current so sooner or later I will have to go there.

### January 3
- <b>The Clicks Communicator</b>
  - I noticed some entries in my RSS feeds this morning making reference to the Blackberry, and I suspect they were in reference to the <a href="https://clicksphone.com/communicator">Clicks Communicator</a>, a new Android-based phone to launch later this year. This is from <a href="https://www.clicks.tech/">the company</a> that has been selling a physical keyboard case for the iPhone. The Clicks Communicator has a built-in physical keyboard, hence the reference to Blackberry.
  - The device software is built on Android 16 with a customized launcher that is optimized for communications. What it looks to me like is the Android notification shade made front and center to the device. It has hardware buttons to initiate voice to text input, if one prefers and has an LED around the primary button that will flash different colors one configures for different notifications. The color LED reminds me of the roller ball of the first Android phone, the T-Mobile G1.
  - The negatives start with the price, while one can reserve one now for a $399 total price by paying $199 to reserve it, the Communicator will retail for $499, which I think is too much for a device being promoted as a second phone. The intro video compares the Communicator to a Kindle as it compares to the iPad, but Kindles cost much less than $499.
  - Another big miss in my opinion is not providing a removable battery nor Magsafe support, although I imagine this might be something that could be provided via special "cover." The device includes the things smartphones lost over the years like the physical buttons, storage card slots, and 3.5mm audio adapter, so why not go all the way and provide removable batteries?
  - The Clicks Communicator is going to be a niche device, it's not going to take over the smartphone leaders. I got to think that $499 starting price will have to come down to the $300 to $400 range to justify the purchase as an "accessory" to an every day carry smartphone. The question then is, will enough sell for the device to last long enough for the price to come down? The answer depends on whether there is truly a demand for this type of device.

### January 2
- For the first time I used the <a href="https://dayone.app">Day One app</a> to create a book of my blog posts I wrote during the past year. I've known about this ability and have wanted to do it for a while, but it wasn't until recently that I found a way to send all of my posts to the app. I was surprised to find that one can only create and purchase the book on the iOS/iPadOS versions of the app, I wonder why they don't include this feature in the MacOS app. I have also created a PDF of all my blog posts, but the book I ordered is only for the past year.

### January 1
- I published my <a href="https://frankmcpherson.blog/2026/01/01/year-in-books-for.html">2025 Year In Books</a> to my blog using <a href="https://epilogue.micro.blog/">Epilogue</a> and wrote <a href="https://frankmcpherson.blog/2026/01/01/at-the-start-of.html">my first blog post for the year</a> in Obsidian. My first attempts to use the micro.publish plugin to publish the post failed and it took me a little bit of time to update the plugin, which resolved the problem
- Happy New Year!