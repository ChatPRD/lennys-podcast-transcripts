---
guest: Alexander Embiricos
title: How to drive word of mouth | Nilan Peiris (CPO of Wise)
youtube_url: https://www.youtube.com/watch?v=xZifSLGOrrw
video_id: xZifSLGOrrw
description: 'Nilan Peiris is Chief Product Officer at Wise, one of the fastest-growing
  (and profitable) tech companies in the world. Wise allows anyone to send money in
  more than 60 currencies to over 160...

  '
duration_seconds: 4594.0
duration: '1:16:34'
view_count: 13919
channel: Lenny's Podcast
keywords:
- growth
- retention
- roadmap
- prioritization
- hiring
- team building
- culture
- strategy
- vision
- mission
- market
- persona
- design
- ux
- ui
---

# How to drive word of mouth | Nilan Peiris (CPO of Wise)

## Transcript

Lenny Rachitsky (00:00:00):
You lead work on Codex.

Alexander Embiricos (00:00:01):
Codex is OpenAI's coding agent. We think of Codex as just the beginning of a software engineering teammate. It's a bit like this really smart intern that refuses to read Slack, doesn't check Datadog unless you ask it to.

Lenny Rachitsky (00:00:12):
I remember Karpathy tweeted the gnarliest bugs that he runs into that he just spends hours trying to figure out nothing else has solved, he gives it to Codex, lets it run for an hour and it solves it.

Alexander Embiricos (00:00:21):
Starting to see glimpses of the future where we're actually starting to have Codex be on call for its own training. Codex writes a lot of the code that helps manage its training run, the key infrastructure. So we have a Codex code review that's catching a lot of mistakes. It's actually caught some pretty interesting configuration mistakes. One of the most mind-blowing examples of acceleration, the Sora Android app, like a fully new app, we built it in 18 days and then 10 days later, so 28 days total, we went to the public.

Lenny Rachitsky (00:00:45):
How do you think you win in this space?

Alexander Embiricos (00:00:47):
One of our major goals with Codex is to get to proactivity. If we're going to build a super system, has to be able to do things. One of the learnings over the past year is that for models to do stuff, they're much more effective when they can use a computer. It turns out the best way for models to use computers is simply to write code. And so we're kind of getting to this idea where if you want to build any agent, maybe you should be building a coding agent.

Lenny Rachitsky (00:01:04):
When you think about progress on Codex, I imagine you have a bunch of evals and there's all these public benchmarks.

Alexander Embiricos (00:01:10):
A few of us are constantly on Reddit. There's praise up there and there's a lot of complaints. What we can do is as a product team just try to always think about how are we building a tool so that it feels like we're maximally accelerating people rather than building a tool that makes it more unclear what you should do as the human?

Lenny Rachitsky (00:01:24):
Being at OpenAI, I can't not ask about how far you think we are from AGI.

Alexander Embiricos (00:01:28):
The current underappreciated limiting factor is literally human typing speed or human multitasking speed.

Lenny Rachitsky (00:01:35):
Today, my guest is Alexander Embiricos, product lead for Codex, OpenAI's incredibly popular and powerful coding agent. In the words of Nick Turley, head of ChatGPT and former podcast guest, "Alex is one of my all time favorite humans I've ever worked with, and bringing him and his company into OpenAI ended up being one of the best decisions we've ever made." Similarly, Kevin Weil, OpenAI's CPO, said, "Alex is simply the best."

(00:01:59):
In our conversation, we chat about what it's truly like to build product at OpenAI, how Codex allowed the Sora team to ship the Sora app, which became the number one app in the app store in under one month. Also, the 20x growth Codex is seeing right now and what they did to make it so good at coding, why his team is now focused on making it easier to review code, not just write code, his AGI timelines, his thoughts on when AI agents will actually be really useful, and so much more. A huge thank you to Ed Bayes, Nick Turley, and Dennis Yang for suggesting topics for this conversation. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. And if you become an annual subscriber of my newsletter, you get a year free of 19 incredible products, including a year free of Devin, Lovable, Replit, Bolt, n8n, Linear, Superhuman, Descript, Wispr Flow, Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, Mobbin, PostHog, and Stripe Atlas. Head on over to lennysnewsletter.com and click Product Pass.

(00:02:55):
With that, I bring you Alexander Embiricos, after a short word from our sponsors.

(00:03:00):
Here's a puzzle for you. What do OpenAI, Cursor, Perplexity, Vercel, Plaid, and hundreds of other winning companies have in common? The answer is they're all powered by today's sponsor, WorkOS. If you're building software for enterprises, you've probably felt the pain of integrating single sign-on, SCIM, RBAC, audit logs, and other features required by big customers. WorkOS turns those deal blockers into drop-in APIs with a modern developer platform built specifically for B2B SaaS. Whether you're a seed stage startup trying to land your first enterprise customer or a unicorn expanding globally, WorkOS is the fastest path to becoming enterprise ready and unlocking growth. They're essentially Stripe for enterprise features. Visit workos.com to get started or just hit up their Slack support where they have real engineers in there who answer your questions super fast. WorkOS allows you to build like the best, with delightful APIs, comprehensive docs and a smooth developer experience. Go to workos.com to make your app enterprise ready today.

(00:04:01):
This episode is brought to you by Fin, the number one AI agent for customer service. If your customer support tickets are piling up, then you need Fin. Fin is the highest performing AI agent on the market with a 65% average resolution rate. Fin resolves even the most complex customer queries. No other AI agent performs better. In head to head bake offs with competitors, Fin wins every time. Yes, switching to a new tool can be scary, but Fin works on any help desk with no migration needed, which means you don't have to overhaul your current system or deal with delays in service for your customers. And Fin is trusted by over 6,000 customer service leaders and top companies like Anthropic, Shutterstock, Synthesia, Clay, Vanta, Lovable, Monday.com and more. And because Fin is powered by the Fin AI Engine, which is a continuously improving system that allows you to analyze, train, test, and deploy with ease, Fin can continuously improve your results too. So if you're ready to transform your customer service and scale your support, give Fin a try for only 99 cents per resolution. Plus Fin comes with a 90-day money back guarantee. Find out how Fin can work for your team at fin.ai/Lenny. That's fin.ai/lenny.

(00:05:14):
Alexander, thank you so much for being here and welcome to the podcast.

Alexander Embiricos (00:05:18):
Thank you so much. I've been following for ages and I'm excited to be here.

Lenny Rachitsky (00:05:21):
I'm even more excited. I really appreciate that. I want to start with your time at OpenAI. So you joined OpenAI about a year ago. Before that, you had your own startup for about five years. Before that, you were a product manager at Dropbox. I imagine OpenAI is very different from every other place you've worked. Let me just ask you this, what is most different about how OpenAI operates and what's something that you've learned there that you think you're going to take with you wherever you go, assuming you ever leave?

Alexander Embiricos (00:05:49):
By far, I would say the speed and ambition of working at OpenAI are just dramatically more than what I can imagine. And I guess it's kind of an embarrassing thing to say because everyone who's a startup founder thinks like, "Oh yeah, my startup moves super fast and the talent bar is super high and we're super ambitious." But I have to say, working in OpenAI just made me reimagine what that even means.

Lenny Rachitsky (00:06:11):
We hear this a lot about feels like every AI company is just like, "Oh my God, I can't believe how fast they're moving." Is there an example of just like, "Wow, that wouldn't have happened this quickly anywhere else"?

Alexander Embiricos (00:06:20):
The most obvious thing that comes to mind is just the explosive growth of Codex itself. I think it's a while since we bumped our external number, but it's like the 10x-ing of Codex's scale was just super fast in a matter of months and it's well more since then. And once you've lived through that, or at least speaking for myself, having lived through that now, I feel like anytime I'm going to spend my time on building tech product, there's that speed and scale that I now need to meet.

(00:06:52):
If I think of what I was doing in my startup, it moved way slower and there's always this balance with startups of how much do you commit to an idea that you have versus find out that it's not working and then pivot. But I think one thing I've realized at OpenAI is the amount of impact that we can have and, in fact, need to have to do a good job is so high that I have to be way more ruthless with how I spend my time now.

Lenny Rachitsky (00:07:15):
Before we get to Codex, is there a way that they've structured the org or, I don't know, the way that OpenAI operates that allows the team to move this quickly? Because everyone wants to move super fast. I imagine there's a structural approach to allowing this to happen.

Alexander Embiricos (00:07:29):
I mean, so one thing is just the technology that we're building with has just transformed so many things from both how we build, but also what kinds of things we can enable for users. And we spend most of our time talking about the sort of improvements within the foundation models, but I believe that even if we had no more progress today with models, which is absolutely not the case, but even if we had no more progress, we are way behind on product. There's so much more product to build. So I think just the moment is ripe, if that makes sense.

(00:08:01):
But I think there's a lot of counterintuitive things that surprised me when I arrived as far as how things are structured. One example that comes to mind is when I was working on my startup and before that, when I was at Dropbox, it was very important, especially as a PM to always rally the ship and it was like make sure you're pointed in the right direction and then you can accelerate in that direction. But here, I think because we don't exactly know what capabilities will even come up soon and we don't know what's going to work technically, and then we also don't know what's going to land even if it works technically, it's much more important for us to be very humble and learn a lot more empirically and just try things quickly. And the org is set up in that way to be incredibly bottoms up.

