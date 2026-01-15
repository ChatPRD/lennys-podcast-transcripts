---
guest: Bret Taylor
title: 'He saved OpenAI, invented the “Like” button, and built Google Maps: Bret Taylor
  (Sierra)'
youtube_url: https://www.youtube.com/watch?v=qImgGtnNbx0
video_id: qImgGtnNbx0
description: Bret Taylor’s legendary career includes being CTO of Meta, co-CEO of
  Salesforce, chairman of the board at OpenAI (yes, during that drama), co-creating
  both Google Maps and the Like button,...
duration_seconds: 5338.0
duration: '1:28:58'
view_count: 91720
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- pricing
- hiring
- leadership
- management
- strategy
- vision
- mission
- differentiation
- market
- persona
- jobs to be done
- design
- ui
---

# Inside the expert network training every frontier AI model | Garrett Lord

## Transcript

Lenny Rachitsky (00:00:00):
You're CTO of Meta. You are a co-CEO of Salesforce, you're chairman of the board at OpenAI. How do you think the AI market is going to play out?

Bret Taylor (00:00:07):
The whole market is going to go towards agents. I think the whole market is going to go towards outcomes-based pricing. It's just so obviously the correct way to build and sell software.

Lenny Rachitsky (00:00:16):
This makes me think about, I had Marc Benioff on the podcast. You guys were co-CEOs. He was extremely agent-pilled.

Bret Taylor (00:00:21):
It's so hard to sell productivity software, which I learned the hard way.

Lenny Rachitsky (00:00:24):
What's a story that comes to mind when you think about your biggest mistake?

Bret Taylor (00:00:27):
I was the product manager for, it was called Google Local had a pretty tough product review with Marissa and Larry, and to not do that well with a link from the Google homepage is embarrassing.

Lenny Rachitsky (00:00:37):
I think it's really empowering for people to hear it's possible to succeed in spite of a massive failure like this.

Bret Taylor (00:00:41):
They gave me another shot to do the V2 of it that resulted in Google Maps. We got about 10 million people using it on the first day.

Lenny Rachitsky (00:00:48):
What mindset contributed to you being successful in such a variety of roles?

Bret Taylor (00:00:52):
Waking up every morning, what is the most impactful thing I could do today?

Lenny Rachitsky (00:00:56):
Today, my guest is Bret Taylor. Bret is an absolute legendary builder and founder. He co-created Google Maps at Google. He co-founded the social network, FriendFeed invented the like button and the real-time newsfeed, which he sold to Facebook. He then became CTO at Facebook. He then started a productivity company called Quip, which he sold to Salesforce for $750 million. He then became co-CEO of Salesforce. He's also currently chairman of the board at OpenAI. At one point he was chairman of the board at Twitter. Today, co-founder and CEO of Sierra an AI started building agent to help companies with customer service sales and more.

(00:01:32):
In our conversation, we cover so much ground, including what skills and mindsets have most helped Bret be so successful in so many roles, why we're all still sleeping on the impact that agents are going to have on the business world. How coding is going to change in the coming years, where the biggest opportunities remain for startups, lessons on pricing and go-to-market in AI, the story behind the like button and so much more. This is a truly epic conversation with a legendary builder.

(00:01:57):
If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become an annual subscriber of my newsletter, you get a year free of a bunch of incredible products, including Replit, Lovable, Bolt, n8n, Linear, Superhuman, Descript, Wispr Flow, Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, Mobbin and more. Check it out at Lenny'snewsletter.com and click bundle. With that, I bring you Bret Taylor.

(00:02:22):
This episode is brought to you by CodeRabbit, the AI code review platform transforming how engineering teams ship faster with AI without sacrificing code quality. Code reviews are critical, but time-consuming CodeRabbit acts as your AI co-pilot providing instant code review comments and potential impacts of every pull request. Beyond just flagging issues, CodeRabbit provides one click fix suggestions and lets you define custom code quality rules using AST GREP patterns, catching subtle issues that traditional static analysis tools might miss.

(00:02:55):
Coderabbit also provides free AI code reviews directly in the IDE. It's available in VS. Code, Cursor and Windsurf. CodeRabbit has so far reviewed more than 10 million PRs installed on 1 million repositories and is used by over 70,000 open source projects. Get CodeRabbit for free for an entire year at CodeRabbit.ai using code, Lenny. That's CodeRabbit.ai.

(00:03:20):
This episode is brought to you by Basecamp. Basecamp is the famously straightforward project management system from 37signals. Most project management systems are either inadequate or frustratingly complex, but Basecamp is refreshingly clear. It's simple to get started, easy to organize and Basecamp's visual tools help you see exactly what everyone is working on and how all work is progressing. Keep all your files and conversations about projects directly connected to the projects themselves so that you always know where stuff is and you're not constantly switching contexts. Running a business is hard. Managing your project should be easy. I've been a long time fan of what 37signals has been up to and I'm really excited to be sharing this with you. Sign up for a free account at basecamp.com/Lenny. Get somewhere with Basecamp.

(00:04:10):
Bret, thank you so much for being here and welcome to the podcast.

Bret Taylor (00:04:14):
Thanks for having me.

Lenny Rachitsky (00:04:15):
My pleasure. There's so much that I want to talk about. You've done so many incredible things over the course of your career. Just boggles the mind, the things that you've done, and we're going to talk about a lot of that sort of stuff, but I want to actually start with the opposite. I want to talk about a time that you messed up, a time that you screwed up in a big way. We have this recurring segment on the podcast called Fail Corner, and so, I thought it'd be fun to just start there before we get into all the great stuff you've done. What's a story that comes to mind when you think about maybe your biggest mistake in building a product?

Bret Taylor (00:04:43):
It may not be the biggest, but it was my first prominent mistake as a product manager at Google. So for me, it feels big because it was very formative for me as a product designer. So I joined Google in late 2002, early 2003, and I was one of the earliest associate product managers at the company and first, was working on the search system, essentially expanding our index from 1 billion webpages to 10 billion, which was a big deal at the time. It seems quaint now. Then I did a decent job and so my boss, Marissa Meyer, gave me the opportunity to lead a new product initiative, which was a big bet on me and it was both an opportunity to do something for Google, but I was also being pretty scrutinized just as a young new product manager and the premise given to me was work on local search.

(00:05:40):
At the time, the Yellow Pages was still dominant and well, Google was really good at searching the web. It wasn't really good for finding a plumber or a restaurant just because it wasn't really a huge part of the internet at the time. So this content wasn't necessarily on the internet and even if it was, you didn't really want to find plumbers in Manhattan, you wanted to find plumbers in San Francisco, if you're me. And so it was both a technical problem and a product problem and a content problem.

(00:06:11):
We launched the first version of that product that I was the product manager for, was called Google Local and it was, I'll be a little bit more critical now than I might've been at the time, but it was a little bit of a me too version of Yahoo Yellow Pages, essentially grafting on Yellow Pages search on top of Google Search and with a properly crafted query you could see those listings at the top of your search results but a standalone site at local.google.com. Actually, it was an important enough initiative that actually, there was on the Google homepage, it had Web, Images and Local was up there as well, so it's got top bill.

(00:06:54):
I mean you could put almost any link on the Google homepage and get a lot of traffic to it. And despite that, it didn't do that well and to not do that well with a link from the Google homepage is embarrassing. There's not much one can do more than giving you that kind of traffic to give you an add that as a product leader or a product manager. And the product was fine, it worked, but it really wasn't differentiated. And in many ways, I think, again, I think I've had these reflections more sense than at the time, that I had some of the time, but why use this instead of Yahoo Yellow Pages? But more than anything else, why use this instead of the Yellow Pages? It was a digital version of something that had come before. Had a pretty tough product review with Marissa and Larry and others and it was fine. I wasn't about to get fired or something, but it was, I don't know, the shine on my reputation was waning a little bit.

(00:07:52):
And they gave me another shot to do a V2 of it and I got the impression it wasn't like my last shot, but I certainly was feeling a little dejected from going from a hot shot, new PM to a new thing. So, we spent a lot of time thinking about how can you make something that's just much more compelling and not just a digital version of the Yellow Pages and not just so similar to some of the other products out there. And that ended up being the thread that we pulled that resulted in Google Maps. We had licensed from MapQuest, the ability to put this little map next to the search results, it was always the ugliest part of the product and we always made these backhanded comments about it internally and we spent a lot of time saying, what if we inverted the hierarchy here and made the map the canvas?

(00:08:49):
We ended up finding Lars and Jens Rasmussen who had been working on this Windows mapping product and we got them into the company and started exploring this space and it ended up where, through that exploration we ended up integrating a lot of different products. We ended up integrating mapping local search, driving directions, like all of these products at the time were actually separate product categories and ended up with something that redefined the industry and certainly my career. But it took, I think for me as a product leader, it changed the way I think about product just because there's feature and functionality and then there's like why should I use this thing in the first place? And it was notable, there was a couple of interesting moments.

