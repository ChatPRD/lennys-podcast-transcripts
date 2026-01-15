---
guest: Austin Hay
title: The ultimate guide to Martech | Austin Hay (Reforge, Ramp, Runway)
youtube_url: https://www.youtube.com/watch?v=B79p85DHLkU
video_id: B79p85DHLkU
description: 'Austin Hay is currently Head of Marketing Technology at Ramp and was
  previously the VP of Business Operations at Runway, the VP of Growth at mParticle,
  and the fourth employee at the unicorn...

  '
duration_seconds: 5077.0
duration: '1:24:37'
view_count: 15343
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- onboarding
- metrics
- mvp
- experimentation
- analytics
- funnel
- conversion
- revenue
- hiring
- culture
- leadership
- management
---

# The ultimate guide to Martech | Austin Hay (Reforge, Ramp, Runway)

## Transcript

Austin Hay (00:00:00):
From 2010 to 2020, we had the golden years of deterministic matching where it was very easy to run an ad and understand with precision who installed the app. Maybe you didn't know their name, but you actually would know their IDFA and you could tie that to their PII. You can't do that anymore. So, what that means is these ad networks are becoming more complex, sophisticated, and interesting, right at the same time that it's harder for marketers to really understand how they're spending money. And so I am paying a lot of attention to how marketers make decisions with probabilistic data because most of the work that I'm doing now is actually saying, well, given that we don't have determinist data about a per certain audience or where somebody came from, how can I find other information that will create a model for 30% of the population and we can use that to extrapolate to a hundred.

Lenny (00:00:52):
Welcome to Lenny's Podcast, where I interview you world-class product leaders and growth experts to learn from their hardwood experiences building and growing today's most successful products. Today my guest is Austin Hay. Austin is one of the smartest people in the world on the field of MarTech, aka Marketing Technology. He's advised companies like Notion, Airbnb, Walmart, Postmates, Robinhood, even Pete's Coffee and Mars on their MarTech strategy and tactics. He's currently head of marketing technology at Ramp. Before that, he was VP of business operations at Runway. Before that, he was VP of growth at mParticle and the fourth employee at the Unicorn Branch Metrics. He's also a teacher at Reforge on this very topic of MarTech. In our conversation, Austin explains what exactly is MarTech, how it fits into your growth organization when you need to hire a MarTech person and what to look for plus his favorite interview questions.

(00:01:43):
Also, his favorite tools, frameworks, team structures, and emerging platforms that he's most excited about. This episode is for anyone who's responsible for growth and is curious about ways to optimize your approach and how marketing technology fits into that. Enjoy this episode with Austin Hay after a short word from our sponsors. Today's episode is brought to you by OneSchema, the embeddable CSV importer for SaaS. Customers always seem to want to give you their data in the messiest possible CSV file. And building a spreadsheet importer becomes a never ending sync for your engineering and support resources. You keep adding features to your spreadsheet importer, but customers keep running into issues. Six months later, you're fixing yet another date conversion edge case bug. Most tools aren't built for handling messy data, but OneSchema is.

(00:02:28):
Companies like Scale AI and PAVE are using OneSchema to make it fast and easy to launch delightful spreadsheet import experiences from embeddable CSV import to importing CSVs from an SFTP folder on a recurring basis. Spreadsheet import is such an awful experience in so many products. Customers get frustrated by useless messages like error on line 53 and never end up getting started with your product. OneSchema intelligently corrects messy data so that your customers don't have to spend hours in Excel just to get started with your product.

(00:02:59):
For listeners of this podcast, OneSchema is offering a $1,000 discount. Learn more at oneschema.co/lenny. This episode is brought to you by Mixpanel. Get deep insights into what your users are doing at every stage of the funnel at a fair price that scales as you grow. Mixpanel gives you quick answers about your users from awareness to acquisition through retention, and by capturing website activity, ad data, and multi-touch attribution, right in Mixpanel, you can improve every aspect of the full user funnel. Powered by first party behavioral data instead of third party cookies. Mixpanel is built to be more powerful and easier to use than Google Analytics. Explore plans for teams of every size and see what Mixpanel can do for you at mixpanel.com/friends/lenny. And while you're at it, they're also hiring. So, check it out at mixpanel.com/friends/lenny. Austin, thank you so much for being here. Welcome to the podcast.

Austin Hay (00:04:03):
Lenny. Thank you so much for having me.

Lenny (00:04:04):
We are going to get super nerdy today and we're going to dive deep into the very cool field of MarTech. How excited are you about us chatting about MarTech?

Austin Hay (00:04:15):
I'm so excited. Because it seems like you might be one of the first people in product and growth to talk about MarTech.

Lenny (00:04:21):
Wow, okay. That makes me even more excited. Yeah, it's something that I haven't fully understood and so I'm excited to dig real deep. So, let's start with just the basics. What exactly is MarTech and then what does someone who is in MarTech do?

Austin Hay (00:04:35):
Such a good question. Because marketing technology is like this very amorphous, cross-functional discipline that lives at the crossroads of product and growth and engineering and marketing. It brings together processes and systems from a wide range of disciplines. And I think really the way to think about marketing technology is it's a product manager whose specific role and focus is the system or the third party or first party platform because marketing technology can mean a collection of third party tools, which is a lot of people think, but as a company scales and grows actually it could include a collection of first party homegrown solutions that you build yourself with or in addition to third party. So, I like to think about marketing technology more as one piece is people and process and the other is the system and the platform. And that probably sounds pretty familiar to what a lot of product people think about their world as, and that's how I define MarTech.

(00:05:31):
And then you asked this other question around what exactly the role of somebody in MarTech, and maybe we'll talk about this a little later, but it's such a function of the size and the stage of the company that you're at. At Airbnb, I would say Dmitri who you might've worked with was the MarTech guide. He managed a lot of our Airbnb's, the first and third party tools. Airbnb at that size was, I don't know, maybe 800 people or so. And so it makes sense to have a function with product and engineering resources. A small startup for example, when I was working with Siqi, we were just talking about this at Runway, there was no such thing as MarTech. There was me and Tanner and Siqi standing up tools and using them because you just have to use the tools to get the job done. And so I would say on the spectrum of what is MarTech, you really have to look at the size and the stages of the company and as you grow you start to see it become more refined or pronounced.

Lenny (00:06:17):
So, if someone listening to this that has done growth or has a growth PM may be like, oh, but this is sort of what I do. What is the difference between someone that just runs growth or has a growth team versus someone that's specifically a MarTech person?

Austin Hay (00:06:30):
At some levels there's maybe no difference. There's a lot of startups I would say are 30 people or less where you have a growth team and your growth acquisition person is using a CDP to send data to their ad network to run their ads because that's part of their job and maybe they are the MarTech person. And actually you find a lot of people who consider themselves MarTech professionals now having started in growth or user acquisition roles because they had to just use tools in order to get their jobs done. But what I would say is as a company grows and scales, it moves from being a community or village driven aspect of your products to being something that's centrally owned. If you're a startup, again, like 30 to 40 people, everybody might chip in to manage your CDP or use Amplitude or build a first party solution on top of those.

(00:07:16):
It's a mixture of first and third party tools and engineering and product and marketing all work together on it. That doesn't scale though. As you cross a hundred to 200 people, somebody has to be responsible for knowing how data flows through tools, how it's worked, what's the schema. And that's not even considering procurement and legal stuff. You have infinite liability if you don't manage your contracts well. And so usually around I would call it a hundred to 150 people is the critical mass where you can't just have a village approach to systems and tools much like in the IT org, if it was a village approach to SSO businesses would be in a lot of danger. That's where you typically start to see the question of, all right, we need a systems and tools person. We need somebody to manage these systems and manage that platform.

(00:08:01):
And there's a variety of ways it can go. I've seen it go just into pure product that's with a product operations org and a product ops person actually will manage a lot of third and first party tools. I've seen it go into the IT org, Walmart for example, at a really big scale. They had a MarProd function which was marketing products. It was product within the marketing function or product that was designed to serve marketing. And then of course you can have more traditional routes like you can have marketing technology as a single standalone unit or business technology as a standalone unit. Some of this depends too on whether the business is B2C versus B2B. Classically in a B2B business you see it in rev ops or some types of systems role because you have to serve not only users coming into your funnel, but then the businesses that you're serving afterwards.

(00:08:46):
That's also where you typically see tools like Salesforce coming into play and more advanced CRMs. In a B2C business, your user funnel is actually really simple acquiring users and you're getting them into your product and then product is taking them over. There's no additional CRM, so usually your CDP is the source of truth and that's where you might actually see marketing technology fit in with growth a lot more. Just some examples like at Postmates, I worked for them for a long time as a consultant. Marketing technology was just part of growth. We had a director of growth even before that, Siqi Chen who's the CEO of runway, and I guess you were his first manager as I just learned, he was the first VP of growth and marketing technology was just part of growth and product owned that as a system.

