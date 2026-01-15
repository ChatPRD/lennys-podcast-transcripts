---
guest: Brandon Chu
title: 'AI prompt engineering in 2025: What works and what doesn’t | Sander Schulhoff'
youtube_url: https://www.youtube.com/watch?v=eKuFqQKYRrA
video_id: eKuFqQKYRrA
description: Sander Schulhoff is the OG prompt engineer. He created the very first
  prompt engineering guide on the internet (two months before ChatGPT’s release) and
  recently wrote the most comprehensive...
duration_seconds: 5867.0
duration: '1:37:47'
view_count: 78637
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- onboarding
- metrics
- roadmap
- prioritization
- experimentation
- funnel
- conversion
- revenue
- hiring
- culture
- leadership
- management
---

# Lessons from scaling Uber and Opendoor | Brian Tolkin (Head of Product at Opendoor, ex-Uber)

## Transcript

Lenny (00:03):
If you're a product manager, you've almost certainly come across one of Brandon Chu's Medium posts. His writing about all aspects of the job is some of the best writing out there on the skills of being a PM, and has informed a lot of my thinking on both product management and writing. Brandon is currently a VP of Product at Shopify, where he's been for seven years, and in our conversation, we talk about what it's like to build product at Shopify, what Shopify has learned about being effective working remotely, having done it from day one, the impact of writing on one's career and how to get started, the benefits of becoming a platform PM, the manager track versus the IC track, and a bunch of other stuff. Brandon is a wealth of knowledge on the art of product management, and I'm really excited to bring this episode to you.

(00:46):
Do you want to reduce friction in your onboarding flow? Then let me tell you about Stytch, and that's Stytch with a Y. Stytch is on a mission to eliminate friction from the internet. They're starting by making user authentication and onboarding more seamless and more secure. They offer super flexible, out of the box authentication solutions for companies of all sizes, from email magic links to SMS pass codes, one tap social logins, to even biometrics. Stytch is your all-in-one platform for authentication. Stytch customers have been able to increase conversion by over 60% after spending just one day integrating, and with their API and SDKs, you can improve user conversion and retention and security all while saving valuable engineering time. Your engineers will come and thank you for using Stytch, because Stytch keeps you from having to build authentication in-house, and the integration process is super fast and super smooth. To get 1,000 dollars in free credits, just go to stytch.com, and that's Stytch with a Y, and sign up and just mention that I sent you.

(01:52):
This episode is brought to you by Persona. Persona helps founders, product managers, and engineers easily solve any identity related problem, including handling KYC, AML, and basically all manner of identity fraud. You can integrate Persona in an afternoon, and personalize your flows using their SDK to meet your users on any device. Persona's identity building blocks allow you to manage your entire end to end onboarding flow, verifying that each new user and their data are legitimate. Persona is trusted by both startups and the world's largest companies, including Square, BlockFi, Gusto, and Udemy. And for a limited time, Persona is offering listeners of this podcast a free end to end KYC and AML solution, where you can collect the user's government ID and/or their selfie, and automatically verify that those two pieces of data are legitimate. You can also enrich that information to automatically see if the person exists on various watch lists. Just go to withpersona.com/lenny to get started. Brandon, thank you so much for joining me.

Brandon Chu (03:01):
Hey, Lenny. Thanks for having me.

Lenny (03:03):
I'm curious. When you were younger, what did you want to be when you grew up?

Brandon Chu (03:06):
An astronaut.

Lenny (03:07):
Say more.

Brandon Chu (03:08):
I've always just had a longing for space. I have a vision in my mind, and I still think I'm going to do this. One day, I'm going to see the whole earth in one view, and it's going to make me feel... This is going to sound weird... But make me feel really small, which I think will make me feel connected. And so, even since I was 16, I've been saving 2,000 dollars a year in a separate account that I just invest into the market, because I calculated that it would cost half a million dollars by the time I was 55, and I think it's going to actually work out timing-wise, because it's like the cost is coming close.

Lenny (03:40):
This is an amazing story. That's a very PM-y way of approaching it. Just start putting money away.

Brandon Chu (03:44):
I guess so.

Lenny (03:45):
Plan for going to space, hoping the tech would catch up. This is going to be a great podcast V2 when you're on your way to space.

Brandon Chu (03:51):
Yeah. We'll do it for sure. I'll bring my Starlink up there.

Lenny (03:54):
I just got an email from Starlink that you can now move your Starlink around and get internet as you move.

Brandon Chu (03:58):
Oh, that's amazing. So they're going to have a mount on Teslas and you just plug it into your Tesla and just, yeah.

Lenny (04:04):
Exactly. It's all coming together. Okay. So you wanted to be an astronaut, eventually got into product. I love to hear... I like that segue. I got into product initially and then just kind your journey to where you are today, which is VP of Product at Shopify.

Brandon Chu (04:19):
So way back in university, I kind of grew up actually in the era where people really wanted to work on Wall Street still. So I actually came up through the finance ranks and stuff like that. And I worked in industry at Kraft Foods of all places for about four years, but how I kind of broke into product management is I got really bored that really quickly. And I started moonlighting and bootstrapping a startup on the side and it was called Tunezy and it helped YouTube musicians at the time, which were blowing up. This is kind of when Justin Bieber was becoming famous by doing webcam cover music and stuff like that. And we helped YouTube musicians monetize their fan bases by offering fan experiences at their tour stops. And so this was really early. This is before YouTube even had a music category. And so my co-founder and I, neither of us were technical, but we were pretty good at pitching.