(00:09:34):
When we launched Google Maps we got about 10 million people using it on the first day, which at that scale of the internet at the time was huge. And then in August of 2005, we integrated satellite imagery from a recent acquisition called Keyhole, which became Google Earth and we got 90 million people using it on the same day. Everyone wanted to look at the top of their house when the imagery came out. And it was really interesting because there's so many subtle product lessons in there. First is, I think as you have these new technologies, rather than literally digitizing what came before, if you can create an entirely new experience, it answers the question for a new customer, why should I give this the time of day? And so, really disassembling the Lego set and reassembling into something new rather than just digitizing what was there before. Certainly, that was the lesson I think in Google Maps, really was native to the platform in a way that a paper map couldn't be and that was a really meaningful breakthrough.

(00:10:35):
And then with satellite imagery, it honestly wasn't the most important part of Google Maps, but it was the sizzle to the steak and it created, I don't think the term viral was a thing people said back then, but it created a viral moment. We were on Saturday Night Live, which is the coolest thing. Andy Samberg in, I think it was called Lazy Sunday rapped about Google Maps and Lars and I were texting each other. We did it. We're on Saturday Live. Mission accomplished. And it was also showing that as you're there thinking about products, there's the why you decide to use a product and then what is the enduring value. And those are deeply related but not all the same thing. And I just learned so many lessons that I took with me for every subsequent product that I worked on.

Lenny Rachitsky (00:11:18):
That is an awesome story. One I think it's really empowering for people to hear, even you Bret, who I'm going to share all the successes you've had, have had a massive failure with the CEO of Google [inaudible 00:11:30] just like Bret, you screwed up. And it was such a big bet. So one, just it's possible to succeed as you have succeeded in spite of a massive failure like this. And then some of the product lessons you shared, just to highlight a few of these things because I think this is great, is just you will often not win if you just make something that's a better copy of something else, what you want to look for is something that is an entirely new experience, something that's differentiated, something that's a lot more compelling. Let's flip to talk about what you've learned from actually being very successful at a lot of things.

(00:12:02):
So I was looking at your resume and you basically have been very successful at every level of the career ladder and in such a huge variety of roles. So let me just read a few of these things for folks that aren't super familiar with your background. You were CTO of Meta, you were co-CEO of Salesforce, you're also CPO and COO at Salesforce. At Google, you joined as an associate product manager where you famously, you didn't mention this but you rebuilt Google Maps on weekend. We're not going to talk about that. You're chairman of the board at OpenAI. You were chairman of the board at Twitter. You've also founded three different companies, one social network, one productivity docs company called Quip, and now, Sierra. Fun fact, at FriendFeed you invented the like button and I don't know if people know that and also just the newsfeed, I'll just throw that out there to give you some credit.

(00:12:50):
So you're basically an associate product manager, an IC product manager, an engineer, CPO, COO, CTO, CEO of three different companies including a public company. Very rare that somebody is successful at all these types of roles and all these levels. So, let me just ask you this question. What mindsets or habits or just ways of working have you worked on building in yourself that you think have most contributed to you being successful in such a variety of roles and levels?

Bret Taylor (00:13:19):
Yeah. It's actually something I am proud of. I like the fact I've worn different hats. It's actually amusing when I meet colleagues that I've known from one of those jobs, they'll often think of me through the lens of that job. And so, I'll go to meet folks from Facebook and they think of me largely as an engineer. I'll meet folks from Google, they think me largely as a product person. At Salesforce, a lot of the folks there interacted with me as like a, lack of a better word, a suit, the boss. And I'm not sure they think of me as an engineer at all, even though I was still probably coding on the weekends for fun. And one of the things that is a principle for me is to have a really flexible view of my own identity. I probably would self-describe as an engineer, but more broadly I think of myself as a builder and I like to build products and I think companies are one of the most effective ways to build products.

(00:14:17):
There's also things like open source, but I think I'm a huge believer in the confluence of technology and capitalism to produce just incredible outcomes for customers. And as a consequence, I think to really build something of significance, I think to be a great founder, you really need to be able to not have such a ossified view of your identity that you can't transform into what the company needs you to be at that point. And every founder you'll talk to, one day, I think selling is a big part of being a founder. You have to sell investors on wanting to invest in your company. You have to sell candidates on wanting to work at your company. You have to sell customers to want to use the product that your customer produces. You have to have good design taste, not just for your product but for your marketing and essentially, soliciting your customers.

(00:15:09):
You have to have good engineering. If you're building a technology company, the technology comes first. It's why this industry is so transformative. I probably credit, and I've told this story before, but I'm very grateful for her, but I probably credit Sheryl Sandberg for really changing the way I approach new jobs. The story, and I might be embellishment a little bit, but I think it's broadly accurate. So I had just become the chief technology officer of Facebook and when I first got the job, it was the flavor of CTO or that relatively small group reporting into me, but contributed almost as a very senior architect on a number of projects. And then at some point, Mark Zuckerberg reorganized the company and split it into a bunch of different groups. I ended up with a very large group, 100 under me and I was essentially running our platform and mobile groups, products, design engineering.

(00:16:10):
So I went from a handful of reports to, I don't know, over 1,000 or something. It was a big group. And it was the largest management job. I had become a manager at Google, but a modest team. And so, I was doing okay but not great. And I had this moment where Sheryl saw me, I think I was editing a presentation for a partner just because the presentation I got didn't meet my quality bar and I was editing it and griping about it. She pulled me into a room and gave me talking to a little bit about holding my team to as high of a standard as I have. If someone wasn't meeting my expectations, what was my plan to manage them out of the company or... Just giving me management one-on-one.

(00:16:57):
And she's a remarkable mentor in the sense she can give you feedback that's very direct and often, a bit uncomfortable, but you know she cares about you. And so it was the type of feedback you listen to. I went home that night and I was stewing on it and not very happy. I was like, you get naturally a little defensive in those moments. Is that really true? Am I really fucking it up or is she overreacting? And then I woke up the next day, I was like, "No, she's right." And I had realized this subconscious limiter that was limiting my success in the job, which is, I was trying to conform the job to the things I thought I liked to do. So, I was spending a lot of my time on some product and technology things that I was passionate about, thinking I'm the boss. I should focus on what I want to focus on instead of thinking about, okay, I'm running the mobile and platform teams at Facebook. What's the most important thing to do today to make our mobile and developer platform successful?

(00:18:03):
And when I reframed the job that way, I did different things. And the thing that was the biggest pleasant surprise to me was I liked it. I thought I liked engineering and product, but in fact, when I changed an organization and it turned out to be more successful, I derived a great deal of joy from seeing that success. Our developer platform had a lot of partners and when there was an issue there and I'd spend time on partnerships and it worked and our platform became healthier, the partner became more successful. I took pride in that success and then I just started being better at my job and I realized that the actual act of engineering or product design or all the things I thought I liked, what I really liked is impact.

(00:18:49):
And so, that conversation led to my waking up every morning, sometimes literally, but certainly, in the broadest sets of the words saying, "What is the most impactful thing I can do today?" And really thinking almost like, if you had an external board of advisors telling you what are the things where if you focus on them, you can maximize the likelihood that what you're trying to achieve will happen? Sometimes, it's recruiting, sometimes, it's product, sometimes, it's engineering, sometimes, it's sales. And I've become much more self-reflective just about what is important to work on. And I have become much more receptive to doing things that I previously would've said aren't my favorite things to do because I derive so much joy from having an impact that I enjoy a lot more things now. And so, I really credit Sheryl, I'm so grateful. And actually, it's interesting, I think a lot about this when I give feedback to people now, just those moments that can change the trajectory of your career. I give her all the credit for it.

Lenny Rachitsky (00:19:53):
There's so many people that share stories of Sheryl Sandberg giving them advice and that changing their life. What a mensch.

Bret Taylor (00:20:01):
Yeah.

Lenny Rachitsky (00:20:01):
My biggest takeaway from this, which is this question of what is the most impactful thing I could do today? Such a powerful heuristic just to keep in mind. To your point, you may realize you don't want to be doing sales or hiring, but if that's the most impactful thing and you end up doing it, you may realize I like this and I'm good at this and have thought about-

Bret Taylor (00:20:18):
Can I double click on that though for a second?

Lenny Rachitsky (00:20:19):
Absolutely.

Bret Taylor (00:20:20):
I think it's really hard. One of the dangers for founders and product managers, but I think particularly for founders is incorrect storytelling. People don't like my product because of X. And if you tell that to yourself and you tell it to your team, all of a sudden, it goes from being an intuition to being a fact. Well, you better hope you're right because if you orient your strategy around fixing a problem and you're wrong, your company's going to fail. So why did you lose a deal? You could talk to the salesperson who is on the account or perhaps maybe a product manager was involved in the conversation. It's very important to have intellectual honesty in those moments because you could say something like, "Oh, they didn't buy it because the platform cost too much." And that's something a salesperson might say.

