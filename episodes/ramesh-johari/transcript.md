---
guest: Ramesh Johari
title: Marketplace lessons from Uber, Airbnb, Bumble, and more | Ramesh Johari (Stanford
  professor)
youtube_url: https://www.youtube.com/watch?v=BVzTfsUMaK8
video_id: BVzTfsUMaK8
description: 'Ramesh Johari is a professor at Stanford University focusing on data
  science methods and practice, as well as the design and operation of online markets
  and platforms. Beyond academia, Ramesh...

  '
duration_seconds: 5016.0
duration: '1:23:36'
view_count: 44479
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- metrics
- roadmap
- a/b testing
- experimentation
- data-driven
- analytics
- funnel
- pricing
- monetization
- subscription
- revenue
- hiring
---

# Marketplace lessons from Uber, Airbnb, Bumble, and more | Ramesh Johari (Stanford professor)

## Transcript

Ramesh Johari (00:00:00):
Marketplaces are a little bit like a game of whac-a-mole. One example that I came across with one of the companies I worked with that I love is our new supply side was having a pretty bad experience.

(00:00:12):
So what we decided to do is build some custom bespoke features that were really going to direct them to more experienced folks on the other side of the market. Good. And then, yeah, lo and behold, pretty soon those metrics start to look better. But then we're looking at it, we're like, "Wait a second. Now the existing folks on the other side are having a worse experience," so you kind of whiplash around. You're like, "Oh, wait a second. We better do something about that." So we take them, we try to match them up with the more experienced folks, and now suddenly a month after that, you're like, "Wait a second," and your metrics just keep moving around. And that's because the whac-a-mole game here is ultimately, a lot of marketplace management is moving attention and inventory around. Many of the changes that are most consequential create winners and losers. And rolling with those changes is about recognizing whether the winners you've created are more important to your business than the losers you've created in the process.

Lenny (00:01:00):
Today my guest is Ramesh Johari. Ramesh is a professor at Stanford University, where he does research on and teaches data science methods and practices with a specific focus on the design and operation of online marketplaces. He's advised and worked with some of the biggest marketplaces in the world, including Airbnb, Uber, Stripe, Bumble, Stitch Fix, Upwork, and many others. And in our conversation, we get super nerdy on how to build a thriving marketplace, including where to focus your resources to fuel the marketplace flywheel growth, why data and data science is so central to building a successful marketplace, how to design a better review system. Why as a founder, you shouldn't think of yourself as a marketplace founder, but instead simply as a founder. Also, how AI is going to impact data science and marketplaces, and experimentation, and so much more. If you're building a marketplace business, or thinking about building a marketplace, or just curious, this episode is for you. With that, I bring you Ramesh Johari after a short word from our sponsors. 

(00:02:04):
This episode is brought to you by Sanity. Your website is the heart of your growth engine. For that engine to drive big results, you need to be able to move super fast, ship new content, experiment, learn and iterate. But most content management systems just aren't built for this. Your content teams wrestle with rigid interfaces as they build new pages. You spend endless time copying and pasting across pages and recreating content for other channels and applications. And their ideas for new experiments are squashed when developers can't build them within the constraints of outdated tech. 

(00:02:35):
Forward-thinking companies like Figma, Amplitude, Loom, Riot Games, Linear, and more use Sanity to build content growth engines that scale drive innovation and accelerate customer acquisition. With Sanity, your team can dream bigger and move faster. As the most powerful headless CMS on the market, you can tailor editorial workflows to match your business, reuse content seamlessly across any page or channel, and bring your ideas to market without developer friction. Sanity makes life better for your whole team. It's fast for developers to build with, intuitive for content managers, and it integrates seamlessly with the rest of your tech stack. Get started with Sanity's generous free plan. And as a Lenny's Podcast listener, you can get a boosted plan with double the monthly usage. Head over to sanity.io/lenny to get started for free. That's sanity.io/lenny.

(00:03:26):
This episode is brought to you by Hex. If you're a data person, you probably have to jump between different tools to run queries, build visualizations, write Python, and send around a lot of screenshots and CSV files. Hex brings everything together. Its powerful Notebook UI lets you analyze data in SQL, Python, or no code in any combination, and work together with live multiplayer and version control. And now Hex's, AI tools can generate queries and code, create visualizations, and even kickstart a whole analysis for you all from natural language prompts. It's like having an analytics co-pilot built right into where you're already doing your work. Then when you're ready to share, you can use Hex's drag and drop app builder to configure beautiful reports or dashboards that anyone can use. Join the hundreds of data teams like Notion, AllTrails, Loom, Mixpanel, and Algolia using Hex every day to make their work more impactful. Sign up today at hex.tech/lenny to get a 60 day free trial of the Hex team plan. That's hex.tech/lenny.

(00:04:31):
Ramesh, thank you so much for being here. Welcome to the podcast.

Ramesh Johari (00:04:35):
Thanks so much for having me, Lenny. It's great to be on. 

Lenny (00:04:38):
It's great to have you on. A big thank you to Riley Newman for connecting us. Riley was the first data scientist at Airbnb and head of data science at Airbnb, and that role is actually a really good microcosm of what we're going to be focusing on in our chat today. We're going to get super nerdy about marketplaces, and experimentation, and data. I know that's your jam. Are you ready to dive in?

Ramesh Johari (00:05:00):
I really am. Yeah. And I actually want to thank Riley too. I got to know Riley when I was at oDesk first as a research scientist, and then I directed their data science team. This is way back in 2012, and I was looking around for people who are experts on how we think about data and marketplaces, and Riley Newman came up and so I invited him to come talk to us at oDesk, and we've stayed in touch since then. 

(00:05:26):
Those were early days of where this industry was, and I've had a kind of lengthy career now thinking about those kinds of problems. So I'm pretty excited to talk about it with you.

Lenny (00:05:37):
Let's start broad and set a little foundation. You have a really interesting way to describe what a marketplace business even is. So Ramesh, what is a marketplace business, and also why is data so important and such an integral part of building a successful marketplace business?

Ramesh Johari (00:05:53):
It's interesting when people sit down and think about, say Airbnb, what does Airbnb sell? Average person is like, "That's pretty obvious. Airbnb sells rooms. I go there to book a room I want to stay at," right? Other people say, "What does Uber sell? Uber sells me rides. I'd use Uber when I need to get a ride from somewhere to somewhere else."

(00:06:10):
And in some sense, you're not wrong. I mean, you go there. That's a platform to get these things. But that's not what the platform is selling. That's a really important distinction. There are people on the platform that are selling that to you. The hosts on Airbnb are selling you listings. The drivers on Uber are selling you rides. But Uber and Airbnb are selling you the taking away of something, which is a weird thing to think about. What they're taking away is the friction of finding a place to stay. They're taking away the friction of finding a driver.

(00:06:42):
In economics, we call those things transaction costs. When you take econ 1, you learn about markets and how supply meets demand, and we get prices out of that. But what you don't learn until econ 201 is that markets don't always work. And one of the reasons markets don't always work is because we have what are called market failures due to the presence of these kinds of friction. So what's a market failure? It's that Lenny wants to get from Palo Alto to Burlingame and he can't do it. Why can't he do it? He doesn't have anyone to drive him. Well, why doesn't he just call someone to drive him? Well, who's he supposed to call? Who are those people? Are they out there? Are they willing to drive him right now, right at 10:00 AM on a Friday? Are they willing to take him somewhere?

(00:07:22):
When I want to stay somewhere when I'm traveling, a friction is, who's willing to give me their room? I mean on principle, there's people who are willing to let me stay in their living room, but I don't know who they are. 

(00:07:31):
So those are frictions, and what the marketplaces are selling you is taking the friction away. That's what you're paying them for. And it's an important observation, because what that means is the marketplace's customers aren't just the people buying the rides, they're buying the listings. Actually, the hosts are Airbnb's customers, and the drivers are also Uber's customers. So both sides of the marketplace are the customers of the platform. Both sides depend on the platform to help the platform take that friction away. Because just like you want a place to stay or you want to ride, the driver is at Uber because he wants to earn money by taking people places. And the host is on Airbnb because they want to earn money by selling their listing.

(00:08:10):
I think this concept that we're making money by taking transaction costs away is such a fundamental idea that's misunderstood around marketplaces. That when you're an entrepreneur starting a marketplace or thinking about your business model, I think you can be wildly off if you forget that that's the thing that's fundamentally your value proposition. And then you asked about the role of data, and more broadly data science in marketplaces.

(00:08:36):
So it's an interesting thing, right? The example I always love to give are the ancient Agoras in Greece or Trajan's Market in Rome. When you look at pictures of these things, what really stands out to me is the rock. I mean, these things are made of stone. It's not like you were going to move a booth from one place to another place without moving a lot of rock from one place to another place. 

(00:09:00):
So you flash forward to 2023, and here we are with technology undergirding pretty much every kind of commerce now. And it means we can architect and re-architect the marketplace kind of on the fly, and we really are doing it all the time.