(05:08):
And so we kind of entered a lot of startup competitions and we got some funding and some office space and we quit our jobs literally the weekend after we won that. And then fast forward three and a half, four years, we never really made a really big company out of it, but we kind of soft landed sold the company. And I'd say that's my first foray because my job as a co-founder there was really to work with engineering and design. And it was through that experience that I learned everything about product and I got a lot more technical too. I was able to do a little bit on the front end. And so from that, after the acquisition and the integration that parlayed that into product management career basically. So I joined a growth stage startup in Canada, in Toronto called FreshBooks, which is still around today.

(05:50):
They're a Series D company now. And I kind of learned the chops of product management there because the folks there were X Microsoft 15 years, really technical, process-oriented and framework heavy product management. And I had my just scrappy entrepreneurial experience. So I kind of hardened my PM skills through that over about four years. And then I joined Shopify the week of the IPO actually. So that's almost seven years ago and it was one of the largest companies I ever worked at. I had 500 people even then at least because I'd been in startups prior. So I thought maybe the story's over.- But as I met Tobi through my interview process, I realized that that was definitely not true. And it obviously is not true now.

(06:30):
So yeah. I've been seven years there, various PM roles, areas of the product and then eventually really started to build some domain expertise around platform management and developer ecosystems and kind of grew my career there. And through that domain, became product director and then a VP of product. And then in classic Shopify form, I completely threw it all away and started something a little different inside the company 18 months ago. So now I lead what we call product acceleration, which is the team that does all of Shopify's investments and then [inaudible 00:07:02].

Lenny (07:02):
Amazing. So I was looking at your LinkedIn and just hearing this story, especially the Shopify piece, it's a pretty incredible trajectory. And imagine a lot of people listening to this may be like, "Shit. How do I follow a similar path? How do I do it Brandon did." Do you have any advice about what it was that helped you, either habits, skills, behaviors that helped you get to where you're today that maybe newer PMs could learn from?

Brandon Chu (07:26):
I think what I learned over the arc of my career is that especially when it comes to product management specifically, it's a lot of the hard skills that PMs are known for, so organizational, analytical, good communication, even technical skills. There's sort of table stakes and commodities to be an entry level PM. And to be clear, it's not easy to be a PM. It's not an entry level job. And so that is no knock on that. I'm saying to grow beyond that though, I think domain expertise can take you a little bit further like if you're an amazing payments PM or you have some really nuanced knowledge and whatever, 3D modeling or something like that.

(08:05):
But I think ultimately to have the highest trajectory and what certainly was a tailwind for my career was you guys have to lean into those founder skills. And so things like being a great storyteller, how to get the most out of people around you, foster creative and motivated teams and know how to make really, really hard high conviction decisions that actually can't be solved. You got to take a leap of faith and how to do that and bring teams through that type of ambiguity and then how to lead by example and have accountability when you make those choices. So I found that ultimately, those really became the things that were limiters for some careers I observed and then were definitely propelling for a lot of the people that made it to high level of leadership.

Lenny (08:47):
Awesome. And I know you wrote a lot about a lot of these things, which we'll talk about your writing, which I'm a huge fan of and I have been a fan for a long time. But before we get into those, I want to chat a little bit about Shopify and your experience at Shopify and just understanding the product culture at Shopify. As an outsider, Shopify feels like an incredibly strong product culture. And I know a lot of amazing PMs that work there and even outside PMs, just generally amazing people. What would you say are some of the defining characteristics of how teams build product at Shopify maybe that are different from how other companies approach product?

Brandon Chu (09:20):
Shopify has an incredibly strong product culture. Whether it's uniquely different, I can't know for sure, but I would say I'd start with, it's a highly technical company. That's not unique, but it's just something that should be known about Shopify. When I joined, all project management was just in GitHub, just commenting on poll requests and even marketers in order to augment or upload a blog post, you'd have to commit and deploy it. So there was no breaks given for folks that didn't want to touch code and stuff like that. I think it was very much and this all stems from Tobi, a very well renowned developer in the Rails Core community and it all kind of flowed from him.

(09:59):
And so because of that, I think everyone in the company had their hands really deep in the product regardless of what function you are, which brings me the second thing I think is really awesome with Shopify, when it comes to how the product org works, it's that we don't actually put the product org on a pedestal as the only people that can have an opinion about the product or should be listened to when we think about what should be built. There's sort of an understanding of Shopify that everyone at the company from engineers to support, to sales, everyone's responsible for product thinking and it's not just the area for a small group of PMs.

(10:38):
And so that's some of the foundations of it. And again, all stems from Tobi. I'd say the last one is that this comes from the fact that we have Canadian roots. And I say that actually in a way that's almost opposite of the stereotype when it comes to tech anyway. There has been a lot of failed tech companies in Canada and no company that's ever truly been global. And so ambition and a founder mentality has been something that we've architected the culture of the product team around. And so 30 to 40% of the PM team are ex founders either through failed startups or through acquisition.

