---
guest: Scott Wu
title: 'Inside Devin: The AI engineer that''s set to write 50% of its company’s code
  this year | Scott Wu'
youtube_url: https://www.youtube.com/watch?v=gI0ZNhA0rvE
video_id: gI0ZNhA0rvE
description: '*Scott Wu* is the co-founder and CEO of Cognition, the company behind
  Devin—the world’s first autonomous AI software engineer. Unlike other AI coding
  tools, Devin works like an autonomous...

  '
duration_seconds: 5552.0
duration: '1:32:32'
view_count: 19857
channel: Lenny's Podcast
keywords:
- product-market fit
- growth
- onboarding
- churn
- roadmap
- iteration
- revenue
- hiring
- team building
- management
- strategy
- mission
- competition
- market
- persona
---

# Inside Devin: The AI engineer that's set to write 50% of its company’s code this year | Scott Wu

## Transcript

Scott Wu (00:00:00):
Our whole team is only like 15 engineers a year. We use a ton of Devin when we're building Devin. Most folks on the team are definitely working with up to five Devins at once, and so Devin merges like several hundred pull requests into production in the Devin code bases every month.

Lenny Rachitsky (00:00:12):
What percentage of your PRs are Devin versus humans right now?

Scott Wu (00:00:16):
It's in the neighborhood of a quarter or so.

Lenny Rachitsky (00:00:19):
Where do you think this will be at the end of the year?

Scott Wu (00:00:21):
Honestly, we expect it to be a decent bit more than half.

Lenny Rachitsky (00:00:24):
You guys are so ahead of how companies work with AI engineers.

Scott Wu (00:00:28):
AI is going to be the biggest technology shift of our lives, so most of the big tech revolutions that we've had over the last 50 years, like personal computer, and the internet, and the mobile phone, they all had this big hardware component that was a big part of the distribution. Folks who were building for those industries kind of saw their market grow and grow and grow basically steadily year over year as the number of people with mobile phones increased, right, as the number of people connected to the internet increase. One of the things which is already I'd say different in AI, is just how explosive the technology can be. There's no weight on hardware distribution. It means that the space is just growing so exponentially.

Lenny Rachitsky (00:01:02):
How is the act of being an engineer and building changing?

Scott Wu (00:01:05):
I think there's going to be way more programmers and way more engineers a few years from now. Pretty quickly. The form factor of what it means to be a programmer obviously is going to change, but at the end of the day, of course the discipline is all about just being able to tell your computer what's do. And so in that lens, I really think that programming is only going to become more and more important as AI gets more powerful.

Lenny Rachitsky (00:01:20):
Today my guest is Scott Wu. Scott is the co-founder and CEO of Cognition, which makes a product called Devin, the world's first autonomous AI software engineer. Unlike other AI tools that I've highlighted on this podcast, Devin is designed to act like an actual remote engineer that you chat with like you would with any other human engineer through Slack or through its dedicated website. When Devin launched about a year ago, it was very much a junior engineer. Over the past year, they've made a lot of progress and Devin is now being used by tons of companies in production. We chatted about how their engineering team of 15 uses Devins to build Devin, including how every engineer uses about five Devins each to help them code and move faster. How a quarter of their pull requests today are committed by Devins and that they expect this to be over 50% by the end of the year.

(00:02:05):
We also talk about how Scott imagines software engineering is going to look in the future and how the role of an engineer changes from a coder to an architect. We also get into the eight pivots that they went through before landing on this path, why Scott believes AI tools like this will lead to more engineer hiring versus less. Also where the name Devin comes from and so much more. This episode is going to blow your mind. I highly recommend you listen to it if you're at all interested about where engineering, product building, and AI is going. A huge thank you to Claire Voue for suggesting a bunch of great questions for this conversation.

(00:02:38):
If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become an annual subscriber of my newsletter, you get a year free of Linear, Superhuman, Notion, Perplexity, and Granola. Check it out at lenny'snewsletter.com and click bundle. With that, I bring you Scott Wu. This episode is brought to you by Enterpret. Enterpret unifies all your customer interactions from Gong calls, to Zendesk tickets, to Twitter threads, to app store reviews and makes it available for analysis. It's trusted by leading product orgs like Canva, Notion, Loom, Linear, monday.com, and Strava to bring the voice of the customer into the product development process, helping you build best in class products faster.

(00:03:19):
What makes Enterpret special is its ability to build and update customer specific AI models that provide the most granular and accurate insights into your business. Connect customer insights to revenue and operational data in your CRM or data warehouse to map the business impact of each customer need and prioritize confidently and empower your entire team to easily take action on use cases like win-loss analysis, critical bug detection, and identifying drivers of churn with Enterpret's AI assistant Wisdom. Looking to automate your feedback loops and prioritize your roadmap with confidence like Notion, Canva, and Linear visit E-N-T-E-R-P-R-E-T.com/lenny to connect with the team and to get two free months when you sign up for an annual plan. This is a limited time offer. That's enterpret.com/lenny. Many of you are building AI products, which is why I'm very excited to chat with Brandon Foo, Founder and CEO of Paragon. Hey Brandon.

Brandon Foo (00:04:15):
Hey Lenny. Thanks for having me.

Lenny Rachitsky (00:04:17):
So integrations have become a big deal for AI products. Why is that?

Brandon Foo (00:04:21):
Integrations are mission-critical for AI for two reasons. First, AI products need contacts from their customer's business data such as Google Drive files, Slack messages or CRM records. Second, for AI products to automate work on behalf of users, AI agents need to be able to take action across these different third-party tools.

Lenny Rachitsky (00:04:40):
So where does Paragon fit into all this?

Brandon Foo (00:04:42):
Well, these integrations are a pain to build and that's why Paragon provides an embedded platform that enables engineers to ship these product integrations in just days instead of months across every use case from RAG data ingestion to agentic actions.

Lenny Rachitsky (00:04:57):
And I know from firsthand experience that maintenance is even harder than just building it for the first time.

Brandon Foo (00:05:01):
Exactly. We believe product teams should focus engineering efforts and competitive advantages, not integrations. That's why companies like You.com, AI21 and hundreds of others use Paragon to accelerate their integration strategy.

Lenny Rachitsky (00:05:15):
If you want to avoid wasting months of engineering on integrations that your customers need, check out paragon@useparagon.com/lenny. Scott, thank you so much for being here and welcome to the podcast.

Scott Wu (00:05:29):
Thanks so much for having me. Excited to be on.

Lenny Rachitsky (00:05:31):
I'm really excited to have you here because you are building and you've been building something that is very different from what a lot of other AI companies have been doing for a long time, although they are starting to converge to where you guys are now. We're going to talk about that and it's also just such a unique point in the history of AI and just the journey of AI. And so it's really cool to be chatting right now. And I feel like we're going to chat again in a few years and be like, wow, we were so right about so much and so wrong about so much.

Scott Wu (00:05:59):
Yeah.

Lenny Rachitsky (00:06:00):
And so I'm excited to have you here. Let's start with talking about Devin, giving people an understanding of just what the heck Devin is, is the main product that you guys build. What is the simplest way to understand what is Devin?

Scott Wu (00:06:10):
Absolutely. And so Devin is a fully autonomous software engineer that is going to work on tasks end to end, and so there are a lot of great tools for all parts of the stack of the AI code workflow. What Devin does is it is a full asynchronous workflow, and so you can tag Devin on an issue in Slack, you're talking about an issue and you tag Devin, you can tag Devin in Linear, you can have Devin and Devin will make pull requests in your GitHub, and so it's very much built to work with engineering teams as your junior engineer.

Lenny Rachitsky (00:06:38):
Amazing, okay. So I remember when you guys launched this, there was this big pitch of this is your new AI engineer and it was really good at a lot of stuff. It wasn't great at other things. It's been a year now about since you guys launched, is that right?

Scott Wu (00:06:50):
Yeah, yeah.

Lenny Rachitsky (00:06:51):
What's the best way to think about the level of seniority that engineer had back in the day when you guys launched and then the level of seniority of engineer today if that's, I don't know, measure of how to think about Devin?

Scott Wu (00:07:02):
Yeah, and it's crazy to think about by the way, because a year ago when we did the initial launch, I mean people didn't really believe that an agent was possible. Right. And it was, I mean, it was a very different time. So like start of 2024, things with model capabilities were definitely quite a bit earlier on, reasoning especially was quite a bit earlier on. And yeah, I mean, in the time since then it's obviously developed a lot. I think in terms of practical skills, there's some comparisons we make. Sometimes we kind of say, well, when we got started it was kind of like a high school CS student and then as time went on, it became more of a college intern and now it's like a junior engineer. But I would say though that those are more rough guidelines because I really like the phrase jagged intelligence for example, because obviously there are certain things that it is much better at than a human. There are certain things that it's much worse at than a human.

(00:07:52):
And I think over the last year we've learned a lot especially about not just coding agents but agents in general just really building out how all of us should be working and interacting with agents as part of our flow. And so a lot of the things that we built, I mean, there was no Slack, there was no GitHub integration, there was no Linear, there was no interactive planning phase working back and forth. There was no way to touch up Devin's code. And so a lot of the features that we've built on the product side since then have really been about basically yeah, figuring out how to make working with Devin and handing off tasks to Devin as smooth of an experience as possible.

Lenny Rachitsky (00:08:27):
That's so interesting. So a lot of the work has gone not into how do we just make Devin the best possible engineer, but it's how to work with this new type of entity that we haven't ever worked with.

Scott Wu (00:08:37):
I think it's a 50/50 of both. I think the capabilities obviously have improved a ton and we've seen these get better and get measurably better. But I think the other side of it is everything to do with yeah, really the product interface and the tools and so on. And I think today folks generally know how to use chatbots and to with chatbots, right, and that's an interface that people are familiar with and obviously with agents it's still like a real curve, I think to learn how to use them and how to get the most out of them. And so it's really exciting to see a lot of others starting to build and do a lot more in the agent space as well. But I think this is the kind of thing that we're all really figuring out together as a space.

Lenny Rachitsky (00:09:15):
What can you share about just the scale of Devin at this point, whatever you're comfortable sharing, and then just where do you think the level of Devin's coding abilities will be in a year?

Scott Wu (00:09:24):
So we work with companies of all stages and sizes. On the smallest end, it goes to startups of just one or two people who are using Devin to build out a lot of their kind of initial prototype or initial product all the way up to big public companies, Fortune 100 companies or public banks or things like that who are using Devin across their engineering teams. In general, we've seen a huge range of the use cases there. And obviously the kinds of engineering work that you're doing at a one or two person startup, they're very different from the kind of work that you're doing at a public bank.

