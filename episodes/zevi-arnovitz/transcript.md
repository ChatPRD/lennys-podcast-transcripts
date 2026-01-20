---
guest: Zevi Arnovitz
title: "The non-technical PM's guide to building with Cursor | Zevi Arnovitz (Meta)"
youtube_url: https://www.youtube.com/watch?v=1em64iUFt3U
video_id: 1em64iUFt3U
publish_date: 2026-01-18
description: "Zevi Arnovitz is a product manager at Meta with no technical background who has figured out how to build and ship real products using AI. His engineering team at Meta asks him to teach them how he does what he does. In this episode, Zevi breaks down his complete AI workflow that allows non-technical people to build sophisticated products with Cursor.

*We discuss:*
1. The complete AI workflow that lets non-technical people build real products in Cursor
2. How to use multiple AI models for different tasks (Claude for planning, Gemini for UI)
3. Using slash commands to automate prompts
4. Zevi's 'peer review' technique, which uses different AI models to review each other's code
5. Why this might be the best time to be a junior in tech, despite the challenging job market
6. How Zevi used AI to prepare for his Meta PM interviews"
duration_seconds: 4512
duration: '1:15:12'
view_count: 0
channel: Lenny's Podcast
keywords: []
---

# The non-technical PM's guide to building with Cursor | Zevi Arnovitz (Meta)

## Transcript

Lenny Rachitsky (00:00:00):
You are a product manager shipping product without knowing how to write code, barely knowing how to review code.

Zevi Arnovitz (00:00:05):
I have zero technical background, did music in high school ... when Sonnet 3.5 came out. I remember watching a YouTube video building apps using Bolt or Lovable. It basically felt like someone came up to me and said, "You have superpowers now."

Lenny Rachitsky (00:00:20):
These days, you're using Cursor with Claude Code.

Zevi Arnovitz (00:00:23):
If you're non-technical like me, code is terrifying, but AI just makes it so much possible. In the next coming years, I think everyone's going to become a builder. Titles are going to collapse and responsibilities are going to collapse.

Lenny Rachitsky (00:00:35):
The main challenge people have is reviewing the code that AI has written.

Zevi Arnovitz (00:00:40):
It's very difficult for me to catch mistakes. What I'll do is basically /review. This tells Claude to start reviewing its own code, but what's even cooler is I have Codex as well as Cursor open. I will have each of them review the code.

Lenny Rachitsky (00:00:55):
This comes back to this quote. I think everyone's always hearing. It's not that you will be replaced by AI. You'll be replaced by someone who's better at using AI than you.

Zevi Arnovitz (00:01:05):
It's the best time to be a junior, contrary to what a lot of people are saying, how there's no more junior roles out there. Yeah, that's true, but also when else in history could you get out of school and just build a startup on your own?

Lenny Rachitsky (00:01:18):
Today, my guest is Zevi Arnovitz. Zevi is a PM at Meta. Prior to that, he was a PM at Wix, and this is a truly remarkable conversation that every non-technical product person needs to hear.

Zevi is super young and has no technical background, but as a smart, young, ambitious person, has learned how to use Cursor and Claude Code to build significant and real products completely on his own, and he's created his own very clever and effective workflow that everyone listening can copy.

To make that copying even easier, at the top of the show notes of this episode, you can download all of the prompts and /commands and start doing all of this yourself.

Zevi shows you how to work with cursor to quickly add your ideas to Linear to explore your idea with AI, how to develop your plan, how to then build the thing, and then have different LLMs review your code and update your documentation, and then use all of this as a learning opportunity to develop your own sense of how things work.

I haven't stopped thinking about this conversation since we had it, and everyone needs to pay attention to what AI is unlocking for non-technical people. A huge thank you to Tal Raviv for encouraging me to meet Zevi. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It helps tremendously.

And if you become an annual subscriber of my newsletter, you get 19 premium products for free for an entire year including Lovable, Replit, Bolt, Gamma, n8n, Linear, Devin, PostHog, Superhuman, Descript, Wispr Flow, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, Mobbin, and Stripe Atlas. Head on over to lennysnewsletter.com and click product pass.

With that, I bring you Zevi Arnovitz after a short word from our sponsors. This episode is brought to you by 10Web, the company that pioneered AI website building before ChatGPT. In the last three years, over two million websites have been generated with 10Web's vibe coding platform. 10Web's vibe coding platform is a powerful way to build websites.

Think of it as lovable for WordPress, front end and backend. Users can build any website at any complexity, e-commerce, portfolios, information websites, blogs, and it comes with the WordPress admin panel and thousands of ready to use plugins. 10Web also offers website generation as an API as a service for SaaS companies, marketplaces, hosting providers, MSPs and agencies.

SaaS companies can embed it via API so that users can launch AI generated sites directly inside of their platform, connected to their own data. Agencies and MSPs can get a white label dashboard to manage clients and resell under their brand. Hosting providers can self-host the API builder on their own infrastructure.

Check it out at 10web.io/lenny and use code Lenny for exclusive free credits and 30% off API or white labeled solutions. That's the number 10web.io/lenny, vibe coding platform as an API. Today's episode is brought to you by DX, the developer intelligence platform designed by leading researchers.

To thrive in the AI era, organizations need to adapt quickly, but many organization leaders struggle to answer pressing questions like, which tools are working? How are they being used? What's actually driving value? DX provides the data and insights that leaders need to navigate this shift.

With DX, companies like Dropbox, Booking.com, Adyen, and Intercom get a deep understanding of how AI is providing value to their developers and what impact AI is having on engineering productivity. To learn more, visit DX's website at getdx.com/lenny, that's getdx.com/lenny. Zevi, thank you so much for being here and welcome to the podcast.

Zevi Arnovitz (00:04:30):
Thanks for having me, Lenny. I'm a huge fan of the show and tons of people that I've admired most and learned the most from. I've been on here, so it's a crazy moment for me. I'm really excited for this.

Lenny Rachitsky (00:04:40):
I really appreciate that. I want to start by reading actually a note I got about you from Tal Raviv, who is a previous podcast guest, many times newsletter collaborator. One of the most AI forward product managers that I know I've learned a ton from him. So here's what he said about you when he introduced us.

Zevi is the most hands-on vibe coding PM I know, and I've personally learned so much from him. His engineers at Meta ask him to teach them how to do what he does. Every time we get coffee, I repeatedly get this feeling of everyone needs to be hearing this.

Zevi Arnovitz (00:05:10):
That's so nice.

Lenny Rachitsky (00:05:12):
And so that's the goal. That's the goal of this conversation is to help more people hear what you figured out. We're going to get very hands-on. We're going to do a lot of show versus tell, showing people what you've figured out about how to be a PM, a non-technical PM building stuff.

I want to give people a little bit of background on you because I think this is going to inspire a lot of listeners to feel like they can also do what we're about to show you. This is going to look very advanced, but just give people a little bit of sense of just your background.

Zevi Arnovitz (00:05:35):
I'm very non-technical. I have zero technical background. Did music in high school. A lot of Israelis do technology units in the Army. I was not in a tech unit. And basically a year ago, I was traveling with my wife for three months in Asia and we were in Japan and that was around when Sonnet 3.5 came out.

And I remember watching a YouTube video. I think it was either Greg Isenberg or Riley Brown and they were basically building apps using, it was either Bolt or Lovable, just using AI.

And it was like a crazy moment for me because I was watching this and it basically felt like someone came up to me and said, "Hey Zevi, there's this cool new technology you should check out. You should really give it a try. Oh, and by the way, you have superpowers now."

And the second I got home from Japan, I didn't even unpack my bags, ran to my computer, opened Bolt, opened an account, and for the past year I've been building.

And the last thing I'll say on that is we talked about this a bit before we started recording, but I was prepping with Claude for the episode and I was trying to clarify what my goal is for this episode. And Claude said, "If people walk away thinking how amazing you are, you failed.

And if people walk away and open their computer and start building, you've succeeded." So I really hope that we can inspire some people to do the same.

Lenny Rachitsky (00:06:50):
I love that so much. I feel like that should be the goal for my podcast. If you're like, "I love that guest." It's less of a win. If it's just like, "Oh, I'm so inspired to do the thing that they figured out, that is the real win." I love, Claude is the best.

