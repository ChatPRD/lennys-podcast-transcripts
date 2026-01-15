---
guest: Aishwarya Naresh Reganti + Kiriti Badam
keywords:
- retention
- onboarding
- metrics
- roadmap
- user research
- iteration
- subscription
- culture
- strategy
- vision
- mission
- market
- design
- ui
- prototype
title: 'Why most AI products fail: Lessons from 50+ AI deployments at OpenAI, Google
  & Amazon'
youtube_url: https://www.youtube.com/watch?v=z7T1pCxgvlA
video_id: z7T1pCxgvlA
description: Aishwarya Naresh Reganti and Kiriti Badam have helped build and launch
  more than 50 enterprise AI products across companies like OpenAI, Google, Amazon.
duration_seconds: 5183.0
duration: '1:26:23'
view_count: 21183
---

# Why most AI products fail: Lessons from 50+ AI deployments at OpenAI, Google & Amazon

## Transcript

Lenny Rachitsky (00:00:00):
We worked on a guest post together. They had this really key insight that building AI products is very different from building non-AI products.

Aishwarya Naresh Reganti (00:00:08):
Most people tend to ignore the non-determinism. You don't know how the user might behave with your product, and you also don't know how the LLM might respond to that. The second difference is the agency control trade-off. Every time you hand over decision-making capabilities to agentic systems, you're kind of relinquishing some amount of control on your end.

Lenny Rachitsky (00:00:25):
This significantly changes the way you should be building product.

Kiriti Badam (00:00:28):
So we recommend building step-by-step. When you start small, it forces you to think about what is the problem that I'm going to solve. In all this advancements of the AI, one easy, slippery slope is to keep thinking about complexities of the solution and forget the problem that you're trying to solve.

Aishwarya Naresh Reganti (00:00:42):
It's not about being the first company to have an agent among your competitors. It's about have you built the right flywheels in place so that you can improve over time.

Lenny Rachitsky (00:00:50):
What kind of ways of working do you see in companies that build AI products successfully?

Aishwarya Naresh Reganti (00:00:55):
I used to work with the CEO of now Rackspace. He would have this block every day in the morning, which would say catching up with AI 4:00 to 6:00 AM. Leaders have to get back to being hands-on. You must be comfortable with the fact that your intuitions might not be right. And you probably are the dumbest person in the room and you want to learn from everyone.

Lenny Rachitsky (00:01:13):
What do you think the next year of AI is going to look like?

Kiriti Badam (00:01:16):
Persistence is extremely valuable. Successful companies right now building in any new area, they are going through the pain of learning this, implementing this and understanding what works and what doesn't work. Pain is the new moat.

Lenny Rachitsky (00:01:29):
Today, my guests are Aishwarya Reganti and Kiriti Badam. Kiriti works on Kodex at OpenAI and has spent the last decade building AI and ML infrastructure at Google and at Kumo. Ash was an early AI researcher at Alexa and Microsoft and has published over 35 research papers. Together, they've led and supported over 50 AI product deployments across companies like Amazon, Databricks, OpenAI, Google, and both startups and large enterprises. Together, they also teach the number one rated AI course on Maven, where they teach product leaders all of the key lessons they've learned about building successful AI products. The goal of this episode is to save you and your team a lot of pain and suffering and wasted time trying to build your AI product. Whether you are already struggling to make your product work or want to avoid that struggle, this episode is for you. If you enjoy this podcast, don't forget to subscribe and follow to your favorite podcasting app or YouTube.

(00:02:22):
It helps tremendously. And if you become an annual subscriber of my newsletter, you get a year free of a ton of incredible products, including a year free of Lovable, Replit, Bold, Gamma, NA, and Linear Dev and Posttalk, Superhuman, Descript, Whisper Flow, Perplexity, Warp, Granola, Magic [inaudible 00:02:38] Mobbin, and Stripe Atlas. Head on over to lennysnewsletter.com and click product pass. With that, I bring you Aishwarya, Reganti, and Kiriti Badam after a short word from our sponsors.

(00:02:49):
This episode is brought to you by Merge. Product leaders hate building integrations. They're messy. They're slow to build. They're a huge drain on your roadmap, and they're definitely not why you got into product in the first place. Lucky for you, Merge is obsessed with integrations. With a single API, B2B SaaS companies embed Merge into their product and ship 220 plus customer-facing integrations in weeks, not quarters.

(00:03:14):
Think of merge like Plaid, but for everything B2B SaaS. Companies like Mistral AI, Ramp, and Drata use Merge to connect their customers as accounting, HR, ticketing, CRM, and file storage systems to power everything from automatic onboarding to AI-ready data pipelines. Even better, Merge now supports the secure deployment of connectors to AI agents with a new product so that you can safely power AI workflows with real customer data. If your product needs customer data from dozens of systems, Merge is the fastest, safest way to get it. Book and attend a meeting at merge.dev/lenny, and they'll send you a $50 Amazon gift card. That's merge.dev/lenny. This episode is brought to you by Strella, the customer research platform built for the AI era. Here's the truth about user research. It's never been more important or more painful. Teams want to understand why customers do what they do, but recruiting users running interviews and analyzing insights takes weeks.

(00:04:14):
By the time the results are in, the moment to act has passed. Strella changes that. It's the first platform that uses AI to run and analyze in depth interviews automatically, bringing fast and continuous user research to every team. Strella's AI moderator asks real follow-up questions, probing deeper when answers are vague, and services patterns across hundreds of conversations all in a few hours, not weeks. Product, design, and research teams at companies like Amazon and Duolingo are already using Strella for Figma prototype testing, concept validation, and customer journey research, getting insights overnight instead of waiting for the next sprint. If your team wants to understand customers at the speed you ship products, try Strella. Run your next study at strella.io/lenny. That's S-T-R-E-L-L-A.io/lenny. Ash and Kiriti, thank you so much for being here and welcome to the podcast.

Aishwarya Naresh Reganti (00:05:13):
Thank you, Lenny.

Kiriti Badam (00:05:14):
Thank you for having us. Super excited for this.

Lenny Rachitsky (00:05:16):
Let me set the stage for the conversation that we're going to have today. So you two have built a bunch of AI products yourself. You've gone deep with a lot of companies who have built AI products, have struggled to build AI products, build AI agents. You also teach a course on building AI products successfully and you're kind of on this mission to just reduce pain and suffering and failure that you constantly see people go through when they're building AI products. So to set a little just foundation for the conversation we're going to have, what are you seeing on the ground within companies trying to build AI products? What's going well? What's not going well?

Aishwarya Naresh Reganti (00:05:54):
I think 2025 has been significantly different than 2024. One, the skepticism has significantly reduced. There were tons of leaders last year who probably thought this would be yet another crypto wave and kind of skeptical to get started. And a lot of the use cases that I saw last year were more of slap chat on your data. And that was calling themselves an AI product. And this year, a ton of companies are really rethinking their user experiences and their workflows and all of that and really understanding that you need to deconstruct and reconstruct your processes in order to build successful AI products. And that's the good stuff. The bad stuff is the execution is still all over the place. Think of it. This is a three-year-old field. There are no playbooks, there are no textbooks. So you really need to figure out as you go. And the AI lifecycle, both pre-deployment and post-deployment is very different as compared to a traditional software lifecycle.

(00:06:57):
And so a lot of old contracts and handoffs between traditional roles, like say PMs and engineers and data folks has now been broken and people are really getting adapted to this new way of working together and kind of owning the same feedback loop in a way. Because previously, I feel like PMs and engineers and all of these folks had their own feedback loops to optimize. And now you need to be probably sitting in the same room. You're probably looking at agent traces together and deciding how your product should behave. So it's a tighter form of collaboration. So companies are still kind of figuring that out. That's kind of what I see in my consulting practice this year.

Lenny Rachitsky (00:07:37):
So let me follow that thread. We worked on a guest post together that came out a few months ago. And the thing that stood out to me most that stuck with me most after working on that post is this really key insight that building AI products is very different from building non-AI products. And the thing that you're big on getting across is there's two very big differences. Talk about those two differences.

Aishwarya Naresh Reganti (00:08:01):
Yes. And again, I want to make sure that we drive home the right point. There are tons of similarities of building AI systems and software systems as well, but then there are some things that kind of fundamentally change the way you build software systems versus AI systems. And one of them that most people tend to ignore is the non-determinism. You're pretty much working with a non-deterministic API as compared to traditional software. What does that mean and why does that have to affect us is in traditional software, you pretty much have a very well-mapped decision engine or workflow. Think of something like Booking.com. You have an intention that you want to make a booking in San Francisco for two nights, et cetera. The product has kind of been built so that your intention can be converted into a particular action and you kind of are clicking through a bunch of buttons, options, forms, and all of that, and you finally achieve your intention.

