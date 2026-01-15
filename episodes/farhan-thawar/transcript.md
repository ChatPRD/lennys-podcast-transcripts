---
guest: Farhan Thawar
title: How Shopify builds a high-intensity culture | Farhan Thawar (VP and Head of
  Eng)
youtube_url: https://www.youtube.com/watch?v=C_lhMOjG7PE
video_id: C_lhMOjG7PE
description: 'Farhan Thawar is the head of engineering at Shopify, where he oversees
  more than 1,000 engineers and a platform that powers over 10% of all U.S. e-commerce.
  Before Shopify, he was VP of engineering...

  '
duration_seconds: 6003.0
duration: '1:40:03'
view_count: 23570
channel: Lenny's Podcast
keywords:
- metrics
- roadmap
- iteration
- conversion
- hiring
- culture
- leadership
- management
- strategy
- vision
- mission
- market
- persona
- design
- ux
---

# How Shopify builds a high-intensity culture | Farhan Thawar (VP and Head of Eng)

## Transcript

Farhan Thawar (00:00:00):
If you do the hard path and it doesn't work, actually you still win because you've now done something hard. You've probably worked with smart people. You've learned something along the way that is valuable. I meet lots of job seekers. I go, what are you doing to try to find a job? Are you really learning anything from sending out 10 resumes a day? Why don't you look at the API Docs and build something? Even if you don't get a job at Shopify, you've learned something.

Lenny Rachitsky (00:00:20):
First, I want to talk about another theme, creating intensity in your organization.

Farhan Thawar (00:00:24):
Everyone says, "Oh yeah, work hard and do more hours when you're young, whatever." I'm like, "What if you just did more per minute?"

Lenny Rachitsky (00:00:29):
The more I dig into the Shopify way working, the more fun stuff I never expected emerges. There's been a drive to delete code and simplify.

Farhan Thawar (00:00:37):
We have a Delete Code Club. We can always almost find a million-plus lines of code to delete, which is insane.

Lenny Rachitsky (00:00:42):
I found this great quote from you, "Not everyone can look stupid in public over and over, but I believe it's my superpower."

Farhan Thawar (00:00:48):
I have been in many situations with many sharp people who have said to me, that's the stupidest fucking question I've ever heard. My goal there is not to annoy the person, but it's to understand the content.

Lenny Rachitsky (00:00:59):
I was looking at your LinkedIn and your career history, and I noticed that you've worked for a different billionaire every decade of your life.

Farhan Thawar (00:01:05):
They're mostly different people, but they're similar in one thing is that they haven't...

Lenny Rachitsky (00:01:12):
Today my guest is Farhan Thawar. Farhan is Vice President and Head of Engineering at Shopify. Shopify is an incredibly interesting company because they have over 10,000 employees who are fully remote, and even though they were founded almost 20 years ago, they continue to operate with urgency, velocity and have very first principles, ways of thinking, which translates into them seeing record usage, blowing away their earnings calls just recently, and building a beloved product. A lot of this is thanks to Farhan, who in our conversation shares very specifically what he's done to maintain intensity and urgency within the engineering team. Including their meeting cadences, the counter-intuitive power of pair programming, how they run meetings, how they cancel meetings constantly and so much more. He also shares his experience with indexing towards choosing the harder option when you have multiple options to choose from and why that ends up making your life easier.

(00:02:08):
He also shares a bunch of great hiring advice and a bunch of hiring stories which are going to blow your mind. He also talks about their engineering intern program where they're going to hire over a thousand engineers just for their intern program in 2025. I've had a lot of people on this podcast from Shopify, but that is for a very good reason because this company and its leaders have a lot to teach us about how to run an incredible business and build an incredible product. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing future episodes and it helps the podcast tremendously. With that, I bring you, Farhan Thawar. Farhan, thank you so much for being here, and welcome to the podcast.

Farhan Thawar (00:02:51):
Thanks for having me.

Lenny Rachitsky (00:02:52):
As I was preparing for our conversation, I talked to a bunch of people that you've worked with over the years, and there's basically three themes that kept coming up over and over and over. One is hiring, two is creating intensity in your organization, and three is choosing the hard path. First of all, does that resonate? Second of all, does it sound good to talk about these three themes in our time together?

Farhan Thawar (00:03:16):
Yeah, I mean, I have ideas on where all three of those things came from, and I think that it is something that if you looked back on my career, I've hit points on each of those things, but I don't think at the onset I knew that that's what I was doing, but it turns out in retrospect, that's what I ended up doing.

Lenny Rachitsky (00:03:32):
Perfect, so this is the Steve Jobs. Everything looking backwards it all connects.

Farhan Thawar (00:03:36):
Yes.

Lenny Rachitsky (00:03:37):
Today's episode is brought to you by DX. If you're an engineering leader or on a platform team, at some point your CEO will inevitably ask you for productivity metrics, but measuring engineering organizations is hard, and we can all agree that simple metrics like the number of PRs or commits doesn't tell the full story. That's where DX comes in. DX is an engineering intelligence solution designed by leading researchers, including those behind the DORA and SPACE frameworks. It combines quantitative data from developer tools with qualitative feedback from developers to give you a complete view of engineering productivity and the factors affecting it. Learn why some of the world's most iconic companies like Etsy, Dropbox, Twilio, Vercel, and Webflow rely on DX. Visit DX's website at getdx.com/Lenny. This episode is brought to you by Persona, the adaptable identity platform that helps businesses fight fraud, meet compliance requirements, and build trust.

(00:04:37):
While you're listening to this right now, how do you know that you're really listening to me, Lenny? These days it's easier than ever for fraudsters to steal PII, faces, and identities. That's where Persona comes in. Persona helps leading companies like LinkedIn, Etsy, and Twilio securely verify individuals and businesses across the world. What sets Persona apart is its configurability. Every company has different needs depending on its industry, use cases, risk tolerance, and user demographics. That's why Persona offers flexible building blocks that allow you to build tailored collection and verification flows that maximize conversion while minimizing risks. Plus Persona's orchestration tools, automate your identity process so that you can fight rapidly shifting fraud and meet new waves of regulation. Whether you're a startup or an enterprise business Persona has a plan for you. Learn more at withpersona.com'Lenny. Again, that's with P-E-R-S-O-N-A.com/Lenny. Okay, so let's start by talking about the hard path.

Farhan Thawar (00:05:42):
Okay.

Lenny Rachitsky (00:05:43):
Advice that I've heard you share with people often is when they're trying to decide amongst a bunch of options is to choose the harder path because that makes life easier down the road. Share this advice why it's so important, where you learned, where you developed that this is the right approach.

Farhan Thawar (00:05:59):
But the short version is that if you have a choice and you choose the easy thing and it works great. If you choose the hard thing and it works great, you did more work, but if it doesn't work and you chose the easy thing, you've actually not learned anything because you chose the... You haven't done a lot of work, you haven't probably worked with the smartest people because they're not usually around on the easy path, and what happens is you've gone through this exercise and now you're like, I've kind of lost. I lost the choice, or I was trying to do something, it didn't work out for me. But if you do the hard path and it doesn't work, actually you still win because you've now done something hard. You've probably worked with smart people, you've learned something along the way that is valuable, and I can give you a quick example.

(00:06:41):
So I meet lots of job seekers and they're like, I go, "What are you doing to try to find a job?" I'm like, "I'm sending out 10 resumes a day." I'm like, "Okay." That sounds kind of easy, and are you really learning anything from sending out 10 resumes a day? Versus I would say to them, "Hey, you know all these companies you're interested in, Shopify might be one of them. Why don't you look at the API Docs and build something, build a Shopify app, build an admin extension, build something on top of Shopify." Even if you don't get a job at Shopify, which is maybe your goal, you've learned something, you've built something, you have things in your GitHub repo now and you can show people. You're learning about the product that might translate to a job you might get somewhere else. So I think that even though it's harder, right? Of course, you can't every day build an app on a different platform.

(00:07:23):
Maybe you can once a day. You will learn something in the hard path. And the same thing happened to me in taking hard courses. I would get worse marks, but I ended up meeting smarter people in those courses because they were there for the same reason I was because the content was hard. And so that's something that I've just realized in my life that if I do the hard thing and I just naturally tend towards doing that, I ended up doing... I went to Waterloo and I did a minor in electrical engineering on top of computer science, and when I did my MBA, I did a minor in financial engineering because the smarter people were in that path and they're still my friends today.

Lenny Rachitsky (00:07:54):
So building on the last point you just made, people could hear this and think, okay, if it's harder, that's going to be the right path. Sometimes harder is still a bad idea. For example, joining a terrible company that's extremely frustrating to work at or building, I don't know, a house in a really dumb way, but it's just really hard. What else do you find is important to think about when you're thinking it's not just harder, but also XYZ should probably be true?

Farhan Thawar (00:08:20):
Yeah, one real one is of course the people, because I find that my path has always focused on trying to pick the best learning journey. Where can I learn the most? And for me, everyone's different. Some people might learn better from books or the domain they're in, but for me, I learn a lot from people, and so I try to put myself in those harder rooms on purpose. There was a time when I was doing my MBA in financial engineering, by the way, and I'm a tech guy and still a tech guy, and all these people were going into finance jobs.

(00:08:46):
There was a point where somebody said to me, "Why are you in this class?" Because they knew that I was doing it for fun, and so it was because it was the learning journey. And so I would say a big part of it for me is yes, there's the how do you win even if you lose, because if it goes poorly, you can still come out of it with skills, but if you actually take the hard path, you'll have these intense working relationships with smart people that again will continue on in your life.

(00:09:12):
And that also just forces you to be in this constant state of uncomfort by going into these rooms and saying, "I don't know anything," and it's harder. And I agree with you. You don't want to do dumb things like, oh, let's just do this thing in a dumb way. That's not what I mean. I mean, let's try to do the hard thing that we can learn from. And by the way, it happens to be on the path. It's just is it might take more manual work or it might not be the way most people do it, but we think we can learn more from that path.

Lenny Rachitsky (00:09:37):
Speaking of that, I found this great quote from you, "Not everyone can look stupid in public over and over, but I believe it's my superpower and I try to make it my whole team's superpower too."

Farhan Thawar (00:09:49):
Yeah, I mean, it sounds funny, but again, I'm the one who's always trying super dumb things and sometimes they work, and even my wife hates that I try these things even at home, right? I'll just like, what's an example? It might be a new washing machine and I might try some weird mode with some clothes, and I'm like, "Oh, you ruin the clothes." I'm like, okay. But now I know that this mode should not be used, but maybe I would've uncovered that there's some super fast, quick wash that I can do in 20 minutes that now saves us 40 minutes of wash time every single time we use the washing machine.

(00:10:22):
So there's things like that, but I will ruin lots of clothes trying to do that, but the same at work. We'll try things and sometimes it can lead to disaster, hopefully not, but you can imagine people trying to like, oh, let me try this new configuration of GCP and maybe we'll get some benefit, but maybe we'll take Shopify down. We don't want to do that. So you want to have some sort of guardrails. But there is something around trying dumb things and saying dumb things. Half the time, by the way, when I say something dumb, people go, "I had the same question." They just were scared to say it.

Lenny Rachitsky (00:10:55):
So for folks that may want to, because I feel like this skill is so hard, but so important, being okay with failing, being okay with looking dumb, is there something you tell people to help them build this other than just like, I'm genetically good at this stuff? What helped you become comfortable with being wrong and failing before you were a big shot exec where it's like, oh, he's fine. He knows what he's doing.