(11:15):
And this is really important to us for obvious reasons about just versatility and grit and growth mindset but then also we are building a platform for other entrepreneurs, whether they're merchants on our platform or developers to build their own stuff. And so we have a lot of empathy for our customers through that. And so the way this is all kind of coalesced is the one liner job description we give to PMs as they come in is "Your job is to help teams ship the right thing at the right time in the right way." And it really comes down to two main concepts. There's help teams. So it's like servant leadership. You're not necessarily the CEO of the product. You're not dictator. Everyone's responsible for product thinking and you're there to help the team get to ultimately the right thing. And that is what you are accountable for.

Lenny (12:00):
I love that definition. In practice, do you give PMs a little bit more sway over decisions or do you try to keep it completely equal amongst functions?

Brandon Chu (12:10):
Actually, I think it depends on the level. So I think as you go to towards more the junior PMs and the ICs, there is a much bigger emphasis on balanced decision making between all the Kraft's user experience and engineering, of course. And then it's more when you get to director level or above, that's when there is more emphasis put on where the PM wants to lead, because ultimately, it becomes a pure strategic function at that point and that is your only job. Your only job is to say, "We need to go there and my ass is online for us going there." And so that is something I think we matured into. There was obviously lots of tension as we grew of, "Hey. We used to collaborate, but now you're saying we have to do this thing." And it's like, well, actually, the company, the context changed, my role changed and we have to do something and it has to be someone's job to make that choice. So it's a bit of both is the answer.

Lenny (13:05):
Awesome. Spending a little more time on decision making in general at Shopify. Is there kind of a framework or a specific process you guys use to make bigger decisions?

Brandon Chu (13:15):
What we do have is an annual planning cycle basically, we call investment plans and it's for fairly large SWOTs to the organization. I'm talking like 20% chunks of all of Shopify consolidated under a VP here and there to put forward a vision for what that team's going to accomplish that year, whether that is a directional change or even specific outcomes in some cases. And we spend time aligning with both Tobi, the rest of the C level exec team, even sometimes the board on what that is and what headcount may go with that and what not. But that's sort of the main arc of planning. What happens after that is just chaos, all the teams underneath and like I said, one fifth of Shopify may be moving towards one investment plan, that's at this scale almost 2500 people. Right? So they're all now chaotically moving towards those end goals and iterating through ideas good and bad.

(14:15):
And so this is actually where Shopify is a really hard place too, because we do this because we recognize a couple things. One is it's important that we set broad direction, so everyone can put their energy towards the right place. But we also want a place where we're hiring smart people so that they can figure out what to do. And we also know that in software and in tech and in this world, things change so rapidly. So don't even kid yourself that we're going to plan out everything we're going to have to do for the next year to get there. And so we set this directional kind of outcome and vision based kind of north star for where we want to go. Then product directors start to basically shoot their shot and say, "This is how my group can contribute to those things. Here's what we're going to try to commit to in the next quarter basically."

(14:58):
And it's through that almost back and forth, the trust battery thing that I was talking about plays in. Again, they're selling it to their peers, the engineering directors. They're selling it to the VPs. They're selling it to the broad team as well to get momentum behind it and to say, "You know what? This feels right. Let's start doing that." But what's really amazing and also difficult about Shopify though is we're pretty good at never falling into sunk-cost fallacy. So we'll throw it all away anytime if the world changes. Right?

(15:29):
And so that's why it's actually a really tricky place for a lot of folks because there are cases and it's happened to me many times where it's just like you're building three, six months into something and it's just not important anymore or the world changed. And so that's kind of how the sausage gets made. And it really comes down to giving teams the agency, giving product folks at certain levels the responsibility to make a bet, and then having the humility to understand that soccer's hard, the world changes and that we always have to ask ourselves this is the most important thing that we can do right now.

Lenny (16:03):
It's so important. A lot of companies just want to avoid upsetting people, want to avoid creating chaos. And it's so important to always be rethinking even if it's like we just put a plan together, maybe we should change it because things have changed. And so I'm not surprised Shopify is really good at this.

Brandon Chu (16:20):
To give an example, during COVID, this cultural resilience we had to change was so vital because all of a sudden, these grandiose ideas and visions we had for 2020 didn't matter and what mattered was like, "Oh, shit. Retail businesses are going from a hundred percent to zero." It's like 0% revenue overnight. And how do we help a brick and mortar store across the street now do order online and pick up it in store? How do we do that? How do we throw away everything? This is what matters now. Let's try to ship three things in the next month that matter." And that's very jarring, I think, unless you have a culture that just understands that can happen any day and it kind of gets excited by those.

Lenny (17:02):
I'd love to actually hear whatever you could share on the COVID period of Shopify and just what folks did to work through that.

Brandon Chu (17:08):
Yeah. Through all the roadmaps, we asked ourselves, "Hey. Our customers, their livelihoods are at risk right now." And this is when no one knew it would actually be a tailwind for e-commerce. Right? We didn't know the severity of COVID. It could have been a really, really bad pandemic from a death rate perspective. So no one's betting like, "Oh, everyone's going to stay home for two years and everyone's going to buy stuff online." Everyone's like, "Okay. All our customers are going to go to zero, unless we help them figure out how to actually survive through this."

(17:40):
And so of course, online only merchants or merchants who were well established online have that infrastructure. There wasn't supply chain issues yet. So they're good. The focus then turned, of course, to all these both hybrid brick and mortar online customers and customers that are only brick and mortar. And so we did all those things. Some restaurants and grocery stores on the platform, how do we help them do exactly that buy online, pick up at the curb? How do we help them launch buy gift cards now at a discount so that basically you can, as a consumer, help these companies stay afloat. If you recall back in 2020, that was a huge thing. Buy gift cards at the restaurant you like, because if you don't, it might not exist.