(00:21:16):
Maybe the real reason is they didn't actually see much value in your platform. So it was communicated to the salesperson as it was too expensive. But in fact, the problem was product differentiation. And you could end up going into a discussion on pricing when in fact, there was a much deeper, much harder problem to solve there. But just like when you break up with someone, you don't say, it's because I don't like you anymore. You say it's not you, it's me. You say all these pleasantries because we're all social animals and you want to be pleasant with the people around you. So literally taking what a customer says or what a user says in a focus group or a usability study is rarely correct. It often is related to what the truth is, but it's very important to get right. And so, I think one of the things I've observed with first time founders in particular is you're often a single issue voter based on your skillset.

(00:22:14):
So if you're a great engineer, the answer to almost every problem in your business is engineering. If you're a product designer, the answer almost to the proverbial redesign, I joke, it's like the dead cap balance of a consumer product like this next redesign will fix all of our problems. I don't know if it's ever, ever worked. And then I met a lot of entrepreneurs who come from a business development background, they're always thinking about partnerships and oh, if we just get this partnership done for this distribution channel, everything's going to change. And I think it's really important when you're a founder to be self-aware that you will naturally, subconsciously pick the thing that is your strength, your superpower as a solution to more problems. And in fact, if you think that's a solution to your problem, it may be right, but you probably by default should question it.

(00:23:03):
If you think the thing that you've been doing your whole career is the way to fix your problem, it's at least 30% likely that you've chosen that because of comfort and familiarity not truth. And so, I think one of the skills I think is, it really goes around to do you have a good co-founder? Do you have a good leadership team? If you're a product manager, you're a partner in engineering, you're a partner in marketing, you really want to have very real conversations to ensure that you're actually working on the actual correct thing. And I think it's easy to say what's the most impactful thing to do today? My guess, if a lot of people try that, they'll lie to themselves more often than not. And it's a very challenging question to answer. The question's interesting. Being able to answer it accurately is actually the hard part.

Lenny Rachitsky (00:23:50):
This feels like such an important lesson you've learned. Is there an example that comes to mind where you learned this the hard way where you actually ended up-

Bret Taylor (00:23:57):
Oh, yeah. You just want to spend this whole thing on my failures, but I'm fine with that.

Lenny Rachitsky (00:24:02):
You've had too much success.

Bret Taylor (00:24:04):
Frontier was my first company. At our peak we had 12 employees, 12 of the best people I've ever worked with. Started the company with Jim Norris, who's an engineer I've known since Stanford and Paul Buhite and Sanjeev Singh who Paul started Gmail. Sanjeev was the first engineer at Gmail, so we had the Google Maps people and Gmail people. It was a pretty awesome founding team. We made a social network, as you said. We invented a lot of concepts that became popular in the newsfeed. We invented the like button. It was really neat. It was a fun time. We were only really popular in Turkey, Italy and Iran, and at one point, we were blocked in Iran, so we were only popular in Turkey and Italy and Silicon Valley. To this day, actually a lot of folks in Silicon Valley are like, "I love FriendFeed." I'm like, that's awesome.

(00:24:51):
It wasn't really a successful business. We were a follower-oriented social network, not a friendship-oriented social network, which meant a lot of our content was more like X or Twitter than it is Facebook in that respect. And a lot of sharing newspaper articles, interests, scientific communities, things like that. And there was a period when Twitter, which was one of our competitors at the time, that there was a lot more social networks at the time. I am probably screwing this up a little bit. I think Obama, Ashton Kutcher and Oprah Winfrey all went on Twitter in a summer and we just got our ass kicked.

(00:25:31):
And it was a great example of you... I think 11 of those 12 people were engineers and we were just making product and I think it was Biz Stone. If you talk to the Twitter folks, they could give you the history on this, but I think Biz was really focused on getting celebrities and public figures onto Twitter, which is totally obvious. If you have a social service that's oriented towards following people, put some people on there worth following and instead, we were exclusively focused on polishing the product.

(00:26:00):
And we actually, I think at our peak of popularity, we were very confident just, I think it was a time when Twitter had the fail whale and it was down half the time and people couldn't even use it. And our product, we were innovating faster, we had more features, people liked it and we were up 100% of the time and we totally lost for no reason related to product at all. And it was an example of, I think somewhat famously not a lot of great entrepreneurs have come out of Google because Google was so successful, I think it's hard as a product manager to see distribution and product design and even business model when you have AdWords and money's raining from the sky. There wasn't as much scrutiny and I think folks like the PayPal Mafia I think learned a lot more about entrepreneurialism than a typical PM at Google. So, we're just getting punched in the face and learning this the hard way.

(00:26:57):
And so, that was probably the most prominent example of it and I think we probably did have a... I can tell you all the flaws of that product, but I don't think that was the reason why we lost. There's a lot of reasons. I think there was a lot of flaws of the product, but it was a lot of other stuff. And so, I've learned, accumulated these skills over time, but I say the hard part of that question is answering it correctly, is it's hard when you don't have experience in something, than to have intuition in it. So I think if there's probably a structural flaw, it wasn't that... I don't know if I could have figured out how to reach out to Ashton Kutcher [inaudible 00:27:28], it's not he's on my Rolodex. But I probably wasn't soliciting advice from the right people.

(00:27:36):
I think that what's great about the technology industry is there's a lot of advice. Choosing whom you listen to is actually quite difficult, but I think we're somewhat myopic. We're in our own little world, creating this product and we weren't asking people from the outside in to say, what are you seeing that could go wrong? What are you seeing that could go right? What are you seeing in the industry that we're not doing that you think we might want to do? And this is why boards are important. This is why finding the right advisors, the advisors will actually tell you what you not [inaudible 00:28:09] want to hear, but you need to hear. I think that was probably the missing part. I'm not sure I was great at market at the time, but if I had solicited the right advice, I could have learned that that was a shortcoming. And I think that was a deep lesson I took from that. I'm a huge believer in boards and getting good advice.

Lenny Rachitsky (00:28:26):
Any heuristics or advice for people to know whose advice to listen to? What do you pay attention to when you're like, okay, ignore this person but listen to this person?

Bret Taylor (00:28:35):
Yeah, that one's tough. It does come down to good judgment and being judge of people's character. One thing that is particularly hard is there's not a strong correlation between the confidence with which someone expresses an opinion and the quality of that opinion. I don't want to say it's inversely correlated, but that's funny, with all the podcasts out now, if there's topics I know a lot about, sometimes the most eloquent, confident statements about things I know a lot about, are the least accurate and it sounds extremely persuasive. And so, it does require very good judgment. One thing is I think, not just asking for advice but asking people, who should I talk to get good advice? And you'll find some common answers there and that's often a really strong signal of good judgment.

(00:29:26):
And then one thing I found is when you ask for advice, don't just ask what to do but why. Be an obnoxious two-year-old kid, why? Why? Why? Why? And really try to understand the framework that someone is using to give you advice. The interesting thing about advice is people are often extrapolating from relatively few experiences. So they will say, never do this or always do that. And it's because they had one experience where something backfired or something could have gone better if they had done it. So it's a useful anecdote, but if you don't ask why and understand they had one experience and here's what happened, it can come across as a rule when in fact, it's [inaudible 00:30:08] data and if you ask advice of three people and they all have very similar interactions, you can create a first principles framework from which that advice emerges. And when you start applying it, you're applying it with a degree of nuance that you couldn't if you're just following a rule. So, I think one is, it does come down to good judgment, I think. I don't know how to teach that.

(00:30:30):
I'm a huge believer in good judgment. It's one of the things I hire for. I just think that's something that probably comes from a mix of self perfection. You really need to hold yourselves accountable as an entrepreneur, as a product manager. If you made a bad decision, spend time reflecting on it, number one. And really, try to understand why and try to always improve your judgment. I think at the end of the day, that is why you are a good entrepreneur, a good product manager. And number two, when you get advice, really understand where it's coming from and why so that you can create your own independent view of where that advice came from and recognize that no one's advice is statistically significant or very rarely is it. If you're getting advice on investing from Warren Buffett, yeah, okay, it's statistically significant, but most advice is like something happened to you once and you have regrets.

Lenny Rachitsky (00:31:28):
I love that you're like, I don't know if I have a great answer then you just give us an incredible answer to this question. I want to go in a different direction. You mentioned that you describe yourself as an engineer. I know I heard you code to relax still. Let me just ask you this question, something a lot of people in college are thinking about. Do you think it still makes sense to learn to code? Do you think this will significantly change in the next few years?

