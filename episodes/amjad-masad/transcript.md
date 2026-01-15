---
guest: Amjad Masad
title: 'Behind the product: Replit | Amjad Masad (co-founder and CEO)'
youtube_url: https://www.youtube.com/watch?v=Bp_h674oIhw
video_id: Bp_h674oIhw
description: Amjad Masad is the co-founder and CEO of Replit, a browser-based coding
  environment that allows anyone to write and deploy code. Replit has 34 million users
  globally and is one of the fastest-growi...
duration_seconds: 3849.0
duration: '1:04:09'
view_count: 33941
channel: Lenny's Podcast
keywords:
- activation
- roadmap
- mvp
- iteration
- experimentation
- conversion
- pricing
- revenue
- hiring
- culture
- management
- vision
- mission
- market
- persona
---

# Behind the product: Replit | Amjad Masad (co-founder and CEO)

## Transcript

Amjad Masad (00:00:00):
The idea behind Replit is that making software today is very difficult. We want to make it easier. People view this as a developer in their pocket essentially. We have 34 million users globally. There's people everywhere learning to code on Replit, building startups, building personal software, personal tools.

Lenny Rachitsky (00:00:20):
For people building products, say, product managers, founders, what skills do you see will matter more, matter less?

Amjad Masad (00:00:27):
Typically, you're bottlenecked where your ideas are not fitting in because they need to be made and they need to be made quickly. Now, you open up that bottleneck. So now actually making things is a lot easier. Actually, you become limited by how fast you can generate ideas.

Lenny Rachitsky (00:00:44):
I think people are unaware of just how far things have gone.

Amjad Masad (00:00:47):
I could imagine whatever five years from now, someone running a billion-dollar company with zero employees where it's like the support is handled by AI, the development is handled by AI, and you're just building and creating this thing.

Lenny Rachitsky (00:01:01):
Man, the future is wild. Today, my guest is Amjad Masad. Amjad is the co-founder of Replit, an AI-powered software development and deployment platform for building and shipping software. It's one of the fastest-growing developer communities and AI products in the world. There's a lot of talk these days about how AI is changing, how products will be built, how product teams are going to operate, which functions will be more and less valuable over time. But I feel like very few people have actually seen what modern AI tools can do and have fully grasped how much you can get done with very little technical skill now and in the future. And so I'm going to do an experiment with this podcast where I'm going to do a series of behind the product episodes where we go deep on important products that product builders should be aware of and should probably start playing with.

(00:01:54):
In our conversation, Amjad does a demo of what you can do with Replit today, which is going to blow your mind. And then we spend most of the conversation talking about the implications of this on the future of product development, on the future of product management, and on the future of startups and founders. It's a very exciting time. It's also a very scary and destabilizing time for a lot of people, and my thinking is the more you are aware of what's possible today and where things are going, the better position you'll be in to thrive in this very wild and crazy future that is coming very fast. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing feature episodes, and it helps the podcast tremendously. With that, I bring you Amjad Masad. Amjad, thank you so much for being here. Welcome to the podcast.

Amjad Masad (00:02:46):
It's my pleasure.

Lenny Rachitsky (00:02:47):
I thought it'd be great to start with just having you explain what is Replit? What's the vision? Where is this going? What job does it do for people?

Amjad Masad (00:02:56):
The idea behind Replit is that making software today is very difficult and we want to make it easier. One of the reasons for the difficulty is that it is very fragmented, so you would need to download what's called an IDE. It's basically a code editor. You need to download the runtime, basically Python or JavaScript, need to figure out a package manager to configure your kind of open source packages, and once you've done all of that, you need to figure out how to deploy it, how to share it. So it's a very hard process, and that's one of the ways where people get stuck and never learn how to code because it just feels like this cumbersome IT process.

(00:03:42):
And so the vision for Replit has always been is like, okay, making software is fun, is great, more people should do it, but so for more people to do it, it needs to be easier to do, it needs to be in one place, and it needs to be learnable. It's easier to learn. So that's the product today. It is I think one of the more easier IDEs/ environment/deployment environment on the internet, and I think we make it really easy for people to just jump in even without prior experience of coding, especially now with the new AI products that we built.

Lenny Rachitsky (00:04:22):
This episode is brought to you by WorkOS. If you're building a SaaS app, at some point, your customers will start asking for enterprise features like SAML authentication and SCIM provisioning. That's where WorkOS comes in, making it fast and painless to add enterprise features to your app. Their APIs are easy to understand so that you can ship quickly and get back to building other features. Today, hundreds of companies are already powered by WorkOS, including ones you probably know like Vercel, Webflow, and Loom. WorkOS also recently acquired Warrant, the Fine Grained Authorization service. Warrant's product is based on a groundbreaking authorization system called Zanzibar, which was originally designed for Google to power Google Docs and YouTube. This enables fast authorization checks at enormous scale while maintaining a flexible model that can be adapted to even the most complex use cases. If you're currently looking to build role-based access control or other enterprise features like single sign-on, SCIM, or user management, you should consider WorkOS. It's a drop-in replacement for Auth0 and supports up to 1 million monthly active users for free. Check it out at workos.com to learn more. That's workos.com.

(00:05:40):
This episode is brought to you by Persona, the adaptable identity platform that helps businesses fight fraud, meet compliance requirements, and build trust. While you're listening to this right now, how do you know that you're really listening to me, Lenny? These days, it's easier than ever for fraudsters to steal PII, faces, and identities. That's where Persona comes in. Persona helps leading companies like LinkedIn, Etsy, and Twilio securely verify individuals and businesses across the world. What sets Persona apart is its configurability. Every company has different needs depending on its industry, use cases, risk tolerance, and user demographics. That's why Persona offers flexible building blocks that allow you to build tailored collection and verification flows that maximize conversion while minimizing risk. Plus Persona's orchestration tools automate your identity process so that you can fight rapidly shifting fraud and meet new waves of regulation. Whether you're a startup or an enterprise business, Persona has a plan for you. Learn more at withpersona.com/lenny. Again, that's withpersona.com/lenny. What's the scale of Replit at this point? How large has this gotten? How many people are using it?

