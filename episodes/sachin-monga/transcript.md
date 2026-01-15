---
guest: Sachin Monga
title: Building Substack | Sachin Monga (Substack, Facebook)
youtube_url: https://www.youtube.com/watch?v=zKP2HrMc23s
video_id: zKP2HrMc23s
description: 'Sachin Monga is the Head of Product at Substack, a platform that I personally
  use every day, and love. Before Substack, Sachin co-founded an app called Cocoon,
  which he ended up selling to...

  '
duration_seconds: 3660.0
duration: '1:01:00'
view_count: 5414
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- onboarding
- metrics
- prioritization
- analytics
- funnel
- conversion
- subscription
- hiring
- culture
- management
- strategy
- vision
---

# Building Substack | Sachin Monga (Substack, Facebook)

## Transcript

Sachin Monga (00:00:00):
I really think that we're just starting into this golden era of what it might mean to be a writer on the internet. The economic model for supporting great writing on the internet has been generally pretty terrible for the entirety of the internet's history. In the early days of Substack, there's a couple of these glimmers of hope where you'd have people like Matt Taibbi or Bill Bishop, some of the early writers on Substack that were really well established writers who were clearly just being undervalued and now could come to Substack and see their true value.

Sachin Monga (00:00:33):
And that was awesome. That was really cool to see. But in the last year or so, even in the last few months, I think there's been so many really interesting success stories now from writers who might not even consider themselves writers. People who are able to make a living, maybe even make a fortune just doing great work and not needing to have millions and millions of viewers or play the attention games of other networks, but just do really high quality work and have a relatively small number of people value it highly enough to pay for it.

Lenny (00:01:07):
Welcome to Lenny's Podcast. I'm Lenny, and my goal here is to help you get better at the craft of building and growing products. Today, my guest is Sachin Monga, who is currently the head of product at Substack. Before Substack, he had a startup called Cocoon that he sold to Substack. And before that, he spent over seven years at Facebook working on the video and camera products, building out the developer platform, and leading the ads growth team. In our conversation, we dig into all things Substack, what it's like to build product at Substack, how different it is to work at a startup versus a big company like Facebook, the future of the Substack product.

Lenny (00:01:42):
We also spent a lot of time on what I venture to say will go down in history as one of the most legendary growth features ever created, the Substack recommendations feature. Substack as a product and a company has changed my life and allowed me to do the work that I do now, and it was such a treat to be able to chat with Sachin. I hope that you find this conversation as interesting as I did. With that, I bring you Sachin Monga. Who has an opinion on internal tools? Internal tools are something you probably don't think about until you have to, or it probably didn't even occur to you to think about them.

Lenny (00:02:18):
But if you work at a big company, you probably have a bunch of one-off custom apps or dashboards that are laser focused on just one job to be done for one specific team or just one role, and they're always such a huge pain to build and maintain. And that's why I'm such a big fan of Retool and why I think Retool is so popular. Retool allows teams as small as just one person to build a suite of custom internal apps in a fraction of the time that you think it takes. The productivity gains of custom apps is now within reach, not just for large enterprises but for small teams as well. And as you scale, your company Retool scales with you.

Lenny (00:02:54):
Snowflake saves about 26 hours a week of manual spreadsheet work with custom internal apps built on Retool. Amazon uses Retool to handle GDPR requests. Thousands of teams at companies like Coinbase, DoorDash, and NBC collaborate around custom-built Retool apps to operate with greater efficiency. Maybe you've thought about using Retool before, but just haven't and I'm here to tell you that now teams of up to five can build unlimited Retool apps for free. Get started today at Retool.com/lenny. Do you want to reduce friction in your onboarding flow? Then let me tell you about Stytch, and that's Stytch with a Y.

Lenny (00:03:34):
Stytch is on a mission to eliminate friction from the internet. There's starting by making user authentication and onboarding more seamless and more secure. They offer super flexible out-of-the-box authentication solutions for companies of all sizes. From email magic links to SMS passcodes, one tap social logins to even biometrics, Stytch is your all-in-one platform for authentication. Stytch customers have been able to increase conversion by over 60% after spending just one day integrating. And with their API and SDKs, you can improve user conversion and retention and security all while saving valuable engineering time.

Lenny (00:04:13):
Your engineers will come and thank you for using Stytch, because Stytch keeps you from having to build authentication in house and the integration process is super fast and super smooth. To get $1,000 in free credits, just go to Stytch.com/lenny to sign up, and that's Stytch with a Y. Sachin, welcome to the podcast.

Sachin Monga (00:04:36):
Thanks for having me.

Lenny (00:04:37):
I'm actually really excited to have you on. I've told you this before, I've told the founders before, Substack has changed my life in so many ways. There's no way that I would be doing what I'm doing now if not for Substack and just like the magical combination of features that you all built. I'm also just really curious about how you all build the platform, where it's going, how it all works behind the scenes. Again, thank you for being here.

Sachin Monga (00:05:01):
I'm so happy to be here, and that's so great to hear.

Lenny (00:05:03):
Just to set a little context for folks, can you just talk about how you got to Substack? You're currently head of product at Substack. What was that journey to Substack?

Sachin Monga (00:05:12):
I joined Substack around a year ago now exactly through an acquisition. I'd started a company called Cocoon about three years prior to that with my good friend Alex Cornell. Cocoon is not like Substack. It was essentially a little photo sharing app for close friends and family, but there is a common thread which led us to Substack, which was prior to starting Cocoon, Alex and I had both worked at Facebook for a number of years and had worked on effectively the same problem of helping people share more with their friends and family and had all these ideas for what an idealized experience might look like.We just kept running into the wall that you run into when ultimately advertising is the business model that is powering this whole thing, and what that means is you need to accumulate a lot of time spent and attention and convert that into basically sellable eyeballs. But it's not that hard to imagine what a better solution would be. It's just that ads as the business model made it really hard to pull that off. Cocoon was in a lot of ways like a journey to explore what that might look like for this one particular use case of just helping you feel close to a handful of people.

Sachin Monga (00:06:14):
We always looked up to Substack as a really good example of basically that same principle, which is if you imagine rewiring the internet around paid subscriptions, direct subscriptions between, in Substack's case, readers and writers, what could that unlock and could it unlock a clearly better user experience? We looked at Substack as a real inspiration and an example of that really working out and got to know the founders pretty well and had a few conversations and realized that even though the blogging software and the photo sharing app are pretty different, our underlying motivations were really consistent.

Sachin Monga (00:06:46):
It was a bit of a match made in heaven and the whole team joined Substack a year ago. I've been privileged enough to get to lead the product and design teams, and it's been a blast so far.

Lenny (00:06:57):
Before your startup, you're at Facebook for a number of years, is that right?

Sachin Monga (00:07:00):
Yes. I started in 2011 there on the growth team and had the chance to work on a bunch of different teams there, growth, platform, ads, and then eventually the team we called Sharing, which was helping people share more in the main Facebook app.

Lenny (00:07:12):
Sweet. I want to spend a little time on that, but coming back to Substack, I'm curious just how the product team runs. How many PMs do y'all have? How is it structured? How are you thinking it'll evolve as you scale? What can you share there?

