---
guest: Matt MacInnis
title: '"I deliberately understaff every project" | Leadership lessons from Rippling''s
  $16B journey'
youtube_url: https://www.youtube.com/watch?v=O_W76LR77Vw
video_id: O_W76LR77Vw
description: Matt MacInnis is the chief product officer and former longtime COO at
  Rippling, a unified workforce management platform valued at over $16 billion.
duration_seconds: 5777.0
duration: '1:36:17'
view_count: 28828
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- churn
- metrics
- experimentation
- analytics
- funnel
- revenue
- hiring
- culture
- leadership
- management
- strategy
- vision
---

# "I deliberately understaff every project" | Leadership lessons from Rippling's $16B journey

## Transcript

Matt MacInnis (00:00:00):
It is really important to me that we feel that we've deliberately understaffed every project at the company. If you overstaff, you get politics, you get people working on things that are further down the priority list than necessary. That is poison. It's wasteful. It slows you down. It creates cruft.

Lenny Rachitsky (00:00:15):
You've been a long time COO at Rippling. Recently, you moved into CPO, Chief Product Officer at Rippling. Something you talk a lot about is that extraordinary results require extraordinary efforts.

Matt MacInnis (00:00:26):
If you want to be in the 99th percentile in terms of outcomes, it's going to be really difficult. You got to sort of remind people that if they ever find themselves in the comfort zone at work, they are definitely making a mistake. It's supposed to be really fricking exhausting.

Lenny Rachitsky (00:00:40):
You're a big fan of escalating issues.

Matt MacInnis (00:00:41):
Fundamentally, the most selfish thing you can do is withhold feedback from someone. When you think a thought that would help someone improve and you avoid giving it to them because it would make you uncomfortable. Well, you're optimizing for your own comfort, and it's fundamentally selfish. So many people have teams that are not functioning incredibly well. Teams will always optimize for local comfort over company outcomes. The purest form of ambition and most intense source of energy in the business is the founder CEO. Every next concentric circle of management beyond the founder CEO has the potential to be an order of magnitude drop off in intensity. That is fucking dangerous.

(00:01:17):
As an executive, as a leader, your job is to preserve that intensity at its highest possible level. You've had a couple really interesting experiences with your own startup. We talk in Silicon Valley about never quit, but that is complete absolute venture capital.

Lenny Rachitsky (00:01:33):
Today, my guest is Matt MacInnis, Chief Product Officer and formerly longtime Chief Operating Officer at Rippling. If you don't know much about Rippling, it's a massively successful business last valued at over $16 billion. They have over 5,000 employees, and Matt has been instrumental to that success. He's also got a really rare combination of brutal honesty, a ton of experience building a very complex and very successful business, and being able to clearly articulate what he has learned really well. Matt shared a lot of insights and advice that I've not heard anyone else on this podcast share, and I left this conversation feeling that every leader needs to hear his advice.

(00:02:12):
A huge thank you to Albert Scrashim and Sunil Raman for suggesting topics and questions for this conversation. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It helps tremendously. And if you become an annual subscriber of my newsletter, you get a year free of 19 incredible products, an entire year of Lovable, Replit, Bolt, Gamma, Inata, Linear, Devin, PostHog, Superhuman, descript, Whisperful, Perplexity, warp, granola, Magic Patterns, Raycast, ChatPARD, Mobbin, and Stripe Atlas. Head on over to Lenny'snewsletter.com and click product pass. With that, I bring you Matt MacInnis after a short word from our sponsors.

Amar (00:02:48):
This podcast is sponsored by Google. Hey folks, I'm Amar, product and design lead at Google DeepMind. Have you ever wanted to build an app for yourself, your friends, or finally launch that side project you've been dreaming about? Now you can bring any idea to life, no coding background required with Gemini three in Google AI Studio. It's called vibe coding and we're making it dead simple. Just describe your app and Gemini will wire up the right models for you so you can focus on your creative vision. Head to ai.studio/build to create your first app.

Lenny Rachitsky (00:03:18):
This episode is brought to you by Datadog, now home to Eppo, the leading experimentation and feature flagging platform. Product managers at the world's best companies use Datadog, the same platform their engineers rely on every day to connect product insights to product issues like bugs, UX friction, and business impact. It starts with product analytics where PMs can watch replays, review funnels, dive into retention and explore their growth metrics. Where other tools stop, Datadog goes even further. It helps you actually diagnose the impact of funnel drop-offs and bugs and UX friction. Once you know where to focus, experiments prove what works.

(00:03:56):
I saw this firsthand when I was at Airbnb where our experimentation platform was critical for analyzing what worked and where things went wrong. And the same team that built experimentation at Airbnb built Eppo. Datadog then lets you go beyond the numbers with session replay. Watch exactly how users interact with heat maps and scroll maps to truly understand their behavior. And all of this is powered by feature flags that are tied to real-time data so that you can roll out safely, target precisely and learn continuously. Datadog is more than engineering metrics. It's where great product teams learn faster, fix smarter, and ship with confidence. Request a demo at datadoghq.com/lenny. That's datadoghq.com/lenny.

(00:04:43):
Matt, thank you so much for being here and welcome to the podcast. Thank you for having me. I want to start with something that I know is really important to you, something you talk a lot about that I don't think people hear enough on podcasts like this, which is that extraordinary results require extraordinary efforts. Talk about why this is so important, what you think people need to hear.

Matt MacInnis (00:05:04):
This is a term, that phrasing I actually attribute to a friend of mine, Dan Gill, who's the chief product officer at Carvana, which as a company also doesn't get enough credit for how much of a tech company it actually is. Super interesting. And I think as a general framework for me, and a lot of what I say with you today is not really specific to product in any way. We should actually talk about that. It's like the product function is an instantiation of the general concept of management. Being a chief product officer is not that different from being a chief whatever officer. You have to apply the same frameworks and concepts to get people to achieve goals together. But one thing that is absolutely universal that I think we, honestly, I think we forget it in Silicon Valley or a lot of people don't sort of internalize it, is that if you want to accomplish something truly extraordinary, if you want to be in the 99th percentile in terms of outcomes, it's going to be really difficult.

(00:05:56):
It's going to be really uncomfortable. And you got to sort of remind people of that, that if they ever find themselves in the comfort zone at work, they are definitely making a mistake. They have definitely screwed up somehow. It's not that an extraordinary effort is sufficient to an extraordinary outcome, but it is 100% true that it is necessary. And so I do use that framework as a sort of guiding principle in my own leadership.

Lenny Rachitsky (00:06:23):
To make this even more real for people, what are examples of moments that were extraordinarily hard?

Matt MacInnis (00:06:29):
It is not about any sort of grand single story. I think the story is actually told through a thousand little things. And so for me, the story is told through a thousand Jira tickets, not through a thousand grand events. The extraordinary effort thing is a reminder that it's supposed to be really fricking exhausting. It's supposed to be. So on Friday night, when you get hit with an escalation on Friday night, when you get sort of hit with a bunch of new bugs from someone in the engineering team that you've got a triage, those are the moments where great players and great teams are separated from good players and good teams. And it's so easy to say this at a company like Rippling because we're winning. As a company, for all of our foibles, and we should spend time today talking about where things are not perfect and not great, but the growth rate of the company on the revenue foundation that we have is extraordinary, really, really compelling.

(00:07:33):
And it gives you, as a leader, the air cover to get up in front of your team and say, "Hey guys, I need the last ounce of oil that you've got left." And if your company's not growing very quickly, if things aren't that great, if your growth rate is 30% or 40%, it doesn't feel as good as a contributor in that business to lean in and give everything you've got on Friday or Saturday or Sunday because you don't know that it's going to yield much. And so extraordinary results, outcomes demand extraordinary efforts, but if there's no chance at an extraordinary outcome, it's very hard to get the extraordinary effort. And so I like to remind people at Rippling at least that it's so rare to have the opportunity to be able to be a part of a team where the extraordinary effort that you do put in on Friday or whatever, whenever it is actually contributing to an extraordinary result.

(00:08:27):
It's a very special and rare thing, and it gives me a superpower as a leader because I can lean on that when I'm ringing the oil out of somebody who's in the bored and tired zone.

Lenny Rachitsky (00:08:38):
I saw the same thing actually at Airbnb with Brian Chesky. It always felt like things were going great and maybe we could take a break after something we shipped was killing it. And it always felt like the opposite. It always felt like, how do we press the gas pedal further? How do we go faster? How do we go bigger? There's never a moment to take a break.

Matt MacInnis (00:08:57):
I spent seven years at Apple and learned under Steve Jobs when he was the CEO, learned what we called the death march, which is what we did to the engineers. It was like as soon as you shipped one version of the iPhone, you were just immediately thrown into the pit of building the next one and there was no break. It was just relentless and talk about an extraordinary outcome at the end of the day. There is no relief. In a competitive market, and if the market is valuable, it's competitive, no question. If you leave anything on the field, if you sort of leave a crack for your competitor, 100% chance they're going to go fill that crack. And so you have to be relentless. There can be no relaxation of the organization. It doesn't mean people can't come and go or people can't take vacations or live their lives, of course.

(00:09:48):
And it's not like people are human beings. You can't grind the individuals down, but the team as a collective group of people has to be sort of on the ball all the time. There can't be a break. And if you leave one, you're just begging for the slightly more hungry competitor to come in and eat your lunch. And that's the beauty of capitalism.

Lenny Rachitsky (00:10:12):
Also, very counterintuitively, and maybe the more optimistic perspective here is when you do give your team space to just twiddle their thumbs, bad things start to happen. Morale actually dips in my experience. People get distracted. They're like, "Oh, what are we even doing? It's not interesting." I find that keeping people busy and motivated and fired up, even though you may think they'll be happier taking a many week break and slowing things down, I find they get more, the more I actually goes down in those moments.