Amjad Masad (00:06:55):
We have 34 million users globally. We have a large global presence. There's people everywhere learning to code on Replit, building startups, building personal software, personal tools or internal tools of the companies. More recently, we've been expanding to companies. We released our kind of B2B package in July, and that's been growing really fast. It's been really fun to see people bring Replit to work as well.

Lenny Rachitsky (00:07:25):
Damn, I knew it was popular. I didn't realize it was that large actually. As I was preparing for this podcast episode, there's this tweet that went viral where this guy, Jevin, who I actually know. I know this guy from Canada, he's awesome, tweeted about how his 11-year-old girl built an app in Replit. She just had an idea and she built it. And the best part of it is someone in the... replied to him and they're like, "You have to launch an app. You have to host it somewhere. You have to build a database. You have to deploy it. There's no way to do that." And he's like, "No, that's exactly what Replit did."

Amjad Masad (00:07:59):
Yeah, that's what we do. Everything that commenter was talking about, and he's right. The surprising thing about an 11-year-old building an app is not so much even the coding, it is like all the nonsense around it, and so we just abstract all that away.

Lenny Rachitsky (00:08:19):
I love that and I struggled with that myself when I was an engineer way back in the day.

Amjad Masad (00:08:24):
Oh, you were an engineer. I didn't know that.

Lenny Rachitsky (00:08:26):
I was. I was an engineer for 10 years. I was an engineering manager, and then I jumped ship into product.

Amjad Masad (00:08:31):
Wow.

Lenny Rachitsky (00:08:32):
I'm happy I did but I do miss that. I was not an amazing engineer. I was a good enough startup engineer, so this is the kind of stuff that I would've left to use. So we're going to jump into a demo of what this actually looks like. I thought maybe actually before we get into it, there's other tools that people are aware of that help you build stuff. And so to put a finer point on what this does and how it's different from other things, you may have heard of, say, Cursor, it comes up a lot these days, just talk about a little bit about the competitive landscape of who else is out there that helps you build product.

Amjad Masad (00:09:04):
Again, we go back to this idea of end-to-end platform for making software. So that's from writing code all the way to deploying it, and monetizing it and all of that. Now, every step in the process of the software development lifecycle, there are a lot of different tools. So Cursor is a fork of VS Code that's made that has really awesome AI tools, but that's an editor. You still need runtime, you still need a deployment environment. Actually, quite a few users use Cursor in tandem with Replit, because Replit just simplifies the runtime and deployment environment.

(00:09:42):
And so you have products, AI products, different places in the software development lifecycle, but really what differentiates Replit is that we do everything, but also that makes it harder to adopt for certain people. If you're at a big company, it's very easy to bring a new editor and start coding with it. It's quite hard to bring something that's quite opinionated about everything from how the code runs to how the code deploys, but that's the trade-off we're willing to make is like yeah, we're not going to get into the enterprise main software development pipeline, but we want to empower everyone to be able to build software, and that means product managers, designers. We have operations people, sales ops, HR ops. We have lawyers using Replit, and so it is democratizing the act of software engineering.

Lenny Rachitsky (00:10:49):
Amazing, and that's why you're here. Let's do a demo. While you're pulling it up, you're going to share your screen and show us what this product can do. And the reason I am excited about doing a demo, and this is an experiment, kind of a new type of podcast episode I'm doing where we're diving into specific products and what they can do, I feel like there's so much talk about AI and what it's doing and people keep reading about, oh, AI can do this and AI can do that, and I feel like not many people actually see this stuff in action, especially the most cutting edge stuff. I think people are unaware of just how far things have gone and how much is actually possible, especially when someone that knows what they're doing is using the product. So I'm excited to show people what is actually possible and especially because this is going to impact the future of product management and product teams. So I'll turn that over to you. Give us a demo.

Amjad Masad (00:11:37):
Awesome. So this is Replit's homepage. You can create what's called a Repl, which is a project. We have all sorts of languages. You can pick from really in the hundreds, but most recently, and this is how Replit became a thousand times easier, is you can just describe what you want to make. So you go on this home page, we have this text box, and you can write something like make me a cool app or what have you, but a more descriptive prompt is better.

(00:12:11):
And so I asked RPM at Replit, Aman Mathur who's a fan of the show to tell me what PMs like to build. And so he came up with a prompt. He kind of really crafted a great prompt. So I'm going to put it here. And basically, what we're asking for is we want to build a web application. You can say what stack you want to use or you can leave it up to the AI to decide. Here we're saying build it in Node.js for product managers to track feature requests on a public dashboard. So say I have a product, I'm growing, I have a community, I want that community to engage with building the product. I want them to submit feature requests, vote on them. I want to be able to manage that. So we're talking here about the features of voting system, feature requests.

Lenny Rachitsky (00:13:02):
Read a few of them just for folks that aren't watching on YouTube to give them, send some of the stuff in this prompt.

Amjad Masad (00:13:07):
So a feature requests submission, so allowing the users to add features. A voting system, so allowing users for these features, feature requests and status tracking, being able to, it's like a kind of advance style board with columns like planned and progress, so that way the admin can kind of share with the community what they're building. And we want it to be user-friendly design, so make it modern and all of that nice kind of prompty things. And then admin controls for product manager. So as a product manager, I want to be able to really manage this community.

Lenny Rachitsky (00:13:44):
I love that it builds internal tools too, not just the front end.