Bret Taylor (00:31:47):
I do still think studying computer science is a different answer than learning to code, but I would say I still think it's extremely valuable to study computer science. I say that because I think computer science is more than coding. If you understand things like Big O notation or complexity theory or study algorithms and why a randomized algorithm works and why two algorithms with the same Big O complexity, one can then practice perform better than others and why a cache miss matters and just all these little... There's a lot more to coding than writing the code. The reason I think that is I do think the act of creating software is going to transform from typing into a terminal or typing into Visual Studio code to operating a code-generating machine. I think that is the future of creating software. But I think operating a code-generating machine requires systems thinking and I think that computer science, there are other disciplines as well, but computer science is a wonderful major to learn systems thinking and at the end of the day, AI will facilitate creating this software.

(00:33:08):
We may do a lot more in the next few years we can't even imagine, but your job as the operator of that code-generating machine is to make a product or to solve a problem and you really need to have great systems thinking and you're going to be managing this machine that's doing a lot of the tedious work of making the button or connecting to the network. But as you're thinking of the intersection of a technology and a business problem, you're trying to affect a system that will solve that problem at scale for your customers and that systems thinking is always the hardest part of creating products.

(00:33:40):
I'll just give you, it's this cheesy simple example, but I think it's representative. At Facebook, we spent a lot of time designing the newsfeed and if you ever had a really, really good designer and they showed you at the time, a Photoshop mock-up of the newsfeed, it was just all as beautiful. The photos, the family was happy and the photo was a perfect photo and the posts were all perfectly grammatically correct and of a completely normal length and the comments and there was the like... Everything was just perfect. And then you'd implement that design and you'd look at your own newsfeed and it looked like shit because it turns out not everyone's photos were made by a professional photographer. The posts were all these different lengths. The comments were like, you suck and... All that stuff.

(00:34:29):
And then all of a sudden you realize that designing a newsfeed, Photoshop is the easy part. You need to actually design a system that produces both in content and visual design, like a delightful experience given input you don't control. And that's a system, it's sort of a design and it's just, what we did practically, I am sure it's changed a lot since I left in 2012, but we made a system so designers had to show their newsfeed designs with real newsfeed data that was messy rather than anything artificial because I think it forced the process to be more realistic.

(00:35:10):
But I say that because I think that whether AI is writing code or doing the design or doing all these other things, you need to learn how to have a system in your head. You need to understand the basics of what's hard and what's easy and what's possible and what's impossible. And AI can help you do that too, by the way. But I do think that's a really useful skill. I think in general, with the advent of AI agents and AI approaching super intelligence in certain domains, I think the tools with which we do our job will change a lot. I think it's very important to have a very loose attachment to the way we do our jobs and that story that we won't talk about when I rewrote Google Maps, everyone talks about that story and I think it's because of Paul [inaudible 00:35:57] who told it on some podcasts and that's where it made the rounds.

(00:36:01):
I think that's going to end up this vestige of the past, almost like the human calculators at NASA before the computers were invented, like wow, a person was a calculator? Whoa, that's fun. Tell me that story. I think just what I was good at will no longer be useful in the future or certainly not valuable in the future and that's okay. So I think we need to have a really loose view of it, but the idea that you shouldn't study these disciplines, it's like people say, I don't want to study math because I'm not going to use it in my career for X. Well, studying maths is quite important. It teaches you how to think. It teaches you how the world works, physics, math, and I think computer science especially, at least the foundations of it, will continue to be the foundations of how we build software and understanding that when you're interacting particularly with something that's smarter than you, producing code you might not completely understand how you constrain it and how you get it to produce these outcomes. I think it will require a lot of sophistication actually.

Lenny Rachitsky (00:36:59):
That's such a great answer. There's this always sense of this binary, should I learn to code or not? And your point here is learn to understand how engineering works and how systems work and what your code does and how it all interconnects, but the way you actually do the coding at your desk will change significantly. This reminds me of something you mentioned on a podcast recently. This idea that you think there's going to, or there should be a new programming language that is more designed for LLMs versus humans. Can you just talk about that because I think a lot of people aren't thinking about that?

Bret Taylor (00:37:27):
I don't know if it's a language, I would call it a programming system because I think language might be too limited. My reductive version of the past, what 40 years of computers maybe more, is we created the hardware for computers, then we created punch cards, which is the way in the late '70s you would tell a computer what to do or maybe mid to late '70s. Then we invented early operating systems and time-sharing systems from the invention of things like Unix at Bell Labs and Berkeley, you ended up with the C programming language, Fortran and a lot of higher level programming languages. I think Fortran and then C.

(00:38:15):
And we moved up the layers of abstraction. No one does punch cards anymore, obviously. Few people write assembly language. Some people write C, some people write REST. But a lot of people write Python and TypeScript and things like that. And as we've invented more and more abstractions, we've made it easier to do high-leverage things. So, if you look at how remarkable Google was back in the day or Google Maps, you could probably give a lot of react programmers the task of make a draggable map now and I think a lot of people could do it. That was true RND back in the day.

(00:38:54):
When Salesforce was created in 1998, just putting a database in the cloud was hard and that alone was a technical moat that is now trivial with Amazon Web Services and that technical moat is comically narrow, but the product moat is quite large. I think that if the act of writing code is going from something that is very costly to the marginal cost of that going to zero, how many of the abstractions that we've built are based on human program or productivity? I think a ton. I always laugh that I assume Python is probably the most common generated code just because of how much it's in the training data and data scientists love Python and I love Python too. It's such a comically bad thing for AI to generate just because it's one of the most inefficient programming languages of all time. If you know the global interpreter lock and just slow. And I've written a lot of high-scale web services and it's just quite slow and it's very hard to verify.

(00:40:00):
It's not as bad as Perl, but if you have a big Python program, how many errors will you find at runtime versus before releasing it? So, Python was designed to be very ergonomic, almost looked like pseudo code for humans, for me to write code in a delightful way. That's why data scientists love it so much. So as we move to a world where let's just postulate, and I'm not sure this will be completely true, that we're not going to write a lot of code as people. We're going to be operating these code-generating machines. We probably don't care how ergonomic the programming language is. What we care about is when this machine generates code, do we know that it did what we wanted it to do? And if it doesn't do we want it to do, can we change it easily? I think there's a lot of insights in programming languages that could serve this.

(00:40:48):
So Rust I think, is interesting because if I asked you to look at a C program and say, "Does it leak memory?" You probably couldn't do it that well just because it's really hard and if it's a very, a million line C program, it's going to be very, very hard. If I asked you to verify that a Rust program doesn't leak memory, you would just have to compile it. And because it has compile time, memory safety, just the act of compiling successfully tells you that's true. I think we need more things like that because if an AI is generating this code, by definition, if you have to read every line that is going to be the limiting factor for producing the code or worse, you're just not going to read every line and you're going to emit a bunch of unsafe unverified code into the wild.

(00:41:36):
And so, the question is how do you enable humans to have as much leverage as possible? Which means using computers to do the work on your behalf. You could have obviously the simplest form of this, is AI supervising AI and doing code reviews and that's great. Certainly, self-reflection is a really effective way of improving the robustness of an AI system. But I do think if it doesn't matter how tedious it is to write the code, you could probably layer on some techniques that are out of fashion, like formal verification, unit testing, other things. And if you layer all these on, I'm thinking about it as, I as a... It's like the guy in the matrix with the green letters coming down, how can I make something so I as a operator of the code generating machine can produce incredibly complex scale software, incredibly quickly and know that it works?

(00:42:26):
If you start with that as your design center, I think you'd probably changed the languages, you'd probably changed the systems, you'd probably change all these things and you're probably going to bring to bear a lot of things. And what's really fun about it is you can loosen a lot of constraints, like coding is free. Okay, so that's neat. With that in mind, what do you want to do? What would be best suited for the language, the compiler for testing, for self-reflection, for supervisor models, all these things. I think that's more of a programming system than a language, but I think when we create something like that, it can really enable creators, builders to create incredibly robust, incredibly complex systems.

(00:43:04):
And I'm super excited about VibeCoding, but I don't know generating a prototype has been the limiting factor in software ever. It's actually building increasingly complex systems and actually changing them with agility. If you look at the famous Netscape one to Netscape two rewrite, somewhat, a lot of people attribute that to part of their failure against Internet Explorer. It's like making these things is not hard. Maintaining them is hard and ensuring they're robust is hard. And I think we're in the very early phases of defining what this new system for developing software looks like and I'm very excited to see what emerges.

Lenny Rachitsky (00:43:42):
I feel like we're definitely living in the future when someone like you is suggesting that we build a matrix like experience and that's going to be potentially the future of coding and building. I can't wait for that. It feels like a great opportunity and a fun project.

(00:43:57):
This episode is brought to you by Vanta and I'm very excited to have Christina Cacioppo CEO and co-founder Vanta joining me for this very short conversation.

Christina Cacioppo (00:44:06):
Great to be here. Big fan of the podcast and the newsletter.

Lenny Rachitsky (00:44:09):
Vanta is a long time sponsor of the show, but for some of our newer listeners, what does Vanta do and who is it for?