Matt MacInnis (00:10:44):
So here's a management framework that I use fairly often. As an executive, you don't know how to get any decision exactly right. It's not knowable. You don't know how much budget to allocate. You don't know how many people to put on a project. You don't know how to set a deadline for when you're going to ship something. But of course, you have to set some default so you make your best guess and then you manage to that best guess and you learn as you go because in software development and in business in general, everything's emergent. These are not things that are knowable top down or a priority. And so you take a best guess and knowing that you're not going to get the right answer, you need to decide whether over-steering or under-steering relative to your perceived midpoint is better. And so let's talk about staffing. When you staff a project, is it better to overstaff or is it better to under-staff knowing that you can't get it right? Well, it's better to under-staff. If you overstaff, you get everything that you just said. You get politics, you get people working, I think most importantly on things that are further down the priority list than necessary. You have like 20 things on a stack rank list and you know that you got to do the top five, but the next 15 data's kind of ambiguous, but you've overstaffed the project. So the next 10 things down are getting worked on. Before you even know if they're necessary, that is poison. It's wasteful, it slows you down, it creates crust. And so it's very clear that under-staffing is less evil than over-staffing. In this particular framework, the advice is under-staff deliberately, always. And then the wisdom, the wisdom element is to know not to under-under-staff and sort of knowing the difference between those two things.

(00:12:22):
And so that's the way we work at Rippling. Everyone is constantly asking for more resources and of course where we can afford to and where it's appropriate new resources arrive, but it is really important to me that we feel that we've deliberately understaffed every project at the company.

Lenny Rachitsky (00:12:39):
There's a previous guest, I forget who this was. They used this metaphor if they want their team to be dehydrated to always be wanting more water. And then eventually they're too dehydrated and okay, we needed someone to help. Interesting. Yeah. There's a line along the lines of extraordinary efforts I want to make sure I read because I think this is really good. This may be a way to summarize what you're saying, that good teams get tired and that's when great teams kick the good team's asses.

Matt MacInnis (00:13:04):
Yes. This was a quote actually from Sunil, and he found it from a women's basketball team coach. And it is, to my point earlier about you got to run the engine at the red line at all times because the minute you let your guard down, the minute you slow down, the minute you relax, the minute you leave a crack for your competition, the great teams are going to come in and kick the good team's. And it's like sports, I'm not a very sporty guy, but sports analogies are sort of irresistible because at the end of the day, business is a game and none of this matters. We're not going to carry it to the grave. It's like you're here to do this stuff because it somehow fulfills you while you're on the planet. And I love the sport of business and I find that sports, notwithstanding the fact that I watched very little of it, that military, those are very ripe sources of parallel concepts to apply in leadership.

Lenny Rachitsky (00:13:56):
I find also those most intense, stressful, long nights are the moments you remember most and remember most fondly back to when you're building something. The key though is that it has to go well. As you said, if you are succeeding and winning, all of this is romantic in the end and nostalgic. Remember that time we built this thing and worked late nights and shipped this thing? If it doesn't go anywhere, you don't feel that. So I think that's a really important component of this is you need to be winning and succeeding.

Matt MacInnis (00:14:23):
One thing that I've learned from Parker, Parker's our CEO at Rippling, he said, "You don't really learn from your mistakes, you learn from your successes." And it's like you do, of course, and he would admit you learn a bit from mistakes, but I do think that this is sort of feel good that it's like, "Well, you didn't succeed, but at least you learned something." I've had failures. When I look back at the nine years I spent working on inkling from day one in 2009 until we sold that business to a private equity firm in 2018, up the curve of Silicon Valley coolness, back down the other side into obscurity. Of course, I learned and grew a ton during that time, but in now what I think is six or seven years, I'm trying to do the math, seven years coming up on at Rippling, I've learned so much more because I've seen success.

(00:15:13):
I've seen rapid, wild, crazy off the charts success of the business and it's more informative. There's more to glean from seeing how it's done right than there is to glean from seeing how it's done wrong. If I tell you you're going to get on an airplane and one maintenance technician has seen it done right a hundred times and the other maintenance technician has seen it done wrong a hundred times, but he learned from his mistakes, but still hasn't had any success himself. I mean, give me a break. There's not even a comparison which plane you're going to feel more comfortable on. And so I do think that learning from your mistakes thing is a bit of a feel good trope that actually has very little substance in reality. And it's why as an early career product manager, or it's why frankly at any stage of your career when you want to learn, you should join a winning team.

(00:15:57):
It's cool to go and start a company at 22. Good luck to you. The odds are not in your favor, but the folks who, when I look at a resume and I see that someone's joined, they were at really good companies when those companies were super exciting and in crazy growth mode. I'm like, "I instantly want to interview that candidate because I want to hear what they learned from being part of a winning team." And that's sort of one of my go to heuristics when I'm looking at candidate profiles and I think it's an under-told trope. Sorry, not an under-told trope. It's a piece of advice that I don't think people embrace enough in the valley that success begets success and you should chase success.

Lenny Rachitsky (00:16:35):
Speaking of success and learning, you've been a long time COO at Rippling and the reason you're here recently you moved into CPO, chief product officer at Rippling, which is very exciting and very rare. I don't see a lot of COOs moving into product. Let me ask you why did you move into that role? I feel like you've been killing it at COO. Maybe that's the reason. Be careful what you're good at. And also just what are some surprises about this, about moving into product? Because a lot of people imagine what it's like and then you're actually doing it.

Matt MacInnis (00:17:08):
The story at Rippling is pretty interesting and I'll tell it because I think it explains why I'm making this transition, but this isn't really about me. I think it's sort of a pattern that your listeners would find useful. In general, your best executives are the ones that you can mostly toss into any challenge and they will bring order to chaos. They will fix the thing. And I do appreciate the terms that people have used at Rippling for me, talking about MacInnis's injured birds, where at any given moment some function is in disarray or in jeopardy and I go and focus very carefully on that function to get it back in order batting 800 maybe, like not always wild success, but I did that everywhere except R&D. I would think about helping out with components of the sales organization like our channel team, or I spent time building out the recruiting function a few times when it needed to be sort of rethought in response to our growth, but it never R&D.

(00:18:23):
And so I would have my feet up on the table looking out across the floor at this dumpster fire off in the distance, just sort of emitting smoke and wondering if someone was going to go in and deal with that. And the smoke takes various forms and when you're growing as quickly as rippling is growing, it's not always something that necessarily even impacts customers, but it's the sort of thing where you're like, that architecture's not right or they're not measuring adoption correctly." From the outside, I actually had quite a few criticisms that I could lob in. And what happened at Rippling was we made some hiring mistakes. I think the folks that we had in those roles would agree that they weren't the right people. We had a hiring mistake in engineering leadership where the product leader at the time had to sort of run engineering.

(00:19:07):
We subsequently had a mistake in product hiring and a lot of us had to sort of pitch in. And Parker and I sort of stared at each other through two years of this kind of disarray or this chaos or this agony of things and just never really having good executive leadership over both engineering and product at the same time. And I remember Parker sort of slumped down in his seat and said, "Oh, I have to run another search." And I said, "No, the gig's up. I'm going to go do it." And he really sprung up in his seat. He's like, "Really? You'll go do that?" I'm like, "Dude, this is what the business needs." And so that's what I did. And that really started about a year ago in sort of, I realized I was going to do it and expressed that to Parker in December. I really took it on in January of '25.

(00:19:51):
And so it's been 11 months of learning. Jumping into the product role when the product function itself, although staffed with really talented people, wildly under understaffed, and without a single spiritual leader on top of it to drive consistency and process excellence had become locally optimized but globally incoherent. And if you know Conway's law, you are destined to ship your org chart. And so with a locally optimized, globally incoherent team, you had a locally optimized, globally incoherent product experience that needed to be resolved. And so my efforts over the last 11 months have been to establish greater clarity in terms of how we do things around here, better process, better general leadership, hiring and firing. I mean, just doing the sort of cleanup on aisle three that needed to be done, even though, again, a lot of the people in the team were quite talented and doing an excellent job of managing their specific domains.

(00:20:52):
Jumping into the product role has been quite eye-opening. I feel a little bashful about the naivety of my view from the outside a year ago. Product teams have a hierarchy of needs, and we like to point at the failures to meet elements of that hierarchy higher up the triangle and sort of impugn the failure of that organization for not, as an example, measuring adoption metrics very carefully and not closely tracking those metrics as a means by which to drive execution. When I jumped in, I was like, "Man, we need to establish some basic standards for test coverage. We need to establish some basic standards for how we do what I call a factory inspection on a product once it's ready to roll off the assembly line." Do we have a checklist for what we call product quality and what does product quality mean? Those basic things weren't there. And so the idea that we should be spending time measuring adoption metrics is absolute insanity.

(00:22:08):
You're skipping a lot of steps between here and there. And so we have made great strides and I think it's translating to product quality improvements for our customers, but I feel, as I said, a little dumb for the way I was thinking about it before I jumped into the deep end. There is just no excuse as an executive for sitting outside of the mess and thinking you know the answers. It's a cardinal sin as an executive to do that. You need to go and see. You'd be in the boiler room, you need to study the system, bottom up and develop hypotheses for how to amend the system. And that's what I've been doing.

Lenny Rachitsky (00:22:46):
I love hearing this because so many people have teams that are not functioning incredibly well and hearing from someone that is not a longtime product person come in and try to fix these problems, I think is really useful and interesting for people to hear. To dig into this a little bit more, was the big lesson and kind of eye-opening moment that there's a lot of foundational work that needs to happen to achieve this outcome that you're trying to achieve, which is measure engagement and adoption well? Is it like tracking and metrics and data science? Is that kind of the lesson there?

Matt MacInnis (00:23:18):
The lesson is that everything must be done in its time and order, and you can move really, really quickly. There's no sort of excuse not to move with urgency on all of these things, but you got to do them in order and you have to lead bottom up. You got to lead from the specific circumstances you observe. And I think for me, one of the best things that's happened over the last 11 months is that I've gained a greater trust in my own instincts, that sort of patterns I've matched across other functions do indeed apply in product, but I have both the advantage and disadvantage of not having led a product function before and therefore must think about every problem from first principles. I have no choice. I can read shit on the internet. I can listen to clear thinkers on topics and import their ideas, but I'm very reluctant to import an idea without breaking it down into its constituent parts and figuring out how it applies at Rippling.

(00:24:29):
And so I don't actually give a shit about adoption metrics as a matter of principle. I care about adoption metrics when I care about adoption metrics. I realize that that's a total logical statement, but it's like I'll get there. And so in certain parts of our product, I really do care about adoption metrics. I care a lot about adoption metrics in our applicant tracking system, our recruiting product, because it's in a really good place from a usability standpoint, it's very well instrumented, it's got very happy users, it's got an awesome growth profile, and so we should still ...