Zevi Arnovitz (00:07:00):
I agree.

Lenny Rachitsky (00:07:02):
Okay. So let's dive in and give people, let's start with kind of a high level overview of how you operate and you use AI in your job. What are the core tools and just what's kind of like the frame of reference for the workflow that you figured out and how you operate?

Zevi Arnovitz (00:07:15):
This all started where I was a project's power user. I love projects, GPT projects.

Lenny Rachitsky (00:07:20):
ChatGPT projects?

Zevi Arnovitz (00:07:22):
Yeah, exactly. GPT projects and Claude projects, which are basically a shared folder of chats which share both custom instructions and shared knowledge base. And I think it was around when GPT started using memory where I thought it was interesting, but it really annoyed me because I do a bunch of different things.

I'm a terrible runner, I'm a PM, I was a student, psychology student, so I had all these different facets of life. And what happened was the memory feature was mixing stuff up. So like I talked to GPT about running and it would say, "Oh yeah, after this 5K, you're going to crush all your next product reviews."

And it's like, okay, I understand that you have that in your memory, but it's just not relevant. And projects basically allows you to compartmentalize and have things within the right context. So tracking back to the story I told when we came back from Japan, I started building this app.

The first thing I noticed was that these products were built in a way where, and when I say these products, I mean Bolt and Lovable, were built in a way where they were super eager to write code. So their system prompt was you're a coding agent. So when you'd write something, they'd straight away start coding.

So at the beginning of a project, this was super fun and exciting because they just go and start building your app.

But later on when things got more complex, this created much more problems because planning is really important when you're implementing something technical and let's say you're implementing payments or something that's going to be a change to your database. If the coding agent is just like, "All right, I got it."

And just starts writing code, this always results in terrible things, some really gnarly bugs that I had. And to mitigate this, what I did was I created sort of a CTO. So again, I'm not technical. I have been in product for a while, but I know zero stuff about code.

So basically what I did was I created a CTO with the custom prompt of it being the complete technical owner of the project. So I told it, "I own the problem. I own how we want the users to feel. You're the complete owner of how this is going to be built. I want you to challenge me.

I don't want you to be a people pleaser." All these things that kind of mitigate the regular ChatGPT-isms. I always think about this where for some reason, the easiest way for me to think about AI is to imagine it as people.

And I think ChatGPT would probably be the worst CTO because it's such a people pleaser and it's so sycophantic where ... Just a short story I had a few weeks ago, I was trying to learn about Bun JavaScript, which was acquired by Anthropic and I was trying to understand what they do.

So I was talking to GPT and this wasn't within my co-founder CTO project and I asked it if it's similar to a different framework that I have in my app called Zustand, which nothing to do at all with what Bun JavaScript does. And basically GPT goes, "Oh yeah, it's exactly the same."

And then it started talking about what it meant and I was like, "Wait, no, these are not the same at all." And it said the most terrifying and hilarious thing. He goes, "Oh, I'm sorry. I thought you were just making this up and I was riffing with you."

And I was like, "Oh no, no, no, this is terrible." So basically if regular ChatGPT was a CTO, that would be the CTO who goes along with your dumbest ideas. So creating the project allowed me to mitigate that.

Lenny Rachitsky (00:10:15):
So this is, just to be super clear, you have a ChatGPT project that you've given a prompt to be your CTO of your product and being a non-technical person, this is kind of like the thing you talk to when, and we'll get to what you're actually using to build when you have questions about architecture and decisions that are technical.

Zevi Arnovitz (00:10:30):
Yeah. So now I'll show my full workflow and I don't involve GPT anymore, but I definitely would recommend, even though the technology has gone ... So when I started this, there was no plan mode or ask mode. It was just build on these products on Lovable and Bolt, and they've progressed a ton.

A lot of what I had as workflows have become ingrained in these products, which is really interesting. I would still recommend start with a project for, first of all, the reason that I said, and also it kind of puts you in a place where you're in a chatbot and not writing code.

So you take the time to converse and to learn, which I think is critical. And the second thing is if you're non-technical like me, code is terrifying. It's the scariest thing in the world to look at, and I look at it as kind of like exposure therapy.

I think if you see this where I'm working like in Claude or in Cursor, you might be excited to start using those, but I would really recommend starting slow with a GPT project, beautiful UI, super simple, then maybe graduate to like a Bolt or a Lovable, and then go to Cursor in light mode, slowly, slowly, gradually ease in until you open a terminal, go full dark mode, go full dev.

So I would really recommend doing this gradually.

Lenny Rachitsky (00:11:40):
That is awesome advice. And so just to be clear, these days you're using Cursor with Claude Code powering it. And what I love about that is that you've never written code. The way you put it, you're afraid of even looking at code.

Zevi Arnovitz (00:11:50):
Yeah, 100%.

Lenny Rachitsky (00:11:52):
You can do exposure therapy, and I love that Cursor is useful to you. And what you're telling us is that graduating from a ChatGPT project that is kind of your technical co-founder kind of taught you enough to feel more comfortable going straight to cursor.

You said that you actually went to Bolt and Lovable kind of in the interim and then you went just straight to Cursor. What's the reason to just go straight to Cursor? Is it just Cursor can do everything and once you get the hang of it, it's actually the most powerful tool?

Zevi Arnovitz (00:12:15):
Yeah, I think I graduated from each tool when I kind of outgrew it. So Bolt was awesome until I was trying to connect payments to my app and I kind of started losing it and then I graduated to Cursor and I've actually fallen in love with Claude.

So I'm using Claude Code, but that also runs within Cursor, and I think this is Tal who told me this. I'm not sure who he's quoting, but code is just words at the end of the day. So it's just files on your computer.

So basically you can be working on the same project and carry it from app to app. And especially now, I can work with multiple models and apps on my project. So start slow, but definitely there's a lot of places you can graduate to.

Lenny Rachitsky (00:12:50):
Awesome. Okay. Should we dive into screen share showing how you operate?

Zevi Arnovitz (00:12:55):
Awesome. I pulled up cursor. Can you see it?

Lenny Rachitsky (00:12:58):
Mm-hmm.

Zevi Arnovitz (00:13:00):
Perfect. So within my code base, what you can see here on the left, these are all my code files. Here on the right is Cursor. So this is basically like having AI, which has access to all the code. And here in the middle, I have Claude Code running.

And what you can see here, I'm going to close cursor for a second. What you can see here are all my /commands. Basically what /commands are, they are reusable prompts that I save within the code base that I can run by writing / and then the name of the file.

So here you can see Create Issue, which is the first command that I'm going to use. And basically what this tells Claude, it says the user is meant development and thought of a bug or a feature and improvement, capture it fast so they can keep working.

And then it basically says, this is the format that I want you to capture the linear issue in, and it explains a bunch of things what exactly Claude needs to do to get there. So the way I invoke this is basically I'll do /create issue and this injects this prompt into Claude.

So it says, "I'm ready to help you to capture this issue, what's on your mind."

So basically when I'll do this is if I'm working on a big project and I suddenly come across a bug or have an idea that I don't want to work on right now, but I want to work on later, I'll do this really quick and Claude's main goal is to quickly capture what I'm thinking about.

So quickly to run through my full workflow. So basically it starts with creating an issue. So this is the create issue /command, which basically tells Claude that I'm mid-development and it should quickly capture what I'm thinking about and create an issue within linear. Then later on, when I want to pick this up, I have the exploration phase.

Exploration phase is basically telling Claude, we're going to only explore what we want to solve here. It could either pull from linear or I can just speak freely to it. And what it will do is it will analyze and understand the issue and just ask clarifying questions.

The next phase after we've done finished exploration phase is we're going to create a plan. So you can see create plan.

This basically has a template that I love for creating plans, and the output of this at the end of the day will be a markdown file with our plan that we can end up building along with code. After creating the plan, we have execute plan.

After execution, we have review and then we have peer review, which is really cool and we'll get into later on, and at the end, we update the docs. So this is updating documentation and everything so that agents can write better code later on.

So I think what we'll do is we're going to build a feature live for my app, which I think is really cool. But first what I'd like to do is show you the app so you have some context. So this is StudyMate.