Christina Cacioppo (00:44:16):
Sure. So we started Vanta in 2018 focused on founders helping them start to build out their security programs and get credit for all of that hard security work with compliance certifications like SOC 2 or ISO 2701. Today, we currently help over 9,000 companies including some start-up household names like Atlassian Ramp and LangChain, start and scale their security programs and ultimately, build trust by automating compliance, centralizing GRC, and accelerating security reviews.

Lenny Rachitsky (00:44:46):
That is awesome. I know from experience that these things take a lot of time and a lot of resources and nobody wants to spend time doing this.

Christina Cacioppo (00:44:54):
That is very much our experience, but before the company and to some extent, during it. But the idea is with automation, with AI, with software, we are helping customers build trust with prospects and customers in an efficient way. And our joke, we started this compliance company so you don't have to.

Lenny Rachitsky (00:45:10):
We appreciate you for doing that. And you have a special discount for listeners. They can get $1,000 off Vanta at vanta.com/lenny. That's V-A-N-T-A .com/lenny for $1,000 off Vanta. Thanks for that, Christina.

Christina Cacioppo (00:45:25):
Thank you.

Lenny Rachitsky (00:45:26):
Okay. One more question along these lines and then I want to zoom out on just where AI is heading and something I love to ask folks like you that are at the cutting edge of AI is what you're teaching your kids. I know you have kids, I feel like the world is going to be very different when they grow up. What are you encouraging them to learn that you think is different maybe from previous generations to help them be successful in a world of AI abundance?

Bret Taylor (00:45:53):
I don't know if I'm teaching them differently, but I'm really trying to encourage them to make AI a part of their lives. I was reflecting actually when I took the AP calculus exams in '97, '98 AB and BC, I could use a graphing calculator. And I haven't done this research I was meaning to plug this into ChatGPT before our conversation, but I'll do it after. Did the calculus exam change before and after they allowed the calculator in the exam? I assume it did. But essentially, to when you allow the calculator in the exam, you need to make sure that none of the questions benefit people for having a calculator or not, which actually forces you to rethink the problems to test calculus knowledge that don't benefit from like road arithmetic or the other things you can do on a graphing calculator.

(00:46:47):
I think that a lot of education doesn't presume you have a super intelligence in your pocket. And so, if you ask someone to write an essay on a book that they read, you could probably hallucinate one pretty easily from one of the big providers like ChatGPT. And maybe if you are skilled enough that prompting, maybe even your teacher won't know it's written by an AI. So what do you do? How do you teach kids differently? It's really hard for teachers right now because I think we haven't gone through the transition of adding calculators to the exams. So, I think a lot of the mechanisms we have to evaluate students are broken by the existence of ChatGPT and the like. So I think we're in a very awkward phase, but I think we can still both teach kids how to think and teach kids how to learn. And I think our education system can catch up and I actually think these models can be one of the most effective educational tools in history.

(00:47:46):
I don't know if you're a visual learner or reading learner. I like to read. I didn't love going to lectures. I don't learn that well from them. I like to read the book and if you have a teacher who doesn't teach in your style, you can now go home and ask ChatGPT to teach you in another mechanism. My kids use ChatGPT to quiz them before a test. You can use audio mode or chat mode. It's better than cue cards. My daughter took home a Shakespeare book, she took a picture of a page she didn't understand and ChatGPT explained it to her way better than I would've as well. I think every child in this world has a personalized tutor that can teach them in the way that they best learn, visually, over audio, reading. We have a platform that can test you, that can quiz you. I think it's really an amplifier of agency.

(00:48:39):
I think the kids who have agency, who have aspirations to learn something, I think you have what is the best combination of every teacher you've ever had and these models and you can use it. So with my kids, my oldest daughter learned how to code and she was making a website and every time she had a question for me, I would just make her use ChatGPT. Not because I was trying to be an obnoxious father, but I'm like she needs to learn to use this tool because it's amazing.

(00:49:13):
So, I really am trying to have them learn how to use it constructively in their lives. But all that said, I just feel a ton of empathy for public school teachers right now. It's very hard because the technology is moving faster than our educational system. And I think particularly as it relates to evaluation, it's just really challenging for teachers right now. And I worry because these technologies amplify agency, the opposite can also be true. If you are a student trying to not learn something, I think these tools probably provide a lot of mechanisms to avoid it as well. And so, I think there's a challenge for parents and teachers and I think we're going to end up with a handful of years here.

(00:49:53):
But I brought up the calculus AP exam because obviously, a graphing calculator is not ChatGPT, don't get me wrong. But I think we've been able to figure out a way to conform homework and in-class learning and tests around the technologies available to us fairly successfully to date. And I'm fairly confident we'll figure it out and I think it's going to... And on the much more positive side, I don't know, I went to public schools, I don't know if you did too. You end up with some pretty bad teachers at times and now, you have an outlet. You don't need to be the rich kid who can afford a tutor anymore to get tutoring. If you are a kid who excels in math and your school doesn't have advanced statistics classes, well, now you do.

(00:50:40):
So I think this is just an incredibly democratizing force with kids who have agency and I think that's very exciting. I'm hopeful that there's a 11-year-old right now who's going to start a really amazing company 10 years from now whose ChatGPT is going to be their primary tutor that led to that outcome. And I think that's pretty cool.

Lenny Rachitsky (00:51:02):
I have a two-year-old and it feels like there's a new milestone of, there's like when to give them a phone, when to give them, I don't know, Snapchat, whatever kids use these days and then it's like when to give them their first ChatGPT account. Well no, I wonder how soon that's supposed to happen.

Bret Taylor (00:51:16):
I think my personal take is, it's different than the former two. I don't think mobile phones are great in school or great for kids and I personally advocate for waiting a long time. But I think that ChatGPT is more like Google search and it's one thing to have a device in your pocket that's addictive and has push notifications, but it's another thing to use AI to learn. And so, I think the two are different. And I really think of AI fundamentally as a utility. I don't think a lot of parents before ChatGPT said, "When should I let my kid use Google search?" That's a different type of tool. I think thinking of it like that is the way I think about these technologies.

Lenny Rachitsky (00:51:55):
Is the form factor for your kids like an iPad or a laptop or something?

Bret Taylor (00:51:58):
Yeah. They use the computer on the desk.

Lenny Rachitsky (00:52:01):
Got it. All right. Good tips. This is good for me to learn all these things as my kid ages. Okay, I'm going to zoom out and let's talk about business strategy AI. One of the biggest questions a lot of founders think about these days is just where should I build? What will foundational model companies not squash and do themselves? Being someone building a very successful AI business and also being on the board of OpenAI, feel like you have a really unique perspective on what is probably a good idea and it's probably not a good idea. How do you think the AI market is going to play out and where do you think founders should focus and also just try to avoid?

Bret Taylor (00:52:36):
I think there's three segments of the AI market that will end up fairly meaningful markets and then I'll end with how I think it's going to play out. So first is the frontier model market or foundation model market. I think this will end up the small handful of hyperscalers and really big labs just like the cloud infrastructure as a service market. And the reason for that is that creating a frontier model is entirely a function of CapEx. And you need a company with huge amounts of CapEx capacity to build one of these models. All of the companies that were startups that tried to do this have already been consolidated or almost all of them, inflection, adapt, character and others. And I think there doesn't appear to be a viable business model for a startup because of the amount of CapEx required and there's just not enough fundraising runway to get to escape velocity. And also, the models deteriorate in value fairly quickly as an asset class.

(00:53:33):
And so, you need just a lot of scale to make a return on the investment for a model that deteriorates in value so quickly. So, I think that's going to end up probably no entrepreneur should build a frontier model. That's my take.

Lenny Rachitsky (00:53:47):
Unless you're Elon.

Bret Taylor (00:53:51):
Yeah. Oh, yeah. He's different. And he has the capacity to raise billions in capital and my guess is most of your other listeners don't, and then he is the greatest of all time for reason and he's different. You don't compare yourself to him. The other part of the market is the tooling, and I think there's a lot of folks selling pickaxes in the Gold Rush. This is data labeling, services. This is data platforms, it's eval tools. More specialized models like 11 Labs has a great set of voice models that a lot of companies use that are really high quality and it's like if you're trying to be successful in AI, what are the different tools and services that you need?

(00:54:31):
There is some risk to the tooling market because it's pretty close to the sun. So, if you look at the infrastructure as a service market and the cloud tooling market like the Confluent and Databricks and Snowflake, a lot of the Amazon and Azure and others have competing products in those areas because they're very adjacent to the infrastructure itself and every infrastructure provider is trying to differentiate by moving up the stack and you're right there.

(00:54:57):
So, there's some real meaningful companies as I mentioned, like Snowflake, Databricks, Confluent and others, but there's a lot of others that were obviated by technology from the infrastructure providers themselves. So those companies probably are the most at risk for a developer day from one of these big foundation model companies releasing exactly what they do. So there's probably a lot of people who need your tool, but the question will be if or when is probably the right way to think about it, one of these large infrastructure providers introduces a competitor, why will people continue to choose you? So it's a good market but it's a little bit close to the end as I said.