(00:08:59):
But now that layer in AI products has completely been replaced by a very fluid interface, which is mostly natural language, which means the user can literally come up with a ton of ways of saying or communicating their intentions. And that kind of changes a lot of things because now you don't know how your user's going to be here. That's on the input side. And the output is also that you're working with a non-deterministic probabilistic API, which is your LLM. And LLMs are pretty sensitive to prompt phrasings and they're pretty much black boxes. So you don't even know how the output surface will look like. So you don't know how the user might behave with your product, and you also don't know how the LLM might respond to that. So you're now working with an input, output, and a process. You don't understand all the three very well. You're trying to anticipate behavior and build for it.

(00:09:53):
And with agentic systems, this kind of gets even harder. And that's where we talk about the second difference, which is the agency control trade-off. What we mean by that, and I'm kind of shocked so many people don't talk about this. They're extremely obsessed with building autonomous systems, agents that can do work for you. But every time you hand over decision-making capabilities or autonomy to agentic systems, you're kind of relinquishing some amount of control on your end. And when you do that, you want to make sure that your agent has gained your trust or it is reliable enough that you can allow it to make decisions. And that's where we talk about this agency controlled trade-off, which is if you give your AI agent or your AI system, whatever it is, more agency, which is the ability to make decisions, you're also losing some control and you want to make sure that the agent or the AI system has earned that ability or has built up trust over time.

Lenny Rachitsky (00:10:49):
So just to summarize what you're sharing here, essentially, people have been building product, software products for a long time. We're now in a world where the software you're building is one, non-deterministic, can just do things differently. As you said, you go to booking.com, you find a hotel, it's going to be the same experience every time. You'll see different hotels, but it's a predictable experience. With AI, you can't predict that it's going to be the exact same thing, the thing that you plan it to be every time. And then the other is there's this trade-off between agency and control. How much will the AI do for you versus how much should the person still be in charge? And what I'm hearing is the big point here is this significantly changes the way you should be building product. And we're going to talk about the impact on how the product development lifecycle should change as a result.

(00:11:35):
Is there anything else you want to add there before we get into that?

Kiriti Badam (00:11:39):
Yeah, it's definitely one of the key points that this kind of distinction needs to exist in your mind when you're starting to build. For example, think about if your objective is to hike Half Dome in Yosemite. You don't start hiking it every day, but you start training yourself in minor parts and then you slowly improve and then you go to the end goal. I feel like that's extremely similar to what you want to build AI products in the sense that when you don't start with agents with all the tools and all the context that you have in the company in day one and expect it to work or even tinker at that level. You need to be deliberately starting in places where there is minimal impact and more human control so that you have a good grip of what are the current capabilities and what can I do with them and then slowly lean into the more agency and lesser control.

(00:12:29):
So this gives you that confidence that, okay, I can know that, okay, this is the particular problem that I'm facing and the AI can solve this extent of it. And then let me next think through what context I need to bring in, what kind of tools I need to add to this to improve the experience. So I feel like also it's a good and a bad thing in the sense that it's good that you don't have to see the complexity of the outside world of all of this fancy AI agents force and feel like I cannot do that. Everyone is starting from very minimalistic structures and then evolving. And the second part is the bad thing is that as you are trying to build this one click agents into your company, you don't have to be overwhelmed with this complexity. You can slowly graduate.

(00:13:16):
So that's extremely important. And we see this as a repeating pattern over and over.

Lenny Rachitsky (00:13:20):
Okay. So let's actually follow that because that's a really important component of how you recommend people build AI stuff, AI products, AI agents, all the AI things. So give us an example of what you're talking about here, this idea of starting slow with agency and control and then moving up this rung.

Kiriti Badam (00:13:38):
Yeah. For example, a very important or very prevalent application of AI agents is customer support. Imagine you are a company who has a lot of customer support tickets and why even imagine OpenAI is the exact same thing when we were launching products and there was a huge spike of support volume as we launched successful products like Image or GPT-5 and things like that. The kind of questions you get is different. The kind of problems that the customers bring to you is different. So it's not about just dumping all the list of help center articles that you have into the AI agent. You kind of understand what are the things that you can build. And so initially the first step of it would be something like you have your support agents, the human support agents, but you will be suggesting in terms of, okay, this is what the AI thinks that is the right thing to do.

(00:14:33):
And then you get that feedback loop from the humans that, okay, this is actually a good suggestion for me in this particular case and this is a bad suggestion. And then you can go back and understand, okay, this is what the drawbacks are or this is where the blind spots are, and then how do I fix that? And once you get that, you can increase the autonomy to say that, okay, I don't need to suggest to the human. I'll actually show the answer directly to the customer. And then we can actually add more complexity in terms of, okay, I was only answering questions based on health center articles, but now let me add new functionality. I can actually issue refunds to the customers. I can actually raise feature requests with the engineering team and all of these things. So if you start with all of this on day one, it's incredibly hard to control the complexity.

(00:15:19):
So we recommend building step by step and then increasing it.

Lenny Rachitsky (00:15:23):
Awesome. And you have a visual actually that we'll share of what this looks like. But just to kind of mirror back what you're describing, this idea of start with high control, low agency, the example you gave is the support agents just kind of giving suggestions, is not able to do anything, the user is in charge. And then as that becomes useful and you are confident it's doing the right sort of work, you give it a little more agency and you kind of pull back on the control the user has. And then if that's starting to go well, then you give it more agency and the user needs less control to control it. Awesome.

Aishwarya Naresh Reganti (00:16:02):
I think the higher level idea here is with AI systems, it's all about behavior calibration. It's incredibly impossible to predict upfront how your system behaves. Now, what do you do about it? You make sure that you don't ruin your customer experience or your end user experience. You keep that as is, but then remove the amount of control that the human has. And there is no single right way of doing it. You can decide how to constrain that autonomy. I mean, a different example of how you could constrain autonomy is pre-authorization use cases. Insurance pre-authorization is a very ripe use case for AI because clinicians spend a lot of time pre-authorizing things like blood tests, MRIs and things like that. And there are some cases which are more of low hanging fruits. For instance, MRIs and block tests, because as soon as you know patient's information, it's easier to approve that and AI could do that versus something like an invasive surgery, et cetera, is more high risk. You don't want to be doing that autonomously.

(00:17:11):
So you can kind of determine which of these use cases should go through that human and the loop layer versus which of the use cases AI can conveniently handle. And then all through this process, you're also logging what the human is doing because you want to build a flywheel that you could use in order to improve your system. So you're essentially not showing the user experience, not eroding trust, at the same time logging what humans would otherwise do so that you can continuously improve your system.

Lenny Rachitsky (00:17:41):
So let me give you a few more examples of this kind of progression that you recommend. And the reason I'm spending so much time here is this is a really key part of your recommendation to help people build more successful AI products. This idea of start slow with high control and low agency and then build up over time once you've built confidence that it's doing the right sort of work. So a few more examples that you shared in your post that I'll just read. So say you're building a coding assistant, V1 would be just suggest inline completion and boilerplate snippets. V2 would be generate larger blocks like tests or refactors for humans to review. And then V3 is just apply the changes and open PRs autonomously. And then another example is a marketing assistant. So V1 would be draft emails or social copy, just like here's what I would do.

(00:18:26):
V2 is build a multi-step campaign and run the campaign. And V3 is just launch it A/B tested auto-optimize campaigns across channels. Awesome. Yeah. And again, just to summarize where we're at, just to give people the advice we've shared so far. One is just important to understand AI products are different. They're non-deterministic. And you pointed out, and I forgot to actually mirror back this point, both on the input and the output. The user experience is non-deterministic.People will see different things, different outputs, different chat conversations, different maybe UI if it's designing the UI for you. And also the output obviously is going to be non-terministic. So that's a problem and a challenge. And then-

Aishwarya Naresh Reganti (00:19:08):
I mean, if you think of it's also the most beautiful part of AI, which is, I mean, we are all much more comfortable talking than following a bunch of buttons and all of that. So the bar to using AI products is much lower because you can be as natural as you would be with humans, but that's also the problem, which is there are tons of ways we communicate and you want to make sure that that intent is rightly communicated and the right actions are taken because most of your systems are deterministic and you want to achieve a deterministic outcome, but with non-deterministic technology and that's where it gets a little messy.

Lenny Rachitsky (00:19:44):
Awesome. Okay. I love the optimistic version of why this is good. Okay. And then the other piece is this idea of this trade-off of autonomy versus control when you're designing a thing. And I imagine what you're seeing is people try to jump to the ideal, like the V3 immediately and that's when they get into trouble both. It's probably a lot harder to build that and it just doesn't work. And then they're just like, "Okay, this is a failure. What are we even doing?"

Kiriti Badam (00:20:08):
Exactly. I feel there's a bunch of things that you actually have to get confidence in before you get to V3. And it's easy to get overwhelmed that, oh, my AI agent is doing these things wrong in a hundred different ways and you're not going to actually tabulate all of them and fix it. Even though you've learned how do you deal with the evaluation practices and stuff like that, if you're starting on the wrong spot, you are actually going to have a hard time correcting things from there. And when you start small and when you start with building a very minimalistic version with high human control and low agency, it also forces you to think about what is the problem that I'm going to solve. We use this term called problem first. And to me, it was obvious in the sense that that I do need to think about the problem, but it's incredible how well it resonates with the people that in all this advancements of the AI that we are seeing, one easy, slippery slope is to just keep thinking about complexities of the solution and forget the problem that you're trying to solve.

