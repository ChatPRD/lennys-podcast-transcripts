---
guest: Upasna Gautam
title: An inside look at how CNN builds product | Upasna Gautam
youtube_url: https://www.youtube.com/watch?v=gRiCzfFEd7c
video_id: gRiCzfFEd7c
description: 'Upasna Gautam is a product manager at CNN Digital, where she works closely
  with editorial staff and journalists to build their internal content management
  system. She is also a longtime meditation...

  '
duration_seconds: 3492.0
duration: '58:12'
view_count: 2690
channel: Lenny's Podcast
keywords:
- growth
- onboarding
- okrs
- roadmap
- analytics
- conversion
- leadership
- management
- vision
- persona
- design
- ui
- engineering
- startup
- saas
---

# An inside look at how CNN builds product | Upasna Gautam

## Transcript

Upasna Gautam (00:00):
It happens all the time, right? That is the nature of breaking news. I mean, you have to be ready to pivot at the drop of a hat. I had a big working session planned with my users to do research with them, or do user testing, and breaking news breaks, and it takes so much time and effort to gather a team of editors across the globe to do a user testing session. And when breaking news happens, they have to prioritize that over everything. So what do you do in that situation? You can be frustrated, absolutely it's frustrating. But we always have to have the ability to A, pivot of course, but also have backup and buffers in those types of scenarios.
Lenny (00:45):
Welcome to Lenny's Podcast, where I interview world-class product leaders and growth experts to learn from their hard-won experiences building and growing today's most successful products. Today my guest is Upasna Gautam. Upasna is a product manager at CNN, where she leads the team responsible for the content management system that journalists use to write and publish their stories. She's also on the frontlines of elevating the discipline of product management within newsrooms through her work at the News Product Alliance. She's also a longtime meditation and mindfulness teacher, which as we discuss ends up being pretty damn handy working at a place like CNN. We dig into how the product team operates within CNN, how they collaborate with journalists for breaking news, dress rehearsals, and also some simple tricks to build your own mindfulness in your day-to-day work as a PM.
(01:31):
Enjoy this episode with Upasna Gautam after a short word from our wonderful sponsors. This episode is brought to you by Amplitude. If you're setting up your analytics stack but not using Amplitude, what are you doing? Anyone can sell you analytics, while Amplitude unlocks the power of your product and guides you every step of the way. Get the right data, ask the right questions, get the right answers, and make growth happen. To get started with Amplitude for free, visit Amplitude.com. Amplitude, power to your products. Today's episode is brought to you by OneSchema, the embeddable CSV importer for SaaS. Customers always seem to want to give you their data in the messiest possible CSV file, and building a spreadsheet importer becomes a never-ending sink for your engineering and support resources.
(02:19):
You keep adding features to your spreadsheet importer, the customers keep running into issues, six months later you're fixing yet another date conversion etch case bug. Most tools aren't built for handling messy data, but OneSchema is. Companies like Scale AI and Pave are using OneSchema to make it fast and easy to launch delightful spreadsheet import experiences, from embeddable CSV import to importing CSVs from an SFTP folder on a recurring basis. Spreadsheet import is such an awful experience in so many products. Customers get frustrated by useless messages like, "Error online 53," and never end up getting started with your product. OneSchema intelligently corrects messy data so that your customers don't have to spend hours in Excel just to get started with your product. For listeners of this podcast, OneSchema's offering a $1,000 discount. Learn more at OneSchema.co/lenny. Upasna, welcome to the podcast.
Upasna Gautam (03:15):
Thank you Lenny, I'm so excited to be here.
Lenny (03:18):
As you probably know, I'm on this kind of quest to understand how different companies build product, especially companies that are kind of outside the Silicon Valley, just like standard tech scene. And I've always wondered what it was like to build product at a company like CNN, which is very different from where most, I don't know, tech PMs work. And so I'm really excited to have you on and to give us a little glimpse into what it's like to build product at CNN.
Upasna Gautam (03:42):
Awesome, I'm very excited to share as well.
Lenny (03:44):
So I was doing a little research on you before this chat, and I noticed that you've been teaching and studying meditation and mindfulness for, I don't know, maybe a decade? And I imagine that comes in handy at a company like CNN, which also I imagine is quite hectic at times with breaking news all the time. And so here's my question, what have you learned or brought from that practice to your ability to lead and ability to just like keep your team calm and focused during I imagine many hectic moments?
Upasna Gautam (04:16):
Love that question, and working in product in news is a very [inaudible 00:04:22]. We hear a lot about having the skills to thrive in ambiguity in order to be a successful product manager, but to be a successful product manager in news you have to be able to thrive in chaos. And equanimity is the most important skill I've developed I think across my entire life, and it's due to all of those years of practicing mindfulness and meditation. And equanimity is one of my favorite words, it means mental calmness, composure, evenness of temper, especially in crazy, stressful situations. It's the ability to remain un-rattled in like the highest of highs and the lowest of lows. And if you think about it in the dynamic of a workplace or human interaction, it's really the ability to pause before reacting.
(05:11):
And reactivity is the root cause of so many of our workplace woes and product management frustrations, and when you're able to pause before reacting you can start to undo and break a lot of those negative patterns in your brain. And in news, and especially the world's biggest breaking news organization, you can cut through that chaos with equanimity because it also really gives you this outsized advantage in everything from stakeholder management, team morale, to the way you're able to translate user feedback, to product development philosophy. And the thing is is you're always going to hear things and feedback that you don't like, and opinions that you don't like, and you're going to get frustrated. That's product management, that's life.
(05:59):
But real power to me comes from equanimity, and that comes from managing your emotional reactions, and not trying to control others. So I think when you're able to cultivate that level of self-awareness for yourself, you're able to chart a clear path forward for your team and serve as a compass in the chaos.
Lenny (06:22):
Is there a story or an example that comes to mind where things were just like, "Oh shit," and you were able to tap into that skill that you built to stay calm and focused, or even just like help your team stay focused?
Upasna Gautam (06:33):
I mean, it happens all the time right? That is the nature of breaking news. I mean, you have to be ready to pivot at the drop of a hat. And so I think more than just like the big, chaotic moments in those daily interactions when there's chaos, I think that's when it really shows its power and helps me navigate those day-to-day interactions when I had a big working session planned with my users to do research with them, or do user testing, and breaking news breaks, and it takes so much time and effort to gather a team of editors across the globe to do a user testing session. And when breaking news happens, they have to prioritize that over everything. So what do you do in that situation? You can be frustrated, absolutely it's frustrating. But you always have to have the ability to, A, pivot of course, but also have backup and buffers in those types of scenario. So any time we're planning we build in buffers for all of that chaos that's happening on a daily basis.
Lenny (07:41):
Wow, that's cool. Is that a real thing that happened? You were like, in a big meeting with all the researchers and then something went off the rails in the world?
Upasna Gautam (07:47):
Oh yeah, absolutely. Happens all the time.
Lenny (07:49):
I don't know how much you can go into all this, but what is it that you would do in that case, like as a product team? What are they looking for you to do at that moment?
Upasna Gautam (07:56):
For us it's not really anything we have to do. It is more so, "Okay, well our goal at this session was to get user testing done, or user feedback from that user testing session with our editors. And so, what do we do? Okay, well good thing we had a backup planned, right?" We don't actually have to go into that scenario, but since our editors and our journalists are customers we're there to serve their needs, but they're not here to serve our needs. They have a whole another job that they have to do. And so we have to have the ability to adapt and accommodate to those really chaotic schedules across global time zones. And so that happens again like, it's not like once in a while, it's a very regular thing that we have to be aware of and also account for.
Lenny (08:46):
Okay, again, it's like the journalists are the ones in the meeting that like, "Oh, they have to go write about the stuff uncovered."
Upasna Gautam (08:50):
Totally.
Lenny (08:51):
I see, that makes sense. You said that you built in some buffer time to kind of account for these things. Is there like a systematic way of doing that, or is it just broadly, "Let's add buffer time"? Is there like a rule of thumb you think about there?
Upasna Gautam (09:02):
It depends on the scope of the work we're doing at that time. So one of my main responsibilities is to rebuild our content management system, which also involves onboarding our editors and journalists to it off of our legacy platform and onto our new one. So when we're thinking about onboarding especially the teams, our onboarding cycle's very long. It involves training, testing, lots of dialogue and feedback. And then only do we actually test, and then we onboard. And so it is a long cycle, and it's longer than it maybe seems like it needs to be because we have to build in those buffers. Sometimes that buffer is a day or two, and sometimes it's a week or a month. And sometimes when we think we need a buffer, we get it done in a day and we quickly move onto the next phase.
(09:53):
And so I think that quick decision-making in those times is super-important, because you have to be able to assess the situation as it stands. And so I think mindfulness is so important too in practices like this, because being able to objectively see the scenario for what it is, make a quick decision and move on to the next phase is something we have to analyze every single day.
Lenny (10:16):
Makes me think a little bit about a lot of CEOs are very busy and pulled into a lot of things, and so you have to kind of account for their schedule. And it sounds like you have many, many people that you work with that have crazy schedules.
Upasna Gautam (10:29):
Yes.
Lenny (10:30):
I wanted to dig a little bit deeper into how you, your team works with the news team. It's such a unique way of working, most product teams don't have a whole set of journalists that they have to work with as stakeholders. So I'm curious specifically, say a journalist has like, "Hey, I'd love to build a special immersive experience for this story," or, "I need some special feature to help support this work that I'm doing." How does that work? Do they come to you, and, "Okay, here's a roadmap [inaudible 00:10:57] maybe in the quarter [inaudible 00:10:59]." Imagine it's like, "I need this next week." How do you work with the journalist team, basically, on product?
Upasna Gautam (11:04):
Yep. This is pretty much the foundation of all of my work. We talk to our editorial staff every single day, and after a lot of observation and learning I implemented a system to manage that kind of intake with four different touch points or events. So we have weekly demo days, working sessions, breaking news dress rehearsals, and office hours. So with weekly demo days, I facilitate those with my product design lead and my tech lead. And we use that as an open form of communication to deep dive into features that exist on our platform, also to preview or give a sneak peek of new features to come, and kind of recreate their workflows and do a show and tell. Again, we wanted to open that up as a forum to not just our editorial partners but also anyone across the business who is interested in learning about the product and which is our platform.
(12:00):
And it was also a great way to kind of evangelize the product too. Coming off of a legacy system after several years onto a brand-new one is a big change at a place like CNN, and so we definitely tried to make sure that smart repetition in different ways is top priority. So, weekly demo days is one. Working sessions are interesting. I use the term working session because it's a combination of several things. This is a really critical part of our onboarding process where we gather breakout groups of our journalists and editors to work with us to recreate their workflows in the new platform. This allows us to address any friction or issues of course that are occurring in their workflows. But also we're able to gather a lot of awesome feedback from them in those sessions.
(12:54):
We used to call them user testing sessions, but decided to move away from that and just call them working sessions so they're more collaborative. And again, it's a really critical part of our onboarding process. We usually do three to six of them depending on the size of the group before the team is actually onboarded for two hours per session. So they're like deep dives into their specific workflows, so as you can imagine the way the politics team programs content is wildly different than the way the entertainment team does, or the way that the health team does, and very different than the way that the CNN homepage even interacts. So all of those are separate teams we have to work with when it comes to getting feedback. So in addition to that, we also do I mentioned breaking news dress rehearsals.
(13:44):
And you can imagine this is exactly what it sounds like. We create a script and do a simulation of a breaking news scenario to stress test our platform, because all breaking news scenarios are definitely not the same either. So this gives us a lot of great feedback in that short amount of time at the speed of breaking news. And then last but not least, we have office hours which I just started last year, and that's also probably what you can imagine, open blocks of time where me and my product design partner and my tech lead are just there to answer questions, help people troubleshoot any friction they might be experiencing in their workflow, get their feedback. We just wanted to open up another line of communications, so we do those right now once a week. Sometimes they go up to two times a week if we're in a really vigorous onboarding phase.
(14:33):
After those conversations and sessions and events happen, you know it's our job to translate their needs into the functions that we, A, either maybe already have that we can optimize, B, we build anew, or we tell them it's not viable. And the good thing is that because they've been along for the ride with us throughout the product discovery process we've earned their trust and respect. So that when we tell them something like it's not viable, they usually get it.
Lenny (15:07):
Man, I have so much questions about just working with journalists. I feel like pushing back on a journalist is probably extra hard versus other types of stakeholders.
Upasna Gautam (15:14):
It is.
Lenny (15:15):
Can we zoom out a little bit, and you talked about what you work on at CNN, which is the content management system and things around that. Can you just talk about whatever you can share, just like what does the product team look like at CNN, how many PMs are there, how's like the product work structured and where do you fit in there?
Upasna Gautam (15:31):
Yes. I mentioned earlier my team sits on CNN Digital, and I think when most people think of CNN of course you think of TV and linear programming. I have nothing to do with that, CNN Digital is digital, and it's made up of several teams that are structured around a lot of different product areas. It includes everything from the content management platforms that I work on, to data infrastructure, to personalization, to video experience, which includes like the products of video editor, and the video player, to podcasts, there's a lot. So each of those are product teams. And so we also split out... The way CNN is split out into CNN Digital is because there's a separate core content platform that powers broadcast and linear TV.
(16:21):
And the one that I work on powers CNN Digital. So on my team, the core platform team, our stakeholders and our customers, like I mentioned, are journalists and are editors. Which presents a really unique dynamic, and it's one that I love. We have direct access to our customers at all times of day, for better or for worse, and they're embedded into our product development process. And each of those teams under CNN Digital is kind of like a squad, very similar to how it is at other larger tech companies. We have PMs, we have engineers, designers, and delivery managers embedded in those squads. And since my team is a core platform team, our main responsibility is to A, build our newer, faster, more flexible content management platform to replace our legacy one, and B, onboard our entire editorial staff to it.
(17:19):
And so even more specifically my role is focused on rebuilding the tooling and the editorial experience of that platform, as well as doing the actual onboarding of our journalists. So we work cross-functionally because our team kind of is the umbrella over a lot of different teams, so we truly work cross-functionally to make sure that we're serving our journalists with the tools that they need to do their job in the most efficient way possible.
Lenny (17:48):
What would surprise people most about how product is built at CNN?
Upasna Gautam (17:54):
I think the most surprising thing may actually be that there's just so many different types of products that we build. Like I said, I think when most people think of CNN you see TV, and you think of Anderson Cooper, and all of the things that are very publicly visible. Most of our product work and product teams all sit behind the scenes, and so I think just that in itself, like the sheer size of that is surprising to a lot of people. So I mentioned like all of the different teams, product teams that are based off of function, content management platforms, infrastructure, personalization, video, podcasts, linear TV. And I think that in itself, like the sheer size of it, we're not the size of Google by any means. But at the same time we have the expertise and the depth and breadth of a lot of those larger tech companies.
Lenny (18:52):
I'm curious about the day-to-day operational work of how you build product at CNN. So our first question here is just, you use like OKRs, and OKRs with like key objectives, and outcomes, and 70% of a goal is success.
Upasna Gautam (19:06):
Yeah, absolutely, we do. We've used OKRs for a long time, and they've served as an anchor for my team over the last three years. I can't go into specifics on like what our OKRs are, but I did kind of cover the two main parts of it, which is rebuilding our content management platform and onboarding our users to it. So again, it's a long game at CNN when you're working on a core platform to replace a legacy one. And so we break those OKRs down of course even further into, we look two to three years out and build goals based off of that. Then we break them down by quarter and month, and then out of that for my team and what I do I need to, for my own sake and my team's sake, break those down by the week. And when we're in rapid development phases, we're planning on a daily basis.
Lenny (20:01):
How about in terms of just planning broadly? How far out does the product team at CNN plan in detail, like have an actual roadmap? And is that standardized across teams, or can each team kind of do their own approach?
Upasna Gautam (20:13):
It's a combination of both. So we have one that is an over-arching roadmap that tracks to like our company OKRs and our product organization OKRs. And then from there I mentioned we have our squads, product teams, and we have OKRs on those as well track up to the larger, broader ones. And so once we get down to that level though, there is flexibility and we have autonomy to tackle those how we want. Which is really great, because the scope of work across our different product teams is drastically different. Working on core platform, like I do, versus working on video experience, versus podcasts. I mean, it's apples and oranges. And so it's really awesome that we have the flexibility to kind of make it work for us, while also having these larger goals that we know that, "Okay, this is what we need to work towards."
(21:12):
And I mean, like the saying we always hear in product, of, "Stay firm on the goal, but flexible on the process." And we've definitely been able to use that and leverage that in the way that we track against our goals.
Lenny (21:27):
Something else that a lot of people are always curious about is product review meetings and design review meetings. You talked about a couple of these meetings that you have, but do you have standard product review meetings where folks get together and just review stuff and progress? And if so, how do they work? Like who runs them, who comes to them, how do you make decisions, things like that?
Upasna Gautam (21:46):
We have multiple variations of those. Some are standing ceremonies of course, and some are ad-hoc. Again, it's really based on the work we're doing in whatever phase we're in. But when it comes to product review, and product discovery or design review meetings, in addition to my design lead I've made it a point to bring in my tech lead and engineers along for this product discovery ride, and that's definitely been a game-changer as well. When our engineers are able to understand our journalists' needs at the same level as we are, they're able to define the how to do it with so much greater clarity and precision. And so my tech lead is embedded also in our product discovery process, he joins our user testing sessions, and our design jams, and our editorial conversation planning sessions.
(22:37):
And it's helped him and the rest of our tech and engineering team become experts on the why are we doing this and what are we working towards, to better determine technical feasibility. And he's done an amazing job of also passing that knowledge down to the rest of our engineers on our team, so it's really like this mentality of getting that important feedback from our journalists, understanding their pain points and then sharing and teaching it across the team. And I think the key takeaway on that is it's so important to think of your engineers as partners and not just resources. And when they are embedded into the process right upfront, it makes the whole process in general more efficient.
Lenny (23:21):
So it sounds like that was maybe an evolution of the way the team works, as engineering has been looped into a lot of this early stuff more recently?
Upasna Gautam (23:30):
Totally, yeah. Recently-
Lenny (23:33):
Cool.
Upasna Gautam (23:33):
... meaning, I mean... Again, long game right? Because it's been a couple of years.
Lenny (23:39):
Got it. Going in a slightly different direction, I'm curious if there's any fun or unique traditions or rituals that the CNN product team has. These are always fun to hear about.
Upasna Gautam (23:51):
I'll be very honest, we are not one of the cool teams. The politics team and the breaking news teams have all these cool rituals and fun things that they do.
Lenny (24:02):
What kind of stuff do they do?
Upasna Gautam (24:03):
It's different also because they're usually in-person in the newsroom and I work remotely, and so... And actually most of my team works remotely. And so they have their rituals, but I will say one of the things that we started to do is... So onboarding teams has been a big goal of ours, and that we've slowly checked off the list over 2022. And any time we successfully onboard a team or launch a new feature, it's not anything crazy or fun, like there's only so much you can do when you work remotely. But we definitely make it a point to celebrate, and it's been hard to figure out ways to keep team morale up when you're all-remote. And it started with... We knew we needed to start doing something when we would have a big launch, and it was so anticlimactic.
(24:51):
And we literally hit publish and onboard onto like a politics page, and we were like, "Oh, okay, so I guess that's it." So one thing we started doing is sending like these gift boxes of like random tchotchkes and stuff that mean things to us from the whole year, and it's like just cheap little gag gifts and stuff that we send to each other. I have random stuff all over my desk, I don't even know if I can share some of it. So we try to make it a point to at least share and celebrate, and then when we're in-person we do too. But again, being remote, there's definitely a challenge there.
Lenny (25:32):
Are you ever able to get like a cameo from an Anderson Cooper, or someone else on-air to thank the teams? That feels like a cool feature potentially.
Upasna Gautam (25:41):
So one of my key stakeholders, she leads the video team at CNN, and she is a... We've had some discussions about doing a sizzler reel for our content management platform, since we're onboarding people and building new features. And there have been discussions with her about getting a celebrity to come and promote the product for us, so working on it.
Lenny (26:07):
Yeah, it feels like a missed opportunity, you've got so much talent around.
Upasna Gautam (26:11):
Totally.
Lenny (26:12):
This episode is brought to you by Vanta, helping you streamline your security compliance to accelerate growth. If your business stores any data in the cloud, then you've likely been asked or you're going to be asked about your SOC 2 compliance. SOC 2 is a way to prove your company's taking proper security measures to protect customer data, and builds trust with customers and partners, especially those with serious security requirements. Also if you want to sell to the enterprise, proving security is essential. SOC 2 can either open the door for bigger and better deals, or it can put your business on hold. If you don't have a SOC 2, there's a good chance you won't even get a seat at the table.
(26:52):
But getting a SOC to your port can be a huge burden, especially for startups. It's time-consuming, tedious, and expensive. Enter, Vanta. Over 3,000 fast-growing companies use Vanta to automate up to 90% of the work involved with SOC 2. Vanta can get you ready for security audits in weeks instead of months, less than a third of the time that it usually takes. For a limited time, Lenny's Podcast listeners get $1,000 off Vanta. Just go to Vanta.com/lenny, that's V-A-N-T-A.com/lenny to learn more and to claim your discount. Get started today. Coming back a little bit to the way y'all built product, I'm curious how you balance new product work and new features versus maintenance and bugs. Do you have kind of a... Is there like a philosophy at CNN of how much goes to bugs, maintenance versus new stuff, or is it per team and just, how do y'all think about that?
Upasna Gautam (27:45):
It's certainly team-specific, because again, the scope of work across teams really varies. But since my team's product is an entire platform, it's my job to ensure we're still clear on our goals because like I said, they may change on a week-by-week basis. One sprint might be high-priority feature development, in another sprint maybe we're focused on medium-priority optimizations and bug fixes. But we know that any time there's a critical incident in production, it also takes critical priority over everything else. So it's a balancing and juggling act that relies heavily on intuitive decision-making. But I will say we're also really fortunate to have a global, 24/7 editorial support team that we work really closely with.
(28:35):
So they are the ones who handle, troubleshoot, escalate incidents up to the relevant teams. There are a lot of layers to that protocol when a critical incident occurs. And so our editorial support team is that first layer of support, whereas my team might be the second or third depending on the level of severity and who it gets escalated to. So there's definitely a lot of processes in place, we're not always that first line of defense, which is actually... It alleviates a lot of stress, to know that we have an entire team around the clock globally dedicated just to that.
Lenny (29:12):
When you're talking about these incidents and moments it makes me wonder, is there a memory of just like a wild time of something happened in the news, or just like, "Oh man, we've got to get on top of this thing"? Is there like a memory that you think of like, "Wow, that was crazy"?
Upasna Gautam (29:26):
It's funny but also crazy and amazing, is... So our new content management platform, we've been building it for a while and stress testing it for a while. And politics and election season at CNN is Superbowl like times a hundred. And so we have to be all hands on deck, like all layers of support intact. And so we have also a lot of layers of fallback in case something happened, right? Like there's layers and layers of infrastructure fallback if CNN.com goes down, or another service goes down. And so it actually did happen a couple of years ago in the 2020 election, and one of the fallbacks at that time, because we were not...
(30:14):
We're still on our current content management platform, but we had our new one as we're building it as one of the levels of fall. And if X, Y, Z fails, then it goes to our current platform, and it did. And so that's actually happened, where our new platform saved the day even though it wasn't fully ready. But that just goes to show we think about that kind of stuff like in granular detail, when we think about everything that could possibly go wrong. Because it has happened, and it will happen, and it does go wrong. So that was kind of cool, it was validation to know that the platform we have is really stable, and strong, and secure, that it was a fallback for the election.
Lenny (31:03):
Okay, and it must have felt good, it feels like a promotion material right there that your work-in-progress system saved the day.
Upasna Gautam (31:10):
Yeah, I agree.
Lenny (31:12):
You talked about how you have like these breaking news dress rehearsals. I just noted that, and I thought it would be cool to just revisit that briefly. Like, how does that work? You just get the team together, and like, "Here's a news story that just broke. What do we do?" Like, how does that work?
Upasna Gautam (31:27):
It is scripted, right. So we can only get so close to the real thing. But one thing we do is we script everything, like the teams and the players that we need involved in it, what the incident is. And it usually starts when breaking news occurs with an email, the news-gathering team sends an email to our writers and our producers. And then from there it goes out all the places it needs to go. There's a video that needs to be created, there's an article that needs to be written. Again, the TV side I have no insight into, it's like a foreign land to me. But as far as the digital scope goes, there's a lot of work that has to be done. Even things like photo and imagery, we have a whole team dedicated just to selecting photos.
(32:11):
The photo desk is very involved with that process. And so that is all scripted out, and so we say, "Okay, here's the news, here's how it's going to break," and then we run it. And so we use interpersonal communication tools at work of course, email, and we run the whole thing from the minute the email is sent to... And of course since we're testing the platform with this breaking news dress rehearsal, to the minute you hit publish on that page. And there's a lot of stuff that goes on in there, and it all happens in the span of minutes. And so while that is happening, while that dress rehearsal is happening, we have our engineers and our editorial support team on hand as well. So they're observing what's happening while it's usually me and one of our editorial stakeholders and leads facilitating the actual rehearsal part.
(33:02):
And you know, getting user feedback on, "Okay, did something break, did everything work as it was supposed to work?" And also allows us to understand like how far we can go with stress testing different features on our system. So each one is different, but it's a crazy amount of stuff and information you can gather in such a short span of time. Because if it cannot serve the needs of breaking news, then it's useless. So it's a lot of work that goes into it for this three-minute event.
Lenny (33:35):
That is cool. It feels like just a cool tactic you could use anywhere, and that's a good segue to the next question I had, is just having built product at CNN and seeing how the product team works, what is it that you think you'll take with you to future product teams and future companies if you ever move on to anything else?
Upasna Gautam (33:53):
So I of course can't speak for the entire scene and product team, but I can speak for myself and my specific team. In order to stay competitive in our modern news landscape, building this content management platform and the technology behind it has taught us how to enable rapid development and integration of new features and workflows. And we've been able to quickly test hypotheses while reducing risk, and again, time is of the essence when it comes to breaking news. And when you layer that with a very complex content management technology, there's a lot of moving parts. And we've been able to do that successfully, and it's pretty amazing. And because of that we've developed, I think, this unique skill of high agency under high pressure.
(34:49):
And I really think that that skill or combination of skills is our superpower, and that is something you can take anywhere, that is something that is an asset to any product development team.
Lenny (35:03):
Let's circle back to our original topic about mindfulness and meditation. Other than just living through it and either becoming a meditation expert or having worked at a company like CNN that has a lot of this, is there any, I don't know, tactic you could share, something that someone could take tomorrow and be like, "Okay, I'm going to get better at dealing with crazy, unexpected events," based on the experience you've had?
Upasna Gautam (35:25):
Two parts to this. So one, I would be remiss as a meditation educator if I didn't say that there is no substitution for meditation. So just do it, it takes a long time, and it's a lifelong work-in-progress. But the good thing is that it also... Like the more you do it and consistently you do it, it compounds over time. Okay, if you think of any job description for a product manager it's mostly the same core stuff. You need to be able to lead a team without having authority, you need to have great communication skills, you need to be able to bribe in ambiguity, you need to be able to work with a lot of different people on the technical side and business side, all of the stuff that we hear all the time right?
[NEW_PARAGRAPH]But how do you actually become better at those things? Like, there's only so much you can gain from reading a book. To me it's either A, you've got to go do it, and B, meditation has helped so much because of the clarity of mind and clarity of thinking you're able to cultivate because of it, especially when it comes to communication. And this comes back to another tactic I think. So meditation is one, you can't get around it. It's a very, very powerful tool, I will die on that hill. But thinking about workplace tactics, communication is so essential. When I started at CNN it was a very new chapter for me, it's my first official product management role after working a decade in tech, in data and search infrastructure.
(36:57):
And it was really scary to make that change so far into my career. But when I asked my boss why he took such a big chance on me he said, "It's because of your communication skills and relationship-building skills, and that I've seen you in a room where engineers listen to you and what you have to say, and you listen to them." And he was like, "That in itself is really, really hard to teach." And I was like, "Okay, yeah, I can do that." So when I think about what communication means I also attach that to mindfulness. Like mindful communication is so critical for successful product management, no matter what type of product environment you're in. And it means being like deeply aware of the conversation you're having.
(37:43):
And when I'm having this conversation with you, I'm only having this conversation with you. When I'm talking to my design lead, I'm only talking to my design lead. When one of my journalists is venting because this feature is not working the way we told them it was going to, I am shutting my mouth and I'm listening to them vent, and then I'm extracting what the root cause of the problem is. And I think the takeaway and the tactic is that goes back to exactly what we talked about in the beginning is the ability to pause before reacting is the key to mindful communication and being a successful product manager. I think a lot of times we are taught to have all the answers, or we're expected to have all of the answers.
(38:27):
And people assume we have all of the answers so it's a really frustrating, sometimes, place to be in. But, if you listen and you know where to go to get the answers, that in itself is like a tremendous place to be. So I think the power of meditation, being able to pause before reacting lets you do things like conversate in the language of the listener. So when I'm talking to my journalists I'm not using technical terms or like content management technology terms. They have a whole different vocabulary that they use, they have shortcuts that they have lingo for in our content management system. They call things nicknames, and so you have to speak many different languages as a product manager. And if there's one thing that learning and teaching mindfulness has strengthened, it is that communication, yes, it's very important.
(39:24):
How do you become an effective communicator? I think a lot of times we think of speaking articulately first and foremost, or we think about writing well, which those two are really, really important things. But those can't be effective for us as product leaders if we're not listening, so I think listening and being able to converse in the language of the listener is the utmost importance. And how do you do that in your day-to-day? It's like, okay, if you're having a conversation with your customer are you actually listening to what they say, or are you going in with your own assumptions? Because maybe you're a user of the product. And it was very interesting, because I actually started writing freelance for CNN this past year.
(40:12):
And I was like, "Oh, okay, I'm a user now." And no I'm not, I'm not going to say that it helped me understand their pain points so much more and where they're coming from in a whole different light. But again, I am merely a proxy, I'm not actually the user. What they do is still drastically different. And so when having those customer interactions and stakeholder interactions, the priority should be to listen. And I think that is one of the most important things I've learned, and it's also helped build trust and respect between a previously fragmented structure where product and editorial didn't talk to each other, and now we're a unified partnership.
Lenny (41:00):
Oh, I love that. I love the reminder that a lot of communication is incredibly important for product managers, and so much of it is not actually you talking, it's you being really good at listening, and that makes you a better communicator. I imagine some people listening to this are going to be like, "Yeah, meditation, I should be doing that." What's like one thing someone could do to move forward on the path to starting to meditate? Is there a resource to recommend, a tip of just starting to do something there?
Upasna Gautam (41:27):
Totally. I think when people think of meditation, you immediately think of sitting on a mediation cushion like a monk for an hour. And that doesn't have to be true, especially if you're just starting. And there's also of course social media has commercialized what meditation is a lot as well. But at its core, all it is is being deeply aware of the present moment. So I always tell people who are for example like really busy moms who have no time in the morning for an hour-long meditation is, "Okay, take something in your day that you do every single day. You brush your teeth every morning, right? Okay, take brushing your teeth. Can you brush your teeth and just brush your teeth? And when you're brushing your teeth you are engaging all of your senses, and being fully present and aware of how it feels, how it smells, how it sounds."
(42:27):
That's two, three minutes of your day. That's meditation, and I think it's an amazing way and an easy way... Oh, sorry, not easy. Simple, not easy way, always, to think about what meditation actually is. Is like, instead of like having to uproot your whole life and the way you live to bring meditation in, think about what you already do every day and how you can just be more present, like fully present. And that's one of the core examples I give, is start with brushing your teeth and just brush your teeth. There's an old app I've been using for a long time if you're into that, I stopped using it recently but it's still amazing. It's called Insight Timer, the free version is amazing. It started as like a single-frame app probably about 10 years ago, and it's turned into this...
(43:18):
They've done amazing things with that product. So that's what I recommend, but again, you don't... I think, again, when people have a vision of meditation in their mind they're like, "Well I need these tools, and I need these resources, and I need these things, and I need knowledge." You don't need anything, you need five minutes and yourself, and that's it.
Lenny (43:37):
Amazing. I imagine many people listening to this coming into thinking, "I'm going to learn about CNN and how they build product," and then get a free meditation lesson. What a bonus, that was awesome. I'm going to be brushing my teeth very mindfully today-
Upasna Gautam (43:49):
Love it.
Lenny (43:49):
... my takeaway.
Upasna Gautam (43:50):
Love it.
Lenny (43:52):
Final question, around something that I know is important to you, that is basically there's this growing shift of product thinking in the news industry at large. And I know that's something that you're passionate about and something you're trying to create, is just to kind of move the media industry and the news industry toward more product thinking. So I'd love for you to just talk about what you're doing there, what's happening there, and then maybe if there's anything people could do to help in that effort.
Upasna Gautam (44:16):
Compared to the rest of product management as a discipline and the tech industry, product management in news is still in its, I will say infancy. And that's just because it hasn't been an integrated role for as long as it has been in big tech. But it is starting to become more and more not just prominent now, but people are realizing the value and power of it because especially in smaller newsrooms... I mean, CNN, places like The New York Times, The Washington Post, we have great, embedded, strong product teams. But that is not the case for the majority of newsrooms across the country and the world. Newsrooms are strapped for resources, they are strapped in all resources, including financial resources.
(45:07):
And so first, bringing in product and tech talent is expensive, and that in itself has forced editorial staff and journalists to take on other jobs that they never signed up for. And so they've had to learn how to do things product management, and engineering, and coding hacks, because there was nobody else to do it. And so it's interesting because a lot of times when you talk to editors and journalists, they're doing so many other things other than just their reporting of the news, right? They've had to take on other roles because of those restraints in the newsroom. And so there was a group established and a community established during the pandemic called the News Product Alliance. And there was like a realization occurring all at the same time that, "Wow, there's a lot of us doing this work.
[NEW_PARAGRAPH]"Like, what do we call it? Is this product management?" And it was, it's product management at so many different levels. And so the News Product Alliance was formed during the pandemic in 2020 I believe by several media and news executives, who had been there and have seen people in their newsrooms do that. And the goal of it is to increase the awareness and education of product thinking and product management in newsrooms, while also increasing the diversity of thought and the diversity of people in those positions as well. And making the resources more readily available, especially for those smaller newsrooms that don't have the money to hire tech talent. And that in itself has...
(46:56):
So that group, the News Product Alliance, has grown dramatically in the past three years since I've been a part of it, since the beginning. And we regularly produce the resources that are catered... Product management resources that are catered to working in a newsroom, because it is different, it is very unique. But there are of course frameworks and processes that are still relevant, right? Like editors who have been cobbling together how to make this thing that they want, but hey, maybe this PRD framework will help you, just to keep it on track. So these very simple, like rudimentary types of things have helped them so much. And so last year we kicked off a mentorship network in which we had about 400 people apply.
(47:46):
We accepted 150 mentees from across the world, and matched them with 50 mentors from different newsrooms across the world in leadership positions. And each mentee defined a goal that they wanted to work on, and all of course having to do with product management. And some of them were creating a product management role for themselves in the newsroom. Some of it was creating a product management practice, maybe they were given the title of product manager and said, "Okay, you can hire a couple of people." But it was all on them, and they had no idea what to do, right? And so some of it, it's across the board, and it's amazing to see people doing this from scratch who never in a million years thought they'd walk into it.
(48:32):
You know, they're not coming from big tech, they don't have startup backgrounds. They had journalism degrees from around the world, and they're learning how to do product, and build... Not just learning how to do it, they're building product practices, they're actually building and developing products and features, and they're creating more leaders in this space as well, and across their newsrooms to empower each other. So it's been really amazing to see, and it's the most valuable professional organization I've been a part of just because it is so niche that talking about product management is always fun. But when you talk about it at a level that specific, it becomes even more valuable.
Lenny (49:16):
That is some really impactful product work. Where can people find that if they want to maybe participate, maybe apply if you're doing another cohort in the future?
Upasna Gautam (49:24):
Go to Newsproduct.org, there is a very active Slack group with a couple thousand people in it, a very active and popular job board as well. And you just have to submit an application on the website... A form, sorry, on the website to join the Slack, and ten you'll get an invitation to join the Slack. And then you'll have all of the resources at your fingertips, it's very low barrier to entry, and we want everyone and everyone who is interested in the intersection of news and product to be a part of it. And the cool thing about it is like I mentioned, it's a global network. We have people from the biggest newsrooms across the world, to all of the regional ones, to even big tech, one of my fellow board members was doing news at Twitter.
(50:10):
One was working on the Google News Initiative. So it's a really, really awesome group of people, and everyone is so hungry and passionate about sharing and paying it forward.
Lenny (50:23):
We'll put a link to this in the show notes. One last question, and what kind of people are you looking for? Who should apply, if they're listening?
Upasna Gautam (50:29):
If you are interested in working in news and have a product background, or the inverse of that, if you work in news and you're interested in breaking into product. So either side of the coin or any combination of that, news media, product technology, even... We have a lot of audience development, and analytics, and data science folks in there too. It's just an amazing community for knowledge sharing in tech and news, so there will be a fit for you somewhere, or to learn something, or at the very least to meet other really amazing people.
Lenny (51:07):
Well, with that we've reached our very exciting lightning round. I've got five questions for you, and are you ready?
Upasna Gautam (51:14):
I'm ready.
Lenny (51:16):
All right. What are two or three books that you recommend most to other people, or that you've recommended most?
Upasna Gautam (51:21):
One, Mindfulness in Plain English. Two, How To Win Friends and Influence People. I have to attribute a lot of my communication skills to my dad forcing me to read that book when I was like 10 years old, and-
Lenny (51:36):
Wow, 10 years old. Intense.
Upasna Gautam (51:39):
He was an engineer, and they were in their very beginning phases of introducing... Well, at that time there was no product, but product-type stuff into his engineering practice. And so he had to read the book and was like, "You need to read this book." So I never forgot about it. And then the third one is actually, it's not a book, but it's an article that I think is still very powerful and relevant to this day. It's The New Product Development Game, published by Harvard Business Review in 1986. And it looks at a really different approach, one that I resonate a lot with because it's a lot along the lines of how we work at CNN, around rapid development, and time and flexibility being like key anchors of successful product development. So, I threw that in there as well.
Lenny (52:29):
Favorite recent movie or TV show? And it can't be White Lotus.
Upasna Gautam (52:32):
Okay, I haven't even seen that show.
Lenny (52:34):
Okay, great. That's come up so many times, we've got to not allow it anymore.
Upasna Gautam (52:38):
TV show is a toss up between The Mandalorian and Ted Lasso. I know it's not very new, but I don't watch tons and tons of TV, and I usually find like the few that I latch onto, and then I get obsessed with, and then I've got to take a break for a while. So, those are my last two obsessions. Movie is Everything Everywhere All At Once, the last amazing one that really, really struck a chord with me.
Lenny (53:02):
If you like Mandalorian check out Andor, it's incredible.
Upasna Gautam (53:05):
Oh yeah, it's good too.
Lenny (53:06):
It's like the best Star Wars thing. Okay, you've seen it. Okay, great, you're on it.
Upasna Gautam (53:09):
I still love Mandalorian more, I do like that one too.
Lenny (53:11):
Wow.
Upasna Gautam (53:12):
My husband is obsessed.
Lenny (53:15):
Okay, okay. Wow, contrarian. Favorite interview question that you like to ask candidates?
Upasna Gautam (53:21):
What's something that would not exist without your initiative?
Lenny (53:28):
Mm-hmm. And what do you look for in an answer that's a sign that this is someone you may want to hire?
Upasna Gautam (53:31):
The whole point of the question is like, do you have and can you exhibit high agency? And especially again, working in news it's so important. And so there's not like a specific answer, I think the ability to actually define something specific and tangible in itself is a really, really, really good sign. I think a lot of people definitely get startled by that question sometimes, because it requires you to kind of have to know what it is that you put on the table, right? So yeah, it's different every single time. But if they can define something out of that question, it's usually a positive sign.
Lenny (54:15):
Cool, thanks for sharing that additional detail. Next question, what's something relatively minor you've changed in your product development process at CNN or on your team specifically that's had a tremendous impact on your ability to execute?
Upasna Gautam (54:29):
Bridging the gap between product and editorial, that mutual trust and respect has had an outsized impact on our success as a high-performing team.
Lenny (54:38):
Sadly not something other people can use, but that's cool to know. Then we'll have to hire some journalists now, I think, to take advantage of that learning.
Upasna Gautam (54:46):
I can add onto that to make it relevant for others-
Lenny (54:50):
Sure.
Upasna Gautam (54:50):
... which is, it just goes back to, there's no substitute for having those direct conversations with your customers and your users. And it's like, when you understand that the assumptions you make are not one to one, or ever going to be one to one with their actual feedback. And developing that line of communication with your users and your customers is of utmost importance, I think that in itself is the key takeaway. It's like, how do you bridge the gap between collecting that feedback, having those conversations. Like, how far are you from your users, how frequently are you having conversations, how consistently are you having conversations? And I always think the more frequently and the more consistently, and earlier on in the process that you're having those conversations, the better.
Lenny (55:44):
Final question, maybe you already answered this. What's the most crazy or most memorable story from working at CNN?
Upasna Gautam (55:51):
Every election season is absolutely crazy in the best way possible. It's incredible to see our democracy in action, and watch history unfold. And while that's happening, using the platform you had a direct hand in building, and it's never lost on me that my work impacts the world every single day. And on the crazy, frustrating, stressful days, that is what serves as my anchor.
Lenny (56:19):
Awesome. Plus, this was amazing, I learned how to brush my teeth more mindfully, about elections, downtime, Trump, all these things. Final two questions, where can folks find you online if they want to reach out and learn more, and how can listeners be useful to you?
Upasna Gautam (56:34):
It's very easy to find me. Online I'm pretty active on Twitter and Instagram. I recently became an amateur content creator, so I share lots of stuff here and there on social. So any social platform... Well not any, only on Twitter, LinkedIn and Instagram. So any of those three is good, and I always love to hear feedback on stuff that resonated and made sense, and the stuff that there are further questions on. Always love having conversations around that. So yeah, DMs are always open.
Lenny (57:10):
I know we'll link to this in the show notes, but just, what's your handle on these networks?
Upasna Gautam (57:12):
It's my first and last name, very creative. I thought about it all by myself.
Lenny (57:16):
Awesome. And then I don't know if you answered the second question, how can listeners be useful to you?
Upasna Gautam (57:21):
It's the feedback, right? Like I love to hear what you found valuable, what helped you, what's a tactic that you took away and employed that helped you, things that made sense, things that didn't make sense, what you'd like to hear more about, any specific topic that would be valuable to do a deeper dive on. All of those things are very valuable to me.
Lenny (57:42):
Amazing. Again, thank you for being here, and adios.
Upasna Gautam (57:46):
Thank you.
Lenny (57:49):
Thank you so much for listening. If you found this valuable you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at Lennyspodcast.com. See you in the next episode.