Sachin Monga (00:07:25):
Sure. Maybe to start from when I started at Substack, we had zero PMs. We had a handful of designers. We had maybe 15 or so engineers. I think we're coming to the close of this kind of one-time inflection point of becoming a product driven company and having a product process and structure and PMs and full stack product teams. When I started at Substack, there was really not much of this. We're still pretty early, but we have something going now.

Sachin Monga (00:07:51):
We have four product managers in addition to myself, and we have three essentially kind of full stack product teams now that have a PM and an engineering manager, a data person or a designer, engineers and things are starting to roll. We're finally emerging from this transition phase and it's been super fun.

Lenny (00:08:10):
What are these three teams?

Sachin Monga (00:08:11):
The three teams are: we have a writer team that serves writers, we have a reader team that serves readers, and we have a growth team that does growthy things. I should mention, we have a fourth engineering team that's like the systems team that doesn't have a product manager on it, but is keeping the lights on and helping us scale.

Lenny (00:08:28):
Awesome. That makes sense. You currently align it around the type of user plus the platform stuff. Do you have a sense of where this might evolve over the next few years just structure wise? Do you think it'll stick to that? Do you have a plan of how this might radically shift as you grow?

Sachin Monga (00:08:43):
Yeah. I'm actually kind of shocked that it's lasted this long and stayed consistent. I remember at Facebook, we would change our team structure what felt like every three months or six months and just have a reorg every once in a while. Part of why I think it's remained pretty consistent is exactly what you mentioned, which is the teams aren't oriented around product surfaces. We don't have a team that's like the app team or a team that's like the dashboard team or the podcasting team. We have teams that are oriented around customers and solving bit of a timeless customer problem. We'll never be done serving writers.

Sachin Monga (00:09:16):
We just started honestly having a concerted focus on serving readers. Growth is never a problem that you check the box off on. I hope that we are able to maintain this general structure. I think as Substack grows and expands, I'm sure we'll have more than three teams. This is where we're at right now, but I really like the focus on a customer and a timeless mission really rather than orienting around what might be a bit more of an ephemeral surface area or product de jour.

Lenny (00:09:46):
Awesome. Shout out to the writer team. Thanks for building all the awesome stuff that I get to use. It makes sense why you are more recently investing in the reader team because Substack has this magical advantage platforms have where your supply drives all your demand. I go out and promote my newsletter, people sign up for Substack. It makes sense why there's not initially a huge focus on the demand growth, but makes sense to get there. It sounds like your app is awesome.

Lenny (00:10:11):
One thing I wanted to touch on is you're kind of in this interesting position as a head of product at a small-ish company with a founder who's very product sense strong, and that's a classic challenge for a product leader to be in, where it's a smallish company, either a first PM or even a head of product, where the founder's very opinionated about the product. I'm curious what you've learned about how to work in that environment as a PM.

Sachin Monga (00:10:36):
That's a great question. I don't know if I have the recipe for this, but I can just maybe share a few of the things that come to mind. I think the first thing was really treating my role in the beginning more as a facilitator than a decision maker when it comes to product. I think the team was also small enough that everyone in theory could have a good sense of what everyone else was up to. A specific problem we had I think when I joined was that we were just getting to the point where we wouldn't have one weekly meeting where Chris could be in the room, Chris is the CEO of Substack and the person you're mentioning, and decide what we're doing in the next two weeks.

Sachin Monga (00:11:13):
We were just emerging from that phase. We had this problem which was all of a sudden, Chris didn't really know what all the teams were doing and the teams didn't really know what Chris had in mind for what they should do and what the vision was. We were hiring really quickly and hiring people who might not have all of the context of being in the room with him for years and being in all of the all-hands meetings. When I first joined, I felt like my main role was actually just solving that. And if nothing else, if Chris could have a really good sense of what all the teams are doing and if the teams knew where he was coming from and could start to get better at modeling him and his vision, that would be a win.

Sachin Monga (00:11:43):
For the first couple months I'd say, that was all I tried to do. I think now Chris and I have some reps under our belt and the teams have some reps under their belts too, and that trust just starts to form. We start the week, Chris and I, we sit down for an hour. We go through what do we feel like are the big problems to focus on this week, what are the things we're worried about. We sit down at the end of the week and we check in again. There's just a lot of open communication. I think that helps a lot.

Lenny (00:12:07):
Got it. It sounds like the core of this is building trust, which makes sense. The way that you've been building trust, one is just do it again and again and then Chris starts to trust, "Okay, Sachin's going to do the things that I think are probably the right things." And then you said you have this weekly meeting. Is there anything else that either tactically you find as a really important component of this relationship or any other lessons you've learned about just how to keep this relationship healthy and constructive?

Sachin Monga (00:12:34):
One thing that I think about a little bit because like any startup, there's going to be times that are really difficult, times that are really fun. Substack is certainly going through this really transformative time, but we're really evolving in a lot of ways from a tool into a network. We're in the thick of seeing this vision through in a lot of ways Chris has had in his mind for five years. We did a thing at an all-hands a little while ago where Substack went through Y Combinator I think it was maybe now six years ago and we watched the 60 second demo they pitched from 2017.

Sachin Monga (00:13:04):
What was so cool about that was we're actually doing all those things now that Chris got up on stage and talked about like, "One day in the future, Substack is going to get into podcasting, and we're going to have this network effect that helps writers grow by virtue of there being other writers in the platform." There's all these things that we kind of couldn't do until we earned our place at the table and the right to be able to do those things that we're doing now. To go back to your question, I think a thing that I really try to be mindful of right now is, how do I catch up?

Sachin Monga (00:13:35):
Chris has been thinking about this problem for five times as long as I have. If I can get a good sense of where his vision starts from and catch up those few years and help the teams do the same, that'll go a long way. Because at the same time, everyone now is coming at it from a different perspective. We've a lot more data and evidence. It's really good to have people on the team that have come from other companies and comply that perspective. It's a lot of, again, facilitation and I view that as a big part of my role.

Lenny (00:14:01):
Awesome. I'm curious, what are the biggest challenges with being in the position you're in? Are there any examples of a man that sucked? Or if you want to go in a different direction, is there a certain type of person that just isn't a good fit for this kind of role, had a product at a smallish company with a very product minded founder?

Sachin Monga (00:14:19):
Oh, let's start with the first one. I think the biggest challenge with this role/company phase, like I mentioned, we're going through this one-time transition from not really having a product function or a product process to having one, is almost by definition any time you figure out how to do a thing, you'll now reach this next phase of growth and it'll be obsolete. Something that I've repeated a bunch of the teams is I'm never too worried if we have the perfect planning process or the perfect execution cadence or the perfect communication process, whatever our process is, we're never going to have a perfect one.

Sachin Monga (00:14:52):
And even if we did, it would soon be obsolete because we did a really good job and now we've grown 2X or something and we have more people and the process needs to change. The main thing I care about is are we just getting better every week, every month, certainly every year. I think that's easier said than done. It sounds good in theory, but then when you're in the thick of it. you're constantly basically feeling like you don't know how to do the thing. Because as soon as you figure it out, it's obsolete. It's just really hard. I think that's true of basically just startups in general, high growth companies. Doing the thing well means that you're not going to know what you're doing.

