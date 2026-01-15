---
guest: Ryan Singer
title: A better way to plan, build, and ship products | Ryan Singer (creator of “Shape
  Up")
youtube_url: https://www.youtube.com/watch?v=GF-yUANql0c
video_id: GF-yUANql0c
description: 'Ryan Singer is one of the earliest employees and the former Head of
  Strategy at 37signals (the makers of Basecamp), where he spent nearly two decades
  refining a product development approach...

  '
duration_seconds: 6310.0
duration: '1:45:10'
view_count: 29557
channel: Lenny's Podcast
keywords:
- growth
- activation
- onboarding
- churn
- experimentation
- funnel
- conversion
- revenue
- leadership
- management
- strategy
- vision
- mission
- market
- design
---

# A better way to plan, build, and ship products | Ryan Singer (creator of “Shape Up")

## Transcript

Ryan Singer (00:00:00):
I often use this analogy of if you're doing a home renovation, you can have the most beautiful rendering of the new bedroom and we're going to have these lamps on the side of the bed that are coming out from the wall. But if you haven't checked if there's electricity in that wall there or not, it's going to drastically change the cost and the time and everything.

(00:00:16):
What we need to do in a shaping session is we come out with some kind of diagram where engineers, product and design, they're saying, "We understand that." So the first thing is we are not going to start something unless we can see the end from the beginning. We're not going to take a big concept and then say, "What's the estimate for this thing?"

(00:00:37):
We're going to go the other way around and we're going to say, what is the maximum amount of time we're willing to go before we actually finish something? How do we come up with a idea that's going to work in the amount of time that the business is interested in spending?

Lenny Rachitsky (00:00:54):
Today my guest is Ryan Singer. Ryan was one of the first few hires at 37signals, and through his experience of building Basecamp and 17 years of building product at 37signals, he wrote a book called Shape Up, which shares a very different approach to building software.

(00:01:10):
Appetites instead of deadlines. A big focus on bringing design engine product together into a room to shape the plan versus writing long PRDs or trying to finalize designs before you start building.

(00:01:22):
I've noticed more and more teams adopting the Shape Up method, and especially with AI starting to change how we work and build product, there's this shift coming in how product teams will operate. And so I thought this was the perfect time to do a deep dive into the Shape Up method.

(00:01:37):
This episode is basically going to give you everything you need to give Shape Up a shot on your team or at your company to see if it fixes the problems that you're having shipping great products.

(00:01:46):
A big thank you to Des Trainer, Bob Moesta and Chris Speck for suggesting questions and topics for this conversation. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube.

(00:01:57):
Also, if you become a paid subscriber of my newsletter, you get an entire year free of Perplexity Pro, Notion, Superhuman, Linear and Granola. Check it out at lenny'snewsletter.com. With that, I bring you Ryan Singer.

(00:02:14):
This episode is brought to you by WorkOS. If you're building a SaaS app, at some point your customers will start asking for enterprise features like SAML authentication and SCIM provisioning. That's where WorkOS comes in, making it fast and painless to add enterprise features to your app.

(00:02:31):
Their APIs are easy to understand so that you can ship quickly and get back to building other features. Today, hundreds of companies are already powered by WorkOS, including ones you probably know like Versel, Webflow and Loom. WorkOS also recently acquired Warrant. The fine-grain authorization service.

(00:02:51):
Warrant's product is based on a groundbreaking authorization system called Zanzibar, which was originally designed for Google to power Google Docs and YouTube. This enables fast authorization checks at enormous scale while maintaining a flexible model that can be adapted to even the most complex use cases.

(00:03:09):
If you're currently looking to build role-based access control or other enterprise features like single sign-on SCIM or user management, you should consider WorkOS. It's a drop-in replacement for Auth0 and supports up to 1 million monthly active users for free. Check it out at workos.com to learn more. That's workos. com.

(00:03:33):
This episode is brought to you by Merge. Product leaders, yes, like you, cringe when they hear the word integration. They're not fun for you to scope, build, launch or maintain, and integrations probably aren't what led you to product work in the first place?

(00:03:48):
Lucky for you the folks at Merge are obsessed with integrations. Their single API helps SaaS companies launch over 200 product integrations in weeks, not quarters. Think of Merge like Plaid, but for everything B2B SaaS.

(00:04:02):
Organizations like RAMP, Dorada and Electric use Merge to access their customer's accounting data to reconcile bill payments, file storage data to create searchable databases and their product or HRAS data to auto-provision and deprovision access for the customer's employees.

(00:04:18):
And yes, if you need AI-ready data for your SaaS product, then Merge is the fastest way to get it. So, want to solve your organization's integration dilemma once and for all? Book and attend a meeting at merge.dev/lenny and receive a $50 Amazon gift card. That's merge.dev/lenny.

(00:04:42):
Ryan, thank you so much for being here. Welcome to the podcast.

Ryan Singer (00:04:46):
I am really happy to be here. Thanks a lot.

Lenny Rachitsky (00:04:48):
I think this is going to be a legendary episode. There's a lot of interest these days in different ways of working, especially ways that are Agile and SAFe and Scrum and all these ways that people hear about working. Especially in this world of AI where everything's just changing. It feels like there's just an increased interest in exploring different ways of working and specifically it feels like there's been a rise in interest in Shape Up the stuff that you talk about.

(00:05:14):
So, I am really excited to basically help people understand what is this way of working, is it right for them? What are ways to start implementing it? What are maybe some pitfalls you may run into? And as much as possible get into a lot of real talk about how things are actually going on product teams that people often don't like to hear.

(00:05:31):
So, first of all, have you also seen this increased interest in Shape Up?

Ryan Singer (00:05:38):
Yeah, I think it's interesting that we're talking now. I mean, the book came out in 2019 and it's, I've been hearing more and more like, "Oh, we know somebody who's trying it or we're hearing it when we go talk to other companies." So, I think, it's a wave that's slowly building.

(00:05:57):
And it's funny, when it came out, I even tried to have an online forum to get everyone who's interested to talk together and what I started to learn pretty early on is that people don't like to talk about their struggles shipping.

(00:06:13):
Especially CPOs and CTOs don't like to go on a public forum and say, "Our company isn't shipping or our engineering team is stuck, or our team is always lost in the weeds." That's not an easy community topic on an online forum.

(00:06:28):
So, I think, there's also some reasons why it's been word of mouth slowly gathering steam.

Lenny Rachitsky (00:06:33):
That's something I struggle with on this podcast. As you said, it's a product and product teams don't want to be sharing when things aren't going great. That's why I introduced Failure Corner on the podcast where it's like, "Okay, but tell me a time things didn't go well."

Ryan Singer (00:06:46):
Oh yeah, that's great. Yeah, because it's so hard to get to that, right? And it's not all just this golden path, rosy, where we're all shipping beautiful, meaningful things all day.

(00:06:55):
It's a hard business and there's no perfect school either that produces expert product managers and CPOs and CTOs and stuff like that. So we're all trying to figure this out and we don't have a lot of sources, so there is a lot of struggle.

Lenny Rachitsky (00:07:12):
And there aren't many options for how to build product. All people really read about is Scrum/Agile/SAFe as they scale and then there's Waterfall, which, "No, I never do Waterfall." Then there's the start up way of just ship and maybe one or two week cycles and then there's Shape Up, so it feels like it's one of the rare other options that exists. And so-

Ryan Singer (00:07:33):
That's one of the things I've been hearing. It's, I hear like, "Oh, we thought there was only Scrum or Kanban, and then we heard there was this Shape Up thing. What's that?

Lenny Rachitsky (00:07:42):
And I think it's always been connected to Basecamp. We're going to talk about that. Just, it works for companies that are nothing like Basecamp. Maybe just touch on that briefly.

Ryan Singer (00:07:53):
Well, I mean, that came as a surprise to me. I mean, when I wrote the book, I had been in Basecamp at that time, I think 15 years, and I actually didn't even know the outside world. I mean, it was Jason's idea to even write the book. Because he said, "Look, a lot of people are going to want to know about this. A lot of people are struggling." And I'm like, "Well, okay."

(00:08:16):
I knew our inside story of we had some growing pains and we had to be able to formalize the way that we were working and shipping so that as we brought new people in that they could participate in that and we could stay fast. So, I knew our internal struggles, but I honestly didn't know anything about the outside world.

(00:08:33):
And it was only after the book came out that it gave me this excuse to start talking to people from all kinds of different companies, and it's been really interesting. There are some really amazing cases of companies of very different characteristics from Basecamp, like VC funded, significantly bigger, very different pressures, different team structure, different skills who are doing it.

(00:08:58):
At the same time, there is also a lot of questions that are coming in my way because honestly, there are so few teams that are structured just like Basecamp, that there are a lot of gaps in the book of like, "Well, what about this, and what about that, and how do we do that in our situation?"

(00:09:11):
So, a lot of my focus today is actually closing those gaps and helping people figure out how can I make this work for me or for our team?

Lenny Rachitsky (00:09:19):
And you specifically told me, you just now call it instead of Shape Up it's Shape Up In Real Life or Shape Up For Real Life.

Ryan Singer (00:09:24):
Yeah. Well, my wife heard me saying the same thing over and over again on every phone call. And she's overhearing me and she's like, "You have to make a course, you have to do something. You always are saying the same thing."

(00:09:37):
So then this led to this course that we made, which is called Shaping and Real Life. And well, yeah, the idea is the real life part, right? How do I make this work if my designers don't code? It's very contentious to get engineering time. You know what I mean? When there's all these different pressures that Basecamp didn't have.

Lenny Rachitsky (00:09:56):
We're going to get into the nitty gritty of how this actually works and the key elements, but can you just give a very short overarching summary of how Shape Up is different from how other product approaches are?

Ryan Singer (00:10:07):
I think the way it's different starts with how the way we were working was a little bit different. So, I started working with Jason and David on the first version of Basecamp, which was the flagship product of 37signals back in 2003. We were a team of three.

(00:10:25):
And, I mean, I think, it's for any really small team, when you're just starting out, you don't need a process. You don't need a way of working. It just happens organically because you're together. You don't have to explain it to other people, it just happens on its own, right?

(00:10:40):
But there was always this really intense urgency from both Jason and David, "We've got to get to something we can ship. We have to finish this and move on. We have to get to something that's done." There was just no tolerance for big things that got fuzzy and started to drag. There was always this sharpening to get to what is this thing really and when are we going to get to the end soon?

(00:11:03):
And on top of that, even when we were building V1, David wasn't actually full-time as our only technical person. He was programming 10 hours a week. So, we had this really intense pressure of how can we really use David's time well?

(00:11:20):
We don't want to ever give something that this is the thing we want to build, and then it turns out not to be what we want and we have to throw it away and then come back again or you know what I mean? Those bad cycles of waste.

Lenny Rachitsky (00:11:32):
Let me actually ask about this because this is really interesting. So this is DHH. He was working part-time when he started 37signal.

Ryan Singer (00:11:40):
10 hours a week. Yeah.

Lenny Rachitsky (00:11:41):
Was he working on Ruby basically and that whole thing?

Ryan Singer (00:11:45):
Well, Rails came out of the first... So, he told Jason, "I want to try building this in Ruby," because before they had done some collaboration and David had done things in PHP before that and he had this new idea, he wanted to try Ruby, this language he fell in love with.

(00:12:04):
And then the framework, Ruby on Rails, he ended up releasing that after Basecamp was standing. Because it was extracted from the things that were necessary to give V1 of Basecamp to stand up.

Lenny Rachitsky (00:12:16):
So that's what he was doing the rest of his time instead of-

Ryan Singer (00:12:19):
I don't know. I don't know what he was doing the rest of his time.

Lenny Rachitsky (00:12:19):
Probably something great. Something-

Ryan Singer (00:12:23):
But he's always been like that. He's always doing something interesting. He's either racing or who knows what, you know what I mean? But all I knew was that we got 10 hours of that time.

Lenny Rachitsky (00:12:33):
Yeah, I love that that was a constraint to design a way of working that uses engineering time most efficiently.

Ryan Singer (00:12:39):
Yeah, I mean, put that together. So, David's constraint of 10 hours a week and then Jason has this, I mean, I think, many really successful founders and especially CEOs have this thing, it's like all they want to see is movement. You know what I mean? Forward, forward, forward.

(00:12:55):
So when do we get to see it? When do we get to try it? When do I get to put it into somebody's hands? So that combination, there was just so much urgency even though there was no outside pressure. You know what I mean? It was completely just let's say cultural energy of how do we keep getting somewhere and getting to something that we can celebrate and get excited about.

Lenny Rachitsky (00:13:17):
I love that. That's an attribute, I think, of a lot of successful founders. So that makes sense to hear that.

Ryan Singer (00:13:22):
Totally, totally. And that's why where I come back to you, this is the part of the story where, I think, so many companies would say, "Yeah, I know that experience," right? Because, I think, that's probably the seedling of, as you said, of successful companies.

(00:13:34):
Is that combination of urgency and also that those guys were so talented and that they had a clear vision of what they wanted to do and all of that. It's this amazing time actually, these early days.

Lenny Rachitsky (00:13:44):
Is there anything more to the backstory that's important to share or super interesting?

Ryan Singer (00:13:47):
Yeah, I mean, the other big piece of it was, so Jason and I were this product, what do you call it? The two thirds. So, I was doing UX at the time and I was doing hands-on coding as well. So we're very, very integrated. Everybody does a little bit of everything. All of us were coding.

(00:14:09):
Jason was in the actual app templates as well doing HTML and CSS to do the views. He's doing hands-on design. We're all very much connected with why are we building this? What is this? David's doing the bulk of the programming, and Jason and I were having these little sessions.

(00:14:28):
These little sessions where we would really figure out what the idea was and there would be this moment where you would have a few strokes of this Sharpie pen on a big pad of paper and all of a sudden you'd be like, "Oh yeah, that's the idea. That's the thing we want to go try to build."

(00:14:46):
And for me, those sessions with Jason, they were these short, very, very intense sessions where you're trying to crack the nut together. Where's the idea? What's the concept? How can we go... What's this thing that we're going to go and 10 hours later, right, David's going to come back and we're going to be like, "This is awesome. This thing works and it does something we're excited about," right?

(00:15:10):
That was really the seedling. I mean, actually that continued over years and years and years, those sessions. And that's the seedling of this word in the book shaping. What does it mean to do shaping? It wasn't sitting alone writing a document, it wasn't making a bunch of requirements.

(00:15:31):
It wasn't making a beautiful Figma file to represent a concept that could maybe be a feature. It was this super intense, really exciting collaborative, "What about this? What about that? Oh, maybe this." So that was a really big part of how we worked also.

(00:15:51):
Very intensely collaborative sessions to figure out what the idea is and getting it sharp enough and crispy enough that we could very confidently get a yes from David. That he would know exactly what it is and what it means and come back.

(00:16:06):
It would be what we pictured and it would work the way that we hoped so that we would keep going and we wouldn't have to reverse or go back to the drawing board.

Lenny Rachitsky (00:16:15):
What it sounds like is essentially you're trying to maintain the startup way of working as the company grows. Everything you're describing is how it feels to be at a startup, and this is a method to keep that. Does that sound right?

Ryan Singer (00:16:28):
That's exactly what became Shape Up, was how do we hold onto that as much as possible? I mean, one big ingredient, we had an advantage also, which was that Jason and David hired so deliberately slowly, and this is a fortunate side effect of the fact that they didn't take investment money.

(00:16:51):
So there was never that moment of now's the moment when we grow. It was always one person. And then the organism adapts. One more person. And so, this natural way of working, it was organically spreading. There were, I think, maybe 10 years before we had the first, "Wait a minute, what just happened?" That project didn't go well, that's not how things normally run.

(00:17:26):
Of course there were always ups and downs, but it was about 10 years later when we had the first project. I mean, I remember the project. I remember being at the end of... It was at that time already, it had been maybe six weeks or seven weeks. We hadn't yet completely locked the six-week thing that went into Shape Up.

(00:17:47):
And I remember we had a review session and there was a fairly new person who's doing half of the work on that team, and we had the review session and it was like instead of, "Oh, look, this is about ready to ship." It was like, "There are a lot of open questions here."

(00:18:06):
"And not only are there a lot of open questions here, we're not getting quick answers as we're asking." And what we're starting to realize is like, "Oh, not only is this not going to ship, but we can't even see the end of this."

(00:18:26):
That was one of those moments where you're like, "Oh, this isn't going to automatically, organically just keep it spreading as we hire forever." You know what I mean? We did reach a point where it's like, "Oh, we're going to have to figure out when this goes well, why does it go well and what do we do differently and how do we formalize that so it's reproducible as we keep onboarding more people?"

(00:18:52):
That's actually when Shape Up as a framework started. That's when I really started to lean in and I took over that responsibility of, "Okay, how do I systematize this?"

Lenny Rachitsky (00:19:03):
That's a great segue to let's actually talk about how the Shape Up method works. Maybe just at a high level, what are the core ingredients to the Shape Up method?

Ryan Singer (00:19:10):
There's basically three maybe big things. So, the first thing is this notion of we are not going to start something unless we can see the end from the beginning. So, we're not going to take a big concept and then say, "What's the estimate for this thing?" We're not going to say, "Oh, we need to build a calendar and then do a whole bunch of Figma files or write a whole bunch of requirements and then ask for an estimate."

(00:19:39):
We're going to go the other way around and we're going to say, "What is our appetite for this? What is the maximum amount of time we're willing to go before we actually finish something?" And we have that startup moment that we talked about. That moment of like, "Ah, you know what I mean? It works. We got somewhere." At least this, if not the whole project, this meaningful piece, we can literally walk away from.

(00:20:03):
So then what we found was that there was a lot of experimentation. We found that six weeks is the maximum that we can see into the future where we could actually say, "How do we work backward and figure out something we could build in that six weeks and really land it?"

(00:20:21):
That's the first piece. Is working backward from the amount of time we actually want to spend on something and say, "What can we do? What could we shape so that after that amount of time we've gotten to somewhere we want to be?"

(00:20:36):
It's like if you're going to buy a car or you're going to buy a house or you're going to rent a new flat or whatever, you have to have a budget in mind, right? And the budget then is how you choose between all kinds of alternatives and make a lot of hard choices and trade-offs to figure out like, "Well, I want the faster engine, but I have to give this up, or I want it to be fun to drive, but we also need space for longer road trips." You're making all these trade-offs, right?

(00:21:07):
So, this second piece is this work that we call shaping and the shaping work is, how do we actually take this fixed amount of time that we've given for ourselves and vary the scope? How do we come up with a idea, some version of this that's going to work in the amount of time that the business is interested in spending?

(00:21:34):
So, this is those creative sessions that I was talking about where we're jumping all over the room in front of the whiteboard and getting to an idea. And there, the really key thing is that we're getting to an idea where we can see the idea. We understand why we're doing this.

(00:21:52):
We're wrestling with the problem and we're wrestling with the solution until we have an idea that we can actually say, "This is what we want to go build." So it's not just calendar or dashboard or newsletter builder, but it's this idea of how we're going to tackle this problem about the calendar request, right? So that's the shaping.

(00:22:15):
And then the third piece is when we've actually carved out a fixed amount of time, when we've shaped a solution that is from a experience standpoint, from a functionality standpoint, from a technical standpoint, doable and desirable, something that we can make happen in that amount of time, then we can give it to a team.

(00:22:41):
We don't have to do the sometimes called scrum, the paper shredder. That's where you take an idea and then you split it into 100 tickets, right, and you hope that it all glues together still after you've done that step. We don't want to do that.

(00:22:57):
Instead, we want to have a whole idea, give it to a team so they see the whole, they really understand it, right? And then they can come up with their tasks and they can figure out how to track that and break it into pieces so they can actually take more responsibility.

(00:23:13):
And so what we see is way more engagement, especially from the technical team, right? Because instead of, "Here's your ticket," or "Here's your user story," it's like, "Here's the thing you understand, that makes sense, and now you're going to have freedom to figure out how to actually make this a reality."

(00:23:32):
There's going to be a million things to solve in the implementation detail, and now you have a bunch of fun problems and you don't have to keep asking questions to other people to understand what this is or how do I make a trade off or that thing.

Lenny Rachitsky (00:23:44):
One of the core elements of this, and I want to confirm is that you can pick and choose these things into your team. You don't need to do this wholesale, correct?

Ryan Singer (00:23:54):
You don't need to do any of it. So, this is where it helps to look at what's going wrong and what are we trying to fix? And then what do I want to bring into this, right?

(00:24:08):
And usually, what I notice is that people, they like to start sometimes with, "Oh, I want to give the team, let's say six weeks and I want to give the team more latitude or let's say more creative freedom, that they're going to be responsible in this six weeks to figure out how to make it happen."

(00:24:24):
And usually a lot of the drive for that is, "I'm getting tired of having so many meetings and rituals and things that are not actually working on the problem and doing the work." I mean, especially scrum teams, they often complain about that.

(00:24:40):
So, what they sometimes see in this is like, "Oh, I love this idea that the team is just going to be cooking for six weeks and they're not going to, we're going to meet as needed and we're going to workshop things, but we're not going to be busy with all these rituals all the time," right?

(00:24:54):
Now, the thing that's tricky is that if you want that reality of the team happily buzzing and humming like some happy bee colony for this six weeks, they need to have a lot more clarity around what's the thing that we're solving, right?

(00:25:12):
And so when we start working backward from that, then what we see is that, "Oh, well, if we don't shape better, then the team isn't going to have the clarity that they need to take over that responsibility, so they can make choices and make decisions and make trade offs so that they can get to the end of this thing." And the worst is that sometimes see cases where people are like, "Okay, we're doing Shape Up. So, you guys are going to build the newsletter builder, okay? But you only get six weeks to do it. So use your fixed time, vary your scope and enjoy your responsibility." You know what I mean? Which is just cruel, right?

(00:25:50):
Because I think I'll quote Bob Moesta, who's been on your show a couple times, "You can't put 10 pounds of crap in a five pound bag." So, it's a high academic statement and we can't just take any project, no matter how giant it is, and then throw it at a team and say, "Figure it out and ship something meaningful in six weeks by cutting away scope," right?

(00:26:13):
So, it starts to raise questions about how do we actually decide together what this project is? Do we actually have clarity around what the idea is and what we're going to build?

Lenny Rachitsky (00:26:30):
Let me follow up on a couple of the elements. So appetites, I think for any product manager, engineer, designer, anyone that has experienced, "Okay, we estimate this landing page is going to take a couple of weeks. Great, let's work on it," and then it ends up being six weeks can understand why this makes sense.

(00:26:47):
It's just like, "This landing page is not that important to us. Let us just say we will commit two weeks to it. We'll do as much as we can in two weeks and then we move on. And scope is not allowed to go beyond that." Makes total sense. This just makes so much sense as you listen to this, especially for people that have...

Lenny Rachitsky (00:27:00):
So much sense as you listen to this, especially for people that have just fallen into the problems of estimates not being accurate. Then there's a six-week element and the key there is your, and this is counter to maybe two-week sprints like Scrum, is that kind of the where this comes?

Ryan Singer (00:27:18):
So, actually, it turns out that the six-week is only a maximum and that's really where this number does some work for us. If we think of six weeks as a maximum, that's going to force us to ask some really good questions to ourselves about what piece of this do we really think we can land? Because if you try to say, in six months, we're going to ship this thing, you can't get your arms around all of the problems that have to get solved for an entire six-month chunk of work to actually happen. There are so many unknowns, there are so many ticking time bombs of things that we didn't understand or couldn't foresee, but if we set a ceiling at six weeks, we have a much better chance of, I think that's the size of something where we can actually shape it and surface enough unknowns and reveal that complexity before we're in the middle of it.

(00:28:15):
It doesn't mean that we can't use this technique to do a two-week project, especially if you're on a growth team, you don't want to wait six weeks or, you know what I mean? You're going to have to artificially bundle things together to do six weeks. It's like, look, I've got something I want to ship in the next week and then I've got a thing that might take two weeks after that and then a week after that. So, it's more a question of what we're trying to take on. It's really that upper limit.

Lenny Rachitsky (00:28:39):
Okay. So, it could be a two-week cycle and the appetite is-

Ryan Singer (00:28:41):
It could be a two-week thing.

Lenny Rachitsky (00:28:43):
Cool. So, it's like we're going to build this new landing page, we're going to give it two weeks and then do a shaping session on that.

Ryan Singer (00:28:48):
Now, the other side of that is when it comes to feature development or building something that's going to be needy enough to sell, then there's very few things that are going to be a substantial value add to a product that you can do in two weeks. So, then you get into a point where, well now, we're just sprinting and we're just taking one bite after the other. And then that's where we can land in that situation where we feel like, "Ah, I can never see the end of this. I just keep going back and saying, one more sprint, one more sprint, one more sprint." But six weeks is this long enough chunk or sometimes, four weeks that the question is kind of, what's big enough that we can actually get somewhere with this amount of time?

Lenny Rachitsky (00:29:32):
And there's an implied element to this that I think is worth highlighting. The whole idea is you commit to the appetite and if you are not on track to hit that instead of extending the date you cut in order to still hit it.

Ryan Singer (00:29:48):
This is a tricky one.

(00:29:51):
So, you're right that it's implied, but the thing is, in real life, if you make a commitment and you get alignment that we are going to spend six weeks of engineering time building this thing, if you get to that end of that six weeks and something is going wrong, it wasn't shaped, we can't see the end of it. It's more complicated than we thought. All these different things. And by the way, we can also talk about why those things happen, but when we get in that situation, if we're at the end of the six weeks and it's not looking good, we can't just cut off what we agreed to that made this thing valuable. We can't just cut the scope and say, "Oh, well now, we managed to ship inside of six weeks." That's going to kill everybody's morale. Everyone's going to feel disappointed. We're going to feel like this wasn't really worthwhile.

(00:30:43):
And now, we go into the next cycle with this debt feeling that we didn't actually finish the thing we were supposed to finish, so now, we're like overtime. None of that is good. And if we also go the other extreme and just say, well, should we say in the book, we had this principle at base camp which was this notion of the circuit breaker. If a project is not on track to actually finish after the six weeks, we're just going to cancel it and rethink. Almost no teams have the stomach for that, but the version of that that's more stomachable is look, we can't just cancel the project and then say, "Let's see what comes next." But what we can do is say, "We're not going to keep reinvesting in something that we don't understand."

(00:31:34):
So, let's take this out of build mode and bring this back into shaping mode, which might mean different people, a different conversation asking different questions, doing a different kind of work to suss out what is it that's fuzzy here? What is it that we couldn't see? What do we not understand? How do we get to the clarity that we need, so that we can actually say this thing is going to happen if we give it another whack.

Lenny Rachitsky (00:32:02):
I love just how real this approach is not this theoretical. Okay, cool. After six weeks, use just the scope and it's all that's cool.

Ryan Singer (00:32:10):
Yeah, you just cut the scope.

Lenny Rachitsky (00:32:11):
Yeah.

Ryan Singer (00:32:11):
No problem.

Lenny Rachitsky (00:32:12):
Shape your gut, put your gut.

Ryan Singer (00:32:13):
I've seen some Shape Up adoptions that looked like that by the way, and that's not the way. The shaping step is crucial. And what you mentioned with your landing page example, by the way, it's so seductive because we can imagine, oh, Parkinson's law, right? If you give me six weeks to do the landing page, I'll find a way to use it, but if you give me two weeks, then I'll stop after two weeks. But when it comes to real product work, where there's some functionality that we have to figure out how to make it exist, we can't just cut the scope if we run out of time. So, what it means is that the shaping work is really working hard together to figure out what are the main moving pieces of this thing. How do we narrow down our understanding of the problem and how do we identify what the moving parts are of the solution and what actually connects together for this feature to work?

(00:33:19):
And when we really get to the level where we can say, "Oh, we need to do this, this, and then the engine is going to turn," that's the place where we can say, "Oh, this is well-shaped." And it's a different kind of work. In shaping in real life, we call it, we actually teach it as doing live shaping sessions, and this was how I did it for years with Jason. We'd get into the room and I had both the technical and the UX side, so both sides were represented there in one person in that case, but for a lot of teams today, we actually teach them how to bring the senior engineering person who isn't just senior in title, the one who actually knows where the bodies are buried, how the old stuff works and what's truly possible and what's hard and what's easy in our infrastructure, like the person that really knows.

(00:34:12):
You bring that person together with the product person who deeply understands the backstory of why this is an opportunity and what we're trying to solve with this. And then a designer in the room and they're whiteboarding and wrestling with each other to get to what's a version of this thing that we believe in that's real that we can actually finish in that time.

Lenny Rachitsky (00:34:30):
This is great. Let's go one level deeper on this shaping session. So, a few tactical questions. How long are these sessions? It sounds like the people that join are a designer and an engineer and an NPM. So, add anything else there. And when do they happen is at the end of a... Do you call it a cycle by the way or sprint, the six-ish week period?

Ryan Singer (00:34:51):
What I actually like is time box actually, because the thing is that some teams need regular cycles because they have parallel teams and they need that cadence in order to reduce management overhead. But if you're small and you only have one or two teams, you might not need to be on a fixed cadence or a cycle plan. You might be able to just set one time box after another. So, the key thing is actually that that time is pushing back at you and that you're being intentional about, what's my time budget that I need to shape into?

Lenny Rachitsky (00:35:24):
Let me take a quick tangent because if you're, that's so interesting that the time boxes can be very different lengths. Imagine at a larger company, this gets complicated when other teams are trying, there's dependencies and timelines launch and go to market dates and all these things. What's the largest company this approach has worked at? What's the ideal company stage for Shape Up?

Ryan Singer (00:35:47):
It can function in very large companies. We have, for example, I have some friends at a, what is it called? They're doing clinical trials. So, they're in the pharmaceutical industry and the companies, thousands of people, and it's not that every team is doing this, but they have a few teams that are working in important areas and they're doing this and it's completely possible in that context, if you have someone who's at a senior level on the engineering side who is able to make the right architectural choices and also do some negotiating and be the backstop to make sure that someone isn't going to get pulled away onto something else, if you can carve out, oh, this system can be worked on independently of that system. This was actually what David at Basecamp has always been amazing at is this dependency, how...

(00:36:47):
It's actually not. It's not. So many people are used to it and they think that it's just how it is, but it's actually not. It is possible for engineering leadership, good engineering leadership untangles things, so we can work on this system without having to be thinking about this other system somewhere else. So, when you have some untangling with your infrastructure and with your architecture from an engineering standpoint, then you have some freedom. And then if you can also figure out the capacity management side of I'm going to protect this team from that other work for this number of weeks, you can really get a lot done.

Lenny Rachitsky (00:37:23):
This insight that you can operate this way at a larger company and the whole company doesn't have to operate this way, I think is really freeing to a lot of people. What's the adapter? And I want to come back to the actual shaping process, but I can't help but ask this. Say the company's operating a quarterly cadence or six month cadence and then there's a team operating in a two week, sometimes six weeks, sometimes four week cadence advice on how to, what's the adapter that connects those two cadences?

Ryan Singer (00:37:50):
So, there's two different things. So, I've seen cases where they've decided on a four-week plus two-week or so they'll do five-week and then one week of cool down in between and then they time it so that it adds up to a quarter. I've seen that. The other thing I've seen is when the team is just continuously delivering meaningful things, it doesn't have to line up because from the executive level, if you are CP or CTO or in these bigger cases, it's more like a VP in some area, but you're coming to the table where you're supposed to be reporting of what your group is doing. And when you are consistently saying, "We said we were going to do this and nothing finished and now, we're doing this and it's going to finish," and the next time you say, "We said we were going to do that and it's finished, without excuses and without, well, maybe another few more months or we're working at it," that's what everyone wants to see is that movement.

Lenny Rachitsky (00:38:52):
Yeah, if you're doing great, people will leave you alone. That makes sense.

Ryan Singer (00:38:54):
For sure. For sure.

Lenny Rachitsky (00:38:56):
I love that. I love that point. Okay, coming back to shaping, maybe one way that would make it real easy for people to understand, what's the output of the shaping session?

Ryan Singer (00:39:05):
The output of the shaping session is, and by the way, about shaping session, maybe we can talk a little bit about what shaping is not because we need the contrast sometimes. So, very often, when people try Shape Up, what I see is a product team creating either a lot of Figma files or maybe a lot of documentation, like a PRD with a bunch of requirements and a bunch of backstory and good reasons why we're doing this and stuff like that. And what you see is that when you give that to a team as this is what we shaped, what happens is it blows out. So, you probably know about what happens when the Figma file makes first contact with the engineering team. There's a reality check that happens there and very often, there's a back to the drawing board. So, when there's a lot of solutioning all the way down to detail without engineering involved, usually, that's a painful recipe and then it's like, "No, we can't do that," or, "Actually, it doesn't work like that."

(00:40:16):
And then on top of it, the other big challenge is that there's so much that you can't see on the surface of a UI. How do we flow from here to there? What are the different cases of logic? In which case do we move from here to here to here in the flow? What is happening behind the scenes? It's like the engineering team, they have to put on their x-ray goggles and study this thing to try and understand what's happening underneath. I often use this analogy of if you're doing a home renovation, you can have the most beautiful rendering of here's the new bedroom, and we're going to have these lamps on the side of the bed that are coming out from the wall, and you can have the perfect rendering and the perfect lamp and the perfect color, but if you haven't checked if there's electricity in that wall there or not, it's going to drastically change the cost and the time and everything if you're going to have to rip open those walls to feed some lines up to those lamps.

(00:41:15):
So, what we need to do in a shaping session when it's going well is we come out with some kind of drawing or diagram where engineers, product, and design are all looking at that and they're saying, "We understand that. I know exactly what to go build." I'll use the example of the calendar from the book. So, what is a calendar? So, first of all, there was this work that we had to do before we could even shape it, which is like, can we actually narrow down this problem? In shaping in real life, we call this framing. And in the book, there's a chapter called Setting the Boundaries where we get into this and it's like, look, we are not going to just build calendar, which is Google Calendar. Who knows where it ends? We narrowed it down to we understand that for our specific customers who are requesting this again and again, it's more about I need to see empty spaces and in the existing agenda view, I can only see things that are already scheduled and I can't see free spaces where I could book something.

(00:42:21):
So, we got to that point of what we're trying to solve here is the empty spaces. So, that's a good frame. Then what are we actually going to build? We came to, here's a good rule of thumb. If it's shaped well, you can usually describe it in less than 10 moving pieces. If I can say, "It's going to have this, this, this, this, this, and this," and that's how we're going to let people see the empty spaces, that's a good indicator that it's clear enough that it's shaped well. So, in this case, when you go to an airline and you want to book something, you see this two-month grid. So, it's like there's going to be two months side by side, but they're just going to have dots in them to indicate if there's a free day or not, if there's something in that day or not, like the iPhone calendar, I think still has this where it's just dots on the month view.

(00:43:17):
And then if you tap a day with a dot in it or without a dot in it, there's going to be an agenda view that slides underneath, which is going to show you what's scheduled in that day. And then there's going to be navigation to go forward and back in the months, there's going to be a create button to create an event, and that's more or less it. So, what you can see here is it's not like, what is a calendar? It's not a calendar. It's a two-month dot grid with scrolling agenda view underneath and the ability to hit new when you're looking at an empty space to create something in what you're viewing. So, that's the kind of thing where that's shaped and we can talk about what that means and what it entails, and we can have a really practical, realistic conversation about, is that a thing we can do in six weeks?

(00:44:12):
That's going to be a real conversation and not looking at a whole bunch of mock-ups and trying to x-ray to figure out what's actually the intent here and what's really real and what's not and what's possible and what's not.

Lenny Rachitsky (00:44:23):
That was a great example. This is really helpful. So, if I were to try to describe this, essentially what you're coming out of it with a shaping session with is like the user experience with just wire frames/sketches of the screens and the key buttons and flows. So, it's like the architecture with key components, not like a dock of spec and not final design, and also not just a user story. As a user, I need to be able to see empty spaces.

Ryan Singer (00:44:56):
Exactly. So, because the thing where it goes wrong. If we're going to commit engineering time and it's like we believe there's some way to see empty spaces, but the way is a question mark, it's a really risky way to spend that time.

Lenny Rachitsky (00:45:11):
Because you're committing, right? It's like-

Ryan Singer (00:45:12):
Yeah, we're committing and that time is really valuable. That's six weeks of engineer's time, and that time wasn't easy to get in the first place because, of course, there's all these other forces in the company that want to be doing something with the engineers. So, if we want that team to be really using that time well where they are moving, they understand what they're solving and they're creatively engaged because they know what it's supposed to be doing, they need to have that clarity both on the problem side of this is about the empty spaces and on the solution side of it's a dot grid with two months and a scrolling agenda view and a button. There's still a million interesting creative tasks there in the actual high fidelity design in the code. There's so many things to solve there, but that is something that they can all hold in their heads and understand and work on.

Lenny Rachitsky (00:46:06):
This episode is brought to you by Airtable ProductCentral, the unified system that brings your entire product org together in one place. No more scattered tools, no more misaligned teams. If you're like most product leaders, you're tired of constant context switching between tools. That's why Airtable built ProductCentral after decades of working with world-class product companies. Think of it as mission control for your entire product organization. Unlike rigid point solutions, ProductCentral powers, everything from resourcing to voice of customer to road mapping to launch execution. And because it's built on Airtable's no-code platform, you can customize every workflow to match exactly how your team works. No limitations, no compromises. Ready to see it in action? Head to airtable.com/lenny to book a demo. That's airtable.com/lenny.

(00:46:58):
You mentioned, and I think a lot of people listening to this are going to be like, "Oh, I'm scared of doing this," is if you get too detailed, the engineers and designers on the team are just like, "What the hell? You're just telling me what to build. That sucks. I don't want that kind of work." So, is the solution to that the engineering lead was super involved and detailed, and the design lead was super involved, and so you can trust that you're not just the code monkey building the thing they told you to build?

Ryan Singer (00:47:26):
That's really interesting. I got to tell you, the dominant failure case that I see in the real world is always, again and again, not enough detail. And it's also the most common failure mode where the engineers run back to the product folks and say, "I'm not getting enough from you." It is really like that, but I can understand why the hair stands up on the back of the neck a little bit thinking about it because, of course, if you give a senior engineer like, "Here's how I want you to go implement the schema for this database change for this model," they're going to be like, "What do you think? Who are you? Who are you?" You know what I mean? But what's really interesting is it's not a universal thing. The amount of detail that the team is going to feel helps them is a dial that we can turn that depends on who's on the team.

(00:48:28):
So, if you have a more junior person who's on the build team and then you have a more senior engineer who's involved in the shaping, they can make that junior engineer much more successful with additional detail. So, we're going to do this and I would suggest approaching it like this, this, this, and this. That junior person is, when they don't know how to do it, they're not going to ask because they don't want to show that they don't know, and they're going to hide the fact that they're lost and it's going to blow up later in the project. And on the other hand, if they are given more guidance, they're going to be able to be successful. They're going to learn about this is how this person who knows well, kind of approached it and then in the next round or a few projects later, you can dial it back and say, "Well, let's give less detail and see how they handle it."

(00:49:19):
So, you can really give people bigger shoes to grow into and help them to be successful. And then, of course, you can also do it the other way around where if you've got some really stellar talent on the team and you have a long history and you have a lot of trust that they are going to be able to understand and solve it, then of course, you can leave things out.

(00:49:40):
But the thing that I often see is if there's someone on the build team who really feels that they should be involved in the fundamental decisions about the approach, then a better solution would be to actually bring them into the shaping and have them play that technical role in the shaping session. If they have the right skills and the right perspective and the right knowledge to play that role well, then just bring them into the shaping. So, it's all about how do we bring people into a moment where we are using their strengths and then we're giving them an input, so that whatever their work step is that they're able to apply the maximum creativity, but also have the maximum clarity, so that they can really use that time well and also feel good about what they're doing.

Lenny Rachitsky (00:50:29):
It feels like the core of this is de-risk the biggest risks and address the biggest unknowns as much as possible. There's probably this 80% of here are the risks. Let's just understand them deeply before we commit to this appetite.

Ryan Singer (00:50:42):
That is exactly right. There are these, we can call them rabbit holes, we can call them time bombs. There are these things where we say, "Oh, it'll be fine." One example, simple example, I worked with a team and they had a step of onboarding in a FinTech product and there was this step of onboarding and they would lose a lot of people in the funnel at that step because you had to fill out a whole bunch of information, and they figured out that they could actually pipe that data in from one of the partners that they had. They were partnered with banks and they're like, "Oh, we don't even need to be asking people this. So, we're going to fix conversion. We're going to eliminate a step from our user experience. It's going to be great."

(00:51:26):
The thing that they didn't look at was if you go into the code on that step of the onboarding, it's not actually one step. There's like three different branches of that step depending on which bank the customer is integrated on. And so, that's the kind of thing where it all sounds so great and simple, and then you get into the weeds and you realize like, "Oh, wait a minute." You know what I mean? So, now, we have decisions to make. Now, if you're in the middle of a project and it's already been resourced and people are already on the hook that we're supposed to be doing this, and you already got the alignment that the engineering time is happening for this, and you're finding that out in week four. You know what I mean? You did all these beautiful drawings, by the way, and now, you're finding this out in week four, that's a bad place to be.

(00:52:14):
But if we're in the shaping room and we didn't kick this thing off yet, we didn't even green light the project yet, and we have an engineer there, not just the product people, not just the designer, but we have that engineer who really insists on sometimes, I like to think of it like the grumpy old plumber who's seen everything and he insists on opening up the walls and looking at the pipes before he'll give you a quote. So, it's like when you've got that person in the room, they're saying, "Yeah, that all sounds great. Let's take a quick look at the code and figure out what screen you're actually talking about. Just let's just take a quick look." And it only takes a moment to open up the code, find this thing that we're talking about, and really look at it and say, "Oh, it's more complicated than we thought."

(00:52:59):
And now, it's not like, "Okay, now, we're screwed and the project is going to be bigger." Now, we can have a really cool conversation about trade-offs. So, let's say we've got three different integrations here, three different segments integrated into different banks. How big are they relative to each other in terms of the deals we made or the percentage of customers who flow through those three different conditions? If we just did this on one of those branches, would it be a win? And if we did it on all three, how much more time would we have to negotiate for and would it feel worth it? You see, we're getting into this horse-trading of what is important, what's worth it, what do we need to get out of it? And that's really productive. And when you're doing that before the project starts off, that feels like, "Oh, we're talking about the important things. We're not failing right now. We are engaged in the hard questions that are going to enable us to really ship something that's successful later."

Lenny Rachitsky (00:53:54):
Well, let's go one level deeper on this shaping session, because clearly, that is so core to this working, and I know you have a whole book about how to actually do this. So, we're not going to-

Lenny Rachitsky (00:54:00):
... to this working, and I know you have a whole book about how to actually do this, so we're not going to answer all the questions, and there's a lot of detail and nuance. But a few questions, how long do these usually take? It sounds like a whole day experience, and then it sounds like you invite as few people as possible, but not too few people. What's your guidance on who should join?

Ryan Singer (00:54:21):
In this shaping and real life course, we've been doing workshops where we try to help people to learn what it's like in a shaping session. One of the things that's always interesting to me is how... So Kathy and I will be running the session and we have to... People aren't used to working so fast. What are we actually doing right now? What's the decision? What's an idea right now? We're not going to go away and draw something, and then I'll comment on a document and then come back and get together tomorrow. What ideas do we actually have right now starting from zero? So imagine, we've narrowed down the calendar problem too. It's about empty spaces. We are willing, from a business standpoint, to spend six weeks on a whack at this where it's solved. We believe there's a way that's possible, so what can we come up with?

Lenny Rachitsky (00:55:23):
And that's the input to the framing session or sorry, the shaping session.

Ryan Singer (00:55:27):
Exactly. Having a narrowed down problem from the framing work, and this is a whole other topic of very often the PMs are sometimes just taking something at face value and not negotiating down to really narrow down what is this really, and where is the value in this? But let's suppose that that's happened, that we've narrowed down the problem, so now we've got a narrow problem. So now what we need to do is try out different ideas, and this is the real thing. We have to try to break them. So I want to draw an idea, and then I want the technical person to find, oh, this isn't going to... You know what I mean? This isn't going to work because of this reason. Or the product person is going to be looking in and saying, "I get that that's really an easy way to do it technically, but I don't think that we're actually delivering the value if I play through the customer scenario here." You know what I mean?

(00:56:24):
So there's these different angles where the idea can fail, and one of the things that we also coach people to do in a session is not just to go down one path and then be stuck in one idea and now you're going in circles around little details of one idea for three hours, but to really step back and say, "Here's an approach. What if we had the scrolling agenda view, okay? And that's idea A. Then what's a very different way of doing this?" Do you know what I mean? If we didn't want to have the agenda view there, is there a way to do this where it's just a month view? Let's see if we can draw that. So that's the thing that's happening. You asked about the time, and I started with people aren't used to just going all the way in to actually trying ideas.

(00:57:16):
So there is a little bit of learning how to just face that blank page and start trying things together. What we find is that a three-hour session can be very, very productive to help you figure out what do we already have that are possible approaches to this? What are some major missing things? Like, okay, I've got the calendar dot grid, I've got the agenda idea, but what about multi-day events? Do you know what I mean? So there can be these things, these what abouts. So then maybe we break and we think for a little bit, and somebody sketches some ideas on that and does a spike or two on something, and we come back again for another three hours or we come back the next day. And what I would say is if the project that you're trying to do is doable with, let's say, your existing technology, you're not inventing a new algorithm, you're not inventing some new database or... You know what I mean?

(00:58:25):
You're not doing a new AI model. It's more about how do I use the APIs and the frameworks and the tech stack that we have? How do I put that together to build something? Then if the problem is clear and the time is now, you will be able to come to a conclusion about what's possible to build in three sessions, something like that. The key thing is leaning into those sessions and really wrestling with each other. If you have just the product and the designer there and then it's like, well, we'll show this to the technical person later, then it can all blow up. And then you find out it's more complicated than you thought and you have to go back to the drawing board. We need to have all the necessary information in the same room for these sessions to go fast.

Lenny Rachitsky (00:59:17):
There's so much genius built into this approach, and it sits on top of human nature. One is just, you need to actually spend... go into the deep edge cases and nuances and not just-

Ryan Singer (00:59:31):
Yes.

Lenny Rachitsky (00:59:32):
Yeah, that's fine. Let's go with [inaudible 00:59:34].

Ryan Singer (00:59:33):
More concreteness.

Lenny Rachitsky (00:59:34):
Very concrete, very in depth, and then the appetites are... There's just so many elements of this that just connect with the way humans work versus the theory of just like, "Yeah. Well, let's see how long this will take. It'll be a great... and we'll figure it out as we're building. We don't need to really figure this out. Yeah. We don't have time for that."

Ryan Singer (00:59:52):
And we're solving a puzzle together, if it needs to be doable in this amount of time. But it also has to hit these points in terms of the problem we're solving. You know what I mean? It has to do these things, but in this time. One other thing that I would mention is that we can't be drawing Figma files. By the way, I'm being very mean to Figma so far in this conversation. There is a time when it's the right time for the Figma file. What we want to do is have that clarity around the... Let's say, we already know where the sink is going in the kitchen and now we can make final calls about the tile and the exact fixture-

Lenny Rachitsky (01:00:38):
Grout color.

Ryan Singer (01:00:38):
... and stuff like that. Right, grout color. We don't want to have to throw it all away every time something changes. So there's a time and a place where Figma is amazing and feels good and it's like, oh, now it's beautiful. Now, it's amazing. But in a shaping session, you can't collaborate on something so high fidelity. So we need also some ways to collaborate, and this is where you see these techniques in the book, like breadboarding and fat marker sketching. These are tools to help us express an idea very, very clearly in detail. We're going to hit this button and from this button, go to here. This calculation runs, then we get this answer, and then we have this choice to go here or here. That's the thing that we need to be seeing and that's the level of detail where we can move fast together but still see something real as more this breadboarding level.

Lenny Rachitsky (01:01:33):
Fat marker session is very evocative of what this whole session is about, is very high level sketches. That's a great term.

Ryan Singer (01:01:41):
The danger there that I often see is that what we don't want is to say, "Oh, Figma isn't the right thing at this level. So instead, we're going to do fat marker sketches," and what you get is the equivalent of a blurry Figma. Do you know what I mean? Just less detailed. What we need from a fat marker sketch for it to be valuable to us as builders is it has to really communicate the idea. When I look at that, I'm like, "Oh, now I get it?" And if it's more this general wire frame of dashboard goes here and there's going to be four reports, and it's like I still don't know what to build, right?

Lenny Rachitsky (01:01:41):
Mm-hmm.

Ryan Singer (01:02:23):
So if it's not telling me what to build, so maybe this is a way to come back to your question about what's the output of the shaping session, it's like it's shaped if we can give this to a technical person and they say, "Yeah, I know what to go build now."

Lenny Rachitsky (01:02:37):
I'm very happy with our overview of the process. I think we've done a really good job giving people the gist. And obviously, if they want to actually implement it, they can get the book and dive in or work with you, which we'll point people to. Say someone's like, "This is awesome. I want to do this." What would you say is a good first step for a team that's currently... let's say, they're in startup land, and they're just shipping every two weeks, maybe every week? So maybe for that bucket of folks and then also for a larger company, I don't know, Agile Scrum SAFe, and they're just like, "Oh, let's try something different."

Ryan Singer (01:03:07):
Sometimes dev teams, they like the idea of not having the Scrum ritual, so they want to take in the six weeks, but unless the engineering and product come together to figure out how to collaboratively shape, like we talked about before, that time box isn't going to go well. So I-

Lenny Rachitsky (01:03:28):
They think they're going to not have to do standups, but now it's a day of hard thinking.

Ryan Singer (01:03:33):
Well, it turns into even more meetings, because we don't know what to do.

Lenny Rachitsky (01:03:39):
And the more meetings is just that shaping session specifically. Right?

Ryan Singer (01:03:44):
No, what I mean is that if we didn't-

Lenny Rachitsky (01:03:45):
Oh, right. I [inaudible 01:03:46] right.

Ryan Singer (01:03:46):
If we only adopted the six-week cycle and said we're going to figure it out and we didn't adopt the shaping, then we just don't know what to do. And then we reached the end, and we're basically scrambling to shape it as we go. And then we run out of time, and then we feel like this wasn't... It was nice to get a break from the Scrum rituals, but we can't say that we are knocking the champagne bottle on the boat because we're celebrating the launch or whatever, again and again. Right?

Lenny Rachitsky (01:04:13):
That's a good, actually, time to maybe talk about there's obviously the spring kickoff in Scrum. What's main difference for people, because they may be thinking, "Oh, this is just like a spring kickoff." That's-

Ryan Singer (01:04:22):
Oh, that's a good one.

Lenny Rachitsky (01:04:23):
... big deal.

Ryan Singer (01:04:24):
That's a good one. So what you often see in a Scrum team is that there's somebody who creates these tickets of these are the things that are going to happen inside of the sprint. Really, in my opinion, too many cases, it's not the person who's doing the building who's creating those tickets.

Lenny Rachitsky (01:04:45):
So your product owner.

Ryan Singer (01:04:46):
So there's a big, big gap there. We could talk a lot about that, but there's gaps in context. The person who's writing the ticket doesn't actually understand the work that's involved. You know what I mean? So there are so many unknowns and time bombs waiting in those tickets that sound reasonable, but they weren't really created by the person who understands the work that needs to happen. So the key difference is two things. So in Scrum, you have a person who's not the builders making tickets, and this is what in the cruel picture is the paper shredder. In the shape-up world, you have a single idea that was shaped. This is the thing we shaped with the two months in the agenda view and da da. Go make your own tasks, because you're the professionals. Do you know what I mean? So the contractors, if you're building a house, they have to know the plans, but you don't have to tell them, "Now take the hammer and go over here."

(01:05:52):
That's their, right? So in a shape-up world, a kickoff is, here's the well-shaped idea, and now this time box starts. At Basecamp, it was really, really loose because they are just stocked with senior people. They have so many very senior engineers and all the designers are coding. They're very technical, really, really skilled people. What I found is helpful when the team is a little bit more mixed, if they're not all super senior, is a simple exercise of at kickoff, take whatever was shaped and just draw a grid with nine boxes, and give me nine boxes of the nine major chunks that you think have to get implemented from an implementation standpoint. So translate this into nine major scopes of implementation that need to somehow happen over the time box. So really, really useful exercise to kick things off, and we have a lot of teams doing that now.

(01:06:52):
If you take six weeks, that's 30 business days. You divide that by nine, it's four days per box. So you're going to get a lot of clarity from a quick exercise. And again, this is done by the builders. This is a really also good exercise for them to notice like, "Oh, wait a minute, we think there's too much scope here. Even though it seemed reasonable, when we put it into nine boxes, it's like, I don't think we can do this all." Or it's also a good moment where somebody who's more junior might describe their implementation approach, and then someone who's senior can review that and say, "Actually, we've done that before, and we'll run into this trouble if we don't use this other thing." So those really nice coaching moments can happen.

Lenny Rachitsky (01:07:39):
If you were to try this approach and have a shaping session, this is a sign you're heading in a good direction, is if the output, the team that's building it can come up with nine... Does it have to be nine? Is six cool, 10 cool?

Ryan Singer (01:07:55):
What I found is if it's more than 10, then you just get into ticket land of, here's a million things I have to do. You know what I mean? If you have 100 things, that doesn't tell me anything. But if it has to be nine or less.

Lenny Rachitsky (01:08:10):
Nine or less. Okay. Okay, cool.

Ryan Singer (01:08:13):
I actually think... I'm speculating here, but the UX designers in your audience will know about this rule of seven, plus or minus two. It's this cognitive science principle that was found about how many things someone can hold in their head at once. So this nine is the upper limit of seven plus or minus two, and it basically... It's like, do we actually have a picture of what it means to build this that we can also hold in our heads? Can we see the whole castle?

Lenny Rachitsky (01:08:41):
So what I'm hearing is if you're on a, say, Agile Scrum team today, if you want to start trying this out, it's schedule a shaping session, assume it's six weeks to start, try to come into it with a framing of here's the problem we're trying to solve. Is that a good way of thinking about it, like the problem we're trying to solve?

Ryan Singer (01:08:59):
Yeah, for sure. The question is what problem are we trying to solve, because the shaping work is more what are our options for the solution? And if the problem is too fuzzy and big, if the problem is just calendar, then the shaping is going to be this ever-expanding, never-ending thing, and we're not going to be able to get anywhere.

Lenny Rachitsky (01:09:16):
Yeah. Okay. So you spend three hours, maybe six hours in the first session. Would you recommend try to keep it to this many hours when you're first trying it up?

Ryan Singer (01:09:26):
No, I wouldn't do that. I think the key thing is actually if you get to the point where you're trying to hold a shaping session and you manage to get product and engineering into the same room to do it, you are far along. You're doing great if you're at that point. Oh, so much of the challenge is getting to the point of aligning between product and engineering that we cannot have projects that are dragging and dragging and dragging. We can't keep ending in a place where this is the end of a sprint or the end of a cycle and we still can't see the end of it, or we have to make so many cuts and compromises at the last minute that it's not the quality of... or it's not really matching what it was supposed to be in the first place. When those problems are happening or... Also by the way, this is surfacing at the exact level.

(01:10:22):
Imagine, you're the CPO, you're the CTO, and you are supposed to be answering to, "How's that work going?"

(01:10:30):
And it's like, "Well, actually, we're working on it. I can just think of a couple of times when I needed to go to Jason, and he expected me to be making progress on something and I had gotten nowhere on it. And that feeling when you are with top leadership in the room and you don't have a good answer for where you are on something is like... Oh, it's brutal, right? And then from the CEO's perspective, it's like, "Where's the movement? We're running a business here. Really, nothing is shipping still?"

(01:11:03):
This can't just keep happening. So there's some recognition somewhere either at the higher levels or within the team of, we don't want to keep dragging, we don't want to keep being lost in the weeds, and then this can be the activation energy. You gather the power to be like, "Okay, we actually want to try something different."

(01:11:26):
And in that case, what I would say is what usually works best is, okay, we're going to try a pilot project, and what we want to do is, as you said, choose a problem that's important enough to all of us that we think it's meaningful, it's going to be worth trying to do well. And it doesn't have to be six weeks. It could be something that is a little bit smaller, maybe you feel comfortable taking on three week thing for the first time. What's important is just matching these things together.

(01:11:55):
Here's a problem that we actually care about. It's timely, something that we would like to be shipped soon. It's not so small that we're not going to actually learn this new muscle, and it's big enough that it's going to feel like we really achieved something. So maybe that's going to be four weeks, maybe it's going to be six, maybe it's three, I don't know. And then getting to a place where we wrestle a bit with the problem to get the problem narrowed down. We get into our shaping session, and then we do our best. Do you know what I mean? And usually, what happens too is if we have an engineering team that's going to become free to do this work for those X number of weeks, that's the upper limit on how long we can spend to shape, and that's another real life thing, is sometimes we talk about if...

(01:12:51):
On the one hand there's this universe of never ending documents back and forth to get feedback and comments, and then on the other hand there's like the team is going to be available. We're trying to actually do this, so actually, we've got a week to shape because engineering needs to kick off next week. Do you know what I mean? That's a little bit more the real scenario when you're actually in this aligned world of we want to ship something now.

Lenny Rachitsky (01:13:16):
Yeah, real life constraints. That's a really helpful way of telling you how much time you have to do this. For people that are just like, "I don't know, any friends that are using this. It's like weird, this way of working. It's not a thing I hear about all the time." What can you say to them to help them be like, "Okay, I should actually give this a try. Here's how many people are using it. Here's impact that you've seen." Anything you can share that would help them get over that hump?

Ryan Singer (01:13:40):
I would say wait until it hurts more. If the unfamiliarity is the big problem with it, then maybe the things are fine. Because it's not like this is the only way. It's more like, changing is really hard, and if there's a good reason to do it and it's like, look, we've done it the old way. We've tried different experiments. We've even already churned through a new head of product, or we've got a different CTO in and we're still having the same problems, then there comes a point where it's like, I know that this is uncomfortable, and I don't know somebody who's done it, but I think we need to try something different because we can't continue this way.

Lenny Rachitsky (01:14:30):
That is a great answer. Following that same thread, just what are signs that it's time to try something? What sort of pain do you often see that's like, okay, you shouldn't look into this seriously?

Ryan Singer (01:14:44):
There are pains all along the journey. So I think the place where it's most obvious is at the end of the line when we thought we were going to be done and this thing is just dragging and dragging and dragging. The teams, we're not shipping things. We're running in place. We keep going in circles on this like we don't see the end. Of course, that's the culmination, but there's also a lot of pain points along the way.

(01:15:11):
So if we go all the way upstream, if we go to the source of a project, sales talk to a customer... You know what I mean? Or sales talk to a lead, and they have this idea of this thing we need to build, or the CEO had this idea in the shower the other day, or the product team did a whole bunch of research and they have a big case for why this is the thing that's important to build next. Whatever it is, there's a source from the business perspective of this is the thing we should do next.

(01:15:44):
If we just say dashboard and we don't negotiate what that means, if we just say calendar and we don't negotiate what that actually is, then what do we experience? This fuzzy thing where it's really hard to get to a conclusive answer about, yeah, that's what we need to go do. It's like the ever expanding blob. So if you've felt that before, that's already a first pain. And then of course, where does it go from there? So we say calendar, so we don't know what it means, but we say calendar, so now we give it to product and we've either got a whole bunch of Figma files or we have the PRD with a million requirements about what a great calendar is. Of course, I don't want to be cruel to the people who are putting their hearts into that work, because the Figma file is beautiful. It's just coming a little early. And the PRD is full of a lot of true things that are probably really important for decision-making in the project, but the way that it's packaged at that moment isn't something that gets absorbed. You write this document and I'm sorry, who actually reads it? You know what I mean? I know it's painful, but it's like that. And then even when we try to read it, because it wasn't shaped and we didn't get down to it's this, it's that, it's that, and that's how it works, it's hard to walk away from reading that and have anything that's in your head as, this is what we're going to go build. It's like a million puzzle pieces that you're going to have to solve. So what we see is either there's the Figma file and then there's the pushback from engineers. There's the PRD, but then it's like, okay, but we still don't actually know what to build.

(01:17:40):
There's all those things where, instead of moving forward, there's more and more questions, more and more pushback, more and more going back to the drawing board. So that's another big indicator that something is going wrong. And then when we're in the building and we thought we knew what we agreed to, we thought we all said, "Yeah, this is what we want to go make," and it's just more and more questions coming out. More and more unexpected complexity, things that we didn't anticipate, and it just doesn't feel like we're getting warmer and coming closer. It just feels like it's getting harder and harder. Those are all the signs that whatever process you use, that there's a lack of clear shaping and there's a lack of clear framing because there's a lack of clarity around what it is that we're doing.

Lenny Rachitsky (01:18:26):
Before we started recording, you made this interesting point that there's always talk of feature factories and that rarely are they actually efficient factories. They don't actually work. Talk about that.

Ryan Singer (01:18:38):
Yeah. Well, I understand what the feature factory critique is supposed to be. It's actually to the framing point of we're not negotiating the value and the outcome we're trying to get from something. We're just taking it and building it. And then of course, in the end, according to the feature factory critique, we just built it because somebody said we should build it, and then people didn't use it and didn't value it, and the product is just getting bloated. The thing is that, I would say if you have a feature factory, meaning you're continually cranking out features, you're probably quite healthy. All you need to do is feed a different input to the beginning of the factory.

(01:19:18):
What most teams are struggling with is that they don't have predictable repeatable shipping of things. At least from my experience, the bigger really widespread struggle is, stuff isn't moving, it's dragging. I can't see the end. I'm losing my... I'm feeling burned out. You know what I mean? It's not exciting to work on this anymore, all that a thing.

Lenny Rachitsky (01:19:41):
Maybe last question here is what's the sweet spot stage for a company to start using Shape Up? You basically worked in this way from the very beginning when it was just three people. What do you find... Should startups that are just starting out start working in this way, or do you find it's more useful later on?

Ryan Singer (01:19:58):
We didn't formalize it until we had to, and there was a long time where there wasn't a fixed length for projects. There was just an understanding of the urgency and a feeling of what too long felt like. And it didn't actually click into, oh, this is a cycle length and this is six weeks, and then we pause, and this is who comes together to make the decision of what's the next project, and here's who is mainly doing the shape. You know what I mean? All that stuff didn't get solved until we had reached a certain size. Usually, the main tipping point if we start from smaller to big is there's a phase when the founders are still involved in everything, and so it doesn't matter what your process is, it's going to be fine.

(01:20:40):
But then you start to hire the first other people and then for the first time you try to delegate some of those things and the founders try to be less involved, and that's often where a lot of these problems start to appear. And the founders start to ask themselves like, "We used to be fast, and now we hired people because we needed to scale, but now we're slow. So how do we be fast again? Because we know what-

Ryan Singer (01:21:00):
... well. So like, "How will we be fast again?" Because we know what it's like. If we just got back in there as founders and got our hands dirty, like we could make this go. But how do I get the people that we've brought in to make these trade-offs and make these decisions and how do I get the work to flow again? So that's something that we definitely see there. So that's a really good moment. I'm onboarding new people. I don't know what to tell them how to work. I don't want to introduce a bunch of scrum rituals. Just winging it on Kanban isn't working, because they don't have enough clarity around what to go after. So I have to babysit them all the time. You know what I mean? Like these kinds of things.

(01:21:40):
There is another extreme, which is I... We've already gone past that. We've been scrum or whatever for years. The company has been growing, like revenue is coming in, like sales is doing their job, like things are running. But man, nothing is getting out the door. And we're years in and we have an entrenched development. We have like an entrenched engineering team, which is a wall away from an entrenched product team and everybody's apart. And this thing is like, we're like stuck.

(01:22:19):
And that is more where there's going to be some tensions that are starting to appear at the executive level. There's going to be some finger pointing. There's going to be some like, "Why isn't this moving? Why isn't this happening? How can we be spending so much money in all these engineers and we don't have anything to show for it?" And that's a point where there can be kind of a... Some hard conversations need to start happening about, "How do we actually start to negotiate around how we spend time?" And we can't just have endless refactorings and infrastructure projects, but we need to be actually building things that we can sell again.

Lenny Rachitsky (01:22:54):
What an idea.

Ryan Singer (01:22:56):
Yeah. You know? But it can... There are a lot of engineering orgs that have been standing around for a while and it's all refactoring all day and tech debt and stuff like that. And there's reasons why all those things got there, but there comes a point where we have to figure out how to cut through it and make some hard choices so that we can carve out time to build the stuff that's actually going to be needle moving again and not just sustaining us where we are to run in place.

Lenny Rachitsky (01:23:24):
I imagine this latter bucket is who you mostly work with, the kind of companies that bring you in.

Ryan Singer (01:23:33):
It's been a lot of the folks who still remember what it was like to be fast and they're kind of newly too big and they don't like being slow. I've had a lot of that. I think that your intuition is right. That the market for the last category is the biggest, but it's hard to reach them. It's not easy to talk about these things. These are sensitive topics. Do you know what I mean? Like, "Our engineering team isn't shipping," and it's happening at leadership level. There's a ton of complaints happening deeper in the org, but nobody down in the org can change anything. At the end of the day, it's actually the interface at the executive level of being able to say, "How are we using our time? We have to change something."

Lenny Rachitsky (01:24:19):
To make it even more concrete in that first bucket, what's the size of org that you find is most in need of this? It's like, "How many engineers?" Or is it like when they hire the first PM? Like what's kind of the-

Ryan Singer (01:24:29):
I sometimes have the like, "How the heck do I hire the first PM and what do they do?" conversation. But usually, it's later than that. It's after they hired the first PM, after they hired the second PM, and maybe even the third. And they're getting to the... Product and engineering together are like 30, 50 people and it's like, "We thought we put everybody in the right roles. We kind of did what we were supposed to do and everything is just grinding. And why are we so slow?

Lenny Rachitsky (01:24:57):
Perfect. So 30 to 50-ish people seems like a good time to... Basically, you're finding that's when things start to really break down.

Ryan Singer (01:25:05):
That's when they show themselves and I think... I mean, if someone hears this and it all starts to make sense and they're earlier in that wave, then of course the earlier that you can anticipate it, the better, right?

Lenny Rachitsky (01:25:16):
Yeah. That's a good point.

Ryan Singer (01:25:16):
So if you're-

Lenny Rachitsky (01:25:17):
When it's too late is when they come out so-

Ryan Singer (01:25:19):
I mainly hear about it when it's too late. That's why they're reaching out-

Lenny Rachitsky (01:25:22):
Got it. So maybe closer to 30. Okay.

Ryan Singer (01:25:26):
Honestly, I think it starts the first project where, for example, the founding engineer is hands off and then the new hire is taking over responsibility. Or the person who was like sort of founder/CEO is first giving it to a PM to kind of thinking they're going to carry it through. And then, it's not exactly meeting their expectations of what they thought was going to happen. I think that's when those disconnects actually start. It's the first step away from the work where the seeds of all of these problems actually start.

Lenny Rachitsky (01:26:00):
I want to talk about Basecamp and how maybe not every company can operate like Basecamp. Before we get there, is there anything else along the lines of Shape Up that you want to add or share?

Ryan Singer (01:26:10):
Yeah. There's one key thing, which is the role of the PM. I think what we see today, out of necessity in a lot of teams, is that the PMs spend a lot of time chasing around inside of the build phase, inside the time box, to try and make sure that people aren't stuck and getting lost in the weeds and try and keep things moving. And it can sometimes be too close to project management rather than product management.

(01:26:43):
And what we see in Shape Up teams when they hit their stride is that the PM moves upstream. So the PM is less busy with, "How do I get this project to not be in a bad state when it's getting built?" And they're way more in, "How do I understand the business context? How do I narrow down the problem? How do I negotiate back and forth with maybe the CPO who brought this to me to understand where the core of it is?" That really getting the deeper understanding of the business and the problem and the customer domain and like what problem is worth solving and what's even slice of that problem is the valuable slice to argue that we should spend a few weeks on. That's the place where the PMs can really contribute a lot in the Shape Up world. That's kind of what they do, rather than shepherding the process or being a ritual master or something like that.

Lenny Rachitsky (01:27:42):
That sounds pretty wonderful. I've been doing some thinking about what an AI-oriented world does to the role of PM and it feels like very similar to that actually, where the building now is going to happen for you with AI tooling. And that means the bigger question now is like, "What the hell should I build? And is the thing I've built right and correct and likely to work?" And it feels like this is similar, it's like the PM spending a lot more time upfront thinking through what to build. And then, the building is a lot more hands off. So hands off it gets done in like five minutes when you're just like, "Well, build this thing for me." "There it is."

Ryan Singer (01:28:19):
Yeah. Let's see. Let's see. Yeah.

Lenny Rachitsky (01:28:21):
Let's see.

Ryan Singer (01:28:22):
I'm also very curious. Yeah.

Lenny Rachitsky (01:28:25):
Oh, man. What a wild time. Okay. Let's talk about Basecamp. I think we talked about this ahead of the podcast that... You want people to know that Basecamp is very unique and not everyone can work the way Basecamp works. Just talk about your insight there and your advice there when people see all this advice coming out of Basecamp.

Ryan Singer (01:28:45):
I got to tell you, I had no idea how unique we were until I was outside and there are so many things. For example, it's a lot of the things that people ask me about that are not in the book that started to reveal those things to me. That's so many things that I was just taking for granted. I mean, every designer codes.

(01:29:05):
Imagine, if every designer codes and I don't just mean HTML. I mean, like running the app locally, going in to the place where that view is rendered to make that thing look the way that they want it to look or whatever, right? I mean, like really codes, every designer. So every designer codes, where's the wall between design and engineering? Where is the moment where you arrive with the Figma file and then the disappointment and all of your hopes get destroyed because the engineer is telling you no, right? Like those moments don't even exist in that world.

(01:29:42):
And then, also, I think also there was this lack of distance between sort of the business objective, the thing that we're trying to... The reason we want to maybe do this project and the blessing of the founders and the... Like, there wasn't this kind of executives far away with some big targets and then some layer of PM and then some building. I mean, the founders were always there, right there in the problem definition still.

(01:30:14):
I mean, I can't say today, but I mean up until 2021 when I was still there. So it meant that there was so much clarity all the time around what we're solving and why and why we're making time for it. And then, of course, on the engineering side as well. I mean, imagine, you have no sales org, you have no marketing. That all of selling and marketing is happening by the unicorn founders. So it means that there isn't contention for engineering time, that there isn't like all these different sources of requests that you have to wrestle with,

(01:30:50):
And David did such an extraordinary job of... I mean, the more I see the real world, the more I'm amazed at how every six weeks, there was clear runway in engineering of like, "We have time for whatever the... Whatever we'd agreed together is the most important thing." Just blank check like six weeks at a time. Not a blank check, but you know what I mean? Like a blank six weeks, yeah?

Lenny Rachitsky (01:31:15):
Yeah.

Ryan Singer (01:31:16):
Again and again and again, years without end. Keeping that engineering capacity focused on readiness for product and totally leaning into what's exciting to do to build for the product. And not getting lost in all this refactoring and new infrastructure and technical debt and stuff like that. I mean, those are amazing. So those are some really big differences. And it doesn't mean that you have to be Basecamp to do Shape Up. But what it does mean is that when we say, "Oh, just have a shaping session and if you have the pressure of the time box, then you can make trade-offs together." It's like, "Well, if we are used to having a big wall between, for example, engineering and design, then we're going to have to learn..." Somebody who wants to start shaping is going to have to learn like, "Well, oh, I need to figure out who to bring together and how to have that session and how do we interact with each other. So that we are combining all of that knowledge that maybe at Basecamp was all in the same head in a lot of cases."

Lenny Rachitsky (01:32:18):
This is such an important point for people to hear, because there's so many people that come on podcasts like this and share, "Here's how to do it," based on their experience. And there's so many just assumptions about their resources, the people they hire, the way the founders operate. Like no sales team, I think that's like... I don't even think about that.

Ryan Singer (01:32:36):
Yeah. Imagine, no such thing as a request from sales, yeah? No such thing as pressure of like, "We need this thing in order to upsell or to close this deal." Never.

Lenny Rachitsky (01:32:47):
It sounds like you're in this Basecamp... By the way, was it called 37signals? Like it's interesting you call it Basecamp not 37signal.

Ryan Singer (01:32:54):
Yeah. I mean, so it's just like the timing of when I left. We were originally 37signals and then Basecamp became so big that we renamed ourselves to Basecamp.

Lenny Rachitsky (01:33:03):
I didn't know that.

Ryan Singer (01:33:04):
Yeah. And then, so for example, on the book, it says Shape Up and there's a Basecamp logo on the bottom, not a 37signals logo. But then, since I went back, so it's 37signals again. So I sometimes struggle with I don't know what to call it but it's both. Whatever people can recognize, it's the same powerhouse.

Lenny Rachitsky (01:33:24):
Okay. Cool. I'm glad I'm not the only one that's confused. But 37signal is the current name. Great.

Ryan Singer (01:33:29):
Yeah. Yeah.

Lenny Rachitsky (01:33:30):
So you said that it felt like you left and it was like this bubble you got out of. Was there like a moment where you're like, "You wrote this book. Everyone..." You're like, "Hey, this is how you should work," and then you're like, "Oh, wait. This doesn't actually work in real life for a lot of people."? Is there a moment there?

Ryan Singer (01:33:44):
It wasn't that this doesn't work, I was just in a foreign country. It was like we tried it and it didn't work. One of the common things I would hear is the projects kept running over. "We weren't finishing them at the end of the cycle. They kept running over and running over." And then, I would be like, "Huh. So can you show me your shaping work?" And then, they would show me a PRD and I'd be like, "That doesn't look like what's in the book." And again like, "Can you show me your shaping work?" And they'd show me like a bunch of Figma files.

(01:34:21):
And then, what I started to understand was like we have some people in a role who were used to making a certain artifact at a certain step and they just kept doing that. And I didn't appreciate... It took me a while to realize like, "There's no engineer in the picture here." And it was when we started to actually do the course, I said... Well, I did actually a couple projects where I helped teams hands-on and I learned that they...

(01:34:50):
It was the first actually consulting project that I did where I helped a team who was stuck. And what we did was we chose the engineer who was best suited to come over to product and be there in the shaping. And that was the moment when it was like, "Ah. Now, I'm in the world I know again," when we had all of that mixed in the same room again. And so, that was kind of like... That was really something... I mean, it was a total learning curve for me and there's a lot of things like that. But that was, for example, a really big one. It's like, "Oh, we have to get engineering in there."

Lenny Rachitsky (01:35:24):
You're the type of guest I most love having on this podcast, because you basically work with many, many companies, study what's working, what's not. You're not in the clouds pontificating about something. You're working with teams to make things better. And then, you take all of that learning, put it into a book, and share with us all. And so, the ROI is just incredible for us all because you've spent so much time doing this and you've actually done the work. You're not just in theory about it. So this is amazing. But we're not done yet. One question I wanted to ask is, Jason was tweeting that there's... He's working on a follow-up Shape Up book. What's happening there? Are you involved in that? What's the story?

Ryan Singer (01:36:06):
So I also saw the tweet. And I have to admit, I was a little surprised when I saw this tweet, but I had had a conversation with Jason a year earlier. And he reached out and he said, "Hey, we're thinking about doing a second edition of the book." And my first reaction... Imagine, I was actually really in the middle of learning all these things that teams need to learn in order to catch up to what was natural for Basecamp to do. And so, for me, it was like, "Interesting. I have a lot of new things. I have a lot of new ideas. Maybe collaborating on the second edition could make sense."

(01:36:46):
But what I understood was that what he wanted to do was to make an updated version of how they work, because that's always been a big thing of how... I should use the right name, 37signals, of how they market and also how they lead is they like to really show a clear example. Not like, "This is how you could do it. This is how some people do it," but like, "This is how we do it."

(01:37:09):
And I think it's their strength that they are very, very clear like, "This is how we do it and take it or leave it." What I understood was that if I did another version of the book that was just how Basecamp does it, I think it would leave so much opportunity on the table. Like there's so many people where what they need to learn is more like, "How can it come closer to where I am? If I have the wall today between product and engineering, how do I bring the right people together into a shaping session? How do we actually do that? How do I overcome all of these little challenges because this is so far from our current way of working?"

(01:37:44):
So the work that I'm doing with, for example, with shaping in real life is all about those gaps. And then, I don't know what's going to be in the second edition because they are... I guess someone there is going to be working on that. But what I'm guessing is it's going to be an update on kind of, "Up on top of the mountain over here, this is what Basecamp is doing." So hopefully, it'll be a cool thing to look at as like, "Here's a model of what they're doing." And then the question is, "What can I take from that and what do I need in order to actually be able to make it work in the real situation I'm in?" And that's kind of where... Well, that's my focus.

Lenny Rachitsky (01:38:20):
This is so interesting. Thank you for sharing. It sounds like a fork. You forked it and these are going potentially in different directions but inspired by each other.

Ryan Singer (01:38:29):
Mm-hmm. Totally.

Lenny Rachitsky (01:38:30):
So interesting. Ryan, is there anything else that you want to share before we wrap up?

Ryan Singer (01:38:37):
One thing I could throw out there is sometimes people reach out to me because their projects aren't shipping, there's a lot of struggle, there's a lot of lack of clarity. But the root cause is actually that the input at the very beginning of the process is too unclear or... Like we don't actually know what's important to customers or we're not actually sure where the value is or this kind of a thing. So there is this link, this framing step that we talked about of, "What is really the problem?", before we go into shaping.

(01:39:11):
This is the link to product strategy also. And this is the place where it can be really useful to reach for a lot of, for example, Bob Moesta stuff with the Jobs-to-be-Done and the demand-side work, trying to get clear about big... So that's the tool that I reach for at that phase. And you can think of kind of this... Before the problem definition, there's this question of like, "What's the demand? Where are people struggling? Where is really the place, the itch they're trying to scratch?

(01:39:42):
And then, a lot of the Shape Up stuff is kind of when I have something where I think there's an opportunity or I think there's something meaningful there because of what we learned from customers or the job to be done, research, or whatever it was. Now, how do I turn that into something that we can actually go do and ship in a reasonable amount of time? That's the supply side. That's where the Shape Up part fits in. So maybe it just might be cool for people to see a link there.

Lenny Rachitsky (01:40:06):
That's a great plug for a Bob Moesta episode. We talked in-depth about the Jobs-to-be-Done framework and how to actually apply it. What's the book you'd recommend there? It sounds like basically it's like Shape Up plus this book gives you a lot.

Ryan Singer (01:40:19):
Actually, the one that I recommend the most is Demand-Side Sales 101 and it's funny because it's like sales. Especially for a product person, you're like, "I'm the product person, not the sales person." But it's such a good dive into, "What are people really trying to solve?" And getting into that mindset of, "What's the struggle? What's the problem?" I think that's a really good entry point for that.

Lenny Rachitsky (01:40:43):
Yeah. I don't love that title. I feel like you could have done better there with that book's title because-

Ryan Singer (01:40:48):
It's-

Lenny Rachitsky (01:40:49):
Yeah.

Ryan Singer (01:40:50):
What's interesting about it is that it's very, very pointy for like if you are trying to make progress on sales, then it's this other kind of sales, this demand side sales. So I think maybe it's more for us who are kind of using it for different purposes. Like we're the product people trying to pull something out of it. That it's a little bit less aligned, but it's still useful.

Lenny Rachitsky (01:41:11):
Yeah. But basically it's like the Jobs-to-be-Done book is what-

Ryan Singer (01:41:15):
Yeah. It's kind of like the Jobs-to-be-Done book that's a bit more tactical. If you're really curious about the general spirit of Jobs-to-be-Done, then Competing Against Luck is a really good intro. That's the one that Clay Christensen wrote with a lot of... I think there's a lot of stuff that Bob worked on that's in there. But for a little bit more tactical like, "What's it look like to do the interview? And how to think about the struggling moment?" and stuff like that, this Demand-Side Sales is good for this strategy stuff.

Lenny Rachitsky (01:41:44):
Awesome. And we'll also link to this episode where you could get the gist of it in one hour's time.

Ryan Singer (01:41:48):
Oh, that's right. You did... That episode was great by the way. That's... Yeah-

Lenny Rachitsky (01:41:52):
Thanks, Ryan. Thanks, Ryan. Okay. We did it. This was amazing. I think this is going to help so many people-

Ryan Singer (01:41:58):
We got through it.

Lenny Rachitsky (01:41:58):
We're not done yet. Two final questions for you. Where can folks find the book, find you if they want to work with you? Anything else that you want to share? And how can listeners be useful to you?

Ryan Singer (01:42:08):
Well, they can find me at my website. That's ryansinger.co. I'm also on X on RJS. I'm on LinkedIn. So just reach me there. And how can people be useful to me? I love hearing from people who are having these problems. If you're having these problems where it's like, "Things are dragging," or, "We can't see the end and we're not getting the quality we need," and all this stuff like man. I mean, this is how I learned all this stuff is by talking to people who are in it. So even if it's not clear what's the next step yet. If that problem is real, it would be cool to hear about it. I'd love to chat.

Lenny Rachitsky (01:42:46):
Be careful what you wish for about Moesta. He was just on the podcast and he told me he's got over a hundred LinkedIn DMs with people sharing their struggles with their job search. So here you go.

Ryan Singer (01:42:57):
Oh, yeah. Job moves, that's a big one. I think that's a broad appeal. Yeah.

Lenny Rachitsky (01:43:01):
Yeah. That's true. I'm going to ask you to explain that when you do consulting work, just like how does that work? Who's that for? Just because I know that's something else you do.

Ryan Singer (01:43:10):
So it basically starts with uh, either often first CPO or CTO often reaches out first. And when it works well is when we actually get them together and then they understand that they need to change something or we have like a head of product and a head of engineering, that kind of a thing. If those two are both seeing eye to eye that there's a problem, then we can start a conversation around, "Okay. So who would be the right people for a pilot team? What are the things that are going on business-wise that could be a good pilot project?"

(01:43:41):
And then, I can help to figure out like, "How do we actually..." So almost like guiding through, like narrowing down that pilot project framing so that they have the support that it's going to be successful in shaping. And then, coaching the team so that they actually learn those shaping skills so that they can get through a session and come out with much more clarity. Like how do they actually run those sessions.

(01:44:03):
So it's kind of first working with leadership, "Who do we need to get to do this work? Who are the right people? How do we bring them into a pilot project?" Narrowing down, doing some framing work on the pilot, so it's going to be clearer in the shaping. And then, giving some guidance on how to get through that shaping with some feedback rounds. This is usually a good approach.

Lenny Rachitsky (01:44:22):
Amazing. And they can find this on your website if they want to explore this?

Ryan Singer (01:44:24):
Yes.

Lenny Rachitsky (01:44:26):
Amazing. Ryan, thank you so much for being here.

Ryan Singer (01:44:29):
Yeah. Thanks a lot. You had amazing questions. It's a subject that can go in so many directions and you kept bringing us onto some kind of a main track, so I'm really pleased. It was really nice. Thanks a lot.

Lenny Rachitsky (01:44:39):
I do my best.

Ryan Singer (01:44:39):
Yeah.

Lenny Rachitsky (01:44:40):
Thanks, Ryan, and bye, everyone.

(01:44:45):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

