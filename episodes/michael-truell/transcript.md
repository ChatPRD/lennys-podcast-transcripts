---
guest: Michael Truell
title: 'The rise of Cursor: The $300M ARR AI tool that engineers can’t stop using
  | Michael Truell'
youtube_url: https://www.youtube.com/watch?v=En5cSXgGvZM
video_id: En5cSXgGvZM
description: '*Michael Truell* is the co-founder and CEO of Anysphere, the company
  behind Cursor—the fastest-growing AI code editor in the world, reaching $300 million
  in annual recurring revenue just...

  '
duration_seconds: 4274.0
duration: '1:11:14'
view_count: 122050
channel: Lenny's Podcast
keywords:
- growth
- roadmap
- a/b testing
- experimentation
- analytics
- monetization
- revenue
- hiring
- management
- strategy
- vision
- market
- persona
- design
- ux
---

# The rise of Cursor: The $300M ARR AI tool that engineers can’t stop using | Michael Truell

## Transcript

Michael Truell (00:00:00):
... our goal with Cursor is to invent a new type of programming, a very different way to build software. So a world kind of after code, I think that more and more being an engineer will start to feel like being a logic designer, and really, it will be about specifying your intent for how exactly you want everything to work.

Lenny Rachitsky (00:00:16):
What is the most counter-intuitive thing you've learned so far about building Cursor?

Michael Truell (00:00:20):
We definitely didn't expect to be doing any of our own model development. And at this point, every magic moment in Cursor involves a custom model in some way.

Lenny Rachitsky (00:00:26):
What's something that you wish you knew before you got into this role?

Michael Truell (00:00:29):
Many people you hear hire too fast, I think we actually hired too slow to begin with.

Lenny Rachitsky (00:00:35):
You guys went from $0 to 100 million ARR in a year and a half, which is historic. Was there an inflection point where things just started to really take off?

Michael Truell (00:00:43):
The growth has been fairly just consistent on an exponential. And exponential to begin with feels fairly slow when the numbers are really low, and it didn't really show off to the races to begin with.

Lenny Rachitsky (00:00:51):
What do you think is the secret to your success?

Michael Truell (00:00:53):
I think it's been...

Lenny Rachitsky (00:00:55):
Today, my guest is Michael Truell. Michael is co-founder and CEO of Anysphere, the company behind Cursor. If you've been living under a rock and haven't heard of Cursor, it is the leading AI code editor, and is at the very forefront of changing how engineers and product teams build software. It's also one of the fastest growing products of all time, hitting 100 million ARR just 20 months after launching, and then 300 million ARR just two years since launch.

(00:01:22):
Michael's been working on AI for 10 years. He studied computer science and math at MIT, did AI research at MIT and Google, and is a student of tech and business history. As you'll soon see, Michael thinks deeply about where things are heading, and what the future of building software looks like. We chat about the origin story of Cursor, his prediction of what happens after code, his biggest counter-intuitive lessons from building Cursor, where he sees things going for software engineers, and so much more.

(00:01:49):
Michael does not do many podcasts. The only other podcast he's ever done is Lex Fridman, so it was a true honor to have Michael on. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become an annual subscriber of my newsletter, you get a year free of Perplexity, Linear, Superhuman, Notion, and Granola. Check it out at lennysnewsletter.com, and click bundle. With that, I bring you Michael Truell.

(00:02:14):
This episode is brought to you by Eppo. Eppo is a next-generation A/B testing and feature management platform built by alums of Airbnb and Snowflake for modern growth teams. Companies like Twitch, Miro, ClickUp, and DraftKings rely on Eppo to power their experiments. Experimentation is increasingly essential for driving growth, and for understanding the performance of new features, and Eppo helps you increase experimentation velocity, while unlocking rigorous deep analysis in a way that no other commercial tool does.

(00:02:44):
When I was at Airbnb, one of the things that I loved most was our experimentation platform, where I could set up experiments easily, troubleshoot issues, and analyze performance all on my own. Eppo does all that and more, with advanced statistical methods that can help you shave weeks off experiment time, an accessible UI for diving deeper into performance, and out-of-the-box reporting that helps you avoid annoying, prolonged analytics cycles. Eppo also makes it easy for you to share experiment insights with your team, sparking new ideas for the A/B testing flywheel. Eppo powers experimentation across every use case, including product, growth, machine learning, monetization, and email marketing. Check out Eppo at geteppo.com/lenny, and 10X your experiment velocity. That's getE-P-P-O.com/lenny.

(00:03:31):
This episode is brought to you by Vanta. When it comes to ensuring your company has top-notch security practices, things get complicated fast. Now, you can assess risk, secure the trust of your customers, and automate compliance for SOC 2, ISO 27001, HIPAA, and more with a single platform, Vanta. Vanta's market-leading trust management platform helps you continuously monitor compliance, alongside reporting and tracking risk. Plus, you can save hours by completing security questionnaires with Vanta AI. Join thousands of global companies that use Vanta to automate evidence collection, unify risk management, and streamline security reviews. Get $1,000 off Vanta when you go to vanta.com/lenny. That's V-A-N-T-A.com/lenny.

(00:04:26):
Michael, thank you so much for being here. Welcome to the podcast.

Michael Truell (00:04:30):
Thank you. It's great to be here. Thank you for having me.

Lenny Rachitsky (00:04:33):
When we were chatting earlier, you had this really interesting phrase, this idea of what comes after code. Talk about that, just the vision you have of where you think things are going in terms of moving from code to maybe something else.

Michael Truell (00:04:45):
Our goal with Cursor is to invent sort of a new type of programming, a very different way to build software, that's kind of just distilled down into you describing the intent to the computer for what you want in the most concise way possible, and really distilled down to just defining how you think the software should work, and how you think it should look. With the technology that we have today, and as it matures, we think you can get to a place where you can invent a new method of building software that's [inaudible 00:05:16] higher level, and more productive, in some cases, more accessible too.

(00:05:21):
And that process will be a gradual moving away from what building software looks like today. I want to contrast it with maybe the vision of what software looks like in the future that I think... A couple of visions that are in a popular consciousness that we at least have some disagreement with. One is, there's a group of people who think that software building in the future is going to look very much like it does today, which mostly means text editing, formal programming languages, like TypeScript, and Go, and C, and Rust. And then there's another group that kind of thinks you're just going to type into a bot, and you're going to ask it to build you something, and then you're going to ask it to change something about what you're building, and it's kind of like this chatbot, Slackbot style where you're talking to your engineering department.

(00:06:10):
And we think that there are problems with both of those visions. I think that on the chatbot style end of things... And we think it's going to look weirder than both. The problem with the chatbot style end of things is that lacks a lot of precision. If you want humans to have complete control over what the software looks like, and how it works, you need to let them gesture at what they want to be changed in a form factor that's more precise than just, "Change this about my app." In a text box, removed from the whole thing. And then the version of the world where nothing changes we think is wrong, because we think the technology is going to get much, much, much better.