(00:09:55):
But throughout it's all been basically yeah, being that junior buddy of yours that makes you go faster and really multiplies you, I would say. I think it can multiply you as an engineer obviously by just letting you work with your own team of Devins instead of having to be kind of fully synchronous on a single task. And then it's also kind of multiplying your team and multiplying your team's knowledge base because Devin really accumulates a lot of the knowledge from working with every member of your team and is able to bring that into each new session.

Lenny Rachitsky (00:10:23):
Awesome. We're going to show people how it actually works later in the podcast. We're going to do a few live demos, but let's actually go to the beginning of the journey. What's just the origin story of Devin? How did this all begin?

Scott Wu (00:10:33):
The founding team, I mean most of us have known each other for years and years and years actually. And for almost everyone, this is our first time working together, but we've known each other a long time. And we all actually had our own kind of journeys in AI for the last decade or so. And so for myself, I ran a company before this called Lunchclub, which was an AI for a professional networking product and I ran that for about five years. And one of my co-founders, Steven was one of the first engineers at a company called Scale AI, which has obviously grown a lot and done very well. My other co-founder Walden, was an early engineer at a company called Cursor, which has also obviously grown a lot and done really well. And our whole team was kind of like that. Many of us knew each other from competitive programming and math competitions, but we had stayed very closely in touch in the decade since then and we've all kind of all had our own journeys.

(00:11:22):
And so we had one person who was running teams at Neuro, we had one person who was at Waymo, someone who had their own YC tools startup for machine learning, and we were really excited to build something together. And this was around late 2023, so about a year and a half ago at this point. And yeah, when we got started, I mean I think there were a couple of things that we felt really strongly about and one was that reinforcement learning was really working and was going to be the next big paradigm shift in capabilities. Back then it was the initial ChatGPT launch in 2022, and those models were, to first order were what we would call imitation learning in AI, right, which is basically you have the model read all the texts that you can find on the internet and then train it to talk like somebody on the internet would talk. Right. And there are kind of obviously a lot more details on top of that, but that's kind of the first order pass of what was really done.

(00:12:16):
And it was amazing. Right. I mean, it passed the churn test, it was able to respond and to have encyclopedic knowledge about a lot of things. And I think this new paradigm which we've gotten into over this last year or year and a half is really high compute RL, which is a very different paradigm, right, which is basically the ability to go and do work on task and put something together and then be evaluated on whether that was correct or incorrect and use that knowledge to decide what to do and to learn from that. Right. And so we felt very strongly that that was going to happen. I think for us, code was the natural thing to work on for a couple reasons. One, because we're all programmer nerds ourselves, and so teaching AI to code is about as cool as it gets for us, but also because code has this whole automated feedback loop, right, where you can run the code and that is the kind of automated feedback that really feeds into the RL, which makes these models so great at coding.

(00:13:06):
And then the other thing that we felt very strongly about was that the product experience was going to shift from what I'll call text completion to agents basically. Right. And to first order, I would kind of say there's been a lot of great experiences in text completion. It's been used for marketing, it's been used for customer support, it's been used for education and in Coda obviously as well. The GitHub copilot was kind of really the dominant product of that initial wave. Right.

(00:13:34):
But I think that the big shift that we really felt we would see is moving from kind of this text to text model to an actual autonomous system that can make decisions, that can interact with the real world, that can take in feedback, that can iterate and take multiple steps to solve problems. And now we call that agents, but that was what we were really excited about at the time. So it was always coding, it was always agents. And in some ways that kind of feels like it should have been cleared from the start. But even with that, I feel like we've pivoted eight times or something within coding agents over the last year and a half, so.

Lenny Rachitsky (00:14:08):
I just noticed recently all the AI, top AI companies sort of, not all, but many of them, the product that is winning is different, has a different name from the company, which is not typical, Cursors, Anysphere, Bolt, StackBlitz, you guys are Cognition Labs, like V0 is Vercel. And it just tells me these all emerge later in the company's journey and they tried a bunch of stuff and like, oh wow, this thing worked and it's so interesting that it's so common amongst these top AI companies.

Scott Wu (00:14:34):
Yeah, and there's even, I mean OpenAI, ChatGPT, Anthropic and Claude and Google. Yeah, it's funny. Yeah, yeah, I agree. So when we got started, it wasn't even really a company. I mean, it was more like a project or a hackathon almost. We got a bunch, we booked an Airbnb basically for a couple of weeks. This was around Thanksgiving time and just got a bunch of people together who were just excited to hack on some projects and build something cool. And it's funny, actually the first thing that we were building for actually was more solving these more contest programming problems and using an agentic loop to really do better on that. And so obviously if you run your code on the test cases, you can evaluate, there's a lot of agentic work that you can do there to try and do better, and that we spent some time on that initially. And then we've kind of gone from, I mean the story of the whole company for us in some sense has been going from hacker house to hacker house.

(00:15:26):
So after that we had another hacker house and that's where kind of some of the initial ideas for Devin came and really building a software engineering agent and not just a coding agent and having to interact with a lot of these tools, but even then there were so many iterations. And even the idea of talking to Devin for example was like, it was something that we had to come up with. Right. Initially, it was just like you hand off a task and then it works and then it shows you this whole finished code. Right. And now obviously it's like you can jump in at any time, you can get feedback on the plan, you guys can scope out the task together when you're working with Devin. And a lot of these things we had to develop obviously, and certainly we've learned a lot about the use cases, the form factor. We've made a lot of big improvements and step function improvements on the capabilities and Devin's ability to use tools and to bug and make decisions.

(00:16:11):
And so it's yeah, it's been a fun journey. I mean, I think I would say that the grounding question for us really, which is one that we think about all the time, is really just what is the future of software engineering and how should we be working with AI to write code? Because I think at the end of the day, of course that's what underlines all of the product decisions that we make, so.

Lenny Rachitsky (00:16:34):
I like that you're asking the juicy question I wanted to get to. Before I ask it just for the history books, when did you guys start kind of hacking around and when did Devin launch? How long was that period?

Scott Wu (00:16:45):
Yeah, so we started in November of 2023, which was then yeah, just like hackathon mode. We officially made it into a company around the start of 2024, and then our initial launch was in March. And so it was like nonstop, I mean it's been nonstop for the entire last 17 months, but it's getting to the launch and then obviously working with enterprises and developing the product a lot more, building it and getting it to work for a lot of practical use cases and then making it fully available self-serve in December of last year. And now we've rolled out 2.0 obviously just a few weeks ago. And so it's been a very busy time for us.

Lenny Rachitsky (00:17:25):
Understatement of the century. Let me ask this question because you touched on it a bit, this whole idea of Devin as a person and this idea of creating a personality for Devin. It's unlike any other, I believe, AI app. No one else has a name and you don't think of it as a person. What made you guys decide to go that approach and just how do you design it to work well that way?

Scott Wu (00:17:44):
I would say it's a decision we're pretty proud of, I would say. I mean, I think there's a lot of different product experiences out there, and I think the thing that really makes Devin unique in what it does is that you can really hand off and more and more what we've seen honestly is that I think a lot of kind of explaining the Devin experience to folks is really just explain it as, yeah, this is your junior buddy. And that goes for a lot of the parts of the flow where in the onboarding for example, initially I would say we've definitely had a lot of users come in and just kind of see the blank screen and not really know, or they'd ask, "Hey, I'm going to do this whole big re-architecture, the whole code base."

(00:18:21):
And basically what we've learned over time is to basically get folks to think more like whoa, whoa, whoa, let's work on getting the repository set up first. Let's make sure we hand Devin a couple one pointer tasks so it can get familiar with the code base. Let's get it the thing. If Devin needs to be able to test the code or run the linter or CI or things like that. Obviously we want to make sure Devin's got its own virtual machine set up to be able to do that.

(00:18:45):
And similarly, I think the usage pattern, I think often it wasn't clear and obviously you can sit and just kind of watch Devin do it action by action and work that way, but we found that the best workflow really as a team building a lot of stuff was to work with multiple Devins and to run them asynchronously and to kick them off and to only jump in basically as you needed to provide feedback or steer the plan or anything like that. And so in many ways, I think Devin as a name really is our attempt to kind of capture the soul of that as a product where it really is treating it like a bit more of an autonomous entity that you can hand off tasks, that you can work with, that you should be teaching and learning with over time.

Lenny Rachitsky (00:19:29):
I want to come back to an area you started us down and then I took us away from which is impact on software engineering and how software engineering is going to change. So there's kind of two parts to this. Just like when people are using Devin today, say this year, how is the act of being an engineer and building changing for those companies? What does that look like?

Scott Wu (00:19:49):
By the way, we're all software engineers ourselves. It's like I'm a programmer by training and still a programmer at heart certainly. And I think the way that we've always thought about it is there's layers of abstraction and there's tools, and one way I would say it at a high level is kind of I think of AI in general as, yeah, I mean computers are obviously getting more and more intelligence and are able to do more and more and it's possible there may come a day where computers truly do everything that we do and humans are not responsible for any of it.

(00:20:20):
I don't expect that to come particularly soon, but I guess what I would say is until that point, for as long as we're still part of the equation, one of the most important things to do obviously is for us as humans is to instruct our computers on what we want and what we want to build and what we want to do. Right. And software engineering is, we think of it today obviously as Python and C++ and JavaScript and all these things, but at the end of the day, of course the discipline is all about just being to tell your computer what to do. And so in that lens, I really think that programming is, if anything, is only going to become more and more important as AI gets more powerful. And I think the thing that's really exciting for us is yeah, it's really seeing that kind of iterative transformation. And so you ask what things look like today, and I would say, yeah, it really is like having a junior buddy or really a team of junior buddies that you can work with. Right.

(00:21:12):
And so every engineer on our team, we use a ton of Devin when we're building Devin, and so Devin merges several hundred pull requests into production in the Devin code bases every month, which is, I mean, our whole team is only 15 engineers, and so it's a pretty sizable fraction of all the code that we write. And the way that we use it is basically, yeah, everyone's got their whole team of Devins. If you're going to be looking through various issues, if you're going through feature requests, if you're going through bugs, if you're going through new paradigms that you want to build, then it is naturally the case that there's a lot of handoff points where you just say, "Hey, at Devin, here's what's going on. Can you please take a pass at this?" Right.

