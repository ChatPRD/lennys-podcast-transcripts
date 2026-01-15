---
guest: Guillermo Rauch
title: 'Everyone’s an engineer now: Inside v0’s mission to create 100 million builders
  | Guillermo Rauch'
youtube_url: https://www.youtube.com/watch?v=-QsTmu2CqhA
video_id: -QsTmu2CqhA
description: Guillermo Rauch is the founder and CEO of Vercel, creators of v0 (one
  of the most popular AI app building tools), and the mind behind foundational JavaScript
  frameworks like Next.js and Socket.io....
duration_seconds: 5264.0
duration: '1:27:44'
view_count: 37057
channel: Lenny's Podcast
keywords:
- retention
- iteration
- subscription
- revenue
- management
- vision
- mission
- market
- persona
- jobs to be done
- design
- ui
- prototype
- startup
- founder
---

# Everyone’s an engineer now: Inside v0’s mission to create 100 million builders | Guillermo Rauch

## Transcript

Guillermo Rauch (00:00:00):
One of our users yesterday submitted feedback.

MUSIC (00:00:00):
(instrumental music)

Guillermo Rauch (00:00:02):
They were saying, "v0 is like a super genius five-year-old PhD with ADHD." I'm not going to oversell this. It knows everything about everything, but it has these sparks of brilliance.

Lenny Rachitsky (00:00:14):
How do you think things are going to change for product managers, for product teams?

Guillermo Rauch (00:00:18):
People could be more full stack. Imagine a designer that can ship a fully baked product, a product manager that can prototype and ship to production. We shouldn't put limits on ourselves and what we can build, and what we can ship, and what we can dream about making possible on these web surfaces.

Lenny Rachitsky (00:00:34):
A lot of people are wondering, "What happens to engineers? Should I learn how to code?"

Guillermo Rauch (00:00:37):
A lot of the programming jobs to be done that used to be specializations, I think, are going away, in a way. They're translation tasks, but knowing how things work under the hood is going to be very important for you because you're going to be able to influence the model and make it follow your intention a lot better.

Lenny Rachitsky (00:00:52):
We hear this word taste all the time, in terms of building taste, people are always like, "How the hell do I do that?"

Guillermo Rauch (00:00:57):
Taste, sometimes I think we think of as this inaccessible thing that, "Oh, that person was born with taste." I see it as a skill that it can develop. I think is extremely important to try lots of products. We have one of our internal operating principles as increasing exposure hours. Try to quantify how much time you expose yourself to watching how people use your products and you'll develop that muscle.

Lenny Rachitsky (00:01:25):
Where do you think the biggest change is going to happen?

Guillermo Rauch (00:01:26):
We need to stop talking about AI at some point. I just see a future where AI becomes synonymous with software. We build software and we use software to build software.

Lenny Rachitsky (00:01:38):
Today my guest is Guillermo Rauch. Guillermo is the founder and CEO of Vercel, which, amongst other things, makes a product called v0, which has become one of the most popular AI website building tools in the world. He's also a legendary engineer and contributor to open source. He's created some of those popular JavaScript frameworks in the world like Next.js and Socket.IO. He's both a builder and is building a product that's going to change the way we all build products in the future. This episode is incredible. If you want to really understand how product development is going to change with the rise of AI and what skills you should be focusing on right now, I highly recommend you keep listening.

(00:02:14):
If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become a yearly subscriber of my newsletter, you get a year free of Linear, Notion, Superhuman, Perplexity Pro, and Granola. Check it out at lennysnewsletter.com. With that, I bring you Guillermo Rauch. 

(00:02:34):
This episode is brought to you by WorkOS. If you're building a SaaS app, at some point your customers will start asking for enterprise features like SAML authentication and SCIM provisioning. That's where WorkOS comes in, making it fast and painless to add enterprise features to your app. Their APIs are easy to understand so that you can ship quickly and get back to building other features. Today, hundreds of companies are already by WorkOS, including ones you probably know like Vercel, Webflow and Loom. WorkoOs also recently acquired Warrant, the fine-grained authorization service Warrant's product is based on a groundbreaking authorization system called Zanzibar, which was originally designed for Google to power Google Docs and YouTube. This enables fast authorization checks at enormous scale while maintaining a flexible model that can be adapted to even the most complex use cases. If you're currently looking to build role-based access control or other enterprise features like single sign-on, SCIM, or user management, you should consider WorkOS. It's a drop-in replacement for Auth0 and supports up to one million monthly active users for free. Check it out at WorkOS.com to learn more. That's workos.com.

(00:03:52):
This episode is brought to you by Vanta. When it comes to ensuring your company has top-notch security practices, things get complicated fast. Now you can assess risk, secure the trust of your customers, and automate compliance for SOC 2, ISO 27001, HIPAA, and more with a single platform, Vanta. Vanta's market-leading trust management platform helps you continuously monitor compliance alongside reporting and tracking risk. Plus, you can save hours by completing security questionnaires with Vanta AI. Join thousands of global companies that use Vanta to automate evidence collection, unify risk management, and streamline security reviews. Get $1,000 off Vanta when you go to vanta.com/lenny. That's V-A-N-T-A.com/lenny. Guillermo, thank you so much for being here. Welcome to the podcast.

Guillermo Rauch (00:04:50):
Thanks for having me. Longtime listener, first time, I guess participating in the podcast, and love being here.

Lenny Rachitsky (00:04:57):
Oh, I appreciate that. Okay, I know you saw this, I did this survey recently where I asked my readers, "What tools do you use most in your day-to-day work as a product builder, as or product manager?" And in the category of engineering tools, v0 came in right below Cursor and GitHub for people's most used AI building tools. So clearly people love what you're doing.

Guillermo Rauch (00:05:18):
Yeah, we're very happy to see that. And for us, we're at the very beginning of the journey in some ways, because v0 is a relatively new tool, but for Vercel, our company has been around for a while. The way that I explain to people is, "Anytime you're using the internet, if there's a website or web application that's really fast, innovative, hopefully it's running on our platform." We're out there. We are running a lot of websites at scale. If you watched the Super Bowl recently, three different companies were promoting digital products that were built and delivered on Vercel. So not only can you deploy your ideas and build them on Vercel, they can scale to huge volumes of traffic and huge audiences. 

(00:05:58):
So a lot of people know us because of a framework called Next.js. It's an open source framework based on the React technology, open source by Meta, and it powers some of the most innovative products on the internet. So when you use Claude, or Grok, or Midjourney, you're using Next.js. You're using Vercel's technologies. So with v0, what we're trying to do is, and it's funny, because you put us rightfully, I think, in the building or development category in that survey, but what we're trying to do with v0 is help more people participate in building software, increase the total addressable market of people that are actually shipping things, shipping real products. And at the same time, just like you would with ChatGPT, we want v0 to be just extremely, extremely easy, and the outputs that it generates, make them as refined and realistic as possible. The things that you created with v0 hopefully live up to that standard set by some of the best and largest websites on the internet.

Lenny Rachitsky (00:07:04):
I was going to ask you how v0 came out of Vercel, and my theory was it was like you guys are sitting around being like, "How do we get more people building websites?" And it's like, "Okay, let's just help them do it really easily." It's like TAM expansion for Vercel. Is that?

Guillermo Rauch (00:07:17):
Yeah.

Lenny Rachitsky (00:07:17):
Or it-

Guillermo Rauch (00:07:19):
In some ways what I've been doing for not only 10 years that I've been almost working on Vercel, but maybe my entire life because my strength as a developer is kind of meta. It's been to create developer tools. So I've created a bunch of open source frameworks that are really popular. So Next.js is one, but before that in a previous life, I created another tool called Socket.IO, which is a real-time communication mechanism that powers, for example, every time you use Notion, I think you interviewed Ivan, when Notion is to broadcast messages in real time to other collaborators, they use a real-time engine that I built for Socket.IO. 

(00:07:59):
So the reason that startups and companies have used my products in the past is because I took something that was very difficult to do, but very compelling. It was with real-time in the past. It's building cutting-edge applications on the web with Next.js. And I try to make it as easy as possible. But you still needed to know development skills. For us and the opportunity was if there is maybe five million React developers, which is the the library engine that we use, and there's maybe 20 million JavaScript developers, how many product builders are people with aspirations of building products exist? My back of the napkin, minimum calculation is a hundred million. 

