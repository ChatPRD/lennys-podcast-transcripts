---
guest: Brian Tolkin
title: Lessons from scaling Uber and Opendoor | Brian Tolkin (Head of Product at Opendoor,
  ex-Uber)
youtube_url: https://www.youtube.com/watch?v=sRukk520Fds
video_id: sRukk520Fds
description: 'Brian Tolkin is the Head of Product at Opendoor. Previously, he was
  one of the early employees at Uber, where he was instrumental in launching and growing
  UberPool, UberHop, and UberExpress...

  '
duration_seconds: 4480.0
duration: '1:14:40'
view_count: 11209
channel: Lenny's Podcast
keywords:
- growth
- acquisition
- onboarding
- metrics
- roadmap
- iteration
- a/b testing
- experimentation
- data-driven
- analytics
- funnel
- pricing
- team building
- culture
- strategy
---

# Lessons from scaling Uber and Opendoor | Brian Tolkin (Head of Product at Opendoor, ex-Uber)

## Transcript

Lenny Rachitsky (00:00:00):
You've worked at two businesses that have done incredibly well combining product in ops.

Brian Tolkin (00:00:03):
Uber always has this mentality and Opendoor does two of the product operations, twin turbine jet plane where you can fly the plane on one engine for a little bit if you need to, but it's operating most efficiently and effectively if both are working together.

Lenny Rachitsky (00:00:17):
What has having been in ops done to make you a better product leader?

Brian Tolkin (00:00:21):
Gave a really deep understanding of how the business actually works. It's a pretty good foundation for them going on to say, okay, what do we actually want to build in a more scalable technology way.

Lenny Rachitsky (00:00:31):
Something else I've heard that you're very good at is staying very calm under pressure.

Brian Tolkin (00:00:34):
I've slept on the floor in China before launching uberPOOL, and when you reflect the stress onto your teams, everybody tenses out. It counterintuitively doesn't produce better outcomes.

Lenny Rachitsky (00:00:51):
Today my guest is Brian Tolkin. Brian is currently head of product and design at Opendoor. Before that, he spent nearly five years at Uber where he joined as employee 100. Before Uber had UberX or uberPOOL or any shared rides, he actually started on the ops team at Uber, moved into product, ended up leading product and launch of uberPOOL, and then taking it global. He also started the product operations function at Uber. Before that function was really even a thing, which I didn't know until the chat that we had. In our conversation, Brian shares a ton of lessons about building products with a heavy operational component. Also, how to run great product reviews, how he implements the jobs to be done, framework and Opendoor's successfully.

(00:01:32):
The story behind Zillow trying to compete with Opendoor failing and then partnering instead. Plus a ton of great stories from the early days of Uber and Opendoor, and so much more. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing feature episodes and it helps the podcast tremendously. With that, I bring you Brian Tolkin. Brian, thank you so much for being here and welcome to the podcast.

Brian Tolkin (00:02:00):
Thank you, appreciate it. Thanks for having me.

Lenny Rachitsky (00:02:02):
First of all, just a huge thank you to Kayvon Beykpour for connecting us, introducing us. He said all kinds of amazingly nice things about you. He also gave me some very hard questions to ask you. I hope you've come prepared.

Brian Tolkin (00:02:12):
Terrific. Put me in my hot seat.

Lenny Rachitsky (00:02:14):
Okay, I want to spend a bunch of time talking about product and ops. You started your career in operations. At Uber you actually started on the ops team and you moved into product. You've also worked at both Uber and at Opendoor, which have both huge operational components. I think it's really rare that people, one, see a company scale to the heights of Uber and Opendoor with such a heavy operational component that are still tech companies and also it's really where someone starts an ops and then moves into product and ends up where you are, where your chief product officer, really successful company. So I have a bunch of questions here. Maybe the first is just what has having been in ops done to make you a better product leader? How does that change the way that you operate as a product leader?

Brian Tolkin (00:02:58):
Starting on the operations side gave a really deep understanding of how the business actually works. You are truly operating it day in and day out and the success of the city is in large part driven by the inputs that you are putting into it every single day on the ground and whether or not there was rain that weekend, which was a nice driver of metrics, but talking to customers every single day like one-on-one onboarding drivers responding to support tickets, there's no centralized support team, there was no closer to the customer, right? And so I think that foundation actually for really understanding what moves the business and being super close to the customer actually is a pretty good foundation for them going on to say, okay, what do we actually want to build in a more scalable technology way?

Lenny Rachitsky (00:03:52):
This episode is brought to you by Pendo, the only all-in-one product experience platform for any type of application. Tired of bouncing around multiple tools to uncover what's really happening inside your product? With all the tools you need in one simple to use platform, Pendo makes it easy to answer critical questions about how users are engaging with your product and then turn those insights into action. Also, you can get your users to do what you actually want them to do. First, Pendo is built around product analytics, seeing what your users are actually doing in your apps so that you can optimize their experience. Next, Pendo lets you deploy in-app guides that lead users through the actions that matter most.

(00:04:31):
Then Pendo integrates user feedback so that you can capture and analyze what people actually want. And the new thing in Pendo, session replays. A very cool way to visualize user sessions. I'm not surprised at all that over 10,000 companies use it today. Visit pendo.io/lenny to create your free Pendo account today and start building better experiences across every corner of your product. PS, you want to take your product led knowhow a step further? Check out Pendo's lineup of free certification courses led by talk product experts and designed to help you grow and advance in your career. Learn more and experience the power of the Pendo platform today at pendo.io/lenny.

MUSIC (00:05:09):
Pendo.

Lenny Rachitsky (00:05:15):
This episode is brought to you by Explo, a game changer for customer facing analytics and data reporting. Are your users craving more dashboards, reports and analytics within your product? Are you tired of trying to build it yourself? As a product leader, you probably have these requests in your roadmap, but the struggle to prioritize them is real. Building analytics from scratch can be time-consuming, expensive, and a really challenging process. Enter Explo. Explo is a fully white labeled embedded analytics solution designed entirely with your user in mind. Getting started is easy. Explo connects to any relational database or warehouse and with its low-code functionality, you can build and style dashboards in. Once you're ready, simply embed the dashboard or report into your application with a tiny code snippet. The best part, your end users can use Explo's AI features for their own report and dashboard generation eliminating customer data requests for your support team. Build and embed a fully white labeled analytics experience in days.

(00:06:18):
Try it for free at explo.co/lenny. That's E-X-P-L-O/lenny. I've seen that a lot of companies, and this was definitely true to Airbnb, where the product team looks down a little bit on the ops team where they're like, "oh, we're doing things that are going to scale to millions of users. We're doing these things that are going to apply to everyone." There's this ops team over there doing a few things that are going to not scale. They keep asking us for things to build for their one-off ideas. What do you think that product teams often maybe miss or don't understand about the ops teams that would help them see them in a different light?

Brian Tolkin (00:06:56):
Yeah, it's a great question and I think Uber always had this mentality and OpenDoor does too of like a twin turbine jet plane where you can fly the plane on one engine for a little bit if you need to, but it's operating most efficiently and effectively if both are working together, and I think that's really true, right? The reality is operations teams, local teams, can iterate faster, can scale talking to customers really much more efficiently, have great qualitative insights, and so if it's seen more as a harmony instead of a competition, I think that's really, really helpful where it's like, okay, how do we get the insights that are happening day in and day out in the field, on the ground, whatever that may be, and help us build better products because of that, right?

(00:07:50):
Like a PM sitting in San Francisco can't be in Opendoor's case 50 markets, walking houses every single day in Uber's case, whatever, a thousand cities understanding the nuances of safety in South America and it's just not possible, but what you can do is foster a really good relationship and a really good feedback loop of how people who do deeply understand those things can help give insights. Now is actually the birth of product operations was that insight as well.