Amjad Masad (00:13:47):
Yes. Exactly. Exactly. All right, so we're going to start building. Since this is a pretty big, big prompt, the initial coding might take a while. There's different styles of using Replit agents. I often go with minimalist prompts. That's also how I code as well. I have a vague idea for what I want to build and iterate from there. Other people, product managers like to write PRDs and more descriptive things, and you can do either of those things. The AI now responded and then said, I'll build all of that for you. I'm going to build up the initial prototype and you can tell me how it feels, and then we can make it better from there. The AI is also suggesting, adding comment threads, implementing email notifications, and so I can select those and it's being creative, it's telling me what else I could build, but for now, I'm just going to go with a prototype and then we can assess from there.

(00:14:50):
So as you see, as the prototype is starting, you can see this progress pane where we can watch the AI doing its thing here. It's created a Postgres database. Obviously, when we're building a full-stack application, you need to be able to save things. This is one of the cool things about Replit. We have all these services, storage, database. So now it's coding, it's building the database schema. Now, it's building the home page, and it's actually quite fun and edifying to watch it build this, because you can really start to learn how to structure web apps. And if it runs into a problem and as things get complicated, it might run into a problem and you want to be able to help debug and things like that, it's good to be able to have an idea of what's going on, but it's not necessary. I think a lot of people just don't care about the code and are still able to build things, but we want to make the process transparent. We want to show people exactly what the agent is doing.

Lenny Rachitsky (00:15:57):
You're basically sitting there behind an engineer on a computer and just watching them code is what the experience feels like.

Amjad Masad (00:16:04):
Yeah, and actually, the way we built it is it's a multiplayer system. So Replit has real time, what we call multiplier coding, and we reused the multiplayer system to build the agent. So the agent in the code is structured as another user of the platform. So basically, we're both coding together. So I can go into the files here and that's the thing that makes Replit really cool. I think people are familiar with some of the more chat interfaces like v0 and others where it's purely chat, but this is a full IDE where you can go and look at the files and edit them yourself or ask the AI for an explanation.

Lenny Rachitsky (00:16:51):
What's the limitation of what this can do today? What can't you do? Say you're like, you have zero coding experience, what sorts of products can you not yet build with something like this that might be possible in the future? How far does this take you now?

Amjad Masad (00:17:08):
You can build MVPs. I think you can also start to get some initial users. I think when you start iterating on the product like large iterations, you might run into problems. For example, it's not very good at database migrations, and so we're trying to fix that. So when you're iterating on the product, a lot of the times, you're actually changing the structure of the app and that requires database migrations. And so now it might change the database in a way that creates an error that's unrecoverable. And at that point, you might get stuck, especially if you don't know how to code.

(00:17:56):
Some people will figure it out by going to ChatGPT and Claude and asking questions and I actually am really inspired about how persistent some of our users are, which is really amazing. But I think you'll get an MVP pass, the MVP where it's a product that's working and you need to change and iterate on it. It's still a struggle now, but I expect over the next few months, we'll continue. It's if you think about it's like we're building as you were building, so we're building out the agent so that it can continue getting better as our users are also building their applications.

Lenny Rachitsky (00:18:40):
Got it. So what I'm hearing is it's really good at building the first version and helping you get to something that you can even have people use. It's not amazing yet evolving from there, using AI to help you make the product better and better and better and iterate.

Amjad Masad (00:18:55):
Yes.

Lenny Rachitsky (00:18:55):
But you can get in there if you know how to code and take it from there, right?

Amjad Masad (00:19:00):
Yes or you can hire someone. We have a feature on the site called Bounties where you can hire human coders to kind of help you finish.

Lenny Rachitsky (00:19:14):
That's going to be our job for humans. That'll remain for a while.

Amjad Masad (00:19:18):
You know what we want to do? We want to get to a point where the agent can go grab a human when it runs into a problem. I think that would be sick.

Lenny Rachitsky (00:19:32):
Oh, my God. It's like everything's reversed. I love it. Oh, I think it might be done. Check that out.

Amjad Masad (00:19:38):
Yeah. So now the agent is asking us, is the application running and showing the homepage?

Lenny Rachitsky (00:19:46):
Like it's confirming.

Amjad Masad (00:19:48):
Yeah, almost asking us to do a QA. I'll just say yes. So it found an error. So there's an error here and it's like there's a dumb warning, "I'm going to fix it." So in the meantime, as it's fixing it, so it can be proactive, right? Because it looks at all the errors and things like that, but in the meantime, we can use it. I just created an account. It's coding.

Lenny Rachitsky (00:20:12):
[inaudible 00:20:12] It's cool.

Amjad Masad (00:20:11):
Let's see how it restart. Okay, we'll wait for it.

Lenny Rachitsky (00:20:16):
How long would you say it would take an engineer to build this? A typical engineer?

Amjad Masad (00:20:22):
A few days, I would say to a week. I mean, if you're really good, it might be hours but it probably would take me a few days. I would say I'm like decent engineer, it'll take you a few days.

Lenny Rachitsky (00:20:40):
And it took how much? 5 to 10 minutes.

Amjad Masad (00:20:43):
Yeah, and it probably cost us something in the sense.

Lenny Rachitsky (00:20:50):
Wow, in terms of compute.

Amjad Masad (00:20:52):
In terms of compute, yeah. Probably, I would estimate it like 15 cents or something like that.

Lenny Rachitsky (00:20:58):
Wow. Okay, so here it is.

Amjad Masad (00:21:01):
Here it is. And the agent was like, "Okay, this is looking good, completed it if you want to deploy it." But I'm like, "Okay, I'm going to test it first."

Lenny Rachitsky (00:21:09):
And so currently, it's living just locally on your local host.

Amjad Masad (00:21:13):
Yeah. It's not local host, it's on a Replit but yes, it's the equivalent of local host. Because it's really easy, I can even invite you to this session. You can be here with me and so it's all online.