(00:08:45):
And I'll tell you, it's funny where I get that number from. Slack has about a hundred million monthly active users. And what you do on Slack is you go in IT and you talk to people. A lot of those people are building digital products. And they talk to one another about what they would want to see in the world. They talk to customers through shared channels. I love that feature. We talk to a lot of the Vercel customers and they tell us, like, "I want to build this, I want to see that. I want this feature, I want that thing." So the opportunity with v0 was, it's not that you're going to stop talking to other people, but what if you could yap into the computer and see something happen, build a prototype, build your first version of a product, build a demo, build a full stack product, build it and ship it?

(00:09:30):
And so the inspiration for it was very natural to the mission of Vercel. But concretely, the genesis, the story was when ChatGPT came out, we noticed that it was very good at writing the code that our tools used. So ChatGPT, right out of the bat, was good at JavaScript, was good at Tailwind, which is a CSS styling technology, was good at Next.js, and again, the power of open source. Our tools were already in the training data of the internet. And so that long-term bet and vision in open source really paid off. So because the models were so good at writing this kind of code, the idea for v0 came naturally from, "What if we could build a ChatGPT for building web products?"

Lenny Rachitsky (00:10:14):
Speaking of that, I didn't actually know. So I had Bolt's CEO on the podcast and he talked about how Claude kind of unlocked what they're doing and do you guys sit on ChatGPT and OpenAI's stuff?

Guillermo Rauch (00:10:25):
We started out on OpenAI. And we've always used a combination of models. It's funny, right now on Twitter there's thread with a million views of people trying to reverse engineer the prompt and the models they used. 

Lenny Rachitsky (00:10:25):
I saw that on Reddit. Yeah.

Guillermo Rauch (00:10:36):
And they're all finding that there is all these kinds of different models that are specialists in different tasks. And there's a pipeline of models where a model could hand off work to another model. And so OpenAI, Gemini, Claude, but we predate Anthropic because I'll give credit to ChatGPT that the utility of it was so general purpose, but from the very first release, it was very good. In fact, by the way, if I'm not mistaken, the first prototype of v0 might have even predated ChatGPT, or at the very least I think we were running on GPT 3.5. So we've always had this vision of unlocking more power for the web through LLMs, and there's a lot of very interesting technical details of why, by the way, LMs happen to be so good at the task of web design and web development that we could get into. But it was the perfect timing for us.

Lenny Rachitsky (00:11:34):
I want to come back to that. That's actually a really good question. But let me ask a couple other questions here. In terms of v0, what's the scale at this point? We hear all these numbers about all the folks in the space. What can you share about what's happening with v0?

Guillermo Rauch (00:11:45):
I can share that it's growing exponentially, and that over 1.3 million users have interacted with v0 so far. We had our largest day ever yesterday and today, again, we're one of the largest customers of most of cloud providers at this point. We're hitting the limits of every GPU, LLM infrastructure out there in the planet. And the most exciting thing for me is what I'm seeing people build with v0. So we launched a feature about a month ago, maybe even less than a month ago, called v0 Community. It already has 20,000 submissions. I am sure people in your audience have used Figma, one of the things that I love about Figma is Figma files, that I can go and grab a starting point for something. It could be a logo, could be a menu, and you can start with something that someone has already contributed, like that spirit of open source.

(00:12:44):
And so in less than a month, I think we've done over 20,000 community submissions. So we've learned so much about building AI products with this and we continue to open source and share our best practices. But one of the things that I've definitely learned is prompting it seems like the easiest interface in the world because it's just an input and you put text in it. But there's a little bit of a writer's block sometimes. So one of my favorite things that I've seen, and I'm even looking at the home page right now, and you can see a random assortment of community submissions. And they have 1,200 forks, and 1,500 forks, and 6,000 forks, and this is every time people saying like, "Oh, instead of starting from scratch, I'll start from this application that someone else has built and I'm going to prompt it to modify it and make it my own."

Lenny Rachitsky (00:13:34):
So the community submissions are people building apps on v0 and sharing what they built?

Guillermo Rauch (00:13:39):
Correct. 

Lenny Rachitsky (00:13:39):
You can look at the code and fork it?

Guillermo Rauch (00:13:40):
It is becoming like a compounding investment. People share something, someone else grabs it, makes it better. Maybe you used it at that point. In many ways, I see this as the next evolution of GitHub, whereas GitHub, it was a marvel for software development because I don't know if you remember this, but the initial, little tagline underneath the GitHub logo was social coding. And it had this democratization effect of building software. But you still needed to know how to code. And so what we're after is social product building in many ways, everybody should be able to cook and share what they're building.

Lenny Rachitsky (00:14:25):
I hadn't thought of it this way, but I love that it connects so much to your open source roots, where people are building on v0, and then sharing what they're building and then people can build off those things. It's kind like an open source AI building experience.

Guillermo Rauch (00:14:36):
It's fascinating, right? In many ways, if you think about the Git commit, the Git commit is super interesting. If you watch how an engineer works, they look at a problem, they spend a lot of time in their code editor, and at the end they say, "I think I got it. I think I've fixed it." And then they produce a Git commit. They summarize their intent and what they try to do after they've done the work. v0 inverts that. The Git commit is you go into the chat and say, "Please change the color of this button. And when I click it, save this form to a database." And so you're starting with the intent and the output is the code. 

(00:15:26):
And as a side effect, we can also produce a Git commit for you. That feature's not online yet, but it's coming in the next couple of days. Spoiler alert for the group. And so I like this idea of we can create this super set of all software building with this platform. And that is true to my initial intention with Vercel. Our mission is to enable the world to build and ship the best products. And so enabling that for the largest possible group of people is very exciting to me.

Lenny Rachitsky (00:15:55):
So let's go to this question of just the elephant in the room for a lot of people seeing these things happening, product builders that have been doing things a certain way for a long time with apps like this coming around, whether you could just type a thing in, and build it for you, and it's beautiful. How do you think things are going to change for product managers, for product teams? Where do you think the biggest change is going to happen? How do you think product will be built in the next few years?

Guillermo Rauch (00:16:19):
The most profound one that I alluded to is that conversations between product builders and their customers will be mediated by these zero links, these artifacts. I think when Claude came up with the name artifacts, I found it phenomenal, because we're all in this world, especially in this group of people, we're here to build awesome things and share them with the world. Steve Jobs said this awesome speech about, "It's like our form of giving back to the world is to try and do the best possible job we can and share it with the world." And so the idea that when we talk, we would not have the power to make those ideas a reality, it seems like an L to me. I would love to see people constantly live in the product, be in the design, spend time tuning and trying out new ideas. And that's what the ideal work of the future should look like, and less about again, that abstraction, that being removed from the product or even sometimes I can feel powerless to not be able to change something. 

(00:17:47):
This happens a lot when departments collaborate within an organization. Marketing wants design to do something, marketing wants engineering, engineering needs a design. It cuts always. One of the things that people got excited about that we published on the Vercel blog was about design engineering, because a lot of the people that we were noticing were being very successful at Vercel were people that had both the design and engineering skills. And that was actually another huge motivator and inspiration for v0, because we realized that people could be more full stack. We shouldn't put limits on ourselves, and what we can build, and what we can ship, and what we can dream about making possible on these web surfaces. 

(00:18:36):
And so you could imagine removing all those limitations, a designer that can ship a fully-baked product, a product manager that can prototype and shift to production. A lot of people that use v0 are back-end engineers that never had the ability to, they could ship an API, they could build a great low-level infrastructure system, but to actually bring their end-to-end vision to life, v0's completing that for them.

Lenny Rachitsky (00:19:07):
Let me follow the thread on engineers. A lot of people are wondering, "Do we need engineers in the future? What happens to engineers? Should I learn how to code?" Your long-time engineer thoughts for folks that are trying to decide the career for themselves?

Guillermo Rauch (00:19:21):
Yeah, I think knowing how things work is the most important skill in the world. I foresee a lot of people becoming incredibly impactful in building and shipping amazing products, and building gigantic companies, and everything you could imagine, where a single person can do the job of a hundred different people in a hundred different specializations. Take the example of one skill set that's really important to build a front-end product is you need to know how to use CSS or Tailwind to style it. And once upon a time, I would hire people that were truly specialists in this task, the task of there's a Figma design or there is some kind of sketch, and translating that into reality because they knew really well how to manipulate layouts, layout code, box model code, we call it, and borders, paddings, margins, flex box, all these technologies for styling. 

(00:20:32):
And notice, I actually use the word translation very intentionally, because the origin of the LLM or the transform architecture at least, goes as far back as the architecture for systems like Google Translate. They were generative LLM techniques, basically. That's how they cross that chasm of, remember when translating tools were horrible and then one day the problem was just solved? And I look at a lot of the programming jobs to be done that used to be specializations, that I think are going away, in a way, or the tasks to be done, they're translation tasks. We were translating from a screenshot, or intent, or a design into a React, and Tailwind, and CSS implementation. 