Sachin Monga (00:15:24):
Maybe that leads into my answer to the second question, which is that's not really for everyone. I think there's almost like a personality type that has to be okay with being humbled all the time and feeling like you don't know what you're doing. I think you could be an amazing product manager at a company that is a bit more stable and consistent and get really good at what you're doing and someone who's going to be really good at a company that is on a bit of this trajectory, for folks who aren't watching the video, making a motion with my hand, that's not growing too fast, it's kind of a different job. The rate of change is a huge factor.

Lenny (00:16:03):
The point you made about how things are going to keep changing as you grow is such an important point that I don't feel like comes up as much as I thought would come up on this podcast. People are always asking me for advice. How do I structure my product team? How do I prioritize? How do I do planning? The main thing I've learned is no matter what you end up with, it's going to change in three to six months anyway because you'll learn more. The advice is just do the best thing you can think of right now. Don't assume this will last anyway, and that's good enough. There's never the perfect way to do it. It's always the best way you could do it at this moment, and then you learn how to evolve it.

Sachin Monga (00:16:35):
100% agree.

Lenny (00:16:37):
You worked at Facebook for I think it was seven years. I'm curious what were you able to take from that experience about how Facebook, in a massive company like that, builds product to a smaller company like Substack. What translates well and then what just doesn't?

Sachin Monga (00:16:51):
Over time, I'm finding that less translates than I thought. I don't know how much of that has to do with Facebook specifically though. I'll maybe mention one thing. Working on the core Facebook app, which was what I was working on for the bulk of my time there, Facebook may be the most extreme example of trying to solve so many different problems for so many different people in one tiny rectangle basically, that a big part of the product manager's job in a situation like that is going to be managing trade-offs. It's a super fascinating intellectual problem.

Sachin Monga (00:17:22):
I think going back to the previous point, a lot of people really thrive in that kind of environment, where if we do this thing really well, it is going to directly trade-off against doing this other thing. It's not even a sequencing thing. When you think about prioritization, sometimes you think, we will do this, and then we'll do this, and then we'll do this. In Facebook's case, sometimes it's, "Oh, if we do this, we just can't do this. It's going to be bad for this other thing. If we put a watch tab at the bottom, will that mean that people don't get a marketplace tab? What does that mean for this whole org and what the product is?" I think when it comes to something like prioritization, it's a very different ballgame.

Sachin Monga (00:17:56):
There's certainly some things that are consistent. You generally want to prioritize things that are going to be high impact, low effort. These types of product management frameworks, I think a lot of it can hold constant. But when you really get into the object level like what does your day look like, I think being a PM at a high growth... I can't generalize this, but the job at Substack right now, it looks quite different than what I recognized as my job from Facebook circa 2018. I think it's maybe even gotten more the case that the PM's job in a situation like that will be navigating these types of internal trade-offs. I think on something like prioritization, very different.

Lenny (00:18:31):
Just to double click on that a little bit, the main difference you're saying is that at a Facebook, it's not like whether we do a thing, it's just like what comes first, second, third. At a Substack, it's like we probably won't get to this for a year if we don't prioritize it now. Is that how you think about it, just like the time scale on your trade-offs?

Sachin Monga (00:18:46):
No. I think actually at Facebook, it's not necessarily whether we do a thing. It's not like we do this now or we do this later. It's doing this thing might mean we can't do this other thing at all, or it'll mean that instead of that chart being steady until we make the number go up, it might go down. By doing A, it might mean B is harder to do forever. Whereas at a startup, a lot of it is time. Time is the main variable. We can do this now and that means that we can't do this other thing until later. There's also an element of sequencing that matters I think a lot at a company like Substack that is in this formative stage of becoming an entirely new thing in a lot of ways.

Sachin Monga (00:19:21):
Substack started off like a single player tool for writers. It was like software for writers. If you describe Substack now as simply a newsletter tool, that would be reductive. It's really now much more of this ecosystem that's evolving in all sorts of interesting ways. There is a bit of an order of operations at play here where doing something right now might unlock our ability to do something later. That matters a lot in a situation like we're in at Substack.

Lenny (00:19:49):
Got it. Essentially there's a lot more one-way doors at a larger company. Here, you can make decisions more quickly partly, but also you can go back and there's not all these second order effects of decision you're making.

Sachin Monga (00:20:00):
I think that's right, or at least there are different types of second order effects.

Lenny (00:20:03):
Got it. I know at Substack writers are like the beacon and the vision of making writers successful, helping people make a living writing. I imagine writers are the North Star or helping writers be successful, but is there anything where you can share about how you prioritize things that you work on within Substack? How do you think about the North Star?

Sachin Monga (00:20:20):
Going back to your question about Chris too, I think Chris and Hamish and Jay, the founders I think really start from a place of principle in a lot of ways. Why are we even doing this thing? It's not just to help writers make money. It's not just to unlock these cool things. It starts with an opinion for how the internet should work, where people should be in control over their destiny to a much greater extent than has ever really been the case over at least the last 10, 15 years, where all of a sudden, everyone just started spending all of their time in a handful of these public squares that were powered by ads.

Sachin Monga (00:20:57):
When you think about what that means for Substack right now, that that means writers are in control over being able to deliver their best work on their terms to their audience, make money directly from their subscribers, and also that readers should be in control over their experience. When you show up to Substack.com, that experience should be something that you have a much greater degree of agency over or if you download the app than if you maybe opened up TikTok or something.

Sachin Monga (00:21:20):
I think where that leads you down from a prioritization standpoint is often starting from, okay, if we could do something in a bunch of different ways, is there a way that provides more control to the writer or more control over the experience that the reader has to them? Is there a way that provides much less control? All things equal, do the one that holds constant this principle of control. We could talk about a few other examples like this, but I think from a prioritization standpoint and from a strategic standpoint, Substack is a pretty principled company, and I think it's been really fun and interesting to get to work in an environment like this and also see how it actually can work.

Sachin Monga (00:21:57):
You are excited about recommendations, the recommendations feature, and we can talk about that in more detail. I think that's a good example where there's certainly a way to do that where writers have the max amount of control. We picked that way even if it might seem harder to pull off. And then that feedback loop of, "Oh, that actually worked," is really awesome to get to experience.

Lenny (00:22:17):
Yes, I definitely wanted to talk about this recommendation feature. I feel like it's maybe the most underappreciated radical shift in Substack and just platforms in general. I think this is going to go down as one of the most legendary impactful features of any platform or marketplace. I'm just putting this out there. It's such a huge deal and I don't think people appreciate this. Just to quickly summarize what this is, essentially you allowed writers like me to recommend other newsletters that I specifically pick. I pick 10 newsletters that I think are awesome. Once someone subscribes to my newsletter, they see these 10 as, "Hey, you should check these out. I think these are awesome."