(00:08:45):
This is, again, one of those things that, as you were saying, everyone wants to move fast. I think everyone likes to say that they're bottoms up, or at least a lot of people do, but OpenAI is truly, truly bottoms up. And that's been a learning experience for me that now it'll be interesting if I ever work at... I don't think it'll even make sense to work at a non-AI company in the future. I don't even know what that means. But if I were to imagine it or go back in time, I think I would run things totally new.

Lenny Rachitsky (00:09:10):
What I'm hearing is this ready, fire, aim is the approach more than ready, aim, fire. And there's something, and as you process that, because that may not come across well, but I actually have heard this a lot at AI companies is because you don't know, and Nick Turley shared I think the same sentiment, because you don't know how people will use it it doesn't make sense to spend a lot of time making it perfect. It's better to just get it out there in a primordial way, see how people use it, and then go big on that use case.

Alexander Embiricos (00:09:39):
Yeah. Okay, to use this analogy a little bit, I feel like there is an aim component, but the aim component is much fuzzier. It's kind of like, roughly what do we think can happen? Someone I've learned a ton from working here is a research lead, and he likes to say that at OpenAI, we can have really good conversations about something that's a year plus from now, and there's a lot of ambiguity in what will happen, but that's a right sort of timeline. And then we can have really good conversations about what's happening in low months or weeks. But there's this awkward middle ground, which was as you start approaching a year, but you're not at a year where it's very difficult to reason about, right?

(00:10:18):
And so as far as aiming, I think we want to know, "Okay, what are some of the futures that we're trying to build towards?" And a lot of the problems we're dealing with in AI, such as alignment are problems you need to be thinking out really far out into the future. So we're kind of aiming fuzzily there, but when it comes down to the more tactically like, "Oh yeah, what product will we build and therefore how will people use that product?" That's the place where we're much more like, "Let's find out empirically."

Lenny Rachitsky (00:10:41):
That's a good way of putting it. Something else that when people hear this, people sometimes hear companies like yours saying, "Okay, we're going to be bottoms up. We're going to try a bunch of stuff. We're not going to have exactly a plan of where it's going in the next few months." The key is you all hire the best people in the world. And so that feels like a really key ingredient in order to be this successful at bottoms up work.

Alexander Embiricos (00:11:02):
It just super resonates with me. I was just, again, surprised or even shocked when I arrived at the level of individual drive and autonomy that everyone here has. So I think the way that OpenAI runs, you can't read this or listen to a podcast and be like, "I'm just going to deploy this to my company." Maybe this is a harsh thing to say, but I think very few companies have the talent caliber to be able to do that. So it might need to be adjusted if you were going to implement this.

Lenny Rachitsky (00:11:34):
Okay. So let's talk Codex. You lead work on Codex. How's Codex going? What numbers can you share? Is there anything you can share there? Also, just not everyone knows exactly what Codex is, explain what Codex is.

Alexander Embiricos (00:11:45):
Totally, yeah. So I had the very lucky job of living in the future and leading products on Codex. And Codex is OpenAI's coding agent. So super concretely, that means it's an IDE extension, a VS code extension that you can install or a terminal tool that you can install. And when you do so, you can then basically pair with Codex to answer questions about code, write code, run tests, execute code, and do a bunch of the work in that thick middle section of the software development lifecycle, which is all about writing code that you're going to get into production.

(00:12:21):
More broadly, we think of Codex as what it currently is just the beginning of a software engineering teammate. So when we use a big word like teammate, some of the things we're imagining are that it's not only able to write code, but actually it participates early on in the ideation and planning phases of writing software and then further downstream in terms of validation, deploying and maintaining code.

(00:12:46):
To make that a little more fun, one thing I like to imagine is if you think of what Codex is today, it's a bit like this really smart intern that refuses to read Slack and doesn't check Datadog or Century unless you ask it to. And so no matter how smart it is, how much are you going to trust it to write code without you also working with it? So that's how people use it mostly today is they pair with it. But we want to get to the point where it can work just like a new intern that you hire, you don't only ask them to write code, but you ask them to participate across the cycle. So you know that even if they don't get something right the first try, they're eventually going to be able to iterate their rate there.

Lenny Rachitsky (00:13:21):
I thought the point about not reading Slack and Datadog was it's just not distracted, it's just constantly focused and is always in flow. But I get what you're saying there is it doesn't have all the context on everything that's going on.

Alexander Embiricos (00:13:31):
Yeah. And that's not only true when it's performing a task, but again, if you think of the best team and teammates, you don't tell them what to do. Maybe when you first hire them, you have a couple meetings and you're like, "Hey," you learn, "Okay, these prompts work for this teammate, these prompts don't. This is how to communicate with this person." Then eventually you give them some starter tasks, you delegate a few tasks. But then eventually you just say like, "Hey, great. Okay, you're working with this set of people in this area of the code base. Feel free to work with other people on other parts of the code base too, even. And yeah, you tell me what you think makes sense to be done." And so we think of this as proactivity and one of our major goals with Codex is to get to proactivity.

(00:14:09):
I think this is critically important to achieve the mission of OpenAI, which is to deliver the benefits of AGI to all humanity. I like to joke today that AI products, and it's a half joke, they're actually really hard to use because you have to be very thoughtful about when it could help you. And if you're not prompting a model to help you, it's probably not helping you at that time. And if you think of how many times the average user is prompting AI today, it's probably tens of times. But if you think of how many times people could actually get benefit from a really intelligent entity, it's thousands of times per day. And so a large part of our goal with Codex is to figure out what is the shape of an actual teammate agent that is helpful by default.

Lenny Rachitsky (00:14:54):
When people think about Cursor and even Cloud Code, it's like a IDE that helps you code and auto completes code and maybe does some agentic work. What I'm hearing here is the vision is different, which is it's a teammate. It's like a remote teammate, a building code for you that you talk to and ask to do things. And that also does IDE, auto complete and things like that. Is that a kind of a differentiator in the way you think about Codex?

Alexander Embiricos (00:15:18):
It's basically this idea that if you're a developer and you're trying to get something done, we want you to just feel like you have superpowers and you're able to move much, much faster. But we don't think that in order for you to reap those benefits, you need to be sitting there constantly thinking about, "How can I invoke AI at this point to do this thing?" We want you to be able to plug it in to the way that you work and have it just start to do stuff without you having to think about it.

Lenny Rachitsky (00:15:44):
Okay. I have a lot of questions along those lines, but just how's it going? Is there any stats, any numbers you can share about how Codex is doing?

Alexander Embiricos (00:15:49):
Yeah, Codex has been growing absolutely explosively since the launch of GPT-5 back in August. There's definitely some interesting product insights to talk about as to how we unlock that growth, if you're interested. But again, the last stat we shared there was we were well over 10x since August. In fact, it's been 20x since then. Also, the Codex models are serving many trillions of tokens a week now, and it's basically our most served coding model. One of the really cool things that we've seen is that the way that we decided to set up the Codex team was to build a really tightly integrated product and research team that are iterating on the model and the harness together. And it turns out that lets you just do a lot more and try many more experiments as to how these things will work together.

(00:16:35):
And so we were just training these models for use in our first party harness that we were very opinionated about. And then what we've started to see more recently actually is that other major API coding customers are now starting to adopt these models as well. And so we've reached a point where actually the Codex model is the most served coding model in the API as well.

Lenny Rachitsky (00:16:55):
You hinted at this, what unlocked this growth, I'm extremely interested in hearing that. It felt like before, I don't know, maybe this was before you joined the team, it just felt like Cloud Code was killing it. Just everyone was sitting on top of Cloud Code. It was by far the best way to code. And then all of a sudden Codex comes around. I remember Karpathy tweeted that he just has never seen a model like this. I think the tweet was the gnarliest bugs that he runs into that he just spends hours trying to figure out nothing else has solved, he gives it to Codex, lets it run for an hour and it solves it. What'd you guys do?

Alexander Embiricos (00:17:30):
We have this strong sort of mission here at OpenAI basically to build AGI. And so we think a lot about how can we shape the product so that it can scale. Earlier I was mentioning like, "Hey, if you're an engineer, you should be getting help from AI thousands of times per day," and so we thought a lot about the primitives for that when we launched our first version of Codex, which was Codex Cloud. And that was basically a product that had its own computer, lived in the cloud, you could delegate to it. And the coolest part about that is you could run many, many tasks in parallel. But some of the challenges that we saw are that it's a little bit harder to set that up, both in terms of environment configuration, like giving the model the tools it needs to validate its changes and to learn how to prompt in that way.

(00:18:20):
My analogy for this is, going back to this teammate analogy, it's like if you hired a teammate, but you're never allowed to get on a call with them and you can only go back and forth asynchronously over time. That works for some teammates and eventually that's actually how you want to spend most of your time. So that's still the future, but it's hard to initially adopt. And so we still have that vision of like, that's what we're trying to get you to, a teammate that you delegate to and then is proactive, and we're seeing that growing. But the key unlock is actually first you need to land with users in a way that's much more intuitive and trivial to get value from.

(00:18:54):
So the way that most people discover, the vast majority of users discover Codex today is either they download an IDE extension or they run it in their CLI and the agent works there with you on your computer interactively. And it works within a sandbox, which is actually a really cool piece of tech to help that be safe and secure, but it has access to all those dependencies. So if the agent needs to do something, it needs to run a command, it can do so within the sandbox. We don't have to set up any environment. And if it's a command that doesn't work in the sandbox, it can just ask you. And so you can get into this really strong feedback loop using the model. And then over time, our team's job is to help turn that feedback loop into you as a byproduct of using the product, configuring it so that you can then be delegating to it down the line.