(00:55:38):
Then there's the applied AI market. I think this will play out for companies who build agents. I think agent is the new app. I think that's going to be the product form factor. There's companies like Sierra, we help companies build agents to answer the phone or answer the chat for customer experience and customer service. There's companies like Harvey that make agents for both a legal, paralegal profession, anti-trust reviews, reviewing contracts etc, etc. There's companies that do content marketing. There's companies that do supply chain analysis. I think this is like the software as a service market. They'll probably be higher margin companies because you're selling something that achieves a business outcome as opposed to being a byproduct of the models themselves. They will almost certainly pay taxes down to the model providers, which is why those model providers will end up extremely large scale but probably slightly lower margin and I think the market for them will be probably less technical.

(00:56:37):
If you think about the purest form of software as a service, it's not like you ask what database do you use? It's really about the feature and function. I think that's where agents will go. I think it's going to be more about product than it is about technology over time. Just going back to my metaphor, in 1998 when Mark and Parker started Salesforce, just getting that database running in the cloud was like a technical achievement. Nowadays, no one asks about that because you can just spin up a database in AWS or Azure and it's like no problem. I think today, orchestrating an agentic process on top of the models, sounds really fancy and it's really hard and all that stuff. I'm pretty sure that's going to be easy in three or four years. It's just like just as the technology improves. And so, over time you say, what is an agent company? Well, it looks a little bit like [inaudible 00:57:30] as a service.

(00:57:30):
You talk a little bit less about how you deal with the models in the same way modern SaaS, few people ask what database you use, but you'll probably ask a lot about the workflows and what business outcomes that you're driving. Are you generating leads for a sales team? Are you minimizing your procurement spend? Whatever value you're providing, it's going to slowly evolve towards that.

(00:57:53):
I'm very excited. I don't think startups should probably build foundation models. But you can shoot your shot if you have a vision for the future, go for it. But I think it's probably a challenging market that's already consolidated. I'm very excited about the other two markets. I'm particularly excited as building agents becomes easier, to see a lot of long tail agent companies come out. I was looking at a website for the top 50 software companies in the stock market and obviously, the top five are the big, big boom ones like Microsoft, Amazon, Google, all that, but the next 50 are all SaaS companies and some of them are very exciting, some of them are super boring, but this is how the software market has evolved and I think we're going to see something similar with agents.

(00:58:38):
It's not just going to be these huge markets like we're in customer service and software engineering. It's going to be a lot of things where people are spending a lot of time and resources that an agent can just solve, but it requires an entrepreneur who actually understands that business problem, and deeply, and I think that's where a lot of the value is going to be unlocked in the AI market.

Lenny Rachitsky (00:59:00):
That is incredibly helpful. This makes me think about, I had Marc Benioff on the podcast, you guys were co-CEOs and he was extremely agent-pilled. All he wanted to talk about was Agentforce. Clearly you're also very agent-pilled. What is it that-

Bret Taylor (00:59:14):
I've never heard the term agent-pilled [inaudible 00:59:18].

Lenny Rachitsky (00:59:18):
Clearly you guys saw something that was just like, okay, we need to go all in on agents. This is the future. What is it you think people are missing about just why this is such a critical change in the way software is going to work? What are people not seeing?

Bret Taylor (00:59:31):
If you talk to an economist like Larry Summers who, on the OpenAI board with me, they'll talk about what is the value of technology? Will it help strive productivity in the economy. And if you look at one of the big jumps in productivity in the economy was in the '90s, and I think a lot of folks I talked to think it was actually that very first wave of computing where people made ERP systems and just put accounting into computers and databases, even mainframes, we're talking like the PC era. Because it was such a huge step-up, just imagine the ledgers of numbers that you'd have for a large multinational company before and it truly just transformed departments.

(01:00:14):
I'll give you a little toy example. My dad just retired. He was a mechanical engineer and he was talking about when he first started his career in the late '70s and he went into a mechanical engineering firm, the majority of the firm were drafts people. So basically, you take an engineering design but you needed to do all the different vantage points and for all the different floors and to give to the contractor to do the thing. Now, there are zero drafts people at his company. You just make the design in first AutoCAD and now Revit and it's a 3D model and the drafting has actually been eliminated. It's just not a thing one needs to do anymore. The actual design and drafting, drafting is not a thing that exists. It's just a design. That's true productivity gains, right? It's like the job of the mechanical engineering firm was to do a design. The drafting was this necessary output for the contractor, but it wasn't really adding value. It was just like the supply chain change.

(01:01:12):
If you look at the history of the software industry from the PC on, there's been meaningful productivity gains but just not nearly as meaningful as that first huge jump. And I'm not smart enough to know exactly why, but it is interesting, the promise of productivity gains from technology hasn't been as realized I think as some people thought. I think agents will truly start to bend the curve again like we did in the very early days of computing because software is going from helping an individual be slightly more productive to actually accomplishing a job autonomously. And as a consequence, just like you don't need drafts people in a mechanical engineering firm, you just won't need someone doing that thing anymore. It means they can do something else that's higher leverage and more productive and you can actually... A smaller group of people can accomplish more and truly drive productivity gains in the economy.

(01:02:15):
And I think if you've ever sold enterprise software, you end up in these discussions as a vendor with the customer where you'll have a value discussion and you'll do these somewhat convoluted things like okay, it's like you're selling a sales thing. Okay, well, if every salesperson sells 5% more... And you should pay us a million dollars. And it's roughly that conversation and it's so unattributable especially... And it's why it's so hard to sell productivity software, which I learned the hard way, it's just hard to know what's the value of making everyone 10% more productive? Did you actually make them 10% more productive or did something else change? You don't really know all these things. But now with an agent actually accomplishing a job, not only is it actually truly driving productivity in a very real way, but it's measurable as well.

(01:03:10):
So all those things combined means I think this is actually a step change in how we think about software because it does a job autonomously, which is more self-evident, a productivity driver. It's measurable so people value it differently as well, which is why I also believe in outcomes-based pricing for software.

(01:03:32):
And all of that combined to me, it feels like as significant as the cloud or I think more technologically, but just in terms of how it transforms the business model of the software industry where there's going to be a before and after. I don't know how many people still sell perpetually licensed on premises software, but it's de minimis at this point. I think we're going to go through a similar transition. The whole market is going to go towards agents. I think the whole market is going to go towards outcomes-based pricing, not because it's the only way, but the market is going to pull everyone there because it's just so obviously the correct way to build and sell software.

Lenny Rachitsky (01:04:08):
Let me pull on that last thread. So we had Madhavan on the podcast recently, pricing expert, legend, monetizing innovation author and he talked about pricing strategy for AI companies and he was very much in your camp of, if you can, you need to price your product as an outcome-based product and the access uses exactly what you shared, which is, you can do that if you can attribute the impact and it's autonomous, it's running on its own. And he actually used Sierra as one of the shining examples of this being successful. Can you just briefly just explain a little bit what is outcome-based pricing for people that haven't heard this term before and then just how does it work for Sierra to give an example?

Bret Taylor (01:04:45):
Yeah, I'll start with the example and then I'll broaden it. So at Sierra, we help companies make customer facing AI agents primarily for customer service, but more broadly, for customer experience. So if you have a problem with your [inaudible 01:04:58], you'll call or chat with Harmony, who's their AI agent. If you have ADT home security and your alarm doesn't work, you can chat with their AI agent. Sonos speakers, a lot of different consumer brands. And if you think about running a call center, there's a cost for every phone call that you take. Most of it is labor costs, but if you have, let's just say a typical phone call is anywhere between 10 and $20 USD. Some of it's software, some of it's telephony, but a lot of it is just like the hourly wage of the person answering the phone.

(01:05:32):
So if an AI agent can take that call and solve it, that is in the industry often called a call deflection or a containment. And that essentially means you saved, call it $15 because you didn't have to have someone pick up the phone. So in our industry, basically we say, "Hey, if the AI agent solves the customer's problem, they're happy with it and you didn't have to pick up the phone," there's a pre-negotiated rate for that and we call it resolution based. There are other outcomes as well. We have some sales agents being paid a sales commission, believe it or not. We do. We really think of our agents as truly customer experience like the concierge for your brand and we want to make sure that our business model is aligned with our customer's business model.

(01:06:22):
As you said, these agents need to be autonomous and the outcome has to be measurable. That's not always possible, but I think it's broadly possible. And what's really neat about it is if you talk to any CFO or head of procurement with their big vendors, they look at the bill of materials and it's overwhelming and it's impossible to know if you're getting the value that you hoped from that contract. I think consumption based, which was popular particularly in the infrastructure space is closer to it. But I'm not sure a token is actually a good measure of value from AI either. I always use the analogy, like right now, most of the coding agents are priced per token or per utilization, but there's this famous story of an Apple engineer who had a bad manager who's like had you report how many lines of code you wrote every day? Which every engineer in the world knows is an idiotic way to measure productivity.