Lenny (00:22:55):
It's very curated. There's no algorithm involved, which to your point is Substack's I think vision and mission is just avoid algorithms as much as possible. The reason I think this is crazy and amazing is at this point, 70% of my growth is coming from this one feature. There's something like 500 other newsletters recommending me. As soon as the feature launched and you look at my growth chart, it's just a hockey stick starting that day. I don't think people appreciate this enough, and I'm really excited to just chat about how this feature came to be.

Lenny (00:23:26):
Coming back to a point we talked about earlier of Chris having a very strong opinion about how to build product, something I heard through a birdie is that Chris was not excited about this feature when it was proposed and it took a bit of pushing to get it out. Maybe we start there. How did this come to be?

Sachin Monga (00:23:39):
Sure. The way it came to be was that we noticed this organic behavior emerging, which was that a lot of readers of Substacks were starting to discover Substacks, but the way that was happening was typically through the lens of that original writer. This could happen in a bunch of different ways, right? I think you've used the guest post feature to have guests write post on your newsletter. Obviously that is a really good way for your readers to go and discover some of these other writers in a way that you're curating. There's some less obvious ways that this happens too.

Sachin Monga (00:24:10):
If you have comments on, which I think you do, if I scroll down and click on the profile of someone who's commenting on your post, it'll show me the other Substack that person reads too. Again, this is a very personalized and very writer centric way of doing discovery. At the same time, we talked about the supply and demand side of the marketplace. The supply side of Substack has just grown over time consistently to the point where now there's a huge amount of amazing writers on the platform and a huge number of collective readers on the platform too that we knew that this sort of like cross-pollination, this discovery loop could be a really powerful thing.

Sachin Monga (00:24:47):
If you'd start from the first principles, you're like, "All right, how do we help readers discover more things?' The most obvious way to do this would be something like, "Here are some Substacks you might. Based on what we know about your reading habits, here's like a few that Substack is just going to recommend you." This is the thing that worked really well. At Facebook in particular, I think when I joined in 2011, it was definitely still during the era... I think Facebook maybe had just over 500 million users and was on this path to a billion and beyond.

Sachin Monga (00:25:13):
This thing that we called PYMK, which was People You May Know, this little unit that would show up in the newsfeed and it would just tell you that eight other people that you obviously know because you have million mutual friends. That kind of thing drove a very non-trivial amount of Facebook growth in the early days. Of course, lots of other products have done things like this. We could have done something like that.

Sachin Monga (00:25:32):
But then going back to that principle of like, okay, well, if we were to do that, let's say we were to insert it at the bottom of our post or in an email or something, it's clearly a thing now where the writer who owns that space is not really in control over what the experiences that they're offering their readers. The reader who signed up for Lenny is now seeing these other things that have nothing to do with Lenny. Does that break this control principle, like putting writers in charge, putting readers in charge? Okay, so then back to the drawing board, what would be the most obvious maximal way to just put writers in control? What is the simplest version of this?

Sachin Monga (00:26:05):
What if we just ask writers, who do you recommend? What if we just put that in the subscribe flow and just made it as simple as possible? I think Chris' reaction to that originally when that idea came up was that's probably just going to be really hard to pull off. There's a lot more things that have to be true. You need writers to opt in. You need to pick good people. You need to find a way to surface those recommendations to the readers in a way that's going to generate a good amount of surface area. I think it was a bit of skepticism that something like that could work, but we tried it and it took off really quickly.

Sachin Monga (00:26:39):
There was this virality at play now where when you recommend a bunch of people, those people will get an email that say, "Hey, Lenny's recommending you and here's all the readers that he's sending you." It created this goodwill viral loop, which was really interesting to see play out. I think there was a bunch of interesting lessons in there. We could stick into anything that seems interesting, but I think Chris' skepticism was not, should we do cross-pollination discovery? Clearly this is something that's working, but is this kind of thing going to work given how many steps are required for it to be true that this becomes really impactful? It turned out that it took off way faster than I think we had imagined.

Lenny (00:27:13):
Is there any stats you can share about just the impact it's having, what it's done to Substack?

Sachin Monga (00:27:17):
Yeah, sure. Recommendations specifically now have driven in the millions of new subscriptions for writers across the board, across I think like tens of thousands of unique writers that have received subscriptions from the recommendations feature. Of course, recommendations in particular are still just one component in this broader basket of network driven discovery.

Sachin Monga (00:27:39):
I think we recently shared the stat, more than one in three new subscriptions across Substack are coming from the Substack network and around one in 10 paid subscriptions now too. But these numbers are just, as you can imagine, growing up and to the right, getting stronger every day, and I think we'll have some more interesting stats to share on that soon.

Lenny (00:27:58):
Awesome. One thing I wanted to acknowledge, I think some people worry about this feature that it drives lower intent users. I find that not to be true. They're definitely lower intent, but it's not meaningfully and significantly. The fact that 70% of my user growth comes from this feature and my open rates have only come down a little bit, it says a lot about it. It's like useful really in tenfold people as much as it can be from someone that hasn't actually been planning to subscribe and just recently found out about it. It's really impressive how high intent they are all things considered.

Sachin Monga (00:28:31):
You bring up a point too that leads into some of the next things we're thinking about here, which is that right now most of the subscriptions that come from recommendations are coming from one particular flow in the product, which is when someone subscribes to someone else on Substack, they will then see a recommendation for Lenny. It's being serviced to people at a moment where not only are they just hearing about you for the first time, but they might just be hearing about the recommending writer for the first time too. They are new subscribers. They don't have this long standing trusted relationship built up yet.

Sachin Monga (00:29:04):
Of course, you have people now who've been subscribing to you for years and who trust you greatly and would probably take your recommendation very seriously, but the people that you're recommending are only getting these subscribers at the first moment that someone finds out about Lenny in many cases. A big part of the next step of this product now is thinking about recommendations less as a step of the flow and more like a really interesting social graph that is being built of goodwill and of influence. You now recommend a bunch of other writers. There's much more that could be done in the network than just show some of those writers in the subscribe flow of lennysnewsletter.com.

Sachin Monga (00:29:43):
There's a lot more we could do there. I'm curious if you have any ideas, but we've got a bunch of ideas that we're cooking up that I think will not only drive more subscriptions, but also probably higher intent ones as well, because these are going to be people that might already have been reading you for years who never right now would know who you're recommending.

Lenny (00:29:58):
No great ideas to share. I do find since it's only free subscribers, I have to do more work to upsell them to try paid. On the other hand, having a huge pool of interested people that aren't ready to convert yet is only beneficial. When I send a free post and mention, "Hey, I have a paid subscription. You can get more," it works really well.

Lenny (00:30:17):
This episode is brought to you by Vanta, helping you streamline your security compliance to accelerate growth. If your business stores any data in the cloud, then you've likely been asked or you're going to be asked about your SOC 2 compliance. SOC 2 is a way to prove your company's taking proper security measures to protect customer data and builds trust with customers and partners, especially those with serious security requirements. Also, if you want to sell to the enterprise, proving security is essential. SOC 2 can either open the door for bigger and better deals, or it can put your business on hold. If you don't have a SOC 2, there's a good chance you won't even get a seat at the table.