(00:21:47):
And sometimes Devin will be able to do the task 100% autonomously and just makes the PR and then you merge the PR and that's great. Sometimes you want to be able to jump in for the 10 or 20% that really needs your help. Maybe there's a few details with how exactly you want to scope it or how you're architecting this feature, or maybe you want to go and test the front end at the end yourself to make sure it looks exactly the way that you want and give your one or two lines of feedback after that. Right. But a lot of it is really yeah, is kind of like yeah, learning to work with Devin to be able to just do more in parallel and build more.

Lenny Rachitsky (00:22:20):
What percentage of your PRs are Devin versus humans right now?

Scott Wu (00:22:25):
Yeah, I'd have to look, but it's in the neighborhood of a quarter or so of all of our-

Lenny Rachitsky (00:22:30):
Wow.

Scott Wu (00:22:31):
Yeah. Yeah.

Lenny Rachitsky (00:22:33):
And then what was it like six months ago?

Scott Wu (00:22:35):
Oh yeah, it's grown a ton for, I mean, we've seen it grown exponentially internally ourselves as well. And so it's kind of an interesting one where again, it's always both the capabilities and the product interface. And so I think the intelligence has increased a lot. But the other thing of course is that we've spent a lot of time in figuring out how to build and to really kind of build for an interface where you can get Devin's value on tasks where Devin is able to do the 80 or 90%. And so Devin is obviously not perfect and it'll make mistakes and so on. And a lot of the question is basically, yeah, how do you scope out your initial task with Devin and then just kind of set Devin off and have it go and do the things that you want do? How do you come in at the end and review and give feedback? How do you make sure Devin learns over time? How are you able to kind of just check in as needed and course correct if you want to?

Lenny Rachitsky (00:23:24):
Okay, so today about quarter of your PRs are Devins. Where do you think this will be at the end of the year? What would you guess?

Scott Wu (00:23:31):
I think by the end of this year, we expect it to be more than half. And I mean, as time goes on, one of the things that we've seen is just you're able to do more and more and more work asynchronously. Right. And you're able to hand off more and more. I think the soul of programming, the soul of software engineering has really been about through all the areas, not just now, but even when it was assembly, right, and even when it was Pascal and even when it was punch cards or whatever, I think the soul of it has really been basically just about defining the problem that you're facing and really thinking through exactly...

Scott Wu (00:24:00):
... about defining the problem that you're facing and really thinking through exactly what is the solution that you want to build. Thinking through the architecture, thinking through the details, and really mapping out in your mind exactly what you want to build basically and what you want to have your computer do. I think that's what makes software engineering really great and I think that's the funnest part of software engineering. 

(00:24:21):
I think, at the same time, that's probably in the neighborhood of 10% of the average software engineer's time, right? Because 90% of the time is you've got this Kubernetes error, then you've got to debug, and you have to see what went wrong and the system crash, or you left some port open and this is messing up, or there's a bug report that you have to take care of, or you've got to migrate your code, or you got it upgraded to a new version or things like that. A lot more implementation. 

(00:24:48):
One of the ways that we've kind of thought about Devin in building Devin is really allowing engineers to go from bricklayer to architect, so to speak. A lot of it is just getting to the point where you can do the high-level directing and you can basically specify things exactly how you want. I think it's very much about still having the human in control and having the human able to do the full specification, but just multiplying the magnitude of what you can do and what you can build in one day or one hour or however long.

Lenny Rachitsky (00:25:18):
In the future, say someone is trying to get into software engineering, thinking about becoming an engineer, first of all, do you think people should... Classic question everyone's getting these days. Should you still learn to code? 

Scott Wu (00:25:29):
Yeah. 

Lenny Rachitsky (00:25:30):
I'd love your perspective there. And then two, for people that are engineers today, what skills do you think will be more and more important and then less important in this discussion of moving from bricklayer to architect? 

Scott Wu (00:25:41):
Yeah, for sure. I love this question. First of all, the question of whether you should still learn to code, my answer would be absolutely yes. I think, to a large extent, when you take computer science classes and when you learn these fundamentals, sure you're learning a little bit about how a particular language is, syntax works or something like that. But honestly, most of what you're learning really is about the ability to logically break down problems for number one. And two, I would say is just the model of a computer and a lot of these decisions and a lot of the abstractions that we've built over time. 

(00:26:11):
What is a database and how should you think about a database? What is a garbage collection system and how do those work and all of these different pieces? The reason I think that's important is because it's the same with a lot of these other... Arguably we've already gone through these phases in programming and I think this next one is going to be somewhat faster and somewhat bigger, but in many ways a similar flavor, which is when you work with Python today, obviously, a lot of things are already abstracted away from you.

(00:26:38):
In some sense, someone from 50 years ago might already call Python. You just get to explain in English what you want and now the computer does it for you. That's great and I think it's really powerful. It's opened it up. I mean, we have far more programmers, obviously, than we ever have before because of that, but I would say certainly as you're building your skills as an engineer, it really helps a lot to understand the abstractions and to be able to peel the layers beneath. Folks will use assembly for example if they're really performance optimizing a piece of code, but also in order to build good systems and to understand these things, you certainly want to understand these abstractions of how does networking work. 

(00:27:18):
What is TCP/IP like exactly or what happens with this Python code when it gets interpreted or all of these details. Similarly, I think we will get to a state where, with no experience at all, you're going to be able to build some pretty cool stuff and to do some pretty amazing work just by explaining what it is that you want. But I think that, for quite some time, you really want to be able to think precisely about the details, to peel back the abstractions, to be very precise about what it is that you want to build and how.

Lenny Rachitsky (00:27:48):
And then for skills that you think are more and more valuable for engineers, where should engineers today be leaning more and more into versus like, "Forget this. I don't need to think about this anymore"?

Scott Wu (00:28:00):
For sure. I think architect... I mean, we already have a term for architect and engineering and I think it is directionally the right term. It's, I think, one thing to just do a routine implementation and write boilerplate code and things like that. I would say that, in many ways, AI coding has already made us much faster at that, but I think a lot of the core questions of understanding very complex systems and working in the context of the whole company and thinking about the product that you're building or the work that you're doing and understanding, "Okay, what are the problems that we want to solve? How do we want to solve those problems? What is exactly the solution that we want to build? What are all of these key decisions and trade-offs that we're going to be making?"

(00:28:40):
Basically, I think folks who are able to do that really, really well are just going to be able to leverage themselves more and more. If anything, I think there's going to be way more programmers and way more engineers a few years from now than there are today. I think pretty quickly the form factor of what it means to be a programmer, obviously, is going to change. And in some sense, it already has, but I think there's just going to be so much more for us to build. Folks talk about Jevons Paradox all the time. I mean, software is truly the shining example of Jevons Paradox, where we have always managed as a society to find more and more things that we want to build software for and build more code for. I really think there's a lot more out there to do.

Lenny Rachitsky (00:29:23):
For people that don't know Jevons Paradox, can you briefly explain it?

Scott Wu (00:29:26):
Absolutely. Yeah. Jevons Paradox just says that as the price of something goes down, it can still be the case that the total spend on it actually goes up. You can think about this with money, you can think about this with time or resources, but the direct version here is, I think, as it becomes easier and easier to program and as programming becomes more and more effective, I think we're going to have a lot more programmers. I think in a kind of zero-sum view, you might say, "Well, we're going to be 10 times faster at software engineering and it means that we're going to need 10 times fewer software engineers." But I think in practice, what really is going to happen is actually we're going to build even more than 10 times as much code. And because all of the work that we do is so capped, obviously, on our ability to actually build and execute and iterate, we're going to have so many great ideas out there, we're going to have so many great products out there. People are going to build a lot more personalized experiences, for example, and there's going to be a lot to do.

Lenny Rachitsky (00:30:22):
Going back to the way you guys use Devin, you said that every engineer has this fleet of Devins. How many Devins per engineer do you find most people are working with these days at your company?

Scott Wu (00:30:33):
Yeah. It's very asynchronous. Obviously, you can kick them up and start them up and shut them down basically as you see fit, but most folks on the team are often working with up to five Devins at once, I would say. It's a nice flow where you think through, "All right, what are the five things that we want to get done today?" You have Devin one do number one, you have Devin two do number two, Devin three... For what it's worth, I think it's taken us some time to adjust to it and get to the point where it's really intuitive for us, but I think it's definitely a different experience where you're handing off most things asynchronously. 

(00:31:14):
The goal for each of your tasks is to be there for the parts that really need your expertise, either you really, really need to define exactly what it is that you're solving for and what you're building or maybe some of the more complex parts where you want to steer Devin towards, particularly what kinds of changes you want to make. "I want the class to be set up this way and we should go and change all the downstream references to this as well or whatever." But basically having Devin do the bulk of the work asynchronously with you.

Lenny Rachitsky (00:31:43):
And then how many engineers do you guys have roughly?

Scott Wu (00:31:46):
Yeah, our engineering team today is about 15 people.

Lenny Rachitsky (00:31:48):
15. 15.

Scott Wu (00:31:50):
15, yeah.

Lenny Rachitsky (00:31:50):
Holy moly. Okay. And then each one has five-ish Devins.

Scott Wu (00:31:54):
Yeah.

Lenny Rachitsky (00:31:54):
So there's five times the number of Devins as engineers. What I love about this is just a glimpse into where the future is going. You guys are so ahead of how companies work with AI engineers. Seeing how you operate is going to be, as a sense, essentially how most companies will end up operating.

Scott Wu (00:32:11):
Yeah. For what it's worth, we've already seen this shift, I would say, ourselves where... In terms of the team, obviously, folks don't spend that much of their time just writing out boilerplate or just doing pure implementation of features. People get to spend much more of their time focused on really just thinking about the core questions of, "How do we make Devin better? What is the right interface for Devin? What is the right flow or the right set of features that's really going to make this as great of an experience as possible?" That's how we like things.

Lenny Rachitsky (00:32:46):
When is the point you reach, where there's takeoff of this being the by... Your Devin starts moving so much further ahead of everyone else. Once you have enough Devins doing all these things, they're just like wherever and you're 10 years, 20 years, 30 years, 100 years ahead.

