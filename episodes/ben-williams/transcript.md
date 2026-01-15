---
guest: Ben Williams
title: How Snyk built a product-led growth juggernaut | Ben Williams (VP of Product
  at Snyk)
youtube_url: https://www.youtube.com/watch?v=21sFTZzIfUk
video_id: 21sFTZzIfUk
description: 'Ben Williams is VP of Product at Snyk, an industry-leading security
  platform for developers, last valued at $8.5b. He’s also a product and growth advisor
  with over 20 years of experience...

  '
duration_seconds: 5494.0
duration: '1:31:34'
view_count: 11302
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- activation
- onboarding
- metrics
- okrs
- kpis
- user research
- iteration
- experimentation
- analytics
- funnel
- conversion
- pricing
---

# How Snyk built a product-led growth juggernaut | Ben Williams (VP of Product at Snyk)

## Transcript

Ben Williams (00:00:00):
Being able to identify the various micro and macro loops, how they're all connected, being able to document them in a qualitative model to communicate a shared understanding of how you grow, it's really powerful. Augmenting that then with the quantitative side of things that helps guide quarter to quarter focus and ensure you can be intentional about where you're investing, that becomes a big enabler. You're never going to have a shortage of ideas in a high performing growth team. So, knowing where to focus amidst that kind of sea of ideas is a really important role of the strategy.
Lenny (00:00:40):
Welcome to Lenny's Podcast. I'm Lenny, and my goal here is to help you get better at the craft of building and growing products. I interview world-class product leaders and growth experts to learn from their hard-won experiences building and scaling today's most successful companies. Today my guest is Ben Williams. Ben is a VP of product at Snyk which is likely one of the biggest and most interesting companies that you've never heard of. Snyk makes it easy for developers to catch security issues in their code, and there's a lot to learn from how Snyk got started. It started through product-led growth, evolved into product-led sales, was very community driven, and it was also laser-focused on developers which has become one of the most lucrative markets to go after.
(00:01:19):
In our conversation, we cover how the founders have Snyk out their first a hundred users, what they got wrong when they tried to monetize early on, when they hired their first marketing and sales people, how they structured and grew their growth and product teams, what they figured out about what should go into freemium and what shouldn't, and so much more. As you'll soon hear, Ben is British, and so, the episode is automatically going to sound more sophisticated and I can't wait for you to hear it. With that, I bring you Ben Williams.
(00:01:48):
This episode is brought to you by Coda. Coda's an all-in-one doc that combines the best of documents, spreadsheets, and apps in one place. I actually use Coda every single day. It's my home base for organizing my newsletter writing. It's where I plan my content calendar, capture my research, and write the first drafts of each and every post. It's also where I curate my private knowledge repository for paid newsletter subscribers, and it's also how I manage the workflow for this very podcast. Over the years, I've seen Coda evolve from being a tool that makes teams more productive to one that also helps bring the best practices across the tech industry to life with an incredibly rich collection of templates and guides in the Coda Doc Gallery, including resources for many guests on this podcast, including Shreyas, Gokul, and Shishir, the CEO of Coda. Some of the best teams out there, like Pinterest, Spotify, Square and Uber use Coda to run effectively and have published their templates for anyone to use.
(00:02:47):
If you're ping-ponging between lots of documents and spreadsheets, make your life better and start using Coda. You can take advantage of a special limited time offer just for startups. Head over to coda.io/ lenny to sign up and get $1,000 credit on your first statement. That's C-O-D-A.io/lenny to sign up and get $1,000 in credit on your account.
(00:03:15):
This episode is brought to you by Athletic Greens. I've been hearing about AG1 on basically every podcast that I listened to, like Tim Ferris and Lex Fridman, and so, I finally gave it a shot earlier this year and it has quickly become a core part of my morning routine, especially on days that I need to go deep on writing or record a podcast like this. Here's three things that I love about AG1. One, with a small scoop that dissolved in water, you're absorbing 75 vitamins, minerals, probiotics, and adaptogens. I kind of like to think of it as a little safety net for my nutrition in case I've missed something in my diet. Two, they treat AG1 like a software product. Apparently they're on their 52nd iteration and they're constantly evolving it based on the latest science, research studies, and internal testing that they do. And three, it's just one easy thing that I can do every single day to take care of myself.
(00:04:09):
Right now it's time to reclaim your health and arm your immune system with convenient daily nutrition. It's just one scoop in a cup of water every day, and that's it. There's no need for a million different pills and supplements to look out for your health. To make it easy, athletic Greens is going to give you a free one-year supply of immune supporting vitamin D and five free travel packs with your first purchase. All you have to do is visit athleticgreens.com/lenny. Again, that's athletic greens.com/lenny to take ownership over your health and pick up the ultimate daily nutritional insurance.
(00:04:45):
Ben, welcome to the podcast.
Ben Williams (00:04:47):
Thank you very much, Lenny. Thanks first of all for inviting me. It's a pleasure to finally meet you. I've got to say that kind of what you're creating with the newsletter and now the podcast, just such awesome resources for the product growth and wider tech community, so it's real honor to be invited onto the show, and I hope there's a few useful things that people can take away.
Lenny (00:05:07):
Awesome, man. I really appreciate that. I have no doubt there will be many useful things people will be able to take away. I'm really excited to chat about Snyk and the things that you're building there. I feel like Snyk is this very under-talked about company and also super fascinating companies, especially in terms of how it got started, how it scaled, and it's also at the center of so many trends, product-led growth, community-led growth, focusing on developers to grow, and also just security in general is really interesting, and so, I'm really looking forward to our chat.
Ben Williams (00:05:36):
Me too.
Lenny (00:05:37):
Before we get into all of that, I'd love to spend just a minute on your background. So, you're currently VP product at Snyk, and I'm curious how you got to that role and just some of the other wonderful things you've done in your career along the way there.
Ben Williams (00:05:51):
I'll try to keep it reasonably short. My education is in computer science, graduated from the University of Manchester back in the late '90s. I'd already landed as a job as a developer, but ended up having a bunch of other interesting offers, one of which was to join a small startup building requirements management tooling for product and engineering folks. This was all pre-Agile, but that whole space of developer tooling, engineering tooling, it was something I just felt naturally drawn to and it's where I've really specialized through my whole career. I actually joined that company as a solutions engineer, so lots of demos and so on. I was really close to the product team, but also speaking with customers every day which as is quite common I think was my path into products there.
(00:06:34):
Several years and a few acquisitions later, I find myself in IBM with the Rational software developer tooling group. I was leading parts of the product strategy there and a bunch of initiatives. I actually, I learned a ton of useful stuff there, but also that I had a strong preference for working in smaller, fast-growing orgs verse 350,000 people [inaudible 00:06:55]. After an interesting unexpected interlude, leading a DevOps transformation at a fintech and some consulting and advising, I then joined CloudBees. They're a DevOps startup with an open-core model. I was leading product design and growth there. Stayed with them for three years through several raises and a period of really fast growth before finally joining Snyk to build out our growth organization and lead our developer experience initiatives. I have a broad remit at Snyk now than just the growth org, but yeah, that's how it started.
Lenny (00:07:26):
Awesome. To give folks a sense of just how successful and big Snyk has gotten, one is just what does Snyk do, we haven't even talked about that yet, and then two, just some stats about the scale of the company and the business at this point.
Ben Williams (00:07:40):
The developer security company, we make it ridiculously easy for developers and their teams to improve their security posture while still moving fast. So, Snyk can find and automatically fixed vulnerabilities in code, open source dependencies, containers, infrastructure and cloud configurations, and all underpinned by the best security intelligence data in the market with a laser focus on developer experiences, which is why we're, we are really different. It's also an amazingly fast-growing business with some stellar PLG-focused investors and board members from the likes of Ed Sim at boldstart to Tamar Yehoshua, Slack CPO. We were founded in 2015, last valuation after our Series F was at 8.6 billion. We're securing the software of millions of developers now, well over 2,000 paying customers, now around 1300 people of which are around 500 in R and D with nearly 70 folks in our product org. And the people here just create this amazing culture, and all in all, it's just a really exciting place to be.
Lenny (00:08:44):
Okay. Did you have any sense it would get to this scale when you joined early on?
Ben Williams (00:08:49):
Yes, I think because I wasn't looking for a new role when I ended up joining Snyk, when I was first approached by them, but everyone I spoke with along the interview process, just became more and more impressed with not only the caliber of people here, but the vision, the mission for the company, and all those things you mentioned in terms of PLG, community-led growth, focus on developers, the security space, these were all things that if you create a Venn diagram of all the things that I'm really interested in professionally, super interested in, super exciting to me, then kind of Snyk ended up in the middle of it. So, it's pretty cool.
Lenny (00:09:29):
Awesome. So, that's a good segue to where I wanted to start is how Snyk started and how Snyk got their first hundred users, and I know you weren't there necessarily for that, but I'm curious what you can share about how the founders found their first say a hundred users. How did they get to their initial developers and get people excited?
Ben Williams (00:09:47):
I think it's a really fun story. So, if you don't mind, I'll just take a moment because I think it's important to set the stage by looking back at-
Lenny (00:09:52):
Let's do this.
Ben Williams (00:09:53):
Yeah, just look back at the market in general. So, PLG or bottom up and security, these were never words that were known to have been spoken together in a single sentence, right? So, security has always been a centralized function. Security programs were historically more about audit and policing and enforcement versus developer enablement or empowerment. A sales motion you saw it was always top down. It was seen as immovable, CISOs, other AppSec leaders with the buyers. Security tooling that was out there at the time, they all catered to this dynamic and these were tools that slowed developers down. They created a lot of frustration. They were met with a lot of resistance, not the ideal recipe really for consistent adoption and strong engagement and retention, and ultimately, app security programs based around those kind of solutions just weren't effective as they really needed to be.
(00:10:46):
So, it was a realization around this, timed with adjacent market shifts happening with DevOps that sparked the ideas behind Snyks. So, the founders, Guy, Danny and Assaf, they saw a real opportunity just to do things differently. They believed that the most effective way to improve application security posture was a developer-first approach. They knew that the developers were increasingly caring about the security of their code in the same way that they cared about performance and functional quality of their code. But they also knew that to empower developers to own that security, they needed just much better tools with way less friction than they ever had before. And their approach was, I think looking back, super smart, focus on a community. It wasn't the full extent of what we'd think of as community-led growth now, but it was close.
(00:11:35):
They started with a really narrow, early focus. It was a single persona, single context, single use case, and what that meant for Snyk was developers building applications using Node.js who wanted to ensure that the open source dependencies they were pulling into their apps were secure. Now, open source software, that's a huge accelerant in building modern software. The average software application today is at least 75% of open source libraries and components. So, this was increasingly becoming a primary attack vector for malicious actors who could find a single vulnerability in an open source component and then find it and exploit it in every single application that was using that component. And at the same time, at least back then, open source software was much less tested for security vulnerabilities, and the maintainers of open source libraries were often less security aware. So, you get that context, and then at the same time, Node.js as a run time was gaining traction. So, there was this increasing adoption in the enterprise, more and more dedicated conferences and the like, but the community was still small enough that Snyk could meaningfully influence, and Guy and the others just went all out on being deeply involved in that community. They were presenting at dev conferences, meetups, they were building online content and so on. And the question that they repeatedly posed to the community was do you have known vulnerabilities in your apps, and Snyk was there to help them answer that question. And fun kind of fact on the side, if you search for Snyk in the Urban Dictionary, you'll see it's an acronym for so now you know. But all of this kind of I think really only worked because of the parallel product-led approach. So, while the answer to the question about how does your product monetize users was much less clear cut in the early days for Snyk, the answer to the questions, how does your product acquire and retain users has always been product led.
(00:13:35):
And the initial version of Snyk, it was a command line tool. It was a tool for developers, it could be run locally or easily integrated into CICD pipelines for early feedback. It allowed devs to assume more responsibility for the security of their apps, and that was just very different from the typical incumbent technologies that were run by security teams late in the dev process, long feedback loops, issues thrown over the walls, inevitably just frustrating developers. And all of this was just built on this fundamental belief that the only viable path, and by viable I really mean sustainably effective, the only sustainably effective path for software-centric organizations to meet the challenge of becoming and staying secure was for them to take this developer-led approach to that challenge. So, really kind of complete disruption of the industry and developer adoption for that reason was always a key priority for us.
(00:14:31):
So, with that in mind, Snyk has just been free to use in some capacity from day one, and the early strategy was always about creating something valuable that was readily available, something that solved a real problem in a uniquely differentiated way, and making it pervasive. So, with dev-led option, this core concern, a freemium go-to-market strategy was just the obvious approach. So, eventually, getting back to your original question, that's all of the context and where and when and how they did it, but the first hundred or so users really just came from the founders engaging with the Node.js community and the interest that drove. I think we probably had maybe around 5,000 free users before there are any attempts at monetization.
Lenny (00:15:13):
Awesome. There's a bunch I want to unpack there because what's interesting the way you describe it maps to the series that I recently wrote about consumer growth strategy and how the first three steps after you have an idea is to come up with your super specific who, kind of your target persona, come up with a hook that catches them and gets them excited, and then go find them where they are and pitch them your hook. So, the super specific who for Snyk was you said open source developers working on Node.js. Is that right?
Ben Williams (00:15:41):
Well, it was Node.js developers, and Node.js developers were building their applications using open source Node components.
Lenny (00:15:50):
Mm-hmm. Got it. Was there any other constraint to that, do you know, or those were the two to three attributes of a user?
Ben Williams (00:15:56):
That's really it. The community was growing for sure. It was big enough to have a decent opportunity there-
Lenny (00:16:03):
Makes sense.
Ben Williams (00:16:04):
... but narrow enough that technology wise, it meant that a product could be brought to market in a reasonable time.
Lenny (00:16:10):
Yeah, that's great. And then the hook was basically you have known vulnerabilities in your code base which if I were an engineer, like, "I don't know, shoot, I don't know. Get a find exactly. I'm scared now."
Ben Williams (00:16:20):
Exactly. And then so now you know. Right?
Lenny (00:16:22):
Yeah, exactly. Okay, cool. And then the where, so you said that they went to open source communities. Do you have any more specifics about what those were? Was it like a specific forum? Was it like GitHub somewhere? Was it Reddit? Do you know any idea where those communities lived?
Ben Williams (00:16:36):
Yeah, it was less about a particular place, but more about the community of developers themselves who focused on Node.js. So, a bunch of early evangelism was really at conferences. It was I think the Velocity Conference in Amsterdam where Guy and Assaf kind of first unveiled Snyk to the world, and yeah, it went from there.
Lenny (00:16:58):
I see. Interesting. So, it was in-person events, conferences, and meetups probably focused on Node.js developers.
Ben Williams (00:17:03):
Exactly. Yeah.
Lenny (00:17:05):
Okay, awesome. What happened after that? So, that was the first hundred. Was it just roughly the next stage of growth or did it focus on that for a long time? What was the next stage roughly?
Ben Williams (00:17:14):
Yeah. I think that focus was the really important kind of element there, if I can kind of latch on that. Starting with that narrow focus and building around community engagement, I think it's a well-proven playbook now, particularly in the developer tooling space like New Relic did it notably with Ruby community for example. But ultimately it was important because of this kind of depth verse breadth approach and that depth-first approach that Snyk took was important to be able to effectively validate the solution on the path to product market fit. A JavaScript developer just won't care if you support Golang or Rust, but will absolutely care if a key feature like automated package upgrades just isn't available for their ecosystem.
(00:18:04):
Of course, the bigger problem of vulnerable components in open source across all languages and all ecosystems, that's a very widespread problem. It affects the industry at large, but that just spoke to the potential opportunity that was there to be unlocked. But the key for Snyk I think was just not to go too wide, too early. So, it focused on nailing that initial use case for that specific community of Node.js devs, like I say, narrow enough to be able to really focus on quickly building a compelling solution to a real problem, but also wide enough to be something viable from a growth perspective. And even back then the NPM, the Node Package Manager hosted around 200,000 open source packages. They were downloaded something like two and a half billion times a month by over 2 million devs. And the typical node app would have hundreds of dependencies, mostly indirect and so hidden less immediately visible. But each of those dependencies brought with it some security risks. So, yeah, I think nailing that narrow and deep-use case before expanding wider was absolutely critical and generally just sound advice around finding product market fit and building solid momentum before casting a wider net. It's difficult to maintain that focus for sure as the lure of that bigger term can be really tempting, but ultimately you have to build a service and market well to capture it.
Lenny (00:19:23):
Do you have a sense of when that focus expanded to an adjacent group, how many years into the growth story that happened, or was there some kind of milestone there? Because I know everyone imagines, yeah, we'll expand, the question is when and when does it make sense and when is it too early. Do you have any insights into that phase?
Ben Williams (00:19:43):
Yeah, for sure. First, I think if we're talking about PLG and the story with Snyk, I actually like that definition of product-led acquisition from Julian Shapiro when you spoke with him, and beyond that maniacal focus on finding product market fit for your product, founders really should be thinking about how their product is going to grow, and that's important of course as you think about taking that next step. So, let's assume in a simplistic definition that you found product market fit as demonstrated by a strong retention, and then the real question is where are the new users for your product going to come from, and founders really should have, I think, strong hypothesis around this, your risk essentially, adopting an if we build it, they'll come approach.
(00:20:27):
So, if your acquisition strategy is product- led, then understanding and being intentional about your early acquisition growth loops I think is an essential founder's responsibility. Dedicating time there to design those loops into the product, it's key. And when I say product, I really mean the whole product experience considering every touchpoint in and out of the core application that your users and customers might have with you. Snyk, for example, believed very early that we could build out powerful content loops via fixed pull requests that we raise on GitHub. New users, they'll sign up for Snyk, they'll connect their GitHub accounts, Snyk will scan their code, will find vulnerabilities, will automatically create Snyk-branded pull requests to fix those vulnerabilities. Other devs in the repo will see and interact with those PRs, and some of them will follow links to Snyk, create accounts and some of them will connect their own repos, and so the loop continues. So, company generated, company distributed content loop, it's actually really powerful for us because it's both an acquisition loop and an engagement loop.
(00:21:28):
Over the course of time, we extended that loop by adding support for other source controlled systems beyond GitHub. We layered on a bunch of new loops, and I think if founders can be intentional about this as you're developing early product iterations, then you're going to have a bigger advantage when the product clicks with the market, and that was built into Snyk as we went along. So, that was kind of ready as we found product market fit. But I think to talk about specifically how Snyk took that next stage, it was a function of when we were chatting before this, we talked a little bit about some of the failed experiences spinning up a self-serve revenue channel, and-
Lenny (00:22:09):
Actually before we get there, which I definitely want to get into all that, I love this story you just shared. I hadn't heard of this growth tactic of basically they connect their GitHub account, you find all the vulnerabilities, push a fix, people see that Snyk did this for them and it just provides all this value, and you're saying that was really effective. It's an example of something that worked very well.
Ben Williams (00:22:29):
First of all, that integration in terms of connecting your code with security scanning like that was a first of a kind integration.
Lenny (00:22:38):
Yeah, magic.
Ben Williams (00:22:39):
No one had done that before. But the key was that we ultimately controlled the content. So, not only was the fixed pull request doing something useful in terms of the code, but all of the description of the pull request was explaining about the vulnerability, educating users, and it was all Snyk branded and saying, "If you find this useful, click here, come and learn more about the vulnerability. Sign up for an account if you don't have one." It kept existing users coming back.
PART 1 OF 4 ENDS [00:23:04]
Ben Williams (00:23:03):
You sign up for an account if you don't have one, it kept existing users coming back and it brings new users, a lot of new users, in fact.
Lenny (00:23:06):
You'd be in there all like, "Do you have known vulnerabilities in your code base? Click here to find out." Is that responsible for much of the early growth, that loop?
Ben Williams (00:23:15):
I think that was one of the loops. We also have a couple of, from fairly early on as well, other content loops that are more kind of programmatic SEO assets that have both been pretty instrumental in terms of new user growth, yeah.
Lenny (00:23:31):
It'd be cool to hear about those if they're relatively straightforward to explain, and then we can get to the thing that didn't work, the self-serve monetization piece you were going to get to.
Ben Williams (00:23:40):
We have a bunch of loops actually at this point to start off.
Lenny (00:23:42):
Lucky you.
Ben Williams (00:23:44):
Yeah, I'm a big loopist, funnily enough. But yeah, we have a bunch of loops. Company generated, company distributed content loops have actually worked really well for us. We have a side car product called Snyk Advisor. Snyk Advisor, it's basically a service that developers use to search and find open source packages when they're considering integrating some within their software applications. The unique thing about it is it indexes all of the package managers. It learns about those packages. It augments the data about them with a bunch of metadata, including of course Snyk security scans, but we also find out how actively maintained the software is on the source repo on GitHub or wherever.
(00:24:31):
We build this kind of package health score, so anyone searching on Google for a package that does X, Y, Z or a specific package by name, Snyk Advisor will be right up there in terms of the search results. They'll land on there, they'll get a good idea about that package, they can look at similar packages and it's all, of course, a Snyk website and we have CTAs to say, "If you want to secure your application on a perpetual basis, then just come and join us." That's a great loop. That's all kind of a programmatic asset. There are hundreds of thousands of these package pages, but they're just automatically being generated continuously.
Lenny (00:25:07):
Got it. It's programmatically generated better indexing of open source libraries that you can integrate with. That is so smart. It's programmatic because you can inform on the security vulnerabilities and then the maintenance and activity. Interesting. Yeah, that makes sense. That's all data you could just gather. That's awesome. Okay, so there's that. Is there anything else that's worked really well for you guys to help you grow self-serve?
Ben Williams (00:25:31):
One of the recent ones that's really interesting is security education. We think of Snyk as a change agent in helping DevSecOps transformations and it's fine kind of having this capability, but what we really want to get to is this position where developers truly understand and can be better placed to prevent security vulnerabilities being injected into their code. One of the things that is, again, something that's pretty different from the industry from an incumbent perspective is that we believe it's really important to democratize security education.
(00:26:06):
We have been building this bunch of really high quality but bite size lessons about developer security that focus on developers about security issues and vulnerabilities and we surface them. Again, they're out there in the public domain. There's no paywall to get access to those. All the traditional solutions you need to sign up, you need to pay to get access beyond more than a couple. But these were just, they're all out there in the public domain. That works really well for us from a company generated company distributed loop as well.
Lenny (00:26:36):
So cool. SEO and then integrating to GitHub in an interesting way. Imagine there's also a lot of intra-company virality when someone uses Snyk at a company and they spread it to their colleagues?
Ben Williams (00:26:47):
Yeah, I mean, I didn't talk about those. I think those are pretty well understood. We have both referral loops and invite loops as well.
Lenny (00:26:55):
Okay, awesome. Coming back to what didn't work, and I think you mentioned that there was a monetization attempt that was self-service oriented and that had some challenges. Can you talk about that?
Ben Williams (00:27:06):
At the time, a few things were in place. Valuable product, check, strong developer user growth, check, strong retention, check, but the first self-serve monetization efforts only really saw traction with individual developers paying a hundred dollars a month. Or purchases in larger companies, they just didn't happen as everyone had hoped. There was a really critical part of Snyk's history. At the time a bunch of investors didn't lean in, perhaps shy away from early conviction with the founders on building strong usage without a proven path to monetization at that point. Ed at BOLDStart who I mentioned previously, he was one of the first kind of true believers and was I think really key in helping with providing runway during that time. But it was clear that there was a lot of work still to do. The team dived in, they really figured out what the constraints were and through that process really learned about the importance of catering for the broader governance needs of the enterprise buyer.
(00:28:07):
And that meant a couple of things. First, there was a need to build out table stakes features around governance at scale. Just things that companies of a certain scale and size expected reporting, robust user management and so on. And second that it was time to move beyond that depth first approach, right? That depth first approach was absolutely critical in getting to that point, but it wasn't good enough to take the next step. If you think about it, there's a point in a company scale where you start to see diversification of tech stacks and all of those tech stacks need securing. It's obvious in retrospect that only supporting developers using a narrow slice of those tech stacks wasn't going to meet the needs of the security teams who were ultimately the people who were held accountable for the security of their entire application estate. The teams worked hard over the next few months starting to build support for additional languages and ecosystems and adding those table stakes features.
(00:29:04):
I think back then Snyk were simply ahead of this inevitable curve of developer first security. At the time, the only buyers were security teams and dev first Security for the most part wasn't something that CISOs and ApSec leaders were driving. But if you look at Snyk through that lens of, as I mentioned, being a change agent, being a key piece of the transformational journey of our customers' DevSecOps journeys, you realize how important it was for us to start to build relationships with those security leaders. It was that time also that it was the right time to bring in the first sales and engineering hires as well.
Lenny (00:29:48):
You basically found it couldn't work self-serve, independent of sales being involved in convincing the folks at the top, which makes sense. How do you trust a company with your security if the people at the top responsible for security aren't bought in? Makes sense.
Ben Williams (00:30:04):
Today it's less like that. There are organizations where the buying center is still very much ApSec, but there are also many organizations where kind of technical leaders on the buying decision around security investments. What was always true though even back then was the influencing power of developers, regardless of where the buying center was.
Lenny (00:30:28):
And I imagine as the brand has grown, it's gotten easier to convince people like, "Oh yeah, look at all these other logos using this. It's probably going to be okay."
Ben Williams (00:30:33):
For sure.
Lenny (00:30:36):
Just to understand in your experience with Snyk, it never really worked self-served monetization. It worked as a way to get into a company and then developers started using it in small scale, but you needed sales and marketing to really grow monetization. Is that what you found?
Ben Williams (00:30:51):
I think back then, yes. Now it's a very different story. We have a lot of self-serve only customers scaling pretty large, so.
Lenny (00:30:59):
Got it. That's interesting. I rarely hear that you start out with sales being important and it becomes less important or I imagine it's still very important, but there's like a segment that has emerged that can self-serve. Fascinating.
Ben Williams (00:31:14):
Yeah, I think it is important to acknowledge though, that the product has always played a really key part in the sales process for sure.
Lenny (00:31:21):
That touches on something I wanted to ask. [inaudible 00:31:24] you've mentioned him a couple times, he's got this awesome newsletter, he talks about you guys all the time. I think he's very proud of the progress of Snyk and he talks a lot about that for developers, you got to win hearts and minds of developers to build something that works. Any lessons or pieces of advice for folks that are targeting developers to win hearts and minds and get engineers, developers excited about what you're building?
Ben Williams (00:31:47):
I think there's two things, right? First of all, fundamentally for someone to get excited about using a product, they've got to care enough, right? They've got to have a problem that you're solving. I think there's two things. One, there is a shift that is happening and still happening. I think there's still a long way to go for developers to really care about security as an integral part of their job in the same way they think about functional quality or performance. I think that we're still, we're making strong progress there. It's changing all the time, but there's still a long way to go there. But the reality is that I think in most companies, developers have to care about security because their companies need to be secure. The key then is how do I make the job of being secure for these developers, as painless as it absolutely needs to be?
(00:32:44):
And that means really meeting them where they are, integrating with their tools, finding ways to take security to them instead of trying to pull them out of their workflows. Flow is just this incredibly important concept for developers and you want to strive to keep them in that flow for as long as possible. The GitHub kind of pool requests are a great example of that. Someone can sign up for Snyk and they could theoretically be the only user of Snyk and connect their repos. All of a sudden we're protecting, securing those repos, a hundred, a thousand developers could be working in GitHub with that code, all benefiting from Snyk without necessarily needing to sign up. That's that example of taking the product to users without pulling them out of their workflows. I think that's absolutely critical.
Lenny (00:33:38):
As an outsider hearing all this, it's a product that magically helps you avoid security issues, very little work, does a lot of the work for you. It's hard to imagine it not working looking at it now, and I'm curious what it was about the early days that just felt like maybe that people didn't believe in this working. Is it just there was doubt that it would be smart enough to find your security vulnerability issues? Was it the timing wasn't right, people weren't ready, weren't concerned about security enough? What do you think it was that created challenges early on? Because looking back, it's like, of course this is going to work. How could it not? It sounds just like a magical all win product.
Ben Williams (00:34:16):
First of all, don't think the challenges were there in terms of the developer adoption. Even when those first kind of forays into self-serve were struggling in terms of breaking into some of the larger customers. The developer adoption, the free user base was still growing at a really good pace. That momentum was just constantly building and it's that momentum that has ultimately fueled the sales led business as we've gone through the years. But it was just those few things I think that I mentioned earlier in terms of stumbling blocks that needed to be overcome because when those first sales and marketing hires did join us and we started having conversations and we also tweaked some of the things in the product to meet, had some breadth, had some additional languages, ecosystems, building those table stakes features, then it really unlocked and it was rocket ship time from then.
Lenny (00:35:11):
Got it. Sounds like the biggest issue is monetization. Can we make money doing this? Developers love it, they're using it like crazy, but will people be convinced to scale this an inside an organization and pay us a bunch of money for it?
Ben Williams (00:35:21):
Exactly, yep.
Lenny (00:35:22):
Okay, got it. I want to dive a little bit deeper into your growth team and product team and how you think about organizing teams like that in a product led growth sales org. The first question, just how did the growth team start at Snyk? What was kind of the early days and then what does it look like today?
Ben Williams (00:35:41):
There were some ad hoc efforts happening in various places. We had a small growth marketing function, we had [inaudible 00:35:49]. We also had some ownership of key growth services in R&D. There was a team that owned the new user onboarding flows, for example. But it wasn't until I joined that we really formalized the notion of a growth team. It was very kind of ad hoc before then. When I joined, we created what we call the developer growth group now. Before then there maybe wasn't strong an understanding about what a growth team needs to look like, how they might need to work differently to the core product teams. And I'd say overall it was much later than you'd typically expect to see. And at a bigger scale. You normally are going to start growth teams, one or two people, three or four maybe, and scale out from there. But we started much bigger than that. But at the same time, this bottom up developer first approach, it was baked into the company DNA in terms of how teams think and operate. Yeah, we were growing fast even before we spun up the growth group. I think the significant change that happened there, it was a transition from a simple freemium approach to a holistic and well-coordinated PLG strategy. It's much more common to start earlier, much more common to start at a smaller scale than we did at Snyk, but it worked for us because of this kind of perfect storm of where we had a product with that bottom up growth built in from the beginning. We had founders with a deep appreciation for how the product could grow and there was strongly exec alignment and sponsorship for scaling the motion. The problem when starting the growth group, it was really for the most part more oriented to how we can get the flywheel spinning faster as opposed to getting it moving in the first place.
Lenny (00:37:26):
Where did you initially focus that team? Which part of the flywheel?
Ben Williams (00:37:30):
Right now we have dedicated teams focused on acquisition, activation and monetization along with a supporting team who own our growth platform, including all of our data and experimentation stack. But the macro structure, it's changed over time to enable us to focus on the biggest constraints in our growth model. At the beginning we just focused on acquisition and activation, intentionally deferring any investment into specific monetization initiatives around the self-serve revenue channel until we felt confident that A, we'd built the necessary growth muscles to scale, and B, we'd figured out some of the more pressing issues that were present earlier in the user journey. It was important that we felt really confident about our ability to effectively connect developers to Snyk's value in such a way that introducing and optimizing a self-serve revenue channel would make sense. I also really wanted to avoid one of the common failure modes I've seen around cross-functional collaboration and growth.
(00:38:28):
When I joined, there was an inherent tension built into the system. It was particularly noticeable between R&D and the growth marketing team. We had amazing people in both teams, a ton of really great ideas, but many of them were just not being executed on and it was leading to a lot of friction, a lot of frustration, ultimately caused by misaligned incentives between the different functions. When creating the growth group, we resolved this by ensuring that each of the growth teams were truly cross-functional in nature with everyone in each team aligned around common objectives and KPIs. Every team has engineers, an engineering manager, a product manager, a designer, a growth marketer, decision science support, and a basic shape of the growth teams that'll be familiar to most, but I spoke to a bunch of people over the last couple of years and I've actually learned to my surprise that inclusion of growth marketers in the product teams is not all that common. And I personally think there's just a lot of opportunity being missed there and I expect that to start to become the norm rather than the exception over time.
Lenny (00:39:32):
Okay. I want to talk about that, but before we get there, you said there's a decision science person on the team. What is that about? That's cool.
Ben Williams (00:39:38):
That's right. We started off from a fundamental BI data analyst perspective, but over time we wanted to apply a much deeper level of analysis on the data such that we could start to build in predictive models that could help us make better decisions and can ultimately fuel and power some of the end product experiences. Yeah, we spun up a decision science function and those folks are very smart.
Lenny (00:40:13):
Is that similar to data science or is that a separate ... Okay. It's cool that you call them decision science people versus data science, because that's so much more actionable.
Ben Williams (00:40:23):
Yeah, I think so.
Lenny (00:40:24):
Wow, that's cool. All right. I haven't heard that before. Makes me think of Annie Duke and all the stuff about how to make better decisions and I love ... Is this something anyone else does or is this something you came up with calling [inaudible 00:40:38]-
Ben Williams (00:40:37):
I'm not sure. I don't necessarily think what we are doing is revolutionary there, but maybe the name, I'm not sure.
Lenny (00:40:46):
Yeah, the name is cool. I haven't heard that before. It implies bias towards action versus just we're going to do a bunch of cool stuff with data. Interesting. Okay. Then you said that there's a growth marketer embedded in each team, so maybe just broadly what makes up these teams? Which you touched on briefly, then what have you learned is the value of having a growth marketer embedded within each team?
Ben Williams (00:41:06):
It's important to have balanced teams with strong diversity across multiple vectors. Focusing on functional diversity at the moment, which is kind of what you're asking about with having growth marketers on the team, one of the big benefits you get is a broader pallet of ideas, but also a bigger toolbox when it comes to execution, which generally translates in an ability in a growth team for them to test and learn faster with more parallel, yet at the same time, aligned threats. Perhaps I can give a recent example there. Having a growth marketer in an acquisition focused team led us to some lightweight experimentation on the website in creating an SEO optimized page. It was something that was really high performing, both from the perspective of traffic and conversion, but it didn't require any engineering resources to create. The growth marketer and the team, and they decided together this was something worth pursuing.
(00:42:01):
But the growth marketer was able to kind of execute that independently while engineers were working on other things. But then based on the success of that, the team went on to build out a functional sidecar product that allowed users to basically try Snyk without needing to sign up by simply placing their code in for us to scan and giving them some results there and then. We saw really great results with that visitor traffic, saw a significant increase, sign up rate dropped a little bit as we'd expect it would, but overall new users had a big bump and those users had much higher intent, which we saw play out with increased activation rates.
Lenny (00:42:37):
Awesome. Okay. And so there's essentially four teams under the growth umbrella. There's acquisition, activation, monetization, and then this kind of experimentation platform team. Is that right?
Ben Williams (00:42:47):
Yeah, that's right. And that team is also responsible for making that data available elsewhere in the organization as well. Product led sales is a really important motion for us, and so taking the knowledge we have, the insight we have around behavior with the users and their teams and their companies within the product, and making that available to the GTM teams outside in smart ways, allowing them to focus on the things that are most important to focus on. That's a really important part of what that team does.
Lenny (00:43:20):
It's interesting, you guys are the epitome of product life sales. That's this new trend of from PLG to PLS for sales. It's obvious that they're a big part of this whole process. The fact that monetization happens almost all through sales is interesting. That's interesting. Cool. Okay. That's not a question, just a thought, talking out loud. One other thought I had is, so you talked about SEO being a really important part of your growth. What is the person team like to do the SEO piece, the right content? I imagine they're on the acquisition team, there's maybe a content person that lives within that team.
Ben Williams (00:43:55):
We have actually one of, the smartest SEO people I've ever met within [inaudible 00:44:02].
Lenny (00:44:02):
What's their name? Let's give them a shout out if you want.
Ben Williams (00:44:03):
Anna. Yeah, cool.
Lenny (00:44:05):
Joanna.
Ben Williams (00:44:05):
Well, she's part of growth marketing, but she works extremely closely with the growth teams and she's got a few people in her organization and we bring them into specific SEO focused initiatives when we're looking to build loops around that. Incredibly important to have someone like that who understands that at a far deeper level than I could ever hope to, how SEO works. And particularly in terms of keeping on top of some of the things that Google are constantly doing in terms of their algorithm changes.
Lenny (00:44:37):
And does she actually do the writing for editorially, for I guess even the programmatically made pages or there's someone she outsources-
Ben Williams (00:44:43):
No, but what she does do a great job of is providing the kind of continuously updated guidelines on how content should be structured to lead us to good results.
Lenny (00:44:55):
Then it's just engineers and PMs that end up writing the things? Wow. Cool.
Ben Williams (00:45:00):
Yeah, that's exactly right.
Lenny (00:45:04):
This episode is brought to you by Vanta, helping you streamline your security compliance to accelerate growth. If your business stores any data in the cloud, then you've likely been asked or you're going to be asked about your SOC 2 compliance. SOC 2 is a way to prove your company's taking proper security measures to protect customer data and builds trust with customers and partners, especially those with serious security requirements. Also, if you want to sell to the enterprise, proving security is essential. SOC 2 can either open the door for bigger and better deals or it can put your business on hold.
(00:45:39):
If you don't have a SOC 2, there's a good chance you won't even get a seat at the table. Getting a SOC 2 report can be a huge burden, especially for startups. It's time consuming, tedious and expensive. Enter Vanta. Over 3000 fast growing companies use Vanta to automate up to 90% of the work involved with SOC 2. Vanta can get you ready for security audits in weeks instead of months. Less than a-
PART 2 OF 4 ENDS [00:46:04]
Lenny (00:46:03):
Can get you ready for security audits in weeks instead of months, less than a third of the time that it usually takes. For a limited time. Lenny's podcast listeners, get $1,000 off Vanta. Just go to vanta.com/lenny, That's V-A-N-T-A.com/lenny to learn more and to claim your discount. Get started today. What advice do you have for folks building growth teams and maybe either similar space or just B2B, PLS oriented businesses in general? What have you learned about what is important to get right?
Ben Williams (00:46:34):
This is a big topic. I have a lot of thoughts here based on what I've seen work well and also not so well. I think I can broadly bucket things here into maybe three main topics. So the first would be people and process. The second would be strategy, and the third would be data. Now they're all related and they all have to be working well to be effective in growth. Starting with people maybe touch the first element there in terms of balance teams, you've got to have those balance teams with diversity and ability to create great ideas, but also ability to execute. So that's the first thing.
(00:47:14):
But still on the topic of people, I have this kind of mental model, that potential that at its core is unbounded, but that a bunch of things situationally prevent people from fulfilling their potential. It might be how they're thinking about something. It might be organizational. It might be in relationships with coworkers or in broader team dynamics. It might be in them not even being in the right role even.
(00:47:37):
So fundamentally I think it's the role of managers and leaders to help them identify those things and work with them to find ways to thrive and grow. And I've seen this have particular significance in a growth org where people are just naturally less good fit. Now that doesn't mean that they're not amazing talented humans. It just means they aren't going to do their best work in a growth context.
(00:47:59):
So when you're starting a growth team, you'll often be doing so with internal moves. So this can be something that's maybe a little bit easier to miss than with external candidates where you are likely testing for those things explicitly during the hiring process. I'll share an example with developers.
(00:48:17):
So the devs that really thrive in a growth context are the ones that are motivated by moving quickly, iterating to create measurable impact. They're not attached to their work. They embrace imperfection as part of the process. They happily discard their code, their ideas even. They're curious and they're always looking for ways to be closer to their users.
(00:48:38):
Now those are the folks that generally make great growth engineers and I've also known incredible engineers that are most motivated when they're working on really deep technical challenges and love the process as much as the outcome. And they've struggled in growth. Of course it's never that simple in reality. There's nobody who's really at either extremity of that spectrum. But it's really important to try to answer the question, can this person do their best work in this environment? So I think that's a really key part of it.
(00:49:10):
And yeah, you need to also make sure they're well equipped from a kind of skills and knowledge perspective as well. So they need the right skills and knowledge to be able to do their best work in the context of your growth process. So the ideal state is that every growth team member has common vocabulary. They're comfortable with the growth process. They can work well with data and experimentation platform. They understand the data. They have the right skills and mindset.
(00:49:36):
Education I think plays a big part here. So we're big fans of Reforge, but we've also developed a bunch of internal programs to align and uplevel the teams. Something we learned, I think as an example, is the importance of starting simple and going deeper as the teams build experience. So for example, when it comes to experimentation, don't try at the beginning to introduce multivariate testing or concepts like sequential samplings and alternative evaluation approach.
(00:50:04):
Teams are still trying to just dip their toes in that... This water, it's kind of a recipe for a lot of mistakes. So that would be some advice there.
(00:50:15):
But people also need to be well aligned. I've talked about this actually on another podcast that I did recently. But what I mean by that is their execution needs to be aligned with an evolving growth strategy. The growth strategy needs to be aligned with and at the same time influence where the company's going. The growth strategy needs hooks into the product strategy and ideally there's some overlap and alignment of KPIs so that the growth teams and the core product teams are swimming in the same direction. The skills and experience in the team need to be aligned with the strategy. If you've got to focus on activation and acquisition, then someone who's a plans and pricing expert probably isn't the right set of skills at that point in time.
(00:50:57):
But you also, leaders need to plan to ensure those skills are available as focus of the growth team inevitably shifts over time. But at the end of the day, I think everyone needs to be able to easily answer the question why they're there. Why the work they're doing is important.
(00:51:14):
I don't know if it's too far off track here, but I have a vision and mission framework that I like to use that leads to I think, great simple statements of an imagined better future state and your role in getting there. So I can talk about that a little bit if it's a-
Lenny (00:51:28):
Yeah, let's do it. That sounds too good to pass up.
Ben Williams (00:51:31):
-Cool. So the vision is the nirvana state that you aim to enable for your users and customers in five to 10 years. It's something that could equally be enabled by your competitors if you don't execute effectively or efficiently or quickly enough. You can always prefix a vision statement with in the future, dot, dot dot.
(00:51:52):
Now it's something that should be bound to your target market. So not too wide and not too narrow. And critically it should not mention your company, your product, or anything solution related at all. Completely agnostic of those things.
(00:52:05):
And then the mission, that's the thing that you are going to relentlessly iterate on to take you incrementally closer to the nirvana state described in the vision. It should answer how you'll realize the vision by describing what your fundamental approach will be. In other words, what you will do and how you'll do it. It should ideally aim to encode any unique differentiating advantage you have. So if I think about Snyk at large when it comes to advantage, we might mention our unequal security intelligence and knowledge of application context.
(00:52:36):
And one of the neat things about this framework is if you find utility in doing so, you can apply it at every level from the company level all the way down to individual team. It doesn't mean the process is not difficult and you need to spend a lot of time, but it gives you this set of kind of a framework, a set of bounds that help you really come out with world crafted statements that kind of stand the test of time.
Lenny (00:53:00):
Is there an example you could share of the mission vision, whether it's Snyk or something else?
Ben Williams (00:53:03):
Yeah, yeah. I'll give you one for the growth group of Snyk. So great. The vision, every developer securely unleashes their creativity and the mission is to connect every developer and their organizations to the value of the Snyk platform with frictionless self-serve, adoption and expansion.
Lenny (00:53:19):
Interesting how the vision is so big beyond Snyk's current focus. And to your point, this kind of trickle down, right? There's a company vision and mission and it's the growth team's mission vision.
Ben Williams (00:53:32):
Yep.
Lenny (00:53:32):
Awesome.
Ben Williams (00:53:32):
Exactly.
Lenny (00:53:34):
I want to shift a bit and talk about your product work. So we've talked a lot about the growth org. I'm curious what the broader product org looks like. How many teams do you have? How do you structure it? Is it like product focused, user focused, outcome focused? And then just how does that team work with the growth team?
Ben Williams (00:53:53):
Sure. Happy to go into a bunch of that stuff. I know I'd mentioned earlier kind of three areas of building a growth team. I don't know if you want me to cover those other two. 'Cause we talked about-
Lenny (00:54:02):
Oh yeah, okay, let's do that. Let's finish that thread.
Ben Williams (00:54:05):
-Cool. So people and process was the first and we'll cover process really quickly. I think on the process side, at a minimum here you need well understood, documented growth processes, practices, working cadences. Teams in growth need to work differently in some ways from R and D teams working on core product, assuming otherwise, and just giving growth responsibility to an existing team without working with them to implement appropriate ways of working. I think it's a common track.
(00:54:31):
Ideally you get to a point there where the growth process is something that's continually refined and iterated on trying to build in more predictability. But what I've found I think most singularly most important in a growth process is facilitating a rapid learning cadence and providing the means to socialize those learnings, surfacing them in the right place at the right time so they can be leveraged and at the context. And if you think about experimentation, it's not about delivering outcomes it's about generating learnings that the organization can leverage effectively to deliver outcomes.
(00:55:05):
Might not be now, might not be tomorrow or some point in the future. But the sad reality is that without good process learnings easily end up unused and gathering dust. And you have to ask then what was the point? So as people in process and you know when that's on the right track, when you start to see enthusiastic sharing of learnings, when you see regular contribution of ideas coming from everyone in the form of well crafted hypotheses that are based on data and learnings. And when you see a wide variety of folks, just assuming end to end ownership of managing and running experiments instead of delegating that to the product manager or an engineer and tech lead. So yeah, that's people in process and strategy is-
Lenny (00:55:48):
Let me throw in a question real quick before we get to the last piece.
Ben Williams (00:55:50):
Sure.
Lenny (00:55:51):
So learnings, just to kind of touch on that. I've heard more and more pushback on the idea of learnings being an outcome. Because a lot of... As a leader, you're not going to be like, Cool, we learned so many things but nothing really got done. How do you think about the tension between, yeah, learnings we want to learn, but we also want to move metrics, grow the business and learnings are a way to inform decisions more than even just learn. How do you think about that kind of balance?
Ben Williams (00:56:17):
Ultimately you're there to create impact, right? There's no getting away from that, but learnings is the means. It's the same as, there's a quote that I love from [inaudible 00:56:27] around focus on the user's path to value not on monetization. Because if you focus on the form of the latter will follow, and that's the same thing with learnings and impact here. If you try and focus on the impact itself might struggle. If you focus on the things you need in terms of learnings to take you step by step, that will pave the path to creating impact.
Lenny (00:56:47):
I imagine your OKRs and goals are still like move this metrics some percentage, but you think of that as an output and the input is let's learn a bunch of stuff about what works and doesn't work and use that to inform what we're going to double down on.
Ben Williams (00:57:00):
Exactly. Yeah.
Lenny (00:57:00):
Sweet. Okay.
Ben Williams (00:57:02):
You got to focus on when you build a strategic opportunity, you are thinking about the outcomes, but you don't just go right to the end state. You've got to think about what's the quickest way we can test this hypothesis? And from there, what we learn from that and what do we take into the next set of the next set of experiments and it... You're paving this path along the way. You kind of that rough destination. How you get there, you don't know at the start. And that's what the path that the learnings take you on.
Lenny (00:57:31):
Cool. Okay. And then strategy we're talking about.
Ben Williams (00:57:34):
Strategy. Yeah, so strategy, it's a good one. At a very basic level, you need to be able to answer questions. How do you acquire users? How do you retain users? How do you monetize them? I know you talked with Elena on that in more depth, but from there you need more detail. It's going to guide the growth teams and where they look for strategic opportunity, how they approach that. The best way I've found to articulate a growth strategy that fulfills the promise of usefully guiding the team's execution, it's the loop based model, Reforge, as specific kind of documentation that I think is great around that.
(00:58:15):
Being able to identify the various micro and macro loops, how they're all connected, being able to document them in a qualitative model to communicate a shared understanding of how you grow. It's really powerful. Augmenting that then with the quantitative side of things, that helps guide quarter to quarter focus and ensure you can be intentional about where you're investing. That becomes a big enabler.
(00:58:40):
You're never going to have a shortage of ideas in a high performing growth team. So knowing where to focus amidst that kind of sea of ideas is a really important role of the strategy and fairly on, you'll probably have one or two core loops, but inevitably you'll need to layer on and connect new ones over time. And having a framework for doing that and having a framework for regularly revisiting that in the context of growth, team learnings, changes in broader company strategy, evolution of the product, new features being added, and so on. Market shifts, that becomes a big up level for teams to be able to create timely impact.
(00:59:19):
So the model you create there is what enables you to know at any time where the biggest constraints to your growth are and allows you to balance your growth investments accordingly. It's neat for sure. We've had times where we've focused on a broad set of constraints and opportunities and other times where we've had a much narrower focus. For example, on driving improvement to activation and engagement, even more narrowed like doing that through empty states, for example.
Lenny (00:59:44):
I want to unpack the strategy piece real quick. How do you operationalize this idea of you have this growth model, growth loop, you figured out here's the ways we're growing. How do you tactically connect that to a strategy? Is it, here's how we're growing, here's where we're going to focus this quarter, optimize this part of the loop, or is there some other way? You write it down, basically.
Ben Williams (01:00:05):
Very simply, it's first of all alignment on how you grow the different loops, how they work, the roles of different teams and the roles that they play in fueling those loops and getting them to spin faster. I think that's the first thing, having that common vocabulary and understanding.
(01:00:25):
Second is understanding the way they work in terms of what is constraining them, what are the inputs to them? What are the opportunities for making those loops spin faster? How can multiple loops work together in a macro context?
(01:00:41):
And particularly using the data there to be able to identify and understand and get alignment around where are the biggest constraints in your growth model overall and therefore where are the things that we need to focus on as a team over the next quarter or two quarters, and so on.
(01:01:01):
And that it's constantly changing. As I mentioned, there's a bunch of stuff that needs to feed back into that model in terms of growth loop performance or the learnings you're making and so on. That means it's changing and you're constantly reevaluating and it's guiding kind of quarter to quarter planning.
Lenny (01:01:19):
Cool. So just to make it even more concrete for folks that are listening. So one of your loops is this integration with GitHub where you automatically fix their code and create a PR. You may find at some point somebody clicking that link to becoming a user is too high friction, too many people are falling out. So one strategy for one of say the activation team could be we're going to optimize this part of the funnel. So when clicking from GitHub to sign up as a user and get them to a point where they found value, right?
Ben Williams (01:01:48):
Yep. That exactly that sort of thing. Or earlier on, for example, it might have been with that taken that same example of that same loop, and this is sufficiently far in the past that it's easy for me to talk about. But we start with GitHub. We want to now expand the scope of that loop. We've seen success with it. We see the performance of that loop growing, but we think there's opportunity in saying let's expand that by adding support for Bitbucket. And now all of a sudden we spin up that same loop with Bitbucket and then GitLab and so on.
Lenny (01:02:20):
Awesome. Okay. We could go a whole hour on just that piece, so we'll move on and we'll save that for feed two.
Ben Williams (01:02:26):
Data was the last thing. And growth team just can't function without data that even with early stage products, before you have the needed volume of traffic to be able to run formal tests in reasonable timeframes, you still need to have signals that help you learn and inform your decisions, both quantum and of course qu through speaking with users. My advice there is really just to invest early the infrastructure, the tooling then at a given scale, the dedicated people as well. They're going to be core to building out the growth team and they'll enable data to ultimately pretty much inform all critical decisions.
(01:03:01):
So Snyk was interesting that we didn't have a problem of not having enough data. In fact, there was an abundance of data, like too much. We collected absolutely everything. And the problem I identified very early was that we didn't have enough behavioral specific data and we weren't intentional enough about the data that we were collecting and how we were collecting it, which made the data hard to trust and that becomes a big problem.
(01:03:26):
So we invested in tooling and processes for building out event tracking plans, and now we test conformance to schema of the instrumented code in our CI processes. So we have absolute confidence in the data. So that was getting to a point of trustworthy behavioral data was absolutely key.
(01:03:43):
But the reason I say invest early here is that to remember that it also takes time to accrue enough data that you can learn about and make some key decisions around retention, for example. Also that you have enough data to run regressions on, be able to inform definition of your activation metrics or engagement states and so on. So the earlier you can start collecting the better. So yeah, people in process a strategy and data and you absolutely need all of those things to build and run an affected growth team.
(01:04:14):
When you get all of those things working, it's like rocket fuel for focus creativity, but at the same time slowing down to put the maturity in place as on all scales at the pace Snyk has it's pretty much impossible. You still have to get stuff done while you're kind of building all that stuff out. You have to accept that you're going to make a bunch of mistakes along the way. You have to be a hundred percent comfortable with that. And you have to treat those mistakes as learning opportunities that provide leaves for improvement.
(01:04:43):
And it's also useful to... You know, asked about KPIs and what the team are responsible for it. And that is one way in which a growth team absolutely needs to make impact and it's the way that primarily they're going to be held accountable. But it's also I think, useful to think about the efficacy of the growth org, not just in terms of the impact they drive our experiments and new product experiences and on core growth pick KPIs, but also how they enable and uplevel the rest of the org.
(01:05:10):
So for example, our entire product led sales process, it's powered by an evolving model that describes our understanding of users, teams, accounts, the usage and adoption patterns and signals, the best in form where and how our GTM teams focused. Insights from growth teams often have utility far beyond growth, but people can't know if something is useful to them if you haven't shared it with them. So the learnings made in the growth teams, even those from mistakes or failures, we socialize them widely and visibly.
(01:05:41):
We want every R and D team to be leveraging experimentation where appropriate to learn to create business impact. So one of the things we did here is creating a paved row for adoption of behavioral analytics and experimentation stack, coach teams on getting started to make it as easy as possible for anyone to start to reap the benefits of the platform, built out internal education programs on data driven development, on experimentation, built internal tools to help with metrics design and so on.
(01:06:08):
And then building core platform services as well that are useful for people outside of growth. So we built services that power contextual onboarding, and originally that was the intent, but now those same services can be used anywhere in the product to give contextual experiences. I know that was a bit of a ramble, but hopefully there's one or two useful things in there.
Lenny (01:06:29):
Yeah, there's two things I wanted to quickly follow up and then we can talk about the product team. You said you socialize learnings and experiment results. Is there anything you could share there about tips to do that? You have a tool you do use that for? Is there someone posts stuff in Slack? Is it an email that goes out? How do you actually socialize learning such that say a salesperson can do something with it?
Ben Williams (01:06:50):
Yes. So there's, first of all, there's a bunch of Slack channels like Synk runs on Slack basically. So there's a bunch of Slack channels. Even when we're planning experiments, those are kind of wide and in the open and we invite collaboration on those. But from a ceremony perspective, we try hard to institutionalize ways to generate and leverage learnings. It's something I feel pretty strongly about. So we have these team level impact and learnings reviews loosely modeled from a blog years back down, I don't know... Six years I want to say that Brian Balfour wrote about a similar ceremony from these HubSpot days.
(01:07:26):
And if I had to pick one meeting that as the most important in the growth team, it would be this. The teams continuously document any learnings from data exploration, from experimentation, from user research and so on. They document that in their weekly impact and learnings document.
(01:07:43):
Some teams find it better to pair up and advanced into dedicated learning sessions to deep dive on specific relevant topics. But however it comes together, it's all put into that document.
(01:07:53):
When it comes to the meeting itself, it's usually run by the pm. Most of it is spent discussing learnings that have been documented, their implications, how they can be leveraged in follow up work, where they might have relevance to other teams and so on. For relatively smaller part of the meeting is also spent looking at key metrics. Some teams have actually split that out entirely into a separate meeting. And then no time at all is spent reviewing what the team have actually been doing. It's more on kind of the outcomes and the learning. So that's at the team level.
(01:08:21):
But then we run that same meeting at the group level on a monthly basis. So that's run by the product engineering or marketing director for the growth group. And that's where all of the growth teams come together. They share some key learnings, can't share everything. Of course, what they're doing is picking specific learnings that have potential relevance in utility across the other teams. So also as a standing agenda item for our user research team to share what we call developer insights. That's one of my personal favorite meetings to attend. It's always recorded and socialize with the rest of the company afterwards. And yeah, I'd say that's really important, but there's a bunch of different ways in which we're filing out that information constantly.
Lenny (01:08:59):
So cool. And this is a meeting that anyone can come to like a sales person comes to.
PART 3 OF 4 ENDS [01:09:04]
Lenny (01:09:03):
And this is a meeting that anyone can come to like a sales person comes to see what interesting stuff the product team has learned recently from experiments. How cool. Would you be able to share a template of that document that you put together that we could include in the show notes?
Ben Williams (01:09:13):
Yeah, for sure.
Lenny (01:09:14):
Sweet. And then the meeting, you said it's run by basically like some of the product functions and ideas to share things they've learned in recent experiments, say in the past month.
Ben Williams (01:09:25):
So typically the team level ceremony, it's PM-led. That's from more from a facilitation perspective. The learnings are all brought forward by the various folks in the team and each one of them who's contributed to learning will talk about that learning with the group and facilitate the discussion from there. And then at the group level, those are read by the directors for the growth group and each team it might be an engineering lead, it might be a tech lead, it might be a designer, it might be the product manager. We'll talk about some key learnings from that month.
Lenny (01:09:56):
Makes sense. If there's nothing PMs are good at, it's facilitating meetings. So that makes sense. Okay. And so that's a good segue to just chatting a bit about the product org. I'm curious just like how you structure the product team and then how that works with the growth team.
Ben Williams (01:10:10):
That's good. So the product org, what do you want to know?
Lenny (01:10:13):
Broadly, how do you structure it? Just like how many teams do you have? Do you align it across by outcome or is it by surface area of a product? And then is the growth team like adjacent to this product org? Is it like a unit within the product org or is it integrated? But I don't think it is. So what does that look like org chart wise?
Ben Williams (01:10:34):
I think we've got a fairly common pattern for how we structure our product and wider R&D org. So most of the org functional ownership-based, there are a lot of really complex domains in the core product. So having that localized knowledge is important to be able to own and run the code that teams ship. The growth teams, on the other hand, are structured by outcomes. We talked about that already. Owning areas like acquisition, activation, engagement, monetization. These outcomes and team remits change over time as we talked about. But the teams here are often working on areas of the product where they don't own the code, which I think is the key difference between how we structure our growth teams and product teams with some exceptions. One of the growth teams actually own the onboarding flows and so on. So that does require a lot of trust.
(01:11:25):
It requires very transparent communication mechanisms built into how we work. One of the meetings that we have regularly is experiment plan reviews. They're ad hoc meetings. They're led by the experiment lead, could be the PM, could be anyone else in the team. But the important thing is a bunch of people will be invited there, especially stakeholders from other teams where we might be experimenting on their surfaces and that won't be the first time they've learned about this. We'd like to try and actually include them in co-designing the experiment plan so they're fully on board with it. But absolutely kind of inviting them into those experiment and views really key. If we're going to run an experiment on that surface, we need to make sure that everything in that experiment plan is watertight, especially from a scheduling perspective because the last thing we want is a week and a half into an experiment for some change to happen within that surface from the product team unaware that an experiment's happening and completely invalidate the experiment.
Lenny (01:12:26):
Cool. And then in terms of just org wise, do you have a lieutenant that is responsible for just say the product team and then someone responsible for the growth team or the directors report up to you and you have a bunch of reports? How's that structure?
Ben Williams (01:12:39):
Oh, so our CPO on the exec team [inaudible 01:12:43], he runs the entire product organization. He has four, I want to say VPs, that own different areas. So there's a couple of VPs that own different areas of the product. So first of all, our application security products. Secondly, our cloud security products. Third is platform. And fourth is what we call developer journeys, which is the area I own, which has a few groups within there, one of which being the growth group.
Lenny (01:13:13):
Got it. Okay. Makes sense. Okay. There's just a couple more questions I want to ask that are very tactical specific before we get to a very exciting lightning round to close this out. One is with a freemium product, there's always this question of what to put into free and what to put into the paid plan. Is there anything you've learned about how to think about that? What should be in free and what should be behind a paywall?
Ben Williams (01:13:36):
Was it on your show with Elena that she talked about things that promote your growth model being good to land in free and things that add friction? So I really like that guidance. I'll add that for many businesses there might be some cost of service element to consider as well. Providing a feature to free users is cost prohibitive due to the volume, then that's obviously something you're going to want to reserve for paid. Ultimately, that was the whole reason cited behind Heroku, recently removing their free plain entirely. I think your plans from free to the top, they should have well defined understanding of the target customer, the use cases they should map out or you should map out the motivations for motion between each. You're really clear about what are the drivers for someone to take a step from one plan to the next. For Snyk, the real drivers to move from free to a paid plan, for example, is when you want to secure business critical code and you start having needs around governance and compliance.
(01:14:39):
I think the other interesting dimension is of how you approach trials. Like with most things. I think we're still figuring that out at Snyk. I don't know that there's ever a perfect answer or even a correct answer here. Certainly different from product to product. We have a self-serve trial to support time box evaluation of some of the capabilities that are reserved for our paid plans. But we're intentional in revisiting the model periodically. It's important I think to regularly challenge yourselves to ensure you don't fall into the trap of simply assuming what was best fit in the past is best fit now and in the future. What if the trial duration was limited by some dimension of usage instead of time? Or what if we didn't have a trial at all but put more into the free plan with appropriate limits? How might making those changes impact our growth model?
(01:15:27):
It's not always easy to answer those questions, but I think there are some ways that you could can help test there for example. You might cohort trial users and teams who have low engagement and don't convert during the trial and then when the trial ends, drop them back into a new enhanced freak plan and monitor engagement there. So there're some things you do, but I think that habit of continuously challenging yourselves and reevaluating whether the model, the specific delineations between the plans and how you support evaluation and the motion between those plans, I think it's really important to do that. And also when it comes to PLG and sales, we talked about the self-serve motion. Obviously, it's big and important for Snyk, but the sales led motion critically large as well and significantly impactful. You need to think about the plan design and those motions across both aspects of PLG and the sales led motion. When you have a strong PLG foundation that is inclusive of a product-led sales motion, you're going to be in a really powerful position from the perspective of having a significant volume of highly qualified leads that are coming from the product. We actually track a metric that we call product-driven revenue, which basically accounts for all revenue in customers where we saw meaningful value-based activity in the product before there was any sales contact. And that really tells actually a super interesting story about the PLG efficiency of your company across all revenue channels, self-serve and sales-led. And what's fascinating there is that the product-driven cohort contribute a relatively greater amount to net retention. So when you think about packaging, you know really need to think about and understand that macro level contribution of the freemium motion and know what you're trying to optimize for balancing revenue today versus potential future revenue.
Lenny (01:17:28):
Is that increase in net revenue retention from product-led leads mostly because they start at a cheaper price, do you think? Or is it more that they just end up being better customers?
Ben Williams (01:17:40):
It's a great question. I'm not sure I have a good answer for that.
Lenny (01:17:45):
No problem.
Ben Williams (01:17:46):
I'm still trying to figure that out.
Lenny (01:17:48):
It's a good prompt to have people adding more customers in seats. You talked about the importance to figure out the trial length and what to put in the trial and free and things like that. Is there anything that just has surprised you? Something you've learned from iterating on that comes to mind?
Ben Williams (01:18:04):
I wouldn't say surprised me per se, but it's something that I think it's perhaps obvious in retrospect and that is that companies of different sizes, of different complexities of different industries from those that are very highly regulated to the other end of the spectrum, they're going to take different lengths of time to need to evaluate properly. So being able to cater for those in some way, whether it might be dynamic trial lengths or whether it be trial lengths that are based on usage or things like that, I think it becomes really important. That's something to be thinking about for sure.
Lenny (01:18:47):
Awesome. That's a great learning. I know Elena talks a lot about how trials often, screw you because you don't give people enough time to really evaluate it a company, so that makes sense. Last tactical question that I wanted to touch on is around activation milestones. I'm doing a survey right now with Yuri that I think will come out before this episode airs. But anyway, in real time, I'm curious how you think about setting what the activation milestone is for a new Snyk user. So maybe just share briefly how you think about what is an activation milestone? Why is that important? And then how you define that for Snyk? What is the milestone of a user is activated for your product?
Ben Williams (01:19:28):
First of all, what is activation? So for us, activation is indicative of the team forming a habit around the usage of Snyk. And when I say the usage, I actually mean deriving core value, which is ultimately fixing vulnerabilities. It's not just logging in. It's not even just finding vulnerabilities, it's fixing vulnerabilities. So building a habit around that. And the reason I say team instead of using them is, and we actually base most of our definitions of activation engagement around teams. It's really important because ultimately security is a team sport. That team might be one person, which case a user is equivalent to team, but often a team is multiple people and we actually expect different people to fulfill different parts of the team activation journey.
(01:20:17):
We also want to enumerate aggregate level activity around fix that sometimes happens off-platform where we can't explicitly measure it at the user level. So in the activation process, we have set up moments, aha moments and habit moments and our habit moments that we define as a team being activated, it's related to fixing vulnerabilities within 30 days of team creation. And the reason that is chosen, it's because there is a significant correlation with downstream. And in that case with activation three month retention and retention again based on, again, not just coming back and logging in but still fixing. So teams, that fix of vulnerability within their first 30 days are much more likely to still be fixing three months later.
Lenny (01:21:09):
That's really interesting. I love that. How did you come up with that number? Was there a decision scientist that looked at some inflection of at 30 days, and it's probably not exactly 30 in real life, but it's like a nice round number that's close enough, right?
Ben Williams (01:21:24):
Yep, that's it. So there absolutely was a decision scientist in involved thankfully. We had to collect a lot of baseline data first. So after we built out the data platform, we needed actually to wait for bit to build a good data set. We did a huge amount of quantum analysis, a lot of splunking of the data, applying ML models along with a bunch of supporting call research as well. But we started really with identifying the corpus personas and they used cases, different roles of different users within the team based activation journey, defining our retention metric, which is still fixing. It's whether a team is fixed. Along with natural usage behavior and expected natural usage frequency. And then we found the habit moment that ultimately most strongly correlated with improved long-term retention. And most of the numbers side of things came out of our ML ops platform.
(01:22:19):
But after that, we then worked back to figure out that's the habit moment. That's what we see as activation, but there's a set of steps that teams need to get there. So what's the aha moment before that? What's the setup moment and what are the individual steps that the team needs to go through to reach that set up moment? So that's the overall process and ultimately it's a really strong model that allows us then to feed in the set of user level behaviors that we know can influence those different steps on that path to activation.
Lenny (01:22:50):
Awesome. I'm excited to get this post out and that's a really good anecdote of how a company comes up with it and what they set. I also just thought of another question I may start asking everybody. I know I keep saying we're going to wrap this up, but here's a question and if it doesn't work, we'll get rid of it. You mentioned a bunch of tools that you use and I'm curious, if you had to think of what are the five most important/valuable SaaS products to your organization other than the obvious ones like Salesforce? What comes to mind?
Ben Williams (01:23:21):
When you say organization, do you mean Snyk at large or do you mean the growth?
Lenny (01:23:25):
Let's say, let's start with growth and see where it goes.
Ben Williams (01:23:27):
Okay. So I'm going to say Amplitude, first of all. Segment as a means to be able to get our data from the products to Amplitude and to everywhere else that cares about it. Whether that be a downstream BI system, Snowflake can looker on top of that, or system marketing automation systems like Marketo and stuff like that. So I'd say Amplitude. I will next say full story, which is absolutely fantastic for session replays of course. And it bridges that gap between [inaudible 01:24:11]. I would say userinterviews.com, which is comparable to usertesting.com, both of them amazing services in terms of getting fast curated access to individuals to participate in user research. Sprig is another one. So Sprig is a fantastic in-app survey platform, which is what we primarily use it for, but it also does a bunch of other cool stuff in terms of being able to test UX designs as well in-app. How many have I said?
Lenny (01:24:49):
I think four. If there's anything else, you could add a fifth. If not, we can move on. That's awesome. This is a really interesting list.
Ben Williams (01:24:55):
I'll stick it at four.
Lenny (01:24:56):
Okay. Is there anything for in the wider product team that also comes to mind that you guys find useful?
Ben Williams (01:25:02):
Airtable. In fact, Airtable for growth and product, just so flexible. It's just you can do anything. And in fact, if we think about growth, I should have mentioned that first because that's where we keep most of our experiment plans and knowledge base and our user research base.
Lenny (01:25:18):
Okay. I like this question. I'm going to start asking it. This is great. Okay. That was a precursor tour, very exciting lightning round. I'm just going to ask you a bunch of rapid fire questions, just answer whatever comes to mind. We'll keep it short and quick. Question one, what are two or three books that you recommend most to other people?
Ben Williams (01:25:34):
I have been dreading this question as there are too many. So I'm pick a couple that I've enjoyed reading in recent months. So for product and growth geeks like me, or in fact anyone with more than a passing interest in data, I'll recommend "How to Measure Anything" by Douglas Hubbard. Second up, you had Marty Cagan and he mentioned the book "Sprint" by Jake Knapp and John Zeratsky and I love that book, but personally their "Make Time" book. It was something that radically changed my relationship with information and I recommend that to all time staff, product people out there. And for number three, I'm going to say, "This is How They Tell Me the World Ends" by Nicole Perlroth, which gives an amazing view into the world of digital espionage.
Lenny (01:26:22):
Oh, I read that book. Tim Ferris recommended that at one point. That is a wild ass book. Very beautiful. Cool. I love these recommendations. All right. Great choices. Favorite podcast other than the podcast you're currently on
Ben Williams (01:26:37):
Maybe "Acquired" with Ben Gilbert and David Rosenthal. I just wish I had enough time to listen to them all.
Lenny (01:26:43):
They're very long. I was just at an event where they interviewed someone live as a live podcast. That was very cool. Those guys were pros. What's a favorite recent movie or TV show?
Ben Williams (01:26:54):
So a movie, "Turning Red" on Disney Plus, which we love watching with our kids. It was just fun. TV show, the most recent Curb Season had me in tears as usual.
Lenny (01:27:03):
They haven't had a new one in a while. So that's a little bit out there.
Ben Williams (01:27:09):
The new one's coming.
Lenny (01:27:10):
Oh, it is? I don't love watching that show. My wife loves it. Cringe, painful. But watch it anyway.
Ben Williams (01:27:19):
And my wife's actually the same. She can't watch it because she cringes too much.
Lenny (01:27:23):
We're reverse.
Ben Williams (01:27:24):
I love the awkwardness.
Lenny (01:27:25):
Oh man. It's good for a product leader to have that enjoyment. Favorite interview question that you'd like to ask candidates?
Ben Williams (01:27:34):
Give a couple here if it's not cheating too much. First is one I like to ask when hiring for anyone actually really it's fast forward three years. What's different about you then? A lot of people will default to telling you where they aspire to be in terms of role or title, but what I'm really looking for is signals of humility, of self-awareness around areas of personal and professional growth. So people who can be open about where they think they need to work on to grow themselves as people. I love that. Also, so there's just generally throughout interviews, I'm looking for curiosity. So day-to-day good PMs will be asking why as much as my six year old son does, which is a lot. So I'll try and discern that through the course of the conversation. It's not really a question, but something I'm looking for.
(01:28:27):
And then maybe I want to flip it because building on something that Adam Fishman was saying, his theme of evaluating the people dimension of folks you are potentially going to work with when you're interviewing with a company. And this was a question I got asked myself recently by a candidate, which I just thought would brilliant, and that was, "Tell me about the diversity, equity, inclusion, and belonging initiatives that you've recently personally been involved with?" And it just felt like a really great way for them to be able to test alignment of their personal values with those of someone they'd be working with really closely. So I love that.
Lenny (01:29:01):
Awesome. By the way, I love how many callbacks to other episodes you're making. You're definitely a power adopter of the podcast and I really appreciate that.
Ben Williams (01:29:09):
Okay, there we go.
Lenny (01:29:11):
Last question. Who else in the industry do you most respect as a thought leader, as a leader in general?
Ben Williams (01:29:17):
So maybe I'll cheat on this one a bit too, and I'm not going to combine it to the, when you say industry, I think security industry, but I'm going to look at the product domain and specifically product operations. And in my mind, there's not many people who know more in this area than Christine [inaudible 01:29:34]. So if you ever get chance to talk with her, I know that would be a fun conversation. Many gems would be dropped, I think.
Lenny (01:29:40):
Wow. I will get her on this podcast. That is my new goal. I had not heard of her and that's awesome. Thank you for the suggestion. Ben, this has been awesome. So many nuggets and stories and insights. I so appreciate you being here. Two last questions. Where can folks find you online if they want to reach out or learn more or maybe come work at Snyk? And then how can listeners be useful to you?
Ben Williams (01:30:04):
Firstly, I'm of course want to say a big thanks for having me on, Lenny. I love talking about all this stuff and really appreciate you being willing to let me bend your ear a little bit. As to finding me, I'm a bit of a Twit when it comes to Twitter. I generally spend a bit more time over at LinkedIn, but you can find me on both of those platforms @SemanticBen. And in terms of how people can be useful to me, I'm starting to take on some additional clients in advisory capacity, so feel free to get in touch if you think I could help.
Lenny (01:30:36):
I can't not ask about Symantec Ben and what the story is there and before we let you go.
Ben Williams (01:30:41):
Sure. It's actually when I was at IBM, it was a focus that I had on linked data.
Lenny (01:30:48):
Became Semantic Ben. All right. Awesome. All right. Ben, thank you so much for being here and thanks for listening.
Ben Williams (01:30:56):
Thanks, Lenny. Take care.
Lenny (01:30:59):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcast, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.
PART 4 OF 4 ENDS [01:31:22]