(00:21:10):
So when you're trying to start at a smaller scale of autonomy, you start to really think about what is the problem that I'm trying to solve and how do I break it down into levels of autonomy that I can build later? So that is incredibly useful and we keep repeating this part and over and over with everyone we talk to.

Lenny Rachitsky (00:21:31):
And there's so many other benefits to limiting autonomy because there's just danger also of the thing doing too much for you and just messing up your, I don't know, your database, sending out all these emails you never expected. And there's like so many reasons this is a good idea.

Aishwarya Naresh Reganti (00:21:45):
Yep. I recently read this paper from a bunch of folks at UC Berkeley. Basically Matei Zaharia, [inaudible 00:21:54] and the folks at Databricks and it said about 74% or 75% of the enterprises that they had spoken to, their biggest problem was reliability. And that's also why they weren't comfortable deploying products to their end users or building customer facing products because they just weren't sure or they just weren't comfortable doing that and exposing their users to a bunch of these risks. And that's also why they think a lot of AI products today have to do with productivity because it's much low autonomy versus end-to-end agents that would replace workflows. And yeah, I love their work otherwise as well, but I think that's very in line with what at least we are seeing at my startup as well.

Lenny Rachitsky (00:22:38):
Okay. Very interesting. There's an episode that'll come out before this conversation where we go deep into another problem that this avoids, which is around prompt injection and jailbreaking and just how big of a risk that is for AI products where it's essentially an unsolved and unsolvable problem potentially. I'm not going to go down that track, but that's a pretty scary conversation we had that'll be out before this conversation.

Aishwarya Naresh Reganti (00:23:02):
I think that will be a huge problem once systems go mainstream. We're still so busy building AI products that we're not worried about security, but it will be such a huge problem to kind of, especially with this non-deterministic API again. So you're kind of stuck because there are tons of instructions that you could inject within your prompt and then it's going really bad.

Lenny Rachitsky (00:23:28):
Okay. Let's actually spend a little time here because it's actually really interesting to me and no one's talking about this stuff, which is like the conversation we had is just it's pretty easy to get AI to do stuff it shouldn't do. And there's all these guardrail systems people put in place, but turns out these guardrails aren't actually very good and you can always get around them. And to your point, as agents become more autonomous and robots, it gets pretty scary that you could get AI to do things you shouldn't do.

Kiriti Badam (00:23:54):
I think this is definitely a problem, but I feel in the current spectrum of customers adopting AI, the extent to which companies can actually get advantage of AI or improve their processes or streamline the existing processes that they have, I feel it's still in the very early stage. 2025 has been an extremely busy year for AI agents and customers trying to adopt AI, but I feel the penetration is still not as much as you would actually get advantage out of it. So with the right sort of human in the loop points in here, I feel we can actually avoid a bunch of these things and focus more towards streamlining the processes. And I am more on the optimist side in the sense that you need to try and adopt this before actually trying to be only for highlighting the negative aspects of what could go wrong.

(00:24:47):
So I feel like strongly that companies has this adopt this, they definitely ... No company at OpenAI we talk to has never had been the case that, oh, AI cannot help me in this case. It has always been that, oh, there is this set of things that it can optimize for me and then let me see how I can adopt it.

Lenny Rachitsky (00:25:06):
Sweet. I always like the optimistic perspective. I'm excited for you to listen to this and see what you think because it's really interesting. And to your point, there's a lot of things to focus on. It's one of many things to worry about and think about. Okay, let's get back on track here. So we've shared a bunch of pro-tips and important piece of advice. Let me ask, what other patterns and kind of ways of working do you see in companies that do this well and teams that build AI products successfully? And then just what are the most common pitfalls people fall into? So we could just maybe start with, what are other ways that companies do this well, build AI products successfully?

Aishwarya Naresh Reganti (00:25:43):
I almost think of it as like a success triangle with three dimensions that's never always technical. Every technology problem is a people problem first. And with companies that we have worked with, it's these three dimensions, like great leaders, good culture and technical prowess. With leaders itself, we work with a lot of companies for their AI transformation, training, strategy and stuff like that. And I feel like a lot of companies, the leaders have built intuitions over 10 or 15 years and they're kind of highly regarded for those intuitions. But now with AI in the picture, those intuitions will have to be relearned and leaders have to be vulnerable to do that. I used to work with the CEO of now Rackspace, Gagan. So he would have this block every day in the morning, which would say catching up with AI 4:00 to 6:00 AM, and he would not have any meetings or anything like that.

(00:26:42):
And that was just his time to pick up on the latest AI podcast or information and all of that. And he would have weekend vibe coding sessions and stuff like that. So I think leaders have to get back to being hands-on. And that's not because they have to be implementing these things, but more of rebuilding their intuitions because you must be comfortable with the fact that your intuitions might not be right and you probably are the dumbest person in the room and you want to learn from everyone. And that I've seen that being a very distinguishing factor of companies that build products which are successful because you're kind of bringing in that top-down approach. It's almost always impossible for it to be bottom-up. You can't have a bunch of engineers go and get buy-in from the leader if they just don't trust in the technology or if they have misaligned expectations about the technology.

(00:27:34):
I've heard from so many folks who are building that our leaders just don't understand the extent to which AI can solve a particular problem or they just vibe code something and assume it's easy to take it to production and you really need to understand the range of what AI can solve today so that you can guide decisions within the company. The second one is the culture itself. And again, I work with enterprises where AI is not their main thing and they need to bring in AI into their processes just because a competitor is doing it. And just because it does make sense because there are use cases that are very ripe. Then along the way, I feel a lot of companies have this culture of FOMO and you will be replaced and those kind of things and people get really afraid. Subject matter experts are such a huge part of building AI products that work because you really need to consult them to understand how your AI is behaving or what the ideal behavior should be.

(00:28:27):
But then I've spoken to a bunch of companies where the subject matter experts just don't want to talk to you because they think their job is being replaced. So I mean, again, this comes from the leader itself. You want to build a culture of empowerment, of augmenting AI into your own workflows so that you can 10X at what you're doing instead of saying that probably you'll be replaced if you don't adopt AI and stuff like that. So that kind of an empowering culture always helps. You want to make your entire organization be in it together and make AI work for you instead of trying to guard their own jobs, et cetera. And with AI, it's also true that it opens up a lot more opportunities than before. So you could have your employees doing a lot more things than before and 10x their productivity. And the third one is the technical part which we talk about.

(00:29:18):
I think folks that are successful are incredibly obsessed about understanding their workflows very well and augmenting parts that could be ripe for AI versus the ones that might need human in the loop somewhere, et cetera. Whenever you're trying to automate some part of a workflow, it's never the case that you could use an AI agent and that will solve your problems. It's always, you probably have a machine learning model that's going to do some part of the job. You have deterministic code doing some part of the job. So you really need to be obsessed with understanding that workflow so you can choose the right tool for the problem instead of being obsessed with the technology itself. And another pattern I see is also folks really understand this idea of working with a non-deterministic API, which is your LLM. And what that means is they also understand the AI development lifecycle looks very different and they iterate pretty quickly, which is can I build something iterate quickly in a way that it doesn't ruin my customer experience at the same time gives me enough amount of data so that I can estimate behavior.

(00:30:31):
So they build that flywheel very quickly. As of today, it's not about being the first company to have an agent among your competitors. It's about, have you built the right flywheels in place so that you can improve over time? When someone comes up to me and says, "We have this one click agent, it's going to be deployed in your system." And then in two or three days, it'll start showing you significant gains. I would almost be skeptical because it's just not possible. And that's not because the models aren't there, but because enterprise data and infrastructure is very messy and you need a bit to ... Even the agent needs a bit to understand how these systems work. There are very messy taxonomies everywhere. People tend to do things like get customer data, we want, get customer data, we do, and these kind of things. And all those functions exist and they're being called and basically there's a lot of tech debt that you need to deal with.

(00:31:23):
So most of the times, if you're obsessed with the problem itself and you understand your workflows very well, you will know how to improve your agents over time instead of just slapping an agent and assuming that it'll work from day one. I probably will go as far to say that if someone's selling you one click-agents, it's pure marketing. You don't want to buy into that. I would rather go with a company that says, "We're going to build this pipeline for you," and that will learn over time and build a flywheel to improve than something that's going to work out of the box. To replace any critical workflow or to build something that can give you significant ROI, it easily takes four to six months of work, even if you have the best data layer and infrastructure layer.