Matt MacInnis (00:25:00):
It's got an awesome growth profile. So we should be really focused on the adoption metrics because I think that's going to be an important ingredient to low churn over time, removing friction from the implementation process as an example.

(00:25:13):
There are other parts of our product where I would say I don't care at all about adoption and am much more focused on foundational things like I said earlier, test coverage or whatever, just to make sure that the thing is stable and good and delivering exactly what it's supposed to deliver once it's adopted.

Lenny Rachitsky (00:25:28):
Now that you're on the inside of the product team, what's something that you think people outside of product, say Matt two years ago or other, I don't know, go to market leads, other execs should hear, need to understand about product that they don't until they're on the inside?

Matt MacInnis (00:25:44):
I'll give you another framework that I like to use. In the financial world, there's this concept of alpha. Alpha is outperformance relative to the index. So that's why you have seekingalpha.com as a very popular website. What they mean by that is you're looking to buy something, some combination of assets that will outperform, let's say the S&P 500, if that's your benchmark. So alpha is the outperformance relative to the index.

(00:26:12):
And then you have the concept of beta. Beta is just volatility. Beta's not good. A high beta stock jerks around for no particular reason. It's discorrelated with the index. It's very high beta. Great if you're an options trader, but other than that, it's not really something you want in an asset.

(00:26:28):
So your ideal stock is a very high alpha, very low beta stock. They don't really come in that shape because alpha and beta tend to be correlated, but that's what you want when you buy a financial asset.

(00:26:40):
So what's the analogy? I think you have high alpha people who are very valuable. I think you also have low beta people who are also very valuable people. Dennis Rodman, basketball player, nut job, very high alpha. And there's room on every team for one Dennis Rodman is a favorite of mine. It's like you can have one difficult employee who's got a ton of upside.

(00:27:12):
So this alpha beta thing, I use it pretty often when contemplating what kind of person I want and also what kind of process I want. So when you're building a product from zero to one, you're probably pursuing alpha. You're looking for some angle on this market or this customer problem where the product is actually going to provide an outsized return relative to whatever the default solution is. When you have a more mature product or if you have somebody in the product operations group or whatever, you probably want a more low beta environment where it's like it cranks it out, it does it very reliably.

(00:27:44):
Our payroll product, we badly want the payroll product to be very low beta. We really don't want the payroll product to have any unpredictability or aberration, and so we're willing to accept more process.

(00:27:55):
And here's a fundamental principle of design in an organization, which is that processes, processes in a business exist for the sole purpose of lowering beta. Processes are for decreasing volatility in the output of the system. The downside of a process is that it suppresses alpha. And you have to be super, super careful and judicious in the application of process and the product team to know that you're lowering beta in the places where you want to do that without suppressing alpha in the places where you need it.

(00:28:35):
So as we've gone through the last year of reforming the way that we build product at Rippling, it's been a game of recognizing those places where I need to implement a touch of process, just a touch. Other places where I need to implement a very clear, rigid process where I don't want alpha, I just want low beta. So examples of this are let's say our product quality list, which we lovingly at Rippling call the PQL.

Lenny Rachitsky (00:29:00):
Why PQL?

Matt MacInnis (00:29:01):
Yeah, so it's actually a really important thing. I think if you want to bring about cultural change in a team ... Look, we have 1,300 people in our R&D organization. It's a big ship that we have to steer. If you want to create a moment that sticks in people's brains and sort of becomes a zeitgeist or something that they latch onto, you got to create an entity, a vessel for meaning, and then you got to fill that vessel with your meaning.

Lenny Rachitsky (00:29:23):
A meme, you might say.

Matt MacInnis (00:29:24):
Yeah, well, sure, a meme. A meme is actually a good example of this in common culture. In pop culture. I think it's why, when people come to the table with ideas from the outside, I welcome those outside ideas. But the first thing I ask the person to do is to tell me what they mean without using those words. So when someone comes in and says, "Hey, I want to do this thing on strategy." I'm like, "Cool. Tell me what you mean without using the word strategy." And it forces them to break it down into its constituent parts. And if they can articulate it clearly without using that word, I know that they know what they're talking about. And if they just fumble around with the word strategy again, I'm like, "Okay, you actually haven't thought this through."

(00:30:01):
So with the PQL, with the product quality list, it's like I could come up with some generic term for this, but I really want a new joiner at the company to understand that this is an idiosyncratic thing to Rippling. This is unique to us. You want to understand this thing. I also want it to become a component of common parlance in the day-to-day work of the product management and engineering teams. So PQL, as cheeky or silly as it sounds, was deliberately sort of angular or stood out as a vessel I could fill with a particular meaning, and so we have a product quality list.

(00:30:32):
And the product quality list is lightweight in the sense that it just articulates in the simplest ways the standards we want you to meet when you ship a product. It doesn't apply to every product, not every line applies to every product, but it's comprehensive and it provides me with a framework for iterating over time as we learn.

(00:30:50):
So just yesterday, we shipped the product to Parker. This is part of our process. When we ship a new product, it goes to Parker, who is the big admin for Rippling at Rippling. If you're not aware, Parker is the sole payroll administrator for Rippling for all 5,200 employees. He personally runs payroll always, there is no exception, for all 5,200 people. He does complain about it sometimes, but it's a remarkable achievement for the software and perhaps for him. So he also installs any new app that we're going to install for ourselves because we dog food the hell out of everything we build.

(00:31:22):
Yesterday, he goes to install this new application. We're about to ship a new app for feedback, allowing people to give one another feedback on their companies. And he installs it and he goes in and it dumps them onto an empty screen. And he's like, "What the fuck is this? What is this? What's going on? Hey, wow, talk about fail." So I chop another one of my fingers off, I'm down to nine. And I'm like, "Well, what did we miss?"

(00:31:48):
What we missed was there was a fucking feature flag, a fucking feature flag. And I'm not allowed to say feature flag without fucking in front of it because feature flags are the bane of my existence and the worst things in the world that constantly cause problems. Engineers put one in temporarily and forget about it. It's like shims if you're building a house and the general contractor puts little shims in places and then forgets that they put the shims there and then builds a wall over them and eventually the shim fails and all of a sudden your door doesn't fit. Feature flags are super dangerous and need to be managed carefully, so fucking feature flags.

(00:32:18):
Anyway, we had one. Parker installs it, they forgot to disable the feature flag. He gets a blank screen when he installs the application. What did I do? My reaction was, "Ugh." Go back to the team, give them direct feedback, tell them not to make that mistake again. But also ask the question, "How do we miss this in the factory inspection process?"

(00:32:37):
And the answer is we didn't have any line item in the PQL for feature flags. So I added a line to the fucking PQL that said, "You are allowed to have one feature flag that governs your entire product at ship." It's an extreme standard that might not be achievable, but it's the standard we aspire to.

(00:32:59):
This framework, the PQL, given these lightweight checklists, iterated on consistently in response to everything we learn as we go, constitutes a very nice lightweight way to lower the beta of the system with hopefully only a modicum of negative impact on the alpha for how we build product.

(00:33:22):
You asked me a very simple question, I gave you a very long-winded answer, but these frameworks help me design systems that scale across one going to 2,000 technical workers.

Lenny Rachitsky (00:33:34):
Wow. Okay. By the way, PQL, is that like an acronym or it's just like, I like this word we're going to call it PQL?

Matt MacInnis (00:33:40):
Product quality list.

Lenny Rachitsky (00:33:42):
Okay, I see. So it's the [inaudible 00:33:44]. Okay.

Matt MacInnis (00:33:46):
PQL, which how could you pronounce it other than pickle?

Lenny Rachitsky (00:33:49):
I'm imagining all your decks have little PQL emojis and the-

Matt MacInnis (00:33:53):
The pickle emoji thing, the dancing pickle in Slack, there's a lot of-

Lenny Rachitsky (00:33:56):
[inaudible 00:33:56].

Matt MacInnis (00:33:56):
Yeah. It lends itself to a bit of fun.

Lenny Rachitsky (00:33:58):
What I think about is pickle Rick. Do you get that reference?

Matt MacInnis (00:34:02):
This is a Rorschach test.

Lenny Rachitsky (00:34:04):
Okay. So this high alpha, low beta, I love this concept. So the idea is depending on the team, depending on the problem, we need a high alpha, low beta person or actually okay with a lot of variants for this specific project that's actually [inaudible 00:34:16]-

Matt MacInnis (00:34:16):
Yeah, we're willing to accept a bunch of volatility in this area in exchange for the upside we get from the creativity and risk taking of these people or the lack of process that sort of gives them the latitude to do what they want to do.

Lenny Rachitsky (00:34:26):
So when you're hiring, you're looking for, again, is this person low beta or not? That's going to [inaudible 00:34:30]-

Matt MacInnis (00:34:30):
For sure. It's really quite a useful way. You know when you meet a candidate and you ... My modus operandi, and I think with talk about hiring for a second, I think I've spent a lot of time with teams at Rippling talking about how I hire. And it is born of batting practice. It'd be super interesting to actually be able to rewind the tape on my life and sort of contemplate how many candidates I've met in every context. Many thousands, maybe tens of thousands, I don't know. It's a lot of batting practice and a lot of model training in my brain.

(00:35:06):
So I rely a lot of my intuition, which of course HR people say you're not supposed to do. That's complete bullshit. If you have a good intuition, you should absolutely rely on your intuition.

(00:35:15):
And what you have to do after you have a reaction to a candidate when you're looking at hiring somebody is you need to decode your intuition so that it can be expressed to other people productively. So one of the frameworks that I use for this is SPOTAC. It's a very ugly acronym. There's a hat tip to somebody out there in the universe who originally thought of this. It's not me, but I adopted it. And it's that people are smart, passionate, optimistic, tenacious, adaptable, and kind. Those five things. Six, can't even count. I told you I lost a finger when I made a mistake, so I was down one.

Lenny Rachitsky (00:35:54):
Nine to go.

Matt MacInnis (00:35:54):
SPOTAC isn't by itself a good top down framework, but when you're thinking about, "Oh, why did this candidate just ... Why did it not click? Why did I not like them?" You go down the list, you're like, "Oh, yeah, no, this person, it's that they were not excited about the idea. They weren't passionate." It's that they talked shit about their previous manager and that they were a victim of the performance of their last two companies. That's what it was, they're not optimistic.