(00:21:32):
And right now, v0 is incredibly good at doing that. It's so good that every time we put a new generation of the model out, I run this test of converting my own website and try to generate it with v0. Last time I did it, it had taken me like 10 prompts to replicate it. Keep in mind I'm an expert front-end engineer that's been in the arena since I'm like 10 years old and I'm 35 now. And so I do that test because it's almost like a test of self-imposed humility of, like, "I remember exactly how long it took me to build my website with Next.js, the framework that I created, and ship it." And so with the last model, it took me maybe 10, 15 prompts? With the most recent model, it took me two prompts. 

(00:22:22):
And so that translation from the design intent into working implementation, another anecdote that I like to share with people is the model, because v0 tries to embed all of the best practices of the web, the model output more accessible code than what I wrote. It follows the accessibility guidelines that the web standards consortiums put out better than I did, because it just knows everything. And so those tasks where you can almost model it to a translation task, definitely going away. But knowing how things work under the hood, notice all the ... I'm using specific tokens in this conversation. I'm saying, "CSS," I'm saying, "Layout." I'm naming styles. Knowing those tokens is going to be very important for you because you're going to be able to influence the model and make it follow your intention a lot better. 

(00:23:22):
And so the TLDR would be knowing how things work, the symbolic systems, and that will mean that you have to probably go into each subject with less depth. I have engineers at Vercel that know every single CSS property by heart. They know when they became available in a certain web browser, they've been tracking this specification. It's almost like you're an encyclopedia of knowledge of each CSS property. You probably won't need that in the future, and probably that's good, because you'll free up your mind for more ambitious things.

Lenny Rachitsky (00:23:59):
No, that's fascinating. So what I'm hearing is a skill that will continue to be valuable in the future, but I want to push on this a little bit, no matter how far AI gets, is understanding conceptually how software works, end-to-end-

Guillermo Rauch (00:24:14):
Yes. Absolutely.

Lenny Rachitsky (00:24:14):
... systems, databases, CSS is a thing. So I don't know if you have kids, whether you have kids or not, just say they were trying to decide, "What should I learn to be, to thrive in this future?" Well, how would you summarize it? How far? Should they get into software engineering? 

Guillermo Rauch (00:24:31):
Great question, because I have five kids, and I've already enrolled them in this school of G, myself, in the sense that I'm already guiding them towards the things I think are going to be very useful to them. So understanding how things work needs, I think the ability to understand the fundamental logic behind things, incredibly valuable. So I push them really hard on math. "If you don't know math really well, you're out of my house." Just kidding. But it's a fundamental skill that I want them to know. Eloquence. I joke sometimes. Have you heard a meme of word cells versus-

Lenny Rachitsky (00:25:13):
Yeah- [inaudible 00:25:13]

Guillermo Rauch (00:25:13):
... shape rotators?

Lenny Rachitsky (00:25:14):
Yeah.

Guillermo Rauch (00:25:14):
So a shape rotator is someone that only has a math brain. You could argue the kings and queens of Silicon Valley have been the shape rotators, because those have been the jobs that have historically commanded the most status, respect, net worth, whatever. And then there's the word cells, which is communicating, more of the liberal arts. There's also the funny and awesome slide of Apple saying that they're at the intersection of liberal arts and technology. I've always had immense amounts of respect for both sides of the brain, so to speak. But I think developing great eloquence, and knowing and memorizing those tokens that I talked about, knowing how to refer to things in that global mental map of symbolic systems will be highly valuable. And we have some tools to help people prompt better, but prompt enhancement and embellishment cannot replace thinking and cannot replace your own creativity that you want to infuse into the world.

(00:26:18):
So one of the things that v0 does is it tries and it succeeds, I think, at creating very nice designs out of the box. We try to infuse what we've learned about what do people think is typically good web design? We've influenced the model in that direction. But still we also don't want the whole internet to look the same way. So your ability to steer the model with your words into those references, into those inspirations, is going to be very important. 

(00:26:49):
I actually have an amazing anecdote. We hosted a design demo night at the Vercel HQ in San Francisco last night. And we were showing off how Vercel uses v0 to build v0 and to build Vercel. And one of our designers showed this amazing animation that he built, actually two amazing animations that he built. And in one of them it was this amazing triangle that had an animation that I didn't think was possible to make, in that it was all built with v0. And he used the word turbulence to describe the effect that he wanted.

(00:27:30):
So I just want to call out that to people because the difference between knowing that word and not knowing it is getting that style into that beautiful triangle that he created that was interactive, and it's probably going to end up in some landing page soon that you're going to visit on vercel.com. And so developing eloquence and your linguistic ability I think is going to be very important. So I love my kids to know that. And I think that idea of sharing things, and putting yourself out there, and broadcasting to the world, so another thing that I do is I take my kids to hackathons, which just went to an awesome hackathon at University of San Francisco, USF. It was called the BLOOM Hackathon. And I took two of my kids and I wanted them to watch how people presented their ideas and we had a lot of fun. We also ate waffles and grilled sandwiches, which is a bonus. 

(00:28:29):
So presenting and putting yourself out there. I mentioned in the beginning of the podcast when we were chatting, I've learned so much from you and your guests because you put out all these awesome little posts on X in these videos and these snippets of your interviews. And so the ability to present what you've built and put yourself out there, incredibly important skill in the future. Especially in a world where the marginal cost of producing software and new things are going down, you need to build an audience, you need to know how to talk to people, you need to build your own signature brand and style. And so maybe they're a little too young for that one, but I guess taking them into hackathons probably back, is influencing their neural networks or pre-training data for the future.

Lenny Rachitsky (00:29:19):
I love it. They're going to tell their friends, "My dad took me to a hackathon." "What's that?" So are you encouraging to learn to code? Because it's interesting you mentioned-

Guillermo Rauch (00:29:29):
Yes.

Lenny Rachitsky (00:29:29):
... math, eloquence, presenting, and then, okay, so also learn to code.

Guillermo Rauch (00:29:32):
Yeah, I think again, learning how to prompt, learning how to code. With v0, we show you the code when we build things. So if you can build that mapping of maybe not learning how to code necessarily as an abstraction, if you do have a knack for it, I'm a big believer also that my five kids have super diverse personalities and inclinations, and I don't want to be pushing for something that they wouldn't want to do or whatever. And so learning to code in the abstract might be good for some people, but it may not be the fun thing to do for other people. And so what I would recommend is try to understand how things work. So if you prompt v0 or any other tool and it generates some code, try to build an understanding of what that does at a high level. It's like actually maybe an extension even of eloquence.

(00:30:32):
One of the bets that I made early on with Vercel that really paid off is Vercel, maybe as a metaphor is like AWS in easy mode for a lot of people. We have a very large user base of people that would have otherwise not have been able to configure all of the ins and outs of the cloud, but do want the scale, flexibility, speed, et cetera. They want to create very high quality products and services. So I like to give the Super Bowl example because one of our customers, Ramp, had a 43X increase in traffic when their ad went live. The engineer that worked on that only needed to learn Next.js. Then they pushed their code to Vercel and now they can reach an audience of a hundred million people without a blip, a hundred percent uptime.

(00:31:24):
That superpower comes from, we made it as easy as possible to get started, and the language that we choose is actually very relevant in this story. JavaScript, in my mind, has always been almost like the English of programming languages. It's a language that, if you learn it, you reach billions of devices. So it's not a coincidence that when you ask ChatGPT, or Anthropic, or Gemini to build you web app, it uses these tools. It uses JavaScript, it uses React. It's become the lingua franca of building products on the web. So I would say to my kids, "Look, if you do want to go deeper into programming, start learning there." You can reach huge numbers of people. If you have a passion, I would say there's going to be a fundamental engineering skill that's going to be useful for decades or centuries to come, which is creating foundational infrastructure.

(00:32:26):
Think about LLMs in terms of, they're like Oracles that can go and write software for you, but there's a limit to how much software they can write. There's context windows, there is time and computational constraints. So it's very hard for an agent today to go and say, "I'm going to write a cloud from scratch. I'm going to write all the foundational services. I'm going to write the framework from scratch. I'm going to write the compiler." No, the LM is orchestrating those tools and infrastructure. It's not writing the compiler from scratch. Otherwise, you get into the Newton thing, in order to create an Apple, you have to create the entire underlying universe. No, the elements are interoperating with the universe as it exists. And so the engineers that learn foundational infrastructure are probably going to be extremely empowered still, for years to come.