Lenny Rachitsky (00:32:05):
Amazing. There's a lot there that resonates so deeply with other conversations I've been having on this podcast. One is just for a company to be successful at seeing a lot of impact from AI, the founder-CEO has to be deep into it. I had Dan Shipper on the podcast and they work with a bunch of companies helping them adopt AI. And he said that's the number one predictor of success. Is the CEO chatting with ChatGPT, Claude, whatever, many times a day. I love this example you gave with the Rackspace CEO has catch up on AI news in the morning every day. I was imagining he'd be chatting with the chatbot versus reading news.

Aishwarya Naresh Reganti (00:32:42):
With the kind of information you have as of today, you could just ... I mean, you want to choose the right channels as well because everybody has an opinion. So whose opinion do you want to bank on? I feel like having that good quality set of people that you're listening to really makes sense. So he just has a list of two or three sources that he always looks at. And then he comes back with a bunch of questions and bounces it around with a bunch of AI experts to see what they think about it. And I was part of that group, so I kind of know-

Lenny Rachitsky (00:33:11):
I love that.

Aishwarya Naresh Reganti (00:33:13):
... about the questions that he comes up with.

Lenny Rachitsky (00:33:13):
That's cool.

Aishwarya Naresh Reganti (00:33:15):
It's pretty cool. I was like, "Why are you doing so much?" And then he says, "It trickles down into a bunch of decisions that we take."

Lenny Rachitsky (00:33:21):
Okay. Let me talk about another topic that's very ... It's been a hot topic on this podcast. It was a hot topic on Twitter for a while, evals. A lot of people are obsessed with evals, think they're the solution to a lot of problems in AI. A lot of people think they're overrated that you don't need evals. You can just feel the vibes and you'll be all right. What's your take on evals? How far does that take people in solving a lot of the problems that you talk about?

Kiriti Badam (00:33:47):
In terms of what is going on in the community, I feel there's just this false dichotomy of this either evals is going to solve everything or online monitoring or production monitoring is going to solve everything. And I find no reason to trust one of the extremes in the sense that I will entirely bank my application on this or like that to solve the thing. So if you take a step back, think of what are evals. Evals are basically your trusted product thinking or your knowledge about the product that is going into this set of data sets that you're going to build in the sense that this is what matters to me. This is the kind of problems that my agent should not do and let me build a list of datasets so that I'm going to do well on those. And in terms of production monitoring, what you're doing there is you're deploying your application and then you're having some sort of key metrics that actually communicate back to you on how customers are using your product.

(00:34:47):
You could be deploying any agent and if the customer is giving a thumbs up for your interaction, you better want to know that. So that is what production monitoring is going to do. And this production monitoring has existed for products for a long time, just that now with the AI agents, you need to be monitoring a lot more granularity. It's not just the customer always giving you explicit feedback, but there is many implicit feedback that you can get. For example, in ChatGPT, if you are liking the answer, you can actually give a thumbs up. Or if you don't like the answer, sometimes customers don't give you thumbs down, but actually regenerate the answer. So that is a clear indication that the initial answer that regenerator is not meeting the customer's expectation. So these are the kind of implicit signals you always need to think about.

(00:35:35):
And that spectrum has been increasing in terms of production monitoring. Now let's come back to the initial topic of like, okay, is it evals or is it production monitoring? What does it matter? So I feel, again, we go back to this problem first approach of what is it that you're trying to build. You're trying to build a reliable application for your customers that's not going to do a bad thing. It's always going to do the right thing. Or if it is doing a wrong thing, you're basically alerted very quickly. So I break this down into two parts. One is nobody goes into deploying an application without actually just testing that. This testing could be wipes or this testing could be, "Okay, I have this 10 questions that it should not go wrong no matter what changes I make, and let me build this and let's call this an evaluation dataset." Now, let's say you build this, you deployed this, and then you figured, "Okay, now I need to understand whether it's doing the right thing or not."

(00:36:32):
So if you're a high throughput or a high transaction customer, you cannot practically sit and evaluate all the traces. You need some indication to understand what are the things that I should look at. And this is where production monitoring comes into the picture that you cannot predict the base in which your agent could be doing wrong, but all of these other implicit signals and explicit signals, those are going to communicate back to you what are the traces that you need to look at. And that is where production monitoring helps. And once you get this kind of traces, you need to examine what are the failure patterns that you're seeing in these different types of interactions. And is there something that I really care about that should not happen? And if that kind of failure modes are happening, then I need to think about building an evaluation dataset for it.

(00:37:20):
And okay, let's say I built an evaluation dataset for my agent trying to offer refunds where explicitly I have configured it not to. So I built this evaluation dataset and then I made my changes in tools or prompts or whatever, and then I deployed the second version of the product. Now there is no guarantee that this is the only problem that you're going to see. You still need production monitoring to actually catch different kinds of problems that you might encounter. So I feel evals are important, production monitoring is important, but this notion of only one of them is going to solve things for you that is completely dismissible in my opinion.

Lenny Rachitsky (00:37:58):
All right. A very reasonable answer. And the point here isn't, it's not just as simple as do both. It's more that there are different things to catch and one approach won't catch all the things you need to be paying attention to.

Aishwarya Naresh Reganti (00:38:11):
Exactly.

Lenny Rachitsky (00:38:12):
Awesome.

Aishwarya Naresh Reganti (00:38:13):
I want to take two steps back and kind of talk about how much weight the term evals has had to take in the second half of 2025 because you go meet a data labeling company and they tell you our experts are writing evals and then you have all of these folks saying that PMs should be writing evals, they're the new PRDs. And then you have folks saying that evals is pretty much everything, which is the feedback loop you're supposed to be building to improve your products. Now, step back as a beginner and kind of think what are evals? Why is everyone saying evals? And these are actually different parts of the process and nobody is wrong in the sense that yes, these are evals, but when a data labeling company is telling you that our experts are writing evals, they're actually referring to error analysis or experts just leading notes on what should be right.

(00:39:02):
Lawyers and doctors write evals, that doesn't mean they're building LLM judges or they're building this entire feedback loop. And when you say that a PM should be writing evals, doesn't mean they have to write an LLM judge that's good enough for production. I think there are also very prescriptive ways of doing this and plus one to KD, which is you cannot predict upfront if you need to be building an LLM judge versus you need to be using implicit signals from production monitoring, et cetera. I think Martin Fowler at some point had this term called semantic diffusion back in the 2000s, which kind of means that someone comes up with a term, everybody starts butchering it with their own definitions and then you kind of lose the actual definition of it. That is what is happening to evals or agents or any word in AI as of today, everybody kind of sees a different side to it, I guess.

(00:39:54):
But if you make a bunch of practitioners sit together and ask them, "Is it important to build an actionable feedback loop for AI products?" I think all of them will agree. Now, how you do that really depends on your application itself. When you go to complex use cases, it's incredibly hard to build LLM judges because you see a lot of emerging patterns. If you built a judge that would test for verbosity or something like that, it turns out that you're seeing newer patterns that your LLM judge is not able to catch, and then you just end up building too many evals. And at that point, it just makes sense to look at your user signals, fix them, check if you have regressed and move on instead of actually building these judges. So it all depends. I think one statement that every ML practitioner will tell you is it really depends on the context. Don't be obsessed with prescriptions they're going to change.

Lenny Rachitsky (00:40:45):
That's such an important point, this idea that, especially that evals just means many things to different people now. It's just a term for so many things. And it's complicated to just talk about evals when you see it as the stuff data labeling companies are giving you and things PMR, right? And there's also benchmarks. People call benchmarks a little bit evals. It's like-

Aishwarya Naresh Reganti (00:41:03):
I recently spoke to a client who told me, "We do evals." And I was like, "Okay, can you show me your dataset?" And said, "No, we just checked LM Arena and Artificial Analysis. These are independent benchmarks and we know that this model is the right one for our use case." And I'm like, "You're not doing evals. That's not evals. Those are model evals."

Lenny Rachitsky (00:41:20):
But it makes sense. The word, it could be used in that context. I get why people think that, but yeah, now it's just confusing it even more.

Aishwarya Naresh Reganti (00:41:26):
Yep.

Lenny Rachitsky (00:41:27):
Just one more line of questioning here that I think that's on my mind is the reason this became kind of a big debate is Cloud Code. The head of Cloud Code, Boris, was like, "Nah, we don't do evals on Cloud Code. It's all vibes." What can you share, Kiriti, on Kodex and the Kodex team, how you approach evals?

Kiriti Badam (00:41:44):
So Kodex, we have this balanced approach of you need to have evals and you need to definitely listen to your customers. And I think Alex has been on your podcast recently and he's been talking about how you're extremely focused on building the right product. And a big part of it is basically listening to your customers. And coding agents are extremely unique compared to agents for other domains in the sense that these are actually built for customizability and these are built for engineers. So coding agent is not a product which is going to solve these top five workflows or top six workflows or whatever. It's meant to be customizable in multi different ways. And the implication of that is that your product is going to be used in different integrations and different kinds of tools and different kinds of things. So it gets really hard to build an evaluation dataset for all kinds of interactions that your customers are going to use your product for.