(00:36:24):
The framework is super useful to evaluating people. And I think the alpha beta framework is also super useful when you come away from a conversation and you're like, "I like that guy. I think he'd be really, really good. Why is it that I don't think he would do a good job on this product in particular?" And the answer is like, "This is a high alpha product area and he's a low beta person." Valuable, but definitely not the right fit for this. So I think it's really useful in that context as well.

Lenny Rachitsky (00:36:48):
I love all these frameworks. You're speaking to this audience, framework to frameworks, frameworks.

Matt MacInnis (00:36:52):
Yeah.

Lenny Rachitsky (00:36:53):
So high alpha, low beta, sometimes high beta is okay, SPOTAC. In hiring, is there anything else that you find really useful? Before we move on to a different topic.

Matt MacInnis (00:37:03):
When I first started working in the product organization, I was introduced to an interview framework or an interview tactic that I hadn't really used much at all, I think in my career, which is that every product person at every seniority level is given the same case study. And the case study is extraordinarily difficult. It requires you to think about many, many dimensions simultaneously, to think about data propagation issues. It gets quite technical.

(00:37:37):
And the rubric that we use to sort of evaluate performance of that case study is it gives you guidance on what for us, like an entry level PM looks like, what a junior, mid-career, senior executive PM might look like. And everybody comes away from that interview feeling like poop, like they had failed it. Whereas on our side of it, we're like, "Wow, that person got really far." They saw around three or four corners in a really impressive way. There was 10 they didn't see around, but they saw around four of the hardest ones. And they were not defensive when we gave them new information that called into question the validity of their solution. And they were willing to interrupt us to ask more questions," and and and, like a lot of the sort of basic human interaction models.

(00:38:25):
You never think that giving someone an impossible task and even including the L5 person versus the VP on the same thing would be productive. And let's just say our recruiting team still sort of kvetches a bit about this and feels like we eliminate people too aggressively at this stage of the interview process. But I've found the wisdom in it and think it's actually quite useful to give everyone the same simple, complicated prompt and just see. Hand them a drill bit, give them the concrete wall and see if they can get a millimeter or an inch into the concrete. They're never going to get all the way through the wall. It doesn't matter. You're going to learn a lot. And I've found that to be kind of an eye-opening new thing for me that has been fun.

(00:39:04):
Look, the joy of product and the joy of product management and the joy of being part of product, I think there's a bunch of joys actually, if I could give you a sort of running list, but one of the big joys is that you get to work with some of the smartest people in software. Engineers are very smart. They're not always the best sort of social entities. Salespeople are awesome social entities. They're not always the best systems thinkers. You go down the list.

(00:39:28):
But the magic of product management is that you kind of have to ... We talk about the mini CEO. I think it's kind of a stupid misnomer, but there's some wisdom there. And I think the wisdom is that you have to be a polymath. You've got to be really good at working with other people. You got to be good at communications and articulation. You got to be good at project management. You got to be good at the science and the math and the engineering. And it's really fucking cool. So I think one of the great joys of this job for me has been interacting with the tippity top of the smartest and most polymathic people in the industry.

(00:40:01):
I'll say one other thing about what I love about leading product, which is as a COO, my job was to accept the product as it was and optimize everything around that. My job was to make sure that the product operations, in our business, the interface to the insurance carriers, the interface to the payment entities, the government regulators, that stuff all just sort of worked. It was to make sure that our sales engine, our marketing engine, all the go to-market stuff optimized itself around what the product was. It was about recruiting and making sure we got people in to work on the product. You kind of go down any function that isn't in R&D, and I had some hand in trying to figure out how to make that function work to the best of its ability, given what the product was.

(00:40:48):
And now that I lead product, I'm like, "Oh, wow. This is the high order bit." Not that I didn't sort of understand that, but now I really get that product is the high order bit. If you get the product right, it fits in the market, everything else gets easier. Finance is easier, sales is easier, marketing is easier, recruiting is easier, everything gets fucking easier. So I think the other joy of leading the product function is that I get to set the highest order bit in the business's success to one.

Lenny Rachitsky (00:41:22):
This is really great to hear. A lot of times people outside product don't understand these sorts of things and look down on product a lot of times, especially sales folks, COOs a lot of times. I love that you're seeing this and realizing this and recognizing just how important and interesting and challenging this work is and just how awesome PMs are. As you know, a lot of people are a very anti-product manager. "Why do we need product managers? We don't need them. Slow everything down, all this process."

Matt MacInnis (00:41:51):
Yeah. I have a distinction there, which is that I'm anti-shitty product managers.

Lenny Rachitsky (00:41:53):
That's exactly how I put it. If you hate product managers, you just haven't worked with a great product manager.

Matt MacInnis (00:41:58):
Well, it's like, look, I love wine, wine's one of my things. And I've learned a lot about wine. And one of my favorite lines is like, "I don't like Chardonnay." And I'm like, "No, no, no, no, no. Chardonnay's are the most fucking amazing varieties of wine in the world. You just haven't had good Chardonnay. And there's a Chardonnay out there for you." Product management, it's like you don't like product management, you think product managers suck. It's like, well, you just haven't had a good Chardonnay yet.

Lenny Rachitsky (00:42:22):
That's exactly what I [inaudible 00:42:24]-

Matt MacInnis (00:42:24):
Once you have one, you can't unlearn it.

Lenny Rachitsky (00:42:26):
You're like, "Let's find that PM ASAP."

Matt MacInnis (00:42:30):
No, let's find that Chardonnay ASAP.

Lenny Rachitsky (00:42:34):
[inaudible 00:42:34] with some Chardonnay. You touched on this product market fit point, and I want to double down on this thread. You've had a couple really interesting experiences of struggling to find product market fit with your own startup. You said you worked on it for nine years, you said?

Matt MacInnis (00:42:47):
Mm-hmm.

Lenny Rachitsky (00:42:47):
Okay. And then with Rippling, complete opposite, extreme product market fit, up and to the right. What's something you've learned about just that that you think people maybe don't understand about what it feels like, what it takes to get to product market fit, how things change?

Matt MacInnis (00:42:59):
There's a line that this venture capitalist, whose name I will not mention, said, which was that product market fit is a sort of thing where you absolutely know it when you see it, and therefore if you don't absolutely know it, you don't have it.

(00:43:17):
And this kind of gets back to my point about learning from mistakes versus successes. It's like, ah, man, over and over again, over the course of the many years that I spent at Inkling, we thought we had it. We thought we had product market fit, maybe, maybe. And in hindsight, with the benefit of now having experienced solid product market fit, it was so, so obvious that we didn't.

(00:43:45):
And I've invested in like 60 companies or 70 companies. I don't know, it's not something I actively do. But opportunities, by virtue, I think, of my role at Rippling, sort of show up. And I talk to lots of entrepreneurs and I love it and I find it super stimulating and I love the fresh ideas and it's just something I do as a real cherry on top of the sport that I play already. But when I get the investor updates for the guys who've been at it for like three, four years and I read the updates from them that I sent to my investors in 2011 and 2012, I'm kind of heartbroken.

(00:44:29):
We talk in Silicon Valley about never quit, but that is complete absolute venture capital bullshit. The incentive of venture capitalist is to put money into your company and milk you dry. They never get their money back. There is no way for them to take that investment back. So the only logical desire that they would have is for you to keep trying against all odds because there is the occasional example where someone pivoted from A to X and it was wildly different and it worked. Slack was originally some sort of a gaming company and became corporate chat. Airbnb maybe. It's like there's some examples of companies having made wild pivots and succeeded, but man, is that rare. Just so exceedingly rare.

(00:45:21):
And I think it's important to remember, I'm 45 years old, we're going to be on the planet, the average age of a man in the United States when he dies is something in the mid 70s. I got 20, 30, maybe if I'm lucky, 40 years left on the planet. Very conscious of the time that I have. And I don't regret what I did at Inkling, I learned a lot. It informed what I do now. I don't think the chapter I'm in right now could have come without the chapters before it. So it's a beautiful, wonderful thing that I did what I did. But when I read the investor update and I'm like, "You're where I was and you are not getting out of this."

(00:45:56):
The Silicon Valley try until you die mindset is not pro-entrepreneur, it's pro-venture capitalist. And I know why that is, but I think it's important to say out loud that you should fucking quit. You should reset the clock, you should reset the cap table because trust me, product market fit when it arrives is insane and it's exciting and you should pursue it. And never delude yourself into believing you have it when you don't. It is dangerous and regrettable. How's that for a speech?

Lenny Rachitsky (00:46:33):
Beautiful. The anti-VC speech. The-

Matt MacInnis (00:46:38):
I got more where that came from. By the way, it's not anti-VC. It's anti-

Lenny Rachitsky (00:46:43):
VC propaganda.

Matt MacInnis (00:46:45):
Everybody's acting in accordance with their incentives in Silicon Valley, the executives, the founders, the venture ... Everybody's, of course, behaving in accordance with their incentives. And the venture capitalists have very strong enduring incentives that have shaped the dynamic of how Silicon Valley works. There's nothing wrong with that. It's just really, really important to point them out and scream at them for the 25-year-old entrepreneur who has no fucking clue how this stuff works.

(00:47:12):
Trust me, the 45-year-old entrepreneur or the 50-year-old venture capitalist who've been in the game for a while, they get it. They've observed it. They know what it's like. The system is there to take advantage of the people who don't, or at least it is the easiest prey for the incentive structures, not for venture capitalists as individual people who are beautiful and all of them are just really wonderful people. It's just that the incentive structures lead to some real harm, I think, in certain cases.

Lenny Rachitsky (00:47:37):
And the thing I find is when you do quit, VCs ... I'm always just like, "Hey, let me know when you're starting your next thing. I'm excited to invest." They're rarely, unless they're not a great VC, rarely are they just pissed at you for how could you possibly not make this work [inaudible 00:47:52].

Matt MacInnis (00:47:52):
That's the thing, as a founder, when it's time to throw in the towel on your business and you're so obsessed with giving money back to the cap table, I always remind the entrepreneur like, "Hey, if you're in the seed investing game, your forecast is zero. Your assumption on every investment is that it's going to go to zero." Any seed investor who doesn't take that stance is off their rocker anyway. They're a very bad investor. Seek investors who play the long game, who want to be in your second and third company and are willing to take a bet on the first one and let it go to zero so that you can get on with stuff. This is like, I've had that conversation many times.