Lenny Rachitsky (00:33:23):
There's a world where you could argue ChatGPT will build the next version of ChatGPT. What I'm hearing from you is that's a long ways away, if ever.

Guillermo Rauch (00:33:30):
Absolutely. This is why the common, the running joke is that all of these companies have, you go to their careers page. It's like-

Lenny Rachitsky (00:33:40):
Engineers.

Guillermo Rauch (00:33:41):
... "Engineer, engineer, engineer." The counterpoint of that is that at Vercel had, we have 150 engineers that can write code and 600 total headcount. Now we have 600 engineers. Some of the best things that I've seen created with v0 have not come from our engineering team. They've come from the marketing team, they've come from the sales team, they've come from the product management team. The product management team is fascinating, because now they're actually building the product. So last night I saw how we've specced out in v0, think of it as like a live PRD, we've specced out how the new functionality for deploying a v0 to Vercel is going to work. 

(00:34:26):
The amount of detail that was contained in that v0, I mean, we're all just saying, "Well, just ship it. There's nothing else to discuss." It was animated, it was interactive. We were demonstrating the error state, the success state, the slow stream state. So it really empowers product builders not only with technical skills, I think that does a disservice to the tool. It empowers them to explore and augment their thinking with a lot of things that perhaps they wouldn't have considered otherwise, a lot of states of the product they wouldn't have considered otherwise.

Lenny Rachitsky (00:35:05):
The name v0 implies the product is for prototypes for the first attempt at stuff. And that's definitely where all these tools are finding product market fit prototypes, PMs showing a thing working versus just design. Do you expect v0 and other tools to get to a place where you can build salesforce.com and scale it to billions of dollars? Do you-

Guillermo Rauch (00:35:05):
Absolutely.

Lenny Rachitsky (00:35:27):
You do? Okay.

Guillermo Rauch (00:35:27):
We already have an enterprise customer of v0 that only works with v0. All of their products, all of their features, all of their client communications are v0 native. Two days ago, I just heard anecdotally on X, someone tells me, "My brother just sold his first website to a client completely built in v0." Yesterday at an investor conference, an investor walks up to me and says, "Two of my friends just got engaged on v0." I was like, "Okay, v0 is a dating app now." So the engagement website, the proposal, the wedding, it's all v0 native. 

(00:36:07):
So because we've integrated v0, the Vercel infrastructure, we can do that whole story that I just told you of like, "I have a website to build and I can get it in front of a hundred million people." We can enable that for everybody now. And so the end-to-end full stack, v0 native, and built on this awesome fluid serverless infrastructure that scales to billions of people, all just from prompts, or screenshots, or just copying and pasting your PRDs into the tool.

Lenny Rachitsky (00:36:42):
Let's help people be successful with v0. And then let's also do a demo. But before we get there, let me ask you this. Imagine you could magically sit next to someone who's about to use v0 for the first time and whisper a tip in their ear to be successful with v0. What would a couple tips be?

Guillermo Rauch (00:36:59):
Number one is you can be as ambitious as you want in terms of what you ask the tool. If you can steer the tool towards some kind of inspiration that you have, you're always going to get better results. If you don't have ideas on what to build or what to prompt, I would recommend using the v0 community so that you can find something to fork to get started. I would say in some ways, if you have technical skills, this one is interesting, have some suspension of disbelief. It humbled me, I was saying about accessibility. So be open-minded about whether the tool actually knows some things that you might not know, and so focus more on the product description, focus more on what do you want the end user to experience? What do you want the product to do? And try to be open-minded about how well the tool can implement it. Those would be my main wants. 

(00:38:04):
You also have to have a sense of iteration, I guess. Think of it this way, if you were working with a design firm or an agency that you've hired, you will go back and forth and say, "Try something else." If you were coaching an engineer that's getting stuck in something, you would say, "Try something else." It's amazing how many times I've gotten unstuck in v0 by just saying, "Just try something else."

Lenny Rachitsky (00:38:35):
Just saying that as the prompt, not even giving direct-

Guillermo Rauch (00:38:37):
Just saying that. I mean, the chat is like-

Lenny Rachitsky (00:38:37):
Wow.

Guillermo Rauch (00:38:43):
"v0, we need to have ... " It's like, "Yeah." Like you have a one-on-one performance review with a tool. "Hey, way to talk, try something else. What you're doing so far is not working. And it's amazing." One fitness function that I'm keeping in my head is I really want to find the thing that it cannot build with v0. So as part of the v0 community, I have my own profile. We'll share the link with people. You can see six or seven things that I've built that I consider to be pretty impressive. So for example, I was flying from Tokyo to San Francisco. The internet was horrible. What I like to do during flights is I like to monitor our own flight while I'm on the flight. So I open Flightradar or whatever, and I was extremely bored as well.

(00:39:32):
And I noticed that Flightradar, I don't know which one it was, Flightradar, there's like four or five of them. They were very bloated. They had ads. They were not what I wanted the flight radar to look like. So I built my own during the flight with the worst internet connection that you could imagine in the world, integrated into a flight data API called Edge Aviation. So this is what I told v0, "You're going to build the best flight radar on the planet." I wasn't prescriptive at how, so it used a tool called Mapbox and a JavaScript library called Leaflet. I didn't tell him that, or her, I don't know, v0, what it is. And subsequently, once we cooked on the design, which looks, I would say beautiful, I then got more ambitious and I said, "All right, let's make it real now." 

(00:40:30):
And by the way, that's actually how I would work. So it's how I like to work. I like to work experience first, and that's also how Vercel was built. "Let's start with the front end. Let's start with the planes on the screen." And by the way, there's a lot of subtleties, here. For example, there's so many flights going on at any given time that there's just too many. So I had to work with v0 on improving performance. And once again, I wasn't prescriptive. I just said, "We have a lot of flights, chief. Let's- " 

Lenny Rachitsky (00:41:02):
Did you say, "Chief?"

Guillermo Rauch (00:41:03):
Yeah, I do say that a lot. And this is, I think when I shared it on X, it blew a lot of engineers' minds, because it created a canvas-based, canvas is the sort of underlying rendering surface that very sophisticated products use like Figma. And it created this awesome overlay on top of the map that can render tens of thousands of flights at any given time. And then I told it, "Let's make it a full stack application. Okay, plug into the flights' API." So that's an example of we cooked and there was no limit. And so I'm always in the lookout. The service that I'm providing to the v0 community is I'm part of the team that is really trying to break this and say, "Can it not build something?" And even when it does build it, we're very obsessed with quality and performance. It has to be real. That's our commitment to our users.

Lenny Rachitsky (00:42:00):
And how much did this cost, how much time does this take to make something like this?

Guillermo Rauch (00:42:06):
So the flight radar example or v0?

Lenny Rachitsky (00:42:08):
Yeah, the flight radar example specifically just like very-

Guillermo Rauch (00:42:11):
I mean, that one probably took less than two hours-

Lenny Rachitsky (00:42:11):
Less than two hours?

Guillermo Rauch (00:42:13):
... with the worst internet. 

Lenny Rachitsky (00:42:14):
Yeah, what-

Guillermo Rauch (00:42:15):
Sorry, Japan Airlines, I love you, but you give me a hard time. 

Lenny Rachitsky (00:42:18):
And what did that cost? Like 10 bucks? What would you estimate? 

Guillermo Rauch (00:42:24):
I mean, I pay for the $20 v0 subscription.

Lenny Rachitsky (00:42:25):
20 bucks, okay, for a month. So it's like a month, but you used it for two hours, 20 bucks. 

Guillermo Rauch (00:42:31):
Yeah.

Lenny Rachitsky (00:42:31):
If you had engineers building this, how much do you think that would cost? How long do you think that would take?

Guillermo Rauch (00:42:36):
I mean, weeks, easily. Easily.

Lenny Rachitsky (00:42:40):
And that's like tens of thousands of dollars.

Guillermo Rauch (00:42:42):
Maybe the most cracked engineer at Vercel could knock it out in ... without using any AI, could knock it out in a couple days. But then what about the design? What about me? Because I'm the bottleneck, not the engineer. And this is what's amazing about this collaboration because I'm providing the product guidance. I'm saying, "Draw a dashed line between the ... " And by the way, v0 just blew my mind so hard. I said, "Draw a dashed line between the two destination airports." And v0 said, "Well, I have to account for the spherical, or what is it, it's a pseudosphere, for the curvature of the earth." It's like, "Okay, v0, super genius, whatever." And so that's what I mentioned about how you can go back and forth. It's like a product copilot, it's like an all-knowing being. 