Lenny (00:30:56):
Beginning a SOC 2 report can be a huge burden, especially for startups. It's time consuming, tedious, and expensive. Enter Vanta. Over 3,000 fast growing companies use Vanta to automate up to 90% of the work involved with SOC 2. Vanta can get you ready for security audits in weeks instead of months, less than a third of the time that it usually takes. For a limited time, Lenny's Podcast listeners get $1,000 off Vanta. Just go to vanta.com/lenny. That's V-A-N-T-A.com/lenny to learn more and to claim your discount. Get started today.

Lenny (00:31:34):
Something else I'll mention that I've learned to do is I feel so fortunate being early on Substack and having this thing grow so much, especially from this recommendation feature that I'm actually getting pings from people regularly now of, "Hey, can you recommend my newsletter?" It's like a really good growth hack on Substack right now to try to get a lot of subscribers to recommend you. My system right now is I want to share the wealth as much as I can, so I rotate through different newsletters.

Lenny (00:31:59):
I help get them say a thousand subscribers, and then move on to the next one, assuming I like them. It's not just any random user. So I can share the wealth with a lot of different newsletters and give people a platform, because I have this platform now and that's been working really well.

Sachin Monga (00:32:12):
The Robin Hood of Substack.

Lenny (00:32:14):
Yeah, now I'm going to get all these DMs to recommend people. If I'm unable to, I'm sorry. You talked about how Chris was worried that this would not work. That's interesting. His point of there's so many steps that have to happen for this to be adopted is such a good one. In my experience, getting users to do anything is so hard. To get them to click some buttons and fill things out, that rarely works. It's cool that it really did work.

Lenny (00:32:38):
I think it was part of the early beta, and I found that it was a really thoughtful approach to how it was all rolled out where there was a small group of users and writers that tried it out, see how went, see what the impact was, see if there was any negative impact. Is there anything you could share by just the way this was rolled out that you've learned about how to do this sort of thing?

Sachin Monga (00:32:56):
I mentioned that we're going through this one-time transition of figuring out how to become a product driven company and how to ship products faster, better, et cetera. One of the principles I guess in this playbook that we're trying to write is we call it build with writers, build with readers. In some ways now that I think about it, it's almost like a sub principle of the put readers in charge, put writers in charge. How do you build product responsibly if you care deeply about that? One way to do it would be to almost as a strong default, anytime we're going to make a fundamental change to how Substack works, do it in a way where we bring writers along.

Sachin Monga (00:33:32):
This is still an optional thing. This isn't changing how Substack works for everyone, but this is we think a potentially profound enough thing that the way we did this was not just roll it out for everyone, put a little dialogue in the dashboard that says, "Hey, everyone, now go do this thing," it was like, okay, why don't we call up 10 writers who we think might be interested in this." It's not that hard to just mock up what this could look like, get some feedback. This is the kind of thing that I think a lot of product teams would do. But then maybe a lot of product teams would be like, "Okay, we got good feedback. Let's just build the thing, ship the thing."

Sachin Monga (00:33:59):
Instead, we just ran a little pilot. You and a few other writers were gracious enough to lend your time and talk us through how you would see this working and what you would want. We actually have now we've set up something called the Product Lab, which I'm really excited about. I think you're a part of it. I hope we asked you.

Lenny (00:34:16):
I'm curious to see where this all goes.

Sachin Monga (00:34:19):
This is just an invite only little group of a hundred or so writers that we know are interested in being on the bleeding edge of what Substack is becoming. We're investing a lot in just tools to help writers grow. Now we've got this little lab where we can take a feature recommendations to writers and get quick feedback and ensure that we're never just rolling something out to everyone without going through this step first. It's just been super helpful to have a bit of this infrastructure in place. Often the thing that we end up shipping on day one tends to be pretty different from what we had in mind before we went through this process.

Lenny (00:34:54):
I've been through a bunch of those experiences and it always goes super well. I've been through a few features that just didn't go anywhere and then they, "Nope, we're going to move on and not try this thing." Something else that always comes to mind with Substack is it's often in the news. Substack is a very popular topic amongst reporters.

Sachin Monga (00:35:10):
Writers like to talk about writers.

Lenny (00:35:11):
That's right, especially a platform that might disrupt them someday or friends have gone on and they're maybe jealous about. I'm curious, as a product leader, how you deal with bad press, angry attention, things like that, just keeping people focused, keeping people motivated. Do you discuss stuff? How do you approach stuff that comes out of like, "Oh man," and keep people excited?

Sachin Monga (00:35:33):
The whole thing here is just parsing out the signal from the noise. There's very little chatter in the blogosphere media sphere that would actually impact our day-to-day when I think about it. It's not zero, right? Sometimes there'll be something that ends up blowing up or that people are talking about that we should really take seriously and see how that might impact our strategy. But I'd say 90% of the chatter about Substack is going to probably ultimately just be a distraction to our product team at the end of the day that should just be focused on executing on the vision.

Sachin Monga (00:36:02):
Maybe my skin got thickened from working at Facebook during a bunch of years that... Actually when I started at Facebook, generally things were quite rosy in the press, but we certainly went through a bunch of different phases and a lot of the stuff. I worked on myself that Facebook ended up getting talked about a ton in the press negatively most of the time. You just learn to just keep your heads down and keep shipping. Ultimately, that's all that matters. I feel proud of the way that I think our culture is internally being formed right now. We tend to not get distracted.

Lenny (00:36:37):
It seems to be the case. I'm curious where you see Substack going as a product long-term. What are you excited about? Where are things heading?

Sachin Monga (00:36:45):
Maybe I'll answer that in two parts, one from a writer centric lens and one from a reader centric lens, which I mentioned is a bit of a newer thing for us. From a writer centric lens, I really think that we're just starting into this golden era of what it might mean to be a writer on the internet. Like I mentioned before, the economic model for supporting great writing on the internet has been generally pretty terrible for the entirety of the internet's history.

Sachin Monga (00:37:13):
In the early days of Substack, there's a couple of these glimmers of hope where you'd have people like Matt Taibbi or Bill Bishop, some of the early writers on Substack that were really well established writers who were clearly just being undervalued and now could come to Substack and see their true value. That was awesome. That was really cool to see. But in the last year or so, even in the last few months, I think there's been so many really interesting success stories now from writers who might not even consider themselves writers, let alone well established writers like Matt Taibbi or someone like that.

Sachin Monga (00:37:46):
People who are able to make a living, maybe even make a fortune just doing great work and not needing to have millions and millions of viewers or play the attention games of other networks, but just do really high quality work and have a relatively small number of people value it highly enough to pay for it. That's like a new thing. When I see the next one to two years play out for the writer side of the equation, a lot of what we're going to try to do is just make it much simpler to get started, to have your Substack.

Sachin Monga (00:38:15):
If you have an audience anywhere, Substack's never going to be the place where have the biggest audience probably, but it certainly should be the place where your most valuable audience comes home to, where they get your best work. We're seeing a lot of really interesting success stories now of people that might have a big Instagram following or YouTube following and certainly Twitter following were able to use Substack now as this home base, this place to try to accumulate their most valuable audience that they own in the sense that they get their email address, they can export them at any time, and just build really simple tools to just help them deliver their best work.