(00:09:30):
As a different example though, at Ramp we're big enough and we're a B2B company, but we have a B2C top of funnel where we try to acquire users and get them to fill out our application to get a credit card. We have a distinct revenue operations team that's broken into business technology and marketing technology. So, there's lots of flavors of how it can exist. I think that's kind of the interesting and fun part of Marketing Tech is that it's not just one single version of the world that you apply to many companies, there's like a million variations that I've seen and they all kind of look to solve the same problem.

Lenny (00:10:00):
So, to make it even more specific and really simple for people to think about what someone in MarTech does, essentially it's using technology and tools to drive growth. Is that a simple way of thinking about this one specific roles?

Austin Hay (00:10:11):
Totally. That's exactly right. And I have this adage I always say, which is tools are just meant to solve problems. And the problem set for marketing technologists and business technologists is you focus on the tools.

Lenny (00:10:24):
And so when someone currently say listening doesn't have a MarTech person and they're thinking about, hey, is this a gap we have? What is that slice of work that a MarTech person would take if they currently have say a growth team or a growth PM that's leading growth and a growth team around them?

Austin Hay (00:10:40):
This comes up all the time, by the way, I talk to businesses every year that have this problem of we have a growth team, we're growing pretty fast. We have a guy that we hired, usually an engineer who stood up all these tools for us. Or it could be gal too just to be clear, but this person has been here for two years and knows all of our systems really well, but now they're becoming overwhelmed. They don't have enough time. The systems are too complex. This is the flavor of story that I hear so often around startups who have hired a great growth person and managed tools and systems, but at some point they reach that point in time where it's no longer manageable by one person or even a set of people. And that slice of works looks like setting up new tools, building new tools on top of them because a lot of times you'll take a third party tool, call it like a segment or an amplitude, and you'll build tooling in your own stack behind it to power something much more advanced.

(00:11:35):
And everybody thinks that marketing technology is just the third party tools, but actually it's designing, architecting and building that stuff on top of your third party tools. That's how you actually have a lot of velocity is thinking about not just build versus buy. It's build and buy now. So, you buy the tool to get 90% of the way there and then you build the cool thing on top with the other 10%. And so that architecting decision usually falls on this person. The one really unsexy part of it, which I tend to love because it's really high leverage is the contract part. When you start out as a business, you sign any contract you want with a third party because you're just trying to get going. You have much bigger problems, product market fit, staying alive, runway. But at some point as you scale and you're starting to make money, now you start to care more about not just how much money you're making but how much money you're losing usually from contrasting SaaS tools.

(00:12:24):
And so that's where you start to have more scrutiny around what types of deals are we signing, what are the terms? Do we have liability exposure? What's it going to cost us if we actually scale? And it's great that we have this cool rate at 500 MTUs, what happens when we have a million MPUs? So, I worked at mParticle, which was a CDP provider for a long time and I was their VP of growth and part of their SaaS vendor strategy is like, how can we design these cost structures in a way so that at the company scales we make more money? That's just part of the business. And so if you have that mindset of, well, I'm looking out for the business not just now, but two 30 years in the future, that's where you can also have a lot of value from a systems or marketing technologist.

Lenny (00:13:05):
Maybe a sign that you should start thinking about a MarTech person on a growth team is what I'm hearing is you're starting to accumulate all these different tools and maybe there's a sense that you could be a lot more efficient in connecting data and the backend infrastructure for how you think about growth and how you drive growth and measure growth.

Austin Hay (00:13:24):
Yeah, efficiency and pain. I would say pain drives people more. It's like, hey, we can't do something because nobody knows this thing. We can't do something because we don't know the best way to set up these tools or to change these tools or we can't even move forward where a business plan because we're worried that changing our tools might have an impact. And usually this is related to email marketing tools and data tools, so like CDPs and folks like Braze interval and just because a lot of times your email is the thing driving recurring customers to come back to your product and use it. So, you can't actually sometimes make the changes you want without understanding how something was set up in the first place.

Lenny (00:14:03):
You talked about where this person would live in the organization. There's all these different places. I talked about revenue team, maybe the ops team, maybe growth team, marketing team. What's your general advice for who should lead the hiring of this role and also just roughly who should they report to?

Austin Hay (00:14:21):
So, I have not to shamelessly plug my Reforge course in the fall, but I'm going to be shamelessly plug my Reforge course in the fall. We have this awesome matrix that we built that shows where this person should live, what they do, who they should report into, and it's all part of the fall course if you want like the deep dive into it. There's going to be a section on it, but just the gist of it is I first like to break it down into two dimensions. First is a B2C company or B2B company. And then the second dimension is how important is it to you that this person report into a specific function or not? So, first with B2C and really maybe a simpler version of that is centralized versus decentralized. So, we have B2C, B2B, centralized, decentralized. In a B2C organization I think actually thinks it's quite simple.

(00:15:08):
Most of the time your tools, your marketing tools are intended to help the growth team. The growth team has a job to be done, which is to spur user growth and tools are just meant to solve the problem. So, marketing technology's job is to serve the growth team. Now it obviously serves product and analytics and data, but its key stakeholder and customer is the marketing or growth function. And so I think it makes a lot of sense that if you're designing an org under a CMO or a marketing person, you put marketing technology alongside your head of growth or maybe reporting into your head of growth depending on the seniority of the person. And that works quite well. The key thing there is you just want to make sure that this marketing technology person is a really strong technical architect or some type of technical operator because they're going to be your representation to the product in engineering orgs.

(00:15:53):
Now, some people take a little bit of a slight twist on that. They say, hey, I have a product manager who manages growth that comes from the PM side. You could have a platform PM that serves the same thing in MarTech and they're responsible for all internal platform systems. And then you get into questions of does that belong in product ops or not? And I'm not going to go there. But for B2C, that's the centralized function. For B2C decentralized, what you do instead is you just say like, hey, we're going to have one of these systems, people in every org. Product is going to have a product ops person and growth is going to have a growth ops person, engineering will have engineering ops, and then we kind of divide the lines based on what tools they're managing. I generally don't see that working very well just because as you add more operational people, it just creates more systems.

(00:16:39):
And so unless you're a massive company where you need that type of scale, I think most startups should avoid that decentralized model. And then for B2B, I think B2B is really messy because not only do you have pure B2B where you're only selling to enterprises, but you have this concept of B2B2C, which is where you're actually selling to users and to businesses sometimes at the top of the funnel and the bottom, but also sometimes at the same time like notion. Notion sells to users so, they have a little growth acquisition funnel at the top, but then they also sell to businesses. And I find there's really, again, there's two ways decentralized or centralized actually at Ramp we've gone back and forth between the two models. We started centralized with the Rev ops group, we decentralized it and put marketing technology into the CMO org and now we're rolling it back into the revenue operations org Largely has to do with who is our customer?

(00:17:28):
Whose problems are we solving and where are resources allocated? Because if you have a decentralized model, then you run the risk of having to have lots of resources decentralized across the team. And the question is, can that function actually get work done or resources spread too thin and the priorities on align that it makes it challenging to get work done. And yeah, I would just say especially on B2B, for people out there listening, there is no right answer. And I even think that marketing technology could live in product, it could also live in engineering. Some of this has to do with who is the leader of this function. If it blends more towards ops, meaning managing processes and systems, then yeah, maybe you want to decentralize it and keep it in its representative function. If you have a really technical leader who was an architect or a PM that might indicate where that person should actually be leading their team. So, it's very case specific, which I know is a terrible answer, but it's the way it is.

Lenny (00:18:25):
Makes total sense. If someone were to hire someone like in Austin, are you doing the work yourself? Are you an IC for quite a while or do you end up building a team, say engineers that are building some of this infrastructure, how does that usually play out?

Austin Hay (00:18:38):
I think all marketing technologists at some level are ICs. I think it's a great job personally, because I get to be an IC and a manager. You have to be an IC in that, you are the most senior technical expert on all first party and third party systems. So, you have to know really well how third party tools work and you don't know that without doing the work yourself. So, I do find that some of the best marketing technologists have at least at some point in the last five years, been an operator and expert managing tools and systems. And then usually the teams are small and super cross-functional.

(00:19:10):
So, what I would say is more important to look for than how many people has this person managed is how well can they manage upward, laterally and downward because they're going to have to go talk to the head of rev ops if they want to change something in Salesforce, they're going to have to talk to the VP of product if they want to make a big platform change that touches something else. They're going to be relying constantly on data resources from their head of data. So, I think that this person, the secret sauce is more of how good of a cross-functional team player are they. I almost view them like a true quarterback every [inaudible 00:19:41] says people are quarterbacks. But really marketing technology because it lives between so many departments, it plays that role of having to call plays and pull on different departments.

Lenny (00:19:50):
And because it sounds like you don't have a team to do some of these things and you need to convince people to help you out.

Austin Hay (00:19:56):
Totally. Yeah. It's a game of persuasion and salesmanship. You have to convince people why the problems are big and especially as you get bigger, a lot of the decisions or problems of marketing technology are not about rapidly making a huge transformation. It's slow transformation that can have big implications. I'll just give you one example. Like lots of big companies I talked to have two CDPs or two attribution tools and it's like there's the cost problem. How do we get rid of this secondary tool to reduce the cost? Maybe it's a million dollars, but there's also the complexity and decision-making problem. How do we make people move and work faster by not having the complexity of asking, which tool do I use in such a simple decision?