(00:42:38):
With that said, you also need to understand that, okay, if I'm going to make a change, it's at least not going to damage something that is really core to the product. So we have evaluations for doing that, butt the same time we take extreme care on understanding how the customers are using it. For example, we built this code review product recently and it has been gaining extreme amount of traction. And I feel like many, many bugs in OpenAI as well as even our external customers are getting caught with this. And now let's say if I'm making a model change to the code review or a different kinds of RL mechanism that I trained with it, and now if I'm going to deploy it, I definitely do want A/B test and identify whether it's actually finding the right mistakes and how are users reacting to it? And sometimes if users do get annoyed by your incorrect code regis, they go to the extent of just switching off the product.

(00:43:36):
So those are the signals that you want to look at and make sure that your new changes are doing the right thing. And it's extremely hard for us to think of these kind of scenarios beforehand and develop evaluation data sets for it. So I feel like there's a bit of both. There's a lot of vibes and there's a lot of customer feedback and we are super active on the social media to understand if anybody's having certain types of problems and quickly fix that. So I feel it's a ... How do I put this? It's like a domain of things that you do here.

Lenny Rachitsky (00:44:08):
That makes so much sense. Okay. What I'm hearing, Codex, pro evals, but it's not enough.

Kiriti Badam (00:44:13):
Yes.

Lenny Rachitsky (00:44:13):
But also just watch customer behavior and feedback. And also there's some vibes just like, is this feeling good? As I'm using it, generating great code that I'm excited about that I think is great.

Kiriti Badam (00:44:24):
I don't think if anybody's coming and seeing that I have this concrete set of evals that I can bet my life on and then I don't need to think about anything else, it's not going to work. And every new model that you're going to launch, we get together as a team and test different things. Each person is concentrating on something else. And we have this list of hard problems that we have and we throw that to the model and see how well they're progressing. So it's like custom evals for each engineer, you would say, and just understand what the product is doing in its new model.

Lenny Rachitsky (00:44:58):
If you're a founder, the hardest part of starting a company isn't having the idea, it's scaling the business without getting buried in back office work. That's where Brex comes in. Brex is the intelligent finance platform for founders. With Brex, you get high limit corporate cards, easy banking, high yield treasury, plus a team of AI agents that handle manual finance tasks for you. They'll do all the stuff that you don't want to do, like file your expenses, scour transactions for waste, and run reports all according to your rules. With Brex's AI agents, you can move faster while staying in full control. One in three startups in the United States already runs on Brex. You can too at brex.com.

(00:45:43):
We've been talking for almost an hour already, and we haven't even covered your extremely powerful software development workflow for building AI products that you two developed that you teach in your course, that you basically combined all the stuff we've been talking about into a step-by-step approach to building AI products. You call it the continuous calibration, continuous development framework. Let's pull up a visual to show people what the heck we're talking about, and then just walk us through what this is, how this works, how teams can shift the way they build their AI products to this approach to help them avoid a lot of pain and suffering.

Aishwarya Naresh Reganti (00:46:18):
Before we go about explaining the life cycle, a quick story on why Kiriti and I came up with this is because there are tons of companies that we keep talking to that have the pressure from their competitors because they're all building agents. We should be building agents that are entirely autonomous. And I did end up working with a few customers where we built these end-to-end agents. And turns out that because you start off at a place where you don't know how the user might interact with your system and what kind of responses or actions the AI might come up with, it's really hard to fix problems when you have this really huge workflow, which is taking four or five steps, making tons of decisions. You just end up debugging so much and then kind of hot fixing to the point where at a time we were building for a customer support use case, which is the example that we give in the newsletter as well.

(00:47:13):
And we had to shut down the product because we were doing so many hot fixes and there was no way we could count all the emerging problems that were coming up. And there's also quite some news online. Recently, I think Air Canada had this thing where one of their agents predicted or hallucinated a policy for a refund, which was not part of their original playbook, and they had to go by it because legal stuff. And there have been a ton of really scary incidents. And that's where the idea comes from. How can you build so that you don't lose customer trust and you don't end up, or your agent or AI system doesn't end up making decisions that are super dangerous to the company itself. At the same time, build a flywheel so that you can improve your product as you go. And that's where we came up with this idea of continuous calibration, continuous development.

(00:48:08):
The idea is pretty simple, which is we have this right side of the loop, which is continuous development, where you scope capability and curate data, essentially get a data set of what your expected inputs are and what your expected outputs should be looking at. This is a very good exercise before you start building any AI product because many times you figure out that a lot of the folks within the team are just not aligned on how the product should behave. And that's where your PMs can really give in a lot more information and your subject matter experts as well. So you have this data set that you know your AI product should be doing really well on. It's not comprehensive, but it lets you get started. And then you set up the application and then design the right kind of evaluation metrics. And I intentionally use the term evaluation metrics, although we say evals because I just want to be very specific in what it is because evaluation is a process, evaluation metrics are dimensions that you want to focus on during the process.

(00:49:07):
And then you go about deploying, run your evaluation metrics. And the second part is the continuous calibration, which is the part where you understand what behavior you hadn't expected in the beginning, right? Because when you start the development process, you have this data set that you're optimizing for, but more often than not, you realize that that data set is not comprehensive enough because users start behaving with your systems in ways that you did not predict. And that's where you want to do the calibration piece. I've deployed my system. Now I see that there are patterns that I did not really expect and your evaluation metrics should give you some insight into those patterns, but sometimes you figure out that those metrics were also not enough and you probably have new error patterns that you have not thought about. And that's where you analyze your behavior, spot error patterns.

(00:49:59):
You apply fixes for issues that you see, but you also design newer evaluation metrics to figure out that they are emerging patterns. And that doesn't mean you should always design evaluation metrics. There are some errors that you can just fix and not really come back to because they're very spot errors. For instance, there's a tool calling error just because your tool wasn't defined well and stuff like that. You can just fix it and move on. And this is pretty much how an AI product lifecycle would look like. But what we specifically also mention is while you're going through these iterations, try to think of lower agency iterations in the beginning and higher control iterations. What that means is constrain the number of decisions your AI systems can make and make sure that they're humans in the loop and then increase that over time because you're kind of building a flywheel of behavior and you're understanding what kind of use cases are coming in or how your users are using the system.

(00:50:59):
And one example I think we give in the newsletter itself is the customer support. This is a nice image that kind of shows how you can think of agency and control as two dimensions. And each of your versions keep on increasing the agency or the ability of your AI system to make decisions and lower the control as you go. And one example that we give is that of the customer support agent, where you can break it down into three versions. The first version is just routing, which is your agent able to classify and route a particular ticket to the right department? And sometimes when you read this, you probably think, is it so hard to just do routing? Why can't an agent easily do that? And when you go to enterprises, routing itself can be a super complex problem. Any retail company, any popular retail company that you can think of has hierarchical taxonomies.

(00:51:52):
Most of the times the taxonomies are incredibly messy. I have worked in use cases where you probably have taxonomy that says some kind of hierarchy and then that says shoes and then women's shoes and men's shoes all at the same layer where idea you should be having shoes and then women's shoes and men's shoes should be subclasses. And then you're like, okay, fine. I could just merge that. And you go further and you see that there's also another section on the shoes that says for women and for men, and it's just not aggregated. It's not fixed for some reason. So if an agent kind of sees this kind of a taxonomy, what is it supposed to do? Where is it supposed to route? And a lot of the times we are not aware of these problems until you actually go about building something and understanding it.

(00:52:39):
And when these kind of problems, real human agents see these kind of problems, they know what to check next. Maybe they realize that the node that says for women and for men that's under shoes was last updated in 2019, which means that it's just a dead node that's lying there and not being used. So they kind of know that, okay, we're supposed to be looking at a different node and stuff like that. And I'm not saying agents cannot understand this or models are not capable enough to understand this, but there are really weird rules within enterprises that are not documented anywhere. And you want to make sure that the agents have all of that context instead of just throwing the problem at that.

(00:53:17):
Yeah. Coming back to the versions we had, routing was one where you have really high control because even if your agent routes to the wrong department, humans can take control and undo those actions. And along the way, you also figure out that you probably are dealing with a ton of data issues that you need to fix and make sure that your data layer is good enough for the agent to function. We do is what we said of a Copilot, which is now that you've figured out routing works fine after a few iterations and you've fixed all of your data issues, you could go to the next step, which is, can my agent provide suggestions based on some standard operating procedures that we have for the customer support agent? And it could just generate a draft that the human can make changes to. And when you do this, you're also logging human behavior, which means that how much of this draft was used by the customer support agent or what was omitted. So you're actually getting error analysis for free when you do this because you're literally logging everything that the user is doing that you could then build back into your flywheel.