Farhan Thawar (00:11:17):
I don't know. I mean, I kind of grew up working in retail and people come into the store, and then I would say, "Hey," and you're working on commission, and they're not always buying stuff, and if they don't buy it, you don't make any money. And so maybe just the fact of going up and forcing myself to talk to people and then trying to get them to, and maybe you spend an hour with a client and then they don't buy anything, but you're getting that reaction of a bunch of negatives, and all you have to do is say, okay, and just go to the next customer. You can't really well on it and be like, oh my God, my whole day is ruined. But instead, you have to learn from that and say, "Okay, let me try this. Let me try that." And it's not easy, but it was a way to build up some confidence and people say, this telemarketing, or there's a bunch of things you can do to get a lot of rejection. Cold calling is another one, and that can lead you to actually building up resistance. I don't know if I'm genetically better at it or not. I just think that I literally don't care if I look dumb. I've always said the dumb thing, I'm not doing things on purpose to get nos, which by the way, is part of some sales training, which is go and get 10 nos. But I haven't done that. But I have been in many situations with many sharp people, business people, successful people who have said to me... Turn around and said, "That's the stupidest fucking question I've ever heard." I've definitely had that happen to me. And I'm like, "All right, let's move on to the next question."

Lenny Rachitsky (00:12:36):
I love that attitude and I think that's key to it. It's just bounce off of it and not be crumble and I think it's empowering for folks to hear from someone like you that has done so well that people tell you that is the dumbest question I've ever heard-

Farhan Thawar (00:12:48):
Oh yeah, still.

Lenny Rachitsky (00:12:48):
Still. Okay.

Farhan Thawar (00:12:50):
Yeah. So how about this? That I heard that's the dumbest fucking question. And then recently I heard, I've already explained this to you three times because I kept asking and I didn't understand, and literally I got this message back saying, "I've already explained this to you three times." I'm like, "Okay, I still don't get it." So my goal there is not to annoy the person, but it's to understand the content. And actually, by the way, I say these were messages, I saved them. I literally screenshot it because I'm like, remember this? It doesn't matter. I'm trying to learn.

Lenny Rachitsky (00:13:20):
One more question along these lines. I was looking at your LinkedIn and your career history, and I noticed that you worked for a different billionaire every decade of your life. So there's a guy named Joe Lemond in your twenties and Chamath in your thirties and Toby this decade, maybe yourself next decade, if things go well. Other than what you've shared or maybe it is what you've shared, is there a thread across these three folks that have been really successful that you've learned from that maybe is consistent across them all or even just specific to each one?

Farhan Thawar (00:13:49):
It's interesting because again, this is looking back, you're like, wait a sec, I didn't plan it this way. There's no way you could plan it, right? I'm going to work for a different billionaire every decade. That's not how it works but they're similar. They're mostly different people, but they're similar in one thing is that they have an irrational view of what the world should look like over the next decade or so. They're very long-term thinkers, very rational in that they'll look and say, "Hey, in 10, 15, 20, 25 years, this is what the world's going to look like." And I'm not good at seeing that vision, but I'm good at trying to move towards that vision 1% a week. And so the melding of the two, I know where I'm good and I'm good at pushing the ball forward. And if they're good at the long-term vision, we can both align to say, "You're good at this thing. I'm good at this thing. Why don't we merge forces?"

(00:14:35):
And so that is something that has resonated with me is like, how do I find these irrational all progress depends on the unreasonable man. How do I pair with these people because I'm altogether too reasonable and there's no way for me to become unreasonable, and so I have to merge with these people. And so that is again, something that I specifically have sought out. And even when I was starting my own company in 2015, I actually sat down and wrote a list of all the unreasonable people that I knew in Toronto, and I went down the list and met every single one of these entrepreneurs to figure out are we API compatible and could I work with them? And I ended up picking one of them and starting a company.

Lenny Rachitsky (00:15:15):
That is an amazing story. So first of all, I just love this insight that being aware of this is not a superpower of mine and I'm not going to try to build it. I'm going to find someone to merge with, and connect your APIs together and be the person that builds it, not the person that envisions what to build. I think that's awesome because a lot of people... I need to get good at all these things. I need to become the best at vision and strategy and execution and collaboration and then all these things. And so I think alone, this isn't really interesting instead it's just recognize your strengths and weaknesses and double down on your strengths.

Farhan Thawar (00:15:47):
Yeah, it sounds funny, but me and you talked about it that a framework I wrote down, which I tweet out, me writing that down changed how I picked jobs forever, right? Because I had this lull after my first job in between where I was trying to figure out why nothing felt as exciting as my first job. And it turns out that it took me to sit down and be like, what do I actually care about? And people can get confused. I get confused all the time, by the way, by things that are not on my framework. So for example, a good one, title, company, money, all these things can confuse you because you could have somebody say recruiter messages you and says, "Hey, by the way, here's a new job and here's the compensation." You're like, "Oh my God, this is exciting." And if you don't have a written down framework of the things you actually care about, it's very hard to be distracted. So very hard not to be distracted. You get distracted by that. So instead, I look at the framework and go, does this align with my framework? Right?

(00:16:43):
Actually to the point of, I actually sent my framework to a recruiter one time and I said, "Hey, this thing," because they kept going back and forth to me and I go, "Hey, this doesn't align with my framework." So it really saves me time from not being distracted, but it also forced me to think about every year I can reevaluate what I'm doing and look at the framework and say, "Is this true to my values?" Now, my wife will say this, that I'm like a robot. When I realize that my framework is being violated, I will resign instantly and I've done that before. So without even having another job or anything, I just go like, oh, my framework is being violated and then resign. There's this thing where I know what I enjoy working on, and that framework helps me find it. And so I encourage everyone, anybody looking for a job I always say, "Write down a framework. You can use mine as inspiration, but figure out what you care about and make sure that what you're working on lines up with that."

Lenny Rachitsky (00:17:37):
And this framework is the questions to ask about where to go work. That's your framework. Okay, cool. We'll link to that so folks can check it out. The example of you resigning when it didn't meet your framework, is that a story you're up for sharing? Is there something to learn from that?

Farhan Thawar (00:17:50):
Yeah, sure. So this happened when I was at my previous, a few companies ago, we were running a mobile company called Xtreme Labs. That was the one that Chamath was the major investor in and so we worked with him directly. And what I realized was... And so that company was amazing. We worked on it for many years. It was a mobile app development company. We got to work on mobile apps for the biggest brands in the world, Facebook, Twitter, Instagram, Vine, the NFL, NBA, Bloomberg, Slack, you name it we worked on those mobile apps, and this is right when the iPhone and Android were really gaining steam in '09 to 2013 era. And then we eventually got acquired by Pivotal. And over time, my role at Pivotal, Pivotal, and Pivotal Labs changed from, hey, I was running the biggest office in the world. I was running the biggest pair programming office.

(00:18:34):
I'm a big fan of pair programming to one in which we were really trying to attach consulting to the product. And I ended up being a field CTO, which really, I mean it was fun to learn about that world, but it was different than what I was doing. And so if I looked across my framework, it was violating all the things that I was trying to work. I wasn't working with the smartest people anymore. I was on IC. I wasn't learning as much as I could be learning. And so I wasn't on this and I wasn't having a lot of impact. I was like, oh, wait a sec, this is completely not aligned. And then I just told the team, "Hey, I plan on resigning." And that, by the way, led to great other things because I'm an investor in new companies that have spun out from there and it was a great experience. I'm just saying it at the time, lended me to say, "Hey, you're not actually focused on the right things."

Lenny Rachitsky (00:19:20):
I want to come back to Xtreme Labs. I know there's other stories there that are interesting, but first I want to talk about another theme of things that people often raised when I asked them about you. And this one is intensity, and it's specifically creating intensity in your organization and the value of that, the power of that. I've seen that the way you describe this and I love is how do you expend more kilojoules per hour versus spend more hours on work. So talk about just why intensity, first of all, is so important to an organization.

Farhan Thawar (00:19:53):
Yeah. So I think there's a few things. One, I have this fundamental belief that one hour is one hour. It's the same hour. If you spend an hour or I spend an hour, it's the same time that goes by. And if I just expend more calories in that hour. Let's say we both work nine to five. If I can just get more done in the nine-to-five, we have both... The time has elapsed the same for us, but I just got more done. And that allows me, of course, then I'd be like, "Hey, I'm going to take my kid to soccer and do other stuff." We can still do the same things out of work, but during work, I just want to try to get as much done as possible during the time versus expanding the time and I can give you an example. I used to work at a company where it was like I worked 12 hours a day, but I was playing foosball in the middle of the day.

(00:20:37):
And then we'd go for a coffee break and you do these things. And of course, the time expanded to 12 hours versus trying to compress into that eight-hour day. And pair programming is a great example because, so it's such an intense activity. Two people on one machine, you can get so much done when two people are working together, not being distracted by the internet and distractions, and just focus on writing the solution to the problem at hand. And it's so tiring that usually when people switch on to pair programming, they sleep 10 to 12 hours a night the first few nights because it's so intense. You're working so hard. But for me, that intensity actually leads to extraordinary outcomes even if you don't have to put in more hours. I think most people, you probably hear this all the time, everyone says, "Oh yeah, work hard and do more hours when you're young, whatever."

(00:21:26):
I'm like, what if you just did more per minute? Like quickly get through things. I think there's another unintuitive fact is that people who are really good can actually output high-quality collateral quickly. So take a person who is good and extremely good, the extremely good person can actually get a lot of output in a short amount of time, and the person who's good might take longer. I think there's a time variance there that people don't think about. So you can not drop the quality too much, but get the time down by 2X, 3X, right? Parkinson's Law of scale instead of, if I give you an hour to do something, a really good person can get a high-quality output in one hour.

Lenny Rachitsky (00:22:07):
I want to talk about how you create an org that operates this way, but specifically, you just mentioned pair programming. I know that's one of your favorite tools. Talk about why this is so powerful when you recommended... I think as an outside observer, it's like two engineers on the same code. Why wouldn't we do things half as fast? Talk about just why you're a big fan of pair programming specifically.

Farhan Thawar (00:22:30):
It is the most underutilized management tool in engineering, bar none. It is just not used as much as it could be. So pair programming, for those who don't know, it's two people on one computer. So two keyboards, two mics, two monitors, but one computer, they work together and if it's remote, they use it. You can use a tool like tuple, which we use, and you can just remotely be on one computer, and you're totally right. The famous tweet about pair programming is, wait a sec, we have two engineers on one computer, won't they write half as much code? And the answer is, oh, no, no, they'll write even less than that because it's not about lines of code. The throughput limiter is not hands-on keyboard. It's not like we're both sitting there and the limiter is like us trying to get through the keystrokes onto the screen.

(00:23:12):
The limiter is where is the good elegant solution? How do we think through the problem and build the right solution for the problem at hand? Tobi famously built a lot of Shopify paired programming, and what he would do is he would actually set a timer and him and the CTO Cody would pair program for one hour. And if they did not finish the problem in one hour, they would delete all the code and they would keep the tests and they would start over. And then what their thinking was, if we were not able to articulate and write the code for this feature in one hour, we must be on the wrong design. We must be building the wrong thing and so they delete all the code, kept the tests, and then wrote it again. And sometimes he'd be over by one minute and he would still delete the code and start over because his thinking was the right elegant solution should be able to be written in one hour.

(00:24:03):
And so pair programming, I mean, that's an extreme version of it, but even at Pivotal Labs, if your pair was sick that day and you wrote a bunch of code, the strong version is your pair would come in the next day, delete all the code that you wrote, and then you'd write it again the next day. And again, what better time to rewrite code than right after you've written it because you now know the problem domain? And by the way, it sounds like a waste of time. It sounds like I'm just deleting code but the reason is that code lives a long time. Code is a liability and the right solution, the usually shorter lines, more elegant solution tends to appear after you've done a bunch of pathfinding. And the only way to do that pathfinding is start and then delete and then start and be like, oh, no.

(00:24:47):
Now I know. Delete. And it's super hard to delete, by the way, because we're humans and we have this sunk cost fallacy, so it's hard to delete. But if you can do that, you will actually land upon a much, much better solution. And of course, pair programming has high, high rates of learning because you're just sitting beside... You're not only whether it's tuple or remote or directly, you learn keystrokes and you learn how somebody thinks about a problem. You go back and forth on the talking, and yes, you will write probably less code, but you will move faster along the path of delivering value for your customers than you would if you did it on your own. And there's all these studies that show happiness is higher, knowledge transfer is higher, less silos, intensity is higher, all the things. And at a price of 20% or something of what you would normally do.