It's a platform for students, which allows them to upload study materials and create interactive tests based on their own materials. So here we can go to the top. Let's upload a PDF. We can decide what pages we want to be quizzed on. We can decide the number of questions, the difficulty level.

And basically what happens behind the scenes is we send the information the user uploaded along with the system prompt and any other augmentations the users decided to Gemini and we create a quiz. These are challenging questions that are meant to assess comprehension.

You even have some hints and once we do a few of these, we can submit ... I got them right?

Lenny Rachitsky (00:16:00):
Terrible results.

Zevi Arnovitz (00:16:02):
Yeah, lucky.

Lenny Rachitsky (00:16:04):
And so just to be really clear about this, this is like a side business that you have, an app that you built that's making money. That's like a thing you vibe coded having no technical experience.

Zevi Arnovitz (00:16:12):
Yeah, this is my weekend project. Yeah. This is what I do.

Lenny Rachitsky (00:16:15):
Amazing.

Zevi Arnovitz (00:16:17):
On weekends. Yeah. So you get basically deep explanations into why each question was wrong or each question was right. And at the moment, StudyMate only has multiple choice questions.

And I was doing some competitor research over the last weekend and I saw competitors who had true or false questions and also fill in the blank questions, which I loved. So I think that'd be really cool if we could build that live. How's that sound?

Lenny Rachitsky (00:16:40):
I love it. Crossing your fingers, this all work. I just want to highlight the stuff you shared right before this in cursor. So this is a huge deal, what you describe here.

This is essentially what you've figured out is a way as a person that has no idea how to write any code, how to build a product in Cursor as a product manager using this series of /commands that you've concocted that you're going to be sharing with listeners. They can download all these and just use them directly.

They don't have to figure out all these prompts that you've figured out.

Zevi Arnovitz (00:17:05):
Yeah, 100%. Basically what happened was I formulated the backbone of this with the CTO, and it was basically within the system prompt of the CTO project that I had within GPT. So it said, step one, we do this. Step two, we do this. And now I'll keep building.

And if I see something that happens over and over again, I'll just create a /command and then it will be automated within the workflow.

Lenny Rachitsky (00:17:25):
Amazing. So just to summarize the /command. So one is create an issue in Linear, which I love. Linear is awesome. Shout out Linear.

Zevi Arnovitz (00:17:32):
That's also from the product pass.

Lenny Rachitsky (00:17:34):
From the product pass. Oh my God, what a value? Okay. So step one is create the issue in linear. So it's a command. So this prompt /command you've created, just create issue. Then it's explore, which is explore the idea, help me ideate on what this could be.

And this is Claude helping you think through the feature and product. And then it's actually create the plan. And so it's like the AI helping you build the plan to build the product. Then it's actually execute, which is just build the thing. And then there's this review, peer review step, which is awesome that you'll share.

And then there's document, update documentation based on the new feature that we're adding. Sweet.

Zevi Arnovitz (00:18:05):
Yeah. Cool. So let's go ahead and start building. So I'm going to use Wispr Flow to dictate and basically this starts with /create issue. So this basically sends that prompt. And I love this because I usually do this during when I'm building something else.

So basically it tells Claude that I'm mid building something and I don't have a lot of time to waste time on this. So just ask some brief questions so that you have enough to capture within linear. So I want to add fill in the blank questions to StudyMate.

I want this to be 30% of tests to be generated as fill in the blank questions. I want there to be six potential answers for two blank spots, and of course there's only going to be two correct answers.

So one correct answer and two incorrect answers for each spot and I want the interface to be drag and drop. So that's just basically a quick think of how I want this to work. So it's going to ask me a few questions. Quizzes are 100% multiple choice, question structure, single sentence passage to blanks and priority.

So one and two are correct, and this is not high priority. It's a nice to have feature. So now basically what Claude is going to do is it's going to use MCP, which is basically a technology that was created by Anthropic, which gives AI the ability to use tools. So this is connected to my linear.

So what it's going to do now is it's going to use everything we've said and create an issue within Linear.

Lenny Rachitsky (00:19:20):
And by the way, as this is loading, I just love the way, the way you described this, especially doing voice mode, it's like exactly how you would talk to an engineer describing a feature, "Here's what I want." And then they ask you questions, here's the clarification.

Zevi Arnovitz (00:19:32):
Yeah. So at first when I was doing this with the CTO, I would do it with ChatGPT voice mode, and that was crazy. That literally felt like ideating with a person.

It would push back, ask questions, and maybe one day the coding tools will get there too, but that was exactly ... It really felt like sitting with my CTO. Great. So created STU88. So if we open up Linear now, we should be able to see ... Let's see where STU88. There it is.

Fill in the blank questions with drag and drop interface. So it has a TLDR, it has the current state. It did a little bit of research on the code base, I think, expected outcomes, some context. So yeah, so this is basically ready for me to pick up when I'm interested in building.

So now let's say a few days go by, I finished the current project I'm working on, I can pick it up. So when I pick it up, I do /exploration phase, which is what we said. And then instead of pressing enter, I'll press tab and I'll show you this.

So basically, exploration phase, what it does is it will take an argument. This is basically a placeholder within the prompt, which allows me to enter something that is extra context for the AI. So I can say here, Linear STU88, which is referencing the ticket.

And now what it's going to do is it's going to go, it's going to fetch the Linear ticket.

Lenny Rachitsky (00:20:45):
And what's the idea? What's the goal of the exploration phase? This ideate on the idea. Is that the-

Zevi Arnovitz (00:20:50):
Exactly.

Lenny Rachitsky (00:20:52):
Okay.

Zevi Arnovitz (00:20:54):
So it's both for the CTO to deeply understand the problem that we're trying to solve and also understand the current state of the code base, what files need to be affected, and how is the best way to implement this technically.

And usually what happens is right now, Claude is just basically reading a bunch of files, understanding the basic structure of the code, and then it's going to come back with a bunch of clarifying questions that will decide how we end up implementing this.

Lenny Rachitsky (00:21:15):
So it feels like it's talking to your engineering manager.

Zevi Arnovitz (00:21:18):
Exactly, exactly. 100% this is how I think about it.

Lenny Rachitsky (00:21:21):
And you said that you're a CTO, so you used to use ChatGPT prompt to have a CTO in there. Now the CTO's living inside here in Cursor?

Zevi Arnovitz (00:21:28):
Yeah, because of the way the tools have developed and they've become so good at both exploration and code execution. So now it's just a habit that I call it a CTO, but it's basically all in one. The same agent will both do the exploration and write the plan and end up executing the code.

Lenny Rachitsky (00:21:42):
Got it. So it's basically it's Claude Code. Is there a prompt you gave it to act like that? To act like the right kind of CTO?

Zevi Arnovitz (00:21:48):
Yeah, so within the Claude.md, which is basically the system prompt that's loaded within Claude's context in every conversation, I have some basic stuff like this is our workflow, this is how we work. Within exploration phase, I want you to challenge my thinking, all kinds of stuff like that that can be loaded within the Claude.md file.

Lenny Rachitsky (00:22:05):
Cool. One last question before we move on here, just because I'm thinking about it as this happens, the Linear issue that you generated, how often is it actually great and ready? How often do you have to edit it? What's the quality of the Linear ticket that it generates?

Because a lot of people are probably wondering just like all these terrible linear issues are being created by AI. Are they actually any good?

Zevi Arnovitz (00:22:25):
It's completely different because I'm a company of one. So a lot of the context is within here and there's no need for me to talk to other teams and understand. It's basically very accessible, and also I can easily see when Claude understood something wrong.

I don't want to say that I would create Linear issues at work like this, but definitely if you're building your own side project, they're pretty quality. And also, it just kicks off when I want to start working on it. I wouldn't say it's ready to be built. It's ready to start being explored.

Lenny Rachitsky (00:22:52):
Got it. So it's just the beginning of an idea. Actually, let's come back after we go through this flow of how you would approach this if you were at say Meta or another, maybe a smaller company, how this workflow might work at a larger company that isn't just your own startup.

Zevi Arnovitz (00:23:05):
Yeah. Interesting.

Lenny Rachitsky (00:23:07):
Let's come back to that.