(00:06:54):
And so a world after code, I think that it looks like a world where you have a representation of the logic of your software that does look more like English, you have written down... You can imagine in [inaudible 00:07:08] form, you can imagine in kind of an evolution of programming language towards pseudocode. You have written down the logic of the software, and you can edit that at a high level, and you can point at that. And it won't be the impenetrable millions of lines of code, it'll instead be something that's much Terser, and easier to understand, easier to navigate. But that world where the kind of crazy, hard to understand symbols start to evolve towards something that's a little bit more human-readable, and human-editable, is one that we're working towards.

Lenny Rachitsky (00:07:36):
This is a profound point. I want to make sure people don't miss what you're saying here, which is that what you're envisioning in the next year essentially is kind of when things start to shift, is, people move away from even seeing code, having to think in code in JavaScript and Python, and there's this abstraction that will appear, essentially pseudocode, describing what the code should be doing more in English sentences.

Michael Truell (00:07:59):
Yep. We think it ends up looking like that, and we're very opinionated that that path goes through existing professional engineers, and it looks like this evolution away from code. And it definitely looks like the human still being in the driver's seat, and the human having both a ton of control over all aspects of the software and not giving that up. And then also the human having the ability to make changes very quickly, having a fast duration loop and not just having something in the background that's super slow and takes weeks, go do all your work for you.

Lenny Rachitsky (00:08:33):
This begs the question for people that are currently engineers, or thinking about becoming engineers, or designers, or product manager, what skills do you think will be more and more valuable in this world of what comes after code?

Michael Truell (00:08:50):
I think taste will be increasingly more valuable. And I think often when people think about tastes in the realm of software, they think about visuals, or taste over smooth animations, and coloring things, UI, UX, et cetera on the visual design of things. And the visual side of things is an important part of defining a piece of software, but then, as mentioned before, I think that the other half of defining a piece of software is the logic of it, and how the thing works.

(00:09:22):
And we have amazing tools for specing out the visuals of things, and then when you get into the logic of how a piece of software works, really, the best representation we have of that is code right now. You can kind of gesture at it with Figma, and you can gesture at it with writing down notes, but it's when you have an actual working prototype. And so I think that more and more, being an engineer will start to feel like being a logic designer, and really, it will be about specifying your intent for how exactly you want everything to work. It'd be more about the whats, and a little bit less about how exactly you're going to do things under the hood.

(00:09:59):
I think taste will be increasingly important. I think one aspect of software engineering, and we're very far from this right now, and there are lots of funny memes going around the internet about some of the trials and tribulations people can run into if they trust AI for too many things that comes to engineering, around building apps that have glaring deficiencies, and problems, and functionality issues. But I think we will get to a place where you'll be able to be less careful as a software engineer, which, right now, is an incredibly, incredibly important skill. We'll move a little bit from carefulness, and a little bit more towards taste.

Lenny Rachitsky (00:10:40):
This makes me think of vibe coding, is that kind of what you're describing when you talk about not having to think about the details as much, and just kind of going with the flow?

Michael Truell (00:10:49):
I think it's related. I think that vibe coding right now describes exactly this state of creation that is pretty controversial, where you're generating a lot of coding, you aren't really understanding the details. That is a state of creation that then has lots of problems, you don't really... By not understanding the details under the hood right now, you then very quickly get to a place where you're kind of limited at a certain point, where you create something that's big enough that you can't change. And so I think some of the ideas that we're interested around, how do you give people continued control over all the details when they don't really understand the code? I think that solutions there are very relevant to the people who are vibe coding right now. I think that right now, we lack the ability to let the tastemakers actually have complete control over the software. One of the issues also with vibe coding, and letting taste really shine through from people is, you can create stuff, but a lot of it the AI making decisions that are unwieldy and you don't have to control over.

Lenny Rachitsky (00:11:56):
One more question along these lines. You threw out this word taste. When you say taste, what are you thinking?

Michael Truell (00:12:01):
I'm thinking having the right idea for what should be built. It will become more and more about effortless translation of, here's exactly what you want built, here's how you want everything to work, here's how you want it to look. And then you'll be able to make that on a computer, and it will less be about this kind of translation layer of, you and your team have a picture of what you'd want to build, and then you have to really painstakingly, labor-intensive, lay out that into a format that a computer can then execute and interpret. I think less than the UI side of things, maybe taste is a little bit of a misnomer, but just about having the right idea for what should be built.

Lenny Rachitsky (00:12:39):
Awesome. Okay. I'm going to come back to these topics, but I want to actually zoom us back out to the beginnings of Cursor. I have never heard the origin story, I don't think many people know how this whole thing started. Basically you guys are building one of the fastest growing products in the history of the world, it's changing the way people build products, it's changing careers, professions, it's changing so much. How did it all begin? Any memorable moments along the journey of the early days?

Michael Truell (00:13:05):
Cursor kind of started as a solution search of a problem, and a little bit where it very much came from reflecting on how AI was going to get better over the course of the next 10 years. There were kind of two defining moments, one was being really excited by using the first beta version of Code Pilot, actually. This was the first time we had used an AI product that was really, really, really useful, and was actually just useful at all, and wasn't just a vaporware kind of demo thing.

(00:13:43):
And in addition to being the first AI product that we'd use that was useful, Code Pilot was also one of the most useful, if not the most useful dev tool we'd ever adopted, and that got us really excited. Another moment that got us really excited was the series of scaling on papers coming out of OpenAI and other places that showed that even if we had no new ideas, AI was going to get better and better just by pulling on simple levers, like scaling up the models, and also scaling up the data that was going into the models.

(00:14:12):
And so at the end of 2021, beginning of 2022, this got us excited about how AI products were now possible, this technology was going to mature into the future. And it felt like when we looked around, there were lots of people talking about making models, and it felt like people weren't really picking an area of knowledge work and thinking about what it was going to look like as AI got better and better. And that set us on the path to an idea generation exercise, it was like, "How are these areas of knowledge work going to change in the future as this tech gets more mature? What is the end state of the work going to look like? How are the tools that we use to do that work going to change? How are the models going to need to get better to support changes in the work? And once scaling and pre-training ran out, how are you going to keep pushing for technological capabilities?"

(00:15:07):
And the misstep at the beginning of Cursor is we actually worked on... We sort of did this whole grand exercise, and we decided to work on an area of knowledge work that we thought would be relatively uncompetitive, and sleepy, and boring, and no one would be looking at it, because we thought, "Oh, coding's great, coding's totally going to change with this AI, but people are already doing that." So there was a period of four months to begin with, where we were actually working on a very different idea, which was helping to automate and augment mechanical engineering, and building tools for mechanical engineers.

(00:15:44):
There were problems from the get-go in that. Me and my co-founders, we weren't mechanical engineers. We had friends who were mechanical engineers, but we were very much unfamiliar with the field. So there was a little bit of a blind man and the elephant problem from the get-go. There were problems around, how would you actually take the models that exist to today and make them useful for mechanical engineering? The way we netted out is, you need to actually develop your own models from the get-go. And the way we did that was tricky, and there's not a lot of data on the internet of 3D models of different tools and parts, and the steps that I expect to build up to those 3D models, and then getting them from the sources that have them is also a tricky process too.