(00:54:22):
And then we say, post that, once you've figured out that those drafts look good and most of the times maybe humans are not making too many changes, they're using these drafts as is. That's when you want to go to your end-to-end resolution assistant that could draft a resolution that could solve the ticket as well. And those are the stages of agency where you start with low agency and then you go up high. We also have this really nice table that we put together, which is what do you do at each version and what you learn that can enable you to go to the next step and what information do you get that you can feed into the loop, right? When you're just doing your routing, you have better quality routing data, you also know what kind of prompts you need to be building to improve the routing system.

(00:55:09):
Essentially, you're figuring out your structure for context engineering and building that flywheel that you want. And while I go through this, I want to also be very clear that two things. One is when you build with CCCD in mind, it doesn't mean that you've fixed the problem all for one. It's possible that you've probably gone through V3 and you see a new distribution of data that you never previously imagined, but this is just one way to lower your risk, which is you get enough information about how users behave with your system before going to a point of complete autonomy. And the second thing is you're also kind of building this implicit logging system. A lot of people come and tell us that, "Oh, wait, there are evals. Why do you need something like this? " The issue with just building a bunch of evaluation metrics and then having them in production is evaluation metrics catch only the errors that you're already aware of, but there can be a lot of emerging patterns that you understand only after you put things in production.

(00:56:17):
So for those emerging patterns, you're kind of creating a low risk kind of a framework so that you could understand user behavior and not really be in a position where there are tons of errors and you're trying to fix all of them at once. And this is not the only way to do it. There are tons of different ways. You want to decide how you constrain your autonomy. It could be based on the number of actions that the agent is taking, which is what we do in this example. It could be based on topic. There's just some domains where it's pretty high risk to make a system completely autonomous for certain decisions, but for some other topics, it's okay to make them completely autonomous and depending on the complexity of the problem. And that's where you really want your product managers, your engineers and subject matter experts to align on how to build this system and continuously improve it.

(00:57:10):
The idea is just behavior calibration and not losing user trust as you do that behavior calibration, I guess.

Lenny Rachitsky (00:57:17):
We'll link folks to this actual post if they want to go really deep. You basically go through all of these steps by step, a bunch of examples. And the idea here is, as you said, that the reason, everything about what you're describing here is about making it continuous and iterative and kind of moving along this progression of higher autonomy, less control. And this idea of even calling continuous calibration, continuous development is communicating it's this kind of iterative process. And just to be clear, this naming is kind of ode to CI/CD, continuous integration, continuous deployment suite. And the idea here is that this is the version of that for AI where instead of just integrating into unit tests and deploying constantly, it's running evals, looking at results, iterating on the metrics you're watching, figuring out where it's breaking and iterating on that. Awesome. Okay.

(00:58:08):
So again, we'll point people to this post if they want to go deeper. That was a great overview. Is there anything else before we go into different topic around this framework specifically that you think is important for people to know?

Aishwarya Naresh Reganti (00:58:18):
I think one of the most common questions we get is, how do I know if I need to go to the next stage or if this is calibrated enough? There's not really a rule book you can follow, but it's all about minimizing surprise, which means let's say you're calibrating every one or two days and you figure out that you're not seeing new data distribution patterns, your users have been pretty consistent with how they're behaving with the system. Then the amount of information you gain is kind of very low and that's when you know you can actually go to the next stage. And it's all about the wipes at that point, do you know you're ready, you're not receiving any new information. But also it really helps to understand that sometimes there are events that could completely mess up the calibration of your system. An example is GPT-4o doesn't exist anymore, or it's going to be deprecated in APIs as well.

(00:59:16):
So most companies that were using 4o should switch to 5 and 5 has very different properties. So that's where your calibration's off again. You want to go back and do this process again. Sometimes users start behaving with systems also differently over time or user behavior evolves. Even with consumer products, you don't talk to ChatGPT the same way you were talking, say, two years ago, just because you know the capabilities have increased so much. And also just people get excited when these systems can solve one task, they want to try it out on other tasks as well. We built this system for underwriters at some point. Underwriting is a painful task. There are agreements that are like loan applications are like 30 or 40 pages, and the idea for this bank was to build a system that could help underwriters pick policies and information about the bank so that they could approve loans.

(01:00:15):
And for a good three or four months, everybody was pretty impressed with the system. We had underwriters actually report gains in terms of how much time they were spending, et cetera. And first three months, we realized that they were so excited with the product that they started asking very deep questions that we never anticipated. They would just throw the entire application document at the system and go, "For a case that looks like this, what did previous underwriters do? " And for a user, that just seems like a natural extension of what they were doing, but the building behind it should significantly change. Now, you need to understand what does for a case like this mean in the context of the loan itself? Is it referring to people of a particular income range or is it referring to people in a particular geo and stuff like that?

(01:00:58):
And then you need to pick up historical documents, analyze those documents, and then tell them, "Okay, this is what it looks like," versus just saying that there's a policy X, Y, and Z, and you want to look up that policy. So something that might seem very natural to an end user might be very hard to build as a product builder, and you see that user behavior also evolves over time, and that's when you know that you want to go back and recalibrate.

Lenny Rachitsky (01:01:24):
What do you think is overhyped in the AI space right now? And even more importantly, what do you think is under-hyped?

Kiriti Badam (01:01:34):
As I said, super optimistic in different things that are going in AI. So I wouldn't say overhyped, but I feel kind of misunderstood is the concept of multi-agents. People have this notion of, "I have this incredibly complex problem. Now I'm going to break it down into, hey, you are this agent. Take care of this. You're this agent. Take care of this." And now if I somehow connect all of these agents, they think they're the agent utopia and it's never the case that there are incredibly successful multi-agent systems that are built. There's no doubt about that. But I feel a lot of it comes in terms of how are you limiting the ways in which the system can go off tracks. And for example, if you're building a supervisor agent and there are subagents that actually do the work for the super agent, supervisor agent, that is a very successful pattern.

(01:02:24):
But coming with this notion of I'm going to divide the responsibilities based on functionality and somehow expect all of that to work together in some sort of gossip protocol, that is extremely misunderstood that you could do that. I don't think current ways of building and current model capabilities are right there in terms of building those kind of applications. I feel that is kind of misunderstood than overrated. Underrated, I feel it's hard to probably believe, but I still feel coding agents are underrated in the sense that I feel like you can go on Twitter and you can go on Reddit and you see a lot of chatter about coding agents, but talking to an engineer in any random company, especially outside of Bay Area, you can see the amount of impact this coding agents can create and the penetration is very low. So I feel like 2025 and 2026 is going to be an incredible year for optimizing all of these processes.

(01:03:25):
And I feel that is going to be creating a lot of value with AI.

Lenny Rachitsky (01:03:28):
That's really interesting on that first point. So the idea there is you'll probably be more successful building and using an agent that is able to do its own sub-agent splitting of work versus a bunch of, say, Codex agents. Will you do this task, you do that task?

Kiriti Badam (01:03:44):
You can have agents to do these things and you as a human can orchestrate it or you can have one larger agent that is going to orchestrate all of these things, but letting the agents communicate in terms of peer-to-peer kind of protocol, and then especially doing this in a customer support kind of use case is incredibly hard to control what kind of agent is replying to your customer because you need to shift your guardrails everywhere and things like that.

Lenny Rachitsky (01:04:08):
Yeah. Okay. Great picks. Okay. Ash, what do you got?

Aishwarya Naresh Reganti (01:04:12):
Can I say evals? Will I be canceled?

Lenny Rachitsky (01:04:15):
In which category? Which bucket do they go?

Aishwarya Naresh Reganti (01:04:18):
Overrated.

Lenny Rachitsky (01:04:20):
Overrated. Okay, go for it. We won't let you get canceled.

Aishwarya Naresh Reganti (01:04:22):
Just kidding. I think evals are misunderstood. They are important, folks. I'm not saying they're not important, but I think just this, I'm going to keep jumping across tools and going to pick up and learn if new tool is overrated. I still am old school and feel like you would really need to be obsessed with the business problem you're trying to solve. AI is only a tool. I try to think of it that way. Of course, you need to be learning about the latest and greatest, but don't be so obsessed with just building so quickly. Building is really cheap today. Design is more expensive, really thinking about your product, what you're going to build. Is it going to really solve a pain point? Is what is way more valuable today? And it will only become more true in the near future. So really obsessing about your problem and design is underrated and just rote building is overrated, I guess.

Lenny Rachitsky (01:05:15):
Awesome. Okay. Similar sort of question. From a product point of view, what do you think the next year of AI is going to look like? Give us a vision of where you think things are going to go by, say by the end of 2026.

Kiriti Badam (01:05:30):
Yeah, I feel there's a lot of promise in terms of this background agents are proactive agents who is ... They're going to basically understand your workflow even more. If you think of where is AI failing to create value today, it's mainly about not understanding the context. And the reason that it's not understanding the context is it's not plugged into the right places where actual work is happening. And as you do more of this, you can give the agent more of context and then it start to see the world around you and understand what are the set of metrics that you're optimizing for or what are the kind of activities that you're trying to do. It is a very easy extension from there to actually gain more out of it and then let the agent prompt you back. We already do this in terms of ChatGPT pulse, which kind of gives you this daily update of things you might care about.