Lenny Rachitsky (00:48:28):
This episode is brought to you by GoFundMe Giving Funds, the zero-fee donor-advised fund. I want to tell you about a new DAF product that GoFundMe just launched that makes year-end giving easy. GoFundMe Giving Funds is the DAF or donor-advised fund supported by the world's number one giving platform and trusted by over 200 million people. It's basically your own mini foundation, without the lawyers or admin costs. You contribute money or appreciated assets like stocks, get the tax deduction right away, potentially reduce capital gains, and then decide later where you want to donate. There are zero admin or asset fees, and you can lock in your deductions now and decide where to give later, which is perfect for year-end giving. Join the GoFundMe community of over 200 million people and start saving money on your tax bill, all while helping the causes that you care about most. Start your giving fund today at gofundme.com/lenny. If you transfer your existing DAF over, they'll even cover the DAF pay fees. That's gofundme.com/lenny to get started. This begs the question of just when is it time to quit? If people hearing this might be like, "Oh man," what are some signs that, okay, it's time to wrap it up?

Matt MacInnis (00:49:38):
Here, look, history provides us with a clear guide. When you look at companies having hit it big, they hit big pretty quick. It's very, very dangerous to be late to the party, it's very, very dangerous to be early to the party, and the vast majority of the time, that's the problem. Rippling, had it been started in 2014, would not be what it is today. I think Rippling, had it been started today, would not be what-

Matt MacInnis (00:50:00):
...Not be what it is today. I think Rippling, had it been started today, would not be what it is five years from now today, and so I think timing is a lot and it's very hard to control for, but when you get the timing right and the market is real and the product works, product market fit, like I said earlier, it's super clear, and so if I were to pick a number out of a hat just from my lived experience, I think it's very important, one aside, don't ask people for advice, ask people for relevant experience. If you ask them for advice, they will always give it, but if you ask them for relevant experience, they rarely have any to offer, and if they don't have any to offer, then don't ask for their advice.

(00:50:41):
So ask people for relevant experience, and I try to do this with my own entrepreneurs when I work with them, it's like, let me offer you whatever relevant experience I have, and my relevant experience on this topic of when to quit is like, I think we could have called it after the second or third pivot, which was somewhere around year four. It is of course very important to believe in what you're building and to be persistent, but there is definitely no shame in saying, "Look, we've pivoted once or twice. It's not catching. I got to go do the next thing," and I think if you're year four, year five in your entrepreneurship journey, and it's not just obviously a screaming rip-roaring growth story, it's extraordinarily difficult. This is so extremely rare. So beyond even already the rare scores you're going to face from the outset that now is going to convert to something crazy. So that's hard to hear, I guess, but man, it can be really liberating when you're like, "Fuck it, I'm going to do this. I have the energy. I'm going to do it again. I'm just going to do it with a clean sheet."

Lenny Rachitsky (00:51:48):
That is really helpful. You have this really fun way of describing product market fit around receptors and drugs.

Matt MacInnis (00:51:54):
Oh yeah. Yeah. I think this is a really fundamentally misunderstood dynamic. When founders message me and they're like, "Hey, like my LinkedIn post and my tweet for this launch," I do it. I retweet it, I like it, whatever. Nobody follows my Twitter anyways, it doesn't matter, but I do that, but I think to myself, this is not what this is about. This is not how great companies are built. It can be a nucleating event, but it's not a major thing, because nobody cares about your company. Your launch doesn't matter. Big, fat, pull the slingshot back, launches amount to the teeniest thimble of water in the ocean of noise about startups and companies, and so you just got to build it brick by brick bottom up, and these launches don't really amount to much, and so how do you think about that? How do you think about the insignificance of your launch or you think about all the effort you're putting into building a product that you believe is going to have product market fit?

(00:52:56):
Well, if you recognize that the market is immutable, no amount of tweeting, LinkedIn posting, advertising is going to change whether the market wants your product. It might raise awareness about your product, but it's not going to change whether somebody wants it. Then you take a different mindset. You have to view your startup as running an experiment in the universe to see what you get in return for that, and this analogy of drug discovery and binding receptors is like nobody at Genentech thinks they can market their way to better performance inside your body. The binding receptors for that drug, they exist or they don't, and when they build their product, their goal is to find out whether the binding receptors exist, but fate already has decided the outcome. This is absolutely true of every software product you build. Fate has already decided the outcome. The market's either going to latch onto your product and run with it or it's not. Do not ship the product, find a lack of success, and then try to market your way through that, because the binding receptors likely don't exist, and for me, it was a very liberating mindset, because now I just have to find the right drug, and I can forget trying to convince the body to develop the binding receptors for whatever it is that I'm building.

Lenny Rachitsky (00:54:13):
What I love about your advice here is you were an early investor in Notion, which is one of the classic stories of it took them... I think it was four years to get to something. They moved to Japan, they worked on the whole thing, and so is [inaudible 00:54:24] from there? Is that a rare example where it actually worked? And that's not an example to be inspired by, because it's extremely, extremely rare. Let's talk about alpha beta again.

Matt MacInnis (00:54:32):
Okay. As an investor, you might build a checklist of things you want to make sure are true or false about a company and hope that that's going to yield the kind of investment success you're looking for. Does it have this kind of founder? Is it a C Corp in Delaware? Boom, boom, boom, boom, boom, boom, boom, and these checklists are all about what? They're all about suppressing beta. They're about avoiding avoidable mistakes. They're about bringing stability. Jeff Lewis is an investor who has many angular views on things, and I think one of his most enduring phrases is narrative violations. This idea that the common wisdom must be violated in some way by every company that has an outsized success. It is absolutely true, and when I give these general observations on the patterns in Silicon Valley, the most successful businesses inevitably violate something on that list in some really important way.

(00:55:37):
So Notion, you can't replicate Notion's success as an entrepreneur. You can't replicate it because you're not Ivan. You can't replicate it because you're not Notion. You can't replicate it because it's not 2010 when they started the company. Do the math on that. Or 2011, actually. These guys stuck with it. They went through hell. They pivoted. They went to Japan and sat in kimonos and meditated on what they were going to build, and by hook/crook, they got to where they are today as a really wildly successful business in an extraordinarily difficult market where building businesses is virtually impossible in productivity. It is dominated by Google and Microsoft. Carving out your own niche in that market is just unthinkable, and so I look at Notion as having succeeded by virtue of the narrative violation of persistence, I don't think is a good idea for very many people that happen to work for them, and I look at it as being a function of the founding team and their specific idiosyncrasies, the absolute insistence on craftsmanship from Ivan. This is him. That's his thing.

(00:56:55):
The takeaway lesson is not give up or don't give up. The takeaway lesson is certainly not go do what Notion did. The takeaway lesson is that every company succeeds on the foundations of the idiosyncrasies of the founder. The idiosyncrasies of the founder. Rippling succeeds for almost the polar opposite reasons that Notion succeeds, but in both cases, the companies succeed on the idiosyncrasies of the founder, and so embracing that, recognizing those idiosyncrasies, that's what great investors do. They spot that element of spikiness and greatness in a candidate investment, and they convert that to a commitment, and then of course the investor or the good ones accept what they get in exchange from that for the universe, from the universe.

Lenny Rachitsky (00:57:44):
I love that we went in this direction. I wasn't planning to talk about your investing career. Just to give people a reason to listen to this and maybe rewind, and I want to ask another question around investing. What are some other companies you invested in early?

Matt MacInnis (00:57:55):
First of all, okay, so I sort of hate the question. What are some other companies you've invested in? It's a fair question, but the problem is I'm going to give you a bunch of companies I've invested in that won, that are really notable. So what I would like to do instead of answering that question ... Here, let me give you some bait. I was one of the first investors in Notion. I was perhaps the first, I don't know, ask Ivan. Clever, which had a great exit. I was one of the first investors in Zenefits, if you've heard of it.

Lenny Rachitsky (00:58:26):
Heard of it.

Matt MacInnis (00:58:27):
I was, before I joined, one of the first investors in Rippling, and then more recently invested in ... Here's a funny one. I was one of the first investors in Deal, if you've heard of them.

(00:58:43):
I was able to exit that position, and then hopefully that company's going to zero with their criminal behavior, but whatever, but more recently, if you know Decagon, which is doing some really cool stuff on the AI front.

Lenny Rachitsky (00:58:58):
Killing it.

Matt MacInnis (00:59:00):
I'm in laying chain. Great. So those are some companies that you maybe have heard of, but how about I invested in Macro. Founder was Derek Lee. Macro's out of business. I invested in Debrief, Ned Rockson. It's out of business. I invested in Verb Data with David Hertz out of business. I'm reading from a list. I invested in... What's the number? 70 companies according to this list where I track things and most of them went to zero and all those founders were awesome, all those founders were kick, and all those founders put a ton of energy into building their businesses, and they went to zero and they're enduring relationships.

(00:59:37):
I can call on any of those people, I think, maybe with the exception of Deal, and call in a favor and have... and I've got a few subsequent... and actually a lot of them joined Rippling, believe it or not. So I don't know. Companies I've invested in is a long list, and I love to give you names of companies that don't exist anymore because it's self-serving and a horrible survivorship bias to just list the good ones.

Lenny Rachitsky (01:00:00):
I love that answer. I think you're being modest in the context of your hit rate is clearly very high. Even one or two incredibly successful companies out of 70 is a win in VC, and so you're doing very well, but I think that's a really important perspective. When you see people's logos on their websites of all the companies they've invested in, you have no idea how many hit bats they've had.

Matt MacInnis (01:00:22):
I think it's good practice to ask people to give you the full list. Yeah.

Lenny Rachitsky (01:00:24):
What are your favorite failures that you've invested in?

Matt MacInnis (01:00:29):
Oh, no. I'm not actually... Okay.

Lenny Rachitsky (01:00:31):
Well, obviously, no, we don't need spend time on it, but I think it's actually a really good question, but yeah, what are some of your best failed investments? Show me the logos of the companies that didn't work out.

Matt MacInnis (01:00:39):
It's a juicy question. Yeah.

Lenny Rachitsky (01:00:42):
There's a topic around this area that I wanted to spend time on, and I haven't heard anyone think of things this way, which is this idea you talk about of compounding plus power law plus entropy and how that's a really useful frame to think about business.

