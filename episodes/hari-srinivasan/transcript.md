---
guest: Hari Srinivasan
title: LinkedIn’s product evolution and the art of building complex systems | Hari
  Srinivasan (LinkedIn)
youtube_url: https://www.youtube.com/watch?v=ZUwkTs_QWqg
video_id: ZUwkTs_QWqg
description: 'Hari Srinivasan is VP of Product at LinkedIn Talent Solutions, where
  he oversees LinkedIn Recruiter, LinkedIn Jobs, and LinkedIn Learning. He’s also
  a frequent guest lecturer at Stanford...

  '
duration_seconds: 3888.0
duration: '1:04:48'
view_count: 7237
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- activation
- metrics
- user research
- experimentation
- analytics
- subscription
- hiring
- culture
- leadership
- management
- strategy
- vision
---

# LinkedIn’s product evolution and the art of building complex systems | Hari Srinivasan (LinkedIn)

## Transcript

Hari Srinivasan (00:00:00):
It was March 2020 and we were just watching COVID hit. It was just this heartbreaking moment where in the feed you were seeing all these people, by no fault of their own, starting to post that they've lost their job. We started seeing in our data is you had some areas like maybe hospitality was really getting hit, but some areas like customer service that just couldn't hire enough. You'd think the marketplace would balance pretty quickly. You'd think, okay, maybe these people will start moving to other jobs, but it wasn't happening.

(00:00:24):
A large reason behind this, people are used to looking for certain particular titles, and they didn't start realizing other people could do this job. We made a pretty big push in something we call skills-first hiring. This was the idea that we could translate people's experiences into a set of skills, and by that we could help them really start balancing the marketplace with a much different system. I think that the job market is rebalancing, but it's being done, the pathways are being done in a very different way that seems to be maybe a change that holds through these ups and downs. That'll be very interesting to see.

Lenny (00:00:57):
Welcome to Lenny's Podcast, where I interview world-class product leaders and growth experts, to learn from their hard-won experiences building and growing today's most successful products. Today, my guest is Hari Srinivasan. This episode has a hilarious story.

(00:01:11):
On Twitter, an account called The Curious PM tagged me with a request to have someone from LinkedIn come on the podcast and talk about how they operate and what they've learned about building products that serve so many different types of customers. I replied asking for any suggestions for who he thought I should specifically talk to, and he suggested Hari Srinivasan, by doing some research on LinkedIn. I reached out to Hari, told him about this tweet and he agreed. Here's the episode.

(00:01:39):
Hari's been at LinkedIn for eight-and-a-half years and he leads the Talent Solutions Product Team as VP of product, which is also LinkedIn's biggest business, and includes all of the hiring and learning products, which you'll hear about in this episode. In our chat, Hari shares what he's seeing change in the hiring market, what you can do to improve your odds of finding a job through LinkedIn, what he's learned about building and maintaining really complex systems like LinkedIn, tips for getting into product management, and some lessons from his own course on product management. Plus, we also talk about how LinkedIn has been able to become a real source of valuable content and a lot less cringe over the past couple years, which I've definitely noticed and I share in our chat.

(00:02:20):
What a fun series of events that led to this episode. Big thank you to Jatin, hopefully, I'm pronouncing your name correctly, the guy behind the Curious PM account, for making this all happen. With that, I bring you Hari Srinivasan after a short word from our sponsors.

(00:02:35):
Today's episode is brought to you by Miro, an online collaborative whiteboard that's designed specifically for teams like yours. The best way to see what Miro is all about and how it can help your team collaborate better is not to listen to me talk about it, but to go check it out for yourself. Go to miro.com/lenny. With the help of the Miro team, I created a super cool Miro board with two of my own favorite templates, my one-pager template and my managing-up template, that you can plug and play and start using immediately with your team.

(00:03:05):
I've also embedded a handful of my favorite templates that other people have published in the Miroverse. When you get to the board, you can also leave suggestions for the podcast, answer a question that I have for you, and generally just play around to get a sense of how it all works. Miro is a killer tool for brainstorming with your team, laying out your strategy, sharing user research findings, capturing ideas, giving feedback on wire frames, and generally just collaborating with your colleagues. I actually used Miro to collaborate with the Miro team on creating my own board, and it was super fun and super easy. Go check it out at miro.com/lenny. That's miro.com/lenny.

(00:03:45):
Today's episode is brought to you by Brave Search and their newest product, the Brave Search API, an independent global search index you can use to power your search or AI apps. If your work involves AI, then you know how important new data is to train your LLMs and to power your AI applications. You might be building an incredible AI product, but if you are using the same datasets as your competitors to train your models, you don't have much of an advantage.

(00:04:11):
Brave Search is the fastest-growing search engine since Bing, and it's 100% independent from the big tech companies. Its index features billions of pages of high-quality data from real humans, and it's constantly updated thanks to being the default search engine in the Brave Browser. If you're building products with search capabilities, you're probably experiencing soaring API costs or lack of viable global alternatives to Bing or Google. It's only going to become harder to afford these challenges.

(00:04:38):
The Brave Search API gives you access to its novel web-scale data with competitive features, intuitive structuring, and affordable costs. AI devs will particularly benefit from data containing thorough coverage of recent events. Lenny's Podcast listeners can get started testing the API for free at brave.com/lenny. That's brave.com/lenny.

(00:05:04):
How are you? Welcome to the podcast.

Hari Srinivasan (00:05:06):
Thanks for having me. Been a big fan for a long time.

Lenny (00:05:09):
I really appreciate that. What a fun story behind this conversation. Let me just ask you, how did you feel when I cold-DMed on LinkedIn, asking you to be on this podcast because of a random tweet?

Hari Srinivasan (00:05:20):
I felt very honored. Again, I really have followed your work for a while. It's been really amazing to see what you've built, and I'm a huge fan of different builders. Also, it was a little bit of an honor that someone ... I know we're going to get into the story in a little bit. When you work on something, oftentimes jobs and learning, it's rare I think that it's in the influencer conversation. It's not necessarily something you or other people are properly experiencing on day-to-day. Sometimes, I don't know if we get to tell some of these stories, and I really appreciate you reaching out for that.

Lenny (00:05:50):
Yeah. Absolutely. I guess let me just give a big thank you to Jatin Rajvanshi, also known as The Curious PM, who tweeted about this concept and then is like, "Hey, talk to Hari about LinkedIn." Thank you, Jatin, for making this happen. It was all thanks to you. Usually, when this happens, someone tweets a recommendation of someone, they know each other. I'm like, "Eh, I don't know. This is some promotion of some other person." But you guys don't know each other, right?

Hari Srinivasan (00:06:15):
We don't, no. I'm looking forward to meeting you. Thank you, again, for putting in the word.

Lenny (00:06:20):
Absolutely. Also, thank you to Jatin for recommending a bunch of questions that I'm going to ask you.

Hari Srinivasan (00:06:26):
That I didn't know. Maybe I should've known. That I didn't know. Thanks, again, Jatin. It's very kind of you.

Lenny (00:06:32):
Yeah. Okay. Let's roll into some stuff. I actually want to start with LinkedIn as a platform broadly. I know you don't work on all parts of LinkedIn and don't necessarily know everything that's going on there, but something I've noticed that's pretty major is, it feels like LinkedIn's really made this move from being a very cringey place to post and spend time to, it's actually now interesting.

(00:06:55):
The feed that I see on LinkedIn is interesting. Oftentimes even more interesting than Twitter, which is crazy to say. Also, it's become the biggest source of traffic for my newsletter, more so than Twitter, which I never expected. My question is, as far as you know, what is it that y'all did right in the past couple years that has allowed for this shift to happen? Because this is very rare.