(00:16:30):
But eventually what happened was, we came to our senses, we realized we're not super excited about mechanical engineering, it's not the thing we want to dedicate our lives to. And we looked around, and in the area of programming, it felt like despite a decent amount of time ensuing, not much has changed, and it felt like the people that were working on the space maybe had a disconnect with us, and it felt like they weren't being sufficiently ambitious about where everything was going to go in the future, and how all of software creation was going to blow through these models. And that's what set us off on the path to building Cursor.

Lenny Rachitsky (00:17:04):
Okay. So interesting. Okay, so first of all, I love that... This is advice that you often hear of go after a boring industry because no one's going to be there, and there's opportunity. And sometimes it works, but I love that in this journey, it's like, "No, actually, go after the hottest, most popular space, AI coding, app building." And it worked out. And the way you phrased it just now is, you didn't see enough ambition potentially, that you thought there was more to be done. So it feels like that's an interesting lesson. Even if something looks like, "Okay, it's too late, there's GitHub, Code Pilot's out there." Some other products. If you notice that they're just not as ambitious as they could be, or as you are, or you see almost a flaw in their approach, that there's still a big opportunity. Does that resonate?

Michael Truell (00:17:46):
That totally resonates. A part of it is, you need there to be leapfrogs that can happen, you need there to be things that you can do. And I think the exciting thing about AI is, in a bunch of places, and I think this is very much still true of our space, and can talk about how we think about that and how we deal with that, but I think that just the ceiling is really high. And yes, if you look around, probably even if you take the best tool, any of these fields, there should be a lot more that needs to be done over the next few years. Having that space, having that high ceiling, I think is unique amongst areas of software, at least the degree to which it is high with AI.

Lenny Rachitsky (00:18:30):
Let's come back to the IDE questions. So there's a few routes you could have taken, and other companies are doing different routes. So there's building an IDE for engineers to work within and adding AI magic to it, there's another route of just a full AI agentic dev product, and then there's just a model that is very good at coding, and focusing on building the best possible coding model. What made you decide and see that the IDE path was the best route?

Michael Truell (00:18:54):
The folks who were from the get-go working on just a model were working on end-to-end automation programming. I think they were trying to build something very different from us, which is, we care about giving humans control over all of the decisions in the end tool that they're building. And I think those folks were very much thinking of a future where end-to-end, the whole thing is done by AI, and maybe the AI is making all the decisions too. And so, one, there was a personal interest component. Two, I think that always, we've tried to be intense realists about where the technology is today, very, very, very excited about how AI is going to mature over the course of many decades. But I think that sometimes people... There's an instinct to see AI do magical things in one area, and then kind of anthropomorphize these models, and think it's better than a smart person here, and so it must be better than a smart person there.

(00:19:55):
But these things have massive issues, and we... From the very start, our product development process was really about dogfooding, and using the tool intensely every day. And we never wanted to ship anything that wasn't useful to us, and we had the benefit of doing that because we were the end users part of our product. And I think that that instills a realism in you around where the tech is right now, and so that definitely made us think that we need the humans to be in the driver's seat, the AI cannot do everything. We're also interested in giving humans that control too for personal reasons, and so that gets you away from just your model company that also gets you away from just this end-end stuff without the human having control.

(00:20:39):
And then the way you get to an IDE versus maybe a plug-in to an existing coding environment is the belief that programming is going to flow through these models, and the active programming is going to change a lot over the course of the next few years. And that the extensibility that existing coding environments have is so, so, so limited, so if you think that the UIs may change a lot, if you think that the form factor programming is going to change a lot, necessarily need to have control over the entire application.

Lenny Rachitsky (00:21:04):
I know that you guys today have an IDE, and that's probably the bias you have of this is maybe where the future is heading, but I'm just curious, do you think a big part of the future is also going to be AI engineers that are just sitting in Slack and just doing things for you? Is that something that fits into Cursor one day?

Michael Truell (00:21:20):
I think you'll want the ability to move between all of these things fairly effortlessly, and sometimes I think you will want to have the thing kind of go spin off on its own for a while, and then I think you'll want the ability to pull in the AI's work, and then work with it very, very, very quickly, and then maybe have it go spin off again. And so these kind of background versus foreground form factors, I think you want that all to work well in one place. And I think the background stuff, there's a segment of programming that it's especially useful for, which is type of programming tasks where it's very easy to specify exactly what you want without much description, and exactly what correctness looks like without much description.

(00:22:05):
Bug fixes are a great example of that, but it's definitely not all of programming. So I think that what the IDE is will totally change over time, and our approach to having our own editor was premised on, it's going to have to evolve over time. And I think that that will both include, you can spin off things from different surface areas like Slack, or your issue tracker, or whatever it is, and I think that will also include the pane of glass that you're staring at is going to change a lot. We just mostly think of an IDE as the place where you are building software.

Lenny Rachitsky (00:22:38):
I think something people don't talk enough about with talking about agents and all these AI engineers that are going to be doing all this stuff for you, is basically we're all becoming engineering managers, with a lot of reports that are just not that smart, and you have to do a lot of reviewing, and approving, and specifying. I guess thoughts on that, and is there anything you could do to make that easier? Because that sounds really hard. Anyone that has had a large team, being like, "Oh my god, all these junior people just checking in with me doing not high quality work over and over." It's just like, "What a life. It's going to suck."

Michael Truell (00:23:11):
Yeah. Maybe you [inaudible 00:23:12] one-on-ones with [inaudible 00:23:15].

Lenny Rachitsky (00:23:15):
So many one-on-ones.

Michael Truell (00:23:17):
Yeah. So the customers we've seen have most success with AI I think are still fairly conservative about some of the ways in which they use this stuff. And so I do think today, the most successful customers really lean on things like our next edit prediction, where your coding is normal, and making the next into actions you're going to do. And then they also really lean on scoping down the stuff that you're going to hand off to the bot, and for a fixed percent of your time spent reviewing code, from an agent, or from an AI overall, you could... There's two patterns. One is, you could spend a bunch of time specifying things up front, the AI goes and works, and then you then go and review the AI's work, and then you're done. That's the whole task.

(00:24:07):
Or you can really chop things up. So you can specify a little bit, AI writes something, review, specify a little bit, AI writes something, review. Autocompletes all in the way of that spectrum. And still we see often the most successful people using these tools are chopping things up right now, and keeping things fairly [inaudible 00:24:28].

Lenny Rachitsky (00:24:27):
That sounds less terrible. I'm glad there's a solution here. I want to go back to you guys building Cursor for the first time. What was the point where you realized this is ready? What was a moment of, "Okay, I think this is time to put it out there, and see what happens"?

Michael Truell (00:24:41):
So when we started building Cursor, we were fairly paranoid about spinning for a while, without releasing to the world. And so to begin with too, we actually... The first version of Cursor was hand-rolled. Now we use VS Code as a base, like many browsers use Chromium as a base, and hit foot off of that. To begin with, we didn't, and built the prototype of Cursor from scratch, and that involved a lot of work. We had to build our own... There were a lot of things that go into a modern code editor, including support for many different languages, and navigation support for moving amongst the language, error tracking support for things. There's things like an integrated command line, the ability to use remote servers, the ability to connect to remote servers to view and run code. And so we kind of just went on this blitz of building things incredibly quickly, building our own editor from scratch, and then also the AI components.