(00:19:38):
And again, analogy, keep coming back to it, but if you hire a teammate and you ask them to do work, but you just give them a fresh computer from the store, it's going to be hard for them to do their job. But if as you work with them side by side, you could be like, "Oh, you don't have a password for this service we use, here's the password for this service. Yeah, don't worry, feel free to run this command," then it's much easier for them to then go off and do work for hours without you.

Lenny Rachitsky (00:20:01):
So what I'm hearing is the initial version of Codex was almost too far in the future. It's like a remote in the cloud agent that's coding for you asynchronously. And what you did is, "Okay, let's actually come back a little bit, let's integrate into the way engineers already integrate into IDs and locally and help them on ramp to this new world,"

Alexander Embiricos (00:20:21):
Totally. And it was quite interesting because we dogfood product a ton at OpenAI. So dogfood as in we use our own product. And so Codex has been accelerating OpenAI over the course of the entire year, and the cloud product was a massive accelerant to the company as well. It just turns out that this was one of those places where the signal we got from dogfooding is a little bit different from the signal you get from the general market because at OpenAI, we train reasoning models all day and so we're very used to this kind of prompting and think upfront, run things massively in parallel and it would take some time and then come back to it later asynchronously. And so now when we build, we still get a ton of signal from dogfooding internally, but we're also very cognizant of the different ways that different audiences use the product.

Lenny Rachitsky (00:21:12):
That's really funny. It's like live in the future, but maybe not too far in the future. And I could see how everyone at OpenAI is living very far in the future, and sometimes that won't work for everyone.

Alexander Embiricos (00:21:23):
Yeah.

Lenny Rachitsky (00:21:23):
What about just intelligence training data? I don't know, is there something else that helped Codex accelerate its ability to actually code? Is it better, cleaner data? Is it more just models advancing? Is there anything else that really helped accelerate?

Alexander Embiricos (00:21:38):
Yeah, so there's a few components here. I guess you were mentioning models and the models have improved a ton. In fact, just last Wednesday, we shipped GPT-5.1-Codex-Max, a very accurately named model, that is awesome. It is awesome both because it is for any given task that you were using GPT-5.1-Codex for, it's roughly 30% faster at accomplishing that task. But also it unlocks a ton of intelligence. So if you use it at our higher reasoning levels, it's just even smarter. And that tweet you were saying Karpathy made about, "Hey, give this your gnarliest bugs," obviously there's a ton going on in the market right now, but Codex-Max is definitely carrying that mantle of us tackling the hardest bugs. So that is super cool.

(00:22:28):
But I will say it's like some of how we're thinking about this is evolving a little bit from being like, "Yeah, we're just going to think about the model and let's just train the best model," to really thinking about what is an agent actually overall? And I'm not going to try to define agent exactly, but at least the stack that we think of it as having is it's like you have this model, really smart reasoning model that knows how to do a specific kind of task really well, so we can talk about how we make that possible. But then actually we need to serve that model through an API into a harness, and both of those things also have a really big role here.

(00:23:02):
So for instance, one of the things that we're really proud of is you can have GPT-5.1-Codex-Max work for really long periods of time. That's not normal, but you can set it up to do that or that might happen. But now routinely we'll hear about people saying, "Yeah, it ran overnight or it ran for 24 hours." And so for a model to work continuously for that amount of time, it's going to exceed its context window. And so we have a solution for that, which we call compaction.

(00:23:28):
But compaction is actually a feature that uses all three layers of that stack. So you need to have a model that has a concept of compaction and knows like, "Okay, as I start to approach this context window, I might be asked to prepare to be run in a new context window." And then at the API layer, you need an API that understands this concept and has an endpoint that you can hit to do this change. And at the harness layer, you need a harness that can prepare the payload for this to be done. So shipping this compaction feature that now just made this behavior possible to anyone using Codex actually meant working across all three things. And I think that's increasingly going to be true.

(00:24:02):
Another maybe underappreciated version of this is if you think about all the different coding products out there, they all have very different tool harnesses with very different opinions on how the model should work. So if you want to train a model to be good at all the different ways it could work, maybe you have a strong opinion that it should work using semantic search. Maybe you have a strong opinion that it should call bespoke tools or maybe you have, in our case, a strong opinion that it should just use the shell and work in the terminal, you can move much faster if you're just optimizing for one of those worlds. So the way that we built Codex is that it just uses the shell, but in order to make that safer and secure, we have a sandbox that the model is used to operating in.

(00:24:45):
So I think one of the biggest accelerants, to go all the way back to answer to your question, is just we're building all three things in parallel and tuning each one and constantly experimenting with how those things work with a tightly integrated product and research team.

Lenny Rachitsky (00:24:59):
Do you think you win in this space? Do you think it'll always be this kind of race with other models constantly leapfrogging each other? Do you think there's a world where someone just runs away with it and no one else can ever catch up? Is there a path to just, "We win"?

Alexander Embiricos (00:25:15):
Again, comes back to this idea of building a teammate, and not just a teammate that participates in team planning and prioritization, not just a teammate that really tests its code and helps you maintain and deploy it. But even a teammate... If you think, again, an engineering teammate, they can also schedule a calendar invite or move standup or do whatever, right? And so in my mind, if we just imagine that every day or every week some crazy new capability is just going to be deployed by a research lab, it's just impossible for us as humans to keep up and use all this technology. So I think we need to get to this world where you kind of just have an AI teammate or super assistant that you just talk to and it just knows how to be helpful on its own. So you don't have to be reading the latest tips for how to use it, you've plugged it in and it just provides help.

(00:26:10):
So that's kind of the shape of what I think we're building. And I think that will be a very sticky winning product if we can do so. So the shape that in my head, at least I have, is that we build... Maybe a fun topic is like, "Is Chat the right interface for AI?" I actually think Chat is a very good interface when you don't know what you're supposed to use it for. In the same way that if I think of I'm on MS Teams or in Slack with a teammate, Chat is pretty good. I can ask for whatever I want. It's kind of the common denominator for everything. So you can chat with a super assistant about whatever topic you want, whether it be coding or not. And then if you are a functional expert in a specific domain such as coding, there's a GUI that you can pull up to go really deep and look at the code and work with the code.

(00:26:54):
So I think what we need to build as OpenAI is basically this idea of you have Chat, ChatGPT and not as a tool that's ubiquitously available to everyone, you start using it even outside of work to just help you. You become very comfortable with the idea of being accelerated with AI. So then you get to work and you just can naturally just, "Yeah, I'm just going to ask it for this and I don't need to know about all the connectors or all the different features. I'm just going to ask it for help and it'll surface to me the best way that it can help at this point in time and maybe even chime in when I didn't ask it for help." So in my mind, if we can get to that, I think that's how we really build the winning product.

Lenny Rachitsky (00:27:32):
This is so interesting because with my chat with Nick Turley, the head of ChatGPT, I think he shared that the original name for ChatGPT was Super Assistant or something like that. And it's interesting that there's that approach to the super assistant and then there's this Codex approach. It's almost like the B2C version and the B2B version. And what I'm hearing is the idea here is, okay, you start with coding and building and then it's doing all this other stuff for you, scheduling meetings, I don't know, probably posting in Slack, I don't know, shipping designs. I don't know, is the idea that this is the business version of ChatGPT in a sense, or is there something else there?

Alexander Embiricos (00:28:08):
Yeah. So we're getting to the one-year time horizon conversation. A lot of this might happen sooner, but in terms of fuzziness, I think we're at the one year. So I'll give you a contention and a plausible way we get there, but as for how it happens, who knows? So basically, if we're going to build a super assistant, it has to be able to do things. So we're going to have a model and it's going to be able to do stuff affecting your world. And one of the learnings I think we've seen over the past year or so is that for models to do stuff, they're much more effective when they can use a computer.

(00:28:41):
Right, okay, so now we're like, okay, we need the super assistant that can use a computer, or many computers. And now the question is, okay, well, how should it use the computer? And there's lots of ways to use a computer. You could try to hack the OS and use accessibility APIs, maybe a bit easier as you could point and click. That's a little slow and unpredictable sometimes. And another way, it turns out the best way for models to use computers is simply to write code. So we're kind of getting to this idea where, well, if you want to build any agent, maybe you should be building a coding agent and maybe to the user, a non-technical user, they won't even know they're using a coding agent, the same way that no one thinks about are they using the internet or not, which is they're more just like, "Is WiFi on?"

(00:29:23):
So I think that what we're doing with Codex is we're building a software engineering teammate, and as part of that, we're kind of building an agent that can use a computer by writing code. And so we're already seeing some pull for this. It's quite early, but we're starting to see people who are using Codex for coding adjacent product purposes. And so as that develops, I think we'll just naturally see that, oh, it turns out we should just always have the agent write code if there is a coding way to solve a problem instead of... Even if you're doing a financial analysis, maybe write some code for that.

(00:29:55):
So basically like you were like, "Hey, is this the two ends of this product for the super assistant of ChatGPT?" In my mind, just coding is a core competency of any agent including ChatGPT. And so really what we think we're building is that competency. So here's the really cool thing about agents writing code is that you can import code. Code is composable, interoperable. Because one very reductive view we could have for an agent is it's just going to be given a computer and it's just going to point and click and go around. But that is the future. And then how we get there is difficult to chart a path because a lot of the questions around building agents aren't like, "Can the agent do it?" But it's more about, "Well, how can we help the agent understand the context that it's working in?" And the team that's using it probably has a way that they like to do things. They have guidelines. They probably want certain deterministic guarantees about what the agent can or cannot do. Or they want to know that the agent understands this detail.