Lenny (18:22):
I did that a bunch. I remember. Yeah.

Brandon Chu (18:24):
So these things exist on Shopify in apps because they were never really mission critical, but now it became really mission critical. So all of a sudden we're trying to gear 500 people towards ship gift cards, which sounds like a really small feature, but it's pretty hard when you have millions of merchants and hundreds of millions of consumers using your platform every day, ship it in two weeks. And so it became war time truly. And yes, Tobi got way more involved, as did Craig Miller, our CPO at the time. And we went down from trying to ship maybe the 40 things that quarter to three and nothing else mattered. And that became the rhythm of the company for almost that entire year.

Lenny (19:09):
Wow. How long did that kind of war time period last internally?

Brandon Chu (19:13):
I'd say the edge came off a little bit I think mid 2021. It wasn't that long ago actually, maybe about a year ago that it started. I would say it never really left war time per se, but everyone sort of adjusted to it. And so many other things were happening because we had offices before and we made the decision very early in the pandemic to say, "We're never going to have offices again. We're a digital by default company. Hire anywhere in the world, but let's make sure we have really great infrastructure." And so there was so many things happening inside the company that just changed. It really changed overnight. Shopify, the experience, the culture of the company changed overnight. And so it's hard to say when it stopped, it just evolved.

Lenny (19:58):
I wanted to actually ask about that and so I'm glad you brought that up. The fact that Shopify's been very remote friendly for a long time, I imagine it's rooted in the fact that it was founded in Ottawa and it's probably hard to hire the scale of people that you're all hiring out of Ottawa. And I imagine there was an advantage to having a lot of that experience working remotely in this new modern world. And I also imagine wasn't easy still, but what I'm curious about is what sorts of things have you learned about working remotely that you can share that other companies can maybe learn from Shopify's experience?

Brandon Chu (20:31):
Finding enough that in-person still matters. It does. And that doesn't mean we're rolling back at all the fact that we're remote only, but what we've done is we've actually instituted with something we call bursts. So bursts at Shopify are the ability for your team generally maybe once a quarter or whatnot, to just come together to do really high velocity creative work together, to hang out together. And so we've gone pretty far on this where we actually have in-house built web and mobile apps that allow teams to one click, say I have 20 people. We want to do a burst in Laguna Beach and then click the button and then flights get booked, hotels get booked, food is taken care of. No one has to pay any. There's no expenses that go back and forth. The app itself helps you check into those places.

(21:24):
And we have really cool experiences. And in France and Ireland, I'll leave a little bit to the imagination, but it's really cool. So we started allowing kind of that as the world opened up for travel and now teams are doing it all the time. I'm going next week actually to one with our team.

Lenny (21:24):
You just do a personal burst. I just want to go to The Bahamas first.

Brandon Chu (21:46):
You can try. We've done other things too, because you spoke in Bahamas. I actually worked out of the Caribbean for five weeks in March. And because we also had a policy that we instituted that said for 90 days out of the year, you can work in any country you want. And so what we tried to do with a remote only world is we tried to turn all the weaknesses on its head and to say, "Okay. Well, we can't see each other every day, but let's remember all the ways that sucked from a commute perspective and even when you were together, if you were just working in your desk and never even talking to each other, that wasn't great. So why don't we just optimize for the stuff that was amazing about it and make it super easy and fun?"

(22:23):
And that's what bursts became. And then, hey, we have amazing infrastructure now. We can work with global teams 24/7/365. Why are we forcing people to stay in a location? The reality is the 98 thing is mostly because of a tax thing, but ultimately, we have the infrastructure that people can just log in from wherever. And so why not lean into.

Lenny (22:44):
Yeah. This is really interesting. I love that your answer to how to work remotely better is get together more often, which I hear a lot from companies, but I love that you've built this infrastructure to enable it. I'd love to hear a bit more of how this product works. Is it all in-house? Any advice I guess, for anyone trying to build something like this?

Brandon Chu (23:01):
I hate saying that it is all in-house because that is not easy, really accessible for midsize or below companies, but basically, you initiate an event called the burst. You can choose what type of thing you're trying to do, whether it's a pure work thing or you want to have a little bit of activity and social aspects of it. There's different locations, depending on how many people are going that are available to you. There's a booking system. If you choose to do something a little more low key and just meet in, let's say a major city, then we actually allow you to access our old offices. So the leases didn't go away. So we had to use these offices for something and these offices have now completely been retrofitted. They're beautiful. And they are amazing. I wouldn't even say co-working spaces. They're just community spaces now that you go in and you can use them and you have everything. There's food there. There used to be there's board rooms and whatever you want to have your little offsite or whatever it may be.

(24:01):
And then there's a rating system after. How is the burst there? There's a whole team that manages the logistics of all these things. So that it's very just like we don't have managers all over the company trying to figure out flight plans and stuff like that. And yeah. It's great. And we also get the data to be able to see, hey, what teams haven't been together in a very long time? And ask the lead, "Hey. Why is that? Is it because everything's good and people are busy? Maybe something about a baby or something like that and they can't get around." Or is it a prompt that, "Hey, maybe your energy is low as a team, it's time to get together." So that's the benefit I think of having built that app and that infrastructure is that we get to really understand how it's actually helping.