Zevi Arnovitz (00:23:09):
Cool. All right. So this is Claude coming back. I have a comprehensive understanding of the code base. I thoroughly analyzed StudyMate live codebase and understand the current system, feature quest and key areas that it's identified.

Usually I'd spend a lot of time going over this because this is super, super important, but just for the sake of development right now, we're going to brush through this. Now Claude basically comes back after it's gone through the code base and understood the way it currently works. It's basically telling me what the current understanding is.

So it's talking about how the app is set up at the moment, how the data is structured, what it understood from the feature quest, and what it has identified as key areas, and then it asks me some questions.

So it's asking about the scope, it's asking about the data model, the UX/UI of the feature, how it should be validated, how it should be graded, what changes need to be happened to the AI system prompt and all kinds of questions about the app.

I've prepared answers to all these questions beforehand because I don't think we all want to sit through this. So I'm just going to paste that in and we'll see what Claude says.

Lenny Rachitsky (00:24:10):
Awesome. I love it. And I love just scanning those questions I was asking. It's like such smart, sophisticated, important questions instead of just, "Cool, here I go, I'm going to build it."

Zevi Arnovitz (00:24:20):
Yeah, and I think this is the big difference between just vibe coding and going along with the vibes and really building serious apps. I spend a lot, a lot of time going back and forth and understanding.

Also, a very cool /command that I haven't showed yet is learning opportunity, which basically when something is really difficult for me to understand, I'll do /learning opportunity and then talk about what I want to learn. And this basically primes Claude and says, "I am a technical PM in the making. I have mid-level engineering knowledge.

I understand architecture and basically I want you to explain what we're currently working on using the 80/20 rule." So this is a great way to learn. I would definitely take this and every time you kind of see something that you don't fully understand, I would definitely use this to learn. Great.

So Claude basically comes back and says how it understands the current data model and how it's going to implement. Yeah, so it's ready to create the plan.

So basically what I'm going to do now is I'm going to go and do /create plan and while Claude is doing this, I'm going to show really quick what this looks like. So basically, these plans are from a template that I found on Twitter.

I forgot who it was, but it was just a template that really resonated with me. And it's basically saying, based on our exchange, create a markdown file that will be the plan, include clear, minimal, concise steps, track the status.

So this basically has like status trackers on each task that Claude updates as it's going through and it will have a TLDR, some critical decisions that we've made and the plan itself. So Claude has finished writing the plan, so we'll be able to look and see exactly what the plan is.

So it has a TLDR, it has the critical decisions we've made and the tasks broken down. And this is a perfect plan and it's also a really good way to write this because a lot of times, I'll use different models to execute certain stuff. So Cursor has an amazing model called Composer, which is superfast.

So a lot of things that are not that complex, I'll use Composer. Gemini 3 that just came out is unbelievable at UI. So a lot of times, I'll split the plan into backend and front end, and then I'll have Gemini just read the plan and do the front end.

So having this as a markdown file is really good. And also going forward, it's really good to have within the app so that later on, if an agent is writing code in a certain area, I can see what's already been done there. So what we're going to do now is we're going to execute the plan.

So now I think we're going to do this with Cursor just because Composer is so freaking fast. So what we can do is basically just say execute and then we can tag the file. And Composer is ridiculously fast. So that's it. It's off.

It basically understands what the plan is and it's going to go ahead and start writing the code.

Lenny Rachitsky (00:26:45):
Let me ask you a question while this is happening.

Zevi Arnovitz (00:26:48):
Awesome.

Lenny Rachitsky (00:26:50):
I have many questions, so this is a good time to ask a few of them. You said that Lovable and Bolt and other apps in that space are just not enough to build really serious apps and you have to move to Cursor to do that. Tell us more about that.

Just what's the limitation you ran into with those products and why you switched to Cursor?

Zevi Arnovitz (00:27:05):
I started using Cursor and Claude Code a few months ago and I haven't looked back, but at that time, these teams have been moving like crazy. So I don't want to say I wouldn't trust them. I don't know what the current state is.

But for me, it was basically the issue of I felt that Bolt was being very opinionated on how I should do things. And I felt like my knowledge has gotten to a point where I can graduate and be more in control. By the way, I think that the main difference between all these tools is basically the harness.

So the models are all the same models.

I'll run Claude within Cursor, I'll run it within Claude Code, and it's also the models that Claude is also the model that is underlying Bolt and Lovable, but basically, Bolt and Lovable will add a bunch of levels in the middle that will take all kind of guesswork and hard decisions out for the user.

So the user doesn't have to make these hard decisions. So it's also very easy to build, but the flip side of that is that you have less control.

And basically Claude Code is just taking Claude and shoving it straight in your code system and giving it full tools and to do whatever it wants, but also with that comes a lot of decisions that you need to make.

So I don't know if you can't build really amazing production apps using Bolt or Lovable now, but I think basically if you want the most cutting edge abilities of the models and you want to be able to make all the decisions on your own, it's probably best to be on one of these tools.

Lenny Rachitsky (00:28:20):
What I'm feeling and hearing is that planning work that you did, that's the stuff that Lovable, Bolt, and would you put Replit in that bucket too?

Zevi Arnovitz (00:28:28):
Yeah, for sure. Lovable, Bolt, Replit, Base44.

Lenny Rachitsky (00:28:32):
v0.

Zevi Arnovitz (00:28:34):
Yeah, v0, all same bucket.

Lenny Rachitsky (00:28:36):
So essentially, they're doing that planning for you. And as you said, they're very opinionated. They try to make it easy. So it's just like, "Here's how to do it. Here's the way we think is best for people."

And what you're saying is once you're trying to get a little more serious about it or want to go in a different direction, you don't have the power to change how they plan. So Cursor lets you do that.

Zevi Arnovitz (00:28:55):
Yeah, I don't want this to come out like I'm badmouthing them. Base44, let's say.

Lenny Rachitsky (00:29:00):
No, absolutely.

Zevi Arnovitz (00:29:02):
Yeah. Base44 does an amazing job at basically taking all the complex guesswork out of building product and just allows you to just go with the vibes and build, but it will do sign in with Google for you and it will do a database, but then you don't have decisions on what database am I using.

Do I need sign in with Google this way or another way? It would just do it out of the box. So that's basically the trade-off there.

Lenny Rachitsky (00:29:22):
Awesome. Shout out Maor, the founder of Base44.

Zevi Arnovitz (00:29:25):
Yeah. Maor Shlomo. Yeah. He's amazing.

Lenny Rachitsky (00:29:28):
Okay. I just love how this is like the way you're like flinging, what's the word? Slinging models like Gemini 3 for frontend. I love that you've never written any code and you're just like, "Cool, use Gemini for this and Claude for this.

And I'm just working on Cursor, talking to this CTO, helping you build stuff and build significant product."

Zevi Arnovitz (00:29:45):
Yeah. We just live in the craziest of times where basically the world changes once a week, it feels like. And there is just no boundaries. You can use all of these just on your regular MacBook or regular laptop.

And I have these moments, I call them time machine moments, which is basically this week, for instance, I was prepping for the podcast using Claude with a project. I was building, I was fully localizing StudyMate from Hebrew to English, which I did in two days, which would probably take a dev team weeks.

And I was building a personal site, which went from no domain, no nothing, to live on a domain within an hour and a half. And I was doing all three of these in parallel. And there was a point where basically all three of the agents were running, so I didn't have anything to do.

I just had to let them think, and these are the time machine moments where I feel like I was in the future and I just stick my head out of the time machine and whoever's next to me, at the moment it was my wife, I'll just say, "We live in the future." And she'll be like, "Huh, what?"

And I'll be like, "No, no, don't worry about it." But it's just basically so crazy that all these things are just an API away. You can use anything. So I think it's an awesome time to be curious and optimistic and hardworking.

Lenny Rachitsky (00:30:50):
These are my favorite kinds of podcast guests. People that are living in the future, figuring out all these things and then are just kind of come back, as you said, poke your head out of the rocket ship and just like, "Hey, here's this thing that I figured out. Here's where we're going."

Zevi Arnovitz (00:31:02):
Yeah, best time to be alive. So awesome. So it looks like it's finished. So now what we're going to do is we're going to run the app locally and we'll be able to see what Composer ended up building and we're going to see if anything else is needed on our end to maybe do some manual review.