(00:43:40):
One of our users yesterday submitted feedback to the tool and it was positive feedback. They were very happy, what they were saying, "v0 is a super genius five-year old PhD with ADHD." So you still have to, I'm not going to oversell this like, "It knows everything about everything. It gives everything perfect," of course. But it has these sparks of brilliance. Really, truly, I think, I've been a big believer that AGI undersells what we are collectively building because we already have, all of this sparks of super intelligence. I don't believe that v0 is an AGI if it knows everything about how to draw a dashed line according to the curvature of the earth and this high-performance map of airplanes. That's just superhuman. And yeah, it's a joy to use.

MUSIC (00:44:39):
(instrumental music)

Lenny Rachitsky (00:44:40):
Today's episode is brought to you by LinkedIn ads. One of the hardest and also most important parts of B2B marketing is reaching the right people. I'm constantly getting ads for products that I will never buy. And I almost feel sorry for the money that these companies are spending, pitching me on their spend management software or some kind of cybersecurity solution that my one-man business just does not need. When you're ready to reach the right professionals use LinkedIn ads. LinkedIn has grown to a network of over one billion professionals, including 130 million decision makers. And that's where it stands apart from other ad platforms. You can target your ad buyers by job title, industry, company, role, seniority, skills, even company revenue, all the professionals that you need to reach in one place. Stop wasting budget on the wrong audience and start targeting the right professionals only on LinkedIn ads. LinkedIn will even give you $100 credit on your next campaign so that you can try it for yourself. Just go to linkedin.com/podlenny, that's linkedin.com/podlenny. Terms and conditions apply only on LinkedIn ads.  

(00:45:48):
As you talk, it's interesting, the way I'm thinking about this now, there's almost like three core skills in building apps with AI. There's figuring out what to build, there's making it look good, like design, and then there's getting it unstuck. 

Guillermo Rauch (00:46:02):
Yeah,

Lenny Rachitsky (00:46:03):
And it's interesting how these are going to move.

Guillermo Rauch (00:46:05):
And coaching.

Lenny Rachitsky (00:46:07):
Coaching it. Yeah. Or just like, "Oh, here's the database error. I don't know. It's not figuring it out."

Guillermo Rauch (00:46:12):
Yeah.

Lenny Rachitsky (00:46:14):
I guess does that resonate? I've never thought about [inaudible 00:46:16] before.

Guillermo Rauch (00:46:15):
Oh, absolutely. In fact, I'll tell you a little bit of a story of something. So even going way back in time, Next.js builds on React. React was this UI component library that Facebook created, actually with very similar goals. They had so many cracked engineers, and they had to help them collaborate on an enormous product surface. So they invented or at least pioneered, I would say the concept of this component as a unit of reusability, as a building block, as a Lego brick of how you build software. It's no coincidence that LLMs love to work with React components, by the way. And one of the things that always has stood out to me about that model is it basically enables people to scale in how they work together. And one of the key design principles that they embedded into this thing, is they called it escape hatch.

(00:47:17):
The API, when when React doesn't perfectly model your problem with its component system, they give you escape hatch. They say, "Okay, engineer. You are on your own now. There's no guardrails." And in fact, one of these escape hatches is called dangerously set inner HTML. They want the developer to know uncharted territory. But they did give people the API. That is a profound systems design engineering principle. And throughout my life, I've always thought about escape hatches. 

(00:47:54):
One amazing escape hatch that v0 has is that you're looking at the code that we're generating with Next.js. You can edit it, you can even have other experts look at it. One thing that one of our demos last night came from this awesome company, Lumalabs. They're creating one of the most amazing video models in the world, and they use v0 and Vercel extensively to build their application, their websites, et cetera. And the design engineer was talking about how he was on a v0 that had 120 or so iterations. So he was knee-deep into the latent space. He was in the matrix. And at one point he got stuck. But you know what he did? He copied and pasted the code that we generated and he gave it to ChatGPT o1 and ChatGPT o1 thought about the solution.

(00:48:51):
Honestly, I'd never even thought about this myself. I was so blown away. And it does speak to, I love that your third point of, "You need to learn a skill of how to get unstuck." It's like a profound life lesson. It's just more a generic life advice you need to get. Facebook actually had a principle, "Don't get blocked. Seek to get unblocked, seek help from other people." What's fascinating is that you can seek help from other AIs to get unstuck. And those escape hatches of actually understanding and seeing the code underneath, and even being able to say, "Okay, now let's use Git. Let's turn this into more of a hybrid project, not just prompts, but also traditional software engineering." The fact that that door is open to you is extremely valuable.

Lenny Rachitsky (00:49:44):
Let's actually make the super concrete and show people what this actually looks like in v0. So pull up, we'll share screen, and then we'll do a little live demo. We'll keep it brief. I find people are like, "Okay, I get it." But we'll make it fun and brief at the same time. There it is. I see it.

Guillermo Rauch (00:49:59):
Beautiful. Okay.

Lenny Rachitsky (00:50:00):
How can I help you ship?

Guillermo Rauch (00:50:02):
Yeah, of course. We're all about shipping. Okay, so as I mentioned, you write in English, you yap into the tool. I'll say for a demo, let's create a contact sales form in the style of ... By the way, I had a typo. I don't care. Let's get it. It's Elf Supreme, the clothing company for an online store. Now, I mentioned that sometimes people get blocked, there is a writer paralysis at this step. So we added enhanced prompt. So now you're tapping into the latent space of the model, which has a random component to it. 

(00:50:48):
And by the way, this is still not a substitute. It doesn't contradict what I said earlier, knowing the meaningful tokens, knowing what the right style is, and what it's called, and whatever is still highly valuable. So the first thing you're going to notice is that as the model thinks, you can introspect its thinking. So we added this recently. It's been mostly inspired actually by the Deepseek revolution. I would say. 

(00:51:17):
So the fact that when you tell it, "Develop a contact sales form," what is it going to do? We talked about escape hatches. Okay, it's going to use shadcn/ui, it's going to use Tailwind CSS, it's going to use React. And this is your opportunity that if v0 is not doing exactly what you wanted, this is your opportunity to actually go and correct, or influence, or give feedback and so on. So you're going to notice it spits out a bunch of files, and it gives me the thing that I wanted. I'm going to zoom out a little bit, here. A couple of things that stand out here that again, as an experienced engineer, I can point out. The underlying component system that it uses is the same component system that the best tools on the planet are built with. This is called shadcn. If you go to grok.com today, they're using shadcn to build their UI. They're using Next.js. You're getting that caliber of code. 

(00:52:15):
The other thing that it did is people on social media talk about this a lot. When you use a global shared component system with the world, you don't want everything to look the same. So the fact that he was able to apply the style and he kind of knew what supreme looked like was kind of cool. But now I'm going to say, "Actually, because I am building a financial institution, make it more serious, make it in the style of let's say Charles Schwab. Change typefaces.' So this is the iteration process of like, "I'm going to go and give feedback to the model. I'm going to make it try different things." So once that initial generation was already created, now the model is actually acting more as an editor. It's going and making tweaks to what's already been built.

(00:53:08):
And this actually scales to very large projects. You could have started with something much bigger. So in the meantime, I'm going to show you what Lumalabs created with v0, which is absolutely phenomenal. I learned about this last night. It already has 2,000 forks. I was telling you about the power of our community. So by the way, you can just click community here on the v0 sidebar. I'm going to fork it, because they generously shared it with the world. Notice all the incredible animations here? By the way, they shipped this to hire and attract talent to their company. I recommend them, by the way, you should, if you want to be a brand designer, take them into consideration. Notice that it's an interactive, everything is AI generated, they used their own AI image generation tool to create these beautiful frames. These are all AI generated as well.

Lenny Rachitsky (00:53:59):
Wow.

Guillermo Rauch (00:54:00):
And it's interactive. So there is the autoplaying functionality. This is actually a complex layout in animation system that they built entirely in v0. I was telling you that at one point they even got some advice from O-Wan, so shout out to OpenAI. I'm going to say, "Make it sepia style colors." So this is an example of like, "Okay, I forked something. I already have a starting point." My bank grade contact form is ready. In the meantime, another fun thing to do is you can start with a screenshot. So I'll use another Next.js user as an example, which is fortune.com. Shout out to them. They built a slick website. 