Lenny Rachitsky (00:08:22):
Can you say more on that?

Brian Tolkin (00:08:23):
Yeah, sure. So, sorry, I should probably define what product operations was. At Uber it was basically this notion that we had centralized, this was later in my career at Uber, but we had a centralized product team building stuff mostly in San Francisco, not strictly through the Ross, but at this point around the world, but mostly in San Francisco and then we had a very globally distributed operations team, and there was a bidirectional feedback loop that wasn't super strong and that feedback loop was basically when the EPD teams in San Francisco built new features, how do we effectively put it in global markets and then how do we effectively get input from global markets to better build features. And so one solution to that problem, our solution at the time was to start up a new function called product operations who had accountability and reported into operations but physically sat with and operated much like a member of the product team to help solve that.

Lenny Rachitsky (00:09:23):
Is that maybe the first time there's a... Did you invent product operations as a function?

Brian Tolkin (00:09:28):
I don't think so because at the time, I believe Google had a function, I can't remember what Google called it was something slightly different, but I met with a few folks who had been in similar type roles at Google and a couple other places, so I don't take credit for certainly for inventing IT and other people have actually dabbled in this model at Uber before me there was just a formalization of it and our actual building out of the organization, et cetera.

Lenny Rachitsky (00:09:54):
Did none of that. Sounds like you basically helped make it a thing. I know you're being very modest, I think. Coming back to your point about decentralized operations teams, something I've read is that search pricing came out of one GM and a market just testing, emailing all the drivers, hey, we're going to give you extra if you drive on Saturday night. Is that true?

Brian Tolkin (00:10:15):
That would've been probably a little bit before my time, but that being said, one thing that is true is that surge pricing for actually quite sometimes all of 2012, certainly 2013 probably, I don't know when we necessarily switched, was very much a human in the loop system or a very manual system where GMs in every city would control basically the parameters in which surge would operate and so much of the time that would need, for example, Monday through Friday, there would be no search, it couldn't flip on, and then Friday nights and Saturday nights it would flip on from whatever you set, 7:00 PM to 3:00 AM and the cap was X, whatever the cap was. And then within those parameters the algorithm would optimize for what the price was. But yeah, GMs controlled whether it was on or off and what geographies were surging.

Lenny Rachitsky (00:11:16):
Wow, I didn't know that. Was that out of we believe we are better than the algorithms or we just don't have time to make them amazing yet, so we're just going to help them along?

Brian Tolkin (00:11:25):
Yeah, I think it was probably a function of a bunch of stuff, one of which is like, hey, this is a fairly new concept and it's powerful and dangerous and so let's make sure we understand what's happening. The second is this belief that local city teams know their cities best and so you might know that an event is happening, a baseball game gets out and it's like, oh, I know that this baseball game's going to get out at 10:00 PM so I'm going to set surge at 9:45 and the algorithm may not be able to pick that up. And then the third is the technical constraint of nowadays clearly it's all automated, but it's really hard to build a fully dynamic, always on geospatially aware pricing system and not just a little bit of time.

Lenny Rachitsky (00:12:17):
That makes sense. I feel like you're full of wild stories from your time at Uber. Is there one that comes to mind of just, I think you helped scale in China, uberPOOL?

Brian Tolkin (00:12:17):
Yeah.

Lenny Rachitsky (00:12:29):
Maybe that's the one. I don't know. Can you share wild story from early Uber days?

Brian Tolkin (00:12:31):
Yeah, so in the early days of Uber, one fun story is obviously UberX is a random mainstream product but has a funny, silly name, UberX. This product in the early days was going to be all hybrid and had a bunch of different potential names. I was not personally driving this, this was someone else on the operations team, but they built the model for what this product could be and there's no name for it yet, so it was going to be a placeholder. So what do you put in some placeholder? X. So UberX and then the company was moving quickly enough, the product got the green light, it launched, and here we are, I don't know, 12 years later, 11 years later, whatever it is and UberX is the name that stuck.

Lenny Rachitsky (00:13:21):
That is hilarious. I love it. So it was a placeholder. It's like many products start that way where they're like, this is just the temporary name, and they're like, okay, I guess everyone just knows it this way now we're going to stick with it.

Brian Tolkin (00:13:31):
Exactly. It's too expensive to change and rebrand at this point.

Lenny Rachitsky (00:13:34):
That's an awesome story.

Brian Tolkin (00:13:36):
One that is good about scaling Uber uberPOOL in China is we were launching Uber pool in China and this was going to be, China at the time was pretty big for Uber, but uberPOOL was not there yet, and so we were going to launch. And myself and a few other folks were in Chengdu China, which is the first Chinese market that we were launching uberPOOL in and we were going to be on the ground took to launch. We wanted to go live at, I believe it was 6:00 AM for rush hour on, I don't remember the day, but whatever, Monday morning, and so we're there over the weekend getting ready to set up and at the same time we were doing some data center testing. And so we flipped on all the testing infrastructure and thought it was going to work and nothing works, and the matching algorithm just isn't working and we're like, oh my god, now it's whatever, 5:00 PM the day before we're supposed to go live, 6:00 PM, 7:00 PM okay, let's get on the phone with the US, try and figure out what's going on.

(00:14:43):
I remember I slept about 30 minutes that night between 2:00 and 3:00 AM being like, okay, well, we have to go live at 6:00 AM I think there was some press around it. We were planning on going live and I think we got everything finally working at probably about five 30 or six in the morning and launched just in the nick of time. And I'll never forget, we launched, it was great, we monitored, everything was good, and then we walked out for breakfast at 7:30 in the morning. Everyone sleep depressed, no one slept all night and we got these pancakes street food things and I have to imagine they were not that good, but in my mind it was the best meal I've ever had in my life.

Lenny Rachitsky (00:15:25):
It's like a meal after a marathon or a big hike.

Brian Tolkin (00:15:31):
Exactly. Yeah, exactly.

Lenny Rachitsky (00:15:32):
Everything's so delicious. This comes up a lot of just these moments that are so incredibly stressful and hard and leap deprived end up being the best memories and the best stories to tell and things you look back at fondly. It's so weird how human nature is like that.

Brian Tolkin (00:15:46):
Yeah, I mean another one more recent for Opendoor was when COVID hit, physically we buy and sell homes, and so we were physically going into people's homes and suddenly March 2020 going into people's homes was not something people were comfortable with. And you look at the real estate data coming out of China at the time and it looked like coming to a standstill, and so we actually turned off the core business and we stopped buying homes for a few months. hey, we can't go in and we don't know if anyone's going to be buying any homes, and so what do we do? And we took those few months and then came out the other side and had virtualized the whole process. Then it was pretty stressful, right, because looking at a business that relies on going into people's homes and suddenly you can't do that anymore, what do you do? So, again, a fond memory to look back on a very stressful time in the moment where it feels very, very difficult.

Lenny Rachitsky (00:16:51):
Just since you mentioned Opendoor, I think many people have heard of Opendoor. Maybe just give a quick explanation of what Opendoor does for people that aren't exactly sure.

Brian Tolkin (00:16:58):
So we're a digital platform to buy and sell real estate. The core product today is a seller focused product where people can go online, enter some information about their home, and we'll make an all cash offer to be able to sell simplicity and certainty. So the product really works for people who want something that is certain and simple and easy. I don't know if you've ever sold a home, but it can be a very, very, very successful difficult process with showings and open houses and how to price it and will it sell and all of that stuff. And so we offer basically a way to skip the whole process.