Does that sound good?

Lenny Rachitsky (00:31:18):
Sounds great. And I love, that was like, I don't know, a few minutes where if it was a human engineer, it'd be like days, maybe a week for work.

Zevi Arnovitz (00:31:25):
For sure. Yeah, for sure. No, Composer like the one thing is it's just so, so blazing fast, keeps you in flow. So yeah, full features take minutes.

Lenny Rachitsky (00:31:33):
And it probably costs a couple bucks in AI credits.

Zevi Arnovitz (00:31:36):
I don't even look. I used to be so stingy about paying for products and now I'm just basically, I look at it all as tuition, as stuff that I'm paying for learning. So I don't know how much it costs, but it's definitely worth it.

Lenny Rachitsky (00:31:47):
That explains why they're the fastest growing products in history.

Zevi Arnovitz (00:31:50):
100%.

Lenny Rachitsky (00:31:52):
Your marketing website sets the tone for your brand and is the one touchpoint that every single one of your customers sees. In today's age, if you're still having a hard time making small changes and simple updates to it, you are doing something wrong.

That is why so many companies from early stage startups to Fortune 500s, including companies like DoorDash, Zapier, Perplexity, and ElevenLabs turn to Framer, the website builder that turns your .com from a formality into a tool for growth.

Framer works like your team's favorite design tool and comes with real-time collaboration, a robust CMS with everything you need for great SEO and advanced analytics that includes integrated AB testing. Changes to your Framer site go live to the web in seconds with a single click and without any help from engineering.

Whether you want to launch a new site, test a few landing pages or migrate your full.com, Framer has programs for startups, scale-ups, and large enterprises to make going from idea to live site as easy and fast as possible.

Learn how to turn your website into a growth engine from a framer expert or get started building for free today at framer.com/lenny, that's framer.com/lenny. Rules and restrictions may apply.

Zevi Arnovitz (00:32:55):
So now we have this feature, which basically we built and I can ask it to make some changes because it's running locally and once it's ready, I'll be able to ship it to users. So now the next phase after I've QA'd it and basically tested it manually, I'll have Claude review its own work.

So what I'll do is I'll reopen Claude Code.

Lenny Rachitsky (00:33:12):
I love this because this is one of the things that comes up a lot in this podcast is writing code is now so easy. The main challenge people have is reviewing the code that AI has written.

Zevi Arnovitz (00:33:22):
100%.

Lenny Rachitsky (00:33:24):
And what you're doing here is you're having Claude review its own code.

Zevi Arnovitz (00:33:28):
Yeah, so this is another thing where it's very difficult for me to catch mistakes. So my review process has gone through a bunch of iterations to really be as good as possible and to catch as many things as possible. So I'll always manually QA at first to make sure if I can see any mistakes that Claude made.

And then what I'll do is basically /review. And this tells Claude to start reviewing its own code.

But what's even cooler and something that I'm really proud of is I will usually do multiple reviews and I'll have Codex, which is ChatGPT's competitor to Claude Code, as well as cursor open, and I will have each of them review the code.

And then what I do is I have a /command called peer review, which is really interesting. And basically what it does is it's going to take Claude, which is usually the agent who I'm working with. And just to put this in a mental model, this is basically my dev lead that I'm working with.

The /command is basically saying, "You're the dead lead on this project. Other team leads within the company have looked at your code and reviewed it and found these issues." Don't take what they said at face value. The reason is you have more context than them and you led this project.

You need to either explain why the stuff they found are not real issues and wrong or fix them yourself.

And it's really cool because the way I look at these things is I look at the models, I try to imagine them as people and I can really tell you how each one of these would be as a real human because they have-

Lenny Rachitsky (00:34:50):
Each model.

Zevi Arnovitz (00:34:52):
Yeah. Each model has such distinct characteristics. So let's say Claude, she would be the perfect CTO. She's very communicative. She's very smart. She doesn't just go with the flow and do whatever you tell her.

She's very opinionated, but also super collaborative, which is I think why I'm always drawn to Claude because I need to do so much learning and it's your dream, a very communicative, but very opinionated dev lead, but then there's also Codex. So I use Codex 5.1 Max, whatever.

I don't know, they're not the best at naming models, but GPT's model. I always imagine it as like the best coder within the company who comes to the office with a hoodie and sandals and sits in a dark room.

And you basically only bother him when you have the worst bugs and you say, "Listen, we have this bug and it will just close the door for two hours and come out and say, I fixed it." And you're like, "Wait, what? Are you going to tell us what happened or whatever?" And he's like, "Don't worry about it.

I fixed it." It's like really not communicative, but it solves all the worst problems. And let's say Gemini is like a crazy scientist who's super artsy, super talented at designing, but if you sit next to it and watch it work, it's terrifying. You would fire that person instantly.

This might be just my experience, but when I'm using Gemini within antigravity, which is Google's new competitor to Cursor, when it's writing code, you can see the steps it's taking and it's terrifying. You'll say, "I want you to redesign the top of the dashboard."

And you're looking at its thought process and it will say, "Oh, first things first, I'll delete the dashboard." And then it'll be like, "Nope, that was a mistake. I'll bring it back." And then it will say, "Oh, can I edit the database?" And you're like, "No, do not edit the database. You're just doing a redesign."

And then it will end up designing something beautiful. So the way there is a rollercoaster and very scary, but at the end of the day, Gemini is very good at design. So I think that using all these models and basically playing to their strengths and mitigating their weaknesses by using other models is a game changer for me.

So I'll do peer review a bunch of times and I'll have other models review other models code and kind of have them fight it out basically. Sometimes Claude Code will get really sassy and be like, "This has been raised for the third time. And for the third time I'm telling you, this is not an issue.

This is by design." So it's just a really cool thing that I've added and I haven't seen many people doing it.

Lenny Rachitsky (00:37:05):
That is such an incredible rant/way to understand what's going on. Okay, awesome. So we just ran the review. So show us what we saw there and let's actually try this peer review. I'm really excited to see what you learned there.

Zevi Arnovitz (00:37:18):
Yeah. So basically Claude has reviewed its code and it's found a bunch of bugs, a critical bug it found in the prompt, some high bugs, some medium bugs, and now what I'll do is I'll do the same thing with the other models.

So Codex has a built-in code review that you can do, or I just like to say review all the code in this branch. Of course, branch is referring to the GitHub branch that we're working on. We're not working on the live code base. And then I'll do this with Composer say with, let's do it with Composer One.

So I'll do /review here as well. And basically these are both going to run and do a in-depth review similar to what Claude does. But again, because of the differences between the models, they're all going to catch different things and they're all going to look differently, and this is a really cool way to work.

It's basically if you had other team leads within the company review the code. Here, you can see how fast Composer is. I think GPT probably will take a bunch of time. Like I said, it's in its own dark room right now reviewing code and we'll come back in a few minutes.

Lenny Rachitsky (00:38:15):
Okay, cool. So we can let these run in. We don't actually have to go through the whole process, but is the idea once you get these results, you run peer review and you copy and paste kind of these results. Is that the idea?

Zevi Arnovitz (00:38:25):
Exactly. I'll copy and paste the results. I'll do peer review and then I'll say dev lead one and then paste from one of the models. And then I'll say dev lead two and paste from the other model and basically have them fight it out until I feel like we have no more issues.

Lenny Rachitsky (00:38:40):
Incredible.

Zevi Arnovitz (00:38:42):
For me, this is super important because I'm not technical and I'm not a developer. And I'll also use /learning opportunity a bunch during this to learn about stuff that I don't understand or don't fully grasp.

Lenny Rachitsky (00:38:52):
Incredible. What a clever solution to solving this code review problem where it's like, I don't know what you ... I don't know how to recode, so what am I going to even ... Yeah.

Zevi Arnovitz (00:39:00):
Yeah.

Lenny Rachitsky (00:39:02):
Okay. Incredible. Let's wrap up this workflow. Is there anything else that's important in this workflow? And again, all this stuff is going to be available where people can just plug this stuff into their Cursor account and use it themselves.