(00:09:14):
And these frictions that are getting taken away, they're getting taken away because of data and data science. So I really want to highlight three pieces of this for people, which I want you to think of them as a cycle. But to start with, let's just lay them out one at a time. 

(00:09:29):
One of them is finding people to match with. So that's the problem of, "I want to stay somewhere. Who is out there, who's willing to let me stay with them on a given timeframe?" And then if I'm a host, I have a listing. Who is out there, who's willing to stay at my place when I have it available? So that's finding matches.

(00:09:49):
Then there's making the match. And so here, going back to my time at oDesk, a big problem that we dealt with there was if I've got multiple applicants to my job, who should I hire? Who should I interview? It's a common problem we face in the real world, but now it's all remote. I don't meet these people in person. All I've got is this application they submitted to me. I need help triaging that. Okay? So that's helping make a match out of possible partners you can match with.

(00:10:16):
And then finally, we make matches. Well, what do the matches tell us, right? I mean, if you stay somewhere in Airbnb, you learn something about the host, you learn something about the listing. The host learns about you too. And that's all information that the marketplace should feed back in. So this is where we get to rating systems and feedback systems, even passive data collection, right? Did you leave your booking before you were supposed to leave? Well, maybe that's a sign that something didn't quite work out the way you wanted to work out. So that's passive data collection. Did you leave five stars? That's active data collection.

(00:10:47):
Get all this back in, and what does that do? Well, that lets us do a better job finding potential matches and make potential matches in the future. Every single thing I just said, finding potential matches, making matches, and then learning about those matches, and then cycling back again, that is the data science in marketplaces. 

(00:11:05):
And I feel like every marketplace that you could think of in any vertical has those three problems to deal with and relies on algorithms in data science to help them solve it. And in turn, that is I think really the underpinning of taking those frictions away.

Lenny (00:11:22):
Many founders try to start a marketplace business, think about marketplace opportunities where they don't exist. And there's often these recurring failures of types of marketplaces that just don't work in an area. I was just writing a couple ideas down while you were chatting like cleaners, getting cleaners as a marketplace doesn't seem to work ever. Car wash, there's a classic failure too. Getting tasks done for you on demand as a marketplace seems to not often work.

(00:11:46):
So this might be too big of a question, but I'm just curious if anything comes up of when someone is starting a marketplace or thinking about starting a marketplace business, what do you find are the most common flaws in, this is probably not going to work as a marketplace? 

Ramesh Johari (00:12:01):
That is such a fantastic question, and I want to preface what I say with a couple of comments. So one of them is that I've worked with a lot of different marketplace companies, but anything I say is pertaining to something more sensitive. I may not name the company over the course of the podcast.

(00:12:17):
But the other more important thing I want to say is that I'm a professor at Stanford, and there's a reason I'm not a successful scaled entrepreneur of marketplaces, and that's because I probably haven't unlocked the key to exactly the question you asked. But nevertheless, I have some thoughts on it.

(00:12:33):
The most important one is this. What I've found talking to people who want to start what they think is a marketplace is that they think too much about a marketplace before they're a marketplace. That in my view is the biggest failure mode.

(00:12:46):
You mentioned specific things, cleaners. I wonder about that, right? Is it something about the cleaning industry? It possibly is. I don't claim to be an expert on the microeconomics of the cleaning industry. But often it's not that, it's that I thought I was building a marketplace from the beginning, and that's not the way the world works. So I'll give you one vignette of this that I really like, and that's UrbanSitter. 

(00:13:09):
So first, UrbanSitter is a babysitting marketplace. We can talk about their whole life story, but I think what's most interesting is really the early days. And in the early days, what I found interesting, the way I found out about them actually is that we were stuck looking for some help. And I found out about this new platform where the clever thing was when you used to hire a babysitter, it's like pre Venmo days, you needed cash on hand. Because when the babysitter's done at the end of the day, they're usually high school suits or something. They want to get paid. They're not going to take your IOU, that you'll send them some check in the mail the next day.

(00:13:43):
And unfortunately, you often don't have cash. They don't take credit card. They're high school students. That was an incredible friction to address, which is literally just we accept credit card payments for babysitting. That's it, right?

(00:13:55):
Now from there, what happened is they took advantage of Facebook networks between parents and babysitters to build trusted introductions. So let's say my sitter wasn't available. I get to know sitters in the Facebook network of that sitter. And once they overcame that first thing to get some liquidity onto their platform, they could move towards asking, how do I solve for these frictions that I talked about earlier? How do I solve for helping people find potential matches? How do I solve for people making those matches, right? You can't do that when you don't have liquidity on your platform. It's silly to tell someone, "Hey, I'm really going to help you find all those drivers out there, even though I only have three drivers on my platform." That's not a friction you're solving for. 

(00:14:36):
So in their example, as they evolved, they actually shifted their monetization model away from billing specifically for this friction of allowing you to pay with credit cards, instead to now billing for how you were interviewing and contacting sitters. They had a two-part plan for that. One with a pay as you go menu, one with a more of a subscription option. But the key thing was either way, what you were paying for now was finding potential babysitters, not paying them with a credit card. That wasn't the key thing anymore.

(00:15:05):
So what's the moral there? The moral is a marketplace business never starts as a marketplace business, because what we think of as a marketplace business is something which at scale is removing the friction of the two sides finding each other. But when you start, you don't have that scale. 

(00:15:22):
So when you start, you had better be thinking, "What's my value proposition in a world in which I don't have that scaled liquidity on both sides?" And that's bespoke. It means different things. And in the case of oDesk, where I started, that initial thing was that remote work is a weird thing, because basically you've somehow got to know that this person who you're not next to is doing what you're asking them to do. And so the initial value proposition of oDesk was to provide tools for workers to verify they were working the hours and doing the things that they said they were doing, screenshots and various kinds of tracking.

(00:16:01):
And then in return for that, to be able to provide guarantees on both sides. So now the workers could say, "Hey, I worked what I said so I should get paid." And the employers could say, "I actually see that you worked what you said. And so I feel comfortable that I got what I paid for." That was the initial value proposition, is resolving a trust issue at a remote scale.

(00:16:21):
At that point, liquidity isn't the game. It's asking, what's a problem that people in this space are facing that I can deal with when I'm not a scaled marketplace? So again, with the cleaning industry, I can comment on that from personal experience, but otherwise, I think that's the way I would think about it. It's almost never about building a marketplace when you're building a marketplace.

Lenny (00:16:43):
That's very similar to the advice I always give marketplace founders, is 90% of your problems are going to be non marketplace specific problems. They're going to be the same problems any startup is going to have. How do I grow? It's going to be the same things you need to do.

Ramesh Johari (00:16:58):
So one thing you said was, "That's what you tell marketplace founders." I mean, something I've actually pressed hard on in my own way of thinking about this is that maybe we shouldn't talk about the concept of a marketplace founder. Really there's founders. And I think every entrepreneur... I mean one way to think about it, right? It's very hard to think about a human business endeavor that has not been disrupted by the potential for transactions to take place online.

(00:17:24):
And if that's the case, it means literally any founder is a marketplace founder. It'll be a choice they make after they grow as to whether they want to build a platform. I mean, to take a very hot recent example, no one in their right mind would've thought of OpenAI as a marketplace, but OpenAI is a marketplace now. They may not want to call themselves a marketplace, but they have plugins. The plugins are flooding that platform. People have played with it. It's not an easy thing to find the plugin you need for what you want to do. And that really is a two-sided thing now. There's the plugin creators and there's the users. And they may believe it, they may not believe it, but they are a marketplace. 

(00:18:04):
So I think a different way to think about it is every founder is a marketplace founder. It's going to be a choice they want to make for themselves of whether they want to become that platform. That's I think one. And two is because that's the case, I think one of the other challenges I find founders struggle with is you don't want to overcommit your future. And what I mean by that is that you're building up trust, and you're building up a sense of what kind of business you are in your early days. If you believe that this kind of platform future awaits you, or market platform future awaits you, there may be choices you're making early on that are tying your hands later. 

(00:18:41):
A great example of this is when oDesk started, it was because the tools they were providing were for ongoing monitoring of work. It's a very natural thing to say, "We will just take a constant fraction of the dollars that cross the platform." That all works well and good until after you become mature. Some of these relationships between worker and employer last a long time, and most of the value was generated now not so much because they're able to track each other, because the trust is now there, but because they found each other, because they're able to build that relationship through oDesk.

(00:19:16):
That meant that the longer that goes on, the less value the platform is adding into that relationship, but you're still pulling 10% of all the dollars. So what does that lead to? A word that most marketplace CEOs know well is disintermediation, which is where you were intermediating between the two parties, and now disintermediation means that essentially they're like, "Hey, we don't need you anymore."

(00:19:39):
My favorite example is we had some stuff delivered from IKEA by a Thumbtack worker once, and my wife is like, "Oh, thanks a lot. You're so reliable." He's like, "Hey, great. Here's my business card. Ever need me again? Just call the number on the back." And that was it. Thumbtack got their one lead gen, and then we didn't need the platform anymore. 