Lenny Rachitsky (00:17:41):
So you basically sell your house to Opendoor and it's just like, cool, done, move on.

Brian Tolkin (00:17:45):
You picked your closing date, you move out when you want. Yeah, there's no hassle.

Lenny Rachitsky (00:17:53):
Sounds amazing. I want that. Coming back to ops and product, just to close this thread again, you've worked at two businesses that have done incredibly well combining product and ops. Are there any just broad lessons you've taken away from how to make these two teams and functions work well together and to build a business that's very ops heavy but also offer driven?

Brian Tolkin (00:18:15):
The first one we touched on, which is a, there's just got to be mutual respect. Both functions have their time and their place and their skillsets, and you just don't build big businesses of this type without respecting the fact that that both need to exist. The second, particularly on the product and engineering side, is really understanding where and how the technology leverage comes from the business and then being really focused on making sure generally, especially in the earlier days, you are more limited on the technical resourcing side than you might be on the operational resourcing side. And so how do you be really focused on where to invest your time, effort, and energy technically, which is why most of the engineering effort for Uber was on the dispatching system and the pricing system. That's just where the leverage was at the time, given the scarcity of resources.

(00:19:11):
And so I think the second one is being really intentional about where those techs are and then being really forthcoming and saying, hey, that means all these other places where yes, it can make things easier, more efficient, et cetera, et cetera. We are okay not investing in right now, and that needs to be an explicit decision and very transparent. But then the last bit I would say is a deep understanding that the real world has entropy and it's hard and it's messy for us at Opendoor, we go into homes, someone may not be home, scheduling may be off, at Uber the driver may cancel the radio GPS. All these things happen, right? Computers are deterministic, but humans aren't, right? And so building products that have a little bit more flex or a little bit more fail safes in case those things happen becomes a little bit more of a paramount.

(00:20:08):
One other thing, the last thing I would say is I think that the companies evolve as well. So what I talked about at the beginning of Uber being very focused from an engineering and product side on the dispatching system and the pricing system, obviously over time not to evolve now it centralized all of these functions as the company got bigger and more mature and scale and optimization started to be more important and expansion and that Petri dish of trying new stuff and the tools got better and the tech got easier and there was more internal infrastructure. And so over time things can start one way and shift over time as the business needs.

Lenny Rachitsky (00:20:52):
Let's actually spend more time there. You keep saying things that make me want to dig deeper. So at Airbnb we went through the same thing where there was all these local ops teams driving supply, finding homes, bringing out the platform, and then there's this tipping point where the product in organic growth or word of mouth ended up driving more and then orders of magnitude more. So there was no need for these folks to spend time doing these things. Can you just maybe share an example, either we Opendoor, when you talk about there's a time and a place and a skillset for ops, how that evolved? What was the team doing initially and then what did they end up doing as things grew?

Brian Tolkin (00:21:25):
Yeah, I mean, maybe a very easy good example to pick just one part of the Uber process in the early days is at small scale, actually back when it was Uber black drivers, every driver was individually onboarded in a 90 minute to a two-hour in-person in the office onboarding with deep setting of expectations. The next version of that... So that's obviously very ops driven. The next version of that is a small classroom type setting of three or five or six drivers at a given time. Also, very ops driven. And then as we got into more mass market products like Uber Taxi or UberX, it was like, okay, maybe 20 or 30 at a time. So now it's a little bit bigger classroom setting. And we said, okay, let's make a video. Instead of giving verbally the same presentation, let's just make an onboarding video and that was the next set of scale, but now suddenly we have a different problem, which is okay, you have to validate all of these credentials.

(00:22:32):
So most driver's license who they are, all that stuff at one person, easy at three to four at a time, easy, 10 at a time, a little more challenging but fine. At 20 at a time, okay, you're starting to run up onto it now you fast-forward six months and you're doing a thousand a week or whatever, suddenly your system breaks and it's like, okay, we have reached the point where operational system improvements is no longer viable. So, you say, okay, we have gone from the iteration stage to the scale stage and technology is uniquely good at scaling. So now we say, okay, instead of having a bunch of folks around the world taking pictures of driver's licenses and validating and doing all that stuff, how do we integrate with some type of OCR technology or auto recognition of driver's licenses that feeds to a system that knows what a driver's license is or can do automatic validation and suddenly you've done two things.

(00:23:27):
One, you've scaled your system, and two, you've just created a ton of time for what at the time was probably dozens if not hundreds of people running these onboarding sessions all over the country, the world at the time to do other stuff. And so now you can level that up and say, okay, do we do more analytics? Do we do more figure out the next process that needs optimization or whatever the case may be in that virtuous cycle just continues.

Lenny Rachitsky (00:23:53):
The way I like to think about this is do things that don't scale and then scale the things that you're doing. That's the phrase I always come back to.

Brian Tolkin (00:23:58):
Exactly.

Lenny Rachitsky (00:24:00):
This reminds me of a hot take that previous podcast guest shared in a newsletter post Casey Winters. He talked about that operations is usually, and it's a hot take, that operations is a sign of inefficiency and over time your job is to squeeze that away and make it product software as much as possible. Doesn't mean you always get there. Thoughts?

Brian Tolkin (00:24:23):
Yeah, I actually don't. Fundamentally, it depends on what the operations is, but I don't fundamentally disagree, but I think that the right lens to think about it is... And then those folks can move on to the next challenge. And so there's always another hill to climb. And so I think that was one of the things at Uber and Opendoor where there's this culture of on the ground experimentation that's really helpful where we were just talking about driver onboarding may now be solved with technology so you have a few extra hours a day. How do we get better at optimizing the UberX system? How do you start tinkering with food delivery? How do you start thinking about higher capacity vehicles? How do you think about better feedback loop for those manual surge pricing toggles that we talked about? So I generally agree it just generally free across and solve more problems.

Lenny Rachitsky (00:25:21):
It feels like a big part of this is making sure the operations teams understand there's more opportunity, even if this ends up being automated, your job is not going to go away. We're going to find something new to try and experiment and do things that don't skip.

Brian Tolkin (00:25:34):
Yep.

Lenny Rachitsky (00:25:34):
Awesome. Okay. Going a completely different direction.

Brian Tolkin (00:25:37):
Great.

Lenny Rachitsky (00:25:38):
I hear you're very good at product reviews.

Brian Tolkin (00:25:40):
Okay.

Lenny Rachitsky (00:25:41):
A few people told me this. I'm curious how you set up a product review and any things you've learned, any tips for how to run an effective product review?

Brian Tolkin (00:25:48):
That's very whoever mentioned that. But yes, big fan of doing them actually in particular to maybe bridge the conversations in companies that have ops driven cadences or start out very ops driven because the cadences can sometimes be different. And so the operational cadences that you might have something like a WVRA weekly business review may not be conducive to always picking your head up and saying like, Hey, where's the product going on a slightly longer timeframe. And so I think product reviews in general for all companies are probably really helpful, but actually in particular for some of the product and operations led companies. In terms of things I've learned, I think being really intentional about what the goals are, I think it's okay to say that there are two goals, a goal of accountability and inform to an audience.

(00:26:43):
But also most importantly, I think this is the primary goal is to help make the product better, to help the teams think through a problem and to have that, again, back to our earliest conversation, be a very intellectual conversation about the work and how to make the product better and not super scary. Product reviews hopefully are not feeling like firing squads. That's a scary environment to be in and not necessarily one that's conducive to how do we make the product better. Obviously sometimes the conversations have to get a little intense, but in general that's what we're shooting for is something that helps the team go back and think through how to make the product better.