(00:25:45):
It was after maybe five weeks that we were living on the editor full-time, and had thrown away our previous editor, and we're using a new one. And then once it got to a point where we found it a bit useful, then we put it in other people's hands, and had this very short beta period. And then we launched it out to the world within a couple of months from the first line of code, I think it was probably three months. And it was definitely a, "Let's just get this out to people and build in public quickly." The thing that took us by surprise is we thought we would be building for a couple hundred people for a long time. And from the get-go, there was an immediate rush of interest, and a lot of feedback too. That was super helpful, we learned from that. That's actually why we switched to being based off of VS Code instead of just this hand-rolled thing. A lot of that was motivated by the initial user feedback, and then had been iterating in public from there.

Lenny Rachitsky (00:26:44):
I like how you understated the traction that you got. I think you guys went from $0 to 100 million ARR in a year, year and a half or something like that, which is historic. What do you think was the key to success of something like this? You just talked about dogfooding being a big part of it. You built it in three months, that's insane. What do you think is the secret to your success?

Michael Truell (00:27:12):
The three-month version wasn't very good, and so I think it's been a sustained paranoia about, there are all of these ways in which this thing could get better. The end goal is really to invent a very new form of programming that involves automating a lot of coding, as we know today. And no matter where we are with Cursor, it feels like we're very, very far away from that end goal, there's always a lot to do. A lot of it hasn't been over rotated on that initial push, but instead is the continued evolution of the tool, and just making the tool consistently better.

Lenny Rachitsky (00:27:47):
Was there an inflection point after those three months where things just started to really take off?

Michael Truell (00:27:51):
To be honest, it felt fairly slow to begin with, and maybe it comes from some impatience on our part. I think there's the overall speed of the growth which continues to take us by surprise. I think one of the things that has been most surprising too is that the growth has been fairly just consistent on an exponential, of just consistent month-over-month growth, accelerated at times by launches on our part and other things. But an exponential to begin with feels fairly slow and the numbers are really low, and so it didn't really feel off to the races to begin with.

Lenny Rachitsky (00:28:32):
To me this sounds like build it and they will come actually working. You guys just built an awesome product that you loved yourselves as engineers, you put it out, people just loved it, told everyone about it.

Michael Truell (00:28:42):
It being essentially all just us, the team working on the product, and making the product good in lieu of other things one could spend one's time on. We definitely spent time on tons of other things, for instance, building the team was incredibly important, and doing things like support rotations are very important. But some of the normal things that people would maybe reach for in building the company early on, we really let those fires burn for a long time, especially when it came to things like sales and marketing.

(00:29:15):
And so just working on the product, and building a product that you like first, your team likes, and then also then adjusting it for some set of users, that can kind of sound simple, but then, as you know, it's hard to do that well. And there are a bunch of different directions one could have run in, a bunch of different product directions.

(00:29:35):
I think focus, and strategically picking the right things to build, and prioritizing effectively is tricky. I think another thing that's tricky about this domain is, it's kind of a new form of product building, where it's very interdisciplinary in that we are something in between a normal software company and then a foundation model company, in that we're developing a product for millions of people, and that side of things has to be excellent, but then also one important dimension of product quality is doing more and more on the science, and doing more and more on the model side of things in places where it makes sense. And so that element of things doing that well too has been tricky. The overall thing would note is maybe some of these things sound simple to specify, but doing them well is hard, and they're a lot of different way you can run in.

Lenny Rachitsky (00:30:30):
I'm excited to have Andrew Luo joining us today. Andrew is CEO of OneSchema, one of our podcast sponsors. Welcome, Andrew.

Speaker 3 (00:30:38):
Thanks for having me, Lenny. Great to be here.

Lenny Rachitsky (00:30:40):
So what is new with OneSchema? I know that you work with some of my favorite companies, like Ramp, and [inaudible 00:30:46], and Watershed. I heard you guys launched a new data intake product that automates the hours of manual work that teams spent importing, and mapping, and integrating CSV in Excel files?

Speaker 3 (00:30:55):
Yes. So we just launched the 2.0 of OneSchema FileFeeds. We've rebuilt it from the ground up with AI. We saw so many customers coming to us with teams of data engineers that struggled with the manual work required to clean messy spreadsheets. FileFeeds 2.0 allows non-technical teams to automate the process of transforming CSV and Excel files with just a simple prompt. We support all of the trickiest file integrations, SFTP, S3, and even email.

Lenny Rachitsky (00:31:22):
I can tell you that if my team had to build integrations like this, how nice would it be to take this off our roadmap and instead use something like OneSchema.

Speaker 3 (00:31:30):
Absolutely, Lenny. We've heard so many horror stories of outages from even just a single bad record, in transactions, employee files, purchase orders, you name it. Debugging these issues is often like finding a needle in a haystack. OneSchema stops any bad data from entering your system, and automatically validates your files, generating error reports with the exact issues in all bad files.

Lenny Rachitsky (00:31:51):
I know that importing incorrect data can cause all kinds of pain for your customers and quickly lose their trust. Andrew, thank you so much for joining me. If you want to learn more, head on over to oneschema.co., that's oneschema.co.

(00:32:05):
What is the most counterintuitive thing you've learned so far about building Cursor, building AI products?

Michael Truell (00:32:11):
I think one thing that's been counterintuitive for us, [inaudible 00:32:14] added a little bit before, but is, we definitely didn't expect to be doing any of our own model development when we started. As mentioned, when we got into this, there were companies that were immediately from the get-go going and just focusing on training model from scratch. And we had done the calculation for what it to train before, and just knew that that was not [inaudible 00:32:36] going to be able to do. And also felt a bit like focusing one's attention in the wrong area, because there were lots of amazing models out there, and why develop all this work to replicate what other players had done. Especially on the pre-training side of things, taking a neural network that knows nothing, and then teaching it the whole internet.

(00:32:55):
And so we thought we weren't going to be doing that at all, and it seems clear to us from the start that the existing models, there were lots of things that they could be doing for us that they weren't doing, because there wasn't the right tool built for them. In fact though, we do a ton of model development, and internally, it's a big focus for us on the hiring front, and have assembled a fantastic team there.

(00:33:18):
And it's also been a big win on the product quality side of things for us. And at this point, every magic moment in Cursor involves a custom model in some way. So that was definitely counterintuitive, and surprising, and it's been a gradual thing, where there was an initial use case for training our own model, where it really didn't make sense to use any of the biggest foundation models. That was incredibly successful, moved to another use case that worked really well, and had been going from there. And one of the helpful things in doing this sort of model development is picking your spots carefully, not trying to reinvent the wheel, not trying to focus on places, and maybe where the best foundation models are excellent, but instead kind of focusing on their weaknesses, and how you can complement them.