Lenny (24:42):
This episode is brought to you by PostHog. PostHog offers a suite of product analysis tools, including funnels, heat maps, session recording and experimentation all in one easy to use platform. PostHog is open sourced so you can host it on your own infrastructure, which means that you have control over who has access to your data and makes regulatory compliance a breeze because you don't need to send user info to third parties. PostHog's app system works seamlessly with your data warehouse, both for importing and exporting data, which enables you to bring your data into one place and easily understand user behavior across a range of touchpoints. If you'd like to learn more, check them out at posthog.com/lenny. Just one last technical question about this product because it's so cool. Is there an API that just books flights or does it just send you to kayak and you book these flights?

Brandon Chu (25:31):
I don't know the exact answer, but I would imagine. So we also use trip actions inside of Shopify and I'm pretty sure they have an API, so probably we've done something directly with them. So they've handled all the really complex stuff, but we probably use them for the booking action itself.

Lenny (25:47):
Okay. Sweet. This is super interesting. I've never heard of this. I want to transition to talk a little bit about your writing. So your writing is how I originally discovered you. It's on the top, I don't know, 1% of most useful, actionable, interesting writing on the Kraft Food product management. I still refer to it often and share it with people all the time and it says a lot, because it's a little older at this point and you've kind of slowed down the writing. I'm curious when you were in that writing phase, a lot of people want to write, a lot of people know that it's good for many reasons, but a lot of people don't do it. What would you say worked well for you when you were in that period to get you to actually get stuff written and also just create time for writing?

Brandon Chu (26:27):
Yeah. Well, first of all, thank you. That's super generous. I think if you say I'm in the top 1%, then Lenny, you're definitely in the top 0.1 or 0.01% and so kudos to you.

Lenny (26:27):
I aspire to be you.

Brandon Chu (26:41):
And also thank you for being generous saying I've slowed down a bit. The reality is I haven't written anything since 2018. So when I reflect on it, I think I wrote those in a time where I was figuring out a lot of stuff while I was executing. And I wanted to crystallize in my mind some mental models and frameworks that had been forming somewhat intuitively. The funny thing about those posts when I reflect on them and I've rarely reread them, but every once in a while, someone shares an excerpt and I end up kind of rereading and be like, "Do I even believe this still?" But when people read them, they think like, "Oh, they're learning from someone who's figured it out for a while and now they're sharing it later in their career or something."

(27:21):
But the reality is, and maybe this resonates with you. It's like I figured out everything in those posts at the exact moment I wrote them. It was the writing process itself that actually allowed me to solidify those mental models and those frameworks in my mind. And so I wasn't ahead of the game in any way. It was just I think I really wanted to disambiguate the chaos in my mind about what my job was. And it took me to really interesting places. And I think it was also coupled with two things, which was I had a really good career trajectory at the same time so I could actually observe. I wasn't too mired in being a PM one for five years and then moving. I was moving through things really quickly so I was able to contrast things because it was literally like, "Oh wait, three months ago, it was that. Now, how do I change?"

(28:03):
And that, of course, is not just me, but it's also at Shopify I grew so much during that time. Right? We grew seven years ago. I came at just under 500 people. Were over 12,000 people today. And so it was a really formative time for the whole company and definitely myself. And in terms of just writing well and shipping quality posts and stuff like that, I'm sure this resonates with you. You just got to put in the work. You got to put in a lot of hours. I put 40 hours into a post, do it on the weekends or I brain dumped a first draft of it in two hours and drew 38 hours of editing or getting feedback from people or drawing some diagrams that I put in there. But it was that process.

(28:44):
And I think it was such an amazing thing to learn how to do is to just sit and write for five hours and reread the thing and actually also get feedback from people. Don't be so afraid to share raw, early thoughts and for it to not make sense but then when you give to someone objective and they read it, they'll be like, you really learn things about how you put a narrative together in your mind versus how someone actually reacts to it. And so that fearlessness to get a lot of feedback, I think, was something I developed through those years.

Lenny (29:14):
Everything you said 100% resonates with my approach. There's a quote I often think about. It might be Hemingway or might be misattributed to Hemingway that "I don't know what I think until I've written it down." And that's exactly how I feel like it's a forcing function to help you actually figure out something. And that's exactly how I started.

Brandon Chu (29:33):
And it's a release too, because when you write it down, you just kind of release it from your mind. It's not floating around there because I'm scared to lose it or something like that. And you kind of just now you cleared your mind and you can actually think. You build on top of that knowledge into something else.

Lenny (29:48):
That's exactly how I felt when I first started writing. I just want to get these things out of my head before I forget them partly to help crystallize something that I can actually hold onto that won't fade away.

Brandon Chu (29:57):
Okay. How many posts have you written now?

Lenny (29:59):
I think probably 300.

Brandon Chu (30:01):
300. How are you still motivated to, or where do you even find things to write about now?

Lenny (30:07):
So I have a endless list of things I want to write about. And partly, these ideas come from founders and PMs that are constantly sending me questions that they have. And the way I see it is until nobody has any more questions to ask about starting a company, building a product, driving growth, I'm going to have things to write about.

Brandon Chu (30:27):
That's amazing.