(00:20:39):
And then you get to a really big scale at Walmart where your problem isn't even. How do we consolidate the stack and make it so tools that are helpful for people, but how do we prevent from getting back to that state? How do we put safeguards in place to make sure people actually have access to the tools that they want and can solve their problems? But we're not introducing duplicative tech into our organization because a really well-known, sorry to put SaaS vendors on the spot here, but well-known SaaS vendor plays the land and expand motion. You get in small and then you grow your business. Well, that's a distinct problem for businesses that are trying to control costs and simplify the way the world works.

Lenny (00:21:15):
I want to talk about tools that you recommend and use most often, but I'm thinking maybe we start with a different question, which is around just what does your day look like as a MarTech person? What are you doing day to day and from the lens of your growth PM listening or a leader listening and what could this person do for me and how much leverage can I get if I were to find a MarTech person?

Austin Hay (00:21:37):
There's half of marketing technology, which I would call somewhat administrative and high leverage. It's managing PI requests and PI technology, managing administrative stuff like contracts and admittance to tools and permissions. This is all at a big company scale. You probably don't do this when you're a small company, but that stuff matters because give you an example, you give edit access to somebody who wants HubSpot and they send a fake email test to a million people and now you're on Twitter being embarrassed as a company. It's like-

Lenny (00:22:12):
Does that happen to you?

Austin Hay (00:22:13):
It hasn't happen to me. But I've gotten the emails from certain companies where it's like, this is a test and it came from an intern.

Lenny (00:22:20):
Yeah, same.

Austin Hay (00:22:20):
You're like, that's just permissioning gone wrong. So, I think a big part of the role is designing systems that are automated to handle that stuff because ideally you don't want to be sitting around in your computer all day clicking one conductor request to approve permissions. You should look at the role, look at the experience of tenure and department and make a decision about which accesses you get. So, automating that is a big part of my job. The manual part of my job, which I feel like is actually really fun, is again the designing systems and contracts for the future. So, it's about how do we design a system and create a vision and persuade people about what our system technology can look like over the course of one to two years, the time span that I usually look at. And then how do you change state from then to now? Some of that has to bring in financials and contracts. That's where this plays a role. What are our contract terms today? What's the price we're paying? What is our growth going to be?

(00:23:12):
Can we build a financial model to show how much it's going to cost us both in terms of operational efficiency and actual real fixed and variable costs to end up in that state? And then how do I create a graceful argument to persuade people that we should spend engineering time and resources? And usually it nets out pretty clear. It's like if it's less than a certain amount, how do you justify spending any engineering time on it? You have to wait for the problem to become big enough. But then back to your other point around how do I give growth managers out there something useful. I would say the big thing that people forget in an early stage of a company's lifetime is that the company will outlast you, hopefully. You will not be the last growth manager unless the company fails. So, I tend to take a little bit of a different approach than most, which is like I think you should always be thinking about the future.

(00:24:02):
That doesn't necessarily mean you should make design choices that over index towards the future so much that you miss product market fit or you make poor product decisions. But when you set up tools and you pick tools and you implement them, you should be thinking, what's going to happen a year from now if I don't change anything? And is this going to be a catastrophic situation or not? And then try to take actions to mitigate that risk. Some examples are like if it's $2,000 to get SSO and two days to set it up and that prevents you from having a security problem where somebody downloads all your users, it seems like a great investment.

(00:24:37):
And guess what? Over time, if you don't do that, you're going to eventually have to hire an IT person to go and set up SSF for all your tools. So, some of this is more of just being a good steward about managing first and third party tools with an eye towards the future. It's always a trade-off, right? Because the more time you spend when you're building product early in a company's lifetime, that time could be spent on other things. So, if you waste it managing third party tools or setting up correctly, then maybe you miss out on a key product feature. So, I think it is a tough balance to strike.

Lenny (00:25:06):
Coming back to the different kind of roles within the growth umbrella, if someone has someone leading paid growth let's say, and they're just like a paid growth person, do you also find a MarTech person to work alongside this person? How connected would you be to someone that's just responsible for paid growth?

Austin Hay (00:25:24):
Maybe a key differentiator too. We didn't talk about this in the beginning, but there's marketing technology and marketing operations. So, in my mind, this is just my own kind of mental framework is marketing technology has tech in it. So, it's usually an engineer or somebody with an engineering background doing that function. Marketing operations is usually not always technical. Maybe a systems analyst or business analyst could be somebody really, really smart, but they may not have an engineering background. So, I think that's a key distinction too. And you typically see that in B2B where you'll have mar ops function, which is setting up campaigns, sending email blasts, debugging, doing analytics work, SQL queries, all semi-technical work but not engineering based. So, in my mind when we talk about marketing technology, I'm really thinking it as an engineering based role and even by background, I'm not a software engineer, but I was a civil engineer and I learned how to program and I went through a bunch of coding to get there.

(00:26:21):
So, that's my way into the engineering world. And you typically find that a lot with marketing technologists in particular is they either are software engineers or they've gotten enough experience to moonlight as software engineers. And so we get to this problem set of a user acquisition person. How would they rely on a marketing technologist? Well, I think the most superhuman user acquisition people out there are engineers and they don't need a marketing technologist because they set up the tool themself. They know how the paid campaign runs and they just do it all. And you'll typically find these super humans at small startups where the engineer is just told by the co-founder, hey, go figure out how Facebook ads work. And superhuman is born. More often though that doesn't happen. Or those people once they do it once, they never want to do it again. So, you'll typically find the role split and that's the natural thing that happens.

(00:27:13):
As you scale, you divide responsibility and you'll see you'll have the person who's responsible for bidding and acquiring users and paying down those campaign costs. Then you have the person who's in charge of how does it all work? How do we get this thing to actually run? And that's very similar to what we have at Ramp. We have an amazing user acquisition team. I know Sri Batchu was on here a while back. He hired a guy named Cody Morgan at Ramp who has a user acquisition team. And the way to think of it is, my job is to help support them in running all their campaign needs and when they have a directive from the CEO that says we need to improve CAC or change any of our metrics, it's my job to partner with them to help them do that. And actually one of the coolest and most fun projects that we worked on early when I joined Ramped is we were optimizing.

(00:27:55):
We're trying to get top of funnel data all the way down to the bottom of the funnel and tie it with opportunity data so we could send that back to the ad network so that rather than optimizing your campaign off of when a user clicks a button on the website, you're actually optimizing it off of did the opportunity occur and what was the kind of ideal value for that opportunity? And you're sending that data as a synthetic event back to Facebook and all those guys. So, it can be really cool and super advanced stuff depending how deep on the funnel you get and how complex your business is.

Lenny (00:28:25):
So, you're generally not running campaigns of your own unsafe Facebook or AdWords. You're mostly as a MarTech person supporting people who are doing that.

Austin Hay (00:28:34):
Yeah.

Lenny (00:28:35):
Awesome.

Austin Hay (00:28:35):
Helping them use tools and technologies to do it.

Lenny (00:28:38):
Great. Do people give you goals? Are you responsible for growth goals of your own? And in general, are MarTech people, should they have goals and growth goals on their plate or are they just there to support people who do?

Austin Hay (00:28:52):
Oh, that's a great question and I would like, maybe this is at the end of the podcast, we ask people about this because I would love to know what is a better version of goaling? So, there's two ways that I've thought of it. One is my goals are directly tied to the people I'm serving. So, if user acquisition has, I mean we do, we have a growth goal and we have a CAC goal at Ramp. So, my goals are tied to them, so I'm going to help make sure that that is achieved, but then there's also a cost and efficiency goal that I internally think is valuable. Whether or not the business thinks it is valuable, it doesn't really matter. I come from a sales background and I like to run lean and efficient teams, and so I'm always thinking to myself, how much were the tools when I came in, how much are they now?

(00:29:34):
Have I set us up for success so that as we grow, our cost per user or cost per seat comes down and how much more efficient are we because of that? The ideal world is that you actually are growing as a business making more money, hiring more people, acquiring more users, and your total cost of tooling per person goes down. That's like the dream. And there's lots of ways you can build that financial model, but I mean that's what I think most marketing technology leaders should strive for is to make sure that they're controlling costs over time because most businesses don't. There can be some goals that are discreet in nature that are not cost-efficient, but more like net capability related. So, it's like, hey, we want to design a first party system that's world-class that achieves these three goals, right? Maybe you want to incorporate artificial intelligence into some part of our product platform and incorporate third party tools.

(00:30:25):
And those are more like discrete product goals. In the same way that a business might launch an external product goal to launch a feature, they sometimes also might have internal product goals, clean up our revenue operations systems, make our email marketing system better. In particular, email marketing is one I see come often a lot with small businesses and even medium-sized businesses where they'll have picked a tool at the start of the company's lifecycle and as the company has grown, they've outgrown that tool. They need to move to a Braze or Marketo. And so there'll be a big six-month initiative to say, we just got to switch. That's the goal. We have to safely get off this small tool to a much bigger, more complex tool that's going to cost us more. It's a lot more complex, but we need to do it without losing money. That's usually the job of a MarTech person in some type of change transformation effort.