(00:19:57):
And I think this issue for oDesk meant that after they merged with Elance and became Upwork, they had to think a little bit about, "Okay, what's the monetization strategy we want to use? How do we address this issue that longer term relationships may disintermediate? And does that mean you need a pricing plan that actually takes that into account?" So early commitments in this case to a particular pricing scheme, particular monetization, can really tie your hands as you then realize later you actually are a platform.

Lenny (00:20:26):
I really like this message. It makes me think about Substack actually, which started as just a platform for newsletter writers. And then they're like, "How do we make this more valuable?" Because they take a cut of everyone's revenue. And they've actually invested heavily on helping drive demand to writers, for example, me. And at this point, over 80% of my subscribers come from Substack's network. And so they've built this marketplace element exactly as you're describing, where they just found, "Here's a pain point, writers need more subscribers. How do we help them drive subscribers?" So they figured out all these ways to create demand.

Ramesh Johari (00:20:58):
That's a really positive story, where they managed to actually expand the frontier of their business by enabling that network. For every one of those, there's unfortunately a lot of negative stories. I mean, one that I think is very painful is how eBay had a lot of challenges with its seller community as it introduced more and more fine-grained sources of fees.

(00:21:25):
And I think a lot of that, I mean there's many, many treatises at this point written on eBay, and their history, and how they got to the point that they're at. But I think one kind of simple thing I do want people to think about there is that the sellers on eBay who had matured with the platform, who had grown with it, had come to develop certain expectations about what their lives on that platform would look like. And it's understandable, because a lot of these businesses, they had built their livelihood on that platform. That was their entire business. 

(00:21:56):
So when you now reach in and you say, "I'm going to completely change the rules of the game in which your business model operates," from the perspective of those sellers, that's a breaking of a social contract that's been developed over a very long time. So I love the Substack example, because that's like, "Hey, let me amplify our social contract." But I think for every one of those, there's an eBay warning sign that you can trap yourself a little bit.

Lenny (00:22:24):
Just to close a loop on this really, I think important point, a lot of people listening to this are probably, "I'm a marketplace founder. I'm building a marketplace," are going to hear this and be like, "Oh shit, maybe I need to rethink how I think about what I'm doing." What would be your piece of advice to people like that? Is it focus on the friction point and it may be a marketplace solution, it may be a managed marketplace, it may be you own the supply? Is that the advice, or what would your advice be to someone that's like, "I'm building a marketplace"? How should they reframe their thinking?

Ramesh Johari (00:22:54):
Let's go back to kind of thinking about this concept of a marketplace of reducing friction. So the litmus test I like to give to someone who claims to me that they're building a marketplace business or they're a marketplace founder is do you have what I would call scaled liquidity on both sides of your platform? What does scaled liquidity mean?

(00:23:13):
What it means in lay terms... And by the way, I am a data scientist, and I love to think about these quantitatively. But fundamentally, if it doesn't pass the smell test, then you don't have to keep going with the data science. The smell test is scaled liquidity asks, "Do I have a lot of buyers and a lot of sellers on my platform, or do I only have one of these two, or do I have neither?" If you don't have both, you could call yourself whatever you want to call yourself, but at this moment in time, you're not a marketplace. If you have one, congratulations. You've won the game on one side of the market. And now you if you want, you have a choice point. You can lean into growth on the side that you're doing well with. You got a ton of users, ton of buyers? Great. Lean into it, get more buyers. That's one option. There's no shame in not being a marketplace. Scaling a business is scaling a business. If that's the way to do it, do it. 

(00:24:05):
If you decide you want to be a marketplace, then at that moment when you've got a lot of buyers, but not a lot of sellers, or a lot of sellers, but not a lot of buyers, the choice you're facing is, how do I take advantage of having that one side scaled to attract the other side? We can talk more about that, but there's a lot of ways to kind of hack that, to think about how... So to take Uber as an example, they would walk into a new city, and one thing that Uber was commonly known for doing this was back in the days when really Uber Black was the only service is they just hand out coupons for free rides at events, parties, things like that, to take people home. And that was a way of saying, "Hey, we're subsidizing the drivers in the city. That's our scaled side. Now we're going to use that subsidized driver base to attract riders." 

(00:24:49):
So that's like, how do you get that flywheel going? And again, many people have written about how to take liquidity, scaled liquidity on one side, and use it to attract the other side.

(00:24:59):
If you don't have either side, don't worry about it. Don't worry about being a marketplace. Worry about scaling one side. And in that world, it opens your visibility up completely into the advice of many, many startup advisors. People who have advice not so much about scaling a marketplace, but about scaling a startup. 

(00:25:22):
And I want to say you got to let the ego go at that point. It's fine to articulate to people that your vision of the future is to be a platform or marketplace. As I said, virtually every business is going to have that option at some point in the modern tech enabled economy anyway. So you're not saying something people don't already know when you tell an advisor or an investor that. But I do think you need to be humble enough at the starting point to recognize that there's no sense in talking about a marketplace if you don't have scaling on either side yet.

Lenny (00:25:52):
And then it becomes a question of a business model, unit economics of, can I build say a DoorDash, not as a marketplace? Can I just hire a bunch of people delivering? Is this even possible in a different route?

Ramesh Johari (00:26:06):
Yeah, that's a great point. One of the things I think that's useful for people to think about here that you're raising, at some level, it's kind of tied up I think with that question of whether I should have employees, or contract or freelance work on one side of the marketplace.

(00:26:23):
And that's actually a pretty old question in economics. The way we talk about it often is a distinction between a market or a firm. And one of the interesting puzzles in economics, Ronald Coase is a famous economist who thought about this is, "Well, if markets are so efficient, why do we need firms? If markets are efficient at matching labor up with things that need to get done, why would you ever need a firm?" And that's one of the earliest recognitions that transaction costs are a real thing. And that's one of the things that firms are solving for.

(00:26:52):
And I love what you're saying because what it's recognizing is, "Hey, for your frictions, the best resolution to that might not be to have a marketplace. It might actually be to have very tightly controlled labor." A good example of this actually, Stitch Fix, I think one of the things that's cool about Stitch Fix is the experience that people had early on with stylists at Stitch Fix.

Lenny (00:27:13):
I'm a happy customer, by the way. I think [inaudible 00:27:16].

Ramesh Johari (00:27:15):
Yeah, I think one of the great things about that experience is it felt magical to have someone who kind of got to know you. But that depends on a relationship that doesn't feel like a freelance relationship every single time you're going back. 

(00:27:31):
Another example that I would pull out is pretty much any healthcare platform. So for example, for physical therapy, it'd be weird if every time you went to a physical therapy platform, you just got randomly matched to whoever happened to be available then. So I think there's some curation that needs to happen of that relationship. Does that mean full employee? Maybe not. But it does mean you have to think a little bit about exactly as you brought up, what's the nature of curation of your labor pool?

Lenny (00:28:01):
Awesome. Okay, so let's come back to a point you made early on around the importance of data and the power of data in actually making your marketplace a lot more efficient and work more effectively. So say that you have a data scientist, or a data analyst, or someone that is helping you optimize your marketplace. Where do you often find the biggest leverage and opportunity for a data person to help you make your marketplace more effective?

Ramesh Johari (00:28:25):
This is an incredible question, right? Because I think I could answer it a number of different ways. One question I think that's kind of basic, it's just what should this person be doing? And I'm going to actually evade that question a little bit. I'm going to give some examples of what they could do, but I feel like that's one where context matters a lot. 

(00:28:45):
So as an example, at ride-sharing or grocery delivery marketplaces, pricing means actually, what do you pay for that ride? Or what do you pay for that delivery? So that's actually the price that's set at the moment you actually place the order. Just to be clear, by the way, if you order from DoorDash, I don't mean the price of the restaurant. I mean, what do you pay to DoorDash, right? What's that fee? Is there a surcharge, because it's surge or whatever? Okay, so that's a thing, right?

(00:29:11):
But that's not really a thing in a marketplace where the platform's not setting the prices. So in Airbnb, really hosts are the ones who are in charge of setting prices for their listings. 

(00:29:21):
One answer to your question is, if I'm in a place like Uber, Lyft, DoorDash, I want to have good data scientists thinking about pricing. Because that seems like something which should be heavily dependent on the instantaneous state of supply and demand in my marketplace. So that's one type of answer is, well do I need data scientists working on pricing? Do I need data scientists working on search? Why search? Because maybe in my marketplace, finding the needle in the haystack is really the biggest, highest friction problem. So maybe I need a lot more data scientists saying about search. 

(00:29:51):
That's what I'm going to evade. Okay? I'm going to focus more on something completely different, which is just a more philosophical point about what a data scientist does.

(00:30:00):
So in a lot of companies today, especially, a main thing that you ask data scientists to do is build what's called a machine learning model. Now, machine learning model even already can mean a lot of things to a lot of different people. I'm going to focus on something very concrete. You're asking them to predict something. 

(00:30:16):
When I started at oDesk, this is in 2012, one of the funny things about me is I started at oDesk because I'd had a academic career up to that point in about 10 years, just building mathematical models of things. I was not really very much of a data scientist up to that point. What I expected would happen is I'd go to industry and I'd be told, "Hey, look how important data is." And definitely my eyes were opened.