Matt MacInnis (01:00:58):
So you kicked this conversation off sort of invoking the extraordinary outcomes, demand, extraordinary efforts line, hat tip to Dan Gill, and these are part and parcel. Man, understanding the nature of the universe is a pretty good way to work within it, and so power law distributions happen everywhere. It explains why so few people control so much wealth. It explains why Steph Curry is just so vastly better than the next guy down on the list on the basketball team. It explains why populations are concentrated into a relatively small number of mega cities in the world. It's like, power law distribution just plays out everywhere, and once you see it, you can't unsee it. It sort of plays out in many dynamics.

(01:01:47):
People tend to think that the world plays on a more linear relationship where the X and Y axis are sort of Y equals X, but that is absolutely not the case, and the implications are profound. It's like if you build something to 80 or 90%, the Y axis is barely budged yet. You haven't hit the inflection point in terms of reward, and so the implication of the power law more broadly is that people who are in the top 10%, the top 5%, don't just get 10 or 20% more reward. They get 10X the reward or 100X the reward. It's really dramatic.

(01:02:20):
Entropy, the second law of thermodynamics is a very simple concept. It's the reason your sock drawer becomes messy. It's the reason that potholes form. It's the reason we have to put so much energy into maintaining the aircraft we fly to keep them safe because they really, really, really want to fall apart, and that's the nature of things. If you abandon a city for a few months, it starts to go fallow, and so entropy is just this concept that shit tends toward disorder.

(01:02:48):
The universe, I mean, life itself is a temporary victory against entropy. You and I should not exist. The sun gives energy to the planet. It organizes stuff that we can eat and we fight entropy until we lose the battle somewhere, as I said earlier at the age of 70 or 80, if we're lucky. What does this have to do with product? This is really about effort.

(01:03:17):
The only antidote to entropy, the only antidote to decay in a system is energy. You got to inject energy. So if you have a code base, every line of code that you add to that code base increases the entropy of that system and demands ever more energy from human beings to go and intend to it to make sure it doesn't break, and if you want to achieve greatness, if you want an extraordinary outcome, and in particular, if you want to be in the top 10%, top 5% on the X axis so that the Y axis is through the roof, then you have to relentlessly inject energy at every single step of the game. Teams will, sadly, but because we are all human, teams will always optimize for local comfort over company outcomes.

(01:04:11):
Not because they get together and think, "We should do that," although unions do do that unequivocally, deliberately, but even in a collection of product managers or engineers, what's going to happen over time is entropy is going to creep in and people are going to optimize for local comfort. Your job as an executive, as a leader, is to fight that entropy tooth and nail every single day. It means that every time you see a bug, every time you see a bug, not most of the time, every time you go and you drop it at the feet of the product manager or the engineering manager, every time, in public, preferably, it means that every time someone comes to you to hire someone and says that they have skipped the back channel, every time you're like, "You can't hire this person unless you do the back channel," it means that when you get into the board and tired zone on any process, that you as the executive have got to demand the 99th percentile of energy, because otherwise entropy creeps in and the system decays. You have to do this.

(01:05:19):
One of the messages that I delivered recently at our big executive big... Like our top 75 manager offsite that we do roughly every 18 months, was a reminder that if the purest form of ambition and the purest and most intense source of energy in the business is the founder CEO, that every next concentric circle of management beyond the founder CEO has the potential to be an order of magnitude drop off in intensity, and that is dangerous because if you go to two layers and it's two orders of magnitude drop off and signal and intensity, that is a very dysfunctional organization. So what I say to the team was, it's not that you need to buffer people from the intensity of the CEO, it's that you need to absolutely mirror that intensity.

(01:06:13):
There are plenty of constituents in the business around you who will advocate for relaxing. There is an infinite supply of people under you who will buffer other team members from the intensity of the demands. Your job is not to be one of those buffers. Your job is to preserve that intensity at its highest possible level and let the buffering happen somewhere else, and that's the point is that entropy creeps into the system insidiously and slowly over time off your radar and you have to maintain that intensity every minute of every day to try and fight it if you want to stay at the extreme right end of the power law that obviously governs the outcome of everything that we build.

Lenny Rachitsky (01:07:03):
What does that look like to pass along that intensity? What does that feel like? What does that look like? So say Parker comes to you, "This bug sucks. I got this broken screen." You cut off your finger. Maybe that's the example.

(01:07:18):
Okay. Still got them. I got all 10.

Matt MacInnis (01:07:21):
I'll give you concrete examples. Actually, the joke that I sort of played on this one when I presented to the team was that the next sort of slide in my presentation was with the sound effect, the Slack huddle thing, and Parker's icon in Slack is just, he uses the generic yellow...

Lenny Rachitsky (01:07:42):
The egg?

Matt MacInnis (01:07:43):
Yeah.

Lenny Rachitsky (01:07:43):
Oh, wow.

Matt MacInnis (01:07:46):
It's funny, and so everybody knows the yellow egg is Parker, and so the next slide in the presentation was boop, boop, boop, boop, boop, boop, boop, which is the sound that Slack makes when someone calls you, and it was Parker Conrad is inviting you to a huddle, and then the next slide was Parker Conrad is modeling personal intensity, and the idea is that if you know, you know, if you've ever been dragged into an... "I want to talk about this fucking problem right now and whatever you're doing, unless it's an interview, I want you to come and have a conversation with me."

(01:08:13):
That intensity is one place where it plays out. Every product team at Rippling, and we have a lot of them now, have public feedback channels. I am in there upside down on everything I find when I use those products, and I just model for everybody that this is how at least I want to do it, which is, "I don't like this. I don't understand this. Tell me why this is this way." Boom, boom, boom, boom, boom, and people jump in and respond. The factory inspection process that I mentioned, which is where at the end of the assembly line, I jump out with the pickle and we talk about all of the elements. You have to record a loom of every major flow through the product. I personally review every one of those flows, I got a backlog I got to catch up on today and provide feedback to people always in a public channel so that every other product manager and engineering manager can jump in and see how the process has worked for other teams.

(01:09:01):
It's about modeling the intensity publicly so that other people can say, "Okay, this is how we do things around here," and it gives the reaction from the team that received the message that you have to inject that energy every minute of every day and that there are no exceptions, was not like, "Ooh, that's exhausting." The reaction is, "Oh, that is so invigorating." It's so wonderful to hear that we're going to achieve these great outcomes, or at least we have a shot at doing so, and that you're empowering me to follow my instinct, which is to really push for the best result.

(01:09:39):
The reaction universally is like, "Ugh, what a relief that I get to go be intense," because nobody in a position of leadership wants to be chill, and what's worse than a chill boss? No, don't work for a chill boss. Don't be a chill boss. It's the most pejorative label I could give you. Chill boss or chill PM. Don't be chill. Chill doesn't accomplish shit. Be intense. Be good, be respectful, be intense. Don't be chill.

Lenny Rachitsky (01:10:09):
Again, this advice comes from where we started, which is this is what success looks like, because somebody that is less chill than you is going to find that crack and come after your market. Is that the gist?

Matt MacInnis (01:10:21):
For sure. I mean, again, if you're chill and you move the X axis down 10 or 20 points, the Y axis collapses. It doesn't just drop 10 or 20%. The Y axis collapses, and this is just kind of true in everything we do. So yeah, if you want to win, you should probably try.

Lenny Rachitsky (01:10:45):
This is what I always say to people trying to build lifestyle businesses. There's always this idea, "I'm going to build a side business, I'm going to make recurring income, it's going to be amazing," and in my experience, anytime there's a market or something shows up that's juicy and there's ways to make money, somebody's going to come at you and work harder, raise more money, and there's only so long you can maintain that.

Matt MacInnis (01:11:04):
Well, man, there's a whole other podcast episode on the concept of leverage. If you sell your time, you've only got 24 hours a day to give, but if you can create a product that scales, the marginal cost of a unit of that product is zero like software, it's going to be competitive, man. Sell your time, it's not going to be super competitive, but achieve that level of leverage and it's a pretty efficient market.

Lenny Rachitsky (01:11:33):
To close out this thread of intensity and adding energy to everything, something I've heard about you is you're big on escalating. You're a big fan of escalating issues, and also you always tell people to never not give you negative feedback, to always share feedback to not hide anything. Tell me about those two.

Matt MacInnis (01:11:49):
Fundamentally, the most selfish thing you can do is withhold feedback from someone. Who are you optimizing for when you do that? What are you optimizing for when you think a thought that would help someone improve and you avoid giving it to them because it would make you uncomfortable? Well, you're optimizing for your own comfort and it's fundamentally selfish. It's the most selfish thing you could possibly do, is withhold feedback that would otherwise be useful to someone because you don't want to be uncomfortable. Well, that's not how high performance teams operate. So I demand feedback, and I give it, and it doesn't mean that when I give feedback, it's not open to being questioned or discussed. I mean, of course it is, but when I observe something, I try to say it. That's the feedback topic.

(01:12:35):
The part of this that has been interesting to me is that people withhold, escalate, the customers withhold. Customers don't want to escalate to me as an executive. Even the founders in whose businesses I've invested who use Rippling are reluctant to hit me up when something goes wrong because they don't want to bother me, but it's literally my job, literally my job to find things, problems, and make them better, and by virtue of making those specific things better, to iterate on the processes so that the system that builds the system can get better.

(01:13:09):
There's no greater gift to me as a product executive than receiving an escalation from a customer. We have an escalations team at Rippling, which sounds weird, but it's people who are just particularly skilled at pistol whipping other people in the company to get to real root causes, real root causes. Not like throw away the word root cause, like, "Oh, we fixed the data error and shut the ticket down." No, you went and you found the software that created the data error, and then you found the system that created the software that created the data error, and you solved all of that back to the top.

(01:13:44):
Escalation seems extremely good at that at Rippling. So we have sort of a dedicated little team that does this for us. Escalations are a gift, and it's like, if you're a listener right now on this podcast and you are a Rippling customer and you have shit that you think we should know, the fact that I might already know it is not a reason for you to withhold the gift of your feedback. So it's an attitude that I take to this every day. I've got a little cue of some stuff that I've... Minor things that are from the last couple of days from people who had some knits and issues that I'm just like, I've got them queued up on my to do list today and I'm going to take them to the product teams directly and be like, "I'd like to understand what happened here." Not in a negative way. I just think we'll all get better if we study this one, and so yeah, escalations are a gift, feedback like that is a gift, and nobody is ever inconveniencing me when they do it.