Lenny (00:31:14):
Perfect segue to where I wanted to go, which is tooling and your recommendations and favorite tools. And so maybe we start with just what do you find as a good starting tool stack for people starting to think about MarTech and basically growth, and then what does it end up being generally?

Austin Hay (00:31:32):
In terms of stack, again, we think about B2B and B2C. B2C I would say the stack was largely solved from 2017 to 2020. We've had like a renaissance of the data architecture, so what I'm going to do is I'm dig through B2C then and now and then we can go B2B then and now.

Lenny (00:31:52):
Great.

Austin Hay (00:31:52):
Okay. So, B2C, if you back up to 2016, 2017, you have segment and the rise of the CDP. Consumer based businesses have to collect a user and tie a bunch of data to them and then track their actions to send it out to performance ad networks and email marketing tools and product analytics tools. And so you would see this very commoditized stack. It would be like CDP in the middle bunch of tools connected. The promise of the CDP was you integrate one SDK, your engineers don't hate you send all the data to the other tools you can create audiences.

(00:32:26):
Great. Lasted for a long time. The thing about it though that I think really changed around 2020 is that the cost of ownership of warehousing became much cheaper. And so 2021, you start getting to the place where it actually makes a lot of sense and is really easy to store all your data in a warehouse model all your data in the warehouse, and to do it without needing a vast data team. I would say Airbnb was probably doing all this well before anybody else was, but they had the main advantage of a lot of money and a lot of resources. So, now come 2020, it's cost-efficient to have a data team with your own warehouse and to manage data centrally in something like Snowflake. So, now this question is like, okay, well we got to get data into the warehouse, but how do we move data around is totally different.

(00:33:11):
And that's what really led to the rise of reverse ETLs. So, now you can actually build your own CDP and lots of businesses already have, I'm consulting with a well known financial trading platform a couple of months back, and they have a CDP, they have all this internal data in their warehouse, but they have not been able to activate it because it's pretty old architecture. Everything's batch based end of the day. What they need is a reverse ETL. They don't need to take that data and just get it out into the world. So, they need the reverse ETL component or the transformation component of a CDP. And so I'd say now today when we think about B2C businesses, you can either go to the traditional route, buy CDP, hook up all your tools, third party.

(00:33:52):
I think that's a great move if you do not have a lot of engineering resources because you're not spending a ton of time and energy on a warehouse and all the modeling that comes with it, you're just spending time to implement one SDK. I think if simplicity is the name of the game for your business, CDP, Centralized Stack, great move. If you are an advanced engineering culture and you are cutting edge and you're going to do a bunch of modeling in DBT and you already have Snowflake, you should move towards a model of using a reverse ETL. What it means is that there's a way to get your data into the warehouse and then how you activate it is completely independent from the CDP. And so what that means is actually you can have lots of different variations of the stack.

(00:34:31):
You could use Amplitude as your CDP, collect all your data, stream it into Snowflake. They actually now have an integration with Snowflake that lets you feed data directly out of Snowflake, and then you could use a reverse ETL to just pipe that data wherever you want. There's a really good section though, again, sorry to self aggrandize, but there's a really good section in the Reforge module this fall that talks about what happens when you have multiple ways to move data. You buy amplitude for your CDP and you're moving data to your warehouse. Amplitude is a bunch of integrations, but you also have reverse ETL and you can move data out of your warehouse.

(00:35:05):
Where do you choose? And I would say a lot of businesses get in trouble when they don't have a methodology or a system for how and when to move data from one place to the other, so they just do it haphazardly, right? And the key in systems management is you want to design a process for doing it some type of waterfall or mental model for when it makes sense to move data directly from Amplitude, which is the ingestion point of your data stream or from the warehouse where you can model it and make it better. I think the key is just having a philosophy and approach. There's not really one answer, but that's all B2C. So, B2B I would say ... Yeah, go ahead.

Lenny (00:35:40):
Before we move on to that one, you mentioned reverse ETLs. What are some examples of products that are reverse ETLs so that people can look them up?

Austin Hay (00:35:47):
Yeah, I personally think the reverse ETL is a capability. It's the ability to move data from a warehouse to a tool. So, technically speaking, you'll find reverse ETLs in CDPs and as standalone products. Segment has a reverse ETL function they just launched, and Particle has a reverse ETL function they just launched. Rudder Stack, which is a CDP has always had a reverse ETL function where you can take warehouse data and move it to different cloud infrastructure. Then there are distinct standalone products. Census, which was back Bay 16Z and Hightouch are the two standalone reverse ETLs. And like I said, I'm an investor in Hightouch, love their work, we use them at Ramp. At the end of the day, you should pick tools because they help solve problems, not because of anything else. So, we can come back to that if you want.

Lenny (00:36:32):
Wonderful. Great, great. Yeah, that was perfect. Keep going.

Austin Hay (00:36:35):
Okay. Yeah, so we talked about B2B, or sorry, B2C. B2B, I probably don't have as much history as say people who survived the dot-com crash in 2008. I started really my career in B2B in 2014, so I'll share a little bit of my experience and I'm just hopefully just saying this because listeners may chime in and be like, oh man, this guy doesn't know what the hell he's talking about, which is totally fair game. So, 2014 though, I remember working at Branch, I was working for our COO Mike Molinet, who's now at this really cool company called Thena, but at the time I was working for Mike, and as we talked about before, oftentimes growth stacks just appear because you're given a challenge. And I remember sitting in this tiny room with Mike. We were over in Palo Alto, right off the fills in Palo Alto in this tiny room.

(00:37:27):
It was boiling in the room like so hot we were sweating and we were mapping out on a whiteboard how we would design our first version of our system, like how we capture leads, how we get them into Salesforce, how we would email them with a little tool called Outreach at the time, that was still a startup. And I'll send it to you after this if you want to show them to viewers, but it's so MVP, but it still models what a lot of people have today. There's some ingestion point for your data. There's Salesforce, there's some type of outbounding tool, there's an enrichment tool, and then a lot of other Jerry rig stuff hooked up to Salesforce. And for the most part, that's how B2B still exists today as you have Salesforce and then the whole world and the universe revolves around Salesforce. You just have more advanced tools, you have Gom and stuff like that.

(00:38:12):
I think the big change though, and what is really fascinating and has been fun to watch is in the last two, three years, you now have this whole rise of B2B2C, which takes all the complexity of the top of funnel user acquisition system and stuffs it right alongside your CRM and how you build an elegant system there in that space, I think is one of the most complicated and intricate pieces of being a MarTech person today. And some of it just has to do with the data language. Like all these B2C tools were designed with two objects, a user and an event. And so if you're not a technologist, it's like object orientation is how you kind of think about the world. There's only two concepts for the world in a user acquisition based system. A user who's a person either anonymous or known coming into your website and the things that they do on your website or application, and you use all that data to acquire them or model them.

(00:39:03):
In a B2B business you have all that complexity, but at the end of the day, you might not really need it if all the person is doing is it's just the company is signing the contract and then you don't really care what happens afterwards. You might track users and events inside your application, but it's not for the acquisition, it's for the retention of the user. B2B2C is fascinating because you have all the complexity at the top, but then how and when do you tie a user to a company or some type of entity object, and what tools do you need to do that and where do they live in the system? And do those tools actually have competing priorities? Let me give you the greatest example of this that happened at Notion when I was consulting to them at Chris when I was consulting to them and at Ramp is having both HubSpot and Salesforce.

(00:39:45):
Both are CRMs, both have the ability to track users and companies, neither are CDPs. And how you actually map the data from HubSpot to Salesforce kind of determines how much hell you're in, and there's really no good solution. It's just like you have to figure out for yourself, how do you want to acquire use at the top of the funnel? How do you merge them into the bottom of the funnel of the Salesforce? And again, there are lots of options or versions of the world. You could use Amplitude only and collect all your user and event data and then merge that into Salesforce directly. You could collect all your data in Amplitude or Segment and then post that to HubSpot, which then posts that to Salesforce. But of course, as you make these decisions, your systems becomes more complicated and more than one person can manage. So, there's this trade-off between complexity and resources that you always have to juggle.

Lenny (00:40:33):
Today's episode is brought to you by Brave Search and their newest product, the Brave Search API, an independent global search index you can use to power your search or AI apps. If your work involves AI, then you know how important new data is to train your LLMs and to power your AI applications. You might be building an incredible AI product, but if you're using the same data sets as your competitors to train your models, you don't have much of an advantage. Brave Search is the fastest growing search engine since Bing, and it's 100% independent from the big tech companies. Its index features billions of pages of high quality data from real humans, and it's constantly updated thanks to being the default search engine in the Brave browser. If you're building products with search capabilities, you're probably experiencing soaring API costs or lack of viable global alternatives to Bing or Google.