Lenny Rachitsky (00:21:26):
Got it.

Amjad Masad (00:21:26):
So let's submit a feature. So make the product prettier. That's what a typical user might say. So we have this here, you can upvote it. I guess I can't upvote it because I'm the user that created it, but created another user. You can upvote it. But now we need to be able to move things around as the admin, so I don't know how to log into the admin panel. So I'm going to ask the agent, how do I log into the admin panel? So it might've already built the feature, and it's not exposed in the right way. It'll be able to [inaudible 00:22:08]

Lenny Rachitsky (00:22:08):
What I love about just watching you interact with this thing, and just real quick throughout, it feels like an engineer that is behind the scenes building this thing like on Slack and you're just talking to them. They built this thing, they're like, "Check this out, I'm done." And you're like, "Oh, okay, about how do I log into this admin panel?" And they're like, "Okay, here we go."

Amjad Masad (00:22:26):
Yeah. So it says, "Would you like me to help you register account?" So it's creating an account, an admin account for me. So it's not only builds things, it also maintains things. In this case, it's actually doing SQL queries. It's not writing code to create an admin account for us.

Lenny Rachitsky (00:22:51):
It's insane. I want to talk about the implications of this on product development and product management and founders, but what we just witnessed is somebody, I know you do have technical abilities, but someone that didn't have to have any technical skill, build a real product that people can use in five minutes that looks good and works, and you could keep making it better by talking to this agent.

Amjad Masad (00:23:17):
I'll tell you from our experience what we're seeing, there's so many products that are empowering developers. It's a very easy calculation to say We're going to make engineers 20% better and we're going to sell it to companies and we're going to take 10% of that value, right? That's why there's so many startups now that are just trying to make engineers a little better. Our calculation is like, well, what if you made everyone developer? What does that look like? And so when we released agent and really made programming a lot easier, what we're seeing is that people, exactly like you said, people view this as a developer in their pocket essentially. What we're hearing from customers is that I'm doing things I would otherwise have to go hire a developer, but also because the activation energy is lower than going to hire developer, whether Upwork or other places, I'm building a lot more ideas that otherwise I wouldn't have built.

(00:24:26):
I think it was it called the javelin's paradox or something like that, which is when the cost of things go down, the total consumption of it goes up, which I'm not sure why they call it a paradox, but the cost of electricity goes down, maybe you would expect that the total spend goes down, but actually total spend goes up because people consume more of it. And so I think that's going to be the case of software. As the costs go down, people will just make a lot more software to improve their lives and to improve their work and start more startups and all of that.

Lenny Rachitsky (00:25:05):
So to follow that thread, what are you seeing inside of startups or even big companies in terms of how folks are already using this knowing this is the worst it will be and it will only become smarter and better these days? How are people actually using this that are say product managers or just non-technical people within startups or bigger companies?

Amjad Masad (00:25:26):
On the SMB side of things, a lot of people are building kind of back office tools. So we have real estate agents that have a lot of data, have a lot of things they want to manage in their business that building a lot of these tools, that they otherwise would have to buy, but typically when you buy, it's actually not exactly what you need. And that's kind of the problem with SaaS, like one size fits all. And so a lot of people are seeing it as sort of a SaaS replacement for in-house tools and things like that. And then when you go to the bigger companies, it's anywhere from prototyping to actually production apps to tools as well. So we've seen product managers build, like I said, like a v1 of an app and actually go out and test it with users. I can't name the company, but there's a public company that have used Replit to test a v1 of an app.

(00:26:35):
And obviously after that sort of works, they take it to the engineers and they're like, "Okay, we built this thing. We think it's a great thing. We test it with some users. Let's go actually put it on the roadmap and build it into the actual product." So you are instead of unblocking product managers from having to need engineers for everything that they want to build so they can really build the v0 or v1 of the product.

(00:27:04):
And that's super empowering for them. We saw it also with marketing departments like SpotHero has a head of marketing that actually can code decently well but use Replit to build these apps, and they built a competitive analysis application that looks at a competitor's pricing and makes sure that they're benchmarked correctly. And so it's a full stack app use database and everything and it runs on a continuous fashion. And we see sales engineers use Replit to spin up prototypes really quickly. So actually someone at X, formerly Twitter is on the partner engineering side of things, and he uses Replit agent to spin up applications and prototypes for customers to see how they can use the X API.

Lenny Rachitsky (00:28:06):
I love this. I love these examples. By the way, the demo, is there anything else you want to share about the demo before we close that out?

Amjad Masad (00:28:14):
So it created an admin account. We can ask it with the username, password and kind of go into it and manage it but basically that's it. The app's complete in terms of what we ask for. We can send it out. I can give you a URL. Let's actually just deploy it really quickly to show people how you can deploy.

Lenny Rachitsky (00:28:35):
Maybe the show notes, we'll link to the app, you could check it out.

Amjad Masad (00:28:38):
Sounds good.

Lenny Rachitsky (00:28:38):
Okay, cool. That's amazing. So this is deploying it onto some cloud provider. I don't know what you use, but...

Amjad Masad (00:28:44):
We use Google Cloud. So we abstract all of that away from you, but we use Google Cloud behind the scenes.

Lenny Rachitsky (00:28:52):
Imagine a place where you can find all your potential customers and get your message in front of them in a cost-efficient way. If you're a B2B business, that place exists, and it's called LinkedIn. LinkedIn Ads allows you to build the right relationships, drive results, and reach your customers in a respectful environment. Two of my portfolio companies, Webflow and Census, are LinkedIn success stories. Census had a 10x increase in pipeline with a LinkedIn startup team. For Webflow, after ramping up on LinkedIn in Q4, they had the highest marketing source revenue quarter to date.