(00:25:33):
The analogy I have is the underhanded free throw in basketball, statistically known to sink more baskets, but looks dumb and nobody does it. Literally, Shaquille O'Neal, I'm not that big a basketball fan, but I read this about Shaquille O'Neal, who's a Hall of Famer, and they said, "Why don't you throw underhand?" Because he was notoriously bad at free throws and he goes, "It looks dumb." Even though he's paid millions of dollars a year to do this thing. It looks dumb, doesn't want to do it.

Lenny Rachitsky (00:25:58):
I remember those Shaquille O'Neal years when he had a special free throw coach, and I remember them talking about this-

Lenny Rachitsky (00:26:00):
... When he hit a special free throw coach. And, I remember them talking about this and he's like, "No, I'm never going to do that."

Farhan Thawar (00:26:05):
"I'm never going to do it." Because it looks dumb. And by the way, go back to the beginning of the interview. I don't care what looks dumb or looking stupid, we're going to do this. And so, actually, I ran the biggest pair programming shop in the world.

Lenny Rachitsky (00:26:15):
On that note, so what percentage of shop Shopify do this? Is this how y'all operate?

Farhan Thawar (00:26:21):
Yeah. So, Shopify, I mentioned that Toby and Cody did this at the beginning of Shopify. And the cool thing about pair programming is, and in my old world at XtremeLabs is that we knew exactly what to build, because we were building mobile apps that were almost like contract manufacturing. We're like, "We have an iOS version. Can we build an Android version?" So, we quickly were able to say, "Here's the spec. Go quick." Shopify is such a different company, right? We are a pathfinding company. We are trying to find the right thing to build. And so, pair programming may or may not make sense all the time. Like Pivotal and Xtreme, we were doing 40 hours a week.

(00:26:54):
Shopify is much more of a four to eight hour a week pair programming culture, where you're gathering together on a problem and saying, "Hey, let's pair for half a day, or let's pair every Wednesday." And we use that tool in our arsenal to move quickly down a path. But a lot of other time is spent pathfinding and trying to figure out what to build, and trying to convince field be like, "Hey, we're going to go down this path. Oh, now I know exactly."

(00:27:16):
And sometimes, by the way, 18 months later, we've now figured out all the things and that's the time we should delete everything and start over. And, that's something that we will do at that point. And so, you don't want to be pair programming for 18 months. You want to be wayfinding and pathfinding. And then go, "I see the matrix. Let me just delete everything and now build it." Because the learning is what you're going for. We have all the learning, now let's write the code.

Lenny Rachitsky (00:27:39):
Got it. So it's basically, when the code, you're pretty sure this is correct and it's really important segments of the code base pair program.

Farhan Thawar (00:27:49):
Yeah. And then also we do a lot of pairing during an incident or a way to figure out together, work with somebody and say, "Hey, I'm not really sure and let's jump on a call together or jump on a tuple and go down the path." And say, "Let's figure out together what's going on."

Lenny Rachitsky (00:28:01):
I can't help but ask AI, how does that impact this way of working?

Farhan Thawar (00:28:06):
So, AI is super interesting. What's happening right now with an AI copilot like GitHub Copilot is it is your pair programmer. So, you now can feel like you're pairing actually without another human. You can pair with the AI. And so, what's happening too is that you're seeing people use Whisper, like they're talking to Cursor, and they're talking through Whisper to say, "Okay, let's build a new React component that does this." And they're talking and then it's building. "Oh no, that's not what I meant. I meant doing this." So you can actually not even have to type, just using voice, go back and forth with your pair programmer.

(00:28:35):
I would say, that's amazing. I would still contend take that experience and add two humans together. So you've got an AI copilot and humans, because what's happening is generating code. And the two humans can look and say, "Oh, I know what it's trying to do." And, either delete the code, because you have inspiration and write it yourself, or just take the suggestion and move it forward. But, I love today's world of AI copilots, because you never have to code loan on your own right? You never have to code alone. You can try a different language now, because the API and the syntax is much easier to pull forward. And so, all of those things are a win for engineering and a win for everybody who wants to build any software.

Lenny Rachitsky (00:29:14):
That makes a lot of sense. Basically, everyone's going to be a pair programmer-

Farhan Thawar (00:29:17):
Yes, exactly.

Lenny Rachitsky (00:29:18):
... In the future. Okay, I want to come back to what else you have done at Shopify to create intensity. And I think, again, it's important to highlight the intensity is meant to, "How do we get more done in the time we have and then go home?" Not just work all day every day, weekends kind of intensity.

Farhan Thawar (00:29:35):
Yeah. So we have a few things that we have going for us, right? So one, we have this tool called GSD, which stands for get shit done, which you've probably heard from maybe talking to other Shopify folk, which is this notion of weekly updates to the whole company on what's happening. Again, Parkinson's law at scale. If you ask people every week, they want to show progress every single week. So that's one way I talked about pair programming as well. The other thing we do as a company is, we used to have twice a year was our cadence, Black Friday, Cyber Monday, or we had an event in the summer. And now, we do six-week reviews. So, teams have this notion of every six weeks actually coming together and walking through the roadmap, the resourcing, and what they're working on with their immediate leadership, but then also, with Toby.

(00:30:18):
And so, what's cool about that, and by the way, it's a huge time investment, right? We all get into a room, it's happening tomorrow. So Tuesday, Wednesday, Thursday, a bunch of us will be in the office together and we're going to go through every project in the company, and we're going to talk about the project, the resourcing, how it's going, and we're going to make changes. And again, that creates intensity, because you want to show what has been done, what have you learned since the last six-week review. And, we find six weeks is a very good cadence, because it's short enough that you can remember the context and it's long enough... Six weeks is long enough, especially if you have, let's say, a team of a dozen engineers, you can do a lot. And not only that, you can do a lot in a day, but this is a check-in point.

(00:30:59):
And what I've noticed too with intensity is, let's say, we get a review and there's some feedback we get in that review. We don't wait until the next six-week review, right? The next day we are building things, we are iterating, we are tagging people. And then, by the next week's we're like, "Here's the trajectory." Right? Actually, I want to get that Elon shirt made, "What have you done this week?" Because, Parkinson's law is real. It sounds funny, but I keep bringing this up, but whatever time you allot to something will be the time it takes, right?

(00:31:26):
So, if you're doing something monumental, I don't know, you're doing a reorg or something, right? You can do it the slow way. "Let's sit down, and plan, and roll it out." And it's probably six months in most companies. Shopify, this is a week or two. You sit down, you're like, "Hey, this is the bones of it. Let's bring some more people and think." But then, it's going to start leaking. So we just launch it. Right? And, we do the same thing with lots of things. We just try to move more quickly and get out of the... We don't do change management, we just land it, and then go, "Hey everyone, it's a volatile company. This is what's happening. But this is how we get things done quickly." And then, move on with our lives.

Lenny Rachitsky (00:32:00):
Wow, there's so much there. I have been through the six-month reorgs. And, I think that context you just shared of, "We're at a volatile company, we're changing things. It's not going to be smooth, but we think this is for the best." It's just the culture of Shopify. It sounds like, "We want to keep moving fast. We know this isn't going to be the smoothest thing, but we just know this better to make the change at this point versus wait."

Farhan Thawar (00:32:25):
It's how Toby increased the resiliency in the company. He would walk around in the old days when we had a data center and just unplugged machines, right?

Lenny Rachitsky (00:32:32):
Chaos monkey.

Farhan Thawar (00:32:33):
Yeah, chaos monkey. You're right. But that actually works, because it just says, "Hey, by the way, shit's going to break. And so, let's be resilient to that." And so, same thing here. "Hey, by the way, someone's going to move your cheese. It's fine. We are here to create more entrepreneurs in the world. We're not here to have a six-month change management roadmap. And, that will just actually hurt the speed at which we can deliver value to merchants."

Lenny Rachitsky (00:32:52):
So, on all the things you shared, so there's weekly updates. So the weekly updates are each person shares what they're working on for the week. Is that the idea?

Farhan Thawar (00:32:59):
Each project.

Lenny Rachitsky (00:33:01):
Each project.

Farhan Thawar (00:33:02):
So, each project, it has an update, it might have a video of, "Here's the experience." It'll have a obviously a bunch of writing on what's changed since last time. We have a process called OK1 and OK2, which is like, OK1 is typically at the director level where they're like, "Okay, I'm aligned with the direction that this is going at." Or, "I'm not aligned." And they can make changes. Then, when it goes to OK2, it's typically the VP level of the area, who's now looking to say, "Okay. What you're working on actually aligns with the overall architecture. But by the way, have you looked at this context? Maybe you haven't seen this, this is happening, or the industry." And so, you're trying to align at that level. And then, again, like I mentioned, every six weeks we go through with Toby, and he's an intense guy himself.

(00:33:40):
And so, a lot of it is like, "Hey, why is this taking so long? Are we overthinking it? Are we not trying to move forward on this thing, because we're blocked on something? Is there some piece of infra?" Actually, I'll give you a good example. In one of the reviews from last time, there was an interesting AI problem we were trying to solve with LLMs that required us to have a very large output context window. And, most of the LLMs today have a very small output context window. But in the review, right, we have shared Slack channels with all the LLM folks, right? I messaged in the open AI channel, I messaged in the Gemini channel, whatever. And, within an hour we had increased the context on a bunch of major models and we were able to move forward through the thing, just because I asked.

(00:34:29):
And so, that's an example. It didn't take another six week review, but it increased the intensity, because the team was like, "Oh, we were blocked because we thought we had to now chunk up this data and do this thing because we had smaller output context and we thought we could do a big input context, but we'd have to do this caching." And, it was like this whole thing. I'm like, "Well, did we just ask them if we get bigger?" And then, they were like, "Oh, we don't have this as undocumented, but we'll just enable it right now for Shopify." And so, that created the intensity of the team to be like, "Oh, we can now quickly get unblocked." So that's the example of just moving quick and trying to just, again, ask a dumb question. I'm like, "This is probably not possible, but..." And then, they came back and said, "Oh yeah, we can do that."

Lenny Rachitsky (00:35:03):
That's a great example. And, as you're describing the ways that you create intensity and velocity within Shopify, it's interesting that what you're listing is a bunch of meetings and check ins, which to most people would feel like, "Why do we need so many..." There's all this like, "Less meetings." And I know you guys famously cancel all your meetings and that's a whole thing we can talk about. But, it's interesting that more check ins and regular check ins allow you to move faster. I imagine it's partly because it just makes sure you're not working on things that are unnecessary, and dumb, and not going to be used. And it's just continue to refine, these are actually the most important.

Farhan Thawar (00:35:38):
I mean, it's a combination of trust but verify, right? Because don't forget, the goal of the check-in is not for you to be like, "Ha, ha, I caught you not doing your work." It's not like the Dilbert boss, "Hey, did you do your thing?" Right? Even when I look at the Elon text, which is like, "Hey, what did you get done this week?" It wasn't to try to catch Parag in a, "You didn't do anything or you did a bunch of useless stuff." It was hopefully to pair on the problem, meaning, when I ask somebody, "Hey, did we move forward on this LLM project, because we now have this larger context window?" And then, they came back and said, "Oh, here's what we learned." So then, I can then look at the answer and say, "Oh, so now, have you thought of this? Have you tried..." It's a way to pair on the problem.

(00:36:18):
So, we have this word, everybody talks about micromanagement as a word, and we don't actually think it's a dirty word at Shopify, but the reason we don't think it's a dirty word is because it's not just, again, Dilbert boss saying, "Where did you do the thing?" It's like, "Hey, can I work on this problem with you? And if I work on this problem with you, I got to see where you are pretty often, and then give you advice, or you're going to share context with me, because I'm not in the work every day." To then come back and say, "Oh, based on what I know and what you know, can we move this in this direction? Maybe that's better for merchants."

(00:36:50):
I don't want to overuse the pairing paradigm, but it is really much like, "Can I pair with you?" And I learned this actually very early in my Shopify tenure, because Toby would have these one-on-ones with me and I'd be like, "Toby, you don't have to waste your time, man. You hired me. I got this." Well, he goes, "Oh, you misunderstand why you're here. We are here to work on problems together." And I was like, "Oh, I didn't even think..." I thought he hired me to take problems away. He hired me to work on problems with me. That's completely different than what I thought.