Lenny (30:28):
And it feels like that's an endless supply. The bigger challenges, it gets harder and harder because the easier stuff is getting knocked out. And so that's the bigger challenges. Things remaining are things that take more time, more research, more digging, things like that. But at this point, yeah, I've been doing it for over three years and still got plenty of ideas.

Brandon Chu (30:48):
[inaudible 00:30:48].

Lenny (30:47):
And there's no better motivator than somebody paying you for your content and [inaudible 00:30:51].

Brandon Chu (30:51):
Well, it's a symbiotic relationship.Right? All those questions and feedback from your subscribers and whatnot is fodder for the next thing that you're going to give. And I think that's an amazing relationship.

Lenny (31:02):
That's exactly right. I wanted to ask you, do you think every PM/leader should spend time writing? Who should? Who shouldn't? What are you feeling on that?

Brandon Chu (31:10):
I think yes. Even if it's not to be publicly shared or whatnot, I think ultimately, especially in a increasingly digital world and increasingly remote world, you've got to be able to articulate yourself. Again, even going back to that process of writing and what it does for how you understand what you're saying, you owe your team, your peers, your stakeholders that level of clarity. So even if you write it and throw away, you've created a clarity in your mind and you can articulate it as such and people deserve that. And I think that if you're going to be a really good PM, you have to have that skill.

Lenny (31:45):
What impact have you seen as a result of your writing that you've done?

Brandon Chu (31:49):
Oh, it's honestly been the most important thing I've ever done in my career unbelievably. And it's had probably two really interesting effects. One is that as Shopify grew and when we were going through hyperscale, you probably recognize this from your Airbnb days as well but people are falling from the sky. Every day there's 20 new people showing up and you having been there already, now you got to figure out what all these people are doing and give them all the context and all these types of things. And how do you even teach them the culture and the ways that you work and stuff like this. And so one amazing, and just the context, I'm really old at Shopify now. I'm like 99.1% tenure. So I'm ancient at the company.

Lenny (32:30):
Is there a stat that shows up? Is there a little dashboard?

Brandon Chu (32:32):
There is in our little internal wiki thing.

Lenny (32:35):
[inaudible 00:32:35].

Brandon Chu (32:34):
So I'm literally ancient in the company. And so one of the amazing effects that the writing had was that people that would join my team already knew how I thought. It was pretty onboarded a lot of the PMs that would join my team because obviously, they're going to look for who their leads is and Google that a bit and they see a posting and be like, "Is this person legit or not or whatever?" And so I didn't really even have to onboard many people in so many ways. They kind of knew how I thought about the world. And also, even when I was in Shopify and writing those posts, there's so much noise in Shopify. It's a very chaotic place. There's so many exciting things happening that it is very hard to tell a 200 person PM org, "Stop. Pay attention to this idea."

(33:20):
So I actually found that writing externally and getting momentum externally was a better way to influence internally what was happening, to the effect that Tobi would read my post here and there and he'd be like, "Great post." And I'd be like, "Hey, daddy loves me." But no, but seriously, it would help build my trust battery with Tobi because of the way that those posts gain traction and whatnot. So it has had an incredible, incredible impact on my personal career. And also I think it has brought a lot of really great people to Shopify. Literally every week a new PM messages me and says like, "Hey. I just joined. Your post had a lot of influence on me or whatever. And I'd love to meet up and blah, blah, blah." But that has been amazing and it's so rewarding. Another small example, this wasn't in the black box, product management like general cannon or whatever per se, but I was working on the integration product with Facebook Messenger via Shopify.

(34:16):
And as part of our launch, I wrote just to get more, because we're a very small company than them. So we're using any angle we can. So I'm writing on my personal blog about this thing that we launched and David Marcus, who's now leading their blockchain crypto stuff, but he was CEO of PayPal for a while. And then he came in to lead all the Facebook's payment stuff and Messenger. Oh, sorry. Kind of lead Messenger. Anyway, he shared it on his Facebook and on Twitter. And then that blew up and all of a sudden, the CPO of Shopify, Craig or whatever, now starts thinking I'm legit even though... Because someone of his caliber was also sharing these things, about a product that we built and whatnot. So it was just really interesting how these little things had an impact on how people perceive you and thus how much impact and momentum you can create inside a company.

Lenny (35:08):
If you think about it, say you spend 40 hours on that post, what are or why that is spending a week or two writing something and the impact that could have on your perception within the company on your future career opportunities and even just people joining the company and that are going to work for you. They're like, "Oh my God, I'm going to work for Brandon Chu. I'm so excited."

Brandon Chu (35:28):
I'd say even if it never got picked up, the ROI is already huge because it just again helps you refine how you talk about the work and the decisions, but that aside, it accelerated my career probably a decade.

Lenny (35:41):
That's a really good point. You should not be focused on this needs to go viral for this to be worth the time because I find that the more you think about that, the less well it does because that becomes the wrong intent.

Brandon Chu (35:52):
Yeah. Well, to be perfectly transparent about it, it is a factor in why I stopped writing. It had gained so much traction and I had become an exec now at Shopify and I was so busy at them. I was like, "I don't have the time to make this thing as good as it was. And I'm not even going to put another post out because I don't want to disappoint people." That's a real thing. I think you're probably better conditioned with this having written 300 posts now. I think you're a machine, but for me, it was like, I would put one every couple months maximum or something like that. And so when I lost the time, I had kids and all these types of things, it seemed insurmountable to prioritize.