(00:30:57):
An example would be if we're looking at a crash reporting tool, hitting a connector for it, every sub-team probably has a different meta prompt for how they want the crashes to be analyzed. And so we start to get to this thing where, yeah, we have this agent sitting in front of a computer, but we need to make that configurable for the team or for the user and let them... Stuff that the agent does often, we probably just want to build in as a competency that this agent has that it can do.

(00:31:24):
So I think we end up with this generalizable thing, that you were saying, of an agent that can just write its own scripts for whatever it wants to do. But I think that the really key part here is can we make it so that everything that the agent has to do often or that it does well, we can just remember and store so that the agent doesn't have to write a script for that again? Or maybe if I just joined a team and you are already on the same team as me, I can just use all those scripts that the agents had written already.

Lenny Rachitsky (00:31:53):
Yeah, it's like if this is our teammate, they can share things that it's learned from working with other people at the company. It just makes sense as a metaphor.

Alexander Embiricos (00:32:01):
Right. Yeah.

Lenny Rachitsky (00:32:02):
It feels like you're in the Karpathy camp of, "Agents today are not that great and mostly slop and maybe in the future they'll be awesome." Does that resonate?

Alexander Embiricos (00:32:11):
So I think coding agents are pretty great. I think we're seeing a ton of value there.

Lenny Rachitsky (00:32:11):
Yeah, that feels right. That feels right, yeah.

Alexander Embiricos (00:32:17):
And then I think agents outside of coding, it's still very early. And this is just my opinion, but I think they're going to get a whole lot better once they can use coding too in a composable way. It's kind of the fun part of when you're building for software engineers, at my startup, we were building for software engineers too for a lot of that journey, and they're just such a fun audience to build for because they also like building for themselves and are often even more creative than we are in thinking about how to use the technology. So by building for software engineers, you get to just observe a ton of emergent behaviors and things that you should do and build into the product.

Lenny Rachitsky (00:32:54):
I love how you say that because a lot of people building for engineers get really annoyed because the engineers they're just always complaining about stuff. They're like, "Ah, that sucks. Why'd you build it this way?" I love that you enjoy it, but I think it's probably because you're building such an amazing tool for engineers that can actually solve problems and just code for them.

(00:33:12):
Kind of along those lines, there's always this talk of what will happen with jobs, engineers, coding, do you have to learn coding? All these things. Clearly the way you're describing it is it's a teammate, it's going to work with you, make you more superhuman, it's not going to replace you. What's the way you just think about the impact on the field of engineering, having this super intelligent engineering teammate?

Alexander Embiricos (00:33:33):
I think there's two sides to it, but the one we were just talking about is this idea that maybe every agent should actually use code and be a coding agent. And in my mind, that's just a small part of this broader idea that, hey, as we make code even more ubiquitous... I mean, you could probably claim it's ubiquitous today, even pre AI, right? But as we make code even more ubiquitous, it's actually just going to be used for many more purposes. And so there's just going to be a ton more need for humans with this competency.

(00:34:01):
So that's my view. I think this is quite a complex topic. So it's something we talk about a lot and we have to see how it pans out. But I think what we can do basically as a product team building in the space is just try to always think about how are we building a tool so that it feels like we're maximally accelerating people rather than building a tool that makes it more unclear what you should do as the human?

(00:34:27):
I think, to give an example right now, nowadays when you work with a coding agent, it writes a ton of code, but it turns out writing code is actually one of the most fun parts of software engineering for many software engineers. So then you end up reviewing AI code. And that's often a less fun part of the job for many software engineers. So I actually think we see that this plays out all the time in a ton of micro decisions. So we as a product team, we're always thinking about, "Okay, how do we make this more fun? How do we make you feel more empowered? Where is this not working?" And I would argue that reviewing agent written code is a place that today is less fun.

(00:35:04):
So then I think, "Okay, what can we do about that?" Well, we can ship a code review feature that helps you build confidence in the AI written code. Okay, cool. Another thing we could do is we can make it so that the agent's better able to validate its work. And it gets all the way down into micro decisions. If you're going to have an agent capability to validate work, and let's say you have... I'm thinking of Codex Web right now, you have a pain that sort of reflects the work the agent did, what do you see first? Do you see the diff or do you see the image preview of the code it wrote? And I think if you're thinking about this from perspective, "How do I empower the human? How do I make them feel as accelerated as possible?" You obviously see the image first. You shouldn't be reviewing the code unless first you've seen the image, unless maybe it's been reviewed by an AI and now it's time for you to take a look.

Lenny Rachitsky (00:35:49):
When I had Michael Truell, the CEO of Cursor on the podcast, he had this kind of vision of us moving to something beyond code. And I've seen this rise of something called spec-driven development where you just write the spec and then the AI writes code for you. So you start working at this higher abstraction level. Is that something you see where we're going, just like engineers not having to actually write code or look at code and there's going to be this higher level of abstraction that we focus on?

Alexander Embiricos (00:36:16):
Yeah. I mean, I think there's constantly these levels of abstraction and they're actually already played out today. Today, coding agents, mostly it's prompt to patch. We're starting to see people doing spec-driven development or planned and driven development. That's actually one of the ways when people ask, "Hey, how do you run Codex on a really long task?" Well, it's like often collaborate with it first to write a plan.md, like a markdown file that's your plan. And once you're happy with that, then you ask it to go off and do work. And if that plan has verifiable steps, it'll work for much longer. So we're totally seeing that.

(00:36:50):
I think spec-driven development is an interesting idea. It's not clear to me that it'll work out that way because a lot of people don't like writing specs either, but it seems plausible that some people will work that way. A bit of a joke idea though is if you think of the way that many teams work today, they often don't necessarily have specs, but the team is just really self-driven and so stuff just gets done. And so almost that it's like, I'm coming up with this on the spot, so it's not a good name, but chatter-driven development where it's just like stuff is happening on social media and in your team communications tools. And then as a result, code gets written and deployed.

(00:37:29):
So yeah, I think I'm a little bit more oriented in that way of I don't even necessarily want to have to write a spec. Sometimes I want to, only if I like writing specs. Other times I might just want to say like, "Hey, here's the customer service channel and tell me what's interesting to know, but if it's a small bug, just fix it." I don't want to have to write a spec for that, right?

(00:37:51):
I have this sort of hypothetical future that I like to share sometimes with people as a provocation, which is in a world where we have truly amazing agents, what does it look like to be a solopreneur? And one terrible idea for how it could look is that actually there's a mobile app and every idea that the agent has to do is just vertical video on your phone and then you can swipe left if you think it's a bad idea and you can swipe right if it's a good idea. And you can press and hold and speak to your phone if you want to give feedback on the idea before you swipe. And in this world, basically what your job is is just to plug in this app into every single signal system or system of record, and then you just sit back and swipe. I don't know.

Lenny Rachitsky (00:38:39):
I love this. So this is like Tinder meets TikTok meets Codex.

Alexander Embiricos (00:38:42):
It's pretty terrible.

Lenny Rachitsky (00:38:43):
No, this is great. So the idea here is this agent is watching and listening to you, paying attention to the market, your users, and it's like, "Cool, here's something I should do." It's like a proactive engineer just like, "Here, we should build this feature, fix this thing."

Alexander Embiricos (00:38:56):
Exactly. Exactly.

Lenny Rachitsky (00:38:58):
I think it's a really good idea.

Alexander Embiricos (00:39:00):
Communicating with you in the lowest effort way for your consumers.

Lenny Rachitsky (00:39:02):
Yeah, yeah, the modern way we communicate, swipe left to right and vertical feed. And then the Sora video, okay, so I see how this all connects now. I see.

Alexander Embiricos (00:39:11):
Yeah. To be clear, we're not building that, but it's a fun idea. I mean, in this example though, one of the things that it's doing is it's consuming external signals, right? I think the other really interesting thing is if we think about what is the most successful AI product to date, I would argue, it's funny actually not to confuse things at all, but the first time we used the brand Codex at OpenAI was actually the model powering GitHub Copilot. This is way back in the day, years ago. And so we decided to reuse that brand recently because it's just so good, Codex, code execution.

(00:39:46):
But I think actually auto completion and IDEs is one of the most successful AI products today. And part of what's so magical about it is that when it can surface ideas for helping you really rapidly, when it's right, you're accelerated. When it's wrong, it's not that annoying. It can be annoying, but it's not that annoying. So you can create this mixed initiative system that's contextually responding to what you're attempting to do.So in my mind, this is a really interesting thing for us as OpenAI as we're building.

(00:40:22):
So for instance, when I think about launching a browser, which we did with Atlas, in my mind, one of the really interesting things we can then do is we can then contextually surface ways that we can help you as you're going about your day. And so we break out of this, we're just looking at code or we're just in your terminal into this idea that, "Hey, a real teammate is dealing with a lot more than just code. They're dealing with a lot of things that are web content. So how can we help you with that?"

Lenny Rachitsky (00:40:51):
Man, there's so much there. I love this. Okay, so auto complete on web with the browser. That's so interesting. Just like, "Here's all the things that we can help you with as you're browsing and going about your day."

(00:41:01):
I want to talk about Atlas. I'll come back to that. Codex, code execution, did not know that. That's really clever. I get it now. Okay, and then this chatter, what is a chatter-driven development? No, this is a really good idea, but it reminds me, I had Dhanji on the podcast, CTO of Block, and they have this product called Goose, which is their own internal agent thing. And he talked about an engineer at Block just has Goose watch him with his screen and listens to every meeting and proactively does work that he should probably want to do. So ships to PR, sends an email, drafts a Slack message. So he's doing exactly what you're describing in kind of a very early way.