Lenny Rachitsky (00:37:18):
I love that. Okay. One thing you mentioned is meeting thing. For people that don't know what you all did with meetings, I think it might be worth just sharing that briefly, because it's awesome and something a lot of companies can learn from.

Farhan Thawar (00:37:28):
Yeah, sure. Actually, the funny story about the meeting Armageddon, is that, I was messaging Toby prior to me starting at Shopify about meeting Armageddon. And so, I actually think I had a little hand in him doing this before I got to Shopify. I was like, "Hey, have you seen..." I think it was Dropbox, "Have you seen a Dropbox is doing and Meetingageddon? And so, he was like, "This is super interesting." This is years before I started. So, I think it's funny that it ended up being a real thing. But here's what we do. Once a year at a random time, we will delete all recurring meetings that have more than two people, so not one-on- ones, and are internal people only, so not interviews or external partner meetings. And then, we have a two-week moratorium where you're not allowed to add a reoccurring meeting. You can have a regular meeting, but not a reoccurring meeting.

(00:38:11):
And the idea is that there's a lot of inertia behind a recurring meeting. It just always is there, and you know it's coming up, and it's hard to delete, because you're like, "Oh yeah, we talk about this thing every week." And so, what we do is we just do a meeting reset. And, I think, yeah, it's just called chaos monkey and the admins go in and just delete everything. Now what's cool about it is, it forces you to rethink, "Do we need a recurring meeting? Or do we just need one meeting? Or do we need a different cadence?" That's one thing. The other thing is it frees up so much crafter time, right?

(00:38:42):
One of the stats I track across engineering is how many hours are individual contributors in meetings per week? And we noticed that after we did... We did two things by the way. And I have a spicy second one for this, but the first one was we deleted meetings. And the second thing we did was we moved a lot of our Slack into Facebook workplace, which I'll talk about. Those are the only two things we did. And we saw a huge decrease in the amount of time crafters were in meetings. And then, we saw all kinds of other productivity enhancements, because they were able to have that flow time and work on things.

(00:39:12):
So, we're at something like three hours of meetings per week for an individual contributor at Shopify, which is phenomenal. Three hours a week is amazing. I think managers is not that bad. I think I tweeted this. I think it's six or seven hours per week. That's not bad at all, in order to get aligned. And then, all the rest of the time is work time.

Lenny Rachitsky (00:39:29):
And how many hours was it before Meetingageddon and Workplace?

Farhan Thawar (00:39:33):
Yeah, you're asking me a good question. I have to go look and see. But, it came down by something like 50 or 60%. It was something like five or six hours for individual contributors and came down to three. And then, the managers, I think it was 10 that came down to 6, something like that. But it was a huge difference. And the only two things, like I mentioned, were one was the Meetingageddon, the other one was like this, and I can talk about this. This is a-

Lenny Rachitsky (00:39:53):
Yes, let's talk about this.

Farhan Thawar (00:39:54):
... Yeah. So, I mean, I love Slack. It's the IM tool. Everybody uses it. But it can for sure cause distraction. And so, what we did was we moved all announcement information. So, anytime you're sending a status update or large group announcement, we moved all of that to Facebook Meta Workplace, like Facebook for work basically, which is now being deprecated. So, we'll have to figure that out. But, it just moved all this stuff to a ML feed that you can consume differently than you would Slack, because Slack is like I message you and you see an alert and all this stuff, versus Workplace is like, "Oh, I want to go and consume content from the company, and get updates, and share updates." And so, that reduced a lot of distraction as well. And so, I'd love to figure out what the next tool for us is, but it is probably something more like a river of information that I can dip my toe into, versus IM and chat everywhere.

Lenny Rachitsky (00:40:45):
That is super interesting. So, specifically, things that are just updates where you don't need a discussion, you almost want to discourage a discussion.

Farhan Thawar (00:40:50):
Yeah, I mean, it has the commenting, but it's not the same tool. And, by the way, Slack is amazing, we use it. It's just that for this thing, it wasn't working for us. And so, we wanted to move that somewhere else.

Lenny Rachitsky (00:41:03):
I feel like, the more I dig into the Shopify way of working, the more fun stuff I never expected emerges. I'm curious what else is going to emerge. So we've been talking about ways that y'all, and you specifically, have created intensity, especially in the engineering organization. And then, you've also shared just broadly Shopify. What else is on that list? What else have you found helps create more kilojoules per hour?

Farhan Thawar (00:41:24):
Yeah, so again, I think there's nothing, I would say again, start from the beginning, there's nothing more than pair programming, because literally you can't do anything else but be on your computer. So pair programming is the number one. I will say, the weekly cadence helps a lot, right, which you mentioned. Again, which is part of GSD, which is sharing the updates, and then the six-week reviews, that does a lot. On the other side, we also have a lot of metrics and alerts that help us see when potentially things might be happening in the system that can allow us to be like, "Hey, wait a sec, there's too many things going on of this type. We probably have to sit back and reset and figure out what's going on."

(00:41:56):
So one thing that happened, for example, was we started seeing that it was taking a lot of time to develop in our admin, like engineers at Shopify developing in the admin. So we called, what's called, a code yellow, which is before code red. But code yellow is this idea of like, "Hey, we're going to call a code yellow on the admin." We want to make sure that the developer experience inside Shopify is really good. It should be easy to start up the repo. It should be easy to make changes, it should be easy to see the changes. And so, those are the things that, again, we can create intensity, because this code yellow allows the champion to tap anyone on the shoulder and say, "Stop what you're doing and come help this thing." Which is an infrastructure layer thing. And by building out this infrastructure, it allows you to go fast. It takes longer to build infrastructure, but it makes you go fast forever afterwards, right?

(00:42:41):
I'll actually give you an example of one of these. So, we in 2020, 2021, the heyday of pandemic, obviously, there was a crypto summer again and crypto was going nuts. And we were sitting back and saying, "Wow, a lot of our merchants are now asking for NFT gating." NFT gating, which is, "If you have the token, you can now go into the storefront and see my products. You can see my prices and you can check it out, but only if you have the token." And, we were getting a lot of demand from merchants to be like, "We want to do this. We want to sell an NFT. And we want our buyers to have the NFT to have this great experience." And we're like, "We agree. We want you to be able to do whatever you want. And so, we want to build this for you too."

(00:43:18):
And, sitting with Toby, he's like, "You guys are thinking about it wrong." He goes, "How long would it take to build NFT gating?" I'm like, "I don't know. Two, three weeks." He goes, "Now, how long would it take to build a platform layer, which exposes APIs so anyone could build NFT gating in one hour?" I'm like, "I don't know. Two, three months." He goes, "Do that." He goes, "Because you don't know what they're going to build on top of the platform." NFT gating is one thing, one use case, but if you spend the time to build out the infrastructure layer, he calls it putting gas in the tank, if you put the gas in the tank, people could drive on that gas for a long time going forward. And so, he goes, "I always want you to think about..." And the key part was, "What can you build so anyone could build this in one hour?" Right?

(00:44:00):
So, he does this thing to us all the time where he goes, "Oh, this should only be..." He'll say it and people get the wrong thing. He'll say, "Oh, you could write this in a day." And what he means is, "What has to be true so that you could write this in a day? What infrastructure do you need?" And, he actually develops this way. He will write code against an API that doesn't exist, because he's like, "You know what should exist here? This API." He'll write the code, he'll go back and forth and refine the client on the server, and then he'll go, "This is correct, the correct client code. Now, let me go implement the server code."

(00:44:31):
And this is notion of building things as infrastructure that sound slower today, because it's going to take... It's two, three months, instead of two or three weeks. But after that, the things that people built on top, right, were so easy to build, there were so many more scenarios that were emerged. It's just a different way of thinking about software. And, it's intensity in a different way, it's intensity around building this infrastructure layer, which we want to build quickly, but takes two or three months, in this case, but then can get everyone building on top of our infra in a much, much quicker way. And of course, who knows what can flourish from there?

Lenny Rachitsky (00:45:06):
It's interesting and it makes sense that so much of the way you all think is about building the best possible platform, versus the, necessarily, best possible point solution for someone. And it also explains why you spend so much time in crafting really great code and pair programming, because again, it's a platform for other people to build stuff on. So, I think, a lot of this is very useful, especially for platform businesses.

Farhan Thawar (00:45:29):
No, exactly. And actually, you're making me think of a stat. So, last year, maybe a tangent, but I tweeted out that GitHub Copilot has written over 1 million lines of code for Shopify. And people are like, "Oh my god." And it got picked up. And everyone's talking about it. And I go, "I don't know why is everybody getting so crazy, because what I want to see is GitHub Copilot deleting 1 million lines of code." That's when you know we're actually at this point where this is close to an engineer. Right? And so, we famously have deleted millions of lines of code this year, because we were trying to focus on, again, the sunk cost and rebuilding things elegantly, or you don't need this anymore and rebuilding. And I even tweeted out, I think someone said, "Oh, Shopify is in the top 10 Ruby code bases in the world." And I said, "I never want to see us on this list again." We shouldn't be gunning for number one, we should be gunning for number 100, right? We want to be not on this list. Right? Someone else can take the crown.

Lenny Rachitsky (00:46:22):
This episode is brought to you by Vanta. When it comes to ensuring your company has top-notch security practices, things get complicated fast. Now, you can assess risk, secure the trust of your customers, and automate compliance for SOC 2, ISO 7001, HIPAA and more with a single platform, Vanta. Vanta's market leading trust management platform helps you monitor compliance, alongside reporting and tracking risk. Plus, you can save hours by completing security questionnaires with Vanta AI. Join thousands of global companies that use Vanta to automate evidence collection, unify risk management, and streamline security reviews. Get $1,000 off Vanta when you go to Vanta.com/lenny. That's V-A-N-T-A.com/lenny. Wait, talk about more about this. So, there's been a drive to delete code and simplify. What's behind that? What's going on there?

Farhan Thawar (00:47:22):
Yeah, so there's a few things, right? One is, the more context you can fit in your head around a code base. And you can never really fit all of Shopify in your head, because it's a big complicated set of tools we give to merchants. But, the more you can simplify, the much easier everything becomes, resiliency, performance, reliability, maintainability, all the illities become much, much, much easier when the code base is simple. Now, all you need really is the mandate of like, "Oh, well, let's look at this code. And, if I could start this today, would I really build this thing? Or do I now have enough domain expertise to say, 'Oh no, this is the right solution?' So can I delete start over and build this more easily?" And now, everything else becomes easy to build on top of.

(00:48:04):
And so, routinely, we have a delete code club, we have hack days, which happens two or three times a year, where there's always one team that is focused on deleting code. They even have a manual, "Here's how to find things to delete." And, it's amazing. We almost always delete. I don't know if this is good or bad. We can always almost find a million plus lines of code delete, which is insane. But, at the same time, I applaud the teams for going after the cruft and the code base. And everything gets easier, right? Codelets loads faster. It's easier to understand.

(00:48:34):
This is why when I look at GitHub stats, you shouldn't really look at... I think Google put out and said, "Oh, 25% of all code is now written by AI." I'm like, "Where's the delete? Where is the 25% of all code is deleted by AI?" Right? This is where we have to start thinking about it. Because, the right code is never the volumous lines of code metric. It's always something else. It's always elegance. And that's where we have to think about. So, it is something that, as part of us being long-term infrastructure thinking, we really do care about that.

Lenny Rachitsky (00:49:06):
I love this, in part, because it connects to the topic we're talking about, which is speed, velocity, intensity, smaller code base, cleaner, better code base allows you to move faster. I used to be an engineer actually. But, both my engineering brain and my PM brain, I love the idea of killing stuff that's useless, fixing, making code cleaner, and better, and more durable. In reality, very hard for companies to prioritize this thing. Is there anything you found that helps you do that? You mentioned hack days and weeks are one part of that. Probably helps that Toby's an engineer and he understands the value of this stuff. But I guess, for folks that want to do this more, any advice?