(00:41:23):
It's only going to become harder to afford these challenges. The Brave Search API gives you access to its novel web scale data with competitive features, intuitive structuring and affordable costs. AI devs will particularly benefit from data containing thorough coverage of recent events. Lenny's Podcast listeners can get started testing the API for free at brave.com/lenny. That's brave.com/lenny. There's this big question within B2B and B2C around how to do attribution. Well, it's a never ending struggle. I'm curious if you have any pro-tips or best practices or tools that you use to improve the way attribution happens at a company.

Austin Hay (00:42:09):
Actually, I listened to your pod on multi-touch attribution. I'm forgetting who you were with at this point, but it was like I was loving it because it talked about MMM and MTA specifically.

Lenny (00:42:19):
Yeah, that was a newsletter post actually, not even a podcast.

Austin Hay (00:42:22):
Yes. So, back to our conversation around division of responsibility. I'm not always the person you should talk to create an MMM model. I'm not a data scientist. I know how to make MMM models and I know what they are.

Lenny (00:42:36):
Can you explain MMM briefly?

Austin Hay (00:42:38):
Mixed Media Modeling. And MTA stands for Multi-touch Attribution and it's these two ways of measuring the world and marketing to understand how you should allocate resources to campaign spend. MTA and MMM though are both underpinned by how you collect data. They're both informed by the user object and the event objects that you collect on your website or your application that then lead to the data that data scientists use for MTA and MMM. That's the connection between data and MarTech is often the tools and systems that we build and stand up and manage are what are used for these very complicated growth, experimentation and attribution results at the end of it. And one of the most discreet things you can do for MTA, because I get this question all the time around, hey, do we need MTA?

(00:43:21):
What should I do first touch or last touch? Should I do both? And there's actually really, I can send you this guide, but there's six or seven things you can do to basically futureproof yourself from needing either one. Because most businesses either start with first touch or last touch and then eventually want to move to a multi-touch attribution model. And for those who don't know what that is, first touch is where you kind of collect the data about where somebody first came from. Last touch is where you collect the data about where the person last came from. So, an example, would this be like if I went to Lenny's Newsletter from a Google ad and that's all he has? That would be my first touch and my last touch. If I first came from a Google ad to Lenny's Podcast, but then later I came from a Facebook ad or I don't know direct, then that would be my last touch.

(00:44:06):
And so it's this question of does the Google original first Google Channel get credit or does the second one the Facebook or direct get credit? And the first touch attribution model, a hundred percent goes to the first channel and the last touch attribution model, a hundred percent credit goes to the last touch. And a mixed attribution model or multi-touch attribution model, you're trying to figure out how to split the difference. And usually the evolution for businesses is they start with first touch or last touch, then they go to splitting it literally 50/50. And then somebody gets angry because they're not getting enough credit and they say, we've got to go to MTA. And there are both first party solutions for that and third party solutions for MTA. But back to the main thing, the main point is if you think about what you're collecting, this is for website businesses, you're collecting the referrer, like in the URL where the person's coming from, and you need any UTMs associated with that person.

(00:44:58):
And you also need any parameters from the advertising networks that might give them the ability to counter a conversion. Every ad network out there has little things they stuff into your URL that tell you that you came from them. Facebook has FVP, FPID, they sometimes encode it. Google has this thing called Google Click ID, which is just a really long string of characters that don't matter unless you know how to decode it. But all advertisers, and for the longest time advertising worked by putting parameters in URLs, pushing somebody through to your website, collecting those parameters and then passing it back to the ad network so they could get credit for it. And so in my mind, the best practice that everybody should stand up from day one is to basically design the system for MTA and then use whatever makes sense as you grow.

(00:45:45):
And so the way that I typically recommend to people is like imagine when a user comes to your website, you collect the URL, collect the referring URL, collect all the additional marketing parameters that you might want, [inaudible 00:45:57], TikTok ID, Microsoft ID, you should just make a list of them. And if you don't have that list, I can give them to you. And then you should collect all UTMs. So, in the URL, you're going to have UTM campaign, UTM medium. Most marketers use this to note what the campaign type was. Now the thing is that UTM is only going to be specific to the moment in time that the person came to your website. So, back to example about Lenny's podcast. If I come to LE's podcast and I came from a Google ad, then my UTM is only for that Google ad.

(00:46:28):
So, I have a Google Click ID and I have a UTM. So, what you're got to do is you've got to store those parameters locally on the device. Either was a browser or whatever. You got to store it as UTM first campaign, UTM last campaign. And what you do is every single time that a person comes, you replace the last campaign or the last value with the one that's there. So, say the last one was Facebook and then I come later from a direct mailer ad you replace the UTM last medium with the new one. Now what's happening if you're using third party tools is that you're collecting this user information when the person's on the website, you're going to collect it both as a user attribute and as an event that way. What's going to happen on the backend for your data warehouse team is they're going to see a user profile that has both the first attribution information and the last attribution information.

(00:47:20):
And then for all the stuff in the middle, you're firing off a page view event with first and last, where the last might deviate if there were multiple steps in the middle. So, what they can do is they can just coalesce over all the last UTMs they've seen on all your events by user to get both their first one, all the ones in the middle and the last. And so this isn't actually that complicated to set up. Most people just don't do the work early on. And then when they want to go back later and have MTA results, they don't have the data to do it. So, one of the things I tell people who are debating this is let's just get the infrastructure right from the beginning.

(00:47:55):
Let's set up so that you have users, you have user attributes, you're collecting first and last UTM on users. You're firing events with all those. There's some other more complex things you can do too. You can set them in first party cookies and you can also set them in your third party cookies for your tooling vendors. At the end of the day though, what matters is you just are collecting this information from the beginning. That way when you actually want to progress your attribution model, you don't have to wait a really long time to start gathering that data.

Lenny (00:48:24):
Amazing. I love the details that you're sharing. I don't know where else people can find this sort of advice. It sounds like a core part of this is one, just having a data warehouse where you just throw all this data into, and two, having a taxonomy that you can rely on and do multiple things with down the road. Is that roughly right?

Austin Hay (00:48:42):
Yeah, I think that's right. The taxonomy though, I think what's interesting is it's very much guided by your third party tools. And again, that's the reason why I think companies often miss the mark here is because they're not thinking about what can my tool actually allow me to put into it in the first place.

Lenny (00:48:59):
Just to make sure I understand what you're saying there, you're saying generally maybe third party tools limit what you can do, which set you up for hardship later. And maybe what you're saying is do that yourself, that tracking piece, is that roughly what you're saying?

Austin Hay (00:49:14):
Yeah, I think that's right. The way to think of it is if you build your own data warehouse, your schema is unlimited. You can do whatever you want. You can design product schema, you can design user schema and event schema, but most third party B2C tools don't allow you to control the schema. There's only one CDP I know that does that, that's Snowplow. The rest are there's a user object and an event object. So, you can either stuff data as a user property onto the user object or you can stuff data into the event and fire it off as an event, but that's what you're working with. So, what I'm saying is most people just don't think about the object orientation of the third party tools they think about and they don't design their website traffic or their app traffic. We didn't talk about app, which is a whole different slew because doing attribution with Iowas 14 is much more difficult.

(00:50:07):
But even in the website version of the world, people will often just collect UTMs and think that their job is done and it's like actually it's more complex. You have to think about first and last, think about the steps in the middle, design it so that you're putting it on the user profile and in the event. And so this goes back to the main thing that we were talking about earlier, whereas the job of a marketing technologist is to think often one to two years down the road about what we're going to need to solve for and design systems in an elegant way, not to break the bank, but to at least be the minimum viable product to actually get there. And a lot of my job, and I think the job of marketing technologists is trying to preserve that future state in the most minimally invasive engineering and resource way possible.

Lenny (00:50:48):
You've talked a bit about thinking ahead and a bunch of tools and platforms, and I'm wondering are there any new and emerging tools, platforms or even growth channels that you're keeping an eye on or excited about or finding more and more useful?

Austin Hay (00:51:02):
I'd be remiss if we didn't talk about Threads, right? Threads is super interesting. The question will be how quickly can they stand up an API for advertising and what does that look like or do they just blind it in with the existing meta and Facebook architecture? One of the caveats that I'm sure a lot of performance marketers out there will agree with is Facebook has a conflict of interest in reporting, right? They want you to spend money, so obviously they want to report the best results. And that's the reason why attribution parties like Branch and AppsFlyer exist is to somewhat curtail that conflict of interest. And so I'll be really interested just to see how attribution works, especially when you're moving from Instagram to Threads, from Facebook to Threads. Will it be the same architecture, will be the same advertising platform? Will they try to do something new?

(00:51:52):
So, I'm keeping my eyes on that. Reddit is also a very interesting place to convert now. They're opening up their conversions API, and I'm seeing a lot more investment in Reddit just because you can have embedded ads now that almost look like they can be posts that you can comment on. I think it just speaks to the maturity of the advertising business. What's happening in the background of all this is ad attribution from apps has become a lot more difficult and mostly aggregate. From 2010 to 2020, we had the golden years of deterministic matching where it was very easy to run an ad and understand with precision who installed the app. Maybe you didn't know their name, but you actually would know their IDFA and you could tie that to their PI. You can't do that anymore. It's very challenging.