Alexander Embiricos (00:41:45):
Yeah, that's super interesting. And I bet you, so if we went and asked them what the bottleneck to that productivity is, did they share what it is?

Lenny Rachitsky (00:41:54):
Probably looking at it and just making sure this is the right thing to do, yeah.

Alexander Embiricos (00:41:58):
Yeah. So we see this now. We have a Slack integration for Codex. People love if there's something that you need to do quickly, people will just @ mention Codex, "Why do you think this bug is happening?" It doesn't have to be an engineer. Even maybe data scientists often here are using Codex a ton to just answer questions like, "Why do you think this metric moved? What happened?" So questions, you get the answer right back in Slack. It's amazing, super useful. But as for when it's writing code, then you have to go back and look at the code.

(00:42:25):
So the real, I think, bottleneck right now is validating that the code worked and writing code review. So in my mind, if we wanted to get to something like the friend you were talking about's world, I think we really need to figure out how to get people to configure their coding agents to be much more autonomous on those later stages of the work.

Lenny Rachitsky (00:42:46):
It makes sense. Like you said, writing code, I used to be an engineer, I was an engineer for 10 years, really fun to write code, really fun to just get in the flow, build architect, test. Not so fun to look at everyone else's code and just have to go through and be on the hook if it's doing something dumb that's going to take down production. And now that building has become easier, what I've always heard from companies that are really at the cutting edge of this is the bottleneck is now figuring out what to build. And then it's at the end of like, "Okay, we have all this, all 100 PRs to review. Who's going to go through all that?"

Alexander Embiricos (00:43:14):
Right.

Lenny Rachitsky (00:43:15):
Yeah.

(00:43:17):
This episode is brought to you by Jira Product Discovery. The hardest part of building products isn't actually building products. It's everything else. It's proving that the work matters, managing stakeholders, trying to plan ahead. Most teams spend more time reacting than learning, chasing updates, justifying roadmaps, and constantly unblocking work to keep things moving. Jira Product Discovery puts you back in control. With Jira Product Discovery, you can capture insights and prioritize high impact ideas. It's flexible so it adapts to the way your team works and helps you build a roadmap that drives alignment, not questions. And because it's built on Jira, you can track ideas from strategy to delivery all in one place. Less chasing, more time to think, learn, and build the right thing. Get Jira Product Discovery for free at atlassian.com/lenny. That's atlassian.com/lenny.

(00:44:08):
What has the impact of Codex been on the way you operate as a product person as a PM? It's clear how engineering is impacted, code is written for you. What has it done to the way you operate and the way PMs operate at OpenAI?

Alexander Embiricos (00:44:24):
Yeah, I mean, I think mostly I just feel much more empowered. I've always been sort of more technical leaning PM, and especially when I'm working on products for engineers, I feel like it's necessary to dogfood the product. But even beyond that, I just feel like I can do much, much more as a PM. And Scott Belsky talks about this idea of compressing the talent stack. I'm not sure if I've phrased that right. But it's basically this idea that maybe the boundaries between these roles are a little bit less needed than before because people can just do much more. And every time someone can do more, you can skip one communication boundary and make the team that much more efficient.

(00:45:03):
So I think we see it in a bunch of functions now, but I guess since you asked about products specifically, now answering questions much, much easier. You can just ask Codex for thoughts on that. A lot of PM type work, understanding what's changing. Again, just ask Codex for help with that. Prototyping is often faster than writing specs. This is something that a lot of people have talked about.

(00:45:29):
I think something that, I don't think it's super surprising, but something that's slightly surprising is we see... We're mostly building Codex to write code that's going to be deployed to production, but actually we see a lot of throwaway code written with Codex now. It's kind of going back to this idea of ubiquitous code. So you'll see someone wants to do an analysis. If I want to understand something, it's like, okay, just give Codex a bunch of data, but then ask it to build an interactive data viewer for this data. That's just too annoying to do in the past, but now it's just totally worth the time of just getting an agent to go do something.

(00:46:02):
Similarly, I've seen some pretty cool prototypes on our design team about if you want to... Well, a designer basically wanted to build an animation, and this is the Coin Animation Codex, and it was like normally it'd be too annoying to program this animation. So they just vibe coded a animation editor and then they use the animation editor to build the animation, which they then check into their repo.

(00:46:24):
Actually, our designers, there's a ton of acceleration there. And speaking of compressing the talent stack, I think our designers are very PME. So they do a ton of product work and they actually have an entire vibe coded side prototype of the Codex app. And so a lot of how we talk about things is we'll have a really quick jam because there's 10,000 things going on, and then the designer will go think about how this should work. But instead of talking about it again, they'll just vibe code a prototype of that in their standalone prototype. We'll play with it. If we like it, they'll vibe engineer that prototype into an actual PR to land. And then depending on their comfort with the code base, like Codex utilizing Rust is a little harder, maybe they'll land it themselves or they'll get close and then an engineer can help them land the PR.

(00:47:11):
We recently shipped the Sora Android app, and that was one of the most mind-blowing examples of acceleration, actually, because usage of Codex internally at OpenAI is obviously really, really high, but it's been growing over the course of the year, both in terms of now it's basically all technical staff use it, but even the intensity and know how of how to make the most of coding agents has gone up by a ton. And so the Sora Android app, a fully new app, we built it in 18 days. It went from zero to launch to employees, and then 10 days later, so 28 days total, we went to just GA, to the public, and that was done just with the help of Codex. So pretty insane velocity.

(00:47:55):
I would say it was a little bit... I don't want to say easy mode, but there is one thing that Codex is really good at if you're a company that's building software on multiple platforms, so you've already figured out some of the underlying APIs or systems, asking Codex to port things over is really effective because it has something you can go look at. And so the engineers on that team were basically having Codex go look at the iOS app, produce plans of work that needed to be done, and then go implement those. And it was looking at iOS and Android at the same time. And so basically it was two weeks to launch to employees, four weeks total. Insanely fast.

Lenny Rachitsky (00:48:31):
What makes that even more insane is it became the number one app in the app store. This just boggles the mind. Okay, so 28 days?

Alexander Embiricos (00:48:39):
Yeah, so imagine number one app in the app store with a handful of engineers. I think it was two or three possibly in a handful of weeks.

Lenny Rachitsky (00:48:51):
Yeah, this is absurd. Wow.

Alexander Embiricos (00:48:56):
Yeah, so that's a really fun example of acceleration. And then Atlas was the other one that I think Ben did a podcast, the engine lead on Atlas, sharing a little bit about how we built there. Atlas is actually... I mean, it's a browser, and building a browser is really hard. So we had to build a lot of difficult systems in order to do that. And basically we got to the point where that team has a ton of power users of Codex right now, and it got to the point they where basically... We were talking to them about it, because a lot of those engineers are people I used to work with before at my startup. And so they'd say, "Before this would've taken us two to three weeks for two to three engineers, and now it's like one engineer, one week." So massive acceleration there as well.

(00:49:49):
And what's quite cool is that we shipped Atlas on Mac first, but now we're working on the Windows version. So the team now is ramping up on Windows and they're helping us make Codex better on Windows too, which is admittedly earlier, just the model we shipped last week is the first model that natively understands PowerShell. So PowerShell being the native Shell language on Windows. So yeah, it's been really awesome to see the whole company getting accelerated by Codex from... And most obviously, also research and improving how quickly we train models and how well we do it. And then even design, as we talked about, and marketing. Actually, we're at this point now where my product marketer is often also making string changes just directly from Slack or updating docs directly from Slack.

Lenny Rachitsky (00:50:37):
These are amazing examples. You guys are living at the bleeding edge of what is possible, and this is how other companies are going to work. Just shipping, again, what became the number one app in the app store and just beloved all over the... It just took over, I don't know, the world for at least a week. Built, you said, in 28 days and I don't know, 10 days, 18 days just to get the core of it working.

Alexander Embiricos (00:51:00):
Yeah, so it was like 18 days we had a thing that employees were playing with, and then 10 days later we were out.

Lenny Rachitsky (00:51:05):
And you said just a couple engineers.

Alexander Embiricos (00:51:07):
Yeah.

Lenny Rachitsky (00:51:07):
Two or three. Okay. And then Atlas you said took a week to build?

Alexander Embiricos (00:51:12):
No, no, no. So Atlas, not the whole week, but Atlas was a really meaty project. And so I was talking to one of the engineers on Atlas about just what they use Codex for. And it's basically like, "We use Codex for absolutely everything." And I was like, "Okay, well, how would you measure the acceleration?" And so basically the answer I got back was, "Previously would've taken two to three weeks for two to three engineers, and now it's like one engineer, one week."

Lenny Rachitsky (00:51:36):
Do you think this eventually moves to non-engineers doing this sort of thing? Does it have to be an engineer building this thing? Could Sora have been built by, I don't know, a PM or designer?

Alexander Embiricos (00:51:45):
I think we will very much get to the point, well, basically where the boundaries are a little bit blurred. I think you're going to want someone who understands the details of what they're building, but what details those are will evolve. Kind of like how now if you're writing Swift, you don't have to speak assembly. There's a handful of people in the world, and it's really important that they exist and speak assembly, maybe more than a handful, but that's a specialized function that most companies don't need to have.

(00:52:14):
So I think we're just going to naturally see an increase in layers of abstraction. And then the cool thing is now we're entering the language layer of abstraction, like natural language, and then natural language itself is really flexible. You could have engineers talking about a plan and then you could have engineers talking about a spec, and then you could have engineers talking about just a product or an idea. So I think we can also start moving up those layers of abstraction as well.