Farhan Thawar (00:49:42):
Yeah. So actually, when we're building something, we think of it in one of three buckets. We're like, "Are you building an experiment, a feature, or infrastructure?" And, once you bucket things, you can say, "Oh, it's an experiment." You're like, "Cool. This is not infra. This is like, we're trying something to learn." And, by the way, that might turn into an experiment or infra, but it starts off as an experiment. Now, if you're building a feature, a feature is basically you're taking advantage of an existing piece of infra, right? So, token gating is the example I gave. If you could now build that in one hour, you would probably say, "Oh, we have the right infra below it."

(00:50:14):
But if you did what Toby does, which is, he's like, "Here's the infra I wish existed. Here's the feature. The feature might be quick to build, but now I have to go and build the infra." You're now slotting yourself into infra land, which is like, that could take longer, but you're now enabling it for a bunch of use cases. You don't have to think about it at once, because you may have people using your API in a different way.

(00:50:32):
So, I think you have to slot yourself. Now, how do people get into this mode? It is super, super hard. And, I would say, Toby is the secret sauce here, because he pushes us to think about things as infra almost all the time. I mean, one of the things that annoys me the most probably is that I'll always come to him and say, "Hey, we can do A or B." And he looks at me and he goes, "You know what I'm going to say, right?" I'm like, "You're going to say go back and generate more options." Because he doesn't like those. "I don't like A or B. Come back when you have something else." Right? Actually, maybe I'll tell you a little anecdote. He has a story where he says, "There are unlimited amount of wrong options for any problem. There's probably 10,000 right options, but everybody stops at the first right one, instead of what you should be spending all your time on, because the options that don't work, you're not going to spend time on. But you have to figure out which of the 10,000 options is the right one and spend time in what are all these right options? Don't just stop at the first one."

(00:51:24):
And so, when I come to and say, "A or B." I'm picking two of the 10,000. And he's like, "That's not what I... Go back and generate more options, because those are not the optimal ones." So, he is quite the philosopher on these things. And it does really change the way the company works, because he'll push you on these things. And then, we over time learn to spot the same patterns. And I learned to push my team on infra, and deleting code, and making things simple, because by the way, who doesn't want to get free stuff? Right? Free performance, free, easy to navigate code base, free maintainability, free resiliency,, because now, we went and did the hard work of deleting. It is hard. But that goes back to the beginning, right? Choose the hard thing. Don't just build the feature-

Farhan Thawar (00:52:01):
The beginning, right? Choose the hard thing. Don't just build the feature, go make the feature easy to build.

Lenny Rachitsky (00:52:06):
I feel like there's just more and more good stuff. What else is there that might be helpful to folks while you're thinking about it? And interesting, I was reading your tweet where you shared a lot of this advice, and you mentioned this briefly, but I think it's important with pair programming, one of the benefits is there's no multitasking. You're not checking Twitter, Slack while you're working because you're there being watched. And I could see why that is more productive just innately.

Farhan Thawar (00:52:31):
Oh no, for sure. Again, like underhand or free throws not only looks dumb, it feels dumb. People don't... They feel like they're wasting time sitting beside somebody and being like, "Well, I could be on my computer doing this thing." But together they are building a machine. Do you ever read the Undoing Project, which is about Amos Tversky and Daniel Kahneman, the famous philosopher.

Lenny Rachitsky (00:52:54):
By Michael Lewis, I think.

Farhan Thawar (00:52:56):
Behavioral economist. Michael Lewis. Exactly. And he said the famous line was "Alone, we're okay, but together, we're a genius." Right? That's a pair programmer. That's like two people. You're like, "Ah, we're okay. But together, we're a genius." And that's exactly what pair programming is. And hopefully me plus an LLM is a genius as well, but that's the genesis of that thinking. So I would say another thing that helps us create intensity is demo culture. So as part of the GSD updates, hopefully we encourage people to share high fidelity updates, which is not just imagery, but actually a demo. One of the things that can go wrong with just their screenshots is you don't really get the full experience. You can't tell how slow things are or whatever, but with a demo, so you can put a link. We have this tool called Spin, which is an internal development environment like a cloud dev environment where you can say, "Hey, click here to try this on Spin, and then you can try it and you can see how it works."

(00:53:52):
Or they say, "Turn on a beta flag in your own store and then try it." And so this short circuits a lot of misunderstandings, because you're like "I'm going to try it." And you're not waiting until the end, especially with a beta flag. You're like, "Hey, it's in my store. I just realized that I went in and now this page takes 20 seconds to load. Is that what you expect?" You're like, "Oh, we didn't find this use case." You're going to learn that much more quickly.

(00:54:13):
And that creates, again, intensity on the fidelity of the feedback you're getting because famously, some of our PM team will create a friction log. They'll be like, "I am walking.." They'll just create a screen share, create a video and go, "I'm walking through. I turn on the beta flag, I'm walking through this experience. Here's my feedback on the experience." And you're getting this high fidelity throughput coming back to you that you're like, "Okay, let's fix these things for next week's iteration and then share another beta flag and say, 'Okay, try it now. Try it now. Try it now.'" And so you're not debating about status reports, you're kind of debating about the experience.

Lenny Rachitsky (00:54:46):
So I'm trying to think broadly all the things you've shared, kind of how they fit together that allow you to move this fast. And I just looked up a few stats to give people a sense of just the size of the company today and how successful it has been as they hear the stuff we're talking about. So you guys are about 11,000 employees, something like that according to the Googles. And you're hitting not necessarily all-time highs on market cap because COVID gave you guys a big boost for a while, but you're kind of coming back to this insane valuation that you all had during COVID. So it's essentially all-time highs at a 10,000 plus person company moving really fast, shipping constantly. People love the product. And it feels like one key of what you're describing is essentially this operating rhythm that creates these check-ins that keep people moving and focused on the right sorts of tools and getting them quick feedback if they're moving in the wrong direction.

Farhan Thawar (00:55:42):
And having the leaders pair with those people on those problems, not just checking in, but actually pairing with them on the problems that they're facing. So you get both the crafters who are working on the stuff and the leaders who may have broader context working together to kind of unblock.

Lenny Rachitsky (00:55:57):
And it's so interesting that it's like, again, people often are often like, "We don't need meetings. Get rid of all the meetings." You guys do that, but also, there's a lot of power in strategic meetings and check-ins. Another kind of bucket is just the engineering environment, engineers working with engineers, pair programming, things like that. There's a tool you mentioned for pair programming, Tuple, I think.

Farhan Thawar (00:56:17):
Tuple. Yeah. It's funny because we use it exclusively, but we actually have this line internally, we call it, Shopify should be a crafters' paradise. It should be the place where crafters come to practice their craft and get better at their craft. Obviously, resonates from a lot of the engineering crafters, but it's not only engineering, it's UX and PM and ML, all the places where you'd want those people to actually have a great experience. We want them to come to Shopify because we believe this is the best place for that.

Lenny Rachitsky (00:56:46):
I love it. I just wrote a note down of just how you set up your teams for success. Oh, just avoid distractions. So I think the pair programming helps the workspace, workplace shift from Slack helps. I think you're also very firm on their working hours. You basically don't let...

Farhan Thawar (00:56:46):
No.

Lenny Rachitsky (00:57:03):
No. Okay. [inaudible 00:57:04]

Farhan Thawar (00:57:04):
No, not really. Yeah. We're not super firm on working hours from that perspective, but we do have a lot of people on East Coast time zones. A lot of stuff happens then, but we do have people all over the world. But I did mention we do have the check-ins and the six-week reviews on the cadence. So that six week cycle does give you a little bit of the, what did you get done and are you blocked mentality. And you can expect coming in a couple of times and being like, "Hey, we didn't get a lot done being unblocked." For you to change your approach to go, "Okay, I don't want to go to another review where we didn't get a lot done." So what am I doing this time to make sure we unlock a lot of progress? And that check-in can give you that ammo to be like, "Let's do this this time."

Lenny Rachitsky (00:57:44):
And you're also remote first as a company.

Farhan Thawar (00:57:46):
Yes.

Lenny Rachitsky (00:57:46):
Which I think is especially cool. Now a lot of companies are going back to not remote. You guys are staying remote. Why do you guys decide to do that? What have you seen as a big benefit of that?

Farhan Thawar (00:57:55):
Yeah, so we have this remote, so I like to call it 90% remote or 95% remote because we have these intentional IRL experiences. So every summer, we just started last year. Sorry, this year. We're doing this thing called Shopify Summit where we bring the whole company together, get together and it's a combination of talks plus hack days and it's a come together experience like food and parties and bands. And it's a super fun way to re-energize and rebuild your trust battery over time. And then we have this thing called bursts, which is, "Hey, you want to work on a problem? You need to prototype, you need to hack." People can just say, "Hey, I'm starting a burst. We're going to have five people. We're all going to go to Ottawa or Toronto or Montreal or somewhere else and we're going to talk about this problem and get together."

(00:58:38):
And so a combination of those two things mean throughout the year, you can recharge. We have the trust battery notion, which is how much trust can you have between people and it can deplete over time if you're remote. So then we have offices which are like, come in if you want. Like I mentioned, I come in once a week and now Toby moved to Toronto, so now I'm in three days a week. But it's like if you want to come in, you don't have to, right? Today, I work from home, but tomorrow, I'm going in. And that allows you, again, to have those random interactions and allow you to feel like, yeah, we're 90 plus percent remote. But I would say the main reason is we want to hire the best people in the world and those people can be anywhere and just happens to be that not all of them are near an office.

(00:59:20):
But again, with the bursting, here's a good example. For Black Friday, Cyber Monday, I encouraged all engineering leadership to come to Toronto. We're all going to be in the office watching the graphs. And then for hack days, I try to get people to go to the ports, which we have four of them, Toronto, Montreal, Ottawa, and New York, which again are come in if you want, but then get that IRL. And so it's kind of a little bit of a combo. I wouldn't call it hybrid though because you don't really have every Friday you come in or don't come in. It's more like, come in if you want.

Lenny Rachitsky (00:59:48):
There's so many things to talk about. This trust battery metaphor by the way is awesome. I've learned to use it also. And again, it's just basically everyone, your trust with someone is like, think of it as a battery that can deplete and grow and you should try to charge it up when you can and then use that charge over time.

Farhan Thawar (01:00:06):
And it can be strategic by the way. I've seen people use it as a... I'm pretty sure Toby says he starts everyone at 50% and then he gets to know you. And then I've seen people use it as the opposite, saying, "Hey, look, this team is hard charging. I'm going to start you at a hundred. Assume that you already have high trust, do the things, and only if you are doing things that are off alignment, does your trust battery deplete." So I've seen people use it, the terminology as a shortcut way to figure out how to work with somebody.

Lenny Rachitsky (01:00:30):
I love just how first principles you all are, and there are so many things are so unique to how you operate and clearly it's working. And so I feel like we just keep going on and on. I want to talk about hiring. I know you have some pretty unique perspectives on how to hire people that are awesome, but also, hire them quickly. But before we get there, is there anything else that you think might be really valuable to share in terms of intensity, velocity, moving fast?

Farhan Thawar (01:00:53):
I think the personality of the leadership team is quite intense. We have a lot of founders on the exec team, which are impatient, intense people by design. But even some of the non-founders are just accomplished people who tend to be pretty, we all have this attitude of impatience, and so maybe, I don't even know if that's a learned skill you can learn or if it just comes along with your personality, like genetics. But we typically, even at the leadership team, for example, we try to do, here's my weekly thread of all the things that are going on so that we can not only share, but also show progress on things. And then someone can jump in and say, "Oh, this thing you're doing, it relates to my thing that I'm doing over here." It creates this notion of, there's a lot going on all the time and we want to keep the vibes, keep the energy high. So a lot of high energy intense people.

Lenny Rachitsky (01:01:45):
It reminds me while I was at Airbnb, it felt like no matter how well things are going, it always felt like Brian especially is just pedal to the metal. No matter how well things are going, it's not going well enough. How do we go faster? How do we do more?