(00:52:35):
Even when you can do it, the results that you would get are pretty low because nobody's going to be opting into giving you their IDFA. So, what that means is these ad networks are becoming more complex, sophisticated, and interesting right at the same time that it's harder for marketers to really understand how they're spending money. And so I'm paying a lot of attention to how marketers make decisions with probabilistic data because most of the work that I'm doing now is actually saying, well, given that we don't have determinist data about a certain audience or where somebody came from, how can I find other information that will create a model for 30% of the population and we can use that to extrapolate to a hundred. So, probabilistic matching and probabilistic attribution I feel like is a skillset that more marketing technologists and marketers should just get familiar with the way that we make decisions today.

Lenny (00:53:27):
Wow, I hadn't heard of this concept before. And that's how people are starting, or at least you're suggesting that's how people should start thinking about growth results and impact is less, here's how much this ad drove, the likelihood that this ad did this had this sort of impact.

Austin Hay (00:53:46):
And it's not the case with all channels, but it's specific for apps that have mobile apps, they're going to be impacted by it because they just aren't going to be able to discreetly identify one-to-one the person that came from a campaign. They'll know that a group of people came from a campaign, but they won't be able to make measurement with those people alongside other attributes. For website, it's not the same, but there are lots of things that are making it more challenging. One is browsers now are stripping out those URLs we talked about. So, you're just seeing a bigger and bigger percentage of people being counted as organic that actually came from a paid advertisement because when they got redirected to your website, the browser truncated all those URL parameters. The second thing is cookie blockers. We talk about all these third parties before.

(00:54:30):
The way that third parties often collect information is they drop a cookie in your browser that tracks you, if you've heard of Segment, which is one of the most well-known CDPs of the last few years, is they implant a little third party cookie on the site that contains an anonymous user ID and all of your attributes as you're navigating the site. And then once you log in, they convert that to a known or non-anonymous user ID.

(00:54:53):
Usually that's tied to some type of entity ID or a user record. And at that moment in time, if you come back and they see your cookie, they kind of know who you are. Now, if you're blocking cookies, that means you're basically remaining anonymous throughout the entire user journey until you log in. Not to mention a lot of people have lead funnels where you need that information to actually understand what the user is doing before they convert. So, if you're blocking third party cookies before they even get a chance to convert, you have no information about where the person came from. You just saw that they signed up, and so it might as well be organic.

Lenny (00:55:26):
So, you talked about how many people are trying to get used to this new world of ATT and much harder to measure attribution and all that. Is there anything you've learned that has worked well to help you recover from that a little bit in terms of measuring what's happening? Is there any tips you can share or anything you've seen work?

Austin Hay (00:55:44):
Yeah, I mean I think a lot of people are just gravitating towards MMM now without really understanding when MMM is useful or not. I don't know if there's a company called Recast. I think you're an investor. Am I crazy?

Lenny (00:55:57):
I am. And that's who wrote that article that you mentioned actually.

Austin Hay (00:56:01):
That's right. It's Michael and it was somebody else, I can't remember the name besides-

Lenny (00:56:04):
It was another Mike Taylor.

Austin Hay (00:56:06):
I'm not an expert on MMM, so I'm not going to be able to comment to quite the degree that they have. But when I spoke with Michael, and when I think about MMM, a lot of my conversation is this actually really realistic for our business right now? Do we have the data to run an MMM model and how is it going to change or chart the course of our performance ad marketing business in light of having this information? And when I think about it through those lens, most of the time businesses are not ready for MMM. They actually just be an MTA and they need better probabilistic modeling. And I know that's not a super spicy take, but I'd just say at least at Ramp and what I'm seeing at other businesses right now that are operating, it's much more of like we're going back to the days where we understand in broad strokes how much each of our campaigns is driving in advertising revenue.

(00:57:00):
We're not able to tie that discreetly with the user journey. And we know that some percentage of this user base might have been lost or organic. So, in light of those, how do we make spend? And then also you can be pretty smart. You can do, for example, geo-based testing on billboards. Try to isolate that as a factor if you withhold all other confounding factors so you can be smart. Coordinating these types of campaigns though is really challenging, especially if you're a really big business, let's say runs online advertising throughout the US and you're trying to do targeted billboard tests in an isolated number of cities across the states coordinating to turn off demographics, make sure there's not isolating factors. It can be really challenging. So, there's not a silver bullet right now I don't think.

Lenny (00:57:42):
Awesome. Just a few more questions and then a broader question I want to ask. So, say you want to start hiring the next Austin, first of all, what do you look for in the person? What are signs that they're probably going to be worth chatting with? And then what are some interview questions you'd like to ask to get a sense of how strong they are?

Austin Hay (00:58:02):
So, the first thing that I always gravitate towards is just intellectual curiosity. And I know that's very, maybe a little bit overrated, but I think you can tell pretty quickly if somebody's just interested in the world and learning things. And the thing about third party tools is you are constantly learning. You'll never be an expert in everything because there's way too many tools to be an expert on, I forgot what publication, I think it's MarTech editor in chief or something. There's a publication that I subscribed to and everything is classified as MarTech and the diagram is huge, like cover a wall. Now I don't believe everything like that is MarTech, but even if a fraction is, there are way too many tools in technology to ever be an expert. So, you have to be both very interested in learning and very willing to quickly learn if you want to be in the space.

(00:58:50):
And so I generally look for intellectual curiosity as the first sign. The second thing that I think helps people a lot who have intellectual curiosity is they're scrappy in engineering. They might not be the best engineer possible, but they know how to get around. They know JavaScript, they know Python, they can read API documentation and make an API request. They have enough base knowledge to basically understand how to solve a problem that an engineer might do even if they themselves are not an engineer. Now obviously you can get lucky sometimes and you'll find the engineer who never wants to be an engineer again and decides to move into something less technical. And in those cases they're super powerful, but I haven't met a lot of those people in my life. And also there's just some business dynamics to it. You could probably make more as a backend engineer than as a MarTech guy.

(00:59:41):
So, you probably just pursue the pathway that makes more money. It's like a little bit of a utility function. So, I look for intellectual curiosity. I look for basic engineering scrappiness. And as a side note, I would say lots of people out there, the advice that I give them is you don't have to go get a software engineering degree. You can teach yourself, I am self-taught. You can take a coding academy online. I think you get enough knowledge through being able to do web programming or some type of backend programming. So, I would say it's not more than a six-month investment for anybody to really get the skillset that's needed. Obviously once you get the skillset, you can build upon it with years of experience afterwards. But if you're new to the space and you're in marketing ops and you want to get more technical, or if you're a user acquisition manager who did paid performance, but you're like, I really want do things end to end.

(01:00:33):
You can just go pick up some software skills and you probably are going to be pretty dangerous from that. And so those are the two things I gravitate towards. There's obviously many more, but those are the first two. The questions that I like to ask is what does I like to ask people how they prepared for the interview. This is not, I can't take credit for this. My wife told me about, gave me this idea and I loved it. I think it was a16z partner. But I love the question because when you ask, hey, how did you prepare? You're really asking how does the person think? How did they plan? How did they take things seriously or not? What did they read? What did they do? And if you have to prompt them to tell you all the things they did, then they're just not a systems thinker.

(01:01:17):
But if they're like, hey, actually I read these things, I did this. I woke up, I went for a run. The more interesting complex the answer, the more interesting complex the candidate. And so I love the question because it just gives you a really good understanding of the person on a whole, like right out the gate. And then the other question I like to ask is I like to ask, so you're coming in tomorrow to our marketing tech system and by Friday you have to write up a report on all the things we should change. What do you do? And I like to ask that question because it pretty much signals out people who are biased versus not. People who have tooling biases will immediately just like, we should implement this tool because I used it before and I really like to hire people who are not tool specific, who are more tool agnostic and they think about tools as being things to solve problems as opposed to tools being things that you just solve because you've already solved it one way.

(01:02:12):
This isn't a gripe and it's certainly not intended to slice at PMs, but one of my observations of a lot of PMs is they just pick the tools they've already used before because it's easy and it's a shortcut for them, which I understand, but problems are not always the same. So, tools shouldn't always be the same. So, I like to pick people who think about the problem set and the solution space more and they ask questions about what problems you're trying to solve, which I think is much more of an actual PM mindset of trying to work backward from the problem as opposed to just taking the problem and regurgitating stuff that you already know.

Lenny (01:02:45):
Are there any flags you look for that tell you maybe this person isn't someone you want to be working with?

Austin Hay (01:02:51):
I answer that question on two spectrums. One is if I'm hiring as somebody who's hiring an IC versus I'm getting hired. So, one of the red flags whenever I'm approaching a company to work for them is I'll ask for their company financials and a company that's not willing to divulge their financials to a director level or above person, I don't want to do business with because that means they're hiding something. Or they have a culture where they don't trust the most senior leaders of the organization. Either is a bad choice in my perspective. So, that's one of the questions I always ask when I'm going up for a job, when I'm hiring somebody. Red flags, I feel like one of the false flags not a red flag is more like when there's a gap in somebody's job resume, everybody gravitates towards that and it's often really explainable.