(00:52:39):
But I do think this is going to be gradual. I don't think it's going to go off to all of a sudden nobody ever writes anything, any code and it's just specs. I think it's going to be much more like, "Okay, we've set up our coding agent to be really good at previewing the build or at running tests," maybe that's the first part that most people have set up. And it's like, "Okay, now we've set it up so they can execute the build and it can see the results of its own changes, but we haven't yet built a good integration harness so that it can," in the case of Atlas... By the way, I don't know if they've done any of this or not. I think they've done a lot of this. But maybe the next stage is enable it to load a few sample pages to see how well those work. So then, okay, now we're going to set it up to do that.

(00:53:18):
And I think for some time at least, we're going to have humans curating which of these connectors or systems or components that the agent needs to be good at talking to. And then in the future, there will be an even greater unlock where Codex tells you how to set it up or maybe sets itself up in a repo.

Lenny Rachitsky (00:53:34):
What a wild time to be alive. Wow. I'm curious just the second order effects of this sort of thing, just how quickly it is to build stuff. What does that do? Does that mean distribution becomes much, much more important? Does it mean ideas are just worth a lot more? It's interesting to think about how quick how that changes.

Alexander Embiricos (00:53:51):
I'm curious what you think. I still don't think ideas are worth as much as maybe a lot of people think. I still think execution is really hard. You can build something fast, but you still need to execute well on it, still needs to make sense and be a coherent thing overall, yeah, and distribution is massive.

Lenny Rachitsky (00:54:08):
Yeah. Just feels like everything else is now more important. Everything that isn't the building piece, which is coming up with an idea, getting to market, profit, all that kind of stuff.

Alexander Embiricos (00:54:18):
Yeah. I think we might've been in this weird temporary phase where, for a while, it was so hard to build product that you mostly just had to be really good at building product and it maybe didn't matter if you had an intimate understanding of a specific customer. But now I think we're getting to this point where actually if I could only choose one thing to understand, it would be really meaningful understanding of the problems that a certain customer has. If I could only go in with one core competency.

(00:54:52):
So I think that's ultimately still what's going to matter most. If you're starting a new company today and you have a really good understanding and network of customers that are currently underserved by AI tools, I think you're set. Whereas if you're good at building websites, but you don't have any specific customer to build for, I think you're in for a much harder time.

Lenny Rachitsky (00:55:14):
Bullish on vertical AI startups is what I'm hearing. Yeah, I completely agree. There's the general thing that can solve a lot of problems and then there's like, "We're going to solve presentations incredibly well and we're going to understand the presentation problem better than anyone and we're going to plug into your workflows and all these other things that matter for a very specific problem." Okay, incredible.

(00:55:36):
When you think about progress on Codex, I imagine you have a bunch of evals and there's all these public benchmarks. What's something you look at to tell you, "Okay, we're making really good progress," I imagine it's not going to be the one thing, but what do you focus on? What's something you're trying to push? What's a KPI or two?

Alexander Embiricos (00:55:51):
One of the things that I'm constantly reminding myself of is that a tool like Codex naturally is a tool that you would become a power user of. So we can accidentally spend a lot of our time thinking about features that are very deep in the user adoption journey. And so we can kind of end up oversolving for that. And so I think it's just critically important to go look at your D7 retention. Just go try the product, sign up from scratch again. I have a few too many ChatGPT Pro accounts that I've, in order to maximally correctly dogfood, signed up for on my Gmail and they charge me 200 bucks a month. I need to expense those. But I think just the feeling of being end user and the early retention stats are still super important for us because as much as this category is taking off, I think we're still in the very early days of people using them.

(00:56:44):
Another thing that we do that I think we might be the most user feedback/social media pilled team out there in this space is like a few of us are constantly on Reddit and Twitter, and there's praise up there and there's a lot of complaints, but we take the complaints very seriously and look at them. And I think that, again, because you can use a coding agent for so many different things, it often is kind of broken in many sort of ways for specific behaviors. So we actually monitor a lot just what the vibes are on social media pretty often, especially I think for Twitter/X, it's a little bit more hypey and then Reddit is a little more negative but real actually. So I've started increasingly paying attention to how people are talking about using Codex on Reddit actually.

Lenny Rachitsky (00:57:39):
This is important for people to know. Which of the subreddits do you check most? Is there like an r/Codex or?

Alexander Embiricos (00:57:44):
I mean, the algorithm's pretty good at surfacing stuff, but r/Codex is there.

Lenny Rachitsky (00:57:48):
Okay. I'll take. Very interesting. And then if people tag you on Twitter, you still see that, but maybe not as powerful as seeing it on Reddit.

Alexander Embiricos (00:57:56):
Well, yeah. Well, the thing with Twitter is it's a little bit more one-to-one, even if it's in public. Whereas with Reddit, those are really good upvoting mechanics and maybe most people are still not bots, unclear. So you get good signal on what matters and what other people think.

Lenny Rachitsky (00:58:09):
So interestingly, Atlas, I want to talk about that briefly. You guys launched Atlas. I tweeted actually that I tried Atlas and then I don't love the AI only search experience. I was just like, "I just want Google sometimes," or whatever. Just waiting for AI to give me an answer, I'm like, "I don't want to... " And there was no way to switch. I just tweeted, "Hey, I'm switching back. It's not great." And I feel like I made some PMs at OpenAI sad. And I saw someone tweet, "Okay, we have Atlas now," which I imagine was always part of the plan. It's probably an example of just, "We got to ship stuff, see how people use it and then we figure it out." So I guess one is that, I don't know, is there anything there? And two, I'm just curious, why are you guys building a web browser?

Alexander Embiricos (00:58:48):
So I worked on Atlas for a bit. I don't work on it now. But a bit of the narrative here for me just to tell my story a bit was I was working on this screen sharing, pair programming startup, and then we joined OpenAI. And so the idea was really to build a contextual desktop assistant. And the reason I believe that's so important is because I think that it's really annoying to have to give all your context to an assistant and then to figure out how it can help you. So if it could just understand what you are trying to do, then it could maximally accelerate you. So I still think of Codex actually as a contextual assistant from a little bit of a different angle, starting with coding tasks.

(00:59:30):
But some of the thinking, at least for me personally, I can't speak for the whole project, was that a lot of work is done in the web. And if we could build a browser, then we could be contextual for you, but in a much more first class way. We weren't hacking other desktop software which have very varied support for what content they're rendering to the accessibility tree. We wouldn't be relying on screenshots, which are a little bit slower and unreliable. Instead, we could be In the rendering engine and extract whatever we needed to help you. And also I like to think of video games, I don't know if you've played, I don't know, say Halo, you walk up to an object, I mean, this is true for many games, you press... Man, it's been a long time, this is embarrassing. Press X and it just does the right thing. And I was one of those guys who always read the instruction manual for every video game that I bought.

(01:00:24):
And I remember the first time I read about a contextual action and I just thought it was this really cool idea. And the thing about a contextual action is we need to know what you are attempting to do. We have a little bit of context and then we can help. And I think this is critically important because imagine this world that we reach where we have agents that are helping you thousands of times per day.

(01:00:49):
Imagine if the only way we could tell you that we helped you was if we could push notify you. So you get a thousand push notifications a day of an AI saying like, "Hey, I did this thing. Do you like it? " It'd be super annoying, right? Whereas imagine, going back to software engineering, I was looking at a dashboard and I noticed some key metric had gone down. And at that point in time, an AI could maybe go take a look and then surface the fact that it has an opinion on why this metric went down and maybe a fix right there right when I'm looking at the dashboard. That would much more keep me in flow and enable the agent to take action on many more things.

(01:01:26):
So in my mind, part of why I'm excited for us to have a browser is that I think we have then much more context around what we should help with. Users have much more control over what they want us to look at. It's like, "Hey, if you want us to take action on something, you can open it in your AI browser. If you don't, then you can open it in your other browser." So really clear control and boundaries. And then we have the ability to build UX that's mixed initiatives so that we can surface contextual actions to you at the time that they're helpful as opposed to just randomly notifying you.

Lenny Rachitsky (01:01:58):
Hearing the vision for Codex being the super assistant, it's not just there to code for you. It's trying to do a lot for you as a teammate, as this kind of super teammate, and that makes you awesome at work. So I get this. Speaking of that, are there other non-engineering common use cases for Codex? Just ways that non-engineers... We talked about designers prototyping and building stuff, are there any fun or unexpected ways people are using Codex that aren't engineers?

Alexander Embiricos (01:02:24):
I mean, there's a load of unexpected ways, but I think most of where we're seeing real traction with people using things are still for now very, I would say, coding adjacent or tech-oriented, places where there's a mature ecosystem or maybe you're doing data analysis or something like that. I personally am expecting that we're going to see a lot more of that over time. But for now, we're keeping the team very focused on just coding for now because there's so much more work to do.

Lenny Rachitsky (01:02:54):
For people that are thinking about trying out Codex, does it work for all kinds of code bases? What code does it support? If you're like, I don't know, SAP, can you add Codex and start building things? What's the sweet spot? Where does it start to not be amazing yet?