(00:29:26):
With LinkedIn Ads, you'll have direct access to and can build relationships with decision makers including 950 million members, 180 million senior execs and over 10 million C-level executives. You'll be able to drive results with targeting and measurement tools built specifically for B2B. In tech, LinkedIn generated 2 to 5x higher return on ad spend than any other social media platforms. Audiences on LinkedIn have two times the buying power of the average web audience, and you'll work with a partner who respects the B2B world you operate in. Make B2B marketing everything it can be and get $100 credit on your next campaign. Just go to linkedin.com/podlenny to claim your credit. That linkedin.com/podlenny. Terms and conditions apply. Let's go down this thread actually while this is happening, just like what allows for this to be possible technology wise? What is the stack? Whatever you can share that enables this to exist.

Amjad Masad (00:30:26):
Yeah, for sure. First of all, it's all the abstractions that we built. So the way a Replit works is the very bottom layer. It's our runtime. So this is the operating system, this is the package manager, this is the language runtimes. We built a system that is able to install packages in any language, including native packages. So the AI, anytime, it needs a package. I can go here and show one of those. By the way, the AI can take screenshots as well so that it checks it works. So here you can see it is taking screenshots to make sure that the homepage is rendering. Here, you can see it wanted a drag and drop library, and so it installed that. And so it has access to all the packages across all languages, including Linux and all of that. And then the layer on top of that is the editor and the infrastructure that runs the editor, including what I described as the multiplayer editor.

(00:31:33):
And then we expose all of that infrastructure to the AI. And there's almost like a new discipline called AI Computer interfaces. So sort of like HCI is now a ACI and turns out LLMs need interfaces that are actually quite different than humans. They're trying to make them use human interfaces like Anthropic's computer use, but those are really expensive and you need to process all this images and video. So instead, for the shell for example, we give it sort of a text representation of what the shell is doing at a certain increments for package installation. We give it a certain tool for editing. We give it an editor tool that when it's writing the code, it's getting feedback on whether there are errors or not, similar to what a human sees, but it's actually old text just to make it easier. So that's AI computer interface, and obviously, all of that is sitting on foundation models. So the improvement in foundation models has allowed us to build this.

(00:32:51):
The most important model that we use is the Sonnet model from Claude, from Anthropic, and it is the best model at coding. So that's the model we use for coding, but we use models from OpenAI as well because a multi-agent system. And so we have models that are critiquing. We have manager editor model, and we have a critique model and different models will have different powers. We also train some of our models, like the embedding model for search is something we trained internally. So I actually wrote about it back in '22. I said it's going to be society of models, like products will be made of a lot of different models, and it's quite a heavy engineering project.

Lenny Rachitsky (00:33:47):
To say the least. We were talking offline and you said you've been working on this since 2009 when you first built the first idea of Replit. Is that right?

Amjad Masad (00:33:56):
Yes.

Lenny Rachitsky (00:33:58):
Oh, my God.

Amjad Masad (00:33:58):
Here's the deployed app. I can send it to you and you can use it and you can see my request even on the logged out page so I can register, upload it, and log in as admin and move things around. We can see what's in progress, what's completed.

Lenny Rachitsky (00:34:14):
This looks like a product. I could see designers spending days designing, passing it to engineering, PMs, having feedback, engineers taking a few days to build it.

Amjad Masad (00:34:26):
Yes.

Lenny Rachitsky (00:34:27):
And here's just a prompt, here's what I want.

Amjad Masad (00:34:30):
That's right. And we can iterate on it very easily. We can also iterate on the UI. We can say, I don't like this or that, and it'll do a good job. So we can go here, we can start a new session or a new session to create an entirely new feature here, and it'll just do the right thing.

Lenny Rachitsky (00:34:47):
And it builds from that code base. It understands here's what you've built. I want to add this thing.

Amjad Masad (00:34:52):
Yes.

Lenny Rachitsky (00:34:52):
Okay.

Amjad Masad (00:34:53):
And that becomes your history, right? This was the v1 and now I'm working on this new feature, and it's almost like what engineers do in Git commit messages. By the way, it generates Git commit messages for everything that it does so you can roll back as well. And so we're trying to make it so that yes, it's for everyone, but we're trying not to abstract too much away. We want to build tools for you to learn to use. And so we want power users to be able to understand the full power of Replit and it is really deep product. I think you can spend a couple of years to kind of master it.

Lenny Rachitsky (00:35:40):
I want to talk about implications, but I want to come back to something you mentioned that is incredible that people may have missed. You basically built a computer specifically designed for the AI agent to use that is a different version of a computer specifically optimized for how AI wants to use a computer.

Amjad Masad (00:36:00):
Yeah. So there's an entire discipline called like HCI, right? It's like how do you do that-

Lenny Rachitsky (00:36:07):
Human-computer interaction.

Amjad Masad (00:36:08):
Yeah. So now there are papers about AI computer interfaces and interactions. And so large language models are trained on large stacks of corpus from the internet, but they're still kind of alien creatures. So they're not like humans, so they have different behaviors. It's unclear what's the best way to give it an editor. So there's so many experimentation about what's the best way to give it a view on what's editing, how many files can you show it before it starts to hallucinate. And right now, it's more of an art than science, but it's becoming more and more like a science.

Lenny Rachitsky (00:36:55):
This is insane. So it's a simple way to think about it. There's this foundational model, here's what I want you to build, and here's a computer to use to build it.

Amjad Masad (00:37:05):
Yes.

Lenny Rachitsky (00:37:05):
How am I [inaudible 00:37:07]

Amjad Masad (00:37:06):
Here's a computer with a set of tools. Here's a tool to install a package. Here's a tool to edit the code. Here's the tool to run a SQL query and also services. Here's a bunch of services you can graph from. Here's a database service, here's an object source service, here's an auth service. So you can think about it as a bunch of external services, the computer with a bunch of tools, and they're all interfacing with the foundation model.