(00:30:40):
And one of the first things I was asked to think about is, well, okay, someone comes to oDesk, post a job, workers apply to that job. Predict which of these workers is most likely to be hired on that job. That was the narrow question. And so why is that a good question? Because we have a whole awesome set of tools now to solve that kind of a problem exactly. How do we do it? Take a lot of past data of past jobs, past applicants, past hires that were made. Then we ask these crazy big black box algorithms, "All right, do the best job you can predicting who's going to get hired on this job with these applicants." And we use that data to test how well these algorithms are doing. That's machine learning in 30 seconds basically. So we're working on this problem. Great. 

(00:31:25):
And then I kind of poked my head up a little bit. I go, "Why are we working? What is this going to do?" Well, it turns out the reason these kinds of things are important is they get used to make decisions. So what kind of decision do you make with that? Well, one thing you do is you say, "Well, if I could predict who's most likely to be hired, then I should just rank people based on that, and that would be a good matching algorithm. That'd be a good way to sort and triage applicants for employers when they're screening, trying to figure out who to interview, who to hire." Great. Sounds pretty natural.

(00:31:58):
And then you think about it a little bit, and this to me, it's such a passion project to get people to understand that this is why the humans in the loop that help us in businesses and making sense of data are so critical, is the following problem.

(00:32:15):
If you think about it a little bit, you realize what that algorithm is doing, it's really just picking up on patterns in past data. So yeah, that's great. This person is likely to be hired. But what we really want is something different. We're trying to add value by ranking people. 

(00:32:32):
So to give another example that's similar to this, when you're a marketing manager, and you've got a cracked data science team that's built a long-term value, lifetime value model for you, you're not going to get in trouble with anyone if you send your highest value promotions to the highest LTV customers, right? Who's going to blame you for that? Because you're like, "This person is worth a lot, and I sent them this promotion." Say that in your monthly report, nobody's going to give you a hard time.

(00:32:59):
But the problem with that way of thinking is actually predicting what their lifetime value is isn't really the question. The question is, how much more are they going to spend on my platform because I sent them that promotion?

(00:33:11):
That's a very different thing. It's a differential rather than an absolute. I'm not interested in their absolute LTV. I'm absolutely interested in the difference in their LTV because I sent them this promotion.

(00:33:21):
And when you look at it that way, what you realize can happen is picking up on patterns because of good predictions, right? Finding the people that have high LTV because you predicted that is very different than making good decisions, which is about saying the difference in their LTV is going to be higher because I sent them this promotion. 

(00:33:39):
I love this example, because I taught a class here at Stanford. It was like an executive education class. We had all the executives from a company in the room, and one of the people in the room was the chief marketing officer. And I just asked this question like, "Hey, okay, let's say you got this great LTV model, who would you send the promotions to?" It's like, "Definitely the highest LTV people," and there's a CMO in the room. And so it's a little bit of a delicate situation, like pushing back a little bit, right? 

(00:34:03):
I do want to be clear, there's reputational reasons you might do that anyway. I mean, I'm not trying to get away from that. But just to make the narrow point that predicting is about picking up patterns, but making decisions, it's about thinking about these differences.

(00:34:15):
Now, why is that important? Because we learn in high school, correlation is not causation. That's a phrase everybody has heard all over the place. What does that have to do with this? Well, when we teach people to build machine learning models, we're asking them to make predictions, we're asking them to find correlations. Prediction is inherently about correlation. But when we ask people to make decisions, we're asking them to think about causation. "If I make this decision, then will I actually increase the net value of my business? Will I have by sending the promotion, increased the likelihood that this person is going to spend more on my platform?"

(00:34:50):
And so the first and most important thing that I feel very strongly about in what would I get a data scientist to do is no matter who they are, even if it was that person in the weeds thinking about building this prediction model for hiring, get them to be thinking in the back of their mind always that their goal is to help the business make decisions. And that the distinction between causation and correlation matters a lot. We can talk a lot more about how does that play out in terms of their day-to-day work. But at least at a starting point, you have to recognize that the first step is always recognition that prediction isn't the same thing as making decisions.

Lenny (00:35:27):
So the takeaway here is as a data team and as a data scientist on the team, is help the business make predictions. Are there a couple more examples you could share of just what is an example of a decision that you think they often should be making and using data to help them with?

Ramesh Johari (00:35:41):
Maybe the right frame of reference for this, and the word that an academic would use is causal inference. So what we're changing from is machine learning to causal inference. So let's think that through in a couple of different use cases that are related to that marketplace data science flywheel I talked about earlier. Finding matches, making matches, and then learning about matches.

(00:36:04):
So finding matches, like you said, a core part of that is search and recommendation, and each of those relies on rankings. So I want to be able to rank order. Let's say I go do a search on Airbnb. On a rank order, the different listings in the marketplace, right? At some level, it's true that what I'm trying to do there is I'm trying to just predict, what are you going to like the most? 

(00:36:24):
But I think there's an important piece of that also, which is that I want to think a little bit about the distinction between two different ranking algorithms. That's the real decision that's being made. 

(00:36:35):
And when I think about the distinction between two different ranking algorithms, I don't want to be only comparing them in terms of how well they recreate the choices people made in the past. The way I'm really going to evaluate those is in my market, does one of those lead to better matches or more matches than the other one, right?

(00:36:54):
So Airbnb as a business, what are the most obvious core metrics? It's bookings and revenue. So you're going to want to ask a very basic question. If I use the ranking algorithm Lenny just developed last night versus the ranking algorithm Ramesh developed last week, does Lenny's ranking algorithm lead to more bookings than Ramesh's ranking algorithm?

(00:37:11):
And it's so important to put it that way starkly, because that's so different a question than, does Lenny's ranking algorithm do a better job of predicting over the last two years what bookings people made than Ramesh's ranking algorithm? So that's I think at that level.

(00:37:24):
Then we talked a little bit about ranking at the point of making a match, and I think that's where this hiring issue popped up. Because in the end, while we might have these predictive algorithms to rank who you're going to hire, that's not the important question.

(00:37:38):
Interestingly, the important question is actually to evaluate the quality of the match that's made. And we would do that through the next step of that flywheel. We'd ask ourselves, what ratings did they give back to that freelancer? Do they hire that freelancer again? So you're comparing two different algorithms not through their ability to recreate the past, but their ability to make matches in the future that can be objectively evaluated to say, "Hey, I increased the value of the business. I actually made better matches this way." And then rating systems, I think we could talk quite a bit about a similar phenomenon there too.

Lenny (00:38:12):
This episode is brought to you by Eppo. Eppo is a next generation A/B testing and feature management platform built by alums of Airbnb and Snowflake for modern growth teams. Companies like Twitch, Miro, ClickUp, and DraftKings rely on Eppo to power their experiments.

(00:38:28):
Experimentation is increasingly essential for driving growth and for understanding the performance of new features. And Eppo helps you increase experimentation velocity while unlocking rigorous deep analysis in a way that no other commercial tool does. 

(00:38:42):
When I was at Airbnb, one of the things that I loved most was our experimentation platform, where I could set up experiments easily, troubleshoot issues, and analyze performance all on my own. Eppo does all that and more, with advanced statistical methods that can help you shave weeks off experiment time, and accessible UI for diving deeper into performance, and out of the box reporting that helps you avoid annoying prolonged analytic cycles.

(00:39:05):
Eppo also makes it easy for you to share experiment insights with your team, sparking new ideas for the A/B testing flywheel. Eppo powers experimentation across every use case, including product, growth, machine learning, monetization, and email marketing. Check out Eppo at geteppo.com/lenny, and 10x your experiment velocity. That's geteppo.com/lenny.

(00:39:29):
Yeah, I would actually love to talk about rating systems, but there's an implication in everything you're describing of running an experiment versus looking at what would've happened in the previous world made. You've made change, run an experiment, see if it actually makes an impact on bookings and revenue. And that leads me to a question I wanted to ask, which is with experiments, there's kind of this classic challenge, and always elephant in the room of if you just run a bunch of experiments, you're kind of going to micro optimize, lead to these local maxima, and you may miss big opportunities and big unlocks if you're just extremely experiment driven.

(00:40:04):
You spend a lot of time thinking about experimentation. What have you learned or what advice do you have for people to either be less worried about optimizing and missing something big, or just finding a balance with running experiments, but also creating opportunity to find a huge new opportunity?

Ramesh Johari (00:40:21):
Yeah. First of all, I'm really glad you broached the E word. I was dancing around it, and I'm really glad that we talked about experiments. Because yeah, one of the big lessons of this recent conversation we've been having is just, how could you possibly know that difference without doing something like experimenting? 

(00:40:38):
So yeah, I am a big believer in experiments. I mean, I'll just lay those cards on the table. I love working with businesses that think experiments are important to helping make good decisions.

(00:40:49):
Now all that said, I am also someone who feels pretty strongly about this exact issue that you're raising. It's just, you can't experiment your way out of everything. 