(01:07:16):
He famously went in with a report that had a negative number because I think he did a big refactoring, deleted a bunch and it was his way of saying like, fuck you to the man. I think tokens are similar. Yeah, you used a lot of tokens, like good for you, did it produce a pull request that was good? And I think that's the whole point of all this. I think there's a huge difference between outcomes-based pricing and usage based pricing because especially in AI, they're not necessarily even correlated and you could have a long phone call and not solve the customer's problem and they give you a negative review online and call the call center again, all that effort was for nothing. In fact, you might've added negative value. And so, I am a huge believer in this.

(01:07:58):
And what's fun about it is it really just aligns... I think every technology company aspires to be a partner, not a vendor. And I think at Sierra, we are truly a partner to every single one of our customers because we're all aligned on what we want to achieve. And I think that is really where the software industry should go. It requires a lot of different shape of a company. You have to be able to help your customers achieve those outcomes. You can't just throw software at the wall because you'll never get paid if it doesn't. Your orientation becomes so extremely customer-centric when you do this the right way. I think it's just a better version of the software industry. So I think it's right from first principles, it's right for procurement partners and I think it's right for the world.

Lenny Rachitsky (01:08:43):
We've been chatting a little bit about productivity gains. There's a lot of skepticism in the headlines these days of just like what is AI actually doing? Is it actually helping people be more productive? There was a recent study actually, I don't know if you saw, where they showed engineers were less productive with AI because it was just putting them in different directions. They had to research all what's going wrong here? So I think CX is a really good example where you clearly are seeing gains. Are you seeing actual gains at your company or any other company you work with outside of CX in terms of productivity that is like clearly yes, this is working and a huge deal?

Bret Taylor (01:09:15):
I'm extremely bullish on the productivity gains from AI, but I do think the tools and products right now are somewhat immature and it's quite counterintuitive. So, for example, almost every software engineering firm I know uses something like Cursor to help their software engineers. Most people use Cursor right now as a coding autocomplete, though they have a lot of agentic solutions and there's a lot of... OpenAI has Codex and Cloud has... I can't remember the Anthropic products. So there's lots of agentic agents coming as well. One of the interesting things because the technology is immature, the code it produces often has problems. There's a lot of people approaching this to actually realize those productivity gains because as any engineer who's written a lot of code will tell you, it's pretty easy to look at and edit and fix code you wrote.

(01:10:10):
Reviewing other people's code or particularly finding a subtle logical error in someone else's code is actually really hard. It's actually much harder than editing code that you wrote yourself. So if the code produced by a coding agent is often incorrect, it actually can take a lot of cognitive load and time to fix it. And in fact, if you end up producing lots of issues with your customers, you could end up producing a lot of features, but actually, is like mucking up the machine a little bit and having something that's not ideal. There's a couple of techniques that I think are interesting. First, I think there's a lot of AI starts now working on things like code reviews. I think this idea of self-reflection in agents is really important. Having AI supervise the AI is actually very effective. Just think about it this way, if you produce an AI agent that's right 90% of the time, that's not that great, but how hard would it be to make another AI agent to find the errors the other 10% of the time? That might be a tractable problem.

(01:11:10):
And if that thing's right 90% of the time, just for argument's sake, you can wire those things together and have something that's right 99% of the time. So it's just a math problem and it turns out that you can make something to generate code, you can make something to review code and you're essentially using compute for cognitive capacity and you can layer on more layers of cognition and thinking and reasoning and produce things increasingly robust. So I'm very excited about that. The other thing though is root cause analysis. So we have an engineer at Sierra who exclusively focuses on the model context protocol server serving our cursor instance. And our whole philosophy is, if cursor generated something incorrect, rather than just fixing it, try to root cause it. Try to get it so the next time Cursor will produce the correct code and essentially, is context engineering.

(01:12:05):
What context did Cursor not have that would've been necessary to produce the right outcome? So I think people who are trying to get productivity gains in departments like software engineering need to stop waiting for the models to magically work if they want to see the gains now. And you really have to create root cause analysis and systems and say, how do we go root cause every bad line of code and actually give the right context and produce the right system so the models can do it today? Over time that'll probably be less necessary and you'll have less context engineering necessary to do it, but you really have to think of this as a system and I think people are waiting for the models to just magically get better. And I'm like, well that will happen eventually, but if you want the gains now you got to put in the work. That's essentially why applied AI companies exist.

(01:12:53):
And the work is non-trivial, but you can do it. And so, for customers using platforms like Sierra, yeah, AI agents aren't perfect, but we're creating a system that lets customers create a virtuous cycle of improvement. If you want to go from a 65% automated resolution rate to 75%, we have a billion tools to let AI help you do that, identify opportunities for improvement, figure out why people are frustrated, what new capabilities can we add to our agent to improve the resolution rate? And you let AI put the needles at the top of the haystack on your behalf and I think that's really the way to optimize these systems.

Lenny Rachitsky (01:13:28):
I've never heard of this technique of improving Cursor by adding additional context. What's the actual way of doing that? You build an MCP server that everything runs through or is it like you add Cursor rules? What's the actual approach there?

Bret Taylor (01:13:41):
I'm probably out of my depth here, but it's essentially MCP because that's how you provide context to Cursor. And I think that almost always when you have a model making a poor decision, if it's a good model, it's lack of context. And so, you really want to find the intersection of your particular product and code base with the context available to these coding agents and systems and fix it at the root is the principle here.

Lenny Rachitsky (01:14:06):
Got it. That is very cool. I hadn't heard of people doing that, model context protocol, makes sense. We've talked about productivity gains outside TX. Just to give you a chance to share how amazing what you've built is, what are some of the gains you see from people using Sierra?

Bret Taylor (01:14:18):
Yeah, our customers see anywhere between 50 and 90% of their customer service interactions completely automated, which I think is really exciting. And we serve just a really, really broad range of customers. We serve the health insurance industry, the healthcare provider space, banks. You can actually refinance your home using an agent. One of our customers built on our platform to the telecommunications industry, DIRECTV, SiriusXM to a lot of retailers as well, which is really fun. Everyone from Wayfair to clothing retailers like OluKai and Chubbies Shorts. What's really neat about it is it's a pretty diverse range of use cases and it's everything from helping you sign up for... We have an agent that helps with customer support in one of the big dating applications to helping you upgrade or downgrade your SiriusXM plan. Actually, it's really funny, we do technical support from everything from home alarm systems to sonar speakers to more recently, CAT scan machines, which I think is amazing.

(01:15:28):
So technicians going in and fixing the CAT scan machine can chat with an AI agent to help them guide them through that process. We're the leader in the space, we're trying to enable every company in the world to create their agent with their brand at the top that I think will become as meaningful of a digital touch point as their website or their mobile app. In the short term, it can really transform the costs of running a customer service team. And what's remarkable is do so with really high customer satisfaction scores. That Weight Watchers agent, I believe has a customer satisfaction score of 4.6 out of five, which is pretty amazing. And what's interesting about service too, it's often people having a problem. And so, when you have a clear, I don't know if you use them in the airport, I think that agent has a CSAT score of 4.7 out of five people are coming in with a problem and [inaudible 01:16:19] delighted. And I think that's really the opportunity here.

(01:16:22):
And our whole vision is that we're going to move towards a world where every single one of the interactions with your customers can be instant. It can be multilingual, it can be over audio, it can be over chat, it can be digital, it can be over the phone and it can be very personalized. And I think that's really, really exciting. And if you think about all the best moments you've had with a brand, it's like that store associate who you know, and it's like for me, it's like the butcher at the grocery store. I love to cook, he knows me. We talk. Can you actually produce that at scale for a company with 100 million customers and can you do it in a really personal way? And I think we're really on the cusp of enabling that.

Lenny Rachitsky (01:17:03):
Let me ask you one more question before we get to a very exciting lighting round. There's a lot of founders struggling with go-to-market in AI with their AI apps. There's so many apps these days, so many products, so many things coming at buyers, at large B2B companies. Clearly you guys have figured something out. I imagine your name helps, investors help, but what have you learned about just how to successfully do go-to-market with an AI product, say an agent-specific product that you think would be helpful for folks trying to do this better?

Bret Taylor (01:17:35):
I think there's a small handful of go-to-market models that have been proven to work, and I think it's important to choose the right one for the product category you're going after. One category I would say is developer-led. This is somewhere famously Stripe and Twilio where probably two of the original that did this exceptionally. And essentially, the go-to-market motion there is to appeal to an individual engineer often within the department of the CTO who have accountability and a fair amount of latitude to choose a solution. This works if your product is a platform product. It doesn't work, for example, if your product is trying to help a line of business because lines of business typically don't have dedicated engineering teams or let alone, the latitude to just go download a new library or start using a web service like that. It particularly works well if you sell to startups just because startups tend to have engineering teams with quite a bit of latitude to choose services to help them solve the problem given by the founder.