(00:54:48):
But let's say that I'm actually wanting to break into the news business, so I'm just going to paste a screenshot. I could have also attached the Figma file. And I'm going to have, v0 already knows, v0 can answer questions as well about the engineering design product world. So I can ask v0, "What is a newsletter? Explain with a diagram. Use Lenny as an example." So v0 is also a knowledge seeking tool. But we do strongly like, "Steer the tool to create things." So if I paste a screenshot, as you can see, it's cooking on creating a hopefully awesome news website. I specifically asked, because I think it's funny, to explain a newsletter with a diagram, so v0 can create again, explanations, content, knowledge. The creator is Lenny, you were a former Airbnb product lead. I guess I should-

Lenny Rachitsky (00:55:55):
It's all- [inaudible 00:55:55]

Guillermo Rauch (00:55:54):
... have used some examples from Airbnb, by the way. But let's look at here-

Lenny Rachitsky (00:55:54):
It's all good.

Guillermo Rauch (00:55:59):
... what it created with Fortune.

Lenny Rachitsky (00:56:01):
Wow.

Guillermo Rauch (00:56:03):
So notice that, I'm just noticing now the cyber should have been on the center. I'm going to zoom out a little bit. Let's use the refinement tool to center this. I call this, by the way, one of the hardest problems in computer science is actually centering things.

Lenny Rachitsky (00:56:26):
With CSS.

Guillermo Rauch (00:56:28):
That's right, centering a div. And in fact, look at it. It was a div. So notice that I did a precise inline prompt? And the difference between v0 and a lot of other tools is that yes, you do have the code and code is very important, but I call it code last rather than code first. You're living in the product. So center that. Another website that I love also built with Next.js is Semaphore. So I really like their sepia style. So I'm going to say, "Apply this style instead, including- " 

Lenny Rachitsky (00:57:09):
So you're sharing a screen. So you used a screenshot to design, to build a site, and now you're using a different screenshot to tell it, "Make it look like this."

Guillermo Rauch (00:57:16):
Yes. 

Lenny Rachitsky (00:57:17):
Very cool.

Guillermo Rauch (00:57:21):
And so the idea is that v0 can Grok different aspects of what it needs to build. It can be functional aspects, it can be layout aspects. And one of the things that's also very important to know is we influence the model. So a lot of the things that you would have had to prompt you might get for free. One that's important to call out is responsiveness. So as an example, if I notice that if I do this, it's going to make it work quite well on mobile, it's going to give me that hamburger menu. I can now tell it like, "Apply that style to everything."

(00:58:00):
In the meantime, I'll show you, this is actually to me very, very impressive. And I don't know why today I'm so fixated on the theme of sepia. But notice that not only did it change the background, I hope people can notice this. It applied it to the checkboxes and it applied a CSS. I'm assuming this is a CSS filter. Yeah, it applied a CSS filter. Just for the sake of it, because I'm a nerd, I'm going to look at it. But yes, it applied a CSS filter. Confession time, I actually didn't know that there was a sepia function in the filter property of CSS. There were many ways to accomplish this. You could have also written the images or the videos to a canvas, and apply all kinds of algorithms, and whatever. 

Lenny Rachitsky (00:58:48):
I like that it did more elegantly than you would have. 

Guillermo Rauch (00:58:51):
Yeah, exactly. So that's why you can't be too opinionated with the tool. So another cool thing is I do like showing screenshots, but I do want to remind people that the idea is not to clone other people's websites, necessarily. Right? It's-

Lenny Rachitsky (00:59:09):
It's just a cool demo. It's a simple way to show off what it can do.

Guillermo Rauch (00:59:11):
Exactly. 

Lenny Rachitsky (00:59:12):
Yeah.

Guillermo Rauch (00:59:12):
Take screenshots of your own things. Take screenshots of your art boards, take screenshots of things that people post in Slack, and also don't hesitate add functionality.

Lenny Rachitsky (00:59:22):
Incredible. Thank you for doing the demo. I'm just trying to imagine having an engineer I'm working with, asking them to do these things, and not only just how annoying that would be, like, "Make it sepia." 

Guillermo Rauch (00:59:23):
Yeah.

Lenny Rachitsky (00:59:32):
But just how much time it would take from, "Okay, do this thing, copy fortune.com." It'd be like days, weeks. Here, it's just-

Guillermo Rauch (00:59:32):
Months.

Lenny Rachitsky (00:59:39):
... check it out here. Months.

Guillermo Rauch (00:59:40):
If ever.

Lenny Rachitsky (00:59:41):
Yeah.

Guillermo Rauch (00:59:41):
Maybe it never ships. 

Lenny Rachitsky (00:59:44):
That's right. Well, something that I noticed that I loved at the beginning when you were doing the prompting and that prompt improvement feature is it basically is best practices to make it look good and look better. Which I think is one of the more interesting, I don't know, levers to working with AI is it just has best practices to help you build things that are beautiful and also feels like there's this opportunity of just helping you figure out if what you're building is at all a good idea. "What is the problem you're trying to solve?" It feels like there's a PM1 pager step that should exist. Like, "How do you know this is a problem? What have users told you? How many people have told you this?" Things like that.

Guillermo Rauch (01:00:24):
Yeah. There's something to be said about the fact that over time we're more and more peeking into the mind of the AI. That in itself is becoming a killer feature. So the Deepseek stream, the thinking tokens moment was a very big moment for our industry, I think. Because OpenAI did have the technology, but they decided that for competitive reasons, which, it's a reasonable think to think, no pun intended, they were going to withhold it. And also it wasn't clear that there was going to be product end user and product utility. But when Deepseek hit, it was very obvious that people really liked the idea of understanding how the AI thinks and influencing where it should go. We've gotten actually amazing feedback and bug reports where people actually specifically point out, "Look, this is where the AI went wrong. Please fix it." So the more people we get on this product, the more thumbs up, thumbs down, the more user feedback we get.

(01:01:30):
And by the way, I'll tell you for people out there building products, my number one guidance or piece of advice I would give to any startup founder was, "Create a lot of opportunities for people to give you feedback inside the product." I drew inspiration from Stripe. And this was amazing for the early days of Vercel, there was a feedback button with a very slick inline form, with four emojis that would allow you to decide how you were feeling about the feature, the product at that very moment. And that would go straight into Slack. And we were building day in and day out, just streaming users' thoughts right into our consciousness. And maybe we would get, I don't know, tens, hundreds a day, especially the early days, maybe a couple a day and whatever. When you're building AI products, it's a constant stream of user feedback. So for people that are thinking about not building AI products, it's going to be hard to compete with something that has such a tight feedback loop with users. 

(01:02:40):
The whole idea is to capture users' feedback so the next iteration of the model, the prompt, the fine-tuning, the examples, the rag is better. And one of the things that Vercel has done as a result of this insight is we've open-sourced a lot of what makes v0 work. So let's say that you wanted to create the v0 for doctors as an example. You can go to vercel.com/templates, and you can clone a ChatGPT template that basically follows all of the best practices in the world for really high-performance, awesome UIs, and now you can go out and build your own AI products. We've also open-sourced the AISDK, which is the foundational plumbing of v0. It allows you to connect any model and generate UI from its responses, not just output text, but actually generate UI. So maybe because I love showing stuff, I'll just really quickly show you this.

Lenny Rachitsky (01:03:45):
Okay, cool.

Guillermo Rauch (01:03:45):
Because I'm excited about it.

Lenny Rachitsky (01:03:46):
Let's do it.

Guillermo Rauch (01:03:47):
So if you go to chat.vercel@ai super quick, you're going to see this is the open-source ChatGPT demo that we've built. You can ask questions like old-school LLM. But also, you can ask, let's actually finish this, let's ask, "What is the weather in San Francisco?" We call this generative UI. It's responding not with just plain text, it's creating components as a result. Last but not least, and this is a v0 style opportunity, let's ask it to help me write an essay about Silicon Valley. It's going to create a canvas or artifacts style experience, and everything is generative, but also users can edit, refine, et cetera, et cetera, et cetera.

Lenny Rachitsky (01:04:36):
This actually reminds me of something I've been thinking about. There's all these startups that are building vertical AI tools. This is a little bit of a tangent, and there's always this AI stuff for lawyers, AI stuff for doctors, nurses, and the pitch there is that these are going to be founders that know a lot about the specific problem in this-

Guillermo Rauch (01:04:53):
Totally.

Lenny Rachitsky (01:04:53):
... useless market, and so they'll build the tools that are very specific to them.