(00:40:57):
And one frame I like to give people is that although you might say you're an experiment driven business, some businesses will proclaim, "We literally test everything." What that kind of leaves aside a little bit is there's a lot of degrees of freedom in what it means to test everything.

(00:41:15):
Because ultimately, what's getting built and tested are choices that are made through the organizational structure, the data scientists, the PMs, the engineers, everybody's on... Before we're running experiments, we're actually thinking about even what's worth experimenting, what designs are we coming with? So that's one.

(00:41:33):
And the other big one is, how long do we run these experiments? Okay, that's a big choice. And what I generally believe, and I think there's a paper we can link to later that I'll point your readers to as well that... Not my paper, from some folks at Microsoft.

(00:41:49):
What I generally believe is we're risk averse on both these two dimensions, that what people decide to test in a world that has promoted experimentation for everything tends to be more incremental by design. Okay? And we'll come back to that actually, answer the because in a second. So that's one. And two is people tend to run experiments for a long time, and probably longer than they should.

(00:42:14):
Now, what do I mean by these two things? So what's interesting to me about this dynamic is experiments don't live in a vacuum. Companies have incentives. And in companies that really go all in on experimentation, one of the things that gets wrapped up in that is the incentives around experiments. Because if you go all in on experiments, a common thing you'll see is data scientists get judged based on how many wins they had that quarter. How do you get more wins? 

(00:42:43):
Well, it's easier to get wins when you're being incremental. And because it's important to have wins, you have to run them long enough to demonstrate that they're really wins. You're less willing to cut something off in exchange for trying something riskier.

(00:42:56):
So the big lesson of this Microsoft paper, it's called A/B Testing with what's called Fat Tails, which in lay terms just means you're running a business where there's potentially big opportunities out there if you look at the effects of the experiments that you run. There's a couple of lessons there about both trying a lot more stuff that's not all risk averse, and not necessarily running everything for so long. So really getting velocity up.

(00:43:20):
So you could see that there's a big incentive problem there, because the culture that says it's okay to fail big actually requires changing the terminology of wins. This is one of the things I hate most in A/B testing, I have to say. I get where it comes from. Experimentation was never historically in science about winners and losers. It'd be weird if it Ronald Fisher who's kind of the father of experimentation with his agriculture experiments talked about winners. I don't think that's necessarily how he talked about things. Experimentation is always very hypothesis driven. It's about, what are you learning?

(00:43:53):
And that's really an important distinction because what it means is if I go with something big, risky, and it, "fails," meaning that doesn't win. Nevertheless, if I was being rigorous about what hypotheses that's testing about my business, I'm potentially learning a lot.

(00:44:11):
So a great example of this kind of thing is that there's an important feature of marketplaces is badging. So sometimes, it's really important to have badges on your top-rated profiles or whatever, when people are searching. 

(00:44:26):
And without going too far into the details, a common finding with badges is that badges you think are going to be great actually turn out to be terrible. And one reason they're terrible is they focus too much attention on the badged folks, and pull too much attention away from the unbadged folks.

(00:44:44):
And if we judge that only in terms of winners and losers, you throw the baby out with the bath water, you're like, "Well that badging idea was terrible. So ditch that, no badges."

(00:44:51):
But that's not what it's telling you. It's teaching you something about how inventory is being reallocated, how attention's being redirected through the badges. And you really want to think not in terms of winning and losing, but learning.

(00:45:05):
So learning is a win. And I feel that that's a cultural thing fundamentally. It's very hard to somehow attach dollars and cents at the top to data scientists running experiments that fail, but learn. And ultimately, I think getting into that space where you experiment more, meaning you don't run all your experiments for quite as long and you accept the willingness to try experiments that are into the tails where you might fail bigger is a cultural thing. It's about saying that, "We're allowing that to be part of our social contract with our data scientists," or actually our employee contract with our data scientists, that not everything is just about how many launches you had and how many wins there were.

(00:45:45):
It's okay to say, "That's how I want to use experimentation," but if you're going to use it that way, then I would say don't be a, "We experiment everything," business. Because then I think you need some other way to deal with these big changes that teach the whole company a lot, but maybe can't fall into the incentives you've created for your data scientists.

Lenny (00:46:04):
This badging example is, I don't know if you're referring to the Airbnb example, but I actually led the launch of Superhost at Airbnb, which is the ultimate badge on Airbnb. And there was a lot of concern from the data team that it would destroy the marketplace, because they've built, as you've described, this very well-crafted ranking algorithm, with just a prediction of exactly as you described, which listings that guest is most likely to book and be successful booking. And then we're about to throw a badge on random listings in the results. And so this one data scientist on our team's like, "No, we can't do this. This is insane. We're going to destroy it all."

(00:46:42):
And we still went ahead with it. We ran an experiment showing the badge to some people and some not, actually, it was no impact at all. Which Superhost itself had no impact at all on the business as far as we could tell initially, which is also bittersweet because it felt like, "Why did we even work on this thing?" There was a slight benefit where a host felt better, they felt more satisfied with being a host, but I went exactly through what you described, so that's pretty funny.

Ramesh Johari (00:47:11):
Without necessarily going into the weeds on the data science of Superhost, I think there's a lot wrapped up in what you said. I guess another thing I'll say is that I'm a big believer that you don't throw your understanding of the business out the window when you process experiment results. And it's partly, I guess what I mean by this is data science is really about accumulation of evidence. It's never about one finding in isolation. And so another kind of trap I think is to sometimes say, "Well, I hit stat sig on my A/B test, green light. It's all go."

(00:47:47):
And I think you had Ronny Kohavi on your show, and he made a similar point that there are different levels of evidence, and just having an outlier A/B test that goes against everything you believe about your business doesn't mean that you somehow have controverted all your knowledge. And I think that's one side of it.

(00:48:05):
The other thing is you can't always measure everything that's important that's needed to really develop a full sense. So with Superhost, one of the things that's hard to measure is the long-term impact of Superhost. Because in the short run, Superhost causes a rebalancing of inventory. There's going to be winners and losers. Part of Superhost is actually about retaining hosts that get the badge over a longer period of time. Recognizing that hypothesis actually says something about maybe how long the experiment needs to be run or what kinds of data analyses need to be done. 

(00:48:38):
And in the end, if you can't do that, you can't run it long enough, or you can't do that data analysis due to sparsity of data or lack of data to address the question, it matters what you bring to the table. What are your beliefs about that?

(00:48:51):
So what I like to tell people to do there is I like to push people to be what's called quantified rather than data-driven, which is, okay fine, some things we can't measure. But maybe you've got a leadership team with different beliefs about what they think the retention value of Superhost is going to be, and they might be all over the place.

(00:49:10):
You can process your experiment results in the context of these competing beliefs. It's almost like a prediction market kind of a thing. And start asking, "Well okay, if this is what we believe about our business, this is what the data is telling us out of the experiment, let's put those two together and ask, is this enough for us to make the bet that we're still going to go with it?" Even though maybe that short-term test you ran was flat.

Lenny (00:49:31):
That's actually exactly how I think of Superhost looking back. It was a great idea. I'm really happy. I can't even imagine Airbnb without that, even though there's no evidence, at least initially, that it made any impact. I'm guessing they looked at it again, and maybe there's something that came out of it. But even if it had no impact, it just feels like it made the marketplace better. And that was a big learning for me. It doesn't need to always drive a metric that you can measure. There's just like, this is the way it should work.

Ramesh Johari (00:49:59):
So one of the reasons the thing you said happens is because marketplaces are a little bit like a game of whac-a-mole, okay? And what I mean by that is, so narrowly in the context of Superhost, because you're redirecting attention to some hosts at the expense of... It's not even obvious if bookings can really go up. Maybe you get lucky and maybe you get a bunch more bookings. One reason you probably wouldn't expect that in the first place is there's only a limited number of Superhosts. How many more bookings are they going to be absorbing because of all this extra attention? And you're taking attention away from other people. Without doing any data analysis, my prior would've been that booking should probably go down.

(00:50:33):
And one example that I came across with one of the companies I worked with that I love is we were working together over a period of time, and in a month, we looked at some of the data and it suggested that our new supply side was having a pretty bad experience. Say, "We got to do something about this."

(00:50:55):
So what we decided to do is build some custom bespoke features that were really going to direct them to more experienced folks on the other side of the market. Good. And then lo and behold, pretty soon those metrics start to look better. But then we're looking at it, we're like, "Wait a second. Now the existing folks on the other side are having a worse experience."

(00:51:12):
So you kind of whiplash around. You're like, "Wait a second, we better do something about that." So we take them, we try to match them up with the more experienced folks. And now suddenly a month after that you're like, "Wait a second." And your metrics just keep moving around.