Zevi Arnovitz (00:39:12):
100%. The one thing I'll say is that I think just like working in general with AI and even just like working on any product, doing constant postmortems is critical. So a lot of times we'll find all these kind of bugs or maybe Claude will fail to execute something correctly.

And at the beginning when I started vibe coding, I would basically just keep running at it like running at the wall and until it worked. And once it worked, I was like, "All right, awesome. This works. Let's keep going." But I've learned over time that updating documentation and tooling is one of the biggest hacks for productivity.

So when Claude will fail to do something or I'll see this really bad bug that shows that Claude really didn't understand something, I'll ask it, "What in your system prompt or tooling made you make this mistake?" And Claude will kind of like go introspective and think of what made it create that mistake.

And then I'll say, "Okay, great. Let's update your tooling and documentation so that this mistake never occurs again." And I do this every time I'm either building an internal tool or anything. And I think this is just like working.

If you end up doing a bunch of mistakes and then end up releasing the feature to users, so you're like, "All right, it's a big success." But going back and even when you've succeeded, looking and understanding what you did and what you could have done better is critical.

And also using AI, this is probably one of the biggest unlocks.

Going back to your prompts, understanding what was not good enough, iterating on them and then seeing how AI's responses get better, I think that's probably one of the most important things and one of the things that divides between people who are okay with using AI and the people who actually know how to use it.

Lenny Rachitsky (00:40:40):
That is such good advice. So what I'm hearing is when the models do something dumb, make a mistake, you ask it to reflect on what the mistake it made was, and then you update the /command prompts with that knowledge so that in the future, it's not making that same mistake, and it just keeps getting better.

Zevi Arnovitz (00:40:55):
Exactly.

Lenny Rachitsky (00:40:57):
These things just keep getting smarter and smarter. So you're building up this really incredible prompt that just gets better and better.

Zevi Arnovitz (00:41:02):
Exactly. Not always the /commands. It will sometimes update different documentation or its tooling, but basically it's understanding what the root cause of the mistake that the AI made and fixing it.

Lenny Rachitsky (00:41:12):
Awesome. So the models are getting smarter and then there's also the other parts of your workflow can get smarter as you find flaws in the way it does stuff.

Zevi Arnovitz (00:41:20):
100%. Yep.

Lenny Rachitsky (00:41:22):
Amazing. Okay. Is there anything else there before I move in a couple other directions?

Zevi Arnovitz (00:41:27):
I think that's it. I think we covered pretty much everything. Basically, just to wrap this up, what I do is I do a bunch of code review and then update the documentation so that everything is documented. So the next time I try to build a feature in this area, there won't be any mistakes.

And then I'll do a bunch of testing. I'll do some user testing as well before I release this to general availability. Obviously we're not going to release this. This was just a show, but hopefully maybe by the time the podcast comes out, I'll have done this correctly and release the feature.

Lenny Rachitsky (00:41:55):
It's incredible that this was not possible, I don't know, two years ago, maybe a year ago, you are a product manager shipping a product without knowing how to write code, barely knowing how to review code. You said you're afraid of looking at code.

As a product manager, you're building a product in Cursor using all of these different AI models. You're making money with this product. We're so used to this now, but it's insane what is now possible.

Zevi Arnovitz (00:42:15):
It's the best time to be live. 100%. I think that I understand the fear, but AI just makes it so much possible. Just a quick side note here, my brother, who I'm building one of the apps with is an entrepreneur. He has a beautiful business that helps old people and seniors understand to use technology and AI better.

And he's basically doing the same kind of learning as me, and he's replaced all of the tools he was paying for. I think he was paying for Zapier and Airtable, and he's basically built a full-fledged CRM system and automation system for his business completely alone.

So for the people who are curious, optimistic, hardworking, this is the best time to be a builder.

Lenny Rachitsky (00:42:50):
And what I love about this conversation we're having here is it feels like the biggest barrier for a lot of people is like, how do I get started? What exactly do I do? I open up cursor. It looks very intimidating. I don't know how to write code. I don't know how to build stuff.

I don't know about databases. And so you're going to be sharing all these /commands and basically this whole workflow with the audience.

Zevi Arnovitz (00:43:08):
Yeah.

Lenny Rachitsky (00:43:10):
Okay.

Zevi Arnovitz (00:43:12):
And like I said, just start at GPT. Start on GPT, tell it what your idea is, tell it to explain to you what are even the first steps of thinking, what are the decisions you need to make? And just be inquisitive, learn. Don't rush things.

It's very important to just dive in and really spend the time to learn.

Lenny Rachitsky (00:43:28):
And you share this. One of your /commands is learning opportunity, and it's how you learn a lot of these things. Just teach me this thing and how this database issue works.

Zevi Arnovitz (00:43:35):
Exactly.

Lenny Rachitsky (00:43:37):
Okay. There's a couple directions I want to make sure we touch on. One is coming back to a question I asked earlier about how this might work at a larger company. Say it's not like Meta, but just like, I don't know, a thousand person company, 500 people.

How much of this can you plug and play into a workflow as a PM at a larger company? What would be your advice for someone that may want to start trying to ship code, at least showing people what's possible?

Zevi Arnovitz (00:43:58):
I think that first making your code base AI native is a really important step, and I think this needs to be done by technical people. So basically my codebase has a ton of just plain text in it.

So it will have a bunch of markdown files that explain to agents how to work in certain areas of the code base and high level structure so that the agents navigate through the code base easier.

And I think that if this is set up in a really good way, I still don't think PMs should be shipping heavy database chain migrations or any big project, but contained UI projects, especially if you just build it, create the PR and send it to a dev to do the final finishes.

I think that's definitely something that's possible. And I think we're going to see that a lot in the next coming years. I think basically everyone's going to become a builder, so it should be really interesting.

Lenny Rachitsky (00:44:45):
Okay. So your advice here is as a PM, maybe don't go right to Cursor, start building, shipping, trying to ship features to production, especially complicated features. Do you think we'll get there? Do you think in a couple years, PMs will be doing this and it'll feel less scary and crazy?

Zevi Arnovitz (00:45:00):
If there are PMs. Yeah, I think titles are going to collapse and responsibilities are going to collapse and everyone's just going to be building. I definitely think that the models, the context window is getting bigger, the models are getting smarter and I definitely see how PMs or any other background can be writing.

At the moment, I wouldn't wait for that. I would use this as a collaborative learning opportunity to work with your dev team. It's going to be difficult.

A lot of developers are very, very skeptic about the current state, and I think that it's going to be a lot of sales work on your end to convince, but if you're able to convince, and I think teams that are really sold on this and want to take the time to work on their workflow about how can our team become more AI native, I think that these teams are going to probably be a few years in the future and they're going to look back at the few weeks they spent setting this up as the best time they spent.

Lenny Rachitsky (00:45:48):
Let me ask you another question around just the job of a PM. One of the biggest fears people have with these AI tools for PMs for every function I imagine is just you start to rely on these things, your skills start to atrophy, you're producing all this slop that looks great, cool, amazing strategy doc.

No, it's actually not at all good. Are these Linear tickets or just products that are half-baked? What's your take on these two parts of just like, how has this impacted your craft as a PM?

Do you feel like this is weakening your skills because you're so reliant on these tools and just how do you keep the quality of this stuff up and not just like, "Eh, it's just a bunch of AI generated slop."

Zevi Arnovitz (00:46:22):
I have a very strong disagree to this and I've heard it a bunch. I remember when I started using Tal Raviv has this whole course on building a PM Copilot using projects, which is probably one of the best courses that you can take.

And when I started working with my own Copilot, I remember people at work looking and saying like, "Oh, so you're basically outsourcing your thinking." And to me, that's just the worst way to look at it.

And I think for some reason, these people usually have a high correlation with the kind of person who doesn't like to show their presentation when it's only 10% done or doesn't want to ask for help a lot.

I think that there's a misconception with a lot of PMs that the job is always having the right answers and being the smartest person in the room. And at least how I was trained and how I believe the role of the PM is, it's the exact opposite.

It's basically harnessing anything that can get us as quick as possible to delivering the right solution to users. And I just think this is like that really smart person that has context or your mentor or whatever, but is just always available and doesn't judge you and can really help you.