Lenny Rachitsky (01:14:32):
For people that are listening to this and feeling like, "Man, this is so stressful and intense and just like, I don't know if I want to work this way," give them a sense of just how successful Rippling is. I think a lot of people may not even have heard of Rippling. A lot of people are like, "Yeah, it's doing great." What are some things you can share that are public or not public that give people a sense of just how massive this business has become?

Matt MacInnis (01:14:53):
People look at Rippling from the outside, I think they think of us as payroll and HR or whatever, which is cool. It's a bit like saying Microsoft is a desktop operating system company or it's like every company starts from somewhere.

Matt MacInnis (01:15:00):
... system company or ... It's like every company starts from somewhere and grows out from there. We see ourselves as building the most successful business software platform in history. In fact, that's the mission statement of our product organization under the umbrella of the mission statement of the company, which is to free smart people to work on hard problems. And when you translate that from where we are today to where we think we're taking things, it's like we really do believe that the core of every workflow and everything that a company has to do, be it AI or manual traditional GUI based software, is who's doing stuff, who owns it, who's accountable? And so the people record is a really important component of that. You can argue that the customer record's also very important. And of course some big businesses have been built on that primitive as well, but we think the people primitive is actually much more important.

(01:15:43):
And that the only thing that hasn't been done here is somebody hasn't been ambitious enough to build a good business on top of that primitive. Workday is terrible software. Everybody agrees on that. I think Workday agrees on that. Good luck to them. But they have failed actually, despite their success, to build a really broad general purpose software platform for business software on the foundation of the people primitive. So we're going to do that.

(01:16:03):
And we're successful because we deliver on that promise at the scale we're at today. The fact that you can do ... and this is not a sales pitch or sort of like an advertisement for Rippling. I just think it's important to sort of contemplate that when you bring together a bunch of disparate business processes into one system on a common business data graph, an object graph, a data lake with a consistent interface, you can do some pretty magical things.

(01:16:27):
So we do payroll, we do HCM, we do IT, we do spend. We are about to launch a new product in the category of business intelligence and data management. And there's a whole bunch of other stuff coming beyond that. And then you layer in AI on top of this, where we alone, where we alone have all of your business data organized into this nice, neat package with a beautiful semantic layer on top of it. The AI can work magic. And we have shipped nothing, nothing yet in this category that I would say gets anywhere near what we're going to show next year. And it is going to set the standard. It is going to be the most ... The back flips that the AI is doing reading and writing data for the user just on our internal use cases at Rippling is jaw dropping. So I'm super excited about the tailwind this is going to create for us.

(01:17:20):
You ask about what can I share about the success of the company? What I can say, there are tens of thousands of companies that now run on Rippling. We're less than 1% of the market. And the market cap at 16 billion, I think now undervalues where we are from a revenue perspective by a long shot. There is just so much upside to do what we're doing. And SaaS might be dead-ish in terms of point solutions, but long live SaaS in terms of what we're building.

Lenny Rachitsky (01:17:48):
Let me follow that thread in AI. There's been a lot of talk about AI is going to replace SaaS, as you maybe just said.

Matt MacInnis (01:17:55):
Yeah. People are going to vibe code their way to their payroll system, which I ... good luck to the employees of those companies.

Lenny Rachitsky (01:18:01):
And so what I'm hearing here is that you actually do believe a lot of SaaS companies that are selling individual solutions are in big trouble. The answer implied here is this kind of compound startup idea of you need to do a lot of things for people for them to continue to pay for your software. Is that the gist?

Matt MacInnis (01:18:18):
No. I think the gist is ... there's a really good quote. I forget who it's attributable to, but it's, "There's two ways to make money in software, bundling and unbundling." And you just got to get the timing right. So this is a period of bundling. So here's the problem; point solutions don't have enough data in the age of AI to be useful. You got to be able to provide the AI with a lot of context about a lot of data so it can do things. It can do joins. It can do correlations.

(01:18:49):
And so if you're a point solution, you're in hard water because you've got to now rely on data from other sources. You've got to integrate to third party systems. And when you integrate to a third party system, even the best ones are still sort of drinking their data through a straw, which is a real problem. I mean, the biggest HCM software company you can think of integrates to the other biggest payroll software company you can think of through flat files via SFTP. What are they going to do? What are they going to do? It's just never going to work. It's just no way. And so I literally have no idea what they're going to do. They're just not going to build AI software, I guess. Point SaaS is sort of in a rough spot, especially when you cleave two really important systems apart and say they have to integrate. It's very, very hard.

(01:19:39):
The other thing that I would say about the world of, even just like not SaaS, but AI software is that point solutions in the AI world are also in a rough spot for the same reason. It's like if you're selling the shovels like OpenAI and Google with Gemini, you can make money. And if you own the mine, like Rippling, with the data, you can make money. If you're somewhere in the middle, building AI software that then tries to use the shovels from the shovel provider, but then also needs to rent out the mine, or get the ore out of somebody else's mind and start refining it, you're in a very difficult place from an economic standpoint. Because you're not going to be permitted by either of those parties to build a big business on their backs.

(01:20:25):
That's just not how it's going to work. They're going to demand value capture that crushes your unit economics. So I look at the landscape of AI companies that I've seen and I think you have to have a really durable, interesting insight that gives you a shot at viable unit economics to be an interesting business. And that is going to kill off 80 or 90% of the stuff that I see right now as standalone AI businesses.

Lenny Rachitsky (01:20:53):
So what I'm hearing here ... I love that you correct me when I get these things wrong, and that's exactly what I want. What I'm hearing is it's less about how difficult it is to build the SaaS product. It's about, do you have first party data that allows you to build an incredible AI product on top of what you've got?

Matt MacInnis (01:21:09):
Yep. Because look, SaaS software is a bit flipping. All SaaS software applications are bit flippers. It's an interface changing-

Lenny Rachitsky (01:21:09):
Your database?

Matt MacInnis (01:21:18):
Yeah. Changing values in your database, that's what it does. It's a really hard problem. One of Rippling's superpowers is we're a coin sorter. You dump $20,000 for an employee in the top of the coin sorter, and it figures out what goes to the government, what goes to health insurance, what goes to your 401k, what goes to you. And it has to move all that money very, very reliably and seamlessly, very challenging software to build and manage. What's it doing? Even that is just flipping bits in a database. And so AI is a new way to flip bits. AI is just a new way to flip bits. Hopefully a way that abstracts us a little bit further from having to think because our future is Wally. It's going to be great.

Lenny Rachitsky (01:21:57):
Speaking of Wally, actually, I have this Matic Robot. You have one of these?

Matt MacInnis (01:22:04):
Uh-huh.

Lenny Rachitsky (01:22:05):
No. It's like a self-driving car robot, basically, a self-driving car. People built this robot that cleans your house. Maybe I didn't mention that. It's like a house cleaning robot that just goes around.

Matt MacInnis (01:22:15):
Oh, okay.

Lenny Rachitsky (01:22:15):
It's like a Roomba. You should have one. They're expensive, but incredibly cool. And actually in Wally, there's a scene where they actually have basically what these things look like. So it's not so far-fetched for that movie.

Matt MacInnis (01:22:26):
I definitely was actually quite prescient, perhaps with the exception of the gravity defying day beds.

Lenny Rachitsky (01:22:33):
Yeah. I don't know, but that's not good news. You've seen that movie. Oh, man. So on this AI stuff, which I'm hearing is we're going to see a lot more consolidation where these point solution companies realize they need this data. This is existential, and they're going to combine and merge and bundle, as you described?

Matt MacInnis (01:22:51):
It's possible.

Lenny Rachitsky (01:22:52):
Or for now.

Matt MacInnis (01:22:52):
I am not an investigator on this stuff. I think there's some really interesting investors out there who I think are thinking quite deeply about this. And in particular, the conviction, which is like Mike Fornell and Sarah Guo. I think those are two investors who are hyper focused on AI. And when they made the decision to take that approach, at the time I thought that's kind of narrow. Now I'm like, no, no, no, that was the right move. And it just means that they have a very deep, deep, deep set of hypotheses that they've formed over the course of seeing every AI deal in the valley. And there are better people to ask this question of than I am. And I think if you're an entrepreneur, I recommend them to you because I think they're really smart.

Lenny Rachitsky (01:23:35):
Awesome. I love those guys. Also, Sarah and Elad have a podcast called No Priors that I'd also recommend. We'll point it to you in the show notes. So on this AI note, I guess is there anything else that you think would be really helpful for founders that are working in this space building an AI startup to hear they think you were seeing of like, here's what you need to do to win in an AI company?

Matt MacInnis (01:23:58):
So much. I actually think that if I were to give you an answer to this question right now, it would be bullshit. Yeah. I don't have anything ... Back to my point earlier, I don't have enough relevant experience in the abstract to dole out on a podcast on that topic, but I wish them luck.

Lenny Rachitsky (01:24:17):
I love that. Circling back to your advice, don't ask for advice, ask for a relevant experience. And I love that that's where your mind immediately went. I'm going to take us to AI Quarter, which is a recurring segment on this podcast. And the question is just what's one way you've found AI to be useful in your work day-to-day? Is there something that you found it unlocked in how you work?

Matt MacInnis (01:24:37):
I mean, it's not a super exciting thing, but I'll say where I use ... So one of the most important functions that I perform as an executive is the synthesis of ideas, and the ability to communicate those ideas very clearly to people. So when I talk about the product quality list and the pickle, as something that we've come up with internally, I do turn to AI, ChatGPT and Gemini, where I take a really, let's say, angular view of some topic and I give ... really, I write the essay for the AI and I'm like, "Look, this is the crisp idea I want to communicate. Help me come up with pithy ways to articulate these things." And 80% of what it outputs is trash. It's just sort of middle of the road, average, low alpha junk.

(01:25:24):
But it is a thought partner, a non-judgemental thought partner where in 20% of the stuff it comes out with, I'm like, yeah, it's pretty good. That's a new word I didn't think of. That does kind of hit the nail on the head for this concept. And so if I believe that my job is to sort of bring brains along on the journey for some sort of change that I'm trying to bring about, then the most important tool is language. And I do find that the ChatGPT and Gemini do a great job of helping me refine how to articulate the concepts that I want to articulate. They are not useful in coming up with the ideas themselves.