Lenny Rachitsky (00:37:38):
It's funny listening to this how, it starts to feel like the fact that we might be living in a simulation is not as far-fetched as it may feel. Like this feels like the beginnings of what a simulation computer would be.

Amjad Masad (00:37:50):
Yes. You can go really Sci-Fi on this and it's like where is it headed, right?

Lenny Rachitsky (00:38:03):
Yeah.

Amjad Masad (00:38:03):
If we give it enough tools, let's say, I can drop it in Slack and instead of interfacing with it in this fashion, I want to interface with it in a totally autonomous way. So we actually have this feature coming up where instead of me testing it, we give it another agent. So here, instead of me interfacing with it and saying this is running or not running, we can give it another agent that is actually testing the application and then let's say interface with it entirely through Slack. And I'll say something like, give me Taylor Swift tickets the moment they land.

(00:38:49):
And so it'll build an app that continuously monitors the web for when Taylor Swift tickets land and there's an agent that's using the app to be able to get that. And you can imagine it has some kind of wallet or credit card. And then the moment it lands, it gets it. What I'm trying to say is that software, like agents being able to do software, is how AI gets more general because software runs our lives, runs the internet, runs our businesses. And so the more competent AI becomes that software, the more general they are in terms of what they can do.

Lenny Rachitsky (00:39:36):
Okay, this can go in so many directions. I'm going to bring us back to the implications for people building products, say, product managers, founders, how does this change, that function, that skill set? What skills do you see will matter more matter less? Which functions are maybe in some danger and they should start thinking about a different career path?

Amjad Masad (00:39:59):
One interesting persona that we're seeing is the CEO, the CEO of startup. Andrew Wilkinson from Tiny is a big user. And so these people are typically creatives. They built a company, they hired people. A lot of them can't code. A lot of them are designers or product managers or something else. And you can imagine a bottleneck, you can imagine a bunch of ideas in their head, and the ideas have to translate through them talking. And then someone else listening to them and assuming that someone else actually understands what they say, and then that's someone else going and trying to build what they want to build. And also assuming that person has time, because a lot of times, your engineers are kind of stuck building the current thing. They're not thinking about the future thing. And so what gets me excited is a lot of these CEOs are building the future concept, the next product they're going to build, the next, say, company they're going to build.

(00:41:08):
And so it unlocks the creativity and again, sort of unblocks them from that. And look, it's a v1 of the product but it can push things forward. You can touch it, you can feel it, you can say, okay, this really has lags and we should work on it. You give it to your engineers and they can improve on it from there. So that's one persona but I'm really excited about it, the CEO/founder. In companies, one of the things that I think is sort of hard about tech companies is these silos between designers, product managers, and engineers. And everyone feels that pain of, we have low bandwidth communication, which is language and then text on Slack and Zoom calls. And it leads to a lot of frustration, because it's really easy to misinterpret people and again, leads to siloing where people working on something, and then you pass it on to the next team and it's not really what they expect.

(00:42:30):
That happens a lot between designers and engineers, but the common language that everyone shares is code. Ultimately in software tech companies, everything that we're talking about need to eventually flush out in terms of code. And so what if the language becomes actually working prototypes and working applications? For example, we have a Figma extension that translate Figma mocks into React that runs on Replit. So instead of giving the engineers just mocks or screenshots, whatever, you just say, oh, here's a bunch of React code, just make sure it runs on our infrastructure but don't mess with it, don't move the pixels around. And so I think it just opens up silos of the companies, make communication around product a lot more concrete, because I can give you a working prototype and that'll change how people work, if you can imagine that everyone can make software. It's really kind of a radical reimagining of not just what tech companies are but really what most companies are because everyone can be more general.

Lenny Rachitsky (00:44:04):
So say you're a PM listening to this, an engineer or designer, what skills do you think if you were one of these folks? If you were in building Replit right now, what kind of skills would you suggest folks focus on more and would you think are just like, okay, this can be less valuable in the future, don't worry about these sorts of things? And you can either pick one of those three functions or all three.

Amjad Masad (00:44:25):
I think a very important scale that's perhaps harder to develop but it's worth working on is being generative, being more generative, being able to generate new ideas quickly, because you can think about it as a factory line. So you have ideas, you have the production of these ideas or the initial production of these ideas, and then you have other people that want to consume these ideas or work with you on these ideas. And so typically you're bottlenecked by the middle part where your ideas are kind of like they're a lot of them and they're not fitting in, because they need to be made and they need to be made quickly. And so now you open up that bottleneck. So now actually making things is a lot easier. Actually, you become limited by how fast you can generate ideas, and I find that true of myself as well. I consider myself quite generative, but now I have this tool and I can build a lot more and explore a lot more and I'm finding that, well, actually, I'm running out of ideas sometimes.

(00:45:53):
So training that muscle I think is a good thing. I think learning a little bit of coding and not the traditional way of learning coding. If you go to a coding bootcamp, they're going to start with what is Git? Actually my co-founder, Haya, was a designer. When we're first building the Replit together, she went to WebAssembly to do a coding course. And the first day, they spent this whole time on Git and she's like, "What is that? What does it do?" I still don't know what it exactly does, but it's like you're inverting the process, you're giving the tool before the actual problem. And so I think all of that stuff, you don't have to worry about, so things that you don't have to worry about. I think a lot of the, as a PM, as a designer, as someone who's not in your code editor every day, don't worry about all the tooling.