Scott Wu (00:33:00):
Honestly, as a community, I think all of us as engineers around the world, I think, are going to have to think about this and build for this and adapt to these new technologies. But what I would say is, I think more and more... Especially as capabilities get better, but certainly even in studies say today, I think more and more things are going to shift towards this asynchronous flow. And one of the reasons I would say for that is in the real world, you're just capped by real world constraints. I think that one way to put it is kind of like... Don't take these numbers exactly, but it's kind of like the first order math of it is, of course, being able to write files or to complete this function or complete this line or things like that.

(00:33:44):
It helps a ton. It's a really great experience. There's a lot of parts of building software that obviously are almost not that at all, right? If you have a bug that you're trying to fix and so you spin up the local server, you click around on your own product on the front end and try to reproduce the bug yourself. Once you have the error, you take a look at Datadog and you see what happened and you try to find other errors in the logs. You look at those files and you see what went wrong, you make some edits, maybe you go and rerun the whole process again now that you make sure your change looks right. That's a lot of what it means to be a software engineer. These are processes that take real time. I think we're going to shift more and more towards this agentic workflow, because that's in some ways the way to really get to that 200%, 500%, 1000% gains that we'll be getting to with software engineering over the next few years.

Lenny Rachitsky (00:34:39):
Enough talk. Let's show people what the heck this actually looks like. You've got a couple demos prepped that show a few use cases that you found helpful. You're going to pull up your screen and then we'll kick it off and then we'll talk as it's happening.

Scott Wu (00:34:52):
Yeah. The whole process obviously of working with Devin is working asynchronously. I thought it'd be cool for us to actually just watch Devin a little bit in action and then we can go through some other examples of work that Devin's done or things that Devin does for us, even on our team for example. But then we can check back in asynchronously with our Devin after. 

Lenny Rachitsky (00:35:12):
Let's do it. 

Scott Wu (00:35:13):
I'll share this real quick. The key thing that I would just emphasize here is a lot of it obviously is really just about thinking about as a software engineer or as engineers ourselves or engineering teams, PMs, and so on. What are the things that we would want to build that we would want to hand off? We have Devin set up with our own Devin code base, for example, and so I'll go ahead and kick off with Devin for that. I'll just say, "Devin, I'm on with my friend, Lenny."

Lenny Rachitsky (00:35:45):
Hi, Devin.

Scott Wu (00:35:48):
"Can you modify Devin web app two?" Let's feature your newsletter as part of the Devin website. 

Lenny Rachitsky (00:35:59):
Let's do it. On the real Devin website. 

Scott Wu (00:36:02):
"Feature Lenny's site." 

Lenny Rachitsky (00:36:04):
Yeah, lose all your features. 

Scott Wu (00:36:06):
We're going to kick this off. As you can see, Devin gets started instantly and goes ahead and responds. Again, you can work with this asynchronously, you can work with it synchronously as well. For this, we'll just kind of go in a little bit and see exactly what's going on. But as you can see here, Devin's going through files and taking a look through a lot of stuff. We can follow here basically as we need to and see what makes sense. You can see Devin's already called out a few particular pieces where there's the sidebar, which we have implemented on the front end, and there's pieces there. We're going to have a new component and that component's going to link to Lenny's website. That all sounds good. Devin's asking us any questions if there's anything that we have here. Same story here where you can let Devin make its own decisions and hand off, or you can go ahead and give some more thoughts. Should the button open in a new tab or within an application? I'll say let's open it in a new tab.

Lenny Rachitsky (00:37:03):
And you could answer these at any point. Is it waiting for the answer? 

Scott Wu (00:37:06):
You answer these at any point, you can hand off, hand back off. 

Lenny Rachitsky (00:37:07):
It's not going to be like, "Just god damn it. I just wrote it this way. Why didn't you tell me earlier?" 

Scott Wu (00:37:11):
That's right. One of the big pieces with Devin is Devin will always be enthusiastic, will always be ready to put in the hours. 

Lenny Rachitsky (00:37:21):
Thanks for changing scope. Thanks, Scott.

Scott Wu (00:37:24):
We'll give Devin a chance to work and it's going to go through these files and it'll make a pull request for us and we'll see and go from there. But I thought it'd be fun to show some other examples of Devin in action as well. One of the examples actually this morning, which I just used Devin for, is I asked Devin to help me brush my own facts up for this podcast. Obviously, a huge fan of the podcast and the newsletter. I asked Devin, "Hey, Devin. I'm to be on the podcast. Could you please research everything you can about him and make a nice website quiz for me so that I can make sure I know my facts?" This was just this morning, I asked Devin to do this and I'll just show what Devin did, it looks like. Went to Wikipedia first. Unfortunately, it's not a page in Wikipedia, which is... Lenny, we will work on that. 

Lenny Rachitsky (00:38:09):
I'm not a big enough deal yet. 

Scott Wu (00:38:12):
They did you dirty. I mean, we need a page list. And so then it went and found it on Spotify.

Lenny Rachitsky (00:38:19):
So you're watching what it's researching live?

Scott Wu (00:38:21):
Yeah, yeah, yeah. This was this morning, obviously. 

Lenny Rachitsky (00:38:24):
This is a playback of what Devin did. This is part of Devin you could just watch what it did.

Scott Wu (00:38:29):
Yeah, yeah. Especially when you're building engineering products or something like that, you can see each of the steps that Devin was doing, or if Devin tested the code locally, obviously you want to be able to go and look and see what Devin was cooking around with and testing or things like that. It found the newsletter. It's going and looking at this and it's going and reading all of this. And then it says, "Okay, let's get started with putting the code together." It says, "Hey, I've researched." It's going through and writing all of this, putting the app together. It plays its own quiz itself. Actually, we should just play this quiz actually. Let's see how much I know. 

Lenny Rachitsky (00:39:05):
[inaudible 00:39:05]

Scott Wu (00:39:06):
What is the name?

Lenny Rachitsky (00:39:08):
What is the name of the podcast? Lenny's Podcast. For people not watching, so to say, approximately how many subscribers? A million. Very good.

Scott Wu (00:39:17):
Yeah. Yeah. 

Lenny Rachitsky (00:39:18):
What are three main topics Lenny is focused on? Oh, product, growth, and career. Very good. It's a good quiz [inaudible 00:39:25] of people. 

Scott Wu (00:39:25):
What does [inaudible 00:39:26] besides podcasting?

Lenny Rachitsky (00:39:27):
What does Lenny do besides podcasting? 

Scott Wu (00:39:30):
I'd say writing, investing, and advising. How often does Lenny-

Lenny Rachitsky (00:39:35):
[inaudible 00:39:35]

Scott Wu (00:39:35):
Once a week, right?

Lenny Rachitsky (00:39:36):
Once a week.

Scott Wu (00:39:37):
Yeah. We can go through all these and do all these. I took this quiz, by the way, obviously, to make sure that I was well-prepped, but this is kind of one of the more fun examples, obviously, of [inaudible 00:39:46]

Lenny Rachitsky (00:39:46):
Scott, how many subscribers do I have at my newsletter?

Scott Wu (00:39:50):
Over a million, actually. 

Lenny Rachitsky (00:39:52):
[inaudible 00:39:52]

Scott Wu (00:39:53):
And then one last one I'll show and then maybe we can come back to our initial run after. Like I was saying, a lot of this is really built to work with all of the existing code workflows out there. For example, we were doing some exploration with the DeepSeek repository on GitHub and we imported it into Devin and we got our own fork of it set up in Devin. A couple of things I just wanted to show here. One is Devin sets up its whole wiki with all of its internal understanding. When Devin indexes the code base, obviously, building a representation of the code base and learning it and improving it over time is one of the big things that Devin does. Funnily enough, we found that naturally humans really are interested to understand this code base representation as well.

(00:40:38):
Devin Wiki is something that we built here and you can take a look at all these different pieces and see each of these different things. Here are the FP8 operations, here's an SG [inaudible 00:40:46] integration. There's diagrams of how the different layers are built and put together. There's deployment operations. There's a lot of details about the architecture as well. You can ask questions about it as well. For example, you can say, "How does DeepSeek handle multi-token prediction designed for spec deck?" It'll go through and it's able to search through the entire code base and give you an informed answer based off of that. 

(00:41:10):
We use this a lot. It helps when you're scoping out a task for Devin and doing an initial prompt. It also helps, obviously just in a vacuum, you often have questions about your code base that are really nice.

Lenny Rachitsky (00:41:20):
This episode is brought to you by Attio, the AI-native CRM. Attio is built to scale with your business from day one. Connect your email and calendar and Attio instantly builds a CRM that matches your business model, with all of your company's Contacts and interactions enriched with actionable insights. Sync in your product's usage, billing info, or any other data sources and Attio's flexible data model will handle it all without any rigid templates or workarounds. 

(00:41:49):
With Attio, AI isn't just a feature. It's the foundation. You can do things like instantly prospect and route leads with research agents, get real-time insights from AI using customer conversations, and build powerful AI automations for your most complex workflows. Industry leaders like Flatfile, Replicate, and Modal are already experiencing what's next for CRM. Go to A-T-T-I-O.com/lenny to get 15% off your first year. That's A-T-T-I-O.com/lenny. 

(00:42:21):
Something that I've learned as I've been talking to more and more AI building companies and apps is there's a big difference in how large of a code base they could integrate into. That's a big deal for companies that are existing versus startups, people that have large existing code base. How should people think about what kind of code base Devin can plug into?

Scott Wu (00:42:41):
Yeah. We go all the way to the biggest code base as possible. One way I'd kind of put it is how... The way that we as engineers would think about a large code base is certainly when you're making changes or when you're thinking about a particular task. You're not bringing in every single line of the code base at once. You have a high level of traction that you're able to think about and look into and then you're obviously able to zoom in and get to higher resolution on each of these different things. Devin works in much the same way, where the first thing it'll do is it's going to figure out the high level architecture of what's going on here and what this is built for and so on. But within each of the components, it's obviously also going to be able to zoom in and give some more detail about each of these. Here's FP8 to be float 16 and how exactly a lot of that is set up. Here's each of the different parts of the code base. Similarly, we built this to be scalable.

Lenny Rachitsky (00:43:38):
It's essentially coming back to the engineer as architect. Now, it's helping you understand the architecture, kind of circling back to that.

Scott Wu (00:43:46):
Yeah. Yeah, exactly. One of the fun use cases that we've seen actually with folks is they'll often actually get Devin's help to onboard new engineers on the team. When you're new and you're joining, there's obviously a lot of questions that you have about the code base or about how things are set up. It also sometimes can be a little bit awkward to ask your mentor or your manager the questions and if you're worried that they're going to be really dumb questions. It's nice to just be able to ask Devin and to go through Devin's wiki and to understand these internal representations.