Lenny Rachitsky (01:25:59):
That's an awesome tip. I don't know if you've played with Claude much, but I actually find Claude is better at writing and words and language.

Matt MacInnis (01:26:05):
I have not spent a lot of time with Claude. I have used it, but by virtue of this conversation, I'll probably go give it a go.

Lenny Rachitsky (01:26:12):
Right. Yeah. They're all great, but there's something about Claude that is just at writing specifically is much better, but they're all getting better all the time. There's always something new.

(01:26:23):
Matt, we've covered so much ground. We've touched on everything I was hoping to touch on. Before we get to our very exciting lightning round, is there anything else that you were hoping to share or anything else you wanted to touch on or leave listeners with?

Matt MacInnis (01:26:34):
Yeah. We've spent a lot of time talking about intensity and the grind, and the need to just always be operating at the 99th percentile. And I think if you listen to that in a vacuum, it's very easy to believe that that intensity is soul crushing, that it's a negative, that it's maybe not something that you want. And I think there's a backstop for me that I didn't talk about today that I think is important to share, which is that life is amazing. That the fact that we all exist on this blue marble drifting through space and time, that we are some weird instantiation of consciousness, each of us, and that you're here for such a short period of time whittling your stick, doing something, that if you remember how insignificant we are and all of this is, it brings this levity to what we do and to the work we put into building this.

(01:27:47):
Because Silicon Valley in 2025 is Florence and the Renaissance. It's crazy. The amount of creativity and insane invention and progress that's happening for our species right now in this place is absolutely unparalleled in all human history. You've got to zoom out and appreciate that magic. And so then you turn around and you're like, fuck, I've got to work on Friday night, right? I've got to go give it my all. I've got to go compete in the arena of business.

(01:28:22):
You have to never forget that number one, none of this matters. And number two, it is an absolutely beautiful and amazing phenomenon that we get to be alive doing this right now. So play the sport, play it with everything you've got, but never forget that it's just a sport and that none of it matters. I think it's super important as a counterpoint to the intensity that we talked about.

Lenny Rachitsky (01:28:48):
That is beautiful.

Matt MacInnis (01:28:50):
I think about Pale Blue Dot, Carl Sagan's whole thing. Just a stunning photograph that literally changed the way I think about who I am as a person when I saw it. Yeah.

Lenny Rachitsky (01:29:02):
Well, going in a completely different direction, with that, Matt, we reached our very exciting lighting round.

Matt MacInnis (01:29:07):
Okay.

Lenny Rachitsky (01:29:07):
All right, five questions for you. Are you ready?

Matt MacInnis (01:29:09):
Okay.

Lenny Rachitsky (01:29:11):
Here we go. What are two or three books that you find yourself recommending most to other people?

Matt MacInnis (01:29:16):
Okay. Two or three books. You give me a heads-up on this. So one book is Conscious Business. I don't have Conscious Business in front of me because it's actually at the office because we have Conscious Business Reading Club at Rippling. And every member of my current, my product leadership team is going through this right now, Conscious Business, Fred Kofman. It's been used in many businesses, LinkedIn most notably, as a framework for thinking about ... effectively, it's a user manual for human beings. So if you are a leader, a manager, an executive, whatever, particularly younger people in their 20s and 30s who are just sort of getting the hang of being a CEO or a product leader for the first time, this book is absolute fucking gold. It was recommended to me by Bryan Schreier at Sequoia when he was on my board at my previous company. I took way too long to take him up on the advice, wished I had read it sooner. Highly recommend Conscious Business. Changes your life.

(01:30:01):
Number two, Thinking in Systems, Donna Meadows. I always mispronounce her name, Donella Meadows. She died partway through writing this manuscript. Her fellow professors picked it up and finished it for her. It is the best generic framework for thinking about how systems work. You will extrapolate from this book to every aspect of your life after you read it.

(01:30:23):
And then the third is classic 1960s, The Effective Executive. It's an anachronism. It uses weird pronouns for the secretary and the executive. I'll let you guess which ones. But the book itself is so chock-full of simple enduring advice on how to be effective at leading teams. And the good shit is the stuff that's been in print for 70 years, and that's one of them.

Lenny Rachitsky (01:30:48):
Beautiful. I love the first one is you don't have it because you're using it with your team constantly. You mentioned at one point before we started recording, you have eight copies of that book that you just give out to everyone.

Matt MacInnis (01:30:57):
Yeah, and we handed out like candy.

Lenny Rachitsky (01:30:59):
Okay. Is there a favorite recent movie or TV show you've really enjoyed?

Matt MacInnis (01:31:03):
Yeah. So I'm a little embarrassed by this answer, but I'm going to be honest.

Lenny Rachitsky (01:31:07):
Please.

Matt MacInnis (01:31:08):
There's a new series called Heated Rivalry and it's about ... I'm Canadian and I'm gay. So it's about two hockey players. In Canada, rivals between the Bruins and the Maple Leafs, although they don't use those names, who are just heated rivals on the ice. And it's a huge thing that the world is watching, but actually they're secretly in love with each other and they start hooking up. And it's been labeled by the media as smutty but delightful. And I would say that's accurate. So it might not be for everybody, but it is a smash hit right now. It's on HBO Max and Crave, and it's only six episodes. But like I said, a little embarrassing because it's a little chintzy, but it's a lot of fun. It's also really fun to see gay people represented in the media as though they're normal, and it's fun.

Lenny Rachitsky (01:31:57):
And soon to be on Netflix with the acquisition if that goes through.

Matt MacInnis (01:32:00):
Oh, yeah.

Lenny Rachitsky (01:32:00):
It's crazy. Amazing. Okay. Is there a favorite product you recently discovered that you really love?

Matt MacInnis (01:32:06):
My Fellow coffee maker. I love my Fellow coffee maker. It's got an interface that lets you set light, medium, dark roast. It changes the temperature. It blooms the coffee. It tells you how many grams of coffee to put into the basket, slick interface, high quality coffee. It's definitely awesome. And so I have Ashley have one in the office and one at home and one in the garage.

Lenny Rachitsky (01:32:30):
Wow. That is a favorite product. You have three of them in the same cool space.

Matt MacInnis (01:32:30):
Yeah.

Lenny Rachitsky (01:32:35):
Oh no, in the office. Okay.

Matt MacInnis (01:32:35):
Fellow is also a Rippling customer and that's a nice side effect when we get to ...

Lenny Rachitsky (01:32:39):
Have they ever escalated anything to you?

Matt MacInnis (01:32:42):
No. If you're listening and you're from Fellow, I want to hear all your gripes.

Lenny Rachitsky (01:32:46):
Perfect. Two more questions. Do you have a favorite life motto that you find yourself coming back to often in work or in life?

Matt MacInnis (01:32:51):
It's a dark one, and I'll share this one sort of partially for the humor of it, but it's actually sometimes useful immediately. At least it's sort of a moment of smiling when it happens. The motto comes from my dad who said, "Matt, nothing's ever so bad in life that it couldn't get worse." And it's like we were going through some shit yesterday at work and we were like, "Fuck, now that happened." And I looked at the CTO and I'm like, "Dude, nothing's ever so bad that it couldn't get worse." And we had a good laugh and continued to brace for whatever might come next. So not exactly uplifting, but fun to use.

Lenny Rachitsky (01:33:26):
No, it is uplifting. I'm an optimist and I find myself thinking that often with my wife just like, "It could be worse. It could be worse than this. " Definitely. It's actually [inaudible 01:33:36].

Matt MacInnis (01:33:36):
And it might get there.

Lenny Rachitsky (01:33:38):
So let's enjoy this less worse version. Final question. Something you shared with me is that you were a DJ when you were a younger person. Can you just give us a little DJ voice to give people a sense of your skills?

Matt MacInnis (01:33:52):
Well, so first of all, it's not DJ, Lenny. It's radio personality. And yeah, I used to do the greatest hits of all time with hits from the '60s, the '70s, the '80s, and a little bit of the '90s, 101.5 The Hawk. Yeah. You can turn it on. It's very inauthentic, but it sounds good on the radio. It's cool. I did it when I was in high school. I ended up doing the midday segment right before I went to college. And what a gift. What a huge gift in my most formative years to have developed an ability to be in front of a microphone comfortably, because here we are.

Lenny Rachitsky (01:34:28):
I love for people that weren't watching this YouTube, you lean really close to the mic to get that radio personality voice.

Matt MacInnis (01:34:34):
Yeah, you got to be able to hear the saliva in the mouth.

Lenny Rachitsky (01:34:38):
Incredible, and it's like the same person talking. If you're not watching this, you're like, "Where did that guy come from?" That was great. You nailed it. Matt, this was incredible. I really appreciate being here. I really appreciate you sharing all this advice that I have not heard other people share. Two final questions. Is there something you want to plug, point people to, and how can listeners be useful to you?

Matt MacInnis (01:34:55):
Look, my life is rippling. I point people there, and this is my life's work. It's going to be a banger, so stay tuned. And the way that you can help me is that if you're a customer, you got to tell me when you have problems, because that's how we get better.

Lenny Rachitsky (01:35:10):
What's the way to get to you? Is there any place you want to point people to?

Matt MacInnis (01:35:13):
DM me on Twitter, is easy @stanine. You can email me my last name at rippling.com, and I'll go that far without giving out my phone number. How's that? Perfect.

Lenny Rachitsky (01:35:25):
A perfect boundary.

Matt MacInnis (01:35:26):
Yeah.

Lenny Rachitsky (01:35:27):
Matt, thank you so much for being here.

Matt MacInnis (01:35:29):
It's my pleasure. Thank you for having me, Lenny, and congrats on all the success with this podcast. It's been great.

Lenny Rachitsky (01:35:34):
Same to you. It's always a good sign at the end of a conversation when you're like, oh, I got to get me some of that stock and I got to get into that Rippling.

Matt MacInnis (01:35:41):
It's a good buy.

Lenny Rachitsky (01:35:41):
A great job.

Matt MacInnis (01:35:42):
Recommended by-

Lenny Rachitsky (01:35:43):
15 billion.

Matt MacInnis (01:35:44):
Yeah, but you're [inaudible 01:35:46]

Lenny Rachitsky (01:35:45):
You're hard to get [inaudible 01:35:46] All right, man. Thank you so much.

Matt MacInnis (01:35:50):
Thanks.

Lenny Rachitsky (01:35:52):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