(00:47:09):
And if you learn a little bit of coding just by talking to an AI, doing a little bit of debugging, building something with Replit, running into a problem and trying to fix it just using AI, you'll learn a bit of coding. And I have this that's been called not by me, dubbed as Amjad's Law, which is the return on investment for learn to code is doubling every six months. And really just learning a little bit of that skill, learning a bit of skill about how to prompt AI, how to read code, and be able to debug it. Every six months, that's netting you more and more power because you're going to be able to create a lot more. It's going to be easier to create. You're going to be able to create a lot more complete things. So that's another skill that I think could be necessary.

Lenny Rachitsky (00:48:15):
This is super interesting. Okay, so this last point, you made Amjad's Law. It's interesting because when people, as someone's listening to this, I could see them being like, engineers are in trouble. Why do you need engineers at this point? These agents are building the code. Your point is specific engineering skills are going to be incredibly valuable and more and more. How often are they doubling would you say? Every year you said?

Amjad Masad (00:48:40):
No, every six months.

Lenny Rachitsky (00:48:41):
Every six months, these specific engineering skills are becoming more valuable. And the idea is you don't need to know everything. You don't need to know the foundation, to build the app as much. It's more to unblock the agent and understand the mental model of how this stuff is built so that you can move forward fast.

Amjad Masad (00:48:59):
That's right. That's right. Understanding the basic components of it, I would say, yes.

Lenny Rachitsky (00:49:03):
Yeah, so it's like we need new engineering schools to teach you these very specific skills versus spending years on algorithms.

Amjad Masad (00:49:11):
And I think no one has done that yet, and I think this is a big business probably ready to get built. It's like AI native coding. It's totally different than traditional coding. That's why on Hacker News, there's so much skepticism about AI native coding tools, because they're like yeah, it's a glorified autocomplete. And I understand if you're writing operating system, kernels, it's not really doing that much for you, but if you're building products, it's building it for you at this point. And so if you're starting a school to teach AI native coding, you would skip so much of computer science and the basic tools, and you would teach the basic idea of how to structure an app, and then you would teach prompting and then you would teach, I think a little bit of debugging. I think debugging is quite a good skill right now to learn.

Lenny Rachitsky (00:50:22):
Interestingly, if you want to be good at debugging, there's a lot you need to understand, which is basically what you're saying is that's the subset of things to understand is things that break. And to do that, you have to understand how it all works. What are servers? What are APIs? All these things. Okay, so we've been talking about how this is very good right now, building a prototype, building a v1, MVP, people can use it, you can deploy it. You deploy this app, people can start using it, and there's a scale it can reach. Do you see a future where you can build a Salesforce sized business fully Replit or other tools that can scale to hundreds of billions of dollars of value? Or is there just going to always be some limit of like, you need actual engineers and designers sitting on this thing, building it, thinking it? Awesome.

Amjad Masad (00:51:06):
If my law is directionally correct, even if the months are not, I'm not exactly right that the duration is correct, you're going to see a compounding effect of the power. It's actually quite hard to convince yourself. But if you really convince yourself that we are on a massive scale of improvement in AI, then the answer is yes. And it's absurd to my engineering mind that I'm saying it is, but know Ray Kurzweil, this futurist talks about how exponentials are really hard for humans to grasp. And so actually when we started building the agent, I told the team, it's easy and we fall in this trap before. It's easy to build and optimize for today. In '22, we built Copilot-like thing and autocomplete. We train our own models, we optimize the hell out of them. But at some point, that modality was kind of not the right modality, which is the autocomplete modality.

(00:52:11):
And the right modality is actually this, I think for now, as being able to chat inside the programming environment and for the agent to create things for you. But in order for us to make that bat, a year ago the models were actually not there. The models could not do this, but we were like, okay, we're going to build for the models that are landing in six months. And truly six months later, the model started to land that are capable of this, of the reasoning that we needed and whatever. And so that was like saw it if you want, which is, oh, wow, we switched to it and the reasoning improved so much. And six months later, you have a son of you too. And so it's really almost like a six months cadence. And so if we're really on this trajectory, then I would say next year, you're able to just scale and maybe you get thousands of users paying you.

(00:53:08):
The AI can do maintenance. We already showed the AI doing SQL queries and doing migrations, so I will be able to do maintenance, debugging, things like that. I think where it gets really tough is that when you're hitting scale and you want to architect a system that is resilient, and so that means you would start sharding databases and you would start using different queue systems and components and things like that. And I think the AI needs to have access to the entire suite of tools to be able to do this.

(00:53:49):
And I think that's going to be the next bottleneck. And I think the AI needs to be a lot more reliable at doing that. But I could imagine whatever, five years from now, someone running a billion dollar company with zero employees where it's like the support is handled by AI, the development is handled by AI, and you're just building and creating this thing that people are finding valuable and are paying you for it. That being said, it's worth thinking about the economics of it. If the cost of software goes down a lot, then what is the price that you can charge on software? So can you actually build the next Salesforce if anyone can generate Salesforce? And then the question is, and this is why I emphasize being generative, because I think then the thing that will make you better is by being able to iterate and improve the thing really quickly and generate new ideas.

Lenny Rachitsky (00:55:01):
And stay ahead of all the other people building these tools so quickly. Oh, my God. An interesting other kind of mental model I'm seeing as you talk about this sort of thing is not to offend religious folks, but there's this concept of God of the gaps. I imagine you've heard that where it's like God explains all the things that we don't yet understand. And over time that kind of space shrinks and God's like all the things we don't get yet, those gaps. That was God that proves there needs to be a God. And it feels like right now, humans are the gaps in these tools or these agents you talk about that you can hire within Replit are fixing these little gaps. And over time, AI will fix these things themselves.

Amjad Masad (00:55:44):
That's right.

Lenny Rachitsky (00:55:44):
And these gaps will shrink.

Amjad Masad (00:55:47):
Unless we hit some fundamental limit and the current regime of AI, which I'm not an expert about how far transformers could scale, but I feel like we found the thing that could scale pretty far, but maybe there are limitations in data or other things like that that we could be surprised by. But if there isn't, then we are on a massive trajectory of removing these gaps quickly.