Sachin Monga (00:38:47):
It could be writing, could be a podcast, could be video. We're investing a lot in some really interesting community features as well. You're a great example of this. To call Lenny's Newsletter simply a newsletter would be hilariously wrong at this point, right? I think you mentioned to me you had 30 meetups around the world last month or something like that.

Lenny (00:39:03):
That's right.

Sachin Monga (00:39:04):
It's an impressive of run rate of meetups. I think seeing that unfold and seeing how the platform can support that type of community behavior as well is a big thing that I'm excited about. Just more. On the reader's side, I think maybe to segue into that, I think we're again entering this little potential golden age of the internet for how you experience it as a consumer. Where instead of just having a handful of feeds that are basically the same, that you could just scroll through and consume videos of random people doing random things. Not to say that's bad and that should go away.

Sachin Monga (00:39:37):
I do my fair share of just scrolling through my phone and watching random videos too, but it'd be kind of nice to have another place you could go to as well where the best culture is being made and you have an extreme degree of control over what you see and who you choose to lead into that space. You might not spend two hours a day in there, and that's fine, but it might be the first place you go because it's where all the best stuff is and it's where your best communities are going to live too. We kind of see Substack evolving not as some new type of social media, but true alternative to how you might spend that most valuable slice of your time.

Sachin Monga (00:40:13):
We just launched an iPhone app, I guess now it's been six months ago, and it's going really well. We're going to launch an Android app very shortly. We're pushing really hard on this reader experience as well. I think it'll be radically different and much better one or two years from now too.

Lenny (00:40:28):
It's been interesting to see a growing percentage of the great content that I come across be on Substack, and so I think that's a cool trend for y'all. For writers that are thinking about starting a newsletter, thinking about joining Substack, what sorts of advice, tips, guidance do you have for folks that are thinking about getting into the Substack world?

Sachin Monga (00:40:50):
My first piece of advice would be to just start it and see what happens. Start it. Have a way to start gathering subscribers. Put a link to it somewhere. Write one or two things. If you're not much of a writer, try posting a video, recording some audio, turn into a little podcast. Just start basically and see what happens and see what kind of interest there might be out there for what you have to say, especially if you already have a following on other platforms as well.

Sachin Monga (00:41:17):
I think that there's a real risk that if your entire following is locked into one platform where you don't have a ton of control over, your ability to reach those people deterministically and certainly to monetize that in some way, it seems like it's a tenuous place to be in the current age of the internet. I'd say just start. It should be really easy. Go to Substack.com, press the start your Substack button, and see what happens.

Lenny (00:41:41):
That advice may sound to people like, "Oh yeah, that's not actual advice." But I will say that is exactly what I did and that's exactly how I got to what I do now. I had zero intention of ever doing this. Charging for writing that I'm writing, that's crazy. Just the fact that Substack existed and let me try stuff out for free. You sign up. You start it. My newsletter, it's called Lenny's Newsletter because that was like the default recommendation when I signed up, because I told them my name's Lenny and it's like Lenny's Newsletter, because I had no plan to do this. It was just like, let me just sign up and try blogging here for a little bit and that little path.

Lenny (00:42:21):
I think about Chris and Hamish and the founders mapping out a user journey of a vision of how somebody onboards to Substack, to go from never writing to doing it full-time. I feel like I went through that exactly, if they even had that, where I sign up just to try it out. I start writing consistently. It starts going well, then I think about charging, and then I launch the paid plan, and then that goes well. It keeps growing, and then I do it full-time. That's exactly what I went down and there's no world where I would've done this if not for those magical combination of features of just a really simple blog a d newsletter and collecting emails and maybe monetizing down the road.

Sachin Monga (00:43:01):
Yeah, that's amazing to hear.

Lenny (00:43:03):
I think that just start advice is really spot on. Just try it out, see if it's something you want to do. I will say, it's easy to start a newsletter, it's hard to continue a newsletter. The continuing is the most important part, as Seinfeld would say in that clip, who rings the bell.

Sachin Monga (00:43:17):
I will say though to that point too that I'm really excited for what Substack can do in the product to make that easier in a way that doesn't cheapen the experience. There's a bunch of things we could do to. We could automatically post stuff to your readers. We could do a lot of things. Going back to the how do we do discovery, there's a bunch of things that would probably just work, but they would eventually kill what Substack is or have all these nasty second order effects and ruin this promise of putting writers in charge, putting readers in charge.

Sachin Monga (00:43:45):
I'm really excited and I actually view your Substack as a vanguard, as a very leading edge example of this, of you have turned your Substack into not just this thriving community of readers, but also of contributors and creators. You've got these amazing people coming and doing guest posts. You've got the podcast going. You've got these meetups. You've I think in a lot of ways alleviated the burden of how hard it would be to just be writing a long form thing every day and doing that for the rest of your life. That would be really hard. That would make it certainly much harder to keep going.

Sachin Monga (00:44:19):
Not to say that it's easy now, I know how hard it is to do what you do. But I think Substack can do more to turn this ecosystem to funnel this energy into ways for people like you to feel more like a leader of a space and a curator in a lot of ways and still deliver this really valuable service to your audience without having to do all the work yourself. I think we can do a lot more to support that kind of thing.

Lenny (00:44:45):
Is there anything you could share about what sorts of things you're thinking there and what might be possible?

Sachin Monga (00:44:49):
Let's see. Guest posts are working really well, and I'll say that we have a bunch of ideas for how to make guest posts a much bigger thing. Right now, the way guest posts work, kind of like an op-ed or something, like you invite someone to come and just write a post on your Substack. I think there's much more we can do without getting into some of the specifics and scooping the product team that we're working on that I think could make it feel more like you've got a bunch of people who are somewhat more fluidly able to contribute to your Substack and deliver value to your audience.

Sachin Monga (00:45:18):
I've teased this community stuff that we're working on a little bit, but we're piloting a feature right now that's been working really well where writers can get a little bit of like a... We view it as the pub at the back of your Substack where people can hang out and chat and the writer is still in control and sets the tone and sets the rules and norms for the space, but can create space for their subscribers to participate and hang out themselves too. Those are two areas that we're investing in a fair bit right now.

Lenny (00:45:45):
Something that I imagine somebody suggested that I'd suggest you all look into a little bit is open AI assisted writing. I was playing with this product that is called Jasper and there's also Copy.ai. I put in the title of the post I was about to write and it just generated a pretty good paragraph summary of what it could have been. They have this whole feature where you just start typing and it autocompletes things smartly.

Sachin Monga (00:46:11):
That's crazy.

Lenny (00:46:11):
That would be cool. I don't know if you want to go there, but it's pretty good.

Sachin Monga (00:46:15):
That seems like an interesting can of worms.

Lenny (00:46:17):
Right, an interesting can of worms.

Sachin Monga (00:46:18):
We did talk about whether we should change our default publication. You know how your default name was just like Lenny's Newsletter and we probably gave you a little red square or something as your default publication logo originally. A DALL-E generated publication logo service would be pretty cool.