Lenny Rachitsky (00:27:24):
So the two goals you try to communicate for your product reviews, accountability slash informing people what's happening, but also just like we are here to make the product better and setting that context. Yep. Is there anything you'd do specifically to make it not feel like a firing squad? Like you're coming in here to be attacked and criticized? Do you set context at the beginning of the meeting? Is this just a part of the culture?

Brian Tolkin (00:27:43):
Yeah, I think definitely part of the culture, but also I am a firm believer in general that the people closest to the problems also have the best context to solve that problem. And so as a more senior voice in the room, often the job is probing, asking questions, throwing out ideas in a way that says like, hey, this is an idea. This is not a mandate, this is a thought. And if there's context missing that would inform the product direction, then providing that context in not a question asking sense, but hey, this is context that you might not be aware of. And so I think it's all in how you show up as a leader and what that looks like in terms of probing and pushing the team on dimensions that they may not be thinking about. And then understanding that the team is bringing a perspective that you don't have, which is they think about this problem 40, 50, 60 hours a week, and you might think about this problem three hours a week. So you bring them a breath, the team brings a depth in haven't been there yet.

Lenny Rachitsky (00:28:49):
I don't know if you heard Dharmesh Shah's episode or his thing on flash tags. Have you seen this?

Brian Tolkin (00:28:54):
I have not, no.

Lenny Rachitsky (00:28:55):
Okay. He has a whole system. So you talked about how as a leader you want people to not take everything you tell them as feedback as I need to do this. So he has a whole set of hashtags that communicate how important this is to him from hashtag FYI to suggestion, to a plea.

Brian Tolkin (00:29:13):
Yes.

Lenny Rachitsky (00:29:14):
A plea to you.

Brian Tolkin (00:29:17):
This was actually explained to me. I don't think I've seen the original source, so I'll go back and watch it, but this was explained to me as I'm actually a big fan. I think that's great.

Lenny Rachitsky (00:29:26):
Yeah, just get everyone on the same page. Okay. Maybe one last question here. Who do you try to invite to product reviews? Do you have any frameworks and ways of thinking of who to invite, who not to invite?

Brian Tolkin (00:29:36):
Yeah, good question. We, I would say have oscillated over time, but in general, big subscribers of the best conversations happen when they're relatively small, so try and keep it under 10. Could be wide distribution of the document. The artifacts created are actually really powerful and they're powerful for the whole team to understand. And secret power is they're very powerful for new people who are onboarding to be like, here are the last 20 product reviews, you'll get a pretty good idea of what's going on. But generally the conversation itself try and be relatively tight. We try to keep it under 10.

Lenny Rachitsky (00:30:15):
And these artifacts, you mean the recordings of the meeting that people can watch or?

Brian Tolkin (00:30:20):
Yeah. Or just the document depends on what the company culture is, whether you want to record it or just have the document either way.

Lenny Rachitsky (00:30:26):
And then is there some specific cadence you operate on? Is it like a weekly product review that people can sign up for? Does every team, how do you like to set this up the cadence?

Brian Tolkin (00:30:35):
Yeah, obviously it scales are with the size of the company. For us right now, what's working well is signup cadence. We have two slots a week that anyone can sign up for as their product area needs it. And then if there's something that we would love to see that we haven't seen in a bit, we do a little bit of all in telling to make sure that the work is generally cycling through on a quarterly basis.

Lenny Rachitsky (00:30:59):
This episode is brought to you by Attio. A radically new type of CRM. There's a world where your CRM is powerful, easily configured, and deeply intuitive. Attio makes that a reality. Attio is built specifically for the next era of companies. It syncs with your data sources, easily configures to their unique structures and works for any go-to-market motion from self-serve to sales led. Attio automatically enriches your contacts, syncs your email and calendar, gives you powerful reports and lets you quickly build Zapier style automations. The next era of companies deserves more than an inflexible one size fits all CRM. Join modal, replicate 11 labs, and more, and scale your startup to the next level. Head to attio.com/lenny and you'll get 15% off your first year. That's A-T-T-I-O.com/lenny.

(00:31:54):
Adjacent topic. I hear you're a big fan of drops to be done, which is okay, so it's a fun recurring topic on this podcast. We've had many people that love it, many people that hate it. I love seeing both sides of it. I love that you find it helpful and you implement it at Opendoor. I'd love to hear just how you actually apply it at Opendoor, what you've learned about how to apply jobs to be done effectively.

Brian Tolkin (00:32:17):
Yeah. I think like all frameworks, the right answer is to pick your set of frameworks, have more tools in your toolbox, and then actually understand when and how to apply them. So we try to avoid being a hammer and everything's a nail. We try to for course the framework if it's not working. But I think what I really like about it is it forces you to put yourself in the customer's shoes. I think in a slightly deeper way and be a little bit more empathetic when I think about building at Opendoor versus say building at Uber or when you are building at Airbnb is we are not... Most people at Opendoor, we don't have homes to sell every week or every month, nor do we buy homes every week or every month. On average in the US is something people do once every seven years.

(00:33:10):
I'm sure the average at Opendoor is something similar, and so it's a little bit harder to be a customer. I took Uber every day. You probably use Airbnb a number of times a year. And so in some sense for some of those companies, you can bill for yourself, you would intuit the job to be done because you're just doing it for yourself. We don't necessarily have that context. And so a framework that forces us to be really thoughtful and intentional about how a customer might perceive our product is really helpful. The other thing that I like about it is the canonical version of it encourages you to think about the context in which the user's operating or the other things outside of your product that they might be going through.

(00:33:59):
And in our case, the home buying or selling journey often is a certainly multi-week, if not multi-month or multi quarter journey with a lot of complexity and a lot of conversations outside of our product. You may be talking to an agent, you may be talking to a friend, you may be driving around the city trying to find a house, and the framework is very flexible and encouraging of saying what is actually the job to be done of this user when they're thinking about our product and what is the context in which they're operating.

Lenny Rachitsky (00:34:29):
I'd love to go one level deeper to talk about how you actually implement it. Do you have templates of, you have a startup project as a blank, I blank, blank, blank? How do you...

Brian Tolkin (00:34:40):
I would say we're medium rigorous on template standardization or adherence. So we do have a template, the standard product review template talks about jobs to be done and has a section for what is the problem statement and what are the jobs to be done.

Lenny Rachitsky (00:34:58):
And this is a doc that when you're coming to a product review, the person running it and coming is filling out this document?

Brian Tolkin (00:35:04):
Correct, pre-filling it up, sorry, pre-filling it out. And again, I think we are not sticklers about always using that template, but I think the beauty of a template is yes, it sets expectations of what you expect, but it's also just easier often for people to be able to work off something. And so yeah, it's part of our product review template and then part of our planning process as well. Because we've used it for a while. I think there's been an internalization of the culture where people will also just start commenting about it or writing about it and saying, hey, what is the job to be done here? Or what is the user trying to do? Which is maybe another colloquial phrase in it. And so, yeah, I think there's a cultural seeping that has happened.

Lenny Rachitsky (00:35:49):
From memory, just what is in this template. So what's the phrasing that you try to use for setting up a problem?

Brian Tolkin (00:35:55):
Yeah, yeah. I mean, the specific framing, I would have to go remind myself on the template itself, but generally it looks like context, problem, potential solution, risks, risks/premortal and measurement of success. And then we also try to bucket our product reviews by stage. So you could be in the ideation stage, which might look very different than at the very end of the process. Like, Hey, we're getting ready to ship speak now forever hold your piece. Those two artifacts will also be very different.