Farhan Thawar (01:02:00):
Well, I would actually go further. I think if you don't have two or three big projects that are on fire, you're probably not pushing hard enough because you're not really trying things that are outside of your... If everything's going well, are you really taking the risks you need to be taking? So I think you have to over-rotate a bit and there should be a few things on fire at all times, not because you should create that, but it should just happen because you're stretching into new things that potentially or you're going faster than you should have, or there's a new leader you've counted on early because all these things that should create this thing of it might work. And so you want to have a little bit of chaos at the edge.

Lenny Rachitsky (01:02:39):
I love that. And it may sound stressful and why would I want that? Why would I want to work with chaos and fires everywhere? But in reality, if you don't, your business is unlikely to become incredibly successful and that is even more stressful and painful.

Farhan Thawar (01:02:55):
Correct. Yeah, it's like the opposite, right? It's like this idea of people feel like the comfort gives you stability, and really the uncomfort gives you stability because now you're constantly learning and that makes you more robust against things that could come across.

Lenny Rachitsky (01:03:11):
Choosing the harder path, some might say. Okay, let's talk about hiring. You have some really interesting takes on hiring. One that I've heard about is that you don't like the interview process. You kind of like to prefer not to interview and do something instead. Talk about that.

Farhan Thawar (01:03:28):
Yeah. So throughout my career, what I've noticed is that, and I'm sure everybody, this is a dirty little secret, right? Interviews are not a good predictor of performance. We know this. We know this from studies. We know this. Everybody at their company knows this, where somebody interviewed well, wasn't as good in the job or the opposite, didn't interview well and then came in and was phenomenal. One example I have from my startup right before we came to Shopify was I hired two people for machine learning. One was a PhD, taught at the university, was like, oh my god, no brainer, was also recommended by an employee. We're like, "Oh my god, this person's going to be great." The other person was a dude I met at the coffee shop who had never had a software job but was just so interested in machine learning and person A, we let go within a few weeks because not a fit for our culture.

(01:04:12):
And person B was at our startup and is still at Shopify today and is a phenomenal machine learning engineer who literally at our Christmas party was like, "This is my first software job." We're like, "How?" It was just so cute. And we gave them both the shot. The key was I didn't use the resume in either way to bias. We brought them both in. We said, "Here's the environment." It was all pair programming at my startup. And so they pair program, and actually as an aside, I really believe in pair programming when I made people work in pair programming with my own money. I paid for two people to be on one computer. So that's how you know...

Lenny Rachitsky (01:04:50):
Less than half the code.

Farhan Thawar (01:04:51):
Yeah, exactly. Right. Less than half the code. But anyway, so pairing. And it was pretty clear after just a few weeks, I would say let's say up to three months is the amount of time I give people, that person A wasn't going to work out than person B was. So what I really like to do is use this race car analogy. If I told you, "Hey, I want to go hire the best race car driver," there's not really that many questions you could ask them except for put them in the car. And so the same thing happens with us is that of course, we have to do interviews, but we do really spend time in the 30, 60, 90 days to make sure that the thing that they are bringing actually lines up with what we need at Shopify. And you should also be transparent with people because if it's not a fit, it's actually good for them and you to figure that out as quickly as possible because they could be amazing somewhere else.

(01:05:39):
We mentioned the chaotic environment and fast moving environment Shopify is, that's not for everyone, but that's okay, right? We're not looking for... We've talked about that we want to be as the best 10,000 person company in the world. We're not looking for millions of people. We just need the best 10,000. And so if it's not a fit, it's in your interest and our interest to figure that out quickly so that you can go somewhere where you will be amazing and for us to have the people who will be amazing at Shopify. And so job trials, I'm a huge fan of, which leads me to intern programs, what a great interview process because you now have real work product from somebody for four months. They get to see what it's like to be at Shopify for four months. We get to see what it's like for them to be at Shopify for four months, and that can turn into a full-time gig.

(01:06:21):
And that's a great interview process because you literally know exactly. You don't have to... I'll give you a funny example. I think I've heard a company where, "Oh, we have an intern process and then afterwards, we interview them for full-time." I'm like, "What are you going to learn from let's say even eight hours of interviews that you're not going to have learned from four months of real work experience?" And so there's just things like that. You just got to look at the work product. And so I'm a big fan of job trials, and in my previous companies, like you mentioned, I almost didn't interview anybody. I almost just said, "Come in and work." And it allowed us... We had a much higher in the first 90 days, like 20% attrition before 90 days because it just didn't work out. But those after 90 days, we had less than 1% attrition because they knew exactly what they're getting into and we knew exactly how they were going to fit.

Lenny Rachitsky (01:07:04):
So in terms of the hiring process, you're still at Shopify. You're interviewing people, they're doing technical evaluations, things like that. But it sounds like there's a very strong setting of expectations. "We will hire you, but we'll actually clarify if this is a good fit in the first 30, 60, 90 days and we're going to do... We may let you go and there's a good chance we may let you go." Is that just the way you set things up?

Farhan Thawar (01:07:27):
Yeah, I think the way to think about, it's more like we want to make the interview process as close to the real job as possible because by doing that, we can likely assess the skills that you have in your interview closer to what's happening in the job. So that's one. Two, we have this interview step called the life story where we try to figure out if, are all the experiences you've had up until now actually going to be... Does it show that you are a curious person with range? Because if it does, that's likely more of someone who's going to be a fit. I had this famous line from somebody who said, "You know what I don't like about resumes?" I'm like, "What?" They go, "It tells you what you did, but it doesn't tell you why you did those things."

(01:08:10):
And it's such an interesting insight. Your resume should be a why, like why did you go from this company to this? That's the interesting part. Not that you are a PM at Microsoft and a PM at Stripe. It's like, why did you switch from Stripe to Microsoft? There's something interesting there. And so the life story is trying to pull that out. It's like, why did you make the decisions? What did you do in your past that was interesting? Are you curious? I always thought... I read this great book, Range by David Epstein. That book was maybe one of the hardest books for me to read in my life because every page I was like, "I don't believe it." I kept thinking I was a specialist. I kept turning the page going, "I don't like this data that keeps showing that generalists are better." And then by the end, I realized that I'm a generalist. It took me so long to realize, and funny for me because I ended up redesigning the compensation system for Shopify, even though I'm an engineer.

(01:08:56):
So I still thought of myself as an engineer through and through, even though I work on recruiting and HR and all these other things. But I think that that's what we're trying to tease. And then yes, in that first period, we actually have a survey that goes over Slack that says, "Hey, how happy are you with the person that you hired?" And that should, in conversation with the person, you should give them the feedback to figure out, "Hey, are there things you need to adjust to better fit in and make sure the expectations are set up?" But then also, together with the person, figure out, "Hey, if you're not feeling this, let's find you either a different role in the company or somewhere else because we want the people here to have high impact." But that person should have high impact somewhere, could be at Shopify, could be in the same role, could be in a different role, could be at a different company. But that's a good thing for everybody.

Lenny Rachitsky (01:09:41):
And then do you actually do work trials with new engineering hires, or is that something you aspire to do?

Farhan Thawar (01:09:46):
Yeah, I would love to do it. It's hard to do with the volume resumes we get, but we do do it at scale with the internship program. So like 2025, we're going to hire a thousand interns, and that is going to give me a thousand job trials to pick the top X percent of those to come to Shopify full time.

Lenny Rachitsky (01:10:03):
So just to double-click on that, so you're hiring a thousand interns over the course of the year. That's a lot. And the idea there is these folks are actually useful building useful things, and it's an interview process for the internship.

Farhan Thawar (01:10:17):
Yeah, I think it's two things. One is some people look at an internship program as community service. Let's give back to the community. Let's hire early talent. And I'm like, "Hold on a sec. Are you telling me I could hire a thousand people over the year?" And they will come to work with an LLM and a brain because they're growing up in the age of AI. They will be useful to us because they come from a different generation and they have, in our case in commerce, they have a different experience about shopping and AI and bots and chat and voice and all these things. They'll be useful to us. We'll teach them some stuff as well. And then together we can decide if they might end up going somewhere else, in which case, we have the Shopify imprint on them going to whatever other company, which is I think a positive, or they might stay at Shopify and be useful over a longer period.

(01:11:02):
It seems like win, win, win. The other thing that was cool is after I did that tweet, a bunch of other CTOs messaged me and said, "Hey, we're going to hire 1,001 interns to beat you guys." And I'm like, "Great." Just from that one tweet, if I can get the early talent ecosystem restarted here after a really tough last few years and layoffs, it's great for everybody because now they're realizing that they also realize that these people are super valuable and they bring together a completely different set of skills. And by the way, here's a secret in pair programming, interns will always be more intense than the full-time. And so that also helps the flywheel of intensity go for it.

Lenny Rachitsky (01:11:40):
It all just keeps coming back. Did the internship program emerge out of this co-op system that Canadian schools have and a Waterloo has a big co-op program?

Farhan Thawar (01:11:49):
Yeah, I went to Waterloo. And so yeah, hint, hint. So I went to Waterloo and I did co-op and I did intern programs there. It was amazing. What a great experience, because what ends up happening is you leave Waterloo with your degree, but also with two years of experience because I did six four-month work terms, 24 months, and you end up walking. I think one of the big parts of it is just interview skills because I interviewed for 10 plus jobs every four months, and I did that six times. And so you come out having done lots... You have a lot of interview experience, but you also have work experience. And so just taking that to the next level, Shopify has always had interns. And what I felt like we needed to do was, again, restart this notion of early talent in the ecosystem. I would say one or two big differences with our intern program.

(01:12:36):
One is we're making them come in three days a week versus full remote. And the reason for that is, and we're doing it just in three offices right now in Montreal, Toronto and Ottawa. And the reason for that is because we want them to have a cohort because early talent is different than you and I who've been in the industry. We worked in office, we worked out of office. We're more comfortable with navigating partnership discussions and talking to people in different companies. But these people have not. They may have never worked anywhere.

(01:13:02):
And so to not have the IRL component would do them a disservice. And so we specifically made it in those ports and the people are traveling by the way, they're moving to Montreal to do the internship. It's great. And then if you're a mentor or manager for one of the interns, you have to at least see them like IRL once a month. So we're kind of making these experiences. And of course, they'll have a cohort of dozens of people that will be with them along the way. And so we think that'll just make their experience better. And of course, nothing like tapping someone on the shoulder and be like, "Have you seen this era before?" And so it's easier in an early talent situation. And then of course over time, if they become full-time, they can still come to the office. It's come if you want, but they can also go full remote.

Lenny Rachitsky (01:13:39):
That is amazing. For folks that don't know anything about these co-op programs briefly, it's just basically while you're in school, before you graduated, during the summer, you go work at a company.

Farhan Thawar (01:13:39):
No.

Lenny Rachitsky (01:13:48):
Oh, during the year. Okay.

Farhan Thawar (01:13:50):
Yeah, it's during the year. So what happens at Waterloo is, what I did was I did eight months of school at the beginning. So two terms. My first co-op term was summer, but then it was work, school, work, school, alternating for the whole rest of my time at Waterloo.

Lenny Rachitsky (01:14:02):
It's like semesters alternating.

Farhan Thawar (01:14:03):
Exactly. So every four months I did either school term or work time. So I was doing work in January sometimes and September sometimes. And it was super good because again, it also allowed me to be super intense at school for four months and then go to super intense work experience for four months. But yeah, it's a model that... I was just at Waterloo this week doing a talk, so I love that symbiotic relationship between Waterloo and the employers, by the way, not just Waterloo. Lots of schools do a summer program, UFT and others, lots of schools in the states.

Lenny Rachitsky (01:14:32):
Fun fact. So total tangent, I had a startup called Local Mine, started it in Montreal of all places. I'm not Canadian, but moved there for various reasons. It was awesome. And our first hire was actually from the co-op program. I don't know if it was Waterloo, his name is Nick Adams. And he applied. Just he saw our job posting, I think, and were like, "What is a co-op?" And he came to work and then he went back to school, and then we hired him, and then he ended up at Airbnb when we got a card.