(00:51:24):
And that's because the whac-a-mole game here is ultimately, a lot of marketplace management is moving attention and inventory around. Sometimes you get lucky and you really expand the pie for everybody. But I think Servaes Tholen, who was CFO at Upwork that I got to know there and then went to Thumbtack later, he had this line when he came to visit our class that I love, which is, "You have to recognize when you run marketplaces that many of the changes that are most consequential create winners and losers. And rolling with those changes is about recognizing whether the winners you've created are more important to your business view than the losers you've created in the process." And it's a hard reality, because nobody likes to articulate the idea that a feature change is hurting some of the people in your marketplace. But because of this fundamental constraint baked into how marketplaces work, many of the things that we would choose to do and the reallocation they create can't necessarily create observed high expanding wins in the short run. You're often making bets that that's where you're headed, partly through the reallocation that you're doing right now.

(00:52:30):
And so I think that's interesting about Superhost to me is that partly points to thinking about, what's the objective you would've defined, the metric you would've defined in the short run that captures this idea of a trade-off?

Lenny (00:52:42):
That's a great way to think about it. I wanted to come back to this idea you're sharing of maybe you should run experiments more quickly, not wait for stat sig, have a culture of learning versus impact. In practice, it's very difficult, because people are measured by impact. There's performance reviews, there's promotions, there's how much impact did this team drive, are going to look at their experiment results? You've worked with a lot of marketplace companies, a lot of different companies. Is there anything you've seen about something you could do to help the company shift and actually work this way, while also recognizing success, and who's doing great, who's not, which team's driving impact, who's not?

Ramesh Johari (00:53:22):
Interestingly, it's actually an active area of research for me now. What I mean by active area of research is I care a lot about the incentives that we create for data science through how we set up reward mechanisms. So there's a couple things I think that could be helpful, that are maybe there may be a little bit less about... Maybe I'm not going to directly answer the question you ask, because I think that's a hard one, right? I think I recognize that measurement on impact is critical. Well, let me answer that actually from the most obvious way first. I think there's a cultural issue here that's really critical. 

(00:53:56):
One of the things I often find is that my PhD students, our PhD students here often go off and get great data scientist jobs. And in one sense, they're doing amazing stuff. They apply really technically sophisticated methods. But when I look at the problems they're working on, they're often more at the margins of the business than they should be. 

(00:54:13):
And it's a cultural thing. It's basically because if you're measured narrowly on impact and that's all anyone sees around you, then it's very hard to engage with the creative aspect of business change and the strategic aspects of business change. 

(00:54:26):
So the cultural aspect there is, I think it's partly incumbent on the leaders to expect something more of their data scientists. And what I mean by expect more is that you expect them to do more than deliver narrowly defined, statistically rigorous results to you in their reports. You're actually expecting them to talk also about what they're learning about the business in the process. So where that's headed is there's this concept of being hypothesis driven, which is like the technical phrase. What does that mean? Again, in a more lay sense.

(00:54:58):
What it means is tests aren't going to be defined only in terms of winners and losers, that each test should also say something about what will we learn about a business flow, a funnel, preferences of the guests, preferences of the hosts. What will we learn about their demand elasticity if we're changing prices around? These kinds of things. So it's possible to articulate in an experiment doc, a launch doc, what are the hypotheses that are being tested? So that's one thing I would say is just culturally, setting the norms that learning is part of the discourse, and it's expected actually I think is important.

(00:55:33):
But the other thing I would say that's maybe a little bit more about programmatically, what could a data science platform team do? A funny thing about experiments is that we throw past learning away effectively. And this is just an artifact of how we analyze experiments, that the statistical methods used typically, P-values, confidence intervals, these fall into a branch of statistics known as frequentist statistics. And the idea behind frequentist statistics without being overly technical is just I let the data speak for itself. There's no beliefs brought to the table about where that data came from.

(00:56:10):
But if you think about this in a company, in A/B testing a company, it's a weird thing, right? Because I might've run 1,000 A/B tests in the past on this exact same button, or call to action, or color, and now I am going to completely ignore that and focus only on this. 

(00:56:23):
So there's ways to take the past into account, to build what's called a prior belief before I run an experiment, and now take the data from the experiment, connect it with the prior, to come up with a conclusion of, "Okay, in light of the past plus this experiment, what's it telling me about the future?" And that falls broadly under the category of what's called Bayesian A/B testing. 

(00:56:46):
So that's one of the things I think can help culturally, weirdly. It's a super technical thing, but I think it can help culturally, because what it's doing is it's now rewarding people for contributing information to that prior. And I think it then becomes possible to say, "Your experiment that failed actually moved our prior." And that's an important thing, because by doing so, you're now altering how we're going to think about this flow or this pricing plan in all future experiments.

(00:57:14):
So there's an information positive externality, positive network effect that's generated for the rest of your business if I can somehow encode what you learned into the analysis of future experiments. So this is one thing. There's strong connection between the culture and incentives of A/B testing and the ability to actually incorporate past learning into these prior beliefs.

Lenny (00:57:35):
I love that you're doing research in this area. We should bring you back when you've completed it and have the ultimate answer for everyone to change how they operate. 

Ramesh Johari (00:57:42):
Yeah, one of the great things about professors is we never complete anything and never have ultimate answers.

Lenny (00:57:47):
Oh boy.

Ramesh Johari (00:57:47):
Yeah, I'll do my best though.

Lenny (00:57:50):
This touches on a really interesting concept that you shared with me around how, just learning isn't free. People think that they could just learn a bunch of stuff and there's not a cost to it. I'd love for you to just chat a bit about what that means.

Ramesh Johari (00:58:02):
Let me start with an anecdote, that I just absolutely love this anecdote. I use it every year in class. So I was talking to a real estate platform, and they had a marketing data science manager who's basically responsible, as many marketing managers are, for allocation of ad spend across different channels.

(00:58:22):
And what they discovered had happened at the end of the year is in one hand, the team had done great, but the manager had held out some subset of arriving visitors, not showing them any of the innovations they were making.

Lenny (00:58:39):
Like a holdout group? 

Ramesh Johari (00:58:40):
Yeah, exactly. What's called a holdout group in experimentation. And one thing about this holdout is it wasn't authorized. That's not the way things are supposed to work. They've got their ad spend, allocate out your ad spend, great. So at the end of the year, they looked at the hole out and they're like, "Wow, that cost us a couple million dollars, something in that range, and it's not a trivial amount of money. What's the deal? What were you thinking?" Basically. And of course the answer was, "Well, I get that I cost you that much, but number one, now you know what my team's worth. And number two, you would never have had that answer unless I'd done that on my own."

(00:59:16):
Now, why is that so powerful? I think what I find so interesting about experiments is that when you don't know something, it seems not even a question that you would allocate some of your samples to all options, right? Treatment and control. I have two different ways of doing something. I don't know which one's better, so of course I'll give some samples to each. After the fact you're like, "Treatment was better. What the heck were we thinking? Why'd we give all those samples to control? That doesn't make any sense now." There's this great Seinfeld clip where he mentions getting a bill at the end of a large luxurious meal, and people stare at the bill like, "We're not hungry now. Why'd we order all this food?" So it's the same thing. I mean, you know treatment's better now. Why'd you waste all those samples on control?

(00:59:59):
And I think that is such a powerful observation that you have to put yourself in the frame of reference of when you didn't have the answer. And at that moment, what you're essentially saying to yourself is that it's worth paying to learn the answer. I think it sounds obvious the way we're saying it now, or this anecdote of the marketing manager and the holdout sounds obvious. What's culturally not baked in I think is that idea. And the reason I say it's not culturally baked in, by the way, is because of the language of winners and losers. Because if we use that language, we're implicitly saying is that we wasted time when we ran an A/B test on loser. If I reward you for shipping winners, then what I'm really telling you is all the time that you spent testing out failures was wasted time.

(01:00:46):
And I think, of course, you don't want to keep data scientists around who regularly are just generating failures. That's not my point. 

(01:00:54):
But my point is there's a disconnect there. On one hand, we can all look at the story of this marketing manager and chuckle at it. And yet, every day we're instantiating language and processes that are reinforcing that same theme, which is essentially trying to say to you, "If you're wasting samples on things that don't ultimately end up being a winner, then the act of doing so is a failure."

(01:01:16):
So I really feel that that idea that you have to pay to learn, again, it's a cultural thing, but it's also an education issue for businesses are populated by people of all stripes. Not everybody comes from a data science or experimentation background. And this idea that learning is costly is not natural, actually. It's not natural as a matter of human nature. It's certainly not natural as a matter of running a business.

Lenny (01:01:41):
I love that example of the real estate platform where it's very viscerally, clearly cost. They lost because they didn't roll out experiments to this group for a long time. Such a good example of this idea in action. 

(01:01:55):
You mentioned star ratings. I know you spent a lot of time on designing rating systems. Sorry, I didn't mean to imply star ratings. That's just one implementation. Rating systems in general.

(01:02:05):
So maybe just to keep it focused, say a marketplace founder is trying to decide and design how they do ratings, and reviews, and things like that. What's a couple pieces of advice you'd give them for how to do this correctly? And is there a model marketplace you'd point them to like, "These guys really do it really well"? And I know it's super specific based on the marketplace, but is there one just like, "They really nailed it"?