Guillermo Rauch (01:04:58):
Yeah, I'm absolutely convinced that expert AI tools are the future. There's an amazing product being built on Vercel called chatprd.com. It's the v0 for writing PRDs and it's going to get a v0 integration soon so that you can write your PRD with AI and then you can create it with AI. That's just an example of a vertical that you can go after. There's also OpenEvidence. It's like the ChatGPT for doctors, actually. There is an amazing startup building x-ray AI tooling. So the ideas I think are infinite, and what I've seen from users of AI at Vercel, for example, our legal team loves this tool called Get GC.AI. They could in theory go to ChatGPT to ask legal questions, but someone out there decided, "I'm going to build the best legal AI tool in the world." It's going to be up to date. I'm going to obsess about this problem." The CEO herself is a lawyer, so it's going to be hard to compete with that, I think.

Lenny Rachitsky (01:06:03):
But here's what I'm thinking. This is almost the opposite and I'm curious to get your take, but let's not spend too much time on this, because this is a complete change in-

Guillermo Rauch (01:06:10):
No, I love it.

Lenny Rachitsky (01:06:11):
So you showed me the weather widget that you just built, basically it's like a little mini app that the AI built as you're talking to it. Is there a world where when AI, when AGI is far enough and approaching super intelligence? Can it just build you a Harvey, for example, in real time? "Here's the best experience for a lawyer. Here we go. We got it for you."

Guillermo Rauch (01:06:31):
Totally, totally. I believe that eventually, yes, but humans will always want to have some guardrails. The reality is that Get GC is taking a double job. One is making the best tools for lawyers possible, but also putting their weight behind it, saying, "We've actually used this and we believe that this is what the future should look like." There is a sense of direction and opinion about things and I think left to its own devices, AI, I don't know, this is the double-edged like prompt embellishment. AI doesn't always know exactly what we want or what we need. It's still very much a copilot, a partner, an assistant. It's not really running our lives, and I don't know that we even would want that, ultimately.

Lenny Rachitsky (01:07:23):
Okay, I'm going to go in a whole different direction, which is taste. We hear this word taste all the time. It feels like a thing that people are always suggesting. This will continue to be an important skill, to know what is good, basically to know what people are likely to find valuable and good. And I know clearly you have great taste. You're building incredibly beautiful products, v0's clearly, it's like the most beautiful by default builder out there, as we've seen. So in terms of building taste, people are always like, "How the hell do I do that? I have great taste. I know I do. I don't need to." How have you built taste? How do you think you build taste and any advice for folks that are trying to improve their taste?

Guillermo Rauch (01:08:03):
Yes, I think it's extremely important to try lots of products. You need to get yourself out there. I think it's very important to go back to that, get into the world, ship things. Don't be hesitant of self-promotion in a way. So being very honest with yourself, building something, getting it out there, see how people react. Go back to the drawing board. I think it's about exposure. At Vercel we have one of our internal operating principles as increasing exposure hours. Try to quantify how much time you expose yourself to watching how people use your products, even to watch how people use other products, and you'll develop that muscle. Taste, sometimes I think we think of as this inaccessible thing that, "Oh, that person was born with taste." I see it as a skill that it can develop. 

(01:09:07):
And again, the AI will help you a lot here because we try and capture some of the universal principles of it. But there's also trends in the world. I'm not a super couture guy, but you can see that every year Paris Fashion Week has a theme to it and there is some innovations, there have some breakthroughs, whatever. And so trying to stay at the frontier or even try and define the frontier as well is certainly very exciting.

Lenny Rachitsky (01:09:42):
I love how doable this is, increasing your exposure hours. Basically what I'm hearing is, "Use the best apps."

Guillermo Rauch (01:09:50):
Yes.

Lenny Rachitsky (01:09:50):
There's a feedback cycle component to it. Just like, "Show people the thing."

Guillermo Rauch (01:09:54):
And understand these nuances. Right?

Lenny Rachitsky (01:09:54):
Mm-hmm.

Guillermo Rauch (01:09:56):
So I actually recently created, I published it to my community, [inaudible 01:10:01] v0. I created a ChatGPT style interface inspired by Grok. And I captured a few things that Grok does that are just so smart. So on mobile web, when you press enter on their input, they default to creating a new line. Because they know that the way that people are used to submitting things on mobile is not by hitting enter, like we would do on a desktop computer. You can tap the little icon and your message goes out. On desktop, they inverted it. When you press enter, you're expected to submit. And I think if you got a new line, I think a lot of people would get frustrated that most people don't know that they can press command, enter to submit and whatever, and it slows everything down. And you can basically prompt for those things.

(01:10:48):
But you have to pay attention to the details and you have to decide what you want to see in the world. And sometimes that means either defining best practices, or seeking the best practices, and learning from others. Another aspect of exposure hours is that you tend to overrate how well your products work. It's very important to give your product to another person and watch them interact with it, expose yourself to the pain of reality. And the more you submerge yourself in the real deal, nitty-gritty of what happens when people use your interfaces and whatnot, I think you you'll come out stronger, more grounded, hopefully more humbled.

Lenny Rachitsky (01:11:34):
We don't like pain, though, and I like that this is a push, "Create some more pain in your life. Show people the thing you're building." Do you have a heuristic or number of how many exposure hours per week, per month you want your team to have or is it just more is always better?

Guillermo Rauch (01:11:48):
Yeah, I'm more is always better. I mean, because the inertia is to get inside your head, and the inertia is to think that you know everything, and assume that everything is going good, and, "There are no errors. Of course it's fast. It worked on my machine." I think it's always a push for more. I do sometimes little things like I asked my team to color my calendar. So I say I have to have a certain amount of one-on-ones with my team represented on my calendar, kind of like meetings so that I can sync with people and see how the company's doing. Then I want to have customer meetings. And during those customer meetings I push myself to use the products. In fact, with our enterprise customers, something that I do is I try to forget how things are built, what feature of [inaudible 01:12:41] or Vercel they use and whatever. I just frequently use their products. And I want the product to be great, that's all. And then I could try to work backwards. 

(01:12:49):
So a form of exposure hours for me is seeing what kind of success our customers are having in the real world. But again, it's just heuristic. Maybe one third of my meetings this week where customer meetings I tried and watched them do. Another really quick one is we invite people frequently to demo how they use the product live, sometimes to the executive team, sometimes to the whole company. And we always inevitably discover something interesting from the customer about maybe there is something that they're in pain about that we didn't know about, or maybe something was not as intuitive as we thought.

Lenny Rachitsky (01:13:31):
And I find with these sorts of things, when you do them, when you talk to customers, you have them show how they use the product. You always like, "Why have I not done this more often? What am I thinking?" It's just so mind-blowing usually.

Guillermo Rauch (01:13:43):
Yes.

Lenny Rachitsky (01:13:44):
I want to talk about limitations of v0 at this point. So what should people know about just what v0 can't do? If you have an existing code base, can you plug it in and start doing stuff? Or is that coming? What else should people know? Just like, "Okay, it's not going to do this yet. But- " 

Guillermo Rauch (01:13:59):
Yeah, you can import code bases through zip files and Git is coming very soon. It can do full stack development, it can connect to APIs. In the next couple of days, maybe even before this podcast is out, we'll have these very tight integrations so that if you need a database, or if you need an AI model, or if the AI decides it needs that, it'll just seamlessly install it from the Vercel marketplace. And the Vercel marketplace has already curated some of the best infrastructure products in the world to store data, to search data, et cetera. So it's going to make the product even more powerful. I'll say again, I did that exercise, and I do that exercise every day of I have a wild idea and try to see if it can come to life. It's very powerful so far. AIs are still very much a work in progress. They can make mistakes. We have it as a little disclaimer underneath the input. You will find errors, our fitness function. And we've seen such a strong correlation between user love and retention. 

(01:15:05):
v0's actually their retentive product compared to other AI products that I've built in the past, or little demos that we've done, or whatever. People subscribe and use it every single day, and are very, if they notice a bug, they're very, very jittery about it because they're depending on it day in and day out. But I'll say errors are still possible. Every once in a while you might get a runtime error or whatever, but a lot of the technology that we've added is so that v0 is very agentic. It has a lot of agency in how to act. So you're going to see very frequently that if it runs into errors, v0 tries to solve them itself.

(01:15:48):
And then last I will say, when products get really big, AI today is just not as good at dealing with massive code bases. But going back to that idea of the React component, because we break down things into files and components, we tend to do quite well in that dimension. In fact, one thing that Next.js was known for is that in order to start a project, you just create a file, and Next.js will route to that page. If anyone is familiar with PHP, it's like how PHP worked. And so it's so good that LLMs are good at working with files now, because it fits very naturally into our world. And if you can scope down when things get really big, if you can give it a smaller task, to work on a specific component or a specific file, you decrease that likelihood of the LLM not being able to reason over very, very, very long context windows.