Farhan Thawar (01:14:59):
There you go. So for us, actually, when I did my startup Helpful, I had one or two engineers, and then I actually literally just hired four interns because you hired them in February for May. And because I was doing pair programming, I had to make sure I had four full times by then. So I hired the interns in anticipation of having the full times. And I literally had, I think I was off by one week, so one intern had no pair for a week, but then after that in May, I had four full times, four interns, and then they paired the whole time.

Lenny Rachitsky (01:15:31):
What a journey. I want to talk about just one other topic real quick and then we'll wrap this up. And it's around XtremeLabs. So there's a bunch of stuff here. It feels like it's just like this tech mafia of Canada that a lot of incredible people emerged out of, and there's a whole bunch of stuff we can talk about. One fact I heard while you were there is you had a hundred reports, direct reports that reported to you.

Farhan Thawar (01:15:56):
A 120.

Lenny Rachitsky (01:15:57):
120 direct reports feels like a complete nightmare to me. Tell me why you decided to do that, if you'd recommend that for other people.

Farhan Thawar (01:16:05):
Yeah, so what ended up happening there was we started off small. It was 10 people. When I got to XtremeLabs, I wasn't the founder, but I was very early on and I just had everyone report to me. And then as we grew, I just kept having those people report to me and I was trying to figure out, we talked about crafters and crafters paradise, this idea of people don't really... Their managers are useful, but I was trying to figure out could I solve the problems that they needed their manager for in other ways? So for example, what should I be working on? I was like, "Okay, well, we have product backlogs" or "I'm blocked on something," or "I need feedback on the product I'm building," or "I'm stuck on this technical problem." I tried to figure out ways to not have managers be the answers to those questions.

(01:16:48):
I'm like, "There should be another answer." And so pair programming really helps you get unblocked quickly because you have another person that you can bounce technical ideas off of. Having a product backlog can tell you what to work on. We had demos every week, demos internally, and then we had demos with the clients every week because we were a contract manufacturing for mobile. That gave them feedback on whether they were going in the right direction. We had set working hours, which made things super intense in the office. This is again like 2009 to 2013. So all these things didn't really need a manager. And what I realized was what the unblocking thing needed a manager. I'm blocked on this. Well, I said, okay, if... I had all these directors. I did two things famously. One, I had a lot of direct reports, and two, I did not do any scheduled one-on-ones because you can't have 120 direct reports and do a scheduled one-on-ones because you're never doing anything but one-on-ones.

(01:17:31):
So I said, "I'm going to be around a lot because I don't have a lot of one-on-ones. So we can do unscheduled one-on-ones." And what that means is if you are blocked, actually there's a famous picture where I had this weird cube desk where it was like a circle almost in the middle of the whole floor of engineers. And I was always there because I wasn't in a lot of meetings and people that were blocked, they could just come up to me. Actually, one cool thing about pair programming IRL is you can look across and just see if it's working or not. Because if two people are intensely on the computer, you know it's working. If one person is laying back or you're like, "It's not working," so you can just walk up to-

Farhan Thawar (01:18:00):
It's working if one person is laying back or you're like, it's not working. So you could just walk up to them and be like, "What's happening?" But they would come and ask me questions and I can unlock them. Like, hey, we're blocked on this. We don't have this API. We need money for this machine, whatever. And so the unscheduled one-on-ones ended up being a real clarifying thing for me. Because I did scheduled one-on-ones my whole career and I realized after leaving Microsoft for three years, I'm like, where are all those one-on-ones useful once a week for three years, right? A hundred and fifty one-on-ones.

(01:18:26):
So the unscheduled ones were, though. I was like, when I knocked on my manager's door and said, "I have this problem, those were important." So that's what I created at Xtreme. And the 120 directors, it just grew over time. I just didn't think I needed managers. So I was like, let me unblock these people on another way. And we came up with other things to systems to unblock them that didn't require a manager. And I just also had a good memory. I knew exactly everyone's skills and compensation. I knew all that off the top of my head, so that helps.

(01:18:54):
The thing that I broke was actually, this is Chamath. He came in and became our biggest investors. He's obviously is a smart guy, but he said the right thing, which is not, this can never work, because then I would go into defense mode and explain to him why it would work. He just said to me, I'm not going to debate with you whether this works or not, but will it work at 400 people? And I said, probably not. He said, okay, so let's change it.

(01:19:16):
And so we did then ended up putting a little bit more of a structure, but I made a few people directors and I forced them to have 40 direct reports each. I said, we're just going to make it still pretty flat. And then that did end up working, because it still allowed them to use the system to unblock people versus having to do a one-on-one every week, or having to talk about things that potentially a system could unblock. And so I tried to figure out ways to systematize things.

Lenny Rachitsky (01:19:45):
I love it. Just another example of doing things differently, not necessarily just, here's how it's done and I'm going to do it that way and experimenting with it. Even if you knew, okay, maybe long term this isn't the way it's going to operate. I imagine at Shopify you don't have 120 reports.

Farhan Thawar (01:19:58):
No, we have fourteen or something. We do have these guardrails where I think we say, Hey, in engineering you should have between eight and 20. There are definitely people who have more and people who have less. But we do try to keep things as flat as possible, because we do believe that it doesn't make sense to have three people reporting to and then to somebody, and then they only have three people. You just make a very deep hierarchy. We actually do see, by the way, the farther you are from Toby, we can see things in the survey results. The alignment gets out of whack, and so you do actually see that you want to be closer, you want to have a flatter org in general, and that can be achieved by just having more direct reports per level.

Lenny Rachitsky (01:20:39):
Makes sense. Okay, final question before we get to our very exciting lightning round. We have this recurring segments that I call Fail Corner where generally people come on these podcasts, they share all their successes. Here's all the things that I've done, right. Here's all the big wins. And everyone feels like, oh man, I wish I was always successful people. When in reality, everyone that comes on has failed many times. Is there a story of a failure in your career that you could share that helps people see that even folks like you fail, and maybe what you learned from that experience?

Farhan Thawar (01:21:10):
I have a few. I'll say one thing by the way, because I think I read this in Tim Ferriss's book or in the podcast where he said, create a failure resume and write everything down. And I would not recommend doing this because I did this and I got super... I'm like a high energy happy guy. I wrote down, I have a note on my phone called Failure Resume, and I wrote down all the times I failed and it is depressing. So I would not encourage people to do that, but I'm happy to tell you about a few instances.

(01:21:33):
So well, one is actually I've been laid off twice and people would not expect like, oh, I'm doing this thing and I've been laid off twice. And I think in both times it was the right thing, it was the right thing for the company, the right thing for me.

(01:21:45):
And I kind of used that experience as a way to reevaluate and eventually came out with my framework of how I want to spend time. But that's maybe a different story.

(01:21:54):
I'll tell you about one at Shopify, the first week that I started, 2019, we were rebuilding our point of sale system, which now does billions of dollars of GMB. But back then we were like, well, let's rebuild it with a new UX and a new technology platform. And it was my first week and I'm the mobile guy, coming from Extreme Labs. They're like, should we build this in React Native, or should we build this natively on the mobile platforms? And so I went through this evaluation, spent a lot of time, blah, blah, blah, and I came back with a hedged solution, which is kind of dumb. I said, let's do iOS and Swift and let's do Android in React Native. And the reason I said that was I said, I want to learn about React Native and I think Android's the harder platform, so let's build that in React Native, but iOS on Swift because that guarantees us a product in market. And we didn't have any React Native apps in market at the time. A year later we launched the iOS version and it was a huge success. And we then spent another six months building the React Native version for Android and everything else. And we realized pretty quickly that React Native was the platform for the future. We were like, oh my God, this will allow us to have one platform. You could run it on the web as well, and we could use the React engineers from the web to work on it. It was a clear winner. By then, we had also launched a shop app, which is React Native.

(01:23:11):
And so we learned a lot about this. And I went back and I said, hey everybody, I made a huge mistake. We just spent a year building this thing. It's in market, but we're going to have to rewrite. We're going to have to rebase back onto this iOS version. And I think I burned 18 months of time with a hundred engineers, literally from the decision I made in the first week of joining Shopify, and Toby, when I went to Toby and I told him, I go, hey man, I think I made this mistake and we have to do this and it's going to cost us a hundred engineers, another six, whatever. And he looked at me and he goes, you should tell everyone this story. That's all he said. Not like, hey, bad, good. He goes, did you learn something? It was an epiphany for me, but he was like, this is a learning org, and I totally failed and I told everyone I failed and my mistake and everything else, but he goes, just tell everyone because he goes, do you know what mistake you made?

(01:23:57):
And first I was like, I don't think, like, what mistake. He's like, you didn't take. He goes, I will always come down harshly on people who do not take risks, and you did not take a risk in this case. But if you take a risk and it doesn't work out, you'll never get in trouble, because you took the risk and it was the right risk to take, but he goes, but you didn't take the risk.

(01:24:16):
And so what I should have done, and by the way, even now thinking back it would be super hard to do, first week at Shopify, right, is take a risk on a platform that we have not launched in production app on, but he was correct in that we should have, because we would've saved ourselves so much more time. So yeah, total failure, sorry. The product is super successful now and we're all on React Native and even the Shop Green app is on React Native. Everything's React Native, and we're core contributors. It's all good. But I literally burned I think 18 months of time for a hundred engineers as my first decision in the company.

Lenny Rachitsky (01:24:48):
This might be the best example of failure coordinator we've had yet. This is a great example. Both of them actually are, although I'm wondering, okay, that felt like a really good decision to me and it's-

Farhan Thawar (01:24:58):
It sounds like it, right? But It wouldn't have been his.

Lenny Rachitsky (01:25:02):
But it's, obviously you don't want to just take risks. There's a limit of a risk but informed, I guess. Is there anything you missed there that would told you this was the right path? Because in hindsight, of course we should have done this, but looking back, what do you think you should have done other than we should have done the risky path?

Farhan Thawar (01:25:19):
Yeah, I mean one thing about my career as well is I don't really do anything halfway. And when I started looking into React Native, it was never just that I'm going, oh, let me look at the docs and read and build a thing. It's like I flew to Meta and met with the React team. I became a core contributor. I ran the React Native working group, like we became release captains for React Native. I knew that I was going to do all the things, so I'm like, and of course in React Native you can also drop down to native and do things there that are not possible. So I think I hedged incorrectly. I knew I was going to do all these things and I should have looked at my own thought process, say, if I do all the things, can I fail? And I didn't take that into account because again, I did five or six.

(01:25:58):
I literally, I put everyone together. I was running the group, I was like release captain. I would hang out with the React team and Meta, we're doing all the things. We became core contributors at React Native before we became core contributors and react because of all the things I was doing. And so I think just knowing that I was going to go all out, I should have said, you know what? This is not going to fail. And I didn't have the confidence in that path, so I hedged, right? Hedging is the worst. And I remember the CTO at the time said, I'm wondering if I should force you to go React Native. He literally said that. And I said, I will do if you say that, I will do it, but it would've been his decision. And so he didn't do it. He didn't tell me to do it.

Lenny Rachitsky (01:26:36):
Okay, that makes a lot more sense. It's so funny that Facebook had a similar mistake early on in their career-

Farhan Thawar (01:26:44):
HTML5.

Lenny Rachitsky (01:26:45):
Yeah, exactly. I know. I don't know if you were at Zuck's interview at the Chase center that the Acquired podcast did, and he talked about this where their market cap dropped 80%. They were about to go public. They went with this app. No one thought they could do mobile ads. And he's like, that set us back a year and a half. He's like, but based on all the pain he's gone through back since then, he's like, that was not too bad.

Farhan Thawar (01:27:08):
Yeah, it's true actually, maybe what people don't know is, I was at Facebook, XtremeLabs, worked on the Facebook app and we worked on that app. I was in the office when we submitted the iOS app every single day that week, because it kept crashing. And we had obviously direct access to people at Apple, but we'd ship a new app on Monday and it crashed ship an app on... Not just us, but us, Facebook together. And so I remember that whole HTML five fiasco from the inside.

Lenny Rachitsky (01:27:36):
I thought you would say you also told Facebook to decide on the HTML5 app to set them back a year.