Hari Srinivasan (00:07:18):
Well, first, I'm glad you're having a good experience with it. That's really, really kind to here. First of all, it's very interesting you hit on it. Everything at LinkedIn is a very connected ecosystem. One of the things that we always think about is how the whole system fits together. I'm sure we'll get into it more and more about how we build at LinkedIn, but how you make decisions based on the very complicated ecosystem is actually not very difficult because we're all here to help people connect to economic opportunity. Every time there's a discussion, something I'm really, really proud about working here is, everyone knows how that decision is going to be made. It's all about how we're connecting people to economic opportunity.

(00:07:55):
Now, it's funny. Just the other day, I was driving. I was in an Uber with the person who runs a feed. He's this guy, Kamesh, who's just phenomenal. We were just talking about this and one of the things he mentioned to me was, "If you think about what a feed is when it connects someone to opportunity, it's got to do a couple of things really, really well." We've done a ton of member surveys on this, a ton of thought behind it. The first is, as you make relationship connections across the way, that is a real way by which people get opportunity. They keep in touch with those people. They learn they might follow someone, and hopes in getting knowing them and getting that knowledge. We got to make sure that that content is getting to them.

(00:08:29):
Then, when you think outside the network, we have to make sure that the things that people really want, which they keep saying are knowledge and advice and ability to get the real perspectives they need to get there, those are the things out of network they want. We've really, really been focused on driving those two systems. How does someone connect to opportunity both through the people and through the content that they actually want? As you know, when you do a feed, there's so many decisions that go into that complex system, so many decisions. But we've been really, really trying to make sure that we don't lose sight of that and start tuning all those knobs into that direction.

Lenny (00:09:04):
If we're trying to get even more specific with what has changed, clearly there's been a focus internally. Is that true? There's just like, "Hey, let's make this feed a lot more interesting"? Or is this just a never ending and then it's actually started to work investment as far as?

Hari Srinivasan (00:09:19):
Well, there's always been a focus on connecting people to opportunity. There's always been a focus on that. I think what's happened over time is we've gotten more and more clear with what our members really want, which is this ability to feel close to those relationships and the ability to really get that knowledge that they need. As we've gotten better and clear in that understanding and we've been able to dial the knobs in the right way, I hope it's landing in the right place. I don't think it's any place near declaring victory in any part of this product.

(00:09:46):
I think one of the beauty of working with that vision of connecting people to opportunity, there is always some piece of friction. There is always something we could be doing better. I'm always hesitant to say we've ever hit that bar, and I know there's probably people who listen to you who probably maybe have not had that experience. I always encourage you to reach out and let us know ways we can do better. But I'm glad you're having an experience with it. And then to your point, I always feel that as long as we stay focused on that and each of our decisions start moving in that direction, hopefully the product will continue to deliver.

Lenny (00:10:14):
Do you know if there's any product changes that have most contributed to that feed becoming much more interesting?

Hari Srinivasan (00:10:21):
Well, there's a couple of things that I think are very special that we're working on and it's hard to say which is most, because a lot of these things obviously accumulate and compound over time. But certainly, there's a lot of machine learning and algorithms that go behind these systems. Many of them, as we start understanding that these are things that people get value by, it's about how do we make sure that we're giving people that interesting knowledge? As we've gotten crisper on what that means, I think we've been better able to build towards it.

(00:10:50):
The other one, which is new, but I'm just particularly excited about, we're starting to do a lot of things which are gen AI-assisted. You basically can come in and get some prompts and people can bury their perspective on that. I think that combination, it's very early, but it's very exciting on how we might be able to help people unlock knowledge. There's almost a billion people now on the platform, knowledge of those billion people in a way that people can find and see.

Lenny (00:11:12):
Awesome. Again, I know this isn't the area you spend all your time on, but maybe one more question along these lines.

Hari Srinivasan (00:11:18):
Yeah, please.

Lenny (00:11:19):
Yeah. Do you have any sense of the kind of content that works best on LinkedIn in terms of the algorithm you talk about? The algorithm is probably one of the bigger impact things that have changed.

Hari Srinivasan (00:11:29):
If there's anything with knowledge or advice, I think that's what a lot of people are looking for. Every time we run these surveys, every time we talk to people on what they want, those are the things that really when you connect opportunity that people seek after in our system. You're a great example of that. You're able to give knowledge and advice in an area with a lot of depth. I think that maybe that's why you're having some of the success you're seeing on the platform, which is wonderful to see.

Lenny (00:11:53):
I think I'm actually not getting as much success as I could because I don't put in the time. I usually just post a simple thing with a link and I think I could be, if I really ... I just don't have time to do this of just like, post a lot more stuff within the actual post. I think that would do better.

Hari Srinivasan (00:12:09):
That actually makes me happy. My guess is what you want to be doing is learning and creating and not spending a lot of time managing. Maybe that's actually a good thing. It's actually another wonderful thing to hear.

Lenny (00:12:20):
Yeah, absolutely. Okay. Let's move to your sweet spot, which is the talent solution product? Is that what it's called?

Hari Srinivasan (00:12:29):
Yeah. It's basically any product on LinkedIn that helps you get a job or learn a skill. We have products for recruiters and hires, jobs. We have products for job seekers. We have LinkedIn Learning and then certainly, we run a pretty large creator ecosystem for instructors who post content into LinkedIn Learning.

Lenny (00:12:47):
Is it true that this is the biggest business within LinkedIn?

Hari Srinivasan (00:12:50):
It is a very big business between LinkedIn. It's certainly hopefully something that, again, if you go back to that vision of connecting people to opportunity, it's certainly something that I like to think is very, very core to that, how people get jobs and learn skills.

Lenny (00:13:04):
The feed gets all the glory and you guys are making all the money?

Hari Srinivasan (00:13:07):
I would not say that, but again, we joke about those things. It's so hard at LinkedIn to separate one product from the other. It's really the way we run. It's the way we think about the product. It's really the way we build. Let me just give you a super concrete example of that. Certainly, if you have someone coming in and looking at the feed, one thing we might do is suggest a job recommendation based on what they're looking for in that feed. Part of what we have to do is think about how someone who's looking at something in their interest might be driving their job-seeking experience as well.

(00:13:38):
And then when they're looking for a job, it's very important that they know how they can actually get connected in that job. The relationship, the network you build are very much part of that flywheel that go into it. And then even as we start looking at this, you might be looking at a subject and then you want to go deeper on, and there's a course that comes into it as well. All of this to me is a very, very connected ecosystem on how those items work together in order to give people opportunity. We might think of it from the outset as very different things, but inside, even the way we operate and the way we think about it, it's a very, very connected ecosystem.

Lenny (00:14:15):
What are the components again of this part of the org?

Hari Srinivasan (00:14:18):
We think about it as two different marketplaces. There's a hiring marketplace, which is, how do we connect job seekers and recruiters and hiring managers? And then there's a learning marketplace, which is, how do you connect learners to instructors?

Lenny (00:14:29):
Got it. And then within hiring, are there subcomponents?

Hari Srinivasan (00:14:33):
Yeah. Again, we really think about it as a marketplace. We're generally organized around seekers and hires. There's a team that's working on a Recruiter, which is probably one of the more flagship products that LinkedIn has always been around, a team working on jobs, which is, if you ever post a job on LinkedIn, and then a team working to always help job seekers make sure they connect. And then on the other side for learners, instructors, the team working on LinkedIn Learning, which is one of the bigger enterprise learning products in the world. And then a team working to help instructors.

(00:15:02):
Many people don't know this. We actually have two large film studios. We bring in instructors. We film a lot of content. One's in Europe and one's in Santa Barbara. It was all started with the Lynda acquisition. We have a large team of content creators and teams, everyone from makeup artists to script writers, that we get to use over there.

Lenny (00:15:22):
Wow. It's just marketplaces all the way down as you talk about this. Hiring marketplace, learning marketplace, the feed itself. Probably more I'm not thinking about.

Hari Srinivasan (00:15:31):
Yeah. It's very much the one model that we sometimes use internally as well is, how do we operate as marketplaces inside an ecosystem? I think it speaks to the complexity again of the product and hopefully somehow of how we might operate it.