(01:03:39):
A good example is I was hiring somebody once who had a two-year gap in their resume. We didn't end up hiring the person, but they went through all the stages and we didn't hire them, not because of them, but because the job got removed and this person took two years to get a philosophy degree or maybe it was a poetry degree and then also taught himself to program. So, it was a really enriching two years and there were lots of ways that I could see them bringing their past experience and the way that they took time off together to be a really well-rounded candidate.

(01:04:12):
So, I would say I look less for red flags and more for false identifiers on the resume application that may shortcut me towards the decision. Another one is just school people just look at your school where you went to undergrad or grad and they kind of make a decision one way or the other. And I feel like that's also can be a really bad shortcut because there's some amazing founders, for example, who went to school as you maybe had never heard of. Yeah, I know that's not a good way to answer the question, but I don't have a good way of looking for red flags, but I do tend to spend a lot of time on netting out of false flags.

Lenny (01:04:49):
That was a great way to answer the question. I want to move on to something totally different, and this isn't something I've been asking people, but I'm curious if there's something here then maybe if there is, I'll start asking this more regularly. I'm curious if there's just any frameworks that you've found especially useful in your work or even life. Does anything come to mind?

Austin Hay (01:05:07):
One thing that I want to build, so if I ever build this, maybe it'll be a newsletter for you, is just a one-page doc of the most useful life frameworks and they're just the words, and so you obviously have to know them, but I feel like I come across really good frameworks all the time and then I forget them. So, I just want a one pager of Lenny's Life frameworks.

Lenny (01:05:07):
Okay, we're starting this right now.

Austin Hay (01:05:30):
Okay, great.

Lenny (01:05:31):
We'll have number one.

Austin Hay (01:05:31):
All right.

Lenny (01:05:31):
I like this.

Austin Hay (01:05:34):
Okay, so I've already said this and you've promised to put this at the top of the list, so I'm really excited. It's just tools are meant to solve problems and I tell that to every person I hire. I repeat it consistently at Ramp and all of my consulting gigs. And it's not just the words, it's the spirit of it. Tools are really just meant to solve problems. You don't have to buy a tool to solve the problem. You also don't have to buy a specific tool to solve the problem. And I think it embodies so much of what marketing technology is trying to do. It's trying to help people understand their problems and then actually take action on them using tools and technology that are most first party and third party. And most people just focus on the tool part and focus on the buying and integration part.

(01:06:16):
And so I think if you consistently remind yourself that tools are just meant to solve problems, then you really get into a space where you as a systems' person can be an advocate for your marketer or your product people. I think sometimes there is a little bit of a tendency for people to think that people who manage and set up tools are just interested in managing and setting up tools, but really at the end of the day, we're trying to help people actually do stuff. Then there's this PPS framework that I talk about a lot, which is problem, people and system. So, whenever there's a challenge that comes up like at Ramp or in a consulting gig, I like to first say what's the problem? Who are the people involved and what system does it impact? Usually because people just jump straight to the system. They're like, hey, there's this problem, I just need to solve it with the tool. Hey, I'm trying to do X, Y, and Z. Can you just give me admin permission straight to the system?

(01:07:07):
So, if you back up though first you understand the problem like, hey, what is this person trying to solve? What is their discreet issue? A great example is I'm a sales manager and I want to make it so that every time I hire somebody, I don't have to go through this really tough process of onboarding my staff. All right, so that's the problem. Who are the people that involves, does the sales manager need permission from the CRO? Do the sellers need to be trained? Is there some other confounding factor that we're not aware of why we don't want to just automate this thing? Once you have an understanding of the people and the problems that you're trying to solve, then it's really, really easy to design the system to solve that. And so that's my number one framework for technologists in particular is like don't just jump to the system, think backwards, start with the people and the problem and then move to the system solution.

(01:07:52):
And then another one that I've already mentioned too is it's B and B as opposed to BVB. So, build and buy as opposed to build versus buy. People all the time just think the second that you're talking about implementing a tool or procuring a solution, it's, Hey, I want to build this thing or I want to buy this really expensive thing. Build versus buy is a very narrowly constricting decision tree. If it's only build versus buy, then you've already made the decision that you can only do one or the other, which means you're already fighting somebody at your organization. Build and buy means that both of you can win and you can actually create a solution that is not only unique but saves the company time and resources and makes everybody happy. It's more of a consensus driven approach. Whenever I hear in a meeting or a call or some discussion about how we have a tool and it's really expensive and we want to build in herself, I try to just use the build and buy framework to tee people up and say, what about the problem?

(01:08:59):
Can we buy? What about the problem can we build? And where does it make sense to invest our resources and our people accordingly to get the optimal outcome? A great example is a company that I was consulting for was thinking about building their own AB testing tool. And actually we had the same problem at Ramp recently, and they're like, well, we just think we should build ourself. This is core to our technology. We have the engineering resources to do it. And they were evaluating it to build the entire system themselves or buy a third party, I think it was split.io or something like that. And the entire engagement was basically designing a financial model to show them that they could make a lot more money, save money, move faster if they just bought the third party tool at the lowest possible cost and spent all of their resources that they were going to spend building it, building around it and making it their own. And there's lots of, I hate the word synergy, it's just so yucky.

Lenny (01:09:54):
I don't mind it. I think it communicates what you want to communicate, and I feel like people don't say it as often anymore, so maybe it's okay.

Austin Hay (01:10:00):
Yeah, because they're afraid. There are mutual benefits is a better way of saying it, if you build a tool custom to yourself when you've bought a tool because the vendor at that point is committed to you and they want you to be successful, so you often can get accelerated outcomes if you build on top of a third party than if you just build it yourself. A great example is say you buy one of these AB testing tools and you build around it and you're a large customer of them, but you've invested a lot of your own engineering resources to make this solution your own.

(01:10:31):
If they know that and they care about you, they're going to be willing to actually make you happy in the moments where you need a change from them, say some SDK change or a new feature or something like that. A framework that I talk a lot about in my Reforge course is about building a stack. Everybody asks, hey, how do I build my stack? What should I do? What tool should I use? Even you earlier were like, what's the golden stack? Tell me what five tools should I get?

Lenny (01:10:57):
Just tell me.

Austin Hay (01:10:58):
Yeah, yeah. I'll tell you at the very end, I got to hold out. Otherwise, you'll ditch this podcast.

Lenny (01:11:04):
That's right. Yeah. Wait until the end. Is there anything else you want to share before we get to our very exciting lightning round?

Austin Hay (01:11:14):
The only thing I had wanted to fit in, which I feel like is maybe a framework or maybe just a really good decision-making philosophy is this concept of thinking gray. Have you heard of it before?

Lenny (01:11:26):
No. Go on.

Austin Hay (01:11:27):
Okay. So, Steven B. Sample is a professor at USC. He wrote a book called The Contrarian's Guide to Leadership, really great book. It's one of his principles. There's actually a lot of great principles in the book, but this is the one that I think has stuck with me the most in my career. And the concept of thinking gray is so often in life and in our jobs, we are forced to make decisions very quickly. We have to think black or white about a problem set or a solution, and then decide. One of his tactics is this concept of thinking gray, which is actually to not decide for as long as you possibly can before you have to decide. It's really challenging because it involves this little thing called patience, which I do not have a lot of, most of the time, and I know most people don't as well. But it's particularly really relevant in systems thinking and product because so often we believe that we have to make a decision because our boss is telling us because there's an OPR, because we feel the pain because somebody's complaining to me.

(01:12:30):
But actually in reality, you don't have to make a decision at all. You can just let it sit for a while. And this also applies to, I think, how you move through the world and view people. A lot of times we will meet somebody in a company setting or in a business setting, and we are quick to make decisions about them. We even asked me questions about how I hire people very quickly. We're looking for shortcuts to make decisions about evaluating people. One of the best pieces of advice though about thinking gray is it gives you the grace to not decide about people until you have to decide. So, obviously for an interview decision, you have to decide.

(01:13:05):
You have to decide yes or no. But so often you'll come across people and you'll meet them once or twice. And I feel like there's this tendency in the back of everybody's brain to be like, do I like this person? Do I want to work with them? And the question often is not that it's do you have to even make a decision right now? And by leaving yourself to have space to decide, you actually open up the possibility that in the future you'll make a better decision. So, I think that's a really good lesson for systems, and it's obviously a lesson that you can apply to the rest of your life too.

Lenny (01:13:37):
Austin, that was awesome. And with that, we've reached our very exciting lightning round. I've got six questions for you. Are you ready?

Austin Hay (01:13:43):
I'm so ready, Lenny.

Lenny (01:13:45):
What are two or three books that you've recommended most to other people?

Austin Hay (01:13:49):
So, first book I already mentioned, but say it again. It's The Contrarians Guide to Leadership awesome book. Second book that would be really good is the Art and Adventure of Leadership by a guy name Warren Bennis. And these are more philosophically leadership books. They're less about technical specs on how to run a business. So, you have to be into that.

Lenny (01:14:10):
Favorite recent movie or TV show.