Lenny Rachitsky (00:44:15):
I think that's really interesting, because it comes back to your point that Devin is not just a junior engineer. It's what you call a jagged engineer.

Scott Wu (00:44:21):
A jagged intelligence.

Lenny Rachitsky (00:44:22):
A jagged intelligence, where it's almost like a staff engineer at understanding the code base. Usually, you have to ask an engineer that's been there a long time, " What does this do? Where is this thing? How does this work?" It feels like Devin's very good at that.

Scott Wu (00:44:34):
Yeah. Yeah. Obviously, the retrieval and processing a lot of code and a lot of tokens at once is something that language models are really great at. Basically being able to get those gains in the places that you need them is really great. Yeah. Sweet, cool. 

Lenny Rachitsky (00:44:50):
All right. You got a couple more use?

Scott Wu (00:44:51):
Yeah. One last thought I'll show is just... We just rolled this out last week actually, but it's a full Devin automation setup with Linear. If you have tasks that you're doing on the DeepSeek repository, for example, and it's all set up, all you have to do is you just add the Devin label and Devin will come through and it'll give you this. It's going to give you its thoughts on what the tasks looks like and you can take a look at each of the particular files that you see, or it'll point out snippets that it thinks are important. From there, if you feel good about what was built or the conclusions that we came to, then you can just start off the Devin session that will go and actually do that work.

Lenny Rachitsky (00:45:30):
That is insane. That sounds like such a simple idea, but essentially what you're saying is there are tasks in Linear that are fixes and features and now Devin just goes off and can just do them for you.

Scott Wu (00:45:44):
Yeah. Definitely it's a hands-on process. You certainly want to be involved when Devin is scoping out the task or giving you its thoughts. The nice thing, too, by the way, is Devin will give you its confidence level. Here's how likely I am to really understand this piece or that piece or whatever, but it helps make things a lot faster. To your point, a lot of product managers, for example, obviously love to be able to use Devin in Linear to understand the code base better or things like that. Claire Vo, for example, from LaunchDarkly is a big Devin user and she loves basically going and scoping out tasks or asking data questions or asking, "Hey, what's going on? Or is this merged into production yet? Or is this a feature flag right now? Or what percent of people are getting this or that feature?" It's a clean way basically to make that intelligence much more accessible.

Lenny Rachitsky (00:46:40):
I love, just with the integration with Linear, that you can still keep it really simple. You add a little ticket like, "Hey, this link to this home page, do this," and Devin will be really good at understanding what you mean and then show you, "Here's what I'm thinking." Is this right?

Scott Wu (00:46:53):
Yeah. Yeah, cool. Okay. Yeah, Devin did finish working. It seems like there's something going on with the CI and it's debugging that right now, but it went ahead and put up the initial first pass pull request and we can take a look. 

Lenny Rachitsky (00:47:04):
Let's do it.

Scott Wu (00:47:06):
This is the Devin website, obviously, in this custom deploy and we have Lenny's newsletter right here.

Lenny Rachitsky (00:47:11):
Let's ship this to production. We won't be so confused.

Scott Wu (00:47:15):
Yeah.

Lenny Rachitsky (00:47:16):
That's amazing. Okay. Show it again real quick. Just added it to the home page of Devin.

Scott Wu (00:47:22):
Yeah. Devin, obviously, has access to our Devin code base. It does a lot here and so it's super familiar with all the pieces here.

Lenny Rachitsky (00:47:28):
Beautiful.

Scott Wu (00:47:29):
Yeah, I like how that looks. We've got Devin search, we got Devin [inaudible 00:47:33], and we've got Lenny's newsletter. 

Lenny Rachitsky (00:47:34):
[inaudible 00:47:34]. You link to my site. We'll get some PageRank going. 

Scott Wu (00:47:37):
Yeah, yeah, yeah. 

Lenny Rachitsky (00:47:39):
Okay. Is that a good example? Oh, there it is. What a beautiful website for my newsletter. Is that just a good example of the kind of thing Devin is very good at like, "Here's a very specific thing to change on the website"? How does your people think about what Devin is very good at and maybe where it starts to fall apart?

Scott Wu (00:47:55):
The way that we often describe it is, I think, Devin is best when it is working on tasks that are well-defined. One way to put it, you might...

Scott Wu (00:48:00):
On tasks that are well-defined. One way to put it is, you want to be giving Devin tasks, not problems. And a lot of these things like what you just saw, which was kind of like a quick front-end feature request or a bug fix or adding testing and documentation or things like that.

(00:48:16):
One of the things that makes a loop really nice obviously is a quick way to iterate and test. And so with something like this, obviously super easy for us, for example, to just go pull up the preview and see that the link worked. Obviously it would be easy for Devin to do as well. Devin will often go and log in to Devin and start a Devin session and make sure when it's working on our code base, which is kind of hilarious. But yeah, you generally want something that is kind of easy to verify and easy to test is the main thing. And you can work on bigger projects or bigger asks as well, obviously. But in that case you should certainly expect to need to steer Devin more to make sure it's going the right direction.

Lenny Rachitsky (00:48:55):
It's interesting because that's very similar to the way people talk about synthetic data and reinforcement learning, creating data that's very easy. There's a very definitive answer, yes and no.

Scott Wu (00:49:04):
Yeah.

Lenny Rachitsky (00:49:04):
It's very clear.

Scott Wu (00:49:06):
Yeah.

Lenny Rachitsky (00:49:07):
Okay. Let me ask you this question. What's something that you guys debated a lot as you were designing and building Devin?

Scott Wu (00:49:15):
I'll give a couple that comes to mind. One I would say is a question of, I'll call it how opinionated we should be. We had the workflows that we used to Devin for, which was very much as you can see for basically integrating to our Slack and GitHub making pull requests for us in our repos, responding to issue reports or things like that. And naturally we've had certainly a lot of other different things that have come up that folks have tried. I mean, we have folks who order their DoorDash with Devin, for example. Even we have folks, certainly a lot of people who are building cool websites from scratch or working on things like that.

(00:49:53):
Yeah, I mean it is been an interesting trade off for us where I think the way that I would describe it is in our product, certainly the large bulk of the features that we build are for this kind of making pull requests and engineering teams use case. But I think basically our kind of general stance with all the others is obviously if folks want to use Devin for that, that's great and we want to just make sure that they're fully aware about the limitations and about where things can get caught up.

(00:50:20):
It is funny with AI and especially because I would say one of, I would say the most common pieces of advice out there I would say is focus on a really niche cohort. Do things that don't scale, make one use case that's really great and then you grow from there. And I think that's great advice across the board. But yeah, it's kind of interesting because I think with generative AI, you naturally see this where a lot of product experiences can turn out to be more general. And so it's an interesting trade-off for us. This is something that we still always go back and forth on and how much do we want to do more to support all the other kind of use cases out there to handle other things that folks might want to do with Devin.

(00:51:03):
I think another one that comes to mind is how much Devin should be, let's say a single comprehensive project experience versus a suite of tools. And as you can see here, we have Devin search, we have Devin Wiki, we have the linear ticket scooping, and certainly these tools interact with each other, but I think as time has gone on, we've seen it more and more as really building this suite of tools. And I think the core agent experience and the core kind of agent that will go off and build each of these build things for you, for example, is always of course going to be that's Devin, and that is the core piece. I think that will always be what's really special about our work. But I think that all of the other features out there, there is a complex suite of work that's required for real-world software sharing and engineering is just messy at the end of the day.

(00:51:55):
And so I think there are a lot of different flows and a lot of different use cases that makes sense. And an obvious thing to point out is you could ask the same questions to Devin search as you could to Devin and Devin will go through and it'll do the same thing. It'll go through and look through the files and give you an answer and stuff.

(00:52:10):
But with that said, on the one hand, I think on the capability side, there's certainly a lot you can do to really optimize things for very specifically question answer about this repository and that made sense to really build into a specific kind feature.

(00:52:23):
And then on the other side, I would say we found that users actually really, really like having this access of control. Sometimes you have a task that you're thinking about, but you actually don't want Devin to get started on the task just yet. You want to ask Devin and understand what parts of the code base might be relevant. And so you want to be very direct about saying, "This is just an ask and I just want to see the snippets of the code base that relate," or, "I just want to look at the Wiki and understand the existing representation."

(00:52:50):
And so it's on both the capabilities and on the UX side, we've found that that's kind of what's naturally made sense over time.

Lenny Rachitsky (00:52:58):
Well, let's talk about the landscape then of just other companies in the space, which is something a lot of people are always thinking about. There's all these different approaches. You guys are going full on AI engineer, there's obviously ID companies. There's also just models being built that are really good at engineering. Everyone's kind of starting to build agents now. You guys are ahead on this in a lot of ways. OpenAI just recently said they're going to build a software engineering agent. Anthropics got something there. Cursor and Windsurf have their only agents and Replit. Thoughts on just where you guys fit in the landscape and then how do you think you win long term. How do you think about that?

Scott Wu (00:53:31):
Yeah, and for what it's worth, I think all of these are incredible teams. I think really smart and really forward-thinking folks who are building a lot of great products out there. And I think there's a lot to do honestly over the next few years with the advent of AGI or whatever you want to call it. I think one of the quotes that I love is in 2017, if you asked if we had AGI, the answer is no. And in 2025, if you ask if we have AGI, the answer is, "Well, you have to define AGI. And it depends on your subject." And I think it does get to the point of, I mean there is a lot of really amazing stuff happening. I think that it's easy to underrate, I would say just how big of a shift it is that we're seeing where I think there are a lot of great products out there, for example, over the last 10 years, 20 years, 30 years, that have made each of these different niches of the life cycle of building a product a little bit easier, for example, right?

(00:54:28):
There's great products out there for instant response, there's great products out there for logging, there's great products out there for billing, there's all of these different tools. And the obvious thing is what we're seeing with AI is all of these spaces are going to be moving multiple times faster and it's going to be like an order of magnitude shift, if anything.

(00:54:47):
And so I think from our perspective, we've obviously had a very specific lens that we've bet on this whole time, and that is autonomous coding agents. And there's a lot of problems to solve there, to be honest, right? There's still a ton to do on the core capabilities, certainly, and we see cases all the time where it's like, wow, why did Devin make that decision? That seems, no human engineer would've ever done that. There's all sorts of spots where, with the product interface, there's obviously a lot to think about.