Lenny (00:15:46):
I think with your vantage point at being at the center of hiring, a lot is changing within the hiring marketplace in the past, I don't know, year at this point, where it used to be very candidate-oriented, where they had all the power and they salaries were crazy. Everyone's bidding and trying to get people to join their company. Now, it's completely opposite. So many people looking, companies have all the power. I'm curious what you've seen, if that's roughly it, or what you're seeing basically in the hiring market these days.

Hari Srinivasan (00:16:15):
Yeah. Well, first of all, the balance that you're talking about, it is shifting in the sense that there are more seekers in the marketplace now and there are fewer open jobs in the marketplace. Of course, that changes how many applications you get for the job and how you have to look through. I think there's a model where people think it's drifting dramatically to exactly the way it was. I actually think some of the changes that occurred during the last couple of years are actually sticking around. Let me give you a couple examples of where things I think are really changing.

(00:16:44):
The first thing that happened was, and maybe in my opinion, one of the big changes to the world that no one's really talking about it to my degree is the impact of it, but there's been a real move to skills-based hiring. For the longest time, and I'll give you actually a really concrete example, it was March 2020 and we were just watching COVID hit. It was just this heartbreaking moment where in the feed you were seeing all these people, by no fault of their own, starting to post that they've lost their job.

(00:17:09):
We started seeing in our data is you had some areas like maybe hospitality was really getting hit, but some areas like customer service that just couldn't hire enough. You'd think the marketplace would balance pretty quickly. You'd think, okay, maybe these people will start moving to other jobs, but it wasn't happening. A large reason behind this, people are used to looking for certain particular titles, and they didn't start realizing other people could do this job.

(00:17:31):
We made a pretty big push in something we call skills-first hiring. This was the idea that we could translate people's experiences into a set of skills, and by that we could help them really start balancing the marketplace with a much different system. But instead of saying, "I need to have this talent," you can say, "I need someone who can do negotiation, and I need someone who can really help me understand how to deescalate a customer situation."

(00:17:54):
You find a lot of people in hospitality have about 70% of the skills you need for customer service and of course, you could train off the rest. We started seeing the skills-first hiring really start taking off. At this point, roughly 47% of our recruiters will come in, explicitly use skills when they start looking for candidates. That's a pretty big change that we're actually seeing hold. I know it's early in some of these changes, but it's a change where I think people are still continuing to start looking at skills.

(00:18:20):
Another one was this concept of, there's a lot more people who are starting to look for jobs by values. They were saying, "Look, most job sites work by you come in and you look for a job and a title, and that's how you navigate the world." We started realizing a lot of people wanted to come in and instead of look at it like that, they may say, "Look, I really want a job. This aligned with my purpose." Or even by an interest, I may want something in AI. We started launching collections in the way to filter in these things. We're still seeing some of that usage today.

(00:18:47):
I think that the job market is rebalancing, but it's being done, the pathways are being done in a very different way that seems to be maybe a change that holds through these ups and downs. That'll be very interesting to see.

Lenny (00:18:58):
What's interesting is it's not like this would change on its own. You're the biggest jobs marketplace in the world, right?

Hari Srinivasan (00:19:08):
We have a lot of professional jobs on our platform and a lot of professional seekers.

Lenny (00:19:11):
Hopefully, mysterious. I imagine it is. I don't know. I guess Indeed might be a competitor, but okay, let's say it's one of the bigger job markets. You influenced the way jobs are sought and posted and how people find jobs; so in a sense, designing. Sounds like basically, there was an internal decision. Let's focus on the skills approach. What's cool about that is that changes the way hiring happens in the world.

Hari Srinivasan (00:19:33):
It's one of the things that I think is so interesting about building products today is, it has to clearly be something people want. If we had just said we're going to go like this, and every hire was like, "I don't want to do this," or every job seeker said, "I don't care about it," I don't think anything would click. We also have to be receptive enough to amplify that signal and allow it to work through a system so that it could actually be easy to use.

(00:19:56):
I don't think we said that, "Hey, we got to go and do this value-based thing." I think we started feeling it and hearing it from members and then as we adapted, these things start amplifying as they come through. I do think that's hopefully something that I think about a lot is, let's just make sure that we keep a pulse on what people want and we make sure that we can get that through a system at a pretty fast pace. Because then, we will hopefully continue to be a place where people want to go look for jobs and make hires.

Lenny (00:20:25):
What I was thinking about as you were just chatting is this open to work feature that LinkedIn has. I remember days before that existed and people used to just like jury-rig, "Hey, I'm hiring," or, "I'm looking for a job." There's always this sense that if you're open to work, you're not as good. Because why would you be amazing and open to work and not hired? I'm curious if you were even part of this experience. Just, what was it like to come up with that approach to how to communicate that you're open to work?

Hari Srinivasan (00:20:51):
It's been through phases and I think those phases really reflect on the perception of how it's changed. In the beginning it was, you could say you're open to work, but it was a secret signal to recruiters if you will. That certainly still exists, but now we said you could more publicly say it and maybe it'd be a feed post. And then we started launching it. Actually it was around COVID when a lot of the stigmas of unemployment changed dramatically, because everyone started understanding you're in this different situation. We started putting it the frame and that's the more iconic way I think people associate with now.

(00:21:22):
It's funny. Just this week, we tried something new and I feel like it's almost the same journey. There are many customers as you can imagine, that have LinkedIn Learning and LinkedIn Learning is typically an enterprise product. It works across your employee base. We're trying to do Open to Internal Work where you can say, "I'm actually at the point where I may want the next play internally in my role," and an internal recruiter can see you. As you can imagine, I would actually even maybe argue more stigma about being concerned about upsetting your manager. Certainly, there's different cultures and companies about this.

(00:21:52):
I have a feeling in sometimes we like to think five, 10 years out, I think it's going to go on the same journey. That's one hunch I have, that there'll also be an employment-driven way internally for people to find their next play. It'll be interesting to see how it plays out, but already you can feel a little bit of that tension right when we launched it and knowing. Let's see how this goes.

Lenny (00:22:13):
You were talking about how hiring is changing. I'm curious how PM hiring specifically is changing. A lot of people listening to this podcast are product managers. Is there anything unique you're noticing there?

Hari Srinivasan (00:22:22):
Maybe a couple stats that could be very helpful. If you're having a hard time finding a PM role, let's start with this, you're probably not alone. We publish it. You can go to Economic Graph data. This is all public. We publish this. But if you look at tech, it's down about 50% year-over-year. We look at hires over total population on LinkedIn. You can go to Economic Graphs and you can see how it compares trends industry. We don't look at the functional data as much, but the PM data seems to be trending just slightly even maybe below software engineers and data as well, which is maybe a comp for this. I know not everything is perfect industry to function cuts.

(00:22:56):
It is a difficult place, but I'll give you a couple tips because I imagine that may be helpful for a couple of the listeners. It's certainly one of the larger inbounds of things I get. The first is, in those markets, you do want to make sure that the more you can do to form relationships and say that this is what you can do, which is always helpful. Now, I know that not everyone has relationships, but you can always try to develop those at different places and across LinkedIn as well. But that's one thing I would really, really start to look for.

(00:23:24):
The second thing I would really do is we have launched the way now to come in and signal obviously that you are interested in a role. We have those open to work capabilities, but then each job has a set of skills that they're looking for under it, like we talked about in skills-first hiring. Against each skill, you can actually add different kinds of credentials. I would really encourage people to add work products if that's something that they're actually building. You can add different kinds of recommendations or other things they can associate with that skill. Those credentials against it I think are becoming much more interesting for people to say, "Oh, this is someone I'm actually looking for."

(00:23:55):
And then the third thing I would really encourage PMs to start looking through is, this is probably more personal than anything in data, but every PM job is different. If you have experience in that industry and you're able to show that you have experience in that industry or some kind of understanding of it, I think that's a way to separate. I'd really start zoning in on roles where you might see if you don't have the functional experience, the industry experience. I think that would go a long way as how to help you differentiate from yes, what's probably more candidates, or more applications going into each role.