Lenny Rachitsky (00:34:05):
I think this is going to be surprising to a lot of people hearing that you have your own models. When people talk about Cursor and all the folks in the space, they would kind of call them GPT wrappers, they're just sitting on top of ChatGPT or Sonnet. What you're saying is that you have your own models, talk about just the stack behind the scenes.

Michael Truell (00:34:21):
Yeah, of course. So we definitely use the biggest foundation models a bunch of different ways, they're really important components of bringing the Cursor experience to people. The places where we use our own models, so sometimes it's to survey a use case that a foundation model wouldn't be able to serve at all for cost or speed reasons. And so one example of that is the autocomplete side of things. And so this can be a little bit tricky for people who don't code to understand, but code is this weird form of work, where sometimes, really, the next 5, 10, 20, 30 minutes of your work is entirely predictable from looking over your shoulder.

(00:35:02):
And I would contrast this with writing. So writing, lots of people are familiar with Gmail's autocomplete, and the different forms of autocomplete that show up when you're trying to post text messages, or emails, or things like that. They can only be so helpful, because often, it's just really not clear what you're going to be writing just by looking at what you've written before. But in code sometimes, when you edit a part of a code base, you're going to need to change things, and in other parts of code base, and it's entirely clear how you're going to need to change things.

(00:35:30):
So one core part of Cursor is this really suit to autocomplete experience, where you predict the next set of that you're going to be doing across multiple files, across multiple places within a file. And making models good at that use case, one, there's a speed component of, those models need to be really fast, they need to give you a completion within 300 milliseconds. There's also this cost component of, we're running tons, and tons, and tons of molecules, every keystroke, we need to be changing our prediction for what you're going to do next. And then it's also this really specialty use case of, you need models that are really good, not at completing the next token, just a generic tech sequence, but are really good at autocompleting a series of diffs, looking at what's changed within a code base, and then creating the next set of things that are going to change, both deleted and added and all of that, and we found a ton of success in training models specifically for that task.

(00:36:23):
So that's a place where no foundation models are involved, it's kind of our own thing. We don't have a lot of labeling or branding about this in the app, power is a very core part of Cursor. And then another set of places where a user own models are to help things like Sonnet, or Gemini, or GPT, and those sit both on the inputs of those big models, and on the output. On the input side of things, those models are searching throughout a code base, try to figure out the parts of a code base to show to one of these big models. You can kind of think about this as a mini Google search that's specifically built for finding the relevant parts of the code base to show one of these big models.

(00:37:02):
And then on the output side of things, we take the sketches of the changes that these models are suggesting, you make with that code base. And then we have models that then fill in the details of, the high level thinking is done by the smartest models, they spend a few tokens on doing that, and then these smaller specialty incredibly fast models, coupled with some inference tricks, then take those high level changes and turn them actually into full code diffs. And so it's been super helpful for pushing on quality in places where you need a specialty task, and it's been super helpful for pushing on speed, which is such an important dimension of product quality for us too.

Lenny Rachitsky (00:37:39):
This is so interesting. I just had Kevin Weil on the podcast, CPO of OpenAI, and he calls this the ensemble of models, that's the same way-

Michael Truell (00:37:46):
Yes.

Lenny Rachitsky (00:37:46):
... they work, to use the best feature of each one, and to your point, the cost advantages of using cheaper models. These other models, are they based on Llama and things like that, just open source models that you guys plug into and build on?

Michael Truell (00:38:00):
Yeah. So again, we try to be very pragmatic about the place that we're going to do this work, and we don't want to reinvent the wheel. And so starting from the very best pre-trained models that exist out there, often open source ones, sometimes in collaboration with these big model providers that don't share their weights out into the world, because the thing we care about last is the ability to read line by line, the matrix of weights that then go to give you a certain output. We just care about the ability to train these things, to post-train them. And so by and large, yes, open source models, sometimes working with the closed source providers too to tune things.

Lenny Rachitsky (00:38:42):
This leads to a discussion that a lot of AI founders always think about and investors, which is moats, and defensibility in AI. So it feels like one is custom models, is a moat in the space. How do you just think about long-term defensibility in the space, knowing there's other folks, as you said, launching constantly trying to eat your lunch?

Michael Truell (00:39:03):
I think that there are ways to build in inertia and traditional moats, but I think by and large, we're in a space where it is incumbent on us to continue to try to build the best thing, and everyone in this industry. And I truly just think that the ceiling is so high that no matter what entrenchment you build, you can be leapfrogged. And I think that this resembles markets that are maybe a little bit different from normal software markets, normal enterprise markets of the past. I think one that comes to mind is the market for search engines at the end of 1999, or at the end of the '90s and beginning of the 2000s. I think another market that comes to mind that resembles this market in many ways, it's actually just the development of the peripheral computer and many computers in the '70s, '80s, '90s.

(00:40:03):
And I think that, yes, in each of those markets, the ceiling was incredibly high, it was possible to swish. You could keep getting value for the incremental hour of a smart person's time, the incremental R&D dollar for a really long time, you wouldn't run out of useful things to build. And then in search in particular, not on the computer case, adding distribution was helpful for making the product better too, in that you could tune the algorithms, you could tune the learning based off of the data and the feedback you're getting from users. And I think that all of those dynamics exist in our market too. And so I think maybe the sad truth for people like us, but then the amazing truth for the world is, I think that there are many leapfrogs that exist, there's more useful things to build. We're a long way away from where we can compete in 5, 10 years, and it's incumbent in our state to keep that going.

Lenny Rachitsky (00:40:55):
So what I'm hearing, this sounds like a lot more like a consumer sort of moat, where it's just, be the best thing consistently so that people stick with you versus creating lock-in and things like that, where they're just... Like Salesforce, where it's just contracts with the entire company, and you have to use this product.

Michael Truell (00:41:10):
Yeah. I think the important thing to note is, if you're in a space where you run out of useful things to do very quickly, then that's not a great situation to be in. But if you're in a place where big investments, and having more and more great people working on the right path can keep giving you value, then you can get these economies of scale of R&D, and you can deeply work on the technology in the right direction, and get to a place where that is defensible. But yes, it is... I think there's a consumer-like tendency to it, and I really think it's just about building the best thing possible.

Lenny Rachitsky (00:41:48):
Do you think in the future there's one winner in this space, or do you think it's going to be a world of a number of products like this?

Michael Truell (00:41:53):
I think the market is just so very big. You asked about the IDE thing early on, and one thing that I think a trip of some people that were thinking about the space is, they looked at the IDE market of the past 10 years, and they said, "Who's making money off of the editors?" It's this super fragmented space where everyone kind of has their own thing, with their own figuration, and there's one company that actually makes money off making great editors, but that company is only so big. And then the conclusion was, it was going to look like that in the future. And I think that the thing that people missed was that there was only so much you could do building an editor in the 2010s for coders, and the company that made money off of editors was doing things like making it easy to navigate around a code base, and doing some error checking and type checking for things, and having good debugging tools.

(00:42:57):
Which were all very useful, but I think that the set of things you can build for programmers, I think the set of things you can build for knowledge workers in many different areas just goes very far and very deep. The problem in front of all of us is the automation of a lot of busy work and knowledge work, and really changing all the areas of knowledge work in front of us to be much higher level and more productive.