Lenny Rachitsky (00:56:23):
Yeah, very true. We have no idea. We keep thinking it's just going to keep going, but maybe it'll stop at some point. I could keep going and going, but I think we should also let people go play with these things and process all the things we've been talking about. Is there anything else that you think might be helpful for folks to think about or learn or study?

Amjad Masad (00:56:43):
I'll give advice to founders or leaders at companies. The way we work is going to change rapidly, and it's important to be resilient to that change. One thing that I think is really difficult now is having roadmaps, especially if you're doing anything in AI, but really anything that AI could affect, you want to be able to react to it really quickly. And so when the Anthropic drop the computer use set of capability, we slaughtered our roadmap because we don't really have an explicit roadmap. We immediately jumped on it and started building things and we launched some things around it. We're going to be doing more with it, but there's going to be capabilities that are going to drop. And you want to really, in some cases, if it really affects your business, you want to be able to jump on it really, really quickly. So being agile, not being stuck with roadmaps, being able to just say, oh, we're just going to switch priorities right away, is going to be super important.

(00:57:59):
Not being, like I said, with silos at Replit, there's so many people that are on the scale of designer to engineer, designer, product manager. Actually, I mentioned Amman earlier. He started as a designer at Replit, and now as a product manager. We have people who start as designers, become engineers, and we have people in the middle and we're comfortable with that design engineers that fit at different parts of the scale. And the design engineers go to the design correct meetings and some designers go to the engineering meetings. You got to be fluid because again, when designers can code and engineers can design, I mean it really becomes, you can't have a lot of structure around that. So you want to build a culture and you want to build an environment or milieu that is really, really flexible, which is uncomfortable for a lot of people.

Lenny Rachitsky (00:59:03):
Man, the future is wild. Everyone's a hybrid person now. Let me just actually double down on what you just said, which I think is really interesting. It's almost like if you're an engineer, where your skill set will become most valuable is unblocking these AI tools and knowing debugging and figuring out how to allow it to go further and further and further. Within PM and design land, based on what you're describing, where the skills will become more valuable is generating ideas, almost like finding opportunities, discovery, finding what problems need to be solved, and then articulating that as clearly as possible to the AI tooling.

Amjad Masad (00:59:44):
That's right.

Lenny Rachitsky (00:59:45):
Super interesting.

Amjad Masad (00:59:45):
Yeah, this is a very crisp sort of advice that people can follow today, I think.

Lenny Rachitsky (00:59:50):
Oh man, what a world. Okay, I'm jot. This is incredible. My mind is racing. I've got to go build some apps immediately.

Amjad Masad (00:59:58):
Yes, you've back. Love that.

Lenny Rachitsky (01:00:00):
I will do that. So just to leave listeners with a couple things. One is just, what should they know? Where do they find you? How do they try Replit? Anything else other than just go to replit.com?

Amjad Masad (01:00:10):
Yeah, just go to replit.com. It's an open beta right now. We're kind of quickly improving and going to exit beta I think in a few weeks. But if you're comfortable testing something that's not perfect, go to replit.com. If you subscribe to our core plan, you should be able to access the agent and start using it. And we are, I think the place where we're most active is Twitter. So Twitter are like X, the handle Replit, R-E-P-L-I-T or my handle @amasad.

Lenny Rachitsky (01:00:45):
Oh, yeah. One other thing I wanted to make sure we had a chance to touch on is you're working on something new, something that's coming in the very new future, maybe the day this episode drops. Talk about that.

Amjad Masad (01:00:56):
All right. So depending on when the episode is coming out, this could be the first time people hear about it. But we have this product called agent. It is sort of high agency, does everything from setting up the project and all of that. And so now, we are working on assistant. Assistant is let's say the cousin of agent. It is a little less powerful but a lot more controllable. You can focus on features or areas of the code that you want to change and you still don't have to know how to code, but it is a lot more manageable and it is a lot faster.

(01:01:38):
So you saw how it took some time to kind of create the project and code some of the things. Assistant is in the order of milliseconds and seconds to be able to respond to you. And so again, as I talk about the idea of tools, we want people to have as much power and autonomy as possible. And so there are certain instances where agent is the best. It's going to do the debugging for you, it's going to create the database for you. But if you want more control, assistant is going to give you that.

Lenny Rachitsky (01:02:09):
Just so folks totally understand what this is going to do for them. What's the mental model for what this is? If it's like a person, we're helping you out.

Amjad Masad (01:02:17):
Agent is like having a developer work. You give them the PRD, right? And they're going to go and build the thing. Assistant is like you're sitting next to them. So they built the thing and now you walk over to their desk and you say, let me move this button. Three pixels to the left. Let me change this thing. So small increments of changes that you want happen really quickly and you want it reliably, that will give you that. So it's just much faster iteration on UI and things like that.

Lenny Rachitsky (01:02:58):
Incredible. The future is wild. Final question I always ask everybody, how can listeners be useful to you?

Amjad Masad (01:03:04):
Come work at Replit. We have a PM role. I think up if you're product manager. We're hiring engineers and product managers. So come work at Replit or refer someone to Replit, especially if you're like our tools and you want them to get better. The best way to do that is to get us great people we can hire.

Lenny Rachitsky (01:03:25):
Well, you're about to get a flood of product managers applying. Goodluck.

Amjad Masad (01:03:28):
Amazing. I love that.

Lenny Rachitsky (01:03:30):
Amjad, thank you so much for being here. This was incredible.

Amjad Masad (01:03:33):
Thank you. Thank you for your podcast and the community that you've built and newsletter and everything. It's been awesome to watch.

Lenny Rachitsky (01:03:40):
Thanks, man. Appreciate that. Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