Lenny (00:24:30):
When you say industry experience, what's an example of that?

Hari Srinivasan (00:24:32):
Imagine that you are applying for a PM role, but that particular software is in, I don't know, automotive tech. If you happen to have worked in automotive before, have a knowledge about cars, that's a very helpful way to get in. I think if you're able to show that you can show an industry knowledge and an understanding of it, I think it's a real nice way to think about how to position yourself against some of the other candidates.

Lenny (00:24:55):
What else can that person looking for a job do to improve their chances of a recruiter basically finding them? I feel like that's probably the best tactical thing they can do because a lot of LinkedIn is recruiters reaching out and finding you.

Hari Srinivasan (00:25:08):
There's two things that anyone who's hiring is always going to look for. They're going to look for your skills and capabilities and they're going to look for your intent and interest in the role. A lot of our products and the pathways we try to do are making those things simpler. Maybe we'll just start with interest and we'll move back to skills in a minute. A couple of things we've launched recently, and I think they are symbolic of other ways you can connect. If you go to a company page and you're looking at the company, and I think they have to opt into this in some degree, look, you can say you're interested in that company even though they don't have roles. When the next role comes up, they'll have a signal that this person is actually very interested in this role.

(00:25:42):
That's an easy way to signify from an early stage that you have interest in them. That way, when they open up a role, as you can imagine, they start looking through, they'll have a spotlight on recruiter and they can click out on it and come through. Certainly, you can go into open work and say that this is something that I'm open to work right now, and you can signify to the whole population that this is an area that you want to go for as well. I would encourage both of those in some ways. If you're looking for a role, be open about it and tell the companies that you're looking for it. Those are really high signals of intent.

(00:26:09):
The other thing you can do on LinkedIn is you can actually go through when you say open to work and you can specify particular kinds of jobs and things you're looking for. I think that more detailed intent helps make sure you're showing it to the right place.

(00:26:21):
On the skill side, we talked about it a little bit, but I do think there's a big change. When you were just looking at title, I think you only had one way to really prove that you had the skills. You had to have that title, which is very hard to break in. In a world where you're looking at skills, you can go through and say, "Look, I can do these things and you could put evidence behind it." I'd really encourage people to do that. If you just go to any job post, you can see the skills, you can say add and you can see all the evidence and how you can add it. I would really encourage people to do that because when people are in recruiter and they're looking for skills, profiles pop up and you can scroll over a skill and you can actually see all those evidences.

(00:26:56):
Basically, a recruiter could say, "Oh, this is why I'd recommend you to this hiring manager." I think you will find that that's hopefully a very useful way of doing it.

Lenny (00:27:05):
I'm going to lob this question like a fishing line, to see if it catches anything. And if not, we'll move on. Are there any stats that you've seen of just like if you do X, Y, Z, your chances of getting hired or getting people reaching out just go significantly higher?

Hari Srinivasan (00:27:20):
Open to work certainly has a high signal to noise. As you can imagine, when someone's looking to fill a role, that's one they want. We are early in company commitments, but we are seeing some signal there that we got to move through it. Skills has a pretty high signal as well, when you're able to come through and show and demonstrate your skills. We're seeing some correlation to basically people getting a role.

(00:27:41):
And then the final one that is harder for us to look through, but it's certainly important. I do think we show the hiring manager on a lot of the roles. We show these people through. It's harder for us to trace that because of the way the outcomes work, but I would really encourage people to look through that and see if you can get in front of those people.

Lenny (00:27:58):
Is there a max seniority that you find works effectively on LinkedIn to find a job? I imagine CPOs aren't finding jobs on LinkedIn. If I'm looking for a job, do you have a rule of thumb of, if you're at this level, maybe you're not going to have a lot of luck? If you're below the-

Hari Srinivasan (00:28:15):
We certainly have CPO jobs that are posted, but the difference often is job posts versus recruiting. More and more senior roles are often recruited. We find that people will use LinkedIn in order to connect to a CPO and many people who are senior will say, "Oh, I got a message on LinkedIn and that led to this," or they made a long-term recruiting contact. But it may not happen through you finding a job and hitting the application button.

Lenny (00:28:38):
Let's talk about LinkedIn as a company to work in, the culture maybe for a bit. You told me that you have a story about your first product review when you joined LinkedIn and how that was wild. Can you just tell that story? I haven't heard this yet.

Hari Srinivasan (00:28:51):
Yeah. I came through a small acquisition that they made of our company, and I thought it was such a telling moment in this first product review. I went in and as you can imagine when you join a company, there's a lot of advice on how you should make that product work. I didn't know anything. I'd never been a PM. I remember taking a lot of that advice and putting together a presentation and just getting destroyed during that review. I think Jeff was the head of product and CEO at that point. In a very kind way, it was basically like, "Wait, this doesn't make any sense."

(00:29:23):
I just remember driving home and calling my wife and like, "I think I might be fired." I'm not sure if I was fired, but he was very kind about it. He's like, "Just come back and exit." I think five, four weeks. I remembered at that point I was like, if you're going to go in and you know you only have one shot, just do something you believe in and make sure it works. We started from that point and we worked backwards from there in this concept of, "Hey, I do believe that the most important thing is connecting to opportunity and we should really understand how to do that. Let's just start from there." It went very well.

(00:29:50):
To me, it was another way of you're in these large systems, you're in these large companies, you're in these large ... I think LinkedIn is very special because no matter what it is, it's got a very good North Star. It was a moment for me to really hammer that home, that as long as you get that North Star ahead of you, you're going to be just fine. I never worked at a place like that before, and I think a lot of times people wonder. You can imagine. The way we're talking about, we certainly have an engagement ecosystem. We have the hiring business and we have a marketing solutions business. We have a big premium business.

(00:30:24):
You can imagine when you're trying to make decisions across that, it could get very, very complicated. I think when people ask me to describe LinkedIn, I often start with that story because I feel like it helps cut through how decisions are made and what is seen as success here.

Lenny (00:30:39):
Just to clarify, so that North star is that phrase that you used of just connecting people to economic opportunity?

Hari Srinivasan (00:30:45):
That's it. That's it. I know it sounds bigger than it seems, but I can probably ... Time example again. You can understand when someone's driving on it. Having been here for a little bit now, you can understand when someone knows that and when someone doesn't. It's a hard thing to lose track of.

Lenny (00:31:00):
Yeah. It does sound vague and a nice, fuzzy, warm thing that people can say. What you're saying is that it's actually brought up in meetings constantly and product reviews. You're saying in this product review, everything changed when you came at it from that one perspective?

Hari Srinivasan (00:31:16):
Yeah. My first product here was the profile. You can make a profile that does a lot of different things, as you can imagine. You could think about how identity could be used in many different phases and what you should prioritize and not. But if you can explain why this is the thing that you should do that would help someone really do what they want to do, maybe it's have an incredible podcast and send that out there, maybe it's helping someone connect to a job. But if you can understand intent and how this is unblocked and why you want to prioritize that item, all of a sudden the world gets a lot simpler.

Lenny (00:31:51):
How does that actually get operationalized at a company? Is it just the leaders remind people of that? It's painted on the walls? How is that a thing that people come back to over and over?

Hari Srinivasan (00:32:01):
I do think it's a lot of repeat, repeat, repeat. I do think that's it. I do think the culture has a pretty high immune system now in the sense that when you aren't operating by that, people can see it and they operate against it. I think when Jeff was CEO, and Ryan, they are just exceptional at continuously repeating that. It's been so consistent for so long that I think it's just the DNA now. I do think it's exceptional. I think it's exceptional leadership, and I've learned so much from watching it and how it gets operated.

Lenny (00:32:34):
Is there a metric associated with that when people use it in a way of like, no, that's not actually what we mean? Is there some way of making it even more concrete in goals, metrics, ways to understand if people are actually achieving that?