Lenny Rachitsky (00:36:35):
Okay. So it's not as a blank the standard jobs to be done language, it's not exactly how you implement it's more just make sure we're thinking of it what is the problem for the customer? What is the context of their problem?

Brian Tolkin (00:36:47):
Correct. Yeah. Yeah, we're not math living our template.

Lenny Rachitsky (00:36:52):
Okay, awesome. Any other tips or lessons about just working well with this concept of jobs to be done? Maybe when you come into Opendoor and like, hey everyone, we're going to be thinking this way. Is there anything there that would be useful to people if they're trying to operate this way?

Brian Tolkin (00:37:06):
Recognizing that correctly implementing a framework, any framework, but if you don't in particular, we can talk about takes a little bit of time and getting used to and understanding. And so I don't think you can just like, okay, we're going to make the template and then that makes the content better. That just takes people's content and they wedge it into the template. It's actually the cultural internalization of like, hey, this might be phrased as the job to be done, but is this actually the job to be done? Let's talk about why the customer might be in that situation or not be in that situation. Or I think the job to be done might actually be something else.

(00:37:43):
Or you might say, hey, the job to be done is maybe an early day version would be the job to be done is to get an offer from Opendoor. And it's like, well kind of, but the broader job to be done might be price discovery for the customer. And so you can have a rich conversation where it's like, well, one might be a little bit influenced by our business goals. I don't think you just run around and people are like, yeah, I'm going to sell my house, but my goal is to get an offer from Opendoor. And so that's like, okay, the template might be the same, but it's actually the content that takes a little bit of cultural instantiation.

Lenny Rachitsky (00:38:21):
Got it. And it sounds like people talk from what is the job to be done that feels like a core part of the way you think about it. What is the job to be done? Just that language alone feels really powerful. Is there a resource or a book that you point people to help your team learn about the jobs to be done work? Is there one thing you find useful?

Brian Tolkin (00:38:38):
Not about jobs to be done. I do a lot more pointing people towards internal examples of where I saw other PMs maybe do as well or blogs and stuff. But your blog is a column when we pass around, not about jobs to done, but just about many topics.

Lenny Rachitsky (00:38:56):
I'm flattered. Thank you.

Brian Tolkin (00:38:58):
Yes.

Lenny Rachitsky (00:38:58):
I really appreciate that. I was also thinking as you were talking, you're friends with Kayvon and jobs to be done on Twitter was quite the journey for them, traumatic for a lot of people. I think it went very far to the extreme of the-

Brian Tolkin (00:39:11):
Yeah. I think they're more dogmatic about it.

Lenny Rachitsky (00:39:13):
Very dramatic. And so I guess it's a lesson here, maybe don't take it that far.

Brian Tolkin (00:39:19):
Yeah. And I think it probably, and I don't know if Kayvon would agree with this, I imagine he would, the generalized version of you pick the right framework for the right job and if you say there's one framework to rule them all and this is the only framework that works and then of course every problem into it, then we chop.

Lenny Rachitsky (00:39:38):
The way I think about jobs to be done is exactly the way you're describing it where it's just think from the lens of the job to be done for our customers. So for my newsletter, what is the job to be done of my newsletter to help you become better at your job as a product person building product. And that actually ends up being really helpful. And it feels like that's the way you guys think about it at opening.

Brian Tolkin (00:39:57):
Yeah, absolutely. And you're crushing it by the way.

Lenny Rachitsky (00:40:00):
Thank you. So are you. You talked about, I'm going to go into another question to deflect your compliment. You mentioned that Uber, there's a million transactions happening every second, it's massive scale. Opendoor is completely different. You have very few very large transactions. Yeah. I'm curious how you do experiments, if you do experiments, do you do A/B tests? What have you learned about just how to think through low sample sizes plus A/B testing?

Brian Tolkin (00:40:29):
Yeah, very hot topic of conversation. We do A/B test. It is obviously the gold standard. And so we do as much as we can. Of A/B testing there are parts of our funnel and flow that have more volume than others. So top of quality testing easier than down funnels, A/B testing purely product or tech features easier than A/B testing processes, operational processes. But you're totally right. We are not doing hundreds of millions of transactions a year. And so experimentation can be more challenging. And so I think one way to think about it is A, acknowledge the problem, which just to say don't, and we've made this mistake many, many times, but don't just force yourself into A/B testing without running the power analysis and say like, hey, are we going to get results? What is the size that will detect and what is the runtime of that experiment?

(00:41:39):
And be honest, is that acceptable? A second lesson here, is there certain experiments that are important enough and it's hard to triangulate signal in any other way that you may say a six-month runtime is an acceptable outcome and we are going to start it in June and we will be smarter for it for 2025 planning and we're going to set it and forget it and we're grateful we did, and that's okay. But the only mistake here is thinking you'll get an answer in a month when you won't, and then pretending you do and then waking up a month later and being like, "Well, it was insignificant and this and that." We could have known that. And then the third thing is, and experimentation is all about increasing your conviction in the problem or the solution. So the generalized version of the statement is, if there are parts of your funnel or flow that are low end and you can't run a canonical A/B test, how might you otherwise increase your conviction in the solution that you're building?

(00:42:47):
And there turns out there are a decent number of other ways to do that. The first best, most obvious is talk to more customers. But there are other statistical techniques that again, aren't as rigorous or good, but may be possible. You may be able to use observational data, you review with diff and diff, you may be able to look at sister cities or twin cities. You may be able to segment by geo, you may be able to reduce your power and say, hey, we're going to run at 80% confidence for all of our experiments instead of this traditional 95% because that's a worthy trade-off. And if we're wrong one more time out of 10, that's okay.

(00:43:28):
You can do a long-term holdout to match your intuition. And so there's a lot of other techniques to hone your intuition. There's a lot of other techniques to build conviction and confidence. And so we try to be very creative on doing that. And then the last bit I would say is if you're not going to get significance, if there's no other techniques at your disposal, then sometimes you just got to trust your intuition and ship it. And if that's what you believe, then that's what you believed and you shouldn't spend time trying to get false precision.

Lenny Rachitsky (00:44:01):
I want to spend more time on that last point, but real quick, the power analysis you talked about, there's people, don't know, there's calculators out there that you could just plug in, here's how much traffic I'm getting, here's how much of an impact difference I want to see, here's how long it'll take to find out.

Brian Tolkin (00:44:17):
Yep, exactly. Totally. And some of the calculators are great where you can also plug in the traffic and your acceptable runtime and it will tell you the minimum detectable impact and then you can gut check your own intuition. So you can play around with that.

Lenny Rachitsky (00:44:31):
Awesome. We'll try to link to one of those in the show notes. So, on the intuition piece, is there anything more there? Just like how you think about when you run the product team, just how you recommend people leverage intuition versus not. Because some companies are like, we're just going to trust the data. I don't really trust your opinion. You don't know this customer exactly. You talked about Opendoor, I'm not buying houses myself, so I don't know how much I can trust my intuition. Just what's your general advice to your product team of how to think about their intuition and when to rely on it versus not?

Brian Tolkin (00:45:06):
So, at Opendoor, for example, I'd say on the relative spectrum, we're quite data-driven. And then it's when we come into this challenge where we say, okay, that is another technique or tool in the toolbox. I think the generalized version of that is customers, products, people can surprise you. And so this happens all the time for people who build products. I'm sure you've got great stories from Airbnb where you saw something, put it out there just was very-

Lenny Rachitsky (00:45:35):
All the time.