Lenny (00:46:33):
That would be cool. If nothing else, it's just for ideas, but I would love that. Coming back to the idea of someone starting a Substack, we talked about advice, which is the core advice is just start and see how you like it. A big part of this is like, do you want to keep doing this? Because again, it's easy to start, hard to keep going, and also you may realize, "I've created this job for myself I don't like." That's something they should be thoughtful about. But on the flip side, do you see any common mistakes people make when they're starting on Substack that you suggest they try to avoid?

Sachin Monga (00:47:02):
One thing that's interesting here that I think we have a big opportunity to improve in the product is that there's going to be obviously varying levels of intent that people have when they hit that start your Substack button. Some people might come in being like, "This is going to be my full-time job. I want to make this work. I want to not just be a full-time writer, I want to build a media empire on Substack." There's certainly examples of that happening now. You can imagine a version of our onboarding and set up flow that's like the media empire version of it.

Sachin Monga (00:47:28):
You could also imagine the version that's just, "Let me just write one thing. Don't make me make all these decisions. I just want to get in the game." I think that in general, a mistake that people might make is... I'll maybe flip it back to an anecdote related to what I heard from Chris when I was chatting with him the other day, that he had to convince you pretty hard to turn on payments at all. Correct me if I'm spreading misinformation, but is that right?

Lenny (00:47:51):
Yeah. And Hamish too. Especially on how often I can take a break, he's always given me advice of, "You can take a break more often than you think," because I feel like I can never not do a week. Both those pieces of advice. It took me a while to get over, maybe I could charge for this and then maybe I could take some weeks off.

Sachin Monga (00:48:10):
Right, right. I think there's a generalizable piece of advice here that might be my answer to the question of what's a common pitfall, which is people are really worried about how their audience will perceive them and really ultimately their own worth, right? Should I send a newsletter three times a week into people's inbox? Is that too much? Should I ask anyone to pay me ever? Is that crazy? Am I allowed to take a vacation ever given that I've got people paying on an ongoing basis? And is that a bad service to provide if I'm taking a two week summer vacation?

Sachin Monga (00:48:42):
I think almost in all of those cases, and then you could imagine five more things like that, readers, especially the people that are subscribed to you who are paying you, are pretty forgiving and are really there to support you and want you to take that vacation. There's probably more people who would want to pay for you that just don't even know about you that would totally pay if they could. Go back to that spectrum of, am I just trying to write a blog post? Am I trying to start a media empire? It's kind of like many people won't know yet. Just open up optionality for yourself and see what happens. Maybe don't be too worried about what your audience might think.

Sachin Monga (00:49:20):
I think that maybe is one difference between Substack than something like Twitter or Instagram or something. Subscribe as an action is pretty heavyweight. It's like a costly signal, right? It's not as easy as just matching the follow button on a bunch of accounts on Twitter or something like that. If someone is subscribed to you, they're granting you write access to their brain is maybe the way I view it in a nerdy sense. What that means is not just like, "I'll let you write your one long form thing once a week," but, "hey, you've got this other person that you think might have something interesting to say? Cool, let me know. I'm here for it." I think writers underestimate that.

Lenny (00:49:57):
Maybe three things I'll add to this just for folks that are thinking about, should I try this out? Should I not? One, when I joined Substack, I already felt like it was too late, and this was three years ago. I was like, "Nah, it's too late. Everyone's already got their big newsletters. There's no way I'm going to make any dent." I think people feel that now, and I think it's also not true. I think there's so much opportunity.

Sachin Monga (00:50:18):
100%.

Lenny (00:50:19):
Two, when I got to a thousand paid subscribers, which feels very doable, I was making around a 100K, which is exactly... I think it was Kevin Kelly's 1000 True Fans. It was exactly like, "Oh wow! I could make a living with a thousand true fans for real." It's shocking how much you could make with so few people that really care about what you're doing. Think about is there a niche or something you're excited about that you can find a thousand people to pay you 10 bucks a month.

Sachin Monga (00:50:52):
What's cool about that I think now with Substack and with the network effect is if there's a thousand people who are going to pay you 10 bucks a month, there's probably 2,000 and 5,000 and 10,000.

Lenny (00:50:58):
That's exactly what happened to me. I'm like, "If I hit a 100K, holy moly, I am good," and then it just kept growing. That's exactly right. You think there's an out, but the markets for these things are huge. The last point maybe is it took me nine months of doing it every week for free to get to a point where I felt like I can keep doing this. I enjoy doing this. People continue to value it, where I decided to turn on paid. It's a very slow and steady thing initially.

Lenny (00:51:24):
Don't expect it to just blow up. Just do it every week. See how it goes. See if you like it. See people like it. And if they do, keep going. If not, you can stop. When I launched my newsletter, I tweeted. I'm just going to experiment this thing. No idea where it's going to go. Just try it out, so you don't have to set the stakes high when you're starting out.

Sachin Monga (00:51:41):
I think that's exactly right. You mentioned Kevin Kelly's 1000 True Fans, which has become this canonical piece of writing on the internet now. My favorite Kevin Kelly blog post, that's my second favorite, my first favorite is a post that he wrote called You Are Not Late, which is exactly what you... You can probably picture what he says, but it's such a compelling, persuasive argument for the thing you mentioned, which is like... Obviously he wasn't talking about Substack in his post, but he was talking about the internet and how in the grand scheme of things, how lucky we are to...

Sachin Monga (00:52:13):
I don't even know when he wrote it, maybe it was probably 10 years ago at this point, but certainly at a time where a lot of people were feeling, "Oh, Facebook and Google and the internet's done. The battles have been won. I wish I was coming of age. I wish I had graduated from Harvard in 2004 or something." It's just so wrong. We are so early when it comes to how the internet will play out that I think getting to work on that in any capacity right now, getting to shape how the internet is going to play out over the next 10, 20 years is so fun because we are not late.

Lenny (00:52:40):
Here, here. I know Marc Andreessen mentioned those too when he moved to Silicon Valley in the '80s, "It's all over. It's too late. I missed the gold rush of tech," and it was just the beginning. Well, we've reached our very exciting lightning round where I'm just going to ask you a bunch of questions real quick, share whatever comes up. Sound good?

Sachin Monga (00:52:59):
Sure, let's do it.

Lenny (00:53:00):
What are two or three books that you recommend most to other people?

Sachin Monga (00:53:04):
I will plug some books that have nothing to do with the internet or software or tech, but have been the most informative or instructive books for me I think in my career as a product person working on software, which are books about architecture and urban planning. The reason why I find this field so fascinating is because for thousands of years, people have been figuring out how to build spaces that help people interact with each other and build good spaces to occupy. We've only been doing this for, going back to the Kevin Kelly thing, for basically the blink of an eye on the internet and in the digital realm.

Sachin Monga (00:53:35):
There's one book in particular by an architect named Christopher Alexander who sadly just passed away earlier this year. He wrote this book in the '70s. It's called The Timeless Way of Building. This is the book that I recommend to the most people I have. I buy it in bulk and I just give it away to people. The basic premise of the book is that in the '70s, we had just gone through a couple of decades of just mass produced cookie cutter suburban house development in the US. His premise was like we've basically just lost the plot on this. No one likes living in these houses.