(00:55:16):
And I think it's by the way, not just a single thing that we're working towards, but something that will change with every edition of capabilities. I kind of think of it as there's 20 generations of agent product, agent coding experiences to come. I think the one that we'll get to over the course of several years is probably something where you don't even look at the code at all, right? And you're actually just looking at your own product and you're just able to look and specify and say, "Hey, this button should be a little bit rounder. Let's do that. And by the way, let's add a new tab here and maybe we should save this information. Let's start up a database table and let's index it on X, Y, and Z columns." And you're just basically working with your products in real time and having your agent build out those things for you. Obviously there's going to be a lot of generations in between here and there, but I think the product experience itself is going to change every single time.

(00:56:04):
And then obviously there, there's all of the practicality of just getting it out there in the world. And so folks obviously need to learn how to use the new technology. There's a lot to do to deploy into all of the messiness of real world software. There's a lot of COBOL out there still. There's a lot of FORTRAN out there still. There's lots of kind of abstractions and details that folks have done.

(00:56:27):
And so I think from our perspective, we have since the beginning have been laser-focused on agentic coding, and that is the one thing that we've really believed in. It's the one thing that we've designed for and that goes all the way to even the revenue model with ACUs and having the usage-based setup. It does into obviously all the product experiences of thinking how, okay, where do you want to talk to Devin? You want to be able to talk to Devin in Slack, you want to be able to spin this up from your issue. You want to be able to all of these things and then of course the capabilities.

(00:56:58):
And so I don't think there's any one easy answer. I think it's obviously a combination of things, but this has been the space that we've lived in and spent all of our time in for the last year and a half, and it's going to be that way for the next five or 10 years too.

Lenny Rachitsky (00:57:14):
Along these lines, a big question everyone always has in AI's moats and defensibility, it's a question I've been asking every founder that comes on. How do you just think about how to build a moat in this space when it's so much easier to build and so much is built on these models that are themselves advancing so quickly?

Scott Wu (00:57:30):
I'd give one slight tweak on that, which is I think it's often less about moats and more about stickiness. And what I mean by that is moats are in some sense, typically what folks mean by moats is something that means that a competitor couldn't even enter the market. And I agree that at a high level, a lot of different folks at different layers of the AI spectrum, the foundation labs or the application layer or so on, I don't think there's any kind of hard barrier that would prevent others from entering. I think what does exist is stickiness, which I would kind of define as once you have a product experience that you really like, are you excited to keep using that experience or is there an effect where it is just as easy from now on to just switch on to a new one and learn a new one and so on.

(00:58:15):
And I think from that perspective, I think there's a few things that are really great about coding agents in particular. One I would say is there is a lot of just inherent stickiness and learning and buildup over time, which is that as you use Devin and as your whole team uses Devin, it's the same thing with an engineer. If you're joining on day one versus you've been at the company for five years, you wrote half the code yourself, you've touched every file you've built every single piece, you know all the engineers. And so similarly, it's like Devin will really learn and build its representation of your code base and of your stack and of your process over time and will be able to do a lot more with that.

(00:58:51):
And then the other piece of it, which I think is really exciting I'd say is there really is a lot to do of what I would call a multiplayer aspect of code, which if you think about it, is how a lot of things get done in the real world, certainly. And so it's one thing to have your own experience, which you use yourself as just an engineer, but for example, ourselves, we see this all the time where some engineers are working with Devin and teaching Devin things and as I mentioned, folks will have Devin on board their new engineers and kind of convey that knowledge to them.

(00:59:24):
Or similarly, it's like I'll start a session with Devin in Slack and I'll say, "Hey, it'd be cool if we could do this thing." And some other engineer will chime in and say, "Oh, by the way, the reason we did it initially was X and Y." And so Devin, just make sure when you do this change that you still support that workflow. And Devin will say, "Okay, sounds great." Or Devin will make a PR, I'll be working with Devin, we'll make pull requests and GitHub and somebody else will be reviewing that PR or give some comments and Devin will work on that too. You'll be in linear.

(00:59:52):
So all these kind of spaces, it really does just kind of set up for an experience basically where Devin can just grow in the value that it can provide for your whole work over time. And so I think from that perspective, if anything, we want there to be a lot of innovation and a lot of new products and so on. I don't think that the goal is to try to lock other people out of building. There's a lot of stuff to build, and I think there's going to be a lot of different experiences. I think from our perspective, what we think about is more like how can we make Devin more and more and more useful as you're using it more?

Lenny Rachitsky (01:00:27):
It's very similar. We had Michael from Cursor, the CF Cursor on the podcast, and he had a similar point of just he thinks moats are just kind of like consumer, like Google is the way, he thinks it's like Google where people can easily switch. You just have to stay the best, and that's the answer. And it feels like you're adding to that of just like, but also if you can create some stickiness where it is very hard to leave because it's so good at what it's doing and it's built knowledge and integrated to your workflows and builds on that on that stickiness.

Scott Wu (01:00:58):
Yeah, and I think one of the things that's nice about our space too is, software engineering for better for worse has a very clear tie to value. And what it means is, I guess one way to put it is there is always kind of a clear next level, at least for the next while. I think there could be some point where you're just like, "All right, just build the entirety of YouTube for me." And Devin just does the whole, it's like there's probably been a hundred million hours of human engineering time building YouTube, building the algorithm, building all the infrastructure, all of the, everything, every little detail. And maybe there's some time where Devin just does that out of the box. That's obviously going to be a long time from now.

(01:01:36):
I think on the interim, on every level in between, obviously it makes a difference the quality of software engineering. And I think one of the cool things with developers obviously is developers are really willing to learn new experiences and to put in effort if it means that they're able to have a higher and higher quality experience.

Lenny Rachitsky (01:01:57):
Awesome. I'm going to spend a little time on the tech that enables Devin. Without divulging trade secrets, just what allowed you to make Devin so good? Was there an unlock with a certain model? Some folks have shared three points on a 3.5 was a huge unlock for a lot of their products. Just what's kind of the key to the way you've architected or built Devin that makes it work so well?

Scott Wu (01:02:20):
We obviously, we've been betting on agents for a long time. I think that agents were doable and workable a lot earlier than most folks might've thought. But certainly I think as the community has really rallied around it, I mean you see the impacts of that in the pre-training, you see the impacts of that in a lot of the work that's done with these models. I actually don't think there's been any, from our perspective, I don't think there's been any single step function based model shift or anything that has been kind of like a night and day difference in Devin, but I certainly think that the curve of every point on the chart, I mean there's a new model that comes out every week now has obviously made a big difference in terms of what we've been able to do. And then obviously on top of that, we work with the research teams at all these foundation labs to do a lot of our work on top.

(01:03:11):
And so I think that my hot take here at which I would give is, I think in terms of base intelligence, we're honestly basically already there. And I think a lot of what we see actually and what we spend our time on is less so, obviously, we don't our own models or things like that. It's less so increasing the base IQ of a model, for example, and more about teaching it all of the idiosyncrasies of real-world engineering and thinking about here's how you use Datadog and do this, and here's how you might diagnose this error and here are the different things that you could run into and here's how you handle each of those. And when you're ready, here's how you make GitHub PR.

(01:03:50):
And this is true in engineering. It's true in every other space as well. I mean, there's so much detail and idiosyncrasy to the work that we all do obviously day to day. And a lot of it is kind of like teaching the model to mirror the complexity of the real world, I would say, rather than getting it to some higher fundamental level of problem solving, which I think the foundation labs are doing a really great job.

Lenny Rachitsky (01:04:15):
There's something you shared when we were chatting before we started recording around the growth of previous transformative technologies were very hardware oriented and there was a limiting factor to their growth and AI is not that. Can you just share that insight?

Scott Wu (01:04:30):
For a number of reasons? I think AI is going to be the biggest technology shift of our lives, but I think one thing, which is what we were just talking about before this, which is most of the big tech revolutions that we've had over the last 50 years, I mean, I'm thinking about personal computer and the internet and the mobile phone and stuff, they all had this big hardware component that was a big part of the distribution. And so you had the internet, and initially it was just these universities that were talking with one another, but obviously over time we got the whole world plugged into the internet and it took years and years and years. Same thing was true with mobile phones. Same thing was true with PC.

(01:05:06):
And the thing that's interesting about that in particular, which is I would say we're already seeing the effects of that, is in these hardware distribution machines, obviously there's a lot that depends on real time. And so folks who were building for those industries saw their market grow and grow and grow basically steadily year over year as the number of people with mobile phones increased, as the number of people connected to the internet increased. And many of those businesses, it's still crazy to think, but many of those businesses got started right in the beginning. I mean, Apple and Microsoft were started right around the same time. And same is true for a lot of the great internet businesses or wherever, but certainly it was something that touched whole world with time or a large fraction of the whole world. And it had a really massive impact, but it took place over several years because of the time that it took. And I think one of the things which is already I'd say different in AI, is just how explosive the technology can be. Once AI could, and I think we're firmly past the inflection point in AI code where it's, as an engineer, if you're not using AI at all to write code, I mean you're falling behind honestly. And it is a technology that everyone should have and should be using, and there's no kind of weight on hardware distribution that is causing that. It means that the space is just growing so exponentially, basically.

Lenny Rachitsky (01:06:36):
Michael Ballin has this interesting point that cliches are cliches because they're so true and that's why they're cliches. I heard that a million times and I think it's like people hear this like, "Yeah, yeah, I know," but it's actually insane what is happening. That's why you're here to help us through this transition.

Scott Wu (01:06:52):
Yeah, no, I mean, it is a fun time and I think there will be real investment and real work that it takes. But I think from the perspective of us as engineers, for example, I think it just means it's so important to stay in the loop with everything that's happening. And as we're seeing it's not only because of your learning and your ability to work these technologies, but it's also about basically teaching the AI what there is to know about your code base in order to make it really effective at building with you and doing more of the things that you would want it to do.

Lenny Rachitsky (01:07:27):
So along those lines, for people listening that they're like, "Hey, we should be using Devin at our company," what are things you've found to be helpful in helping an engineer at a company get adoption and be able to use Devin either culturally or logistically?

Scott Wu (01:07:42):
So a pattern which we often see with folks is there will be a few folks at the team who are really excited and want to try out the new thing, and they want to put in the investment and are really excited to get it going. And they'll go through all the setup. They'll give Devin the repos, they'll teach Devin how to run the lint and the CI and all of those details. And they'll start off by giving it those initial tasks and help Devin build a foothold basically. And as time goes on, eventually folks will see, "Wow, Devin's writing all these PRs, Devin's doing this [inaudible 01:08:14].