Brian Tolkin (00:45:36):
All the time. And so I think there's definitely a humility to say if you can, if it's relatively easy to test your assumptions or test your hypotheses. That is always better to gut check yourself. And that takes a little bit of humility to say that, but we've all been wrong plenty of times. But if that's just not on the table, I think the reality is you can't pretend it is. And sometimes you got to use taste and judgment and then you say, okay, what is my conviction level and do I have just medium, low or high conviction? And if I have anything low or medium conviction and it's a decision of consequence, I should talk to more customers, check it with another person and see if their intuition matches. Something that gets me personally to the high bucket category.

(00:46:27):
And then I think the last part, which is some part of experimentation is if you just ship something because it's your intuition or it's where you want to see the product go, do you have a reasonable feedback loop to understand whether or not you are correct? So that could be customer support or ticket volume or feature adoption, whatever the case is, it may not be an output metric in the traditional A/B test, but some more rigorous system that says, hey, I had this hypothesis, we just shipped it for x, y, z constraint reason for red.

Lenny Rachitsky (00:47:04):
I think that's awesome advice. I agree with everything you're saying. You mentioned this word humility, and it is a good segue to something I want to talk about, which is Zillow. One of the most interesting things that's happened in your space is Zillow basically decided, hey, we're just going to do what Opendoor is doing, they launched it, you're basically frenemies for a while, and then they're like, no, it's not working. Now you partner and now you work with Zillow on this stuff. So are you able to share what went down there with the story of what happened, how it went, and where things are at now?

Brian Tolkin (00:47:36):
Yeah, I mean we do partner with Zillow. Zillow's been a fantastic partner for us and we've really enjoyed a working relationship with them. I think when you think about it, they have tremendous amount of reach and audience and all these online platforms have tremendous reach and audience. And we happen to have a fairly unique selling solution. And so there's a nice, not to use a business school word, but there's a nice synergy so to speak, between a high intended audience who's doing a lot of browsing and searching and discovery and starting their process on one of these online platforms and what we offer, which is transaction services that allow people to actually move particularly on the seller side. And so there's just a pretty nice symbiotic relationship there with the Zillow's and the regimens of the world. And so both of those have been great partners for us.

Lenny Rachitsky (00:48:43):
What do you think Zillow maybe underestimated or didn't get about the space that made it harder than they anticipated? That seems obvious. Of course, let's go down funnel, let's just do it all. And they're like, "Oh, shit, not working." What do you think they didn't get or what do you think they missed?

Brian Tolkin (00:48:58):
I guess continuing on the humility point, I won't necessarily pretend to be in their shoes, but I will say the business is challenging and it's complex from a number of different dimensions. It's not a traditional software only product, but you have to be really good at pricing. You have to be really good at product, you have to be really good at the operations. You have to be really disciplined at risk. You have to be really good in the capital markets. And so you have to put all of these functions together to build a vertically integrated product. And that's the reality. And so that is something that's been in Opendoor's DNA from day one because we started with a vertically integrated product. And so we can't deliver unless we have all of those things. Right? And so I think that's something that continues to help us to this day, is that vertical integration requires all of those pieces coming together.

Lenny Rachitsky (00:49:53):
That makes a lot of sense, and I think it's a good reminder of there are adjacent markets and businesses that always feel like, "Oh, we could expand to that someday." Such a big opportunity, this business could be so much bigger. And then you realize your business is completely not set up to operate this way. Zillow is very software driven, just I am not going to simplify what they do, but it's a website, very software. And obviously as we talked about Opendoor, a huge operational component. And then as you said, the pricing piece and the debt stuff.

Brian Tolkin (00:50:24):
Yeah. Yeah, totally. Yeah.

Lenny Rachitsky (00:50:26):
Yeah. So I think it's a really good reminder that just when you're taking on something completely different, it may not fit into the way your company operates and partnering makes sense. Anything else there that's interesting to share around the Zillow thing? I guess one is maybe it was just like, I imagine it was very stressful. Zillow's getting into it. "Oh, shit what are we going to do? They got all the traffic." Yeah, anything there?

Brian Tolkin (00:50:46):
Yeah. I mean, it's certainly stressful. I think in general we try to live by whether Zillow or anybody else being competition aware, but not necessarily competition focused. And the reality is vast, vast in our space. A vast majority of people still move the traditional way. And so this isn't something where it's like the size of the prize isn't particularly large enough short or anything like that. The reality is it's the largest asset classroom in the United States, and if we just stay super focused on, hey, who are the customers that we serve really well that we talk to every day, there's a little bit of confidence that comes from being able to stay focused on that regardless of the competitive environment, again, because it's not like the market is fully saturated.

(00:51:40):
This is the same thing back in the Uber days as well. It's like transportation is almost infinitely large. And so, yes, it feels like there's heated competition between Uber and Lester or whatever back in the day, but the reality is there's plenty of trips that happens and people need to get around sitting in plenty of different ways. That's neither Uber and more Lyft. And staying focused on how you can develop for your customer, I think is the best way to focus.

Lenny Rachitsky (00:52:11):
There's a podcast that will come out before this episode with Jeff Weinstein from Stripe who's building Stripe Atlas. They had a similar experience with AngelList launched a direct competitor to Atlas, and then they realized Atlas is so much better. Forget it. We're just going to send everyone to Atlas.

Brian Tolkin (00:52:29):
Really?

Lenny Rachitsky (00:52:30):
Yes. And I think it's the same exact lesson that if you just stay focused on jobs to be done, let's say, of what is the job to be done and do the best possible job, and knowing that the market is much bigger, that you're not really competing with someone else, another company, it's the default behavior in your case. It's like people are just buying their house the old-fashioned way. That's the actual competition.

Brian Tolkin (00:52:51):
Exactly. Yep.

Lenny Rachitsky (00:52:53):
Yeah. Okay. So, along these lines, something else I've heard that you're very good at is staying very calm under pressure and staying very levelheaded when things are really crazy. This is something that a lot of people are not good at, especially leaders. They stress everyone out things. You go crazy, they don't create a good vibe. And then two, something people want to get better. Leaders and non-leader are like any lessons, anything you've learned about just how to develop this skill?

Brian Tolkin (00:53:18):
I think part of this may have been sharpened in the early days of Uber. Everything felt like a fire drill all the time. So the only way to operate, but I think you almost hit the nail on the head in the question, which is a little bit of an intellectual answer of when you reflect the stress onto your teams, everybody tenses up and tightens up. And so it counterintuitively doesn't produce better outcomes. And so I think the other reality to remind ourselves, and these are a bunch of mantras that just are helpful in these moments, is you're never as good as you think you are. You're never as bad as you think you are. And so that more even keeled demeanor, I think allows you to have a clearer head when you're operating under the pressure and to think more clearly.

(00:54:14):
I think one of the maybe least helpful answers, but unfortunately, the reality is you got to be in some stressful situations to also have the perspective that cycles past the things past. And that remaining calm is what matters. And so maybe the advice there is reflecting on one of these situations happen, exposing yourself to them, not running from them and then learning from them so that the next time it comes around you can say, Hey, I've been here before. I've slept on the floor in China before launching uberPOOL and thinking we're going to miss a launch deadline. And what were the tools in my toolbox and my toolkit that showed me that in terms of getting it done or not, and what were the lessons?

Lenny Rachitsky (00:55:06):
I love that. So part of it is just go through this experience many times and you'll start to realize, okay, it's not actually going to be as bad as people may think. You mentioned this toolkit instead of tools. Is there anything else there that you come back to that ends up being helpful? You mentioned this mantra of it's never as bad as people think it is, it is never great as people think it is.