Sachin Monga (00:54:06):
If you think about why these houses all feel bad to live in, it's because the people building the houses now for the first time ever are different than the people living in the house. It's these developers, these real estate developers, these big companies, mass producing these houses. But for thousands of years, we've figured out what makes a good house. The people building the house are the people living in it and they get that, but now the incentive structure got changed and they messed everything up.

Sachin Monga (00:54:27):
I think there's a really interesting parallel there with the internet, specifically how the last decade or so has played out, where the people building the spaces that we occupy are operating under a very complicated incentive structure and it's leading to these suboptimal user experiences. This is what we work on at Substack. This is what I think is fun to work on right now. If you're working on something like this, I would highly recommend The Timeless Way of Building by Christopher Alexander.

Lenny (00:54:51):
Awesome. We're going to include that in the show notes for sure. What are two or three Substacks that you recommend most speaking of recommendation features?

Sachin Monga (00:54:59):
I was just thinking about this as I don't write on stack certainly frequently, and so I don't use the recommendations feature, but who would I recommend if I did besides Lenny, of course? I'll share a couple of random examples maybe, again, outside of maybe the tech product world. There's this guy named Darryl Cooper who has a podcast on Substack called The Martyr Made Podcast that I've gone super deep into lately. It's hard to describe. He basically takes a topic and he will produce the single best explanation of that topic you will ever find, because you'll spend an insane amount, probably 10,000 hours per topic, figuring out getting to the bottom of this story.

Sachin Monga (00:55:38):
He's doing a series right now in the labor movement in America. It sounds like a boring topic maybe, but he's just such an amazing storyteller. He's I think a good example too of this could only really work if he finds his thousand true fans as people who are just like, "Yeah, I'll just pay for this." It would be a very bad advertising business for sure. He publishes pretty infrequently, inconsistently, but it's just the highest quality stuff. That's The Martyr Made Podcast. Since I know this is supposed to be a lightning round and I spent too much time on that, the two others that I'll just quickly throw out there, Colin Meloy is one of my favorite musicians.

Sachin Monga (00:56:10):
He's the lead singer of The Decemberists. He's doing a really cool thing on his Substack right now of just a lot of interesting behind the scenes stuff on tour, publishing, audio and video. It's been really good. If you're a fan of The Decemberists, I highly recommend. One more, let's see, I have been really excited about Ethan Strauss lately. He writes a Substack called the House of Strauss. He's a basketball writer, but I think it's a cool example of like he just has subscribers now. He can write whatever he wants. He writes about a wide range of topics and they're all just really fascinating. I love to see that kind of thing happen on Substack and in general.

Lenny (00:56:41):
That's just reminding me, Kareem Abdul-Jabbar just recommended my newsletter in his Substack.

Sachin Monga (00:56:45):
Oh man, congrats! That must be a life achievement right there.

Lenny (00:56:50):
Yeah. I'm like, what the hell?

Sachin Monga (00:56:52):
Congrats!

Lenny (00:56:53):
Thank you.

Sachin Monga (00:56:54):
He's a great writer. .

Lenny (00:56:54):
I don't know if he reads it. I don't know. I don't know what's going on. I love it. He has got a great Substack, by the way. I think if you just Google Kareem Abdul-Jabbar Substack, you'll find it. On the recommendation feature, I was just thinking, do you want to shout out the folks that built it, the team?

Sachin Monga (00:57:07):
I would love to.

Lenny (00:57:08):
Let's do it.

Sachin Monga (00:57:09):
It's too many. It ended up being a company wide effort, but the product manager on my team, Dayne Rathbone, was specifically I think the spearhead behind the way that we built it, like you mentioned, that we went into. He was a really big proponent for that. Gabriel on our design team designed it and many engineers worked on it. It'll be hard to shout them all out, but I'd shout out Dayne on my team because he ensured that we built it in the way that we ultimately needed to build it for it to work.

Lenny (00:57:36):
Thank you, Dayne and Gabriel. Two final questions. Do you have any favorite recent movies or TV shows that you watched that you love?

Sachin Monga (00:57:44):
Yeah. I just finished the latest season of For All Mankind and loved it.

Lenny (00:57:49):
So good.

Sachin Monga (00:57:50):
Did you watch it all?

Lenny (00:57:52):
Yes. Oh my God! The last couple episodes, you're sitting on the edge of your seat.

Sachin Monga (00:57:55):
I feel like in this season, every episode was like its own standalone movie or something. It started slow the whole show. I think the first season was a bit slow. When I recommend it to people, I'm like, "Just power through it," but they really found their groove. I don't know. I'm stoked for the next season.

Lenny (00:58:10):
Same. Final question, what's a favorite interview question you like to ask folks when you're interviewing them?

Sachin Monga (00:58:16):
I have a tough time answering this question because I have found that there's not one question that will get me the signal I actually want given how diverse the candidate's experiences might be in their context. If you're coming from a Facebook type place or coming from a startup, I might need to ask different questions in order to get the signal I want. Maybe I'll answer it in that way, which is like these days, especially for Substack, what is the signal that I'm trying to get?

Sachin Monga (00:58:43):
I think really for early stage, fast growing startup, we talked so much about how different that is, we just need people who can run through walls to accomplish big goals. Maybe grit and endurance in some ways and drive are the words I would throw out there. I find it's really hard to have one question that will get that signal. We need to tailor it to that person's background.

Lenny (00:59:07):
All right, I'll accept that meta answer. Sachin, thank you so much for being here. As you I've shared, Substack is very near and dear to my heart, and I'm really thankful that you spent the time to dig into a lot of these things that have been on my mind. I imagine it will be helpful to a lot of other people. Two final questions. Where can folks find you online if they want to reach out, learn more? Are y'all hiring? And then how can listeners be useful to you?

Sachin Monga (00:59:31):
First of all, thank you, Lenny, for being such an amazing Substack example setter. We talk about you all the time, as you can imagine internally, and you've been so helpful to the company and to our product team. It's been a real honor to get to come onto the pod and keep doing what you're doing. You can find me on all the various social media platforms. I'm not super active on them, I must admit, but maybe Twitter would be the one where I spend the most time, which is just Sachin Monga, my first name and last name, is my handle.

Sachin Monga (00:59:58):
I'll make one plug for a role that we're hiring for right at Substack, which is a senior data role with a product and growth analytics bent would be the specific archetype we're looking for in this role. If you are listening to the pod and feel like that might be you, I would love to chat. I think my email address too, I don't know if it would get shared, but it's just Sachin, my first name, @substackinc.com. Feel free to send me a note anytime.

Lenny (01:00:24):
Awesome. We'll include that in the show notes. Sounds like y'all are building some cool analytics features maybe based on that role. I'm excited for that. Awesome, man. Thank you for being here.

Sachin Monga (01:00:33):
My pleasure. Thank you so much for having me.

Lenny (01:00:37):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