Austin Hay (01:14:12):
I'm currently watching for the first time Suits, which I'd never seen before, which I think is pretty good because the story arc of every Suits episode is that there's a problem. Then they solve the problem and then the problem is solved at the end. So, it's very gratifying for anybody out there who's a high anxiety person who just wants to have this story arc resolved at the end of the episode. But if that's not your jam and you like excitement, also watching Silo, Witcher. For comic relief, there's Our Flag Means Death, which is hilarious. Have you seen that show?

Lenny (01:14:44):
No, not Our Flag Means Death.

Austin Hay (01:14:46):
Now you need to go watch it. It's about black beard and gay pirate captain. So, strongly recommend that. And then for just really dumb comedy, What We Do in the Shadows is hilarious.

Lenny (01:14:59):
What was that? What We Do in the Shadows?

Austin Hay (01:15:01):
Yeah.

Lenny (01:15:02):
Okay. Wow, a lot of recommendations. Thank you for that. What is a favorite interview question you like to ask candidates?

Austin Hay (01:15:09):
So, I talked about what you did to prepare, but the other one that I think is really good because it forces people to get vulnerable is tell me about the most difficult or challenging thing you've overcome in the last year in your life. It doesn't have to be work related, it could be personal. And I think it's a great way to just reset the atmosphere, make people dig a little bit deeper into who they are and be more vulnerable. And I find usually it also helps calm them down because if they shared them one of the most challenging, difficult, and hard parts of their life, then all the other questions just are pretty easy. So, that's one of my favorites.

Lenny (01:15:43):
What is a favorite product that you've recently discovered that you really like?

Austin Hay (01:15:46):
This sounds super dumb. It's called cal.com, and I'll tell you the story first. I've been a big Calendly user for a long time, but Calendly is pretty expensive. If Calendly is listening, you want to give me promo, cool. But it's very expensive. And then I also just found that it is not always graceful at syncing multiple calendars from both businesses and consulting gigs and personal, and I had trouble remembering my Calendly link. I don't know. The interface is like circa 2016. So, really looking for something a little bit more notion like with a Command K interface and just integrations that work. And cal.com has not failed me. It has been awesome. So, if people are looking for new Calendly tools, strongly recommend.

Lenny (01:16:30):
Wow, I never heard of this. What a great domain, cal.com.

Austin Hay (01:16:32):
I know, right. Killer.

Lenny (01:16:34):
What is a favorite life motto that you often repeat to yourself or share with other people, either in work or in life?

Austin Hay (01:16:42):
I just think a lot about the power of appreciation, and one thing that I've just been thinking a lot about recently is the challenge that people might be facing in their daily lives. I actually was recently listening to another podcast by Adam Fishman, and he had Brian Balfour on. And Adam's basically just interviewing a bunch of dads, which is cool. But the nice thing about being a little bit older in your life being a dad is that you maybe have seen hardship before. And this podcast is great at just exploring the stories of people who I really admire and go through their hardship. And in that it's been a very profound experience, understanding the type of challenges that people have gone through in their lives, people who have lost mothers and fathers early in life, people who have lost children. I myself, my wife and I lost her dad last year.

(01:17:35):
We lost two grandparents to COVID, we lost our dog. So, I think that the way that it ties to appreciation is if you can understand what people are going through and you start to view them a little bit more as a human and understand what's beneath the surface of work, who are they? What do they care about? What are the things that are driving their life forward? It just makes you so much more appreciative for what you have and the good moments when they're actually there. And this doesn't just apply to life. It's also like business too. It makes winning a lot more fun when you know the hell that people have gone through. That's just something I like to talk a lot about with people, especially folks who are younger in their careers who maybe have only seen wins describing what the losses look like so they can picture in their mind and then have some experience when they go through it. It's a big part of my shtick.

Lenny (01:18:23):
What an excellent answer. I am definitely going to keep asking this question. For people who are still listening here is the promised Golden Stack.

Austin Hay (01:18:32):
Okay, so Golden Stack. If I was a B2C business, I'd buy Amplitude for my CDP, I'd buy customer IO and maybe I'd upgrade to Braze in the future. I put everything in Snowflake, I'd buy high touch to reverse ETL, all that data out to my ad networks. For attribution, probably AppsFlyer from a mobile app, if not Branch, but it'd probably be AppsFlyer first. So, that gets you, you got AppsFlyer, Amplitude as your CDP and product analytics, Customer IO for email. Snowflake for your data warehouse, Hightouch for streaming all the data tools. That's like golden stack today if I were implementing it for a B2C business. For B2B, roughly the same, Amplitude. If you need an attribution tool, if it's B2B, actually, if it's a web only business, probably we use Branch because Branch is better for web.

(01:19:23):
So, you have Branch, Amplitude, connect all the data to Salesforce. Hopefully at some point in time somebody builds a better Salesforce. That'll be for our next podcast though, Lenny, can't cover that today. And then reverse ETL is Hightouch. So, very similar except the only difference is what do you do for an email tool? A lot of people use HubSpot. I would try to go away with Customer IO as long as I could and then I'd move to Braze afterwards. So, a big difference is just Braze versus Customer IO for B2B.

Lenny (01:19:49):
Final question for you. I heard that you're a drone pilot and I'm curious, what is the coolest place you've flown your drone or the coolest thing that's happened with your drone?

Austin Hay (01:19:57):
So, this actually gets back to our intellectual curiosity thing. Maybe I just search for weird people when I hire because I just love when people do interesting things that are unrelated to work. And the story is during COVID, I didn't really want to just better myself online through a bunch of educational platforms. I just felt like it would be a little bit soul crushing to sit in front of my computer screen and learn how to do statistics or whatever. So, I was trying to look for things that were interesting, niche, outside of my domain knew nothing about. And the three that I came up with were, I learned to fly a drone. I became a CFP, certified financial planner and I became a notary. And it's just because they seemed really useful things that had nothing to do with my work and would learn about something completely interesting and different.

(01:20:46):
So, those are the three that I chose. The drone stuff, it actually was funny. I started flying here in DC. I live in Virginia, but maybe a mile outside of Washington DC and around DC there's a restricted air zone. And so after I did my FA drone pilot license and I became a certified drone pilot, I really went down the rabbit hole of trying to figure out how to fly a drone in DC, because I've seen them around, but obviously it's a national security and I'm probably dramatically mutilating the exact experience. But as I went to do this, it was very complicated, archaic, but also funny because it was all online. You have to go file out a form, you get a letter from a local representative who says you're in good standing. So, we found a councilman that I just knew. And then you have to fill out all the stuff.

(01:21:39):
This paperwork, the site looks like it's from 1994. There's an office literally in DC where a person approves you. Then you have to let go and get a police officer to effectively babysit you while you fly this drone. And so I did all that and I got to the point where I was going to get babysat and I called our local police department and I was like, yeah. So, I talked to the office, I just need an officer to come out and meet at this time. And they just laughed me off the phone.

(01:22:04):
They're like, we're not going to send a police officer to watch you fly a drone. And I just thought the thing was really funny because yeah, it makes sense. Why would they waste taxpayer dollars to have me fly a drone? But it was a requirement. So, I ended up not being able to fly this drone in DC. But if anybody's listening and they know how to fly a drone and they want to fly, I would be totally down. I have two drones. I have a Mavic Air 2 and a Skydio Enterprise, which Skydio is a really cool company as well if people are looking for drones.

Lenny (01:22:33):
Okay, so you're saying if people have an awesome drone and they live in Virginia, they should come contact you and fly some drones together?

Austin Hay (01:22:38):
Yeah, exactly. Exactly. But just not in DC.

Lenny (01:22:42):
All right. Well, Austin, I think we delivered on the promise of making this extremely nerdy and in the weeds, and I think we've solved a lot of people's problems. I feel a lot of gratitude for you, and I feel like we taught a lot of people about MarTech, which was my goal. So, thank you again for being here. Two final questions. Where can folks find you online if they want to ask you more questions? And how can listeners be useful to you other than coming to fly drones with you?

Austin Hay (01:23:05):
So, first find me online LinkedIn. Threads, I actually have Threads. I don't have Twitter, like hot take, I think Twitter ruins people's careers. I've already seen multiple careers ruined by Twitter. Some people just don't know how to shut their mouth. So, I'm not on Twitter, but I am on Threads and I'm trying to figure it out. So, if you want to document Threads, you can. I'm on LinkedIn and then I have my email address on LinkedIn too, and I'm always willing to talk to people.

Lenny (01:23:28):
Amazing. And is there any way listeners can be useful to you?

Austin Hay (01:23:31):
Yes. I have a marketing technology course coming out with Reforge in the fall. If you're a practitioner of MarTech or you're interested in MarTech, would totally love for you to take the course, would love to your feedback in particular. I love to stand on this podcast and act like I know a lot about MarTech, but I'm still learning. And so I think it would be awesome to just get feedback from the community about what was interesting and helpful, what wasn't there, and we can improve upon. And then the other thing is, if you're ever looking for MarTech help and you want to reach out, that's great.

Lenny (01:24:02):
Amazing. Austin, thank you again so much for being here.

Austin Hay (01:24:04):
Thank you for having me, Lenny. It was a pleasure.

Lenny (01:24:07):
The pleasure was all mine. Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