Hari Srinivasan (00:32:46):
Yeah. Totally. I think at the next level of operation, what we think about is, when we run these marketplaces throughout this ecosystem that connect people to opportunity, what are the outputs that they measure? I'll just give you mine for example. We think a lot about number of hires, converting hires. How many people did we match? Which is a real tangible way of looking at opportunity.

(00:33:04):
And then number of people who learned a skill, which is usually in this world measured more by time than anything if you learn. Spend time for X amount of minutes. We do that skill because oftentimes skills don't have a direct outcome as you can measure to go through. We basically look at those things more than any other to say how successful that we are operating that marketplace.

Lenny (00:33:22):
Got it. Those make total sense to me.

Hari Srinivasan (00:33:24):
Yeah.

Lenny (00:33:24):
Are there other core values of LinkedIn that are public that you can share?

Hari Srinivasan (00:33:28):
You can Google them too and so they're very, very public, but probably the one that I think is most important to talk about in this world is, there's this concept of members first. I think anytime you run an ecosystem as complex as we do and you think about it, even if you're trying to connect people to opportunity, there's two people, how are you going to decide right now who needs it?

(00:33:49):
I think having clarity on which piece of the ecosystem is going to be where the focus is, it helps us make sure we establish a relationship of trust first, make sure to understand who's getting access to data, make sure we understand how decisions are being made. I always love that as a principle that we've stuck by.

Lenny (00:34:05):
Yeah, I see it on the page here. We put members first.

Hari Srinivasan (00:34:10):
Story checks out is what you're telling me.

Lenny (00:34:11):
Checks out. Checks out. What's interesting is the connecting people to opportunity, economic opportunity is not one of these values. It seems like it's even broader. They should at the company basically.

Hari Srinivasan (00:34:21):
The company, yeah.

Lenny (00:34:23):
Got it. Okay. I love that. This episode is brought to you by Eppo. Eppo is a next generation AB testing platform built by Airbnb alums for modern growth teams. Companies like DraftKings, Zapier, ClickUp, Twitch, and Cameo rely on Eppo to power their experiments. Wherever you work, running experiments is increasingly essential, but there are no commercial tools that integrate with a modern growth team stack. This leads to waste of time building internal tools or trying to run your own experiments through a clunky marketing tool.

(00:34:52):
When I was at Airbnb, one of the things that I loved most about working there was our experimentation platform, where I was able to slice and dice data by device types, country, user stage. Eppo does all that and more, delivering results quickly, avoiding knowing prolonged analytics cycles, and helping you easily get to the root cause of any issue you discover. Eppo lets you go beyond basic clickthrough metrics and instead, use your North Star metrics, like activation, retention, subscription, and payments. Eppo supports test on the front end, on the back end, email marketing, even machine learning claims. Check out Eppo geteppo.com. That's geteppo.com and 10X your experiment velocity.

(00:35:32):
You've touched on this idea of a complex system and I want to spend a little bit more time there. LinkedIn is, as you said, very, very complicated. There's all these marketplaces within marketplaces. There's so many customers you got to make happy. They all have to work together. I'm just curious what you've learned about building and maintaining a complex ecosystem like that.

Hari Srinivasan (00:35:55):
It's a fantastic question. I just openly think first of all, just career-wise, I've always been drawn to that. We talk about product as a whole. We always talk about it as a whole, but there's many different things you can build, many different types of things. And then we go, maybe there's hardware and software consumer goods. I actually try to think about products by their complexity curve a lot.

(00:36:17):
I think that the skills you need to manage a complicated ecosystem versus maybe the skills you need to design something that's less interconnected are quite different. I will get to the details maybe of what I mean in a minute, but I do think LinkedIn's a particularly complicated place. And I do think that the skillsets that you think through and you try to manage in a complicated ecosystem are quite different. Maybe some tactics that can help if it's something along those lines.

Lenny (00:36:42):
Yeah, let's do it.

Hari Srinivasan (00:36:43):
One of the things that I often think about is this concept of cause and effect. If you have non-interconnected things, it's actually quite easy not to have to think about that. You made something people love. I wrote a children's book not too long ago and it was fun. It was awesome to write. Once it was done, it was done, and it was out there and it was able to go. That's a little bit different than here. If you make a change, like open to work, all of a sudden you're thinking through the perception of someone on the other side. What is that going to do? Are they going to use the platform less or more? You're thinking about customers. What are they going to do with that data? Are they going to, to your point, perceive someone in a different way or not?

(00:37:21):
You have to think through second and third and maybe even fourth effects and manage that as you go through. I think that is something we really pride ourselves on is, how do we start thinking through these different things, and how do we start measuring them as we go? That is one.

(00:37:35):
The second thing I actually think is it does lead to your point a lot. You need a different kind of decision-making mechanism because there's a lot more ties in the ecosystem, a lot of people who just need a way to break it. We've put in things like we have something called RAPID, which is a really easy way to know who the decision-maker is. Just, you line up who's a recommender, who has to agree, who's a decision-maker. We have something called a five-day escalation rule, which makes sure that those items are in. I think you lead a lot more of those fuse, I don't know what they're called, fuse limits, or just systems in place in order to manage that complexity so that things get done. I think that those processes are actually really, really important to make sure that the ecosystem can run.

Lenny (00:38:10):
Let's talk about these two processes. RAPID, and what was the other one? Five-day-

Hari Srinivasan (00:38:14):
Yeah, five-day alignment. They've both been around LinkedIn for a little bit, but they're great. The RAPID is just a question of oftentimes to your point, if you're running two, three marketplaces, several different business model here, there's a question of who has the decision? Who can make the decision in this situation? Making sure that you have a single person's name with the decision and that person is ... That is really, really important because it gets the clarity real fast.

(00:38:36):
It's more of a personal rule, but one thing I love to say is, if you had three back and forths in an email, you got to pick up the phone. And if you've been on the phone for 20 minutes, it's time to just write that decision-maker and go. That way, you can make sure the concept of an hour, you should be able to get a decision. It doesn't always operate like that. I'm sure there's many PMs on LinkedIn who are operating here maybe, who may have some feedback from me on that, but that's the intent behind it.

(00:38:58):
And then a five-day alignment is, you should hold your managers accountable. That in five days if someone has something that they haven't been able to escalate and solve, that's probably then on the next level of person. But as you run that ecosystem and there's so much complexity around it, I think you need some of those processes in place in order to start answering some of those tiebreakers, if you will.

Lenny (00:39:17):
Ooh, I like that five-day rule. Basically puts the clock on a manager to get to unblock, basically?

Hari Srinivasan (00:39:23):
Yeah. Yeah.

Lenny (00:39:25):
With RAPID, I don't know if I totally understand. Is that an acronym for something? Or is it just-

Hari Srinivasan (00:39:29):
It is.

Lenny (00:39:29):
... make decisions rapidly?

Hari Srinivasan (00:39:31):
No, that's a great question. The D stands for decisions, but the R is for who's recommending it. The A, who has to agree. The I is for other people who may be able to be putting in an input. It's basically a list of people who need to be in the decision chain.

Lenny (00:39:44):
Got it.

Hari Srinivasan (00:39:45):
I would argue the most important thing is to have a single name on that decision line, because that usually makes sure that you can get a decision very quickly.

Lenny (00:39:51):
Are there any other really common frameworks or processes along these lines at LinkedIn that you find really helpful?

Hari Srinivasan (00:39:56):
The third thing is just in how we think about talent, especially in the product organization. I often really do try to suss out during interviews or in how we promote people, just their ability to see systems. Because again, I do think it's a different skillset and a different capability of how we map those things out on a complexity curve. Oftentimes, I think those talent systems will ... those who are able to see the whole, make decisions at the whole, that's rare actually.

(00:40:24):
I think most talent systems are, "Hey, how did your division grow or your product grow, your era grow?" We've tried our best to understand that it's not just about that. You want accountability in the ecosystem of course, but how well does this person work across? I think as we've created telemetry around that or organizational understanding of that, how we've understood ourselves, just, "Hey, this is the skillset that's really important here," I think that's quite rare in driving that kind of complexity system as well.