(00:43:19):
So that was a long-winded way to say, I think the market's really, really big that we're in. I think it's much bigger than people have realized than the other building tools for developers in the past. And I think that there will be a bunch of different solutions. I think that there will be one company, to be determined if it's going to be us, but I do think that there will be one company that builds the general tool that builds almost all the world's software, and that will be a very, very generationally big business. But I think that there will be kind of niches you can occupy in doing something for a particular segment of the market, or for a very particular part of the software development life cycle. But the general programming shifts from just writing formal programming languages to something way higher level. This is the application you purchase and use to do that. I think that there will be generally one winner there, and it will be a very big business.

Lenny Rachitsky (00:44:10):
Juicy. Along those lines, it's interesting that Microsoft was actually at the center of this first, with an amazing product, amazing distribution, Copilot you said was the thing that got you over the hump of, "Wow, there could be something really big here." And it doesn't feel like they're winning, it feels like they're falling behind. What do you think happened there?

Michael Truell (00:44:34):
I think that there are specific historical reasons why Copilot might not have lived up... So far have lived up to the expectations that some people have for it, and then I think that there are structural reasons. I think the structural reason is... And to be clear, Microsoft, in the Copilot case, obviously a big inspiration for our work, and in general, I think they do lots of awesome things, and we're users of many Microsoft products, but I think that this is a market that's not super friendly to incumbents, in that a market that's friendly to incumbents might be one where there's only so much to do, it kind of gets commoditized fairly quickly, and you can bundle that in with other products, and where the ROI between different products is quite small. And in that case, perhaps it doesn't make sense to buy the innovative solution, it makes sense to just kind of buy the thing that's bundled in with other stuff.

(00:45:31):
Another market that might be particularly helpful for incumbents is one where there's... From the get-go, you have your stuff in one place, and it's really, really excruciatingly hard to switch, and for better or for worse. I think in our case, you can try out different tools, and you can decide which product you think is better. And so that's not super friendly to incumbents, and that's more friendly to whoever you think is going to have the most innovative product. And then the specific historical reasons, as I understand them are the group of people that worked on the first version of Copilot have, by and large, gone on to do other things at other places. I think it's been a little hard to coordinate among all the different departments and parties that might be involved in making something like this.

Lenny Rachitsky (00:46:15):
I want to come back to Cursor. A question I like to ask everyone that's building a tool like this, if you could sit next to every new user that uses Cursor for the first time, just whisper a couple tips in their ear to be more successful, most successful with Cursor, what would be 1 or 2 tips?

Michael Truell (00:46:32):
I think right now, and we'd want to fix this at a product level, a lot of being successful with Cursor is kind of having a taste for what the models can do, both what complexity of a task they can handle, and how much you need to specify things to that model, but having a taste for the quality of the model, and where its gaps exist, and what it can do and what it can't. And right now, we don't do a good job in the product of educating people around that, and maybe giving people some swim lanes, giving people some guidelines.

(00:47:06):
But to develop that taste, would give two tips. So one is, as mentioned before, would bias less toward, trying in one go to tell the model, "Hey, here's exactly what I want you to do." Then seeing the output, and then either being disappointed or accepting the entire thing for an entire big task. Instead what I would do is I would chop things up into bits, and you can spend basically the same amount of time specifying things overall, but chopped up more. So you're specifying a little bit, you're getting a little bit of work, you're specifying a little bit, getting a little bit of work, and not doing as much the, "Let's write a giant thing telling the model exactly what to do." I think that will be a little bit of a recipe for disaster right now.

(00:47:48):
And so biasing toward chopping things up. At the same time, and it might make sense to do this on a side project and not on your professional work, I would encourage people to, especially developers who are used to existing workflows for building software, I would encourage people to explicitly try to fall on their face, and try to discover the limits of what these models can do by being ambitious in a safe environment, like perhaps a side project, and trying to kind of go around town, use AI to the fullest. Because a lot of the time, we run into people who haven't given the AI yet a fair shake, and are underestimating its abilities. So generally biasing towards chopping things up and making things smaller, but to discover the limits of what you can do there, explicitly just try to go for broke in a safe environment, and get a taste for... You might be surprised in some of the places where the model doesn't break.

Lenny Rachitsky (00:48:45):
What I'm essentially hearing is build a gut feeling of what the model can do, and how far it can take an idea versus just kind of guiding it along. And I bet that you need to rebuild this gut every time there's a new model launch, when it's on... I don't know, 4.0 comes out, you have to do this again. Is that generally right?

Michael Truell (00:49:04):
Yes. For the past few years, it hasn't been as big as I think the first experience people have had with some of these big models. This is also a problem we would hope to solve much better just for users, and take the burden off of them. But each of these things have slightly different quirks and different personalities.

Lenny Rachitsky (00:49:26):
Along these lines, something that people are always debating tools like Cursor, are they more helpful to junior engineers, or are they more helpful to senior engineers? Do they make senior engineers 10X better? Do they make junior engineers more like senior engineers? Who do you think benefits most today from Cursor?

Michael Truell (00:49:43):
I think across the board. Both of these cohorts benefit in big ways. It's a little hard to say on the relative ranking. I will say, they fall into different anti-patterns. The junior engineers we see going a little too wholesale, relying on AI for everything, and we're not yet in a place where you can kind of do that end-to-end on a professional tool, working with tens, hundreds of other people within a long-lived code base. And then the senior engineers... For many folks, it's not true for all, and we actually often... One of the ways these tools are adopted is, there's developer experience teams within companies, often those are staffed by incredibly senior people, because often, those are people who are building tools to make the rest of the engineers within an organization more productive.

(00:50:33):
And we've seen some very, very boundary pushing kind of... We've seen people who are on the front lines of really trying to adopt the technology as much as possible there. But by and large, I would say on average, as a group, the senior engineers underrate what AI can do for them, and stick to their existing workflows. And so the relative ranking is a little hard, I think they fall into different anti-patterns, but they both, by and large, yet get big benefits with these tools.

Lenny Rachitsky (00:51:04):
That makes absolute sense. I love that it's two ends of the spectrum, expect too much, don't expect enough. It's like the three bears allegory.

Michael Truell (00:51:15):
Yeah.

Lenny Rachitsky (00:51:16):
Yeah. Okay.

Michael Truell (00:51:18):
Yeah. Maybe the sort of senior, but not staff, right in the middle.

Lenny Rachitsky (00:51:24):
Interesting. Okay. Just a couple more questions. What's something that you wish you knew before you got into this role? If you could go back to Michael at the beginning of Cursor, which was not that long ago, and you could give him some advice, what's something that you would tell him?

Michael Truell (00:51:38):
The tough thing with this is, it feels like so much of the hard-won knowledge is tacit, and a bit hard to communicate verbally. And the sad fact of life feels like for some areas of human endeavor, you kind of do need to fall on your face to... Either need to fall on your face to learn the correct thing, or you need to be around someone who's a great example of excellence in the thing. And one area where we have felt this is hiring. I think that we actually were... So we tried to be incredibly patient on the hiring front.