(01:06:20):
And it's very nice to actually have that jog your brain up in terms of, "Oh, this is something that I haven't thought about. Maybe this is good." And now when you extend this to more complex tasks, like a coding agent, which says that, "Okay, I have fixed five of your linear tickets and here are the patches. Just to review them at the start of your day." So I feel that is going to be extremely useful. And I see that as a strong direction in which products are going to build in 2026.

Lenny Rachitsky (01:06:44):
That's so cool. So essentially agents anticipating what you want to do and getting ahead of you and I've solved these problems for you or I think this is going to crash your site. Maybe you should fix this thing right here or I see the spike here and let's refactor our database. Amazing. What a world. Okay. Ash, what do you got?

Aishwarya Naresh Reganti (01:07:04):
I'm all in for multimodal experiences in 2026. I think we have done quite some progress in 2025, and not just in terms of generation, but also understanding. Until now, I think LLMs have been our most commonly used modules, but as humans, we are multimodal creatures, I would say. Language is probably one of our last forms of evolution. As the three of us are talking, I think we're constantly getting so many signals. I'm like, "Oh, Lenny's nodding his head, so probably I would go in this direction or Lenny's bored, so let me stop talking." So there's a chain of thought behind your chain of thought and you're constantly altering it with language that dimension of expression is not explored as well. So if we could build better multimodal experiences that would get us closer to human-like conversation richness. And you will also, just given the kind of models, there's a bunch of boring tasks as well, which are ripe for AI.

(01:08:04):
If multimodal understanding gets better, there are so many handwritten documents and really messy PDFs that cannot be passed even by the best of the models as of today. And if it's possible, there'll be so much data that we can tap into.

Lenny Rachitsky (01:08:21):
Awesome. I just saw Demis from DeepMind, AI, Google, whatever they call the whole org, talking about this where he thinks that's going to be a big part of where they're going, combining the image model work, the LLM, and also their world model stuff, Genie, I think is what it's called. Yes. So that's going to be a wild, wild time. Okay. Last question. If someone wants to just get better at building AI products, what's just maybe one skill or maybe two skills that you think they should lean into and develop?

Aishwarya Naresh Reganti (01:08:52):
I think we did cover a bunch of best practices for AI products, which is start small, try to get your iteration going well and build a flywheel and all of that. But again, if you kind of look at it at a 10,000 feet level for anybody building today, like I was saying, implementation is going to be ridiculously cheap in the next few years. So really nail down your design, your judgment, your taste and all of that. And in general, if you're building a career as well, I feel for the past few years, your former years, say the first two, three years of building your career is always focused on execution, mechanics and all of that. And now we have AI that could help you ramp pretty quickly and post that. I mean, after a few years, I think everybody's job becomes about your taste, your judgment and kind of what is uniquely you.

(01:09:49):
I think nail down on that part and try to figure out how you can bring in that kind of a perspective. It doesn't have to mean that you should be significantly old, have years of experience. We recently hired someone and we use this very popular app for tracking our tasks and we've been using it for years and we pay a high subscription fee for it. And this guy just came with his own vibe coded app to the meeting. He onboarded us to all of it and he's like, "Okay, let's start using this." And I think that kind of agency and that kind of ownership to really rethink experiences is what will set people apart. And I'm not being blind to the fact that vibe coded apps have high maintenance costs. And maybe as we scale as a company, we have to replace it or we have to think of better approaches.

(01:10:36):
But given that we are a small size company now and just ... I was really shocked because I never thought of it. If you've been used to working in a certain way, you associate a cost with building. And I feel like folks who grew up in this age have a much lower cost associated in their mind. They just don't mind building something and going ahead with it. And they're also very enthusiastic to try out new tools. That's also probably why AI products have this retention problem because everybody's so excited about trying out these new tools and all of that. But essentially having the agency and ownership, and I think it's also the going to be the end of the busy work era. You can't be sitting in a corner doing something that doesn't move the needle for a company. You really need to be thinking about end-to-end workflows, how you can bring in more impact.

(01:11:26):
I think all of that will be super important.

Lenny Rachitsky (01:11:28):
That reminds me, I just had Jason Lemkit on the podcast. He's very smart on sales, go to market, run Saster, and he replaced his whole sales team with agents. He had 10 salespeople and then he was 1.2 and 20 agents. And one of the agents, it was just tracking everyone's updates to Salesforce and kind of updating it automatically for them based on their calls. And one of the salespeople was like, "Okay, I quit." And it turned out he wasn't really doing anything. He was just sitting around and he's like, "Okay, this will catch me. I got to get out of here. So to your point about, it'll be harder to sit around and twiddle your thumbs, I think is really right.

Kiriti Badam (01:12:07):
Yeah. I think to add on to that, I feel like persistence is also something that is extremely valuable, especially given that anybody who wants to build something, the information is at your fingertips even more than the past decade. You can learn anything overnight and become that sort of Ironman kind of approach. So I feel like having that persistence and going through the pain of learning this, implementing this and understanding what works and what doesn't work. And as you are going through this pain of developing multiple approaches and then solving the problem, I feel that is going to be the real moat as an individual. I like to call it pain is the new moat, but I feel that is exactly super useful to actually have this in, especially in building these AI products.

Lenny Rachitsky (01:12:56):
Say more about this. I love this concept. Pain is the new moat. Is there more there?

Kiriti Badam (01:13:00):
Yeah, I feel as a company, I mean, successful companies right now building in any new area, they are successful not because they're first to the market or they have this fancy feature that more customers are liking it. They went through the pain of understanding what are the set of non-negotiable things and trade them off exactly with what are the features or what are the model capabilities that they can use to solve that problem. This is not a straightforward process. There's no textbook to do this or there's no straightforward way or a known credit path to be here. So a lot of this pain I was talking about is just going through this iteration of like, "Okay, let's try this and if this doesn't work, let's try this." And that kind of knowledge that you built across the organization or across your own lived experiences, I feel that pain is what translates into the moat of the company. This could be a product of evals or something that you built. And I feel that is going to be the game changer.

Lenny Rachitsky (01:13:59):
That is awesome. It's like turning a coal into diamond.

Kiriti Badam (01:14:03):
Yes.

Lenny Rachitsky (01:14:04):
Okay. I feel like we've done a great job helping people avoid some of the biggest issues people consistently run into building AI products. We covered so many of the pitfalls and the ways to actually do it correctly. Before we get to our very exciting lightning round, is there anything else that you wanted to share? Anything else you want to leave listeners with?

Aishwarya Naresh Reganti (01:14:25):
Be obsessed with your customers. Be obsessed with the problem. AI is just a tool and try to make sure that you're really understanding your workflows. 80% of so called AI engineers, AIPMs spend their time actually understanding their workflows very well. They're not building the fanciest and the most cool models or workflows around it. They're actually in the weeds understanding their customer's behavior and data. And whenever a software engineer who's never done AI before, here's the term, look at your data. I think it's a huge revelation to them, but it's always been the case. You need to go there, look at your data, understand your users, and that's going to be a huge differentiator.

Lenny Rachitsky (01:15:09):
That's a great way to close it. The AI isn't the answer. It's a tool to solve the problem. With that, we have reached our very exciting lightning round. I've got five questions for both of you. Are you ready?

Aishwarya Naresh Reganti (01:15:22):
Yay. Yes.

Lenny Rachitsky (01:15:24):
All right. So you can both answer them. You can pick one which you want to answer. Either way, up to you. What are two or three books you find yourself recommending most to other people?

Aishwarya Naresh Reganti (01:15:32):
For me, it's this book called When Breath Becomes Air, Lenny. It was written by Paul Kalanithi. I think he was an Indian original neurosurgeon who was diagnosed with lung cancer at 31 or 32. And the whole book is his memoir and just is written after he was diagnosed. And it's really beautiful, especially because I read it during COVID and all we ever wanted to do during COVID is stay alive. There are a bunch of really nice quotes within the book as well, but I remember one of them, he was kind of arguing against a very popular quote by Socrates, which is, "The unexamined life is not worth living," or something like that, which means you really need to be thinking about your choices, you need to understand your values, your mission and all of that. And Paul says, "If the unexamined life is not worth living, was the unlived life worth examining?" Which means are you spending so much time just understanding your mission and purpose that you've forgotten to live?

(01:16:32):
And I think everybody who's staying in the AI era and building and continuously going through the space of reinventing themselves need to take a pause and live for a bit, I guess. They need to stop evaling life too much.

Lenny Rachitsky (01:16:46):
I was going to say that. That's where my mind went. You got to write some evals for your life. Oh my God, we've gone too far.

Aishwarya Naresh Reganti (01:16:52):
Yep. Yeah.

Lenny Rachitsky (01:16:53):
Beautiful.

Aishwarya Naresh Reganti (01:16:53):
That's my favorite book.