Brian Tolkin (00:55:23):
Yeah, I mean, I think exposing yourself to other people's stories or however you may learn is really, really helpful. So again, whether it's your podcast or books or biographies or one of the podcasts that I love is Founders Podcast, which talks about historical famous entrepreneurs. And obviously these are elevating very famous people already, but there's a lot to learn from a lot of these stories as well and understanding that the journey in pack is nonlinear, it never is for anybody. And so I think being able to expose yourself to other stories that even may if you don't have those personal experiences and then understanding how others navigate.

Lenny Rachitsky (00:56:11):
Got it. So just hearing of other people's crazy experiences and building on this muscle of like, okay, they've gone through crazy stuff, things work out.

Brian Tolkin (00:56:18):
Yeah, totally.

Lenny Rachitsky (00:56:20):
We'll make it through. Okay. I have this note here that I think either someone mentioned about you or you may have mentioned that product is finding the kernel of truth in a sea of ambiguity and signals. Does that mean anything to you?

Brian Tolkin (00:56:33):
Yeah, absolutely. I mean, I think in most organizations and to do the job effectively, you're going to get signals from everywhere and good ideas come from everywhere. It may be your CS team or CX team. It may be a customer directly. It may be a conversation you had. It may be a YouTube video you watched that sparked an idea. It may be feedback from an executive, it may be whatever. You went out and did a field visit. You are going to get a lot of inputs around what people think about your product, what people think you should do next. And I think that the core job is to understand what really matters, right? What is noise? What is a good idea, what is a suggestion and what is back to the jobs to be done for what is really going to move the customer forward?

(00:57:24):
And unfortunately that means saying no to maybe what sounds like some good ideas along the way, but if you can really figure out this is really what matters, that's the core part of the job. It dovetails even back to our earlier conversation. In the early days of building tech and ops companies is where's the tech leverage? Same question, where's the kernel of what really matters that tech can uniquely solve? And let's go do that and be comfortable with other fires maybe burning. That's what really, really, really matters. It's a hard discipline.

Lenny Rachitsky (00:58:02):
I love that. If there's not an example, that's totally fine, but when you talk about this finding this kernel where tech could be highly leveraged, is there any example that comes to mind of that working out really well?

Brian Tolkin (00:58:13):
I mean, I think back in the Uber days, I think it was like, hey, we're not going to build sophisticated tooling infrastructure. We're not going to build a centralized growth team. We're not going to build any of that. Because if you think about the early Uber network from the simplest form, you've got a rider and a driver and you need to connect them, price the transaction and issue some receipts probably and collect payment. So it's like, okay, do we do that really well? And until we do that really well, all the other stuff is noise. It's immaterial how efficiently we answer support tickets. That's not critical. And so now it's super critical, but in the early days it's not that critical. And even the customer acquisition costs may not be super critical, in this case it's growing rapidly on the things. And so pouring fuel on the fire may not be super efficient there.

(00:59:13):
So I think that's a very good generalized example. One other tip that maybe is helpful that I frankly constantly work on and try to get better at is all these ideas and feedback that comes from everywhere, make sure it's written down for a number of reasons. One, you can then go reference it, but two, part of the job is making sure the people who present those ideas are heard and respected and know that it's at least somewhere where it was considered. And then you can look at it all and say, okay, but what actually really, really, really, really matters here? And yeah, that's another tip.

Lenny Rachitsky (00:59:55):
When you say written down, is there tools you find really helpful here? Is it just put it in a big doc that we're keeping? Is there anything you find to actually operationalize that?

Brian Tolkin (01:00:03):
I've seen different companies do it differently, but wherever you tend to try and keep a backlog, whether that's a Google sheet or your actual backlog in Jira, whatever you use, but at least it feels like, okay, the context was captured, and the idea is there.

Lenny Rachitsky (01:00:19):
Awesome. Okay. I'm going to take us to a recurring segment on this podcast called Failure Corner.

Brian Tolkin (01:00:25):
Okay.

Lenny Rachitsky (01:00:26):
Is there a story you can share of a time you failed in your career had a big failure, and how that experience made you better?

Brian Tolkin (01:00:35):
We can talk about the very early days of uberPOOL, and the first launch, if you will in San Francisco. So, carpooling product, multiple riders in a Mercedes car. And we had this idea that it would be effective for commuters, this was very, very early days. And so part of the launch was, okay, we're going to beta it with just some popular commuting corridors with specific companies or maybe the marina to Google or whatever and try and match people according to what their companies and that's how we'll drive liquidity. And we very quickly realized that back to what the kernel of truth is here is liquidity is the only thing that matters. And there just wasn't enough. There was never going to be enough to do this company based thing. That wasn't the strategy that was going towards from us. And so the reason I don't know if it's a full failure is maybe this is true all failures, you learn from it, you pivot and you go on to the next thing.

(01:01:52):
And obviously we did that and then spent a lot of our time and effort trying to say, okay, what are the bounds of liquidity and driving liquidity that we can do to understand what the most important or what the limits of the product are. So as an example, we launched and maybe people in San Francisco. Remember this $5 anywhere in San Francisco, we work for promotion, which is obviously a great deal, obviously costs a lot of money, but the whole idea here is like, oh, okay, if liquidity is what really matters, if we were to juice that and really drive liquidity, how high can our metrics get? And then we can go chase more sustainable ways to do that. But it was a interesting fail case from launching and learning to say, hey, this initial strategy just isn't going to work, we got to go. And any part of it was a hedging strategy where with a small audience and there'll be a beta population, it's like, well, this one you just got to go.

Lenny Rachitsky (01:02:51):
I think a lesson there is also don't overthink it, don't try to get too cute. Just like we're trying to make a perfect beta test versus realizing, okay, we just need a lot more people in it. Also, your $5 promotion made me think of the early promotions of the ice cream and the bunnies delivery and all that stuff.

Brian Tolkin (01:03:13):
Yeah. That was by the way, a example of fully distributed, the benefit of having those early Petri dishes. Someone a local marketing manager like, Hey, this would be fun. Yeah, that would be really fun. The platform can support it. And those promotions were fantastic. And it started out, I can't remember if the first one was ice cream or puppies, I think it was ice cream. But yeah, branched into all sorts of stuff. Boats, ice cream, puppies, kittens, I think, and all credit goes to local ideas of inspiration just being focused on trying to grow within.

Lenny Rachitsky (01:03:56):
I love that we've circled back to the beginning of our conversation, product and ops working together, the benefits of both. Before we get to a very exciting lightning round, is there anything else that you wanted to share? Any last nuggets of wisdom that you think might be useful to people when they're trying to build product companies teams?

Brian Tolkin (01:04:13):
This was great. We covered quite a bit of ground. I think the only, I don't know if this is a generalized wisdom, but something I've been thinking about as my career has progressed a little bit, especially building out proper organizations, especially as more tools come online, it's very clear that there's different types of PMs and we spent a lot of time talking about once we can operate in the physical and the digital or the product and operations worlds. But even within that, there's more technical PMs who grew up in minute engineering discipline. There are people who came from ops and there are people who came from design and grew up in a more user experience background.

(01:05:01):
And one thing that I've been moved on as is build out the team is thinking similar to a product roadmap is it's not really about is this person good or bad or whatever, it's is this person's skillset and context to the problem that is really needed. And so back to that conversation on, hey, where do we get tech leverage? It's like, Hey, is this person who has this unique skillset as a PM for this problem type? I don't know if that's helpful, but it's something I've been spending a lot of time thinking about, especially this view job posting niche view product manager. Or it's actually like, well, how can we be a little bit more thoughtful about what the actual skillset needs off this type of team?

Lenny Rachitsky (01:05:47):
Awesome. It's like a person product fit.

Brian Tolkin (01:05:50):
There you go.