Ramesh Johari (01:02:30):
Oh man, that's a tough one. I think I'll answer the second part first. I don't feel like anyone's really nailed this. Yeah, I think there's a lot of innovation that's happened, but I think fundamentally, we're still playing with the same kind of tools that we had when eBay and Amazon first started thinking about how to do rating systems ages ago. 

(01:02:48):
And part of the reason we haven't nailed it is because there's a lot of dynamics in play that lead to what's called rating inflation, where if you look at ratings over time in the marketplace... One of my colleagues, John Horton, who was a professor at MIT and has worked very closely with Upwork, we worked together when I was at oDesk, he was the staff economist there. He's written a couple of really nice papers with this empirical phenomenon that over time, you see the median rating inflating, let's say on marketplaces like oDesk, like Uber, like any of these.

(01:03:16):
And there's a lot of reasons for this, but one of them is just that there's a reciprocity issue, which is it's effectively, from your perspective, it's kind of costless if someone says to you, "Hey, please leave me a nice rating." And if you're seeing them or you're interacting with them, most people don't want to be mean. So that happens. 

(01:03:35):
But there's another aspect of it, which is norming. As the ratings in the marketplace go up, they get normed, so that now you're in a condition, you're like, "A four star rating. I'm really screwing this person over." Whereas maybe when the marketplace started, you didn't think that. 

(01:03:47):
So definitely one thing that we worked on in our research was to think about renorming, the meaning of some of these labels. And renorming could mean something like rather than the star ratings just being poor to excellent, the top rating has actually exceeded expectations. You could go one step further and you could say, "How did this compare to this experience you had in the past that you rated really highly?" And Airbnb had something like this in place, where they would actually ask you to compare, or ask you questions about expectations.

(01:04:19):
I find that that's really valuable because it's easier for people to say, "That was good but didn't exceed my expectations. That was good, but definitely not better than this amazing stay I had two months ago," than it is to say, "Well, I'm going to ding this person and give them four stars." So that's one issue.

(01:04:36):
And I think another thing I want to point out for any marketplace founder is that something you want to be really careful about is the concept of averaging and whether are the implications of averaging. And that's because a default for many marketplaces is to just average the ratings that people get. It feels very natural, right? Lenny's got five ratings, let me average them.

(01:04:57):
And that actually has some pretty important distributional consequences for the marketplace. Distributional in the sense of who wins, who loses. And that's because if you're averaging and you're really established on a platform, think of a restaurant on Yelp with 10,000 reviews, it's irrelevant what the next review is. It doesn't matter. Nothing's moving it at that point.

(01:05:17):
If you're new and you break into that market, and your first review is negative, you might be completely screwed. In fact, there's some early work on eBay that showed that if your first rating's negative, that could actually immediately cause an 8% hit on your immediate expected revenue, say nothing of long-term consequences. Subsequent work has found that that's a significant indicator of potential exit from the platform, just because now it's very hard to find work. And some platforms do things like maybe they won't show your ratings until you've accumulated a few.

(01:05:46):
But in the end, this kind of distributional fairness aspect of averaging is pretty significant. And one of the recent papers that we've written is trying to get platforms to think a little bit about that. There's ways to address that interestingly, through the same concept of a prior. And the prior basically says hey, if someone comes into the marketplace and instead of averaging them, I average them together with a prior belief, then maybe what that prior belief does, it says, "Yeah, you got one negative rating, but maybe you got a little bit unlucky," and maybe my prior belief is something which actually pulls your rating up a little bit and allows me to still have you alongside others in the marketplace to give you a chance at getting work, getting rides, etc.

(01:06:28):
So I believe pretty strongly in this kind of distributional fairness element of designing rating systems. I think it's been understudied. And I'll say in general actually, I think rating systems are understudied, which to me is astonishing. Because the biggest change from those Agoras and Trajan's Market elements of those kinds of markets, to me the biggest change is that we get to see what happened with our matches.

(01:06:52):
So as a data scientist working on marketplaces, I feel like it's incredible that more of us don't spend our time thinking about what we're learning from the matches, and what these rating systems are telling us, and what the impact of that is on who wins and who loses in these markets, kind of thinking about the social implications of these things. So that's something I'm pretty passionate about.

Lenny (01:07:14):
I also led the review system flows for a while at Airbnb, and one of the things I'm most proud of is launching what we call double-blind reviews where you don't see the other person's review until you leave your review. The intention was to create more honesty and more accurate reviews.

(01:07:32):
It turned out the biggest impact was review rate went up, because people get this email, "Ramesh left you a review. If you want to see it, should leave a review." And that really increased review rate, which gave us more data. And it was a really fun experiment to work on. 

Ramesh Johari (01:07:44):
There's a great concept in the literature on rating systems called the sound of silence, which is this idea that there's a lot of information in ratings that are not left. So Steve Tadelis, who's a professor at Berkeley, he had a really nice paper with some folks at eBay talking about what they called effective percent positive, where rather than normalizing just by the ratings, they normalized by including ratings that weren't left. And what you found was this was much more predictive of downstream performance of a seller. So there's a lot of information in that lack of a response. So it's cool that you're able to get more of that out.

Lenny (01:08:23):
So much easier just to not leave a review than leave a bad review. Right? The downside to you is just much better. Oh man, marketplaces are so fascinating. I could see why a founder would want to be a marketplace founder, because it's just such an interesting space. And hearing your feedback of, no, you're not a marketplace founder. Let's think about the problem you're solving. And it might be a marketplace, might change people's minds. Also, I feel like there's a podcast episode in every topic we touched on. I know we just scratched the surface a lot of things.

(01:08:52):
I know you got to run. Before we get to our lightning round, is there anything else you wanted to highlight, touch on, leave people with that are maybe working on marketplaces, thinking about a marketplace?

Ramesh Johari (01:09:01):
I think one of the high level points I would make, and like you said, there's an entire podcast in this topic, is that I think people want to imagine LMs and AI driven data science automating out large parts of what it means to do data science in industry. And I think that's probably the wrong perspective. In some mundane sense, that's true. It's easier for me to code than it used to be before. It's easier for me to develop visualizations than it used to be. I can make dashboards faster. So programmatically, I think it's true in some basic sense.

(01:09:35):
But what I believe pretty strongly, and I teach data science here, and my students are asked to use LMs and generative AI on a weekly basis on all their assignments. So I've got an up close and personal beat on this, but I believe very strongly actually is what AI has done for us is it's massively expanded the frontier of things we could think about our problem, hypotheses we could have, maybe things we could test. It's just an astronomical explosion of explanations, and ideas, and principle.

(01:10:06):
And I really think actually what that does is puts more pressure on the human, not less. I think it becomes more important for humans to be in the loop in interacting with these tools to drive the funneling down process of identifying what matters, at all levels. That ranges from you're carrying out a data scientific analysis, and now because you've got these tools, you can hypothesize 10 explanations, maybe 100 explanations. Which of those are you going to focus attention on? What are you going to tell other people to focus their attention on? To you're running experiments, used to have 10 creatives you're testing for a marketing campaign, you got 1,000 creatives, you're testing for that marketing campaign. Maybe that completely changes the game of what it means to run an experiment. What are you actually looking for now? How do you evaluate that you found something that was good enough?

(01:10:52):
And I think these questions are not getting enough attention. I think people are looking for the automated tool that really cuts the human out. But what I've seen so far, and again, who knows? By 2024, I might have a totally different answer for you. I don't think so. But at the moment, what I see is that humans have actually become far more important to the productive data science loop, not far less.

Lenny (01:11:16):
Such an important point. I feel like we need to add AI corner to this podcast where we always think about, how does AI impact what we're talking about on this podcast?

Ramesh Johari (01:11:23):
Yeah, I can see that. I totally see that. 

Lenny (01:11:25):
Okay, we might start doing that. Ramesh, with that, we've reached a very exciting lightning round. I've got six questions for you. Let's try to knock through them so you can go teach your class. Are you ready?

Ramesh Johari (01:11:35):
I am ready.

Lenny (01:11:36):
All right. What are two or three books you've recommended most to other people

Ramesh Johari (01:11:40):
When it comes to books, I have one I love that I start with always, which is How to Lie with Statistics. It's a tiny book, Darrell Huff from 1954, which is just for anyone that likes data at any level, it's such a fun read. It's a great book. 

(01:11:55):
The second thing I recommend to people, and actually this is true even for people who are not expert, is David Freedman was a statistician at Berkeley who passed away in the 2000s, early 2000s. His writing was fantastic in getting us to think hard about process. He was especially fond of what he called shoe leather statistics, where you rolled your sleeves up, you got on the ground, boots on the ground, really getting in there, really trying to understand your data.

(01:12:27):
His writing is fantastic, his explanations are fantastic. He has a few different books at different levels I think people would love reading. Most importantly, what I like about it is he puts such emphasis on driving evidence and understanding of your processes that generate data. And I find often, data scientists don't even look at examples.

(01:12:44):
So at oDesk, it meant are you looking at actual jobs, and what's actually going on in your product before you're trying to do data science on it? So I think that's a Freedman insight, Freedman mantra, and so his writing is great.