Alexander Embiricos (01:03:11):
I'm really glad you asked this question actually because the best way to try Codex is to give it your hardest tasks, which is a little different than some of the other coding agents. Some tools you might think, "Okay, let me start easy or just vibe code something random and decide if I like the tool." Whereas we're really building Codex to be the professional tool that you can give your hardest problems to. And that writes high quality code in your enormous code base that is in fact not perfect right now. So yeah, I think if you're going to try Codex, you want to try it on a real task that you have and not necessarily dumb that task down to something that's trivial, but actually a good one would be you have a hard bug and you don't know what's causing that bug and you ask Codex to help figure that out or to implement that the fix.

Lenny Rachitsky (01:04:00):
I love that answer. Just give it to your hardest problem.

Alexander Embiricos (01:04:03):
I will say if you're like, "Hey, okay, well, the hardest problem I have is that I need to build a new unicorn business," obviously that's not going to work. Not yet. So I think it's like give it the hardest problem, but something that is still one question or one task to start. That's if you're testing and then over time you can learn how to use it for bigger things.

Lenny Rachitsky (01:04:25):
Yeah. What languages does it support?

Alexander Embiricos (01:04:27):
Basically, the way we've trained Codex is there's a distribution of languages that we support and it's fairly aligned with the frequency of these languages in the world. So unless you're writing some very esoteric language or some private language, it should do fine in your language.

Lenny Rachitsky (01:04:41):
If someone was just getting started, is there a tip you could share to help them be successful? If you could just whisper a little tip into someone just setting up Codex for the first time to help them have a really good time, what's something you would whisper?

Alexander Embiricos (01:04:54):
I might say try a few things in parallel. So you could try giving it a hard task, maybe ask it to understand the code base, formulate a plan with it around an idea that you have and kind of build your way up from there. And the meta idea here is, again, it's like you're building trust with a new teammate. And so you wouldn't go to a new teammate and just give them like, "Hey, do this thing. Here's zero context." You would start by first making sure they understand the code base and then you would maybe align on an approach and then you would have them go off and do bit by bit. And I think if you use Codex in that way, you'll just naturally start to understand the different ways of prompting it because it's a super powerful agent and model, but it is a little bit different to prompt Codex than other models.

Lenny Rachitsky (01:05:38):
Just a couple more questions. One, we touched on this a little bit, as AI does more and more coding, there's always this question of, "Should I learn to code and why should I spend time doing this sort of thing?" For people that are trying to figure out what to do with their career, especially if they're into software engineering computer science, do you think there's specific elements of computer science that are more and more important to lean into, maybe things they don't need to worry about? What do you think people should be leaning into skill-wise as this becomes more and more of a thing in our workplace?

Alexander Embiricos (01:06:11):
I think there's a couple angles you could go at this from. Well, the easiest one to think of at least is just be a doer of things. I think that with coding agents getting better and better over time, it's just what you can do as even someone in college or a new grad is just so much more than what that was before. And so I think you just want to be taking advantage of that. And definitely when I'm looking at hiring folks who are earlier career, it's definitely something that I think about is how productive are they using the latest tools? They should be super productive. And if you think of it in that way, they actually have less of a handicap than before versus a more senior career person because the divide is actually getting smaller because they've got these amazing coding agents now. So that's one thing, which is, I guess the advice is just learn about whatever you want, but just make sure you spend time doing things, not just fulfilling homework assignments, I guess.

(01:07:11):
I think the other side of it though is that it's still deeply worth understanding what makes a good overall software system. So I still think that skills, like really strong systems engineering skills, or even really effective communication and collaboration with your team, skills like that I think are important or are going to continue to matter for quite some time. I don't think it's going to be all of a sudden the AI coding agents are just able to build perfect systems without your help. I think it's going to look much more gradual where it's like, okay, we have these AI coding agents, they're able to validate their work. It's still important.

(01:07:51):
For example, I'm thinking of an engineer who was working on Atlas, since we were talking about it, he set up Codex so that it can verify its own work, which is a little bit non-trivial because of the nature of the Atlas project. So the way that he did that was he actually prompted Codex like, "Hey, why can't you verify your work? Fix it," and did that on a loop. And so you still, at various phases, are going to want a human in the loop to help configure the coding agent to be effective. So I think you still want to be able to reason about that. So maybe it's less important that you can type really fast and you understand exactly how to write... Not that anyone writes a 4H loop or something, or you don't need to know how to implement a specific algorithm. But I think you need to be able to reason about the different systems and what makes a software engineering team effective. So I think that's the other really important thing.

(01:08:40):
Then maybe the last angle that you could take is, I think if you're on the frontier of knowledge for a given thing, I still think that's deeply interesting to go down, partially because that knowledge is still going to be... Agents aren't going to be as good at that, but also partially because I think that by trying to advance the frontier of a specific thing, you'll actually end up being forced to take advantage of coding agents and using them to accelerate your own workflow as you go.

Lenny Rachitsky (01:09:09):
What's an example that when you talk about being at the frontier of something?

Alexander Embiricos (01:09:12):
Codex writes a lot of the code that helps manage its training runs, the key infrastructure. We move pretty fast and so we have a Codex code review is catching a lot of mistakes. It's actually cause some pretty interesting configuration mistakes. And we're starting to see glimpses of the future where we're actually starting to have Codex even be on call for its own training, which is pretty interesting. So there's lots there.

Lenny Rachitsky (01:09:38):
Wait, what does that mean to be on call for its own training? So it's running, it's training and it's like, "Oh, something broke, someone needs..." And does it alert people or it's like, "Here, I'm going to fix the problem and restart"?

Alexander Embiricos (01:09:47):
This is an early idea that we're figuring out. But the basic idea is that during a training run, there's a bunch of graphs that today humans are looking at and it's really important to look at those. We call this babysitting.

Lenny Rachitsky (01:09:59):
Because it's very expensive to train, I imagine, and very important to move fast and-

Alexander Embiricos (01:10:03):
Exactly. And there's a lot of systems underlying the training run. And so a system could go down or there could be an error somewhere that gets introduced. And so we might need to fix it or pause things or, I don't know, there's lots of actions we might need to take. And so basically having Codex run on a loop to evaluate how those charts are moving over time is this idea that we have to how to enable us to train way more efficiently.

Lenny Rachitsky (01:10:26):
I love that. And this is very much along the lines of this is the future of agents. Codex isn't just for building code, it's a lot more than that.

Alexander Embiricos (01:10:34):
Yeah.

Lenny Rachitsky (01:10:36):
Okay, last question. Being at OpenAI, I can't not ask about your AGI timeline and how far you think we are from AGI. I know this isn't what you work on, but there's a lot of opinions, a lot of, I don't know, timelines. How far do you think we are from a humanly human version of AI, whatever that means to you?

Alexander Embiricos (01:10:56):
For me, I think that it's a little bit about when do we see the acceleration curves go like this? Or I don't know which way I'm mirrored here. When do we see the hockey stick? And I think that the current limiting factor, I mean, there's many, but I think a current underappreciated limiting factor is literally human typing speed or human multitasking speed on writing prompts. And like you were talking about, it's like you can have an agent watch all the work you're doing, but if you don't have the agent also validating its work, then you're still bottlenecked on can you go review all that code?

(01:11:29):
So my view is that we need to unblock those productivity loops from humans having to prompt and humans having to manually validate all the work. So if we can rebuild systems to let the agent be default useful, we'll start unlocking hockey sticks. Unfortunately, I don't think that's going to be binary. I think it's going to be very dependent on what you're building. So I would imagine that next year, if you're a startup and you're building new pieces, like some new app or something, it'll be possible for you to set it up on a stack where agents are much more self-sufficient than not. But now let's say, I don't know, you mentioned SAP, let's say you work in SAP, they have many complex systems and they're not going to be able to just get the agent to be self-sufficient overnight in those systems. So they're going to have to slowly maybe replace systems or update systems to allow the agent to handle more of the work end to end.

(01:12:22):
So basically my long answer to your question, maybe boring answer is that I think starting next year, we're going to see early adopters starting to hockey stick their productivity. And then over the years that follow, we're going to see larger and larger companies like hockey stick that productivity. And then somewhere in that fuzzy middle is when that hockey sticking will be flowing back into the AI labs and that's when we'll basically be at the AGI tier.

Lenny Rachitsky (01:12:48):
I love this answer. It's very practical and it's something that comes up a lot on this podcast. Just like the time to reveal all the things AI is doing is really annoying and a big bottleneck. I love that you're working on this because it's one thing to just make coding much more efficient and do that for people. It's another to take care of that final step of, "Okay, is this actually great?" And that's so interesting that your sense is that's the limiting factor. It comes back to your earlier point of even if AI did not advance anymore, we have so much more potential to unlock as we learn to use it more effectively. So that is a really unique answer. I haven't heard that perspective on what is the big unlock. Human typing speed to review basically what AI is doing for us. So good.

(01:13:31):
Okay, Alexander, we covered a lot of ground. Is there anything that we haven't covered? Is there anything you wanted to share, maybe double down on before we get to our very exciting lightning round?

Alexander Embiricos (01:13:43):
I think one thing is that the Codex team is growing. And as I was just saying, we're still somewhat limited by human thinking speed and human typing speed. We're working on it. So if you're an engineer or a salesperson, or I'm hiring a product person, please hit us up. I'm not sure the best way to give contact info, but I guess you can go to our jobs page, or do they have contact for you actually? Do listeners have contact for you?

Lenny Rachitsky (01:14:10):
Where they send me like, "Hey, I want to apply to Codex"? I do have a contact form at lennyrachitsky.com. I'm afraid of all the amazing people that are going to ping me. But there we go, we could try that. Let's see how that goes.

Alexander Embiricos (01:14:20):
Okay. Or maybe an easier version, we can edit all that out or up to you. Yeah, or I would just say you can drop us a DM. For example, I'm Embirico on Twitter, and hit me up if you're interested in joining the team.