Farhan Thawar (01:27:41):
I did not. We happened to be there when they were doing it. Yeah.

Lenny Rachitsky (01:27:45):
That's so funny. Amazing. Thank you for sharing that. Before we get to a very exciting lightning round, is there anything else that you think would be valuable to leave listeners with, either touch on something you've mentioned, a last piece of nugget of wisdom, or we just go straight to the round?

Farhan Thawar (01:28:01):
Yeah, I'll say something maybe embarrassing for you. I've been using your performance management framework from your first round review article, not knowing by the way that it was you. I actually found it, you being the famous Lenny podcaster, but the old days, maybe the Lenny, the PM. And I remember reading this a long time ago and just copying, there's a Google link in there to a Google Doc link with a template for a performance review framework that I've been using for years.

(01:28:32):
Literally every review I've done at Shopify uses that framework. And I was writing a post to my admin about how we can use LLMs to make it easier for me to write these reviews, even though obviously you have to read it all and go through it, but I was like, how can I generate some of this with an LLM? And so I wanted to send her the original article. So I went back to the first round review, I found the article and said, oh my God, it's Lenny, the same guy.

(01:28:54):
So I will say one thing that's interesting about that framework is, I've used it now for, like I said, six years here, is that, and I don't think it's me. I think it's actually the framework pulls out good information. I've had multiple people in a review process tell me that, when I deliver the feedback in, of course the format, they would say, wow, I've been in industry a long time. This is the best performance review I've ever had. And it's because the framework pulls out good information. So congrats to you.

(01:29:21):
But I think it was funny that randomly I was coming on this podcast and I just wrote that doc to my admin two, three weeks ago and realized it's the same person.

Lenny Rachitsky (01:29:29):
Well, how about that? I love that. I'll also give credit to a four board guest on this podcast, Vlad Loktev, who was my manager at Airbnb, and that's where I was inspired to write about that framework.

Farhan Thawar (01:29:29):
Amazing.

Lenny Rachitsky (01:29:41):
So it trickles down to him and I don't know where he boarded this, he probably invented it. So credit to Vlad also for that. Another fun fact along these lines, I have another first round of repost about the W framework, which is a framework for planning. They do annual planning. And that's one that I've slowly discovered many, many companies use and they don't know where it came from. They just call it, oh, we have this W framework. Someone flipped it and call the M framework. But that's another one that has trickled into the ether of tech companies, which is awesome.

Farhan Thawar (01:30:10):
Amazing.

Lenny Rachitsky (01:30:12):
With that, Farhan, we have reached our very exciting lightning round. Are you ready?

Farhan Thawar (01:30:17):
I'm ready.

Lenny Rachitsky (01:30:18):
Let's do this. What are two or three books that you have recommended most to other people?

Farhan Thawar (01:30:23):
There's one. So Toby has an annoyingly long set of books that he recommends, and they're all, not all, they're usually good, depends because we're not totally in sync on fiction, for example. But he recommended one to me that I think everyone should read right now called Manna, M-A-N-N-A, from Marshall Brain. It is a book, it's a book about AI. And I think the most interesting thing about it though is about a future in which the AI tells the humans what to do. So it's this idea of, imagine in the future you came into work and the AI would tell you what emails to pay attention to or what dashboard to look at because something weird is going on. It takes that to an interesting level. So I would recommend reading that book. It's not long. That's fun.

(01:31:05):
I think another book that I recommend to people, and it's a weird one to recommend, but it's Business Adventures from John Brooks, the famous, if you ask, I think it's Bill Gates, what his famous book of all time is, it's this book.

(01:31:16):
And the cool thing about the book is that it is not easy to digest for anyone with focus problems. Paul Graham wrote the post How to Do Great Work, and it's super long. The best part about that post is that you have to be able to read the whole thing. And so the same thing with Business Adventures. I think each chapter is, it's 12 chapters, 12 stories, no breaks in between. It's just each one is super long. But it just goes into a problem at such depth that if you can maintain your focus to get through the depths of each problem, you will just learn something, just like that post by Paul Graham.

(01:31:51):
I loved that it was so long because I sent it to people and I said, the test here is can you read it? Can you just get to the end? And not in a pejorative way, like in a... If you can get to the end, you will extract the alpha from this post if you can read it all. So those are... Manna is like the opposite. It's very easy and easy read.

Lenny Rachitsky (01:32:11):
I'm excited to read these. Next question. Do you have a favorite recent movie or TV show you really enjoyed?

Farhan Thawar (01:32:18):
A recent one was Challengers, the tennis movie, with Zendaya just randomly I was at home and I put it on and the cool thing about it was more the cinematography and music. They had this weird style, art house style, where they would be talking and music would get super loud. It was very strange, but a very, very good movie. And then you saw, you said movies and-

Lenny Rachitsky (01:32:40):
Or TV show. Oh, TV show, anything like that.

Farhan Thawar (01:32:42):
Yeah, one of my all time favorites is probably Halt and Catch Fire. I don't know if you've watched that.

Lenny Rachitsky (01:32:47):
About the early tech industry.

Farhan Thawar (01:32:48):
Early tech. And I think there was an Andreessen podcast where he said this is the closest thing to what a real startup looks like. So Halt and Catch Fire like an all time recommend, everybody has to watch it.

Lenny Rachitsky (01:32:59):
Do you have a favorite product that you recently discovered that you really love?

Farhan Thawar (01:33:03):
I don't know if I want to be in the zeitgeist right now, but the Meta Ray-Bans are amazing. And the biggest thing about the Meta Ray-Bans was just that I think I never got into it and I saw people around me wearing it, but I only got into it when somebody said I'd never take my AirPods with me anymore. And I was like, oh, I can swap two devices for one device. I always have sunglasses and AirPods because I'll go for a walk or listen to a podcast and now I can just have one device.

(01:33:26):
And this happened to me. I was in the summer, I was at a pool party and someone called me and I just took it from my sunglasses and people were confused as where I was taking this call from. But they are the right amount of tech. They're in unintrusive, you can't tell, they don't look like any tech. And then also I was playing soccer with my kids. I have three kids. I just turned the video on and I was the goalie and they were taking shots and I was watching them. They had no idea that I was just recording. And it was such a cool moment because I was in playing soccer with them. I wasn't with my phone and I got to get this amazing set of video that I would never would've gotten. So I really liked the Meta Ray-Bans.

Lenny Rachitsky (01:33:58):
We had Boz on the podcast who leads a lot of that work and he's got a to teach us. And I put on Ray-Bans while we were doing the interview just for fun. You could see my setup. Okay, cool. Two more questions. Do you have a favorite life motto that you find useful in work or in life?

Farhan Thawar (01:34:15):
Okay, I do. And it's on a lot of my profile bios, and it is, everything you know is wrong. And the reason I like that one, and people always like, what would you put on a billboard? And people always come back to me and say, that's like they know that as my motto.

(01:34:32):
And the reason for that is it's this notion of if all the knowledge you knew was incorrect, could you from first principles build up a view of the world? And that's kind of how I like to think of things is that, anything could be incorrect. Even things that you think are correct, which is why, again, back to the, I like to experiment. I like to look stupid, because I'm always trying shit because I'm like, I don't know if even though you say this is correct, that this is going to work, right.

(01:34:58):
Actually, one example, my wife hates this is I have a Tesla and I routinely will switch gears without fully stopping the car, which you cannot do in a regular car, but I'll be in drive and then I'll slow down to drive back up into my driveway and while it's moving I switch it into reverse.

(01:35:14):
And you never would know that that's possible except for trying. And sometimes it goes beep beep because you're going too fast. And she hates it. But I'm always trying weird things and so that's why I say everything you know is wrong. Who knows what's possible, just try different things.

Lenny Rachitsky (01:35:29):
I do the same thing with my Tesla. I used to do it with a non-electric car and my wife is always like, don't do that. Screwing it up.

Farhan Thawar (01:35:34):
Yes, exactly.

Lenny Rachitsky (01:35:35):
I love that on an electric car, there's no gear you're breaking, it's just software.

Farhan Thawar (01:35:39):
Exactly.

Lenny Rachitsky (01:35:41):
This quote reminds me of that you shared of everything you know is wrong. The founders of Airbnb always talked about just this point that everything around you was designed somebody, another human. There's not necessarily that much smarter or insightful. It doesn't mean what they did was correct. Somebody else find some better potentially...

Farhan Thawar (01:35:57):
I think Steve Jobs had a similar thing like, hey, you can design anything. Everything's designed by people. I love that one too.

Lenny Rachitsky (01:36:03):
Yeah. Final question. So you told me the story of this PhD you hired versus just a guy you met in a college, sorry, in a coffee shop. I read another similar story where you hired a waitress.

Farhan Thawar (01:36:14):
Yes.

Lenny Rachitsky (01:36:14):
Is that real? Okay, tell that story.

Farhan Thawar (01:36:17):
Yeah, so again, this is another long list of reasons my wife is in annoyed with me, but this is another one of them. Whenever we are out, I'm always scanning and I'm always scanning people and one, do I know anybody around, whatever. I like to scan for people and I have a good memory for faces. But in this case we were at a restaurant and I saw a waitress doing a very, very good job, an extremely, like she was running between different tables, she was smiling her face, taking everyone's order, making sure that there was a thing happening in the kitchen. She was kind of doing a phenomenal job of organizing the entire crazy busy restaurant. And so in talking to her, I said, what do you do outside of this because you look like you're super. She's like, what do you mean? I'm just the waitress.

(01:36:59):
And I said, well, would you like to, this is XtremeLabs. I Said, would you like to work at XtremeLabs? She's like, what's that? So I explained it to her and I got her contact info. She came into the office and she first started off as our receptionist, so she moved from the retail world into the office world, and then I brought her on as my admin and she became one of my recruiters. And I taught her how to recruit and talked to people and she came in with me to info sessions. And over time we actually hired many more people from the restaurant that were really, really good at their job. And what was amazing was, one, she was organized but not reorganized. I had to teach her at Google Docs and G Suite and everything else, but she was super smart but just never had the opportunity.

(01:37:35):
The coolest thing about this is that she ended up being, she ended up taking over one of the HR functions for us. And she had a college degree and because of the work she had done with us, she was able to parlay that into finishing, doing one more year and getting a university degree. And now she's a director of HR at a company, which is amazing from, like, she went from that environment to this environment and a lot of her people, she pulled the smart and intense people she pulled from that environment also ended up on these amazing career paths. If I see someone doing a good job, I'm like, what do they do? How can I work with them? This is one example of pulling somebody out of that environment. I have lots of other ones where I overhear someone in their designer or an engineer and I try to hire them into my company as well.

Lenny Rachitsky (01:38:22):
Wow. That is such a good story. I love that. Maybe restaurants are the new feeder system for tech companies. Did not think about that.

Farhan Thawar (01:38:31):
Yeah, I mean, everyone's smart at something, so I was trying to figure out, she was really good at this thing. She'd be so good at something else.

Lenny Rachitsky (01:38:36):
Amazing. I feel like there's so many stories, more stories to tell, but we're going to wrap it up and let you go, farhan. Two final questions. Where can folks find you a line if they want to reach out, learn more, maybe apply to work at Shopify and how can listeners be useful to you?

Farhan Thawar (01:38:50):
Sure, so Twitter's probably the place I try to hang out the most, X at FNThawar, and maybe I'll put that in the show notes. And then listeners for me. I mean, I love to be challenged. I'm sure that there are people who are like, they heard something that I said and they're like, oh, that's super dumb. We do this instead. Or here's research that says that that won't work. I would love to hear more about these because I'm just again, on a learning journey and if I did something stupid, very likely I would like to learn a better way to do things. So I would love for people to comment and say, hey, this is dumb. You should try this, or, that doesn't make any sense. I would love to learn more. So that's what I'm looking for.

Lenny Rachitsky (01:39:25):
All right, well leave a comment in YouTube or on the Substack post with what Farhan got wrong.

Farhan Thawar (01:39:31):
Amazing.

Lenny Rachitsky (01:39:33):
Thank you so much for being here. Thanks for having me. Bye everyone.

(01:39:38):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