So if you're using it to just create your outputs and then putting them out there, yeah, that's AI slot, but it's also human error. I think it's really important that you own your own outputs. If you put anything out there or show something in a product review and you say, "Oh, sorry, that was built by AI."

That's your mistake. I think if you use these intentionally and really take the time to understand how to use AI in the correct way, it's one of the biggest game changers that will make you much better as a PM.

And another thing here is that, especially for more junior PMs, it allows you to play at such a higher level than you would normally. I think that at Wix, I wasn't thinking of what's the marketing strategy of the company and how will the onboarding be completely revamped within the whole product.

But on my side product, I can just do whatever decisions I want and think of the strategy and marketing and the messaging. And this is basically just getting me reps, which is one of the most important things at the beginning of your career.

So I understand the fear that how do you outsource certain stuff and you're not owning 100% of everything, but I think the upside is so much more valuable. And I think the only way that AI makes you worse at your job is if you're using it wrong.

Lenny Rachitsky (00:48:28):
Is there anything that you've learned about reducing the sloppiness of the output, just like a tip for keeping the quality high of the stuff that it produces?

Zevi Arnovitz (00:48:36):
Similar to people, setting up AI for success, for the task at hand. So if I just brought in a junior to write a deck or something and I didn't give it any guideline, I just said, "Give a strategy deck."

He would probably just go online and find top strategy deck and just reproduce that, which is basically what AI is doing. It's basically just fed all of the internet.

So instead of that, guiding it and giving it context on what your style of writing is and what you're trying to solve and all these different things, I think that's probably one of the biggest unlocks. So that's just a quick tip. And also Cursor has a /command called deslop, which is basically going back over the code.

I don't know if this is integrated into the product yet, but it's on Twitter. Their founders have been talking about this, so that's definitely something I would run after just to make sure that no slop is left behind.

Lenny Rachitsky (00:49:22):
That is so funny, deslop. Okay. One more question, which may lead to something else, but kind of going in a whole different direction. You used AI to help you actually interview for the job that you got at Meta.

Talk about how you did that, because a lot of people right now are struggling to find a job reading about all these people using AI to help them interview. You actually did it. What did you use? What worked?

Zevi Arnovitz (00:49:45):
I feel like the analogy here is I have 12 nieces and nephews and you can see how people who have grown up in a different world, how their mind is formed differently. So if you ask me, how do you answer a phone, I'll do this. But a child now, when you say, "How do you answer the phone?"

They'll do this. They'll do the iPhone answer. And I feel like people who are growing up now in their professional lives were the same just with AI. So every time I'm faced with a new challenge or problem, I think AI first how to solve it. So Meta reached out and said they'd like me to interview.

Straight away, I opened up a project within Claude. I started looking online for all the best information out there, things that I resonated with. I took a ton of frameworks and stuff from Ben Erez who has written a guest post for you, who I think is one of the best minds out there right now.

And basically I created a project which was my coach, which I would come and consult what to do at each phase. I would mock interview with, and this was amazing. Also, I created a game in Base44, which helped me ... I was really struggling with segmentation within the product questions, so thinking of the correct segments.

So I basically just created a quiz game, which creates questions and different segmentations and I have to choose. So this was like, I spun this up. It's a web app that I would play sometimes when I was on the bus to work.

So basically, I think Ben talks about this a bunch, so I don't just go read Ben's stuff, but just creating a project and feeding it with all the best information on the internet and then mocking a bunch. I will say that the biggest game changer for me was doing human mocks.

So cold outreaching to people on LinkedIn and having them do actual mocks for me, I think that at the end of the day, especially for the Meta PM prep, which is super competitive and difficult, I think there's no way to get around that.

Lenny Rachitsky (00:51:30):
That is so cool they use that post. I wasn't aware. We're going to link to it. And in that post, Ben shares all these prompts you can feed ChatGPT to help you prepare for interviews, do mocks online. It's a really important point to say that those take you to a point, but it's actually better to use humans.

I actually have a post coming out soon in collaboration with Noam Segal about how everyone is using AI to interview. And one of the most interesting ways I've heard people and that we've found in this research was that people use it to get feedback. They record the interview and then it gives them feedback.

Here's where you could have done better. Here's what you missed because the feedback loop is so missing. No one ever tells you, here's what you did badly in this interview. No one tells you that, and AI can do that.

Zevi Arnovitz (00:52:10):
So I'll add two things to that. One, which is exactly this. So I'll mock with AI. Also, I did something really cool where there's a question bank online free by Louis Lynn, which basically is an always updating bank of questions that people are asked in real interviews. And I basically used Comet, which is the Perplexity's browser.

And I had the agent run all kinds of analyses on what the most asked questions are. And that's how I knew how to prioritize what questions I would mock. And then at the end of these mocks, I would tell Claude within the project, "You're my coach and I don't want you to make me feel good.

I want you to make me as ready as possible for these interviews. So give me feedback, like you said." And the other thing that I did was really cool was some questions where I didn't have time to mock. I would ask Claude to play the candidate, and then it would just give me a really good answer.

And I could also learn from that, like learning from someone who does a perfect answer.

Lenny Rachitsky (00:53:02):
Oh, man. I really love the way you phrased it, that people kind of in your generation, the default is, "I have something I need to do. Let's go to AI immediately and help me prepare for this thing, help me figure it out."

Zevi Arnovitz (00:53:12):
Yeah.

Lenny Rachitsky (00:53:14):
And this comes back to this quote that I always think about, which I think everyone is always hearing, but it's such an important quote that it's not that you will be replaced by AI at least for a long time. It's you'll be replaced by someone who's better at using AI than you.

Zevi Arnovitz (00:53:26):
I agree.

Lenny Rachitsky (00:53:28):
And that's what these conversations are for to help people keep up with all that and to learn some of these skills. And again, see where the future is going and start to learn how to get there yourself. Okay.

Zevi, before we get to our very exciting lightning round, I'm going to take us to a recurring segment on this podcast I call Failure Corner. And why I love this segment is people come on this, just even this conversation, it's like all these amazing things you figured out, everything is going so well.

People rarely hear the things that don't go well, and those are often the most interesting and impactful stories. So the question is just, what's the story of a time you failed in your career and what did you learn from that experience?

Zevi Arnovitz (00:54:05):
Yeah, I love this. I love this. I love Failure Corner, big fan. So I'll tell a story about when I started at Wix. So basically I started within Wix as a student program and straight out of the student program, you get put into a certain team.

So I was in the editor, which is the core product of Wix. And the other PMs were just the best PMs almost at Wix. There's four other people had much more experience than me and they were ridiculously good. And I remember coming in and thinking like, my first product review, I'm going to blow these people's socks off.

They're not going to believe how good of a PM I am. And I basically didn't really share what I was thinking. I would work tons of hours alone and I was like, "I'm going to kill this product review. They're going to be so impressed." And I ended up failing miserably. My product review was not good.

It wasn't the format they expected. They had a ton of questions that I missed and I felt awful when it was over. I was like, "Ah, you're such an idiot." And I saw that everyone was like, "All right, cool. Yeah, just come back in two weeks and we'll keep getting at this."

And I understood in that moment that they had zero expectation of me being a 10X PM, but the expectation of me was being a 10X learner. And the second I understood that, my whole mindset shifted.

And I think this is probably the best tip that I give now to junior PMs is basically be the best learner you can be at the beginning. No one expects you to know all the answers and no one expects you to be good.

So basically what I did was I took each person on the PM team, there was four other PMs and I assessed what their strength is and used them as a mentor for that. So Neri who's still my mentor till today, he has the best product sense of anyone I've met. Oya is super, she's like a methodology expert.

She just thinks in frameworks. Yahra, who is the head of product, basically can look at a product and then instantly understand the third and fourth order effects of them, the system thinking. So every time I had an issue with one of these areas, I would come to one of them and consult them, and this does two things.

First of all, I learned a ton. And the second thing is that when the next time, the next product review, my success felt to them like their success because it wasn't this kid who's trying to show us up how cool he is. It was like our mentee kind of making us all proud.

And it was such a great shift for me. And basically at the end of the day, I really excelled through this.

Lenny Rachitsky (00:56:20):
That is an awesome story.