(01:12:58):
The last one I was going to mention has nothing to do with data science or anything. It's called Four Thousand Weeks by Oliver Burkeman. I'm not a huge self-help type person, but I really like this book a lot. I think it's a little bit stoic in its approach, like stoic philosophy. But the basic point is you're only on earth somewhere in the neighborhood of 4,000 weeks, and my wife and I have this term we call infinite Q, which is no matter what you think you get done on a given day, more stuff's going to just keep coming in.

(01:13:26):
And he basically says that recognizing that is liberating. Because once you recognize it, it doesn't matter what you do. You're always going to have too much to do. There's no point in stressing out about having too much to do. And just that small shift of mindset than puts a lot more attention on the usual thing people worry about, which is, where do I want to prioritize my time? So he has a great way of writing about it, some concrete rules of thumb to help manage that way of thinking. And yeah, I think it's a great book.

Lenny (01:13:52):
What is a favorite recent movie or TV show?

Ramesh Johari (01:13:55):
I am a climber, and one movie that I really liked was The Alpinist. I know a lot of people have seen Free Solo, but for anyone that kind of likes that genre, I would recommend they watch The Alpinist.

(01:14:06):
I think climbing is an interesting sport because has very much a psychological aspect of it. And I think that movie is pretty good at this meta level where you reflect a little bit on, what does it mean to make a movie about people who are obviously putting themselves into such risky situations? So I really enjoyed that.

(01:14:25):
On TV, we've been watching Only Murders in the Building, but I'm enough episodes behind right now that I probably won't say anything more, because I am trying to avoid any spoilers and I'm sure there's people out there trying to do the same. So great show though on Hulu.

Lenny (01:14:39):
What's a favorite interview question that you like to ask candidates that you're hiring?

Ramesh Johari (01:14:43):
I interview people probably that are a little bit different than most of your podcast listeners. But that said, there's one question I like to ask a lot, and that's if you imagine... Often in our interviews in academia, whether it's grad students or faculty will ask people about their plans.

(01:15:00):
And what I like to ask people is, "Okay, now imagine everything works out, all the challenges you're facing work out, all your plans work out, everything hits the top end of your vision for what this could be. What do you imagine is the impact of having done that? Who's being impacted by that? Why is that a big deal that happened?"

(01:15:20):
And I find that's a really valuable question to ask, because first of all, many people haven't thought about that. We're so short-term focused, we don't even think, "Boy, if everything worked out, what would be the big deal because of what I did?" Startup founders tend to be better at this than most people obviously.

(01:15:35):
But another reason I like it is because you will find in that conversation that their vision expands a little bit of additional spheres that are touched or impacted by what they're thinking about doing. So on both sides, it's kind of a revealing question, I think. So I find that important for my line of work, but my hunch is that might be useful for some of your listeners too.

Lenny (01:15:57):
Yeah, such a unique perspective on interviewing, versus most of the guests that I interview in tech company.

Ramesh Johari (01:16:03):
Yeah, normally there's a coding question, right? I should say I would never ask a coding question post November 2022 after we got AI to help us code. I think it's a superpower.

Lenny (01:16:15):
AI corner. What is a favorite product you've recently discovered that you really like?

Ramesh Johari (01:16:22):
I also really like cycling. And I'm not ashamed to admit that I think that e-bikes are the greatest thing for cycling. Admittedly, I'm late forties, so maybe I'm the right target demographic too. But yeah, I love my e-road bike. It's great, because it's not one of those with a throttle, you have to work, but it kicks in just when you're on your sixth hill and you don't want to go up the last hill anymore on the way home. So yeah, that's amazing. I think that's just transformative for people that like cycling, but have busy lives.

(01:16:51):
And I think another one that my son who's 10 roped me into actually, is we were in Santa Cruz browsing at a kitchenware shop of all places, and he saw an outdoor pizza oven, a tiny portable one. And he just did research for two weeks and insisted we get one. 

(01:17:07):
So he got one over the summer, and after we got it, he refused to eat pizza out anymore as a 10-year-old. So maybe that's the best thing I could say about the quality of pizza you can get from a home outdoor portable pizza oven.

Lenny (01:17:20):
Oh my God, I'm hungry. I am going to go have to get some pizza now. What is a favorite life motto that you like to repeat to yourself, share with folks, find useful in your day-to-day?

Ramesh Johari (01:17:31):
A lot of my work involves talking to students of all stripes. And I guess these students go on to be data scientists, go on to be founders, and a lot of them go in the tech industry. So maybe in that sense, that advice is relevant. 

(01:17:43):
My main thing I tell people is slow down. I think what I've found has been happening, is we're so convinced that speed is the way you're going to find the right answer, that I just don't think we slow down to develop meaningful mental models of the things we're doing. That's certainly true in the research projects I work on. It's consistently true when I talk to people in business, and I ask them about their... By mental model, I just mean if you're running a marketplace, what is your model of what people care about? What makes people stay versus leave? What makes matches work versus not work? All those things shape a roadmap in your mind. And I think a lot of roadmapping, a lot of execution, paper writing in academia has all just become far more fast-paced, at the expense of deeper thinking about these kinds of structural features of the thing you're building. 

(01:18:41):
So with my students, but also I think with people I interact with in industry, I think slowing down is actually more of a virtue than it's given credit for.

Lenny (01:18:50):
Very similar to a motto that a recent guest shared, which I think was go slow to go fast, or stay smooth to go fast.

Ramesh Johari (01:18:59):
Yeah, I like that. Maybe I'll pilfer that, when I go talk to my grad students [inaudible 01:19:03].

Lenny (01:19:04):
Final question. You're a professor at Stanford University, which sounds incredibly cool. What's something about being a professor at Stanford in particular or in general that would surprise people, either good or bad?

Ramesh Johari (01:19:17):
Yeah. I mean, we've had a rough ride, as everybody probably knows. Stanford's been in the news for a lot of not so great reasons, I think over the last five years especially. 

(01:19:29):
So I don't know if this is the right kind of surprise, but I think one thing that I find really energizing at Stanford is people have never asked me for credentialing here. And what I mean by that is that I came from a bunch of other good schools, and obviously I've spent time in industry with a lot of great companies. And a kind of cultural dynamic that can often develop is, "Well, before I'm going to talk to you, I want to know something about why you're worth talking to. Give me your credentials. Where are you a grad student or where are you a professor? Tell me about yourself first."

(01:20:10):
One of the things that I found very surprising when I came here is just how that never happened at any level. Grad students tell me this all the time. Go talk to someone across campus and just launch right into a conversation about how your X meets my Y, and we have something we could do together. As a faculty member, it happens all the time. I just had a conversation a couple days ago with someone about effectively a marketplace of experiment designs for nano fabrication here, which is totally out of left field for things I do, and yet seamless. Our conversation was about the substance rather than the credentialing.

(01:20:46):
I really think part of the reason for that is that Stanford is sort of unique in that it doesn't have a weakness across the board. We have strong professional schools, law, business, medicine, strong engineering schools, strong humanities and social sciences. And then that and the weather is what I usually tell people honestly, which matters a lot. People are willing to walk anywhere. I think those things combine to create a culture and an environment where you don't credential everybody.

(01:21:09):
And I think that means a lot. I think that's something that I haven't found elsewhere. And if people wanted to know something about what's Stanford's like on the inside, I think that's one aspect of it that probably isn't discussed very much. I think that's part of what makes it really fun to be here.

Lenny (01:21:27):
It's also an incredibly dreamy campus, that is very joyful to walk around. That helps, I'm sure. Ramesh, I feel like we got people's brains tingling. I think we've created new marketplace founders, and also convinced people maybe they aren't marketplace founders. So maybe we netted out zero new marketplace founders. Two final questions. Where can folks find you online if they want to reach out? And how can listeners be useful to you?

Ramesh Johari (01:21:49):
I think the easiest way, if someone's interested more on the industrial side is probably LinkedIn. You send me a message or connect there. Also, because I'm an academic, I have my own Stanford webpage, and it's pretty easy to figure out how to find me there as well.

(01:22:02):
And how can listeners help me? I kind of feel the most important thing that someone listening to this could do is take forward some of the messages that came out in terms of what it means to be data literate. And I think there's a lot you can do to educate yourself there. 

(01:22:18):
Maybe one final thought I'll share is that in the same way that AI generates a lot of ideas, AI also generates a lot of prose. And in data science, that can actually be deadly because you're getting more explanations that sometimes maybe are extraneous. 

(01:22:35):
So taking that as a little vignette, I think that what the world needs is data literacy on the part of people interacting with these tools and with each other. So that's the thing I care most about. The things I teach, the things I do research on, they're all connected to that theme. And so that's where I'm pretty excited. I do work with companies regularly, and so if there's interesting opportunities that fall in the sphere of stuff we've discussed on the podcast, always happy to listen.

Lenny (01:23:00):
Awesome. I think we've made a dent in helping people become a little more data literate. Ramesh, thank you so much for being here.

Ramesh Johari (01:23:07):
All right. Thank you so much, Lenny.

Lenny (01:23:08):
Bye everyone.

(01:23:11):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