Lenny Rachitsky (01:14:33):
What a dream job for so many people. What's a sign they... I don't know, what's a way to filter people a little bit so they're not flooding your inbox?

Alexander Embiricos (01:14:42):
So specifically if you want to join the Codex team, then you need to be a technical person who uses these tools. And I think I would just ask yourself the question, "Hey, let's say I were to join OpenAI and work on Codex over the next six months and crush it, what does the life of a software engineer look like then?" And I think if you have an opinion on that, you should apply. And if you don't have an opinion on that and have to think about it first, depending on how long you have to think about it, I guess that would be the filter. I think there's a lot of people thinking about this space. So we're very interested in folks who have already been thinking about what the future should look like with agents. And we don't have to agree on where we're going, but I think we want people who are very passionate about the topic, I guess.

Lenny Rachitsky (01:15:28):
It's very rare to be working on a product that has this much impact and is at such a bleeding edge of where it's possible. What a cool role for the right person. So it's awesome that you have an opening and this audience is a really good fit potentially for that role. So I hope we find someone, that would be incredible. With that, we've reached our very exciting lightning round. I've got five questions for you, Alexander. Are you ready?

Alexander Embiricos (01:15:54):
I don't know what these are, but I'm excited. Let's do it.

Lenny Rachitsky (01:15:57):
They're the same questions I ask everyone except for the last one. So probably not a surprise. I should probably make them more often a surprise. Okay, first question, what are a couple of books that you recommend most to other people, two or three books that come to mind?

Alexander Embiricos (01:16:12):
I have been reading a lot of science fiction recently, and I'm sure this has been recommended before, but The Culture, I think it's Ian Banks is the name of the author. Part of why I love it is because it's basically relatively recent writing about a future with AI, but it's an optimistic future with AI. And I think a lot of sci-fi is fairly dystopian. But the joke, at least on The Culture subreddit is that, let me see if I can get this right, it is a space communist utopia, or I think it's a gay space communist utopia. And I just think it's really fun to think about, to use The Culture as a way to think about what kind of world can we usher in and what decisions can we make today to help usher in that world.

Lenny Rachitsky (01:17:02):
Wow. I don't think anyone's recommended that. I know you're reading, you've mentioned before I start recording, Lord of the Rings right now. If you want another AI-ish sci-fi book, have you read Fire Upon the Deep?

Alexander Embiricos (01:17:15):
No, I haven't.

Lenny Rachitsky (01:17:15):
Okay, it's incredibly good. It's like a sci-fi space opera sort of epic tale with super intelligence.

Alexander Embiricos (01:17:25):
Cool.

Lenny Rachitsky (01:17:25):
Yeah. Mostly not optimistic, but somewhat optimistic.

(01:17:30):
Okay, next question. Is there a favorite recent movie or TV show that you've really enjoyed?

Alexander Embiricos (01:17:36):
Yeah, there's an anime called Jujutsu Kaisen, which I really like. Again, it's got a slightly dark topic of demons. But what I love about it is that the hero is really nice. And I think there's this new wave of anime and cartoons where the protagonists are really friendly and people who care about the world rather than being sort of, if you look at some older anime that started the genre, there's Evangelion or Akita and those characters, the protagonists are deeply flawed, quite unhappy. They didn't start the genre, but it was a trend for a while to poke fun at the idea that in these cartoons the protagonist was very young, but being given a ridiculous amount of responsibility to save the world. So there was kind of a wave of content that was critiquing this by making the character basically go through serious mental issues in the middle of the show. And I'm not saying this is better, but at least it's quite fun to have these really positive protagonists are just trying to help everyone around them.

Lenny Rachitsky (01:18:43):
I love how much we're learning about your personality hearing these recommendations. Nice protagonists, optimistic futures. I like the [inaudible 01:18:53].

Alexander Embiricos (01:18:53):
I think if you don't believe it, you can't will it into existence. So you need a balance.

Lenny Rachitsky (01:18:57):
This is your training data.

(01:18:59):
Is there a product you recently discovered you really love? Could be an app, could be some clothing, could be some kitchen gadget, tech gadget, a hat.

Alexander Embiricos (01:19:09):
Yeah, so I have been quite into combustion engines and cars. Actually, the reason I came to America initially was because I wanted to work on US aircraft, but now I work in software. And so for the longest time, I've basically only had quite old sports cars, old just because they were more affordable. And then recently we got a Tesla instead. And I have to say that I find the Tesla software quite inspiring. In particular, it has the self-driving feature. And I've mentioned a few times today, I think it's really interesting to think about how to build mixed initiative software that makes you feel maximally empowered as a human, maximally in control, but yet you're getting a lot of help. And I think they did a really good job with enabling the car to drive itself, but all these different ways that you can adjust what it's doing without turning off the self-driving. So you can accelerate, it'll listen to that. You can turn a knob to change its speed. You can steer slightly. I think it's actually a masterclass in building an agent that still leaves the human in control.

Lenny Rachitsky (01:20:21):
This reminds me Nick Turley's whole mantra is, "Are we maximally accelerated?"

Alexander Embiricos (01:20:26):
Yeah.

Lenny Rachitsky (01:20:26):
Feels like it's completely infiltrated everything at OpenAI, which makes sense, that tracks.

(01:20:32):
Two more questions. Do you have a life motto that you often think about and come back to in work or in life that's been helpful?

Alexander Embiricos (01:20:39):
I don't know if I have a life motto, but maybe I can tell you about the number one company value from my startup.

Lenny Rachitsky (01:20:45):
Love it.

Alexander Embiricos (01:20:46):
Which is still something that sticks with me, which is to be kind and candid.

Lenny Rachitsky (01:20:51):
That tracks. Kind and candid. Wow, that's a great combo.

Alexander Embiricos (01:20:54):
Yeah. And we had to put them together because we, as founders, realized that we often would be nice and it wasn't actually the right thing to do. We would delay the difficult conversations and we were not candid. And so every time we would remind ourselves of this motto and then we would become more candid. And then six months later, we would realize that we were in fact not candid six months ago and we needed to be even more candid. So then the question is like, "Okay, how should we be candid?" It's like, "Okay, well, let's think of being candid as an act of kindness," but also think of that both in terms of doing it and willing ourselves to do it, but also in terms of how we frame it as people.

Lenny Rachitsky (01:21:32):
That is a beautiful way of summarizing how to lead well. What's the book about challenge directly but care deeply? Radical Candor.

Alexander Embiricos (01:21:43):
Yeah, yeah.

Lenny Rachitsky (01:21:44):
So it's like another way of thinking about Radical Candor.

(01:21:46):
Okay, last question. I was looking up your last name just like, "Hey, what's the story here?" So your last name is Embiricos, and I was talking at ChatGPT and it told me the most famous individuals with the surname are the influential Greek poet and psychoanalyst Andreas Embiricos and his relative, the wealthy shipping magnate and art collector, George Embiricos. So the question is, which of these two do you most identify with, the Greek poet and psychoanalyst or the wealthy shipping magnate and art collector?

Alexander Embiricos (01:22:19):
I think it's going to have to be the poet because he loved the island that our family's from.

Lenny Rachitsky (01:22:27):
Wait, you know those people? Okay, this is not news to you. Okay.

Alexander Embiricos (01:22:30):
Well, I mean, it's an enormous family. But it's like Greek, so these big families, everyone's your uncle.

Lenny Rachitsky (01:22:30):
Love this. Okay.

Alexander Embiricos (01:22:36):
You know what I mean? My mother's Malaysian and also everyone is my uncle or aunt in Malaysia too, if that makes sense.

Lenny Rachitsky (01:22:42):
Yeah.

Alexander Embiricos (01:22:43):
But yeah, he loved this island that the family initiated from. I believe, I don't actually know where that's shipping magnate lived, I think it was New York or something. But anyway, we all came from this island called Andros, which is a really beautiful place. And it's like there's more livestock there than humans. Not too many tourists go there. But I think part of what I think is really cool is he published a lot and a lot of his writing is about the beauty of that island, which I think is super cool.

Lenny Rachitsky (01:23:12):
Wow, that was an amazing answer.

(01:23:14):
Two more questions, where can folks find you if they want to follow you online and maybe reach out? And then how can listeners be useful to you?

Alexander Embiricos (01:23:20):
I'm one of those people who has social media only for the purposes of having work. My phone turns black and white at 9:00 PM at night. But yeah, so Twitter or X, @Embirico. And yeah, if you post in r/Codex, I'll probably see it. So you can go there.

(01:23:40):
How can listeners be useful? I would say please try Codex, please share feedback, let us know what to improve. We pay a ton of attention to feedback. I think, honestly, the growth has been amazing, but it's still very early times, so we still pay a lot of attention and hope to do so forever. And also, I would say if you're interested in working on the future of coding agents and then agents generally, then please apply to our job site and/or message me in those social media places.

Lenny Rachitsky (01:24:10):
Alexander, this was awesome. I always love meeting people working on AI because it always feels like this very, I don't know, sterile, scary, mysterious thing. And then you meet the people building these tools and they're always just so awesome, and you especially, just so nice. And like the examples you shared, optimism and kindness, this is what we want to be. These are the kinds of people we want to be building these tools that are going to drive the future. So I'm really thankful that you did this. I'm grateful to have met you, and thank you so much for being here.

Alexander Embiricos (01:24:45):
Yeah, thanks so much for having me. This was fun.

Lenny Rachitsky (01:24:48):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