(00:52:20):
It was really important to us that, both for personal reasons and also for, I think actually for the company's strategy, having a world-class group of engineers and researchers to work on Cursor with us was going to be incredibly important. Also, getting people who fit... A certain mix of intellectual curiosity and experimentation, because there can be so many new things we need to build. And then also an intellectual honesty, and maybe micro-pessimism, bluntness, because if all the noise, and... Especially as the company's grown, and the business has grown, keeping a level head I think is incredibly important too.

(00:52:59):
But getting the right group of people into the company was the thing that maybe more than anything else, apart from building the product, we really, really fussed over. We actually waited a long time to grow the team because of that. And I think that many people you hear hired too fast, think we actually hired too slow to begin with. I think it could have been remedied, I think we could have been better at it.

(00:53:28):
And the method of recruiting that we ended up eventually falling into and working really well for us, which isn't that novel, of going after people that we think are really world-class, and recruiting them over the course of, in some cases, many years, ended up working for us in the end, but I don't think we were very good at it to begin with. And so I think that there were hard-won lessons around both who was the right profile, who actually made sense in that team, what did greatness look like, and then how to talk with someone about the opportunity, and get them excited if they really weren't looking for anything. There were lots of learnings there about how to do that well, and that took us a bit of time.

Lenny Rachitsky (00:54:12):
What are some of those learnings for folks that are hiring right now? What's something you missed or learned?

Michael Truell (00:54:18):
I think to start with, maybe we actually biased a little bit too much towards looking for people who fit the archetype of well-known school, very young, had done the things that were high credential in those well-known school environments. And actually, I think found... Were lucky early on to find fantastic people who are willing to do this with us who were later careered. I think we should kind of spent a bunch of time on maybe a little bit the wrong profile to begin with, and part of that was a seniority thing. Part of that was kind of an interest and experience thing too, we have hired people who are excellent, excellent, excellent and very young, but they maybe look in some cases slightly different from being straight out of central casting.

(00:55:12):
Another lesson is just, we very much evolved our interview loop, and so now, we have a hand-rolled set of interview questions, and then core our... Core to how we interview too, is actually, we have people onsite for two days, and do a project with us, a work test project. And that has worked really well, that increasingly you're finding that. I think how to learn about what people are interested in, and put our best foot forward, and letting them know about the opportunity when they're really not looking for anything, and have those conversations. There's definitely been... Gotten better at that over time.

Lenny Rachitsky (00:55:53):
Do you have a favorite interview question that you like to ask?

Michael Truell (00:55:56):
I think this two-day work test which we thought would not scale past a few people has had surprising staying power. And the great thing about it is, it lets someone go end-to-end on it like a real project. It's not work that we use, it's canned list of projects. But it gives you two days of seeing a real work product, and it doesn't have to be incredibly time-enhancing other teams from time. You can take the time you would spend in a half day or one day onsite, and you kind of spread it out over those two days, and give someone a lot of time to do work on their projects, and so that can actually help it scale.

(00:56:38):
It helps to enforce, do you want to be around this person type test, because you are around this person for two days, a bunch of meals with them. We didn't expect that one to stick around, but that has been really, really important to our value to process, and then also important to getting people excited at, especially the very early stages of the company. Because before, people are using the product, and know about it. And when the product is comparatively not very good, really, the only thing you have going for you is a team of people that some people find special and want to be around. And the two days would give us a chance to just have this person meet us, and in some cases, hopefully get convinced that they want to throw in with us. That one was unexpected. Not exactly an interview question, but kind of like a forward interview.

Lenny Rachitsky (00:57:29):
The ultimate interview question. So just to be very clear about what you're describing, you give them an assignment, like, "Build this feature in our actual code base, work with the team to code it and ship it." Is that roughly right?

Michael Truell (00:57:40):
Yes. So we don't use the IP, not shift end-to-end, but it's like a mock... Very often in our code base, "Here's a real mini two-day project. You're going to do it end-to-end." Largely being left alone, there's collaboration too. And then we're a pretty imprisoned company, in almost all cases, it's actually just sitting in office with us too.

Lenny Rachitsky (00:58:02):
And you've been saying that this has scaled to even today, so how big are you guys at this point?

Michael Truell (00:58:07):
So we are going on 60 people.

Lenny Rachitsky (00:58:10):
So small for the scale and impact. I was thinking it'd be a lot larger than that.

Michael Truell (00:58:15):
Yeah.

Lenny Rachitsky (00:58:16):
And I imagine the largest percent is engineers?

Michael Truell (00:58:19):
Yeah. To be clear, a big part of the work ahead of us is building a group of people that is bigger, and awesome, and can continue to make the product better, and the service we give to customers better. And so you don't plan to stay that small for longer, wouldn't hope so. But part of the reason that that number is small is, the percentage of engineering and research and design is very high within the company, and so many software companies when they have roughly 40 engineers would be over 100 people, because there's lots of operational work, and often, they're very, very sales-led from the get-go, and that's just quite labor-intensive. And here, we started from a place of being incredibly lean in product-led, and we now serve lots of our market customers, and it built that out, but there's much more to do there.

Lenny Rachitsky (00:59:10):
A question I wanted to ask you, there's so much happening in AI, there's things launching every... There's newsletters, many newsletters, whose entire function is to tell you what is happening in AI every single day. Running a company that's at the center, the white-hot center of this space, how do you stay focused, and how do you help your team stay focused, and heads down, and just build and not get distracted by all these shiny things?

Michael Truell (00:59:35):
I think hiring is a big part of it, and if you get people with the right attitude. All of this should be asterisked in, I think we're doing well there, I think that we'd probably be doing better there too, and it's something that we should probably talk even more about as a company. But I think that hiring people with the right disposition, people who are less focused on external validation, more focused on building something really great, more focused on doing really high quality work, and people who are just generally level-headed, and maybe the highs aren't very high, the lows aren't very low. I think hiring can get you through a lot here, and I think that's actually a learning throughout the company, is that for any... You need process, you need hierarchy, you need lots of things, but for any kind of organizational tool that you're introducing into a company, the result you're looking to get from that tool also... You can go pretty far on hiring people with the right behaviors that you want to resolve from that for organizational thing.

(01:00:39):
And the specific example that comes to mind is, we've been able to get away with not a ton of process yet on the engineering front, and I think we need a little bit more process, but for our size, not a ton of process, by hiring people who I think are really excellent. One is hiring people that are level-headed. I think two is just talking about it a lot. I think three is hopefully leading by example. And for us personally, we've since 2021, 2022 been professionally working on this, and been working on AI, and we've just seen a sea change of the comings and goings of various technologies and ideas of... If you're to transport yourself back to end of 2021, beginning of 2022, this is GPT-3, Instruct GPT doesn't exist, there's no Dolly, there's no stable diffusion. And then we've gone through all of those image technologies existing, ChatGPT and that rise, and GPT-4, all of these new models, all these different modalities, all the video stuff, and only a very small number of these things really kind of affects the business.