Lenny (00:40:52):
One more question along these lines.

Hari Srinivasan (00:40:53):
Yeah.

Lenny (00:40:54):
You've been at LinkedIn for a long time. It feels like historically, LinkedIn as a product team, the external impression was it's very optimizey-oriented and everyone there is just micro-optimizing all the little features of LinkedIn. Everyone I've worked with from LinkedIn, they're just really good at just optimizing things.

(00:41:16):
It feels like a lot of new stuff is happening with LinkedIn these days and I'm curious if that's been a real intentional shift of let's not focus so much on making emails work better and all the click-through rates of everything and more just, let's innovate more, let's do some bigger bets.

Hari Srinivasan (00:41:34):
I do think there's two things to acknowledge. First, there's an incredible growth team, and I think a lot of people that go on from LinkedIn in incredible roles are growth. I think there's an influencer change that a lot of people you meet might be growth-oriented. The second thing is, especially when LinkedIn started, and like you said, I've been here a little bit of time, but growing the network is probably a very, very important thing to get the scale out. I think a lot of things people interacted with at first were maybe more growth mechanisms than other systems.

(00:42:02):
I do think there's always been, at least for the last several years, an underlining line that value is what's going to carry this ecosystem, and value is ultimately what makes the day. To your point, I like to think that they may not be the most, I don't know, the glittery items, but I'm really proud of what we've done with skills. I think that's one of those invisible systems that no one really knows. Like, oh my gosh, that's a huge disruption if people can now get ... That's a huge language that people have created. That's a huge way that people have changed.

(00:42:32):
We're really proud of what we've done with values. Even open to work and commitments, these are major social systems that we've wired through. I'm really proud of what we've done with LinkedIn Learning. I would argue it's one of the bigger creator systems in the world. It's these incredible instructors and the ability to take someone who teaches, maybe is not great on camera, and move them to the studio and give them that capability and take their voice out there.

(00:42:55):
I think there's a lot of different things we've done that maybe because they're more invisible, if you will, or they're hidden in a marketplace that necessarily maybe a lot of the influencer voices may not actually need an access every day, I don't know if they get as much visibility. But I like to think that's been part of the DNA for a while and we've been really thinking through it.

Lenny (00:43:17):
Let's actually talk about LinkedIn Learning. I know this is a big passion of yours. You have your own course within this that I want to talk about. But broadly, just what is LinkedIn Learning, just so people understand? Because I don't know if a lot of people know this exists within LinkedIn.

Hari Srinivasan (00:43:29):
Great question. LinkedIn Learning is basically a way to learn professional skills. We entered the business in 2015 and the thesis was, we think about it as a marketplace again. You have seekers and job and oftentimes, seekers may not have all the skills in order to get the job. We're moving now towards the skills model, but without question, this other second-order impact. I don't think any of us wanted to, if you will, uberize the world. I don't think any of us wanted to make everyone there. We wanted to make sure everyone had the skills in order to learn the skills, in order to get there. Getting the learning business was really, really important for the vision and the mission. Basically, the idea was that we'd have ways to teach people skills that was very much tailored to professionals.

(00:44:12):
Now, that was the vision. The way the mechanism works is, we go and get the best instructors in the world. We will bring them into a film studio. We will do it at home or in a way that makes the content extremely ... We help write the scripts, we obviously have incredible graphic, in a way that makes a teacher and someone who's an expert who may not always have the capability or the time to go and make their own online course and get them in the studio and go from there. And then the vast majority of people will probably have access to it through their company. The vast majority of the usage and the business runs through enterprise and is a large enterprise learning product.

Lenny (00:44:47):
Awesome. Yeah. I'm just as a, I don't know, armchair quarterback strategy person, I could see where this came from of we're trying to help people connect to economic opportunity, find jobs. How do we help them? Oh, they don't have the skill? Let's help them build the skills. Makes a lot of sense. Okay. Within this, you have your own course on product management.

Hari Srinivasan (00:45:05):
Well, it's funny. I'd been thinking about a course for a while, but largely it was this concept of, I wanted to make sure I tried our own product and I understood the instructor pain point. But it's a very scary experience. It's like first, I don't know if I had anything to teach. My own concerns about that. But about four or five years ago, one of the things we started at PM internally was product university. We had our own internal university, which was basically we got some survey, we sent it out. I think everyone told us, well, it's literally the most negative one was people said, "I don't have the skills to do my job."

(00:45:40):
I remember looking around and I'm like, "Well, it's pretty obvious. We hired a bunch of people, there's no PM degree, and we've done nothing." What we started doing is internally creating a product university. It was a bootcamp coming in. We tried to get from different models and one of the things we really learned was, you can't teach this just through frameworks. You needed to have a series of case studies. You need to have a real series examples. But luckily, we had a bunch of things we'd done at LinkedIn, so we started putting a curriculum against that. And then just recently, a few of us got together and we filmed the actual course for it. It's basically taking our product university bootcamp and opening it up to the world.

Lenny (00:46:14):
You opened up some of your internal use cases as a part of this course?

Hari Srinivasan (00:46:17):
We do. Yeah.

Lenny (00:46:18):
That's awesome. I always say that one of the things you don't realize you have as an advantage working at a bigger company is access to tons of strategy documents and vision documents and stories of this. Because once you're out, no one's going to be able to share those with you because they're so private. I don't have access to any of these anymore. That's a really cool perk if you're working at a company like LinkedIn.

Hari Srinivasan (00:46:39):
Thanks. Yeah.

Lenny (00:46:40):
Question about your course. What are some of your biggest lessons that you teach? Can you just give a preview of some of the tidbits that you might learn in this course of yours?

Hari Srinivasan (00:46:48):
Well, again, a lot of it is case studies and use cases in the same way we teach it here, but a couple of things that we do talk through. When we started doing our own product university, we realized a couple big pain points that people hit. The first was, it's actually really hard to know how to validate and what the bar is for a new idea in any organization. I think it's really hard to say that. We provide a lot of framework. Simple things from, "Hey, you got to prove to the world why there's duct tape in here." There's someone actually physically going out and trying to do it.

(00:47:19):
How you can prioritize a list of ideas against a pain point, like how to make a simple expression, and how to look through what's an acute pain point and what's a wide range of people use, how we'd expect data in order to be used in order to validate this. Tools you could use to say if this is a good idea or a bad idea. More importantly tools to make sure you've went through the process and how you can communicate it. That's one framework set that we talked through.

(00:47:42):
The other is a lot about Damian, who leads our growth team. He comes in and he starts talking a lot about thinking in loops. How do you make sure that when you're building something you can have the fuel in order to cascade and grow? I think just the framework of doing that, how you measure that, how you monitor that, is also something that at least when I was starting and doing my startup, it was quite something I wish I had had access to. Those are maybe two good examples of frameworks and tools that we come through.

(00:48:09):
And then of course, trying to overlay that with real cases. Not always successful ones, of course, too. We talk about a lot of the failures we've had and where we probably went wrong if we had to diagnose them in postmortem.

Lenny (00:48:19):
A lot of the people listening to this are people that want to get into product management and aren't PMs yet. I imagine you get asked this a lot, how do I get into product management? What is your advice that you often give?

Hari Srinivasan (00:48:29):
Yeah. Well, let's start with how we look at the world, which is this idea of skills. We have a diagram that I think about, which is skills are on a triangle. You might have heard this one before. I don't know if you have. Skills are on a triangle, and I think you need three different skills to be a great PM. You need to be a Steven Spielberg type creator. Something around data science and the ability to really look at data and see patterns and then see the future. And then especially get more senior. I think it's a lot of general management. You have to basically be able to shine and innovate across the team, understand the budget, understand how companies differently work.