Lenny Rachitsky (01:08:13):
Who's this Devin person that just joined the company's just knocking out PRs?

Scott Wu (01:08:17):
Yeah. And they'll see that, and then naturally they'll get on and they'll get an account. And one of the cool things of course is by the time they join, Devin already knows a good amount of detail about the repositories that they're already working in and they're working with that. And so one of the really cool things which we often see is that the early adopters themselves can really pave the way I think, for everyone else on the team.

(01:08:37):
But yeah, I think the main thing I would just kind of call out is it really does take, it's a very different product experience, and I think for what it's worth, I think there's still a lot more that we can do to make it as intuitive and as clear as possible to folks like how to use Devin and what the right steps are and how to really maximize value out of Devin. But I think that, yeah, it's the kind of thing where if you put in the investment and understand exactly what it takes to get Devin to be successful, we've found ourselves that as time has gone on, we just use Devin more and more and more with every next update.

Lenny Rachitsky (01:09:15):
So let me follow that thread. There is a question I ask every AI app building founder, which is, if you could sit next to every new user of Devin and whisper something in their ear to help them be successful with Devin, one or two tips, what would those tips be?

Scott Wu (01:09:31):
I think the biggest thing I would say is it really is just treat Devin like your new junior engineer. And I think that's the biggest thing. I think folks come in and they see the blank page and they think of all sorts of various things that they want to try out. They think of lots, where I think typically the flow that we see that works best is obviously you can try demos and you can do things, but a lot of it is just like, "Yeah, let's figure out what tickets we want to get done today or this week and let's have Devin get started on those and let's start with the easier ones and then work with Devin and understand what things Devin needs to get set up to be able to test its own code and do this well. And then let's scale up over time." And then obviously as you work with your engineer, you understand better how to communicate with them or what are the right tasks or projects to bring them in on. But I think that really is the one-liner for us.

Lenny Rachitsky (01:10:31):
Okay. There's a question I'd be meeting task. I just want to get back to this because it's something I think a lot about with Devins. Everyone's going to have five Devins, let's say 10 Devins. Everyone's kind of turning into basically an engine manager with a bunch of junior engineers, which isn't necessarily the best job in the world because it's just a bunch of, at least you don't have to do performance reviews and one-on-ones, but it's sitting around, checking a lot of PRs all day. There's a sense of you become an architect, which is kind of what every engineer wants to become eventually, right? They're all, "I just want to think about the architecture. I don't want to code all these stupid, fix bugs."

(01:11:06):
So I get that there's a good side to that, but just I imagine you're thinking a lot about this, just like how do you make life pleasant and fun and enjoyable as basically an engine manager of say, 500 Devins in the future?

Scott Wu (01:11:19):
Yeah, I can just imagine the performance, "Devin, you've done a really great job on your task, but I really would like you to be more proactive in the team meetings." So what I'd say-

Lenny Rachitsky (01:11:29):
[inaudible 01:11:29].

Scott Wu (01:11:29):
It's funny actually because something that in terms of the wording that we thought a lot about as well is just, we've used the term manager of Devins in the past, which of course I think is a big part of it. But I think that the only thing I would point out here is I think that the bricklayer versus architect is closer to the experience than being a manager. Because I think a lot of the difficulty of management or the reason that people shy away from it is more because of a lot of the various.

Scott Wu (01:12:00):
... [inaudible 01:12:00] because of a lot of the various, let's say... There's all of the context, and the ownership, and the responsibility and stuff, and then there's also all of the emotional aspects of it. Where, I think working with Devin is a little more like just being, more as having an interface to hand off tasks and build tasks. And so, the parallel that I would draw is when we invented Python, obviously... It's like, in many ways the description and the outlining of tasks, obviously it was a different paradigm, but I think certainly it was nowhere near what folks typically think of as management bureaucracy today.

(01:12:50):
And I think that with Devin, a lot of it is just like, it's more like finding the right levels of abstraction that you could work with Devin on, and just finding the workflows that work really well, and the obvious thing to say here is, it's like you can always have Devin take a first pass at things. And so you have Devin take the first pass, if it's great, you merge it right away, if it needs some touch up, you can obviously give that feedback, for example, but a lot of it is like, it's more about, basically making Devin part of your flow than it losing control, which I think is the main thing that folks are scared of with management.

Lenny Rachitsky (01:13:34):
Are you thinking about a manager Devin? Like a Devin that manages other Devins?

Scott Wu (01:13:37):
Yeah, yeah. So, for what it's worth, Devin can start other Devins through the API, right? And so, we've seen this happen quite a bit of times, where naturally if you have some big tasks that you want to do, Devin will do this all the time, it'll chunk up and then [inaudible 01:13:53] into smaller Devins. And so, it's the kind of thing that you need to give Devin the credentials to be able to do that, it's not currently something that is default enabled, but I can certainly imagine as time goes on that there's more and more of that

Lenny Rachitsky (01:14:03):
Devins all the way down.

Scott Wu (01:14:05):
Yeah, yeah. I think the thing that's kind interesting too is, with humans, the way I almost say it, in technical terms, it's like there's this coupling of a context and a thread, and what I mean by that is basically, each human can only operate a single threaded on the work that they do, and they have their set of context, and then there's other humans obviously who can do other stuff at the same time, but they have their own context. With agents, one of the cool things is you can have an agent that's doing multiple lines of exploration at once, but is sharing all of the context of everything that they find, and so I think that this is very early, and I think we'll see this, but folks obviously love to talk about basically systems of agents communicating with one another, and I think that there will be a lot of new paradigms to build for, once we get there.

Lenny Rachitsky (01:14:55):
And it's so interesting what you said about the decision between having one Devin and only one Devin do all the things, and you just tell them things and they fire off jobs versus you have five Devins, and they're each doing individual things, it's such an interesting decision to make.

Scott Wu (01:15:10):
Yeah, yeah, yeah, for sure.

Lenny Rachitsky (01:15:12):
Okay, two more questions. Maybe the most counterintuitive thing you've learned so far building Devin, that maybe goes against startup wisdom, common startup wisdom?

Scott Wu (01:15:21):
Something I've thought about a lot lately as we've built this is, this is not my first company, actually for a lot of us, it's not our first company, I think of our 26 or 27 people total on the team, I think 18 of us have started our own company before this. And yeah, one of the things I think about is, there's actually your point about cliches I think really spoke to me as well, which is, there's the really common things which you hear all the time in startups, where you're like, you got to move fast, or you got to hire great people, it's like, okay, well, obviously you do, I wasn't planning on not hiring great people, I wasn't planning on going slow. And similarly it's like, yeah, you really got to build something that people want. And there's these three to five things which are always repeated, and they're always the common wisdom in startups.

(01:16:11):
And I definitely had this idea as a founder, when I was starting initially, that, all right, so those are the three to five basic things, but as you get really deep into it, you spend a lot of years into it, you learn all of the thousands of other things that you have to learn to build a company. And I think to some extent that's, of course, true, and there's lots of little details that you'll get into with all these different things, including team building, and product, and strategy, and engineering decision-making, and fundraising, and sales, and every other component. But I also realized that as time has gone on, more and more, I felt like building companies well sometimes just comes down to doing those three to five things just even more than you could possibly expect.

(01:16:58):
And so, with us, it's like... And everyone says we go fast, but it's like, yeah, we had a hackathon in November, we had another hackathon in December, we started the company officially in January, we got the prototypes out to initial users in February, we did a launch in March, we got our first customers in April... It's just like, basically truly pushing the pace in every spot where we possibly could has really made a difference for us. And similarly, it's like, yeah, everyone always says you should hire great people, but I think that the truth within that truth is basically you should fight to all ends basically, to get the folks that you really want to bring in. And one of my favorite stories to share is we had a candidate who came and interviewed, he was a junior at MIT, so he was very, very young, and we gave him an interview, and he did way better than almost any of the full-time candidates that we had ever talked to. And so, we said, hey, what do you think about taking some time off of school and working with us and building out Devin?

(01:17:57):
We really think you're just going to be able to come in and just have a ton of impact already from day one. And he thought about it for a while, and he came back and he said, you know what? I'm down, I want to do it, but my parents really want me to graduate from school, and I'm just not sure there's a way to make it work. And so, we talked him more and just understood the situation, and then we flew to North Carolina, went straight from the airport to his parents' house, had dinner with him and his parents, we talked a lot, a really nice Gujarati family, we gave them some gifts and just talked to them about it, and try to understand what would it take, and what would we need to make work. And they just said, it sounds like a great opportunity, but we really want our son to be able to graduate.

(01:18:45):
And we talked that through and we figured out a setup basically, where he could work for us essentially full time, but then come in for his required classes, and do what he needed to do to get the diploma basically, but no more than that. And we talked that through, and then we got to a point where everyone was happy with that, and then went straight back to the airport and flew right back, basically. And that was the first and only time that I've ever been in North Carolina, and it was just a great trip. And it is the kind of thing where it's like, hiring great people is one thing, but truly just never giving up, and really giving it everything that you can to make it work for people who really makes sense to be on the team. And he's been with us on the team for over a year now, and he's been an incredible, incredible engineer, and we wouldn't be here without him.

(01:19:31):
And similarly, we had someone else who was again, really, really talented candidate, did amazingly well, very young, and had a lot of great offers at a lot of other companies, and we were talking to them about, he wanted to start his own company someday as well, and we were talking to him about certainly a lot of the obvious things, which are having him meet our investors, or get to do work with customers, or see a lot of these other components so that when the time came that he would have all the experience he needed to start his own company. But one of the other things that was big is he was talking with a lot of great companies already, he didn't want to burn any bridges, and so we actually worked with him and basically hand wrote all of his rejection responses to each of the other companies, and worked with him on it to say, here's how you should say it in a way that's going to come off as that you really did appreciate the time with them, and that obviously you want to remain close with them and stay in touch. And it was the kind of thing obviously where it's like, look, obviously our job is to make sure that he's happy enough that he doesn't want to leave at any time in the near future, but I think it's the kind of thing where the way that you put together a really, really great team is by fighting for what's right for them too.

Lenny Rachitsky (01:20:45):
Wow, those are incredible stories. And it makes so real these, as you say, cliches, hire the best people, this is what it sounds like to hire the best people. This is what it takes.