Lenny Rachitsky (01:05:50):
And I think it's because a lot of companies hire generalists and they're just like, we'll hire someone smart, ambitious, and with experience and general experience and then we'll put them on different things. So I think these are two different philosophies and it probably makes a lot of sense for an Opendoor with very unique type of business, with very specific skills that are necessary to be really good there. Okay, amazing. Brian, with this, we've reached our very exciting lightning round. Are you ready?

Brian Tolkin (01:06:16):
Let's do it. Can't wait.

Lenny Rachitsky (01:06:17):
Let's do it. First question, what are two or three books that you've recommended most to other people?

Brian Tolkin (01:06:23):
Shoe dog, Black Swan, Design of Everyday Things, and for a fun one, Shawn Theron.

Lenny Rachitsky (01:06:36):
Amazing. Four books for the price of two to three. I love it.

Brian Tolkin (01:06:40):
Apologies. I'll stick to the rules.

Lenny Rachitsky (01:06:42):
No, no, there's no rules. There are no rules.

Brian Tolkin (01:06:45):
There you go.

Lenny Rachitsky (01:06:46):
Next question, do you have a favorite recent movie or TV show that you've really enjoyed?

Brian Tolkin (01:06:50):
I like the sports docu ones on Netflix, so Full Swing, Drive to Survive, Break Points, tennis, golf, F1, all of them.

Lenny Rachitsky (01:07:02):
And wasn't there that Nike documentary recently with Ben Affleck?

Brian Tolkin (01:07:05):
There is, which I have not seen. So if it's good, I don't know if that's a recommendation or just an acknowledgement.

Lenny Rachitsky (01:07:12):
It's worth watching. If you like Shoe Dog, I feel like you'd enjoy it. It was entertaining Michael Jordan, things like that. Next question, do you have a favorite product that you have recently discovered that you really love?

Brian Tolkin (01:07:24):
So we just got a puppy and we are about to have our first child. And so all of my purchases recently are puppies and children focused. My buddy gifted us the Phi collar for our dog, and so we've been really enjoying that. Another one as I'm getting busier for news and stuff is Particle, which is a great news aggravation tool, AI news tool.

Lenny Rachitsky (01:07:54):
Cavan's wife's business. I am a huge fan, actually I think it just came out of beta and now it's like a full app that anyone can download. I just actually installed it yesterday again and I love it. I get these pushes every few... I don't know, it's like a couple of times a day of just like, here's what's happening. Also, congratulations I should have said on your pending child.

Brian Tolkin (01:08:16):
Thank you.

Lenny Rachitsky (01:08:17):
Lucky for you. I have a newsletter post with all the products you should buy, it's called New Parent Gift Guide for Product Managers.

Brian Tolkin (01:08:24):
Love it. I will definitely probably buy all of them.

Lenny Rachitsky (01:08:30):
If you don't already have them all. And now everyone's probably sending you their spreadsheets of all their favorite stuff there.

Brian Tolkin (01:08:30):
Exactly.

Lenny Rachitsky (01:08:35):
Okay, next question. Do you have a favorite life motto that you often come back to share with people either in work or life?

Brian Tolkin (01:08:41):
Well, mostly just stay curious.

Lenny Rachitsky (01:08:44):
Stay curious. I love it. Two more questions. Who has most influenced you in the course of your career?

Brian Tolkin (01:08:54):
One of the people who inspired me very early on in my product journey. I've been fortunate to have a number of very good mentors and obviously we talked about earlier while I was founders of books or me a lot from other people's journey. But one person who was personally important to me early in my product journey and very supportive of this guy named Jeff Holden, who was the chief product officer at Uber back in the day, and is like a young PM transferring into product really took me under his wing. And I think I'm forever grateful for that, for Jeff, for helping grow my career, but also try to pay it forward a little bit in terms of people who are going in the career. That was really meaningful for me.

Lenny Rachitsky (01:09:42):
Last question. I hear that your interview at Uber was pretty wild. Can you tell that story?

Brian Tolkin (01:09:48):
Yeah, I can. So, long story short, I was starting a company my senior spring before graduation and we had to go our separate ways. So I hadn't done traditional recruiting ever. And my buddy called me up and was like, "Hey, we're looking for smart, hardworking people at this Uber thing. Are you interested?" And quick side note, I had actually done some very early diligence work on these taxi apps back in 2011, looking at the time was Uber Cab and Cabilis and Taxi Manage can probably names nothing these days. And so I knew what Uber was and so I said, "Yeah, sure, I would love to." And so I had the first round of interview went well, and they said, great. And at that stage is come on onsite, the full enchilada one works, and this was post-graduation and was helping out some companies but didn't have a full-time job.

(01:10:51):
So I said, hey, I'm pretty flexible. How about next Tuesday? I said, great. So we scheduled it and then on Friday or Saturday or over the weekend I looked, I'm like, oh, Tuesday's, July 4th. I scheduled my interview for July 4th. And so I called my buddy and I'm like, hey, I am so sorry. I don't want to make people in on July 4th. Should I cancel? Should I reach out? Everyone's accepted. Whatever you do, do not cancel your interview. Like, okay, I'll be there on July 4th. And so I went in to the office on July 4th and there was a very small handful of people there. It was actually launching that day, was launching Uber's second ever product type, which was Uber SUV. And I had this, I think it was probably five hour gauntlet interview on July 4th from noon to five and missed my July 4th barbecue. And it was quite the experience, but I think maybe set the stage for some of the early days chaos. I'm very glad I didn't cancel the interview.

Lenny Rachitsky (01:11:58):
And was Travis involved in that interview or is it just-

Brian Tolkin (01:11:59):
Travis was involved in the interview. She was one of the... I think there were four or five people, and the two who were generally guiding my interview process and Travis and one other person starting that day. And part of the gauntlet interview was a simulation of the job, if you will. And so some of that was building some novels on the computers and some of it was writing potential emails to drivers and if she had the driver come in and you did chat, so I was in this room by myself typing away on the first part, which was building the model. And I hear him knock on the door and Travis comes in and he just sits down and says, "Hi, I'm Travis." I don't know who you are, but I'm Brian, and we have a 45-minute chat, or maybe it's been about half hour, 45 minutes. And clearly I'm not producing the work that I'm supposed to of the interview.

(01:12:59):
I'm supposed to be building this model. I'm supposed to email it back to the person who sent it to me. Clearly I've done nothing chatting with the CEO. And I hear a knock on the door and the door opens and the person sees that I'm talking to Travis, "Oh, continue, continue" and it was very good. Also, pretty intense conversation with Travis that definitely set the expectations working there.

Lenny Rachitsky (01:13:24):
And clearly worked out. And Travis was happy. Is what-

Brian Tolkin (01:13:28):
I hope so.

Lenny Rachitsky (01:13:28):
... I imagine.

Brian Tolkin (01:13:29):
Yes.

Lenny Rachitsky (01:13:30):
Amazing. Brian, thank you so much for being here. We went through everything that I was hoping to get through. Two final questions. Where can folks find you online, and is there anything you want them to check out that you might be up to? And how can listeners be useful to you?

Brian Tolkin (01:13:44):
Super kind. They can find me online on Twitter, LinkedIn, both just Brian Tolkin, my name. In terms of being useful, if you have a home to sell, feel free to go on to Opendoor. More importantly, if you have feedback on the product, but would love to hear it. Otherwise, any feedback on what people liked or would love to learn more about from what we chatted about would be super great. So I'd love to hear from you.

Lenny Rachitsky (01:14:09):
Brian, thank you so much for being here.

Brian Tolkin (01:14:12):
Lenny, I really appreciate it. This was great. Bye everyone.

Lenny Rachitsky (01:14:16):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