And this idea of learning is such a good thread throughout this whole conversation that AI is good at getting stuff done, but it's also really good at helping you learn how to do the thing and to be this partner, this thought partner, the way you talked about the interview process you went through and this learning opportunity /command.

So awesome. Great story. Zevi, okay. Before we get to our very exciting lightning round, is there anything else that you wanted to share? Anything you want to leave listeners with?

Zevi Arnovitz (00:56:48):
Yeah. So kind of to tie back into the first thing I said where if people walk away thinking, "Zevi's so cool." Then I've failed here. I think that it's just the best time to be alive, I think.

It's the best time to be a junior contrary to what a lot of people are saying how there's no more junior roles out there and people get out of school and you can't find a role. Yeah, that's true.

But also when else in history could you get out of school and just build a startup on your own with a couple of friends completely bootstrapped. And I see more and more people towards the end of my time at Wix, I was interviewing and I saw more and more people building their own stuff with AI.

And I think contrary to what a lot of people think, it's the best time to be a junior. It's the best time to be a learner.

And I think if any listener is listening to this and you're a curious person, you're a hardworking person, I want to say kind, I'm not sure, but if you're a kind person and a good communicator, you have such an unfair advantage and you can give more value to companies than most people who have 20 years of experience.

So I really hope people get inspired by this and start killing it with their projects.

Lenny Rachitsky (00:57:50):
Amazing. So many ways to be inspired from this conversation. Zevi, with that, we've reached our very exciting lightning round. I've got five questions for you. Are you ready?

Zevi Arnovitz (00:57:58):
Yep, let's do it.

Lenny Rachitsky (00:58:00):
What are two or three books that you find yourself recommending most to other people?

Zevi Arnovitz (00:58:05):
So I'll take one from each kind of genre. So in fiction, I love The Fountainhead by Ayn Rand, one of my favorite books. Really makes you think, really makes you feel. Business books, I'm a big fan of Shoe Dog, the Nike story, one of my favorite books.

Lenny Rachitsky (00:58:18):
I just finished reading that. So funny.

Zevi Arnovitz (00:58:20):
Amazing.

Lenny Rachitsky (00:58:22):
This is great. It was great.

Zevi Arnovitz (00:58:24):
Yeah. I love Shoe Dog. And then more on the psychology side Mindset by Carol Dweck, who coined the term growth mindset. It's just such an amazing book. It kind of sounds like a self-help book, but then you understand that it's completely psychological and is based on research and that book completely changed my life.

Really, I was always with a fixed mindset, and then after reading that, I kind of understood that it was something holding me back. And since then, I've been really, really trying to cultivate a growth mindset. So I really recommend everyone reading that.

Lenny Rachitsky (00:58:52):
Again, connects to that thread of the way you described it, being a 10X learner versus a 10X doer. Okay. Next question. Favorite recent movie or TV show you have really enjoyed?

Zevi Arnovitz (00:59:02):
Yeah, actually, my wife is really into film, so we watch a lot of TV. It's probably our favorite together time. I just finished watching The Pitt, which was amazing. It was really good. And my first recommendation to everyone is if you haven't seen Severance run to see Severance, one of my favorite shows.

Lenny Rachitsky (00:59:18):
Is there a favorite product that you have recently discovered that you really love?

Zevi Arnovitz (00:59:22):
This is a good question. I'm always trying new products. I'll always have three or four browsers installed on my computer and all this different kind of stuff, and I recently discovered a Loom alternative. I was kind of disappointed with Loom. They were taking so much money and the product, I don't know, I just didn't love it.

And there's an open source alternative called Cap, which is just really well-crafted. You can see that the person was really sweating the details and it's just a really, really great alternative. So I've been using that recently.

Lenny Rachitsky (00:59:48):
There's also a product called Supercut that I love that's also a Loom alternative. Shout out. Okay. Two more questions. Do you have a favorite life motto that you find yourself coming back to in work or in life?

Zevi Arnovitz (00:59:58):
Yeah. I'm kind of between two right now. One, which has become a Twitter meme basically, which is you can just do things.

I feel like that is basically going always in my head every time I do something that I'm just shocked at the speed and ability to do things now so you can just do things, and the second one I stole from my brother. His motto is nobody knows what the fuck they're doing. And I just love that.

And I think it kind of makes you take life more lightly. So yeah, nobody knows what the they're doing.

Lenny Rachitsky (01:00:25):
I think people see these companies on the outside and it feels like everything they've got all figured out. And if you're ever on the inside of a company that's doing really well, you're like, how is this staying on the rails? How is this still a thing that is working? Doesn't make any sense.

It's all about to fall apart. Yeah. Okay. Last question. You've had a long entrepreneurial thread throughout your career. There's a couple other real world businesses you've started in the past. You did a thermal clothing business and then like a hummus delivery thing. So maybe pick one of those and just tell the story of what that's about.

Zevi Arnovitz (01:00:55):
Yeah, I'd love to. Really fun that you asked about this. So I'll tell the thermal clothing because I think it's really cool. So in high school, I was selling thermal clothes in 10th grade for one of my sister's friends or something, and basically it was just packs of thermal clothing, shirt and pants.

I grew up in Jerusalem, so it's a bit chillier there. So it was perfect for the weather. And in 10th grade, when I was selling them, they were like 20, $25 a piece and I was making like $4 a sale, and if you look in the food chain, I was like sixth or seventh down the line.

So this was like crazy margins. So during the summer I thought about it like I should just go straight to the importer. So throughout the summer I called the importer and at first he was really, really mad. He was like, no, you have to work for me for years to get to this state.

And I said, listen, man, I'm finishing school soon. This is not going to be my career. Either do it or not. And we basically negotiated throughout the whole summer. And this was also like how I did things before ChatGPT. So he would throw out something, he'd say, "Oh, the import tax has gone up."

And I'll just search Google, like Import Tax Israel and start reading. And I'll be on the phone with him and I'll be like, "Hey, I would just basically stall." And then I'd somehow come back with a challenge. And I ended up getting a really great price, like 12 and a half dollars a piece.

So I was making 100% profit and I spread throughout a bunch of different schools. Each school, I had the coolest people in school selling for me.

And then a really fun thing that I did was we had a really awesome basketball team and our basketball team would basically be 30 points up within the first half and it kind of got boring for the crowd. So I wrote a song, like a basketball chant about Thermal Clothes that basically has my number within it.

And the end of it was if you join in now, we'll give you a discount. And it was with drums and everything. And still when I go to Jerusalem, I know some people who I don't even know my number by heart because they know it by the tune.

And sometimes when I walk in Jerusalem, people stop me and say like, "Hey, it's Thermal Zevi." So that was just a really cool experience as a kid.

Lenny Rachitsky (01:02:55):
This explains so much just the marketing genius of that move. Oh man. Okay. Zevi, this was incredible. Two final questions. Where can folks find you if they want to reach out and maybe follow up on some of the stuff?

We'll link to the scripts and prompts and all that in the show notes so you don't have to read that, and then how can listeners be useful to you?

Zevi Arnovitz (01:03:12):
Awesome. So I've been helped throughout my whole career a ton, so I love helping any way I can. So reach out on LinkedIn or on X. I'd really love to help whoever I can. How can listeners be useful to me? So if you're a student, try StudyMate, tell me what you think.

If you're in Israel and you are not using dictation yet, try Dibur2text. Tell me what you think.

Lenny Rachitsky (01:03:32):
Amazing. I just love how much you're giving away and how useful that's going to be to so many people. So again, we'll link to that in the show notes. Zevi, you're awesome. Thank you so much for being here. Thank you so much for sharing so much.

This is going to help, I think, a lot of people and I think it's going to help people get over the hump on. Okay, I see all these people doing cool stuff. Here's how I can actually do this stuff. So thank you so much for being here and for sharing so much.

Zevi Arnovitz (01:03:55):
Thank you for having me. And if you build something cool with some stuff that I learned here, hit me up, send me. I'd love to see.

Lenny Rachitsky (01:04:02):
Amazing. Zevi, thank you so much for being here.

Zevi Arnovitz (01:04:05):
Thank you.

Lenny Rachitsky (01:04:07):
Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcast, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast.

You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.