Lenny Rachitsky (01:16:54):
I want to go back to design. We talked about how v0 is really good at just great design by default. To lean into that more, if someone wants to improve the design of their product, most people are not designers, they don't really know how to make it look good. They don't know what to ask for. Any just tips and best practices for making their app even better, look even nicer?

Guillermo Rauch (01:17:15):
Yeah, it was really interesting. The other day I met with a CIO of a large bank who, on the side does a lot of coding, or tries out new technologies and whatnot. And I showed him v0. And he immediately became a v0 addict. He texts me every day with feedback. He moved two websites of his own from another website builder type provider to v0 and Vercel, deployed them, gave them a domain name, they're live in production. And then he said, "Look, I have this challenge. I have this music festival that I organize with a couple of friends and this is what the designer gave us." And he had this brochure. It looked very much like a print style design. And so he gave that to v0 and the first result, he was dinging me for it. He's like, "Look, this doesn't look good."

(01:18:09):
And then, because I have experience with the tool, I said, "Why don't I just give it the feedback?" Literally you were asking me yesterday, earlier, some of the things that I've learned with the product or the best practice, what would I recommend if it were sitting next to someone? Not only, you should not hesitate to give the AI feedback, it's so interesting, dude. Sometimes people will press a feedback button to tell us what they wanted v0 to do, and literally all we had to do, in many cases is just, "Can you just tell v0 that?" And so he sent me this message saying, "Yeah, I just don't like the design." And I gave him back a prompt that I would've given. I don't know what I said specifically, but it's like, "Make it more jazzy, make it more, make it pop." 

(01:18:56):
And so trying, and again, it goes back to try to draw inspiration from variety that the AI already knows about. So in a couple of prompts, we ended up something that was in his mind, better than the original print design of that brochure, that concert lineup. And at that time, and again, I'm even learning about what v0 is capable of and the best ways to use it. But with design, I think unleashing its creativity, and seeing things, and playing with it is definitely super helpful.

Lenny Rachitsky (01:19:35):
So one thing I'm hearing here is just tell it, "Make this look better." Or, "I don't like- "

Guillermo Rauch (01:19:40):
"Make it pop."

Lenny Rachitsky (01:19:41):
"Make it pop."

Guillermo Rauch (01:19:42):
You can, totally. And if you can use tokens that are relevant, so, "Neobrutalist, minimalist, newspaper-like, vintage, make it look like a telegram." You can try and reach for things that maybe would not naturally come to mind and you'll be surprised about how well it can transfer those ideas into reality.

Lenny Rachitsky (01:20:09):
Incredible. Too easy. Maybe to close out our conversation, we'll see where this topic goes. I had this tweet that I loved, that I super resonate with, "The secrets of product quality is blood, sweat, and tears." I completely agree. I think that's why I think my newsletter's been successful. I spend so much time on every newsletter post, more than I think anyone spends on a newsletter post, like 10, 20, 30 hours. And that's why I think it works. Is there anything more behind that tweet, anything you've learned in just the importance of working hard, I guess to great, great stuff?

Guillermo Rauch (01:20:42):
Yeah, I mentioned exposure hours is a good example of like, "Look, it can be painful. It can be painful to see your baby break in front of everyone and noticing all the ... " The other thing is that a great product is made up of a thousand little details and so you're never really done. There's a humility that comes from the process also of why the best product builders will say nine nos for every yes. Because when you say yes, it's like adopting a puppy. A feature is like adopting a puppy. It grows into a beast that you have to take care of, and it's very demanding and loving. But also it's a lot, and poops everywhere. So you have to have a creative restraint. And while you also have to have a give, you have to withhold, sometimes with the respect of the real world complexity that emerges.

(01:21:42):
A little thing that I kind of obsess about. I'll give kudos to the Midjourney team. I really love how Midjourney works on mobile web. I don't know if they have an app yet, like a native app, but their mobile website is phenomenal. And to get it to be that good, by the way, it's possible. It's actually possible to make great things on mobile web. But it needs that sense of love, and restraint, and obsession, and testing a lot, and using your own products a lot. Dogfooding is a great mechanism, obviously. So we use the heck out of Vercel and v0 to make Vercel and v0, and hopefully that helps us do better. But there is a lot of blood, sweat, and tears in the process.

Lenny Rachitsky (01:22:30):
Yeah. You can tell how much you use the product. It comes through in everything you say. Let me actually ask about this. You talked about how you said you have 600 engineers?

Guillermo Rauch (01:22:38):
No, 600 people, total and a hundred-

Lenny Rachitsky (01:22:40):
600 people total?

Guillermo Rauch (01:22:41):
... 150. 

Lenny Rachitsky (01:22:42):
How is AI changing the way they work? Is there anything there? Because I feel like you guys are the cutting edge of how products are built. What's happening? Is it just everyone's on Cursor and v0 to build stuff?

Guillermo Rauch (01:22:55):
Yeah. Yes, but actually it's more profound. I think it's the, everybody can ship, it's the, we build with AI principles in mind. I actually give a shout-out to the Lumalabs engineer who said, "Well, I'll use AI for everything. I'll use AI also to generate the images for the website." And I'm seeing, for example, our designers that are working on our next conference generate all of the animations with video models. I'm looking at, our marketing team are creating demos of how the infrastructure works with v0 that are better than any static diagram or landing page that I've ever seen. One of my most viral xeets or X posts is something that one of our designers created, which explains how our compute infrastructure works with an interactive demo. And until he created that, by the way he designed, it and created, and we shipped it all in the tool, first of all, it wasn't part of his day-to-day job to do that.

(01:24:06):
v0 is making you such a powerful generalist that you can step out of your comfort zone of like, "Well, my job was to do only this." You can just create. We have a ritual every Friday, we had it this morning, called Demo Fridays. And so it's very important to create the space for people to step out of that comfort zone and use AI. So us giving permission to people to build and ship things is part of that cultural backdrop that makes these things possible. 

(01:24:42):
We had a demo today as part of the Demo Friday of our VP of sales engineering also creating an amazing tool that he's going to use to help prospects understand Vercel with v0. So I've heard from DevOps and infrastructure engineers how much they use tools like Cursor to work on the low levels of the Vercel infrastructure. So I think very quickly we're seeing AI being embedded everywhere. I just heard a product request from a customer that was saying, "Okay, Vercel, you sell domain names. Let me come up with new domain ideas with AI." So I just see a future where AI becomes synonymous with software. I do look forward to it because we need to stop talking about AI at some point. I foresee, it's probably not going to happen, but it is useful to remind people that AI equals software now, and we are a software company. We build software, and we use software to build software.

Lenny Rachitsky (01:25:41):
And AI is just a part of that.

Guillermo Rauch (01:25:42):
Yeah.

Lenny Rachitsky (01:25:43):
Guillermo, what a beautiful way to end it. Is there anything else you wanted to mention? Anything else that you want to leave listeners with before I let you go?

Guillermo Rauch (01:25:53):
I'll leave you with my vision of the future, which is we have this billboard in San Francisco, which is, "Everybody Can Cook." It is also part of the Ratatouille film, one of my favorite movies. I look forward to a future where everybody can get their ideas out there. If you can dream it, you can ship it. And also that when you use products and when you see the creations of other people and the things that they put out into the world, that we are collectively making the world better. So anything you experience hopefully gets faster, higher quality, fewer bugs as we go along. And I think we're all contributing to that. And I look forward to that and I look forward to everyone's feedback on how Vercel can play a part in that future.

Lenny Rachitsky (01:26:45):
So to build on that, where can folks find you online? Should they just go to vercel.com, visit v0.com?

Guillermo Rauch (01:26:45):
Yeah. And go to v0.dev-

Lenny Rachitsky (01:26:45):
.dev.

Guillermo Rauch (01:26:53):
... to get started. I did mention if you want to build your own v0, this is more advanced, but check out our templates on vercel.com/templates. And also I'm BrouchG on X, so you can DM me or tweet at me at any time.

Lenny Rachitsky (01:27:11):
Amazing. Guillermo, thank you so much for being here.

Guillermo Rauch (01:27:13):
Thank you, Lenny. It was so fun. 

Lenny Rachitsky (01:27:15):
Bye, everyone. 

MUSIC (01:27:18):
(instrumental music)

Lenny Rachitsky (01:27:19):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcasts.com. See you in the next episode.