Lenny (36:31):
I wanted to ask, what's your favorite thing that you've written? Which piece is your favorite?

Brandon Chu (36:36):
I don't know if I have a favorite, but the one that always I'd say has overall had the most traction or just constantly, even to today, people still tweet about or message me, whatever, was the one about making good decisions as a PM. Basically, the short of it is, the first thing it argues is that the most important thing to figure out when you're dealing with any decision is actually figuring out how important that decision is. Since we're faced with hundreds of decisions in any given moment around the product or whatever, and that we're only human and we can only prioritize a few, you got to figure out the importance of them so you can prioritize. And so it talks about things like either decision reversible or not. Does it affect a lot of users in a material way or not, stuff like that, ways to prioritize them basically.

(37:22):
And then it kind of argues that okay, given the fact that we only have limited time and that the most important decisions are so much more important than the other 98, 99 of them, you should basically spend all your time on those very few important decisions. And for all other decisions, you should just literally just go with whatever your gut is or delegate it because you're only human and your gut is going to be right a decent amount of time too. And so just make those fast so that you can keep the team velocity high. You don't ever want to be a blocker, that's the other tension and then spend all your time on these few critical decisions.

Lenny (38:00):
Would you say that's still generally the way you work looking back at that post?

Brandon Chu (38:04):
Yeah. Definitely is still the way I work. I probably do it too much in terms of me doing my job here and there.

Lenny (38:09):
Awesome.

Brandon Chu (38:11):
It's like, "Oh, that isn't important." If you take overtime too, you get weathered down about what's actually super dire versus not. And once you've had a few battle scars of things that you thought were going to ruin everything, your career, your reputation, blah, blah, blah, and then actually nothing happened, you just start to raise the bar about what's actually important.

Lenny (38:31):
I love it. We're definitely going to link to that in the description for this episode. Is there a post that you wish you had written or want to write if you have the time?

Brandon Chu (38:39):
I've been wanting to write literally for three years. It'll probably be really long, but just a huge post about being a platform PM as opposed to product PM. And there's so many interesting differences in the ways that you have to think about prioritization. And I even told a story about it's a big cultural change too, that you have to affect people way beyond your team. Now you have to also work and you have to tell us to work multiparties. So you're building a, let's say a developer platform that they're building apps. Okay. Now there's multiple stakeholders. So the developers building these apps that are going to be consumed by these businesses, these merchants, and these apps also may be presented to end buyers. There's now three constituents and there's all these crazy things around policy, data sharing, just tension between which side gets economically rewarded for doing what. There's a lot of really interesting things.

(39:33):
And so one day I hope to write something about that and that's even on just the pure strategy and kind of economic view of it. But then there's also a super fascinating product design and engineering problems of just like, okay, you have this web app or whatever, and you want apps to exist in it. Well, how are they going to exist in it? Right? Okay. Are you just going to let them put their link in there and then it opens up a new tab into that other product that's kind of lame? That's basically a Facebook comment of a link, or are you going to allow the actual third party product to exist inside of your product and how are you going to do that? Is it going to be an eye frame? Well, that's kind of janky.

(40:11):
If it's going to be deeper, then now we're talking about direct data integration. We're talking about maybe your app serving UI on behalf of that app, but then some of the data comes from the third party server and it gets really, really interesting in terms of user experience and whatnot and it's actually quite common in our life that we don't think about it.

(40:29):
So when you long press on an app on your iPhone and it has a shortcut list of things you could do quicker. Right? Okay. Say if you long press your email app, it'll probably say create new email as one of them. That's an extension. That's iOS saying, "Hey, Gmail app. I'm going to give you the ability to actually deep link this experience into your app through our operating system." Right? Someone actually had to design that idea, that user experience and we just take it for granted because that's how it works. Right? But there's so many crazy decisions there about, well, if you go too far, you give Google too much control there and they could do some really messed up stuff. Or if you don't go far enough, then it's really just lame. It's not actually powerful. And so it's a really interesting domain.

Lenny (41:18):
I'm glad you touched on this because this is exactly where I wanted to go next.

Brandon Chu (41:21):
Cool.

Lenny (41:22):
I want to chat about the PM career track, but maybe before we get into that, I know you haven't written this post, but for someone that's designing a platform or an ecosystem, is there any kind of just guiding frameworks or rules of thumb that you've come to to help you make some of these decisions that you talked about?

Brandon Chu (41:39):
I actually say the first thing is as a PM, your psychology has to really change around your own validation. So usually, you can build a product, ship it, customers tell you if it's good or not. The cycles for platform work are five to 10 odd times longer. You're maybe changing something on the infrastructure level, then opening up an API and then doing an alpha period for the API where developers now build on that and test things. And then you move into a beta. And then finally, two years later, some end customer actually uses that app, right, for this. And you're not designing actually the end user's experience. You're designing a canvas for developers to build their own creative ideas on. And it's just a very different type of work. And so I would say that's the first thing psychologically is be prepared for those much longer cycles.