(01:01:45):
So I think we've kind of just built up a little bit of an immune system, and know when an event comes around that actually is really going to matter for us. This dynamic too of there being lots, and lots, and lots of chatter, but then maybe only a few things that really matter, I think has been mirrored in AI over the last decade, where there have been so many papers on deep learning in academia, so many papers on AI in academia, then the amazing thing is there are really a lot of... A lot the progress of AI can be attributed to some very simple elegant ideas that have stayed around, and the vast majority of ideas that have been put out there haven't had staying power, and haven't mattered a ton. And so the dynamic is a little bit mirrored in the evolution of deep learning as a field overall.

Lenny Rachitsky (01:02:33):
Last question. What do you think people still most misunderstand, or maybe don't fully grasp about where things are heading with AI in building in the way the world will change?

Michael Truell (01:02:46):
People are still a little bit occupied too much, either end of a spectrum of it's all going to happen very fast, and this is all bluster, and hype, and snake well, and I think we're in the middle of a technology shift that's going to be incredibly consequential. I think it's going to be more consequential than the internet, I think it's going to be more consequential than any shift in tech that we've seen since the advent of computers. And I think it's going to take a while, and I think it's going to be a multi-decade thing, and I think many different groups will be consequential in pushing it forward.

(01:03:24):
And to get to a world where computers can increasingly do more, and more, and more for us, there's all of these independent problems that need to be knocked down, and progress needs to be made on them, and some of those are on the science side of things of getting these models to understand different types of data, be faster, cheaper, smarter, conform to the modalities that we care about, take actions in the real world. And then some of it's on how we're going to work with them, and what's the experience that a human should actually be seeing and controlling on a computer, and working with these things.

(01:03:58):
But I think it's going to take decades. I think that there's going to be lots of amazing work to do. I think that also, one of the most... A pattern of a group that I think will be especially important here, not to talk our own book, but I think is the company that works on automating and augmenting a particular area of knowledge work, builds both the technology under the surface for that, integrating the best parts from providers, sometimes doing it in-house, and then also builds the product experience for that. I think people who do that, and... We're trying to do it in software, people do that in other areas, I think those folks will be really, really, really consequential. Not just for the end value that users see, but then I think as they get to scale, they'll be really important for pushing forward the technology, because I think they'll be able to build... The most successful of them will be able to build very, very big businesses. So, excited to see the rise of other companies like that in other areas.

Lenny Rachitsky (01:04:59):
I know you guys are hiring. For folks that are interested in, "Hey, I want to go work here, and build this sort of stuff." What kind of roles are you looking for right now? Anyone specifically you're trying... Any roles you're most excited about filling ASAP? What should people know if they're curious?

Michael Truell (01:05:12):
There are so many things that this group of people need to do that we are not get equipped to do. Generic across the board, first of all, and so if you don't think we have a role for something, maybe you should reach out, that won't actually be the case. And maybe we can actually learn from you, and decide that we need something that we weren't yet aware of. But by and large, I think that two of the most important things for us to do this year are have the best product in the space, and then grow it. And we're kind of in this land grab mode, where almost everyone in the world is either using no tool like ours, or they're using one that's maybe developing less quickly. So growing Cursor too is a big goal, and I would say, especially always on the hunt for folks who... Excellent engineers, designers, researchers, but then folks all across the business side too.

Lenny Rachitsky (01:06:13):
I can't help but ask this question now that you talk about engineers, there's this question of just, "AI's going to write all our code." But everyone's still hiring engineers like crazy. All the foundational models, so many open roles.

Michael Truell (01:06:28):
Yeah. We're not out there tooting the horn of, people can learn to code.

Lenny Rachitsky (01:06:29):
Do you think there's going to be an inflection point of engineering roles start to slow down? I know this is a big question, but just... Do you see engineers being more and more needed across all these companies, or do you think at some point there's all these Cursor agents running building for us?

Michael Truell (01:06:45):
Again, we have the view that there's this both long messy middle of it not jumping to a, just you step back, and you ask for all your stuff to be done, and you have your engineering department. And very much, you want to evolve from programming as it exists today, we want humans to be in the driver's seat, and we think even in the end state, that's giving folks control over everything is really important, and you will need professionals to do that, and decide what the software looks like.

(01:07:18):
So both I think that, yes, engineers are definitely needed. I think that engineers will be able to do much more. I think the demand for software is very lasting, which is not the most novel thing, but I think it's kind of crazy to think about how expensive and labor-intensive it is to build things that are pretty simple and easy to specify, or it would look like it to the outside observer, and just how hard those things are to do right now.

(01:07:49):
All of the stuff that exists right now that's justified by the cost and demand that we have now, if you could bring that down by [inaudible 01:07:56], I think you would have tons, and tons, and tons of more stuff that we could do in our computers, tons more tools. And I've felt this, where... One of my early jobs actually was working for a biotechnology company, and it was building internal tools for them, and the off-the-shelf tools that existed were horrible, and did not fit their use case at all. And then the internal tools I was building, there was definitely a ton of demand there for things that could be built, and that far outstripped just the things that I could build in the time that I was with them.

(01:08:29):
The physics of working on computers are so great, you should be able to basically just move everything around, do everything that you want to do. There's still so much friction, I think that there's much more demand for software than what we can build today with things costing like a blockbuster movie to make simple productivity software. And so I think long into the future, yes, there will actually be more demand for engineers.

Lenny Rachitsky (01:08:51):
Is there anything that we didn't cover that you wanted to mention? Any last nugget wisdom you wanted to leave listeners with? You could also say no, because we've done a lot.

Michael Truell (01:09:00):
We think a lot about how you set up a team to be able to make new stuff, in addition to continuing to improve the stuff that you have right now. And I think if we were to be successful, IDE is going to have to change a ton, [inaudible 01:09:18] looks like is going to have to change a ton going into the future. And if you look around, the companies we respect, there are definitely examples of companies that have continued to really ride the wave of many leapfrogs, and continue to actually push the frontier. But they're kind of rare too, it's a hard thing to do. So part of that is just kind of thinking about the thing, and trying to reflect on it in our good days, and the first principle side of things, part of it's also trying to get in and study past examples of greatness here, and that's something that we think about a lot too.

Lenny Rachitsky (01:10:00):
Yeah. Yeah. Before we started recording, you had all these books behind you, and I was like, "What's that over there?" It's the history of some old computer company that was influential in a lot of ways that I've never heard of. And I think that says a lot about you of, where a lot of this innovation comes from, is studying the past, and study history, and what's worked and what hasn't.

(01:10:19):
Okay. Where can folks find you online if they want to reach out and maybe apply? You said that there may be roles they may not even be aware of, where do they go find that, and then how can listeners be useful to you?

Michael Truell (01:10:28):
Yeah. If folks are interested in working on this stuff, would love to speak, they can find... If they go to cursor.com, they can kind of both find the product and find out how to reach us.

Lenny Rachitsky (01:10:41):
Easy. Michael, thank you so much for being here. This was incredible.

Michael Truell (01:10:44):
It was wonderful. Thank you.

Lenny Rachitsky (01:10:46):
Bye, everyone.

(01:10:49):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating, or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