(01:18:44):
Then there's product-led growth. It's a broad term, obviously every company's product matters, but product-led growth more specifically means users can sign up from the website, often get put on a trial. Often you can buy a couple of seats with a credit card and those work where your user and your buyer are the same person. So it works for small business software almost always because sole proprietors do everything. And so you're selling small business software like Shopify in the early days and there's a lot of other products like that where you're trying to sell to small merchants. That's great. It doesn't work well when your buyer and the user of the software are different. So I'll use the example of something like expense reporting software. The user of that software is an individual employee, but the buyer is often a finance department. And so having sign up and buy with your credit card doesn't make sense because the person using is not the person with the credit card and it just doesn't work.

(01:19:39):
And then there's direct sales. And direct sales had gone, I don't want to say out of fashion, but if I think of the best direct sales companies, probably there's a lot of lineage from Oracle, but you think SAP, Oracle, ServiceNow, Salesforce, Adobe perhaps, and there's others as well. And these were companies that sold into large lines of business in a relatively traditional sales motion. I think because product-led growth became very popular. I think a lot companies use that, which is great, that motion produces great products, but if PLG means that you aren't actually engaging with the buyer of your software, you're not going to grow. And so, I've actually seen more recently, with a lot of AI companies, direct sales come a little bit more back into fashion because I think so many of the opportunities in AI actually meet that qualification where the buyer and the user are not necessarily the same person and it really requires that go-to-market motion.

(01:20:40):
Where I see entrepreneurs stumble is they'll choose a go-to-market motion without thinking through what is the process of purchasing this software? What is the process of evaluating the value of this software? And I think people just need to be much more first principles about it and much more thoughtful about it. And candidly, I think a lot of companies should leverage direct sales more than they do. And even though because of the sometimes justified reputation of the quality of products of some of these direct sales companies, it had gotten a bad name. And I think I'm thankful to see it coming back in a lot of the AI market.

Lenny Rachitsky (01:21:20):
I feel like this message is something a lot of founders need to hear, especially founders that aren't from a business background that sales turns them off, they don't think they're going to be great at sales. Just this push of this might be what you have to get really good at and this is how you win and you can't just rely on product like growth.

Bret Taylor (01:21:36):
Yeah.

Lenny Rachitsky (01:21:38):
Bret, is there anything else that you wanted to share? Any last nugget of wisdom? Anything you want to double click on before we get to our very exciting lightning round?

Bret Taylor (01:21:47):
No, go ahead.

Lenny Rachitsky (01:21:48):
Okay, let's do it. Here we go. Welcome to our very exciting lightning round. I've got five questions for you. Are you ready?

Bret Taylor (01:21:53):
Yeah, go ahead.

Lenny Rachitsky (01:21:54):
What are two or three books that you find yourself recommending most to other people?

Bret Taylor (01:21:59):
I don't read a lot of nonfiction, but probably if I had to pick one in the area of the topics we talked about, Competing Against Luck, which was the book that produced Jobs to be Done, which is a framework I really believe in. My only critique is I think most of these business books should be like an article. So maybe buy the book and punch it into ChatGPT and get the summary. But buy the book it's Clayton Christensen talked about it, but it's a really good framework for thinking about delivering value with your products. And I think it definitely influenced me.

(01:22:37):
Actually one book I do recommend is Endurance, which is the story of Shackleton's trip to go to the South Pole. Half the book is him starving to death and eating seal meat with his crew of people frozen in their boat. I've never seen a better story of grit in my entire life. It's remarkable that it's a true story and if you're an entrepreneur going through a hard time, read that, you'd be like, okay, it could be worse. It's a great book too. It's just remarkable that it's a true story.

Lenny Rachitsky (01:23:08):
And one thing he did a great job at is setting expectations for folks that joined that famous newspaper-

Bret Taylor (01:23:13):
That ad. That newspaper ad. I don't know if that's true. It's remarkable if that's true.

Lenny Rachitsky (01:23:17):
Oh, it might not be true.

Bret Taylor (01:23:17):
I don't know. The internet. Who knows?

Lenny Rachitsky (01:23:20):
Goddam. Deep fakes even back then. Okay. Do you have a favorite recent movie or TV show that you've really enjoyed?

Bret Taylor (01:23:27):
I haven't gone to any new TV shows recently? We just watched Inception with the kids and they loved it and made me appreciate Christopher Nolan and what a cool movie. It's the type of movie when you watch the film and you can a conversations for two days afterwards about it. So, just a great film.

Lenny Rachitsky (01:23:46):
I saw someone using I think VO 3 to create their own Inception videos where the worlds wrapping in on each other. Oh, man. Okay. Do you have a favorite product that you have recently discovered that you love or one you've loved for a long time?

Bret Taylor (01:23:59):
I'm really a big fan of Cursor. I think it's changed. I love creating software and I'm excited though for agents. I've been really excited. I was very excited to see Codex from OpenAI and others. So I think Cursor will be in its current form, is a transition product. And I know they're working on agents as well, but I really enjoyed taking something I love and it's been my life's passion and really diving into this AI tool and seeing how it transforms how I create software. So I've just been spending a lot of time with the product just because it's so core to what I love to do and it's a really well crafted product.

Lenny Rachitsky (01:24:39):
I think that's the first time someone's actually mentioned Cursor in this answer, so might be the beginning of a trend. Michael Trell was on the podcast and he actually had a very similar message as you had at the beginning of this chat about the future of code, what comes after code and this concept that there's going to be this additional pseudo code layer on top of code. Very aligned with your thinking. Do you have a favorite life motto that you often come back to and find useful in work or in life?

Bret Taylor (01:25:05):
The best way to predict the future is to invent it, which I think I attribute to Alan Kay of Xerox PARC. He invented a lot of the core abstractions that we use in computing today. I'm an entrepreneur, it's why I love to build things and it's definitely a life motto for me.

Lenny Rachitsky (01:25:29):
I feel like many people say this, I feel like you've actually done this so many times. You're really living this motto. Final question. We talked about you inventing the like button at FriendFeed. Were there other thoughts of what they would call it other than like? Was it just obviously like? Or was there other thinking there?

Bret Taylor (01:25:48):
This was before emoji. So, if you read the comments on FriendFeed posts, at least 70% of them are cool or wow or yeah or neat. And one of the principle uses of FriendFeed was to have discussions about things. So you'd have a post and then a pretty fulsome discussion underneath. And compared to Twitter and others, it was a great place to have those discussions. And so, the product problem we were trying to solve is get all the one word answers out so that the discussion was actually actual comments as opposed to acknowledgements that you read the thing.

(01:26:30):
So, the original framing was one click comment. That was how we thought about it. And so, the first version that I made had a heart, and she denies remembering this, but Anna Yang, now Anna Muller who has worked at the company, she hated it. She said, "If I look at hearts on every post, I'm going to vomit. It's too much." And it also was interesting, we were simulating, it was like an article about a tragedy or something. A heart was just not the right thing. Like which actually turned out to be really hard to translate was just a much more neutral sentiment, and that's why it was hard to translate because it was subtle. So that's how we ended up with this.

(01:27:17):
We started with a heart, and I don't know if we ever heard the word love, but we definitely started off with the iconography and then like, which just felt like this positive yet as neutral as possible within the realm of positive so that it could work for a more complex story. But it was all because we needed a one-click comment. That's where the concept came from.

Lenny Rachitsky (01:27:36):
Wow. I've never heard the story before. It makes me think about LinkedIn now. They're basically trying to solve that same problem. They have all these auto-reply pill tag things. I don't think people like those very much.

Bret Taylor (01:27:37):
Yeah. They have a lot of features.

Lenny Rachitsky (01:27:48):
So many AI features. Bret, this was incredible. This was an honor. I so appreciate you coming on this podcast. Two final questions, where can folks find you online if they want to reach out, maybe go see if they want to work at Sierra and how can listeners be useful to you?

Bret Taylor (01:28:00):
If you want an AI agent to help with customer service, go to sierra.ai. If you want to apply here, sierra.ai/careers where we have offices in San Francisco and New York, Atlanta and London and are hiring pretty aggressively in every department. So please reach out if you're interested.

Lenny Rachitsky (01:28:19):
And how can listeners be useful to you? Is it tryout Sierra, anything else there?

Bret Taylor (01:28:21):
Yeah, tryout Sierra. I'm a single issue voter.

Lenny Rachitsky (01:28:26):
[inaudible 01:28:26] message. I love it.

Bret Taylor (01:28:26):
Yeah.

Lenny Rachitsky (01:28:27):
Bret, thank you so much for being here.

Bret Taylor (01:28:29):
Yeah, thanks for having me.

Lenny Rachitsky (01:28:30):
Bye, everyone.

(01:28:32):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at Lennyspodcast.com. See you in the next episode.