Kiriti Badam (01:16:55):
I like more of science fiction books. So I really like this 3 Body problem series. It's like a three book series. It has elements of grander than science fiction, life outside earth and how it impacts human decision making process. And it also has elements of geopolitics and how much important or valuable abstract science is to human progress. And then when that gets stopped, it's not noticeable in everyday life, but it can cause devastating effects. So I feel like AI helping in these areas, for example, is going to be extremely crucial. And that book is a nice example of what could happen otherwise.

Lenny Rachitsky (01:17:35):
Completely agree. Absolutely. Love. Might be my favorite sci-fi book except, or series even, and it's three. I have to read of all three, by the way. I find that it only got really good about one and a half books in. So if anyone's tried it and like, "What the heck is going on here?" Just keep reading and get to the middle of the second one and then it gets mind-blowing.

Kiriti Badam (01:17:52):
Yes.

Lenny Rachitsky (01:17:54):
If you love sci-fi and you're in AI, you got to read this book called A Fire Upon the Deep by Vernon Vinge. Check it out. It's incredible. I saw Noah Smith on his newsletter recommend this book and there's sequels to it, but this is the one that's so incredible. And it's actually, it turns out it's about AGI and super intelligence and all these things, and it's just so epic. And no one's heard of it.

Kiriti Badam (01:18:19):
Thank you.

Lenny Rachitsky (01:18:20):
There you go. I'm giving you one back. Okay, next question. What's a favorite recent movie or TV show that you've really enjoyed?

Aishwarya Naresh Reganti (01:18:26):
I started rewatching Silicon Valley and I think it's so true. It's so timeless. Everything is repeating all over again. Anybody who's watched it a few years ago should start rewatching it and you'll see that it's eerily similar to everything that's happening right now with the AI wave.

Lenny Rachitsky (01:18:41):
That's a good idea to rewatch it. I love that their whole business was like an algorithm to compress, like a compression algorithm. It's like maybe a precursor to LLMs in some small way. No, I get it. All right, Kiriti, what you got?

Kiriti Badam (01:18:54):
I'm going to drag this and say lot a movie or a TV show, but there's this game I picked up recently called Expedition 33. It has nothing to do with AI, but it's an incredibly well-made game in terms of the gameplay or the movie and the story and the music. It's been amazing.

Lenny Rachitsky (01:19:10):
I love that you have time to play games. That's a great sign. I love that. Someone OpenAI, I'm just imagining you're ... There's nothing else going on except just coding and having meetings.

Kiriti Badam (01:19:20):
Yeah, it has been incredibly hard to find time for that.

Lenny Rachitsky (01:19:22):
That's good. That's a good sign. I'm happy to hear this. Okay. What's a favorite product that you've recently discovered that you really love?

Aishwarya Naresh Reganti (01:19:28):
For me, it's Whisper Flow. I think I've been using it quite a bit and I didn't know I needed it so much. The best part is it's a conceptual transcription tool, which means if you go to Codex and start using Whisper Flow, it starts identifying variables and all of that. And it's so seamless in terms of transcription to instruction. You could say something like, "I'm so excited today. Add three exclamation marks," and it seamlessly switches. It adds those three exclamation marks instead of writing add three exclamation marks. And I think it's pretty cool. If you're not using it, you should try it.

Lenny Rachitsky (01:20:03):
I'll do a plug. Get Whisper Flow for free for an entire year for a year for free by becoming an annual subscriber of my newsletter.

Aishwarya Naresh Reganti (01:20:12):
That's how I got access to it, Lenny.

Lenny Rachitsky (01:20:14):
There we go. I think I pitched this deal. I think people don't truly understand how incredible this is. They're like, "No way this is real. It's real." And 18 other products, lennysproductpass.com, check it out. Moving on. Kiriti.

Kiriti Badam (01:20:28):
Awesome. I actually am a stickler for productivity. I keep experimenting new CLI tools and things which can make me faster. So I feel like a Raycast has been amazing. I've discovered all this new shortcuts that you can use to open different things, type in shortcut commands and things like that. And Caffeinate is another thing that I've recently discovered from my teammates. It helps you prevent Mac from sleeping so you can run this really long Codex task for four or five hours locally, let it build the thing and then you can wake up and be like, "Okay, this is good. I like this."

Lenny Rachitsky (01:21:02):
That's hilarious, that combo. Codex and Caffeinate. You guys need to use it, build that yourself, an OpenAI version of that, or the Codex agent should just keep your Mac from sleeping. That's so funny. By the way, Raycast, also part of Lenny's product pass. One year for your Raycast. Amazing. Yeah.

Aishwarya Naresh Reganti (01:21:20):
Lenny didn't tell us these folks. Yes. These are actually our favorite products.

Lenny Rachitsky (01:21:25):
These are just two of 19 products. No Caffeinate though. I don't know if that's even paid. Okay, let's keep going. Do you have a favorite life motto that you find yourself coming back to in work or in life?

Aishwarya Naresh Reganti (01:21:35):
For me, I think this is one my dad told me when I was a kid and it's always stuck, which is they told it couldn't be done, but the fool didn't know it, so he did it anyway. I think be foolish enough to believe that you can do anything if you put your heart to it, especially now because you have so much data at your hand that could be pointing towards the fact that you probably will be unsuccessful. How many podcasts made it to more than a thousand subscribers or how many companies hit more than one million ARR? And there's always data to show you that you won't be successful, but sometimes just be foolish and go ahead with it.

Lenny Rachitsky (01:22:12):
That's great. Yeah.

Kiriti Badam (01:22:13):
For me, I am more of an overthinker. So I really like this quote from Steve Jobs that you can only connect the dots looking backwards. So a lot of the times there are numerous choices and you don't really know the optimal one to pick, but life works in ways that you can actually see back and be like, "Oh, these are actually beautiful in terms of how our transition." So I feel like that is extremely useful in keep moving forward, keep experimenting.

Lenny Rachitsky (01:22:39):
Final question. Whenever I have two guests on the podcast at once, I like to ask this question. What's something that you admire about the other person?

Aishwarya Naresh Reganti (01:22:48):
I think with Kiriti, he's pretty calm and very grounded and he's always been my sounding board. I can throw a ton of ideas at him and he always comes up with, he's able to anticipate the kind of issues that might land into. And he's extremely kind and lets his work speak instead of actually doing a lot of talking, I guess. But if I had to pick one, I think he's the most incredible husband.

Lenny Rachitsky (01:23:20):
Reveal. Little did people know.

Aishwarya Naresh Reganti (01:23:25):
We've been married for four years and been the most beautiful four years of my life.

Lenny Rachitsky (01:23:31):
Wow. Okay. How do you follow that?

Kiriti Badam (01:23:34):
Yeah, it's super hard to follow that. I would say I am extremely privileged in terms of working with really smart people in great companies in the Silicon Valley. And I feel the unique thing that stands with Aishwarya across like any other smart folks I've worked on is she has this really amazing knack of teaching and explaining something in a very understandable and easy to comprehend way. And that combined with persistence is super useful, especially in this fast-moving AI world that we are in the sense that there's so many new things coming up. It feels overwhelming, but when I hear her talk about, this is how you make sense of this entire thing, this is where it plugs in. I feel like, oh, that is so simple. I can also do that. So she empowers a lot of people by simplifying things and explaining things in the most understandable way.

(01:24:25):
So I feel that is an incredible quality.

Lenny Rachitsky (01:24:27):
Amazing. How sweet. I got to do this all the time. I need more guest to do it. That was great. Okay. Final questions. Where can folks find stuff that you're working on, find you online, share your course link, and then just how can listeners be useful to you?

Aishwarya Naresh Reganti (01:24:41):
I write a lot on LinkedIn. So if you want to listen to pragmatists who've been in the weeds, working on AI products and what they're seeing, you can follow my work. We also have a GitHub repository with about 20K stars, and that repository is all about good resources for learning AI. It's completely free. And if you like what we spoke today, we also run a super popular course. We leave a link to it on building enterprise AI products. And the course is a lot about unlearning mindsets and following a problem-first approach instead of a tool-first or a hype-first approach. So you can check that out as well. And if you don't want to do the course, we write a lot, we give out a lot of free resources, we have free sessions, so make sure you follow our work.

Kiriti Badam (01:25:27):
Yeah, I would also add that you can also find me on LinkedIn. I don't write a lot, I guess, but I'm super all excited to just talk to any complex product that you're building. And if you have thoughts on how you can use coding agents to make your life better or however the problems that you're seeing, always my DMs are open and we can have a great discussion.

Lenny Rachitsky (01:25:47):
Awesome. Well, Kiriti and Ash, thank you so much for being here.

Kiriti Badam (01:25:52):
Thank you so much.

Aishwarya Naresh Reganti (01:25:53):
Thank you, Lenny. This was so much fun.

Lenny Rachitsky (01:25:54):
So much fun. Bye, everyone.

(01:25:58):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