(00:49:01):
I've actually never seen a great PM who's in the center of it. I find the great PMs live on the edges. There's always someone who's this exceptional data scientist and the ability to maybe be a great GM and lead and inspire, or maybe someone who's so creative, who can lead a team in a different way. I think that one thing I would really, really encourage people to do is understand where they fit on that graph and gravitate towards those kinds of roles. Because a lot of times, I think what people do is they think they have to make up for the other pieces of that graph, and it leads them to a path where maybe they're not playing to their strengths. That's one thing I always encourage people.

(00:49:38):
The other thing I would say, and I know it's a little bit of luck in how this works, but I think about my journey, one thing I've really found was really helpful is, I was on the first team that did a hybrid SUV in the US. At the time, it was the Hybrid Escape at Ford. I came from the Midwest and it was one of those products where people would really drive out for hundreds of miles and see, and really a community gravitated around because it was a very special product. Being able to work on something that people loved, really loved early on, and see what that felt like and look like and that success was, it created a bar for what I would hope my products could do. It would.

(00:50:17):
If you're able to get into something that people really love and feel that and experience that, and really understand what that looks like and what it takes to get there, I think that's actually been a really valuable lesson throughout my career because you can understand the whole path on the way up. I look back at that as really something that I would hope other people if they can do it. I know you're making world decisions on many different criteria, but try to find something people love and really experience what that feels like.

Lenny (00:50:40):
To build on that, with PMs that work for you and work with you, when they're looking to get better and build their skills, other than go take some courses on LinkedIn Learning, what do you often recommend they do to help become stronger and better at their job?

Hari Srinivasan (00:50:56):
First, it is that feeling of, you got to own your product and you got to speak up and say this is where I want to drive it. Because a lot of times I think people are scared to do that, or worried about doing that, or don't feel that's their actual role. One, it's extreme clarity on hey this is your role. It's to own this and take this to the next level. When you start molding the clay, people want to come and help. When you start building something cool, people are like, "Oh." They're gravitated to it. But until you can start doing that, that's really tough. One, it's letting people know that's what's expected of them.

(00:51:26):
And then two, I would tell people to just build. As crazy as it sounds, I spend a lot of my time on the side, just trying to build different things. Try different clay, think through different ideas. I think that is a really important skill to have, to just being able to say, "Okay, I'm going to start with a blank sheet and make some art," or whatever it is you want to do. I encourage people to do that because it's a muscle, like anything else. It can atrophy. I really do think no matter what the heart of PM, in is that ability to be a builder, and you do got to make sure you can keep doing it.

Lenny (00:51:57):
Yeah. That's actually a great segue to where I was going to go next, which is, you say you build and you like to build stuff, but you're legitimately building a lot of stuff. You have the site, mindofhari.com, where you share all these side projects. Can you just talk about what's going on there and some of the stuff that you've built?

Hari Srinivasan (00:52:12):
Yeah. Arguably, the only thing I've ever been good at in my life is just building things and creating things. I get a lot of energy from it. Yeah, I have a site. It's called Mind of Hari because it is really whatever's top of mind. I try to do my best to completely separate it from business. I know there's always a draw as a good PM to say, is there a business here? But I try to keep it as art. It's completely art and it's what I want to build. I take on new subjects. I have two little kids and it's fun to ... One of them was a book me and my oldest wrote, and it was a set of bedtime stories we did. And then one day I was like, "Hey, we should just make this a notebook." And we did it. I think it's got about half-a-million readers now. It's been fun to see it take some life and go through.

(00:52:57):
We made a board game recently that I know Stanford Design School or some professors there have been using, and it was called Parallel Universe. It's, how do you have a card and then be able to see maybe the card says there's no windows in this world anymore, and then what would happen in that world? You got to list 10 different things that would happen. That ability to think ahead, the fun sci-fi stuff. I make healthy gummy bears. I just try to take something completely new and have that. I don't know, it's probably one of the more fun moments in this world where you can sit there and just create something and have some new clay. Yeah, that is what that website is about.

Lenny (00:53:34):
Wait, so you made actual gummy bears?

Hari Srinivasan (00:53:36):
Yeah, we are doing something with gummy bears. Lenny, I know you're expecting a new addition. Congratulations, again. But one of the things I found when I had kids is, no matter what I was trying to do, there was candy and sugar everywhere like any Halloween, any birthday party, et cetera. You can't get rid of it because it was just hard to do. So we were like, hey, we're going to sit down and make our own gummy bear. What I found is, this is just a fun tidbit for your readers, if you open a Twizzler or one of those, about 80% of what's in there is sugar because they're optimizing for shelf life. They're optimizing for what's in the store.

(00:54:07):
What we were able to do is basically create a gummy bear. About 40% of it is sugar. It's just got five ingredients. Honey is the sweetener because I don't want to give my kids some alternative sweeteners. But we have a small commercial kitchen and we produce some gummy bears. If you ever want to try them, to any of your followers, I'm happy to send some gummy bears and hopefully you can check them out.

Lenny (00:54:27):
Wait, is there a way to buy them somewhere?

Hari Srinivasan (00:54:29):
Well, you can go to Mind of Hari. We stock them seasonally. One of the things that we found out is there is different laws on how they can be shipped, and obviously we're not optimizing for long storage. But they'll be on Mind of Hari. You can always reach out to me and I'll find you and tell you which farmer's market we're at or whatever and you can come swing by.

Lenny (00:54:48):
Well, I don't see it on Mind of Hari, so maybe by the time this comes out, put it on here. Or if you're trying to-

Hari Srinivasan (00:54:53):
Put it on there?

Lenny (00:54:54):
Yeah.

Hari Srinivasan (00:54:54):
Yeah, it's on the homepage. And then when they're stock, we put them in the shop.

Lenny (00:54:57):
Okay. That means they're out of stock? All right, we're going to sell you out. Let's get all your gummy bears. With that, we've reached our very exciting lightning round. Are you ready?

Hari Srinivasan (00:55:06):
Yeah, let's do it.

Lenny (00:55:07):
What are two or three books you've recommended most to other people?

Hari Srinivasan (00:55:11):
The first one is called Thinking in Systems. It's the one I give the team every now and then. It's just a really good book about how I think sometimes people see systems. Can we talk about it? It could be abstract. I think it goes into real detail on how people can intervene at various parts and how to take actions at different systems. I really enjoy that book.

(00:55:31):
Not directly maybe a book I recommend, but a book that I just read that I thought was phenomenal, just to give it to readers if they want something good, it's called Tomorrow, and Tomorrow, and Tomorrow. It was recommending by a friend. Have you read it? You read it?

Lenny (00:55:41):
Yeah. I honestly didn't love it, but I liked it a lot.

Hari Srinivasan (00:55:45):
For some reason, I've been-

Lenny (00:55:47):
It was sweet.

Hari Srinivasan (00:55:47):
I thought it was very well done and there's a couple chapters I reflected on. I just finished it. I thought it was well done. That's one that I'll throw out there.

Lenny (00:55:54):
Yeah, it was very sweet. I feel like it got hyped too much for me. I'm like, okay.

Hari Srinivasan (00:55:54):
Oh, I didn't actually know it got-

Lenny (00:55:54):
I think that's the key.

Hari Srinivasan (00:56:01):
... much publicity. Okay, that's it. The third one that I just downloaded because I finished it, I'm actually going to open up my audiobook and tell you because I'm about, I don't know, an hour into and I'm really enjoying it, it is An Immense World. I don't know if you've read that one yet. It is about animals and how animals have different senses out there. It goes through a set of different animals and how they see the world.

(00:56:24):
Just one of those reminders that we're so limited sometimes in our own perception and how dogs, for instance, they can breathe in and take in sense even when they're breathing out. It's like vision almost, and it's just phenomenal to me just to think about all the things they're probably sensing as my dog and I are going on our walk.

Lenny (00:56:42):
I've learned dogs shoot air out of their nose first before they smell, to clear things out.

Hari Srinivasan (00:56:48):
Isn't that wild? They can probably see so much more of what happened in the history of a little walk than we're able to just because of that.