(42:29):
Surround yourself with people on your teams that find ways to enjoy that process and also find ways to celebrate rewards along the way like we would, not rewards, but celebrate shipping things along the way. When that API went into alpha, there's no press release, but how do you make the team feel amazing about that work? Right? You have to tell the big narrative about this is going to change how merchants actually get different apps in these areas or whatnot. And here's some of the crazy things that we're seeing in the early adoption, et cetera. So that's my main thing on psychology. I'd say in terms of preparing yourself, you really have to think about before you even get into the technical or design execution of any particular platform area, really think about the principles behind the platform that you're building. So an example, and then a contrast with Shopify's, in Amazon's platform, I'm making this up, but I assume that a pretty big important intro principle is that if there's ever a toss up between deciding between the seller and the buyer, the consumer, we're going to decide with the consumer. Right?

(43:40):
That's why every time you refund something on Amazon, anytime you got a complaint, send you another one. Right? They made that trade off to be a consumer focused platform and obviously, that's been amazing for them, but you also hear the contrasting stories of sellers that are really pissed off Amazon that have ruined their businesses and whatnot. So not to hate on that, but that's a second order effect of that decision. In Shopify's case, we are here to support entrepreneurs and businesses in making their dreams come true and creating independence. And that is sometimes at the cost of developers on our platform. And so sometimes we may make a data policy change saying, "Hey. It's more important that the merchant has access to this data across apps. And it's important that actually you push that data back in Shopify so that you don't hold that data back so that this other app can't use it."

(44:33):
And now we're sending the same end customer two marketing texts when they've already opted out of marketing texts or something like that. And so this is where you have to understand those principles and the stack rank of the constituents there to be able to make good policy and design choices. And I think it's something that if you're not conscious of early as a platform PM, you will blow up some stuff or there will be some bad instances that come up or you'll get blocked by the CEO or whatever on the day before it launches, which has happened to me.

Lenny (45:07):
Oh, no. This sounds like a very hard place to be in an organization, building a platform, building an ecosystem like this. You went into the platform world pretty early when you got to Shopify. And I know a lot of PMs think about, "Should I go platform? Should I go user facing product?" Do you have any advice for folks that are trying to decide which path to take? And is it even a one way door? Is it easy to go to a different direction later?

Brandon Chu (45:32):
That's a really tough question. I think if you have any particular interest in the types of problems that you solve, I'd give you a little snapshot of the things you think about as a platform PM. If that stuff gets you really interested, then follow that guy. I don't think it's either, or I don't think one is better than the other. I think they're completely different types of problem domains. I don't think it's also a one way door. I'd say even if you do primarily user facing or consumer facing side of the product, you're going to be consuming things on some platform somewhere, whether it's an internal API or a third party or whatnot. So you're going to experience platforms good and bad. Right? And so you'll learn about it. And then alternatively on the platform side, you're going to be designing the canvas and you're going to see what gets built there and you're going to learn what are good and bad bounds of not a single user experience, but a universe of user experiences that are possible.

(46:26):
If you create a UI kit or something like that, you're going to see the good and the bad that comes out of that UI kit being given to the third party ecosystem and you'll learn about consumer. And so I also think oscillating between them is an amazing experience too, because there are really long cycles and platform work. And sometimes it's nice to ship and iterate and grow week over week and talk to your users about every single feature that you're shipping every other week. And that's so fun in different ways. And so I think having both is actually the right goal in both experiences.

Lenny (47:00):
To zoom out a little bit and as a final question, if you could suggest just one thing for PMs to do to help them level up in their career and just do better, what would that be?

Brandon Chu (47:13):
Everyone has so many different backgrounds, but I'd say overall, based on most PMs that I've met, I'd say, look, it is hard to do when you are a PM somewhere, but do a legitimate side hustle, found a company on the side and learn everything else. Because I think sometimes you're in this silo of your feature, your area or whatnot. And you forget what it means to sell something to a customer, what it means to support a product, what it means to ship something and get destroyed because it doesn't even work or something like that. And so I think it humbles you a bit. It reminds you of how hard it is to build software and how many people it takes to do that well. And especially if you're not in technical, really lean into it and build something simple, learn how to build something simple for yourself, demystify the technology.

(48:03):
That experience will take you far. I love telling people that literally don't even know what HTML is or something like that, which I was one of those people that from right now over the weekend, you could build a clone of Twitter using a tutorial on Rails or something like that. You can do it. You may not know everything that's actually happening, right? But you could actually get that deployed and it'll work and it'll blow your mind that you did that. And I think once people break through that wall, when they're nontechnical, I think the momentum builds from there and so the side hustle and then also break technical walls or obscurity is what I would recommend.

Lenny (48:43):
Awesome. I love that advice. It's kind of like a microcosm of create your own little business and do all the things and break out of your little box that you're in. Maybe as a PM, where can folks find you online and how can listeners be useful to you?

Brandon Chu (48:55):
You can find me online, I guess, on Twitter @BrandonMChu and be useful to me. The simplest answer for me, I guess is I'm a pretty active angel investor. I've invested in 60 companies over the last five, six years. So if you're interested in an occasionally helpful angel investor, then hit me up. We may be a little bit too busy, but really the honest answer, I don't need anything. I think if anyone's listening and they want to help me out, just go help some stranger in the world that needs it. I'd rather you do that. I think I've been so lucky in life that I don't want anything.

Lenny (49:28):
Awesome. Thank you so much, Brandon.

Brandon Chu (49:29):
Thanks, Lenny. It's been a blast.

Lenny (49:33):
That was awesome. Thank you for listening. If you enjoy the chat, don't forget to subscribe to the podcast. You could also learn more at lennyspodcast.com. I'll see you in the next episode.