Scott Wu (01:20:56):
Yeah, no, and I was just saying, a lot of things we've fought very hard to just reimagine things from the ground up because a lot of it really is just thinking about where do we think the technology is going over the next five, 10 years, and what is the place that we want to have in that future?

Lenny Rachitsky (01:21:16):
I wonder if people are going to be fighting for the best Devin someday. They're just going to [inaudible 01:21:19] Devins.

Scott Wu (01:21:18):
Yeah.

Lenny Rachitsky (01:21:19):
They're [inaudible 01:21:22] so smart.

Scott Wu (01:21:22):
I'll give you overtime pay, benefits, free healthcare, and everything, and then the Devin's like...

Lenny Rachitsky (01:21:29):
Three Devins like Magic: The Gathering cards.

Scott Wu (01:21:31):
Yeah.

Lenny Rachitsky (01:21:32):
And then just going back to your three to five things. So, essentially this is incredible advice, essentially, it's like you always hear hire the best people, move fast, build things people want.

Scott Wu (01:21:41):
Yeah, build something people want, stay as close as possible to your customers, and then I think the other thing is just always think about where things are going, not where they are today. I feel like those are the five things, which is... Especially in AI, with things moving so fast, and there's so much great talent, I feel like a lot of these are even more true, where it's like it's not just thinking about where things are going to be in 10 years, it's like thinking about what's going to happen next week. And obviously, things are moving very quickly, and it is very hard to predict, but you really have to be very rigorous with yourself, I'd say, about thinking through those things and evaluating all of the decisions that you make in that lens.

Lenny Rachitsky (01:22:25):
And staying focused is the big takeaway to me here, is it ends up feeling like there's 1000 things you should do, but it's always these five things.

Scott Wu (01:22:31):
Yeah.

Lenny Rachitsky (01:22:33):
Scott, we covered a lot of ground. We went through every question I had, which is great, is there anything else that you want to share? Anything else you want to leave your listeners with, maybe a final nugget or something really you want to double down on that we said before we let you go?

Scott Wu (01:22:49):
The biggest thing that comes to mind for me is there's a lot of different perceptions about AI, right? I think basically every emotion under the sun right now. There's a lot of fear, for example, there's also a lot of skepticism, and we're very skeptical types as well, and we always wanted to try it ourselves to really see it and believe it. And I think the main thing that comes to mind for me, is I'm honestly really optimistic about what we're building here with AI, not just with code and with Devin, but the whole space, and everything that's getting done. And I think one of the cool things that is really actively happening is just the ability for everyone to multiply themselves, and that's how we've always thought about it, it's how we've thought about what we're building. And I think there is a lot more to do out there in the world, I'm not too worried about us running out of things to do, and from that lens, I think that the thing that we've always been most excited about is, how can we all do more?

Lenny Rachitsky (01:23:52):
I hear you Scott. Well, with that optimism, we've reached our very exciting lightning round. Are you ready?

Scott Wu (01:23:59):
Yeah, let's do it.

Lenny Rachitsky (01:24:00):
Okay, here we go. First question, what are two or three books that you find yourself recommending most to other people?

Scott Wu (01:24:07):
In terms of nonfiction, I think for folks in startups, I think one of the things that I've really enjoyed is just learning and understanding the history of Silicon Valley. And it's all of these things that we think about, somebody invented them. It's one of the great realizations I feel like, is somebody invented the idea of a seed route, somebody invented the idea of venture capital, somebody invented the idea of product-market fit, and all of these different principles that we talk about. And so, for that, there's a book called The Power Law by Sebastian Mallaby, which I really like. And basically, it's just a tour of many of the great businesses and the great products that have been built over the last 60, 70 years in Silicon Valley, which I really love. I think in terms of fiction, I actually have always really liked The Great Gatsby by F. Scott Fitzgerald, it's one of my personal favorites as a fiction book.

Lenny Rachitsky (01:24:57):
Do you have a favorite recent movie or TV show that you've really enjoyed?

Scott Wu (01:25:01):
I have to admit, I have not watched... I can't think of a single movie or TV show that I have watched in the last while, so I'm sure, I'm looking forward to watching a lot of great ones post-AGI.

Lenny Rachitsky (01:25:17):
That's got to be in the trailer, that's great, I like that. And that just shows how hard you're working, just how much shit is going on, and how fast everything's moving. Do you have a favorite product you've recently discovered that you really love? Could be an app, could be something physical, could be a toothbrush.

Scott Wu (01:25:32):
One I would say is I got an Aura frame recently, it's just like a frame that shows photos, and you can show a new photo every day, or every hour, or every 15 minutes, or whatever you like. I've actually, I've really enjoyed it a lot, I think it's a nice way to basically just have a picture frame memories that come up. And then, the other thing I would say as a general purpose thing, it's not particularly new, but I would say, I think AirPods are extremely well-built and well-designed. And I realize now that it's like, I basically use them for all... I'm taking calls on a walk and I'm using AirPods, obviously I'm doing work at my computer, at my desk, I'm plugged into AirPods, and it works quite well, honestly, for a lot of different situations, and they're very comfortable, they're very consistent.

Lenny Rachitsky (01:26:21):
I'm going to double down on the Aura frame, I also, I got one of these for my mom and my mother-in-law, and they're so great for just sharing photos of your kids with your family. And people have, they've heard of digital picture frames, but the Aura just does it really well, and it's really easy to add photos, and they're just really nice looking.

Scott Wu (01:26:39):
You can imagine not that long from now, we'll have the Aura Frame except Studio Ghiblifies every photo that you have in it, and then it's... Yeah.

Lenny Rachitsky (01:26:47):
Or just imagines things you've done that are really cool. Look at my sweet life. Yeah. Cool. And it's Aura, it's A-U-R-A, I believe is how you spell it. Folks who want to check it out, we'll link to it. Not affiliated. Okay, two more questions. Do you have a favorite life motto that you often come back to and find useful in work or in life?

Scott Wu (01:27:06):
Yeah, something I've thought about a lot is a lot of the proverbs out there are actually contradictions, right? It's like birds of a feather, and then you also have opposites attract, and you have all... And it's kind of funny, because you feel that both of them are true, and often they both are true, and a lot of it is about understanding why. And one of those that I feel like, especially in the world of startups that I think about all the time is, I think it is very important to be focused and driven, and to really maximize your potential, and then at the same time, it's also very important to not let your own personal emotion get tied up in your success or failure, and I think especially with startups, because there's always ups and downs, honestly, even in the most successful companies ever, it's just like, it's a rocky road, there's a lot that happens, and a lot that goes down.

(01:28:03):
And I think one of the things which I've thought a lot about is that somehow you really want to do your best, and put everything you can into it, and do everything you can to... Basically, you want to put it all out on the field. But at the same time, you want to be okay with both wins and losses, and you want to be able to move on, and go into the next one each time. And something, yeah, it's funny, but what I've found personally is that obviously it's really important for your own emotional state and mental state to be able to do that, and we've had lots of mistakes, and I've had a lot.

(01:28:49):
I had my first company, which obviously, which was cool, but there are a lot of tricky spots there, and then over the course of Cognition, it feels like it's been already eight years compressed into one year, and it's still going at that pace. But somehow it also actually makes you more successful, I think, too. It's like, you are just more able to give it your best, and to do the things that will lead to success if you're not tying it up in your own personal worth.

Lenny Rachitsky (01:29:19):
That is so interesting, I just had a podcast recording recently where with an executive coach, Jerry Kelowna, that I think will come out before this, might be after this, that's one of his big pieces of advice, and it's a very Buddhist approach of just [inaudible 01:29:33] and attaching to a certain outcome.

Scott Wu (01:29:35):
Yeah.

Lenny Rachitsky (01:29:36):
Okay. Final question, I'm curious if there's a story here, but we could keep it short, is there a story behind Devin as the name, or is there another contender for Devin being the [inaudible 01:29:48]?

Scott Wu (01:29:47):
Devin was the name from pretty early on, we were interested, we were working on coding agents from the beginning, and my co-founders are Steven and Walden, for example, and we had this idea, all right, let's get started, and let's try to expand the box as much as we can. So, have everyone think out of the box and do their own thing, and let's have everyone do their own thing first for a bit, and then we'll consolidate and take everything that we've learned. And so, Walden made a virtual developer version of him, which was called DevWalden, and then Steven made one of him, which is called DevSteven, and we had all these... And then we were kind of combining it all into one thing, and we're like, okay, you know? It's Devin. And that was the thing. And so Devin was, yeah, Devin stuck for us quite early on, I would say.

(01:30:31):
One thing which we did have a big decision on though actually is what the image of Devin would be. And so, as folks know, there's the hexagons and then people have seen this more recently, but there's actually also an otter, a little otter with a laptop in its lap, and that is Devin as well. And we had this debate over what to go with, and what not to go with and stuff, and it's been a while now, but somehow we still have both the hexagons and the otter.

Lenny Rachitsky (01:31:01):
You skipped over where the Devin, did you have just have, it just came to you?

Scott Wu (01:31:06):
Oh, so Devin is, it's a dev. Yeah.

Lenny Rachitsky (01:31:10):
[inaudible 01:31:10].

Scott Wu (01:31:09):
And so, it was kind of like, when we were consolidating all the names, it just seemed clear then that this would be the universal dev that we all liked to work with.

Lenny Rachitsky (01:31:17):
Wow.

Scott Wu (01:31:18):
Yeah.

Lenny Rachitsky (01:31:18):
Incredible. Scott, this was so much fun. Oh my God, I learned a ton, which is always a really good sign. Two final questions, where can folks find you/Devin/anything else you want to point them to, and how can listeners be useful to you?

Scott Wu (01:31:29):
Awesome. Yeah, no, we're at App.devin.ai, and you can find us as well on Twitter or a lot of other social media. We'd obviously love to hear any feedback you have about the Devin product, there's so much to figure out, and I think the, like I said, I think we're all still 20 steps away from really the future of software engineering, and so it really means a lot to hear what folks think about the product as they're trying it out. And so, please let us know anytime if there's things that we can do to make it better.

Lenny Rachitsky (01:32:00):
Scott, thank you so much for being here.

Scott Wu (01:32:02):
Thank you so much for having me. I had a great time.

Lenny Rachitsky (01:32:04):
Me too. Bye everyone.

(01:32:07):
Thank you so much for listening, if you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at LennysPodcast.com. See you in the next episode.