Lenny (00:56:57):
Incredible. Next question. What is a favorite recent movie or TV show?

Hari Srinivasan (00:57:03):
One thing we try to do is watch TV as a family. It brings us together a little bit. We are doing Star Wars with the kids, which is for the first time, which has been a really enjoyable experience, just being able to witness it through them. And then we've been going a little bit back in time. We watched ET. It's fun. It jogs your memory. These are phenomenal movies that we go through. I think your question is on recent TV shows that probably came out more recently.

Lenny (00:57:27):
Those work just as well.

Hari Srinivasan (00:57:28):
Yeah. The other one I did like, it's not a TV show but I ... God, what was it called? It was that podcast that came out. Case 63 I think it was called? Anyways, I hope that's the right name of it. But it was a sci-fi podcast. It was like 10-minute shorts. The premise of it is someone comes from the future and there's a little bit of speculative fiction and is at a psychologist. It's just a phenomenal piece. I'll have to get you the real name. Maybe I can get it for you after for the show notes or whatever.

Lenny (00:57:56):
Yeah, we'll edit your words and add that-

Hari Srinivasan (00:57:59):
Yeah, exactly.

Lenny (00:57:59):
... whatever's in the show notes, that's the one you meant. What is a favorite interview question you like to ask?

Hari Srinivasan (00:58:06):
I do like to ask people what the most complex thing they ever built was. I just love to understand mostly, what do they gravitate to? Is there something you gravitate to? And two, are they able to simplify it? I think those are two really important skills.

Lenny (00:58:19):
What is it that you look for in their answer that tells you it was a good answer?

Hari Srinivasan (00:58:23):
Both of those things. First, did they take on something that was super complex, really, really hard? Because I think there's only a particular group of people who gravitate to those kinds of problems. I do think more and more openly. I think that's a lot of, in my opinion, the ways the world is going to get better by the things that are really, really hard to solve. Intimacy doesn't scale. When you think about how people are going to feel more connected, it's going to be a lot more difficult to solve. When you think about healthcare, it's going to be very, very difficult to solve. Education is a very difficult interconnected space. I think people who gravitate to that, know those problems are hard, have a very special gift. It's hard to replicate that passion. So one, did you do that?

(00:59:06):
And then two, I think people who really understand systems are able to, somehow this is truly, especially people probably way smarter than me, they're able to simplify it. They're able to explain it and say, "This is how I looked at it, but here's how I modeled it. Here's the lovers and how I went after it." Even if it's nonlinear, they're able to say, "This is how the cause and effects works." I'm really looking for once you did it, did you really understand and were you able to crack it? Or at least, did you understand why you weren't able to crack it? I usually find this to be also the most rewarding conversations.

Lenny (00:59:35):
Awesome. Thanks for sharing all that.

Hari Srinivasan (00:59:36):
Yeah.

Lenny (00:59:37):
Next question. What is a favorite recent product that you've discovered that you love?

Hari Srinivasan (00:59:42):
I'll give you one more dad one. My youngest just hates brushing his teeth. Just was like, it was always a thing. I should actually find the name of the toothbrush, but you can just Google or Amazon this and you'll figure it out. Basically, it's like it was this Baby Shark toothbrush, but it's a game. You play that game for two minutes and you can try to pick up different prizes, you brush your teeth.

(01:00:02):
What I loved about it, because I think it's what all great products do, it turns a moment of annoyance to a moment of joy. It went not even just like you solved a pain point. It was an unreasonable experience of like now he loves it. It was just so well done. It's like 10 bucks, and it was 10 bucks extremely well spent. So much delight. Whoever made that toothbrush, thank you.

Lenny (01:00:23):
Damn. Is it playing Baby Shark? I hope not.

Hari Srinivasan (01:00:26):
Well, it can. It has that feature. It has that capability, but it is a small price to pay for me to get out to enjoy.

Lenny (01:00:35):
Good times. What's something relatively minor that you've changed in your product development process that has had a big impact on your team's ability to execute?

Hari Srinivasan (01:00:44):
I do like to change things relatively. Every quarter or six months, sit down and say, what can we get better at? The two areas I find myself innovating, if you will, innovating or tweaking the most, one is around planning. I think every company struggles with this. You get bigger, it probably becomes a more different ... especially when we talked about the complexity of the ecosystem. We started this thing where just basically we call it orange and red priorities. Which is, then a lot of times what people do is, teams will plan bottom-up.

(01:01:12):
They'll come into a manager or a leader and then the leader may shift things around or say, this is what ... I think we've really started shifting it in a different way. We said, these are the big rocks we got to get done. We're going to get those things done first. We're going to be upfront and honest with you, and these are the things and these are price. And then you can plan from there. I think it's relieved a lot of the progress. I think there's an honesty that comes within and that's been a big change.

(01:01:34):
The others just are the way we review products. That's always been a thing. My read is, when we keep our product review process live too long, it gets a little institutionalized and people start making long documents and stuff. You always have to change that every quarter. Basically, I think it always comes down to the same thing, which is, how do you get their problem statement quickly? And then how do you design from there? But the lever that we basically put in place for that was to really shorten the time.

(01:02:00):
I'm trying this thing, I don't know if it's going to work. But could we get to 15-minute reviews basically instead of an hour and see if that alleviates some of this? I'll let you know how it goes when we chat up next, but I'm very curious to see if this is going to be a different kind of system where we might be able to get to clarity quicker, or realize we're not at clarity and then break and come back.

Lenny (01:02:21):
Reminds me of a tweet I think I just saw. Maybe it was an Instagram post of teams that do stand-ups while doing a plank, to keep the meeting really short.

Hari Srinivasan (01:02:29):
That's interesting.

Lenny (01:02:30):
Could be the next one.

Hari Srinivasan (01:02:30):
I haven't tried that one yet, but it might be something we try next.

Lenny (01:02:34):
Last question. You've been at LinkedIn for a long time. I imagine you use LinkedIn a lot. Is there just a pro tip that you can share of how to be more successful with LinkedIn, find more value in LinkedIn, enjoy it more?

Hari Srinivasan (01:02:47):
The first is, I do think certainly there's ways, and the majority of ways that skills work is we infer skills. But I think that there is a skills section on the profile. I think a lot of people ignore it because they don't realize that there's value in it. That's changing, but I'm not sure if it's changing for everybody. I would pay more attention to skills as we get more into the skills-first stuff.

(01:03:05):
The second thing I would probably do, I don't know if it's that hidden, but I would check out LinkedIn Learning. I do think LinkedIn Learning is a gem. I think because it's sold largely through enterprises, a lot of people miss it. I would hope you check it out. But more importantly, tell me areas that we could get better on there as well. I hope that people will find value there.

Lenny (01:03:22):
What's the best way to find out about LinkedIn Learning? They just Google LinkedIn Learning and they'll find the-

Hari Srinivasan (01:03:26):
Yeah. Or go to LinkedIn/learning. Yeah.

Lenny (01:03:30):
Linkedin.com/learning? Okay. Great. Hari, I feel like we've opened the Mind of Hari up on this podcast. I appreciate you being here. Two final questions. Where can folks find you online if they want to reach out, and how can listeners be useful to you?

Hari Srinivasan (01:03:42):
Well, you can find me on LinkedIn. That's an easy one. I do really, really, really appreciate product feedback. I promise you I take it well, for those listening. And two, going back to the heart of this conversation around complexity, it is really hard to know sometimes what everyone's experience is because you're living in a very abstracted ecosystem. The more you could just say, hey, this is working or not, and the intentions are coming from a good place, and if you have a moment and you're not having a great experience, or you are having a great experience, you could write it. I really would appreciate to hear your perspective.

Lenny (01:04:15):
Amazing. Hari, thank you so much for being here.

Hari Srinivasan (01:04:18):
Thanks, Lenny. It's great meeting you.

Lenny (01:04:20):
You, too. Bye, everyone.

(01:04:23):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

