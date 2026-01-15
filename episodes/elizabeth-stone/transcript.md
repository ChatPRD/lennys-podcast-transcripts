---
guest: Elizabeth Stone
title: How Netflix builds a culture of excellence | Elizabeth Stone (CTO)
youtube_url: https://www.youtube.com/watch?v=2XgU6T4DalY
video_id: 2XgU6T4DalY
description: 'Elizabeth Stone is the chief technology officer of Netflix. She previously
  served as vice president of product data science and engineering, and as vice president
  of data and insights, at Netflix....

  '
duration_seconds: 4424.0
duration: '1:13:44'
view_count: 220414
channel: Lenny's Podcast
keywords:
- retention
- metrics
- roadmap
- user research
- iteration
- experimentation
- analytics
- conversion
- hiring
- culture
- leadership
- management
- strategy
- mission
- competition
---

# How Netflix builds a culture of excellence | Elizabeth Stone (CTO)

## Transcript

Elizabeth Stone (00:00:00):
We can't really have any of the other aspects of the culture, including candor, learning, seeking excellence in improvement, freedom and responsibility if you don't start with high talent density. And in some ways, it's very reflective of Reed Hastings as founder of Netflix. So when he founded Netflix and grew the company over time, it was with a belief that there could be a different approach to building a company that would make it a place that people thrived in and loved being and would feel different than other places, both in the quality of that talent density, but even more importantly, the excellence and the outcomes. And that that's where people would derive a lot of sense of fulfillment. So it is very deeply seated at Netflix from its original days. And in order to do that, you have to really hold yourself to a lot of stuff that doesn't feel like natural human behavior.

Lenny (00:01:06):
Today my guest is Elizabeth Stone. Elizabeth is chief technology officer at Netflix, and as far as I can tell, the first economist to ever be named CTO at a Fortune 500 company. Prior to this role, Elizabeth was vice president of Data and Insights. Before Netflix, she was vice president of science at Lyft, COO at Nuna, a trader at Merrill Lynch, and an economist at Analyst Group. In our conversation, we cover a lot of ground. We talk about how an economics background has helped Elizabeth in her career and why she expects to see more economists rise in the ranks of tech companies. She shares some of her secret sauce for rising so quickly at so many companies so consistently. We delve into Netflix's very unique culture of high talent density, radical candor, and freedom and responsibility. We also talk about the structure that Netflix has for their data and user research teams, which she believes is a part of Netflix's secret to success. We also get into what biking and triathlons have taught Elizabeth about life and how she brings that into her work and so much more.

(00:02:08):
A huge thank you to Ali Rao for introducing me to Elizabeth. If you enjoy this podcast, don't forget to subscribe and follow this podcast in your favorite podcasting app or YouTube. This helps tremendously and I really appreciate it. With that, I bring you Elizabeth Stone after a short word from our sponsors.

(00:02:26):
This episode is brought to you by Vanta. When it comes to ensuring your company as top-notch security practices, things get complicated fast. Now you can assess risk, secure the trust of your customers, and automate compliance for SOC 2, ISO 27001, HIPAA and more with a single platform, Vanta. Vanta's market leading trust management platform helps you continuously monitor compliance alongside reporting and tracking risks. Plus, you can save hours by completing security questionnaires with Vanta AI. Join thousands of global companies that use Vanta to automate evidence collection, unify risk management, and streamline security reviews. Get $1,000 off Vanta when you go to vanta.com/lenny. That's V-A-N-T-A.com/lenny.

(00:03:18):
Let me tell you about our product called Sendbird, the all-in-one communications API platform designed for both web and mobile apps. In a world saturated with multi-channel communication, product teams are discovering the effectiveness of in-app communication. With Sendbird, businesses can elevate their in-app experience with decluttered and branded communication featuring AI powered chatbots, one-way messages, chat, video calls and livestream capabilities all tailored for commerce, marketing, and top tier support. Forward-thinking companies such as Hinge, Patreon, Yahoo!, Accolade and more use Sendbird to build in-app communication experiences that drive engagement, conversion and retention. In-app communication has the highest conversion, highest engagement, and highest satisfaction of any communication channel. And when it comes to investing in this channel, trust Sendbird to take your in-app communication experience to the next level. Start today with Sendbird's free plan. And as a listener of Lenny's Podcast, you'll get an additional two months of unlimited usage and access to all premium features including creating your very own generative AI chatbot. Visit sendbird.com/lenny to begin your free journey. That's sendbird.com/lenny.

(00:04:36):
Elizabeth, thank you so much for being here and welcome to the podcast.

Elizabeth Stone (00:04:41):
Thank you. Thank you for having me.

Lenny (00:04:43):
So when we booked this conversation, you are VP of data in Netflix. And since then you got a promotion, you're now the CTO of Netflix, which feels significantly more fancy. Question for you, what is life like now that you are CTO versus VP of data? How is it most different? I'm imagining more meetings.

Elizabeth Stone (00:05:01):
I would say the biggest thing that changed is probably the amount of context switching and the degree to which I feel behind or I have a lot to learn. And I felt like I had a lot to learn in the VP of data and insights role that I was in before in part because we cover a lot of different areas of the business and there's always people to learn from, but the engineering organization just takes that to 100 basically. So more people to get to know, more problem spaces, aspects of technical expertise that I'm just not as deeply familiar with. And yeah, a lot more meetings.

Lenny (00:05:41):
I imagine many higher stakes meetings as well.

Elizabeth Stone (00:05:44):
Yes. So thankfully not a lot of meetings that Netflix feel like now you're really in this scary room, but it does feel like the role has more consequence, which is actually an exciting thing.

Lenny (00:05:57):
Kind along the lines of what you just talked about being a CTO. Your background is actually unusual. You're a trained economist, you got a PhD in economics. And from what I can tell, you're the first CTO of Fortune 500 company that is an economist trained in economics. First of all, is that true? I don't know if I think that's true, but you tell me.

Elizabeth Stone (00:06:16):
I have not checked the list. That was one of the things I did not do after getting the title. It might be unusual. I've heard a lot of feedback on that, so I don't know if I'm the one and only, but I will definitely say it's probably unusual.

Lenny (00:06:30):
Yeah. So I guess the question is just, do you think this is an anomaly and going to continue to be really rare? Do you think this some are going to see more at tech companies? And generally do you think tech companies should hire more economists?

Elizabeth Stone (00:06:41):
Yes to the last question. That's the easiest of it. But one of the things I observed even with the focus on data science where I've been deeper for a period of time is that economics is a flavor of data science. So it is a set of technical skills for sure. It's a way of framing certain problems or solving challenges.

(00:07:06):
And so when I was first switching from economics into tech, it was before there was a lot of sort of the frenzy around data science that we've seen more recently and it was harder to make that argument that economics is a flavor of data science and maybe complimentary to other versions of data science. And I feel more strongly about that now that I've seen it up close. And so maybe by extension I would say just like I think data science can be helpful for a lot of different problems that you might not immediately think, "Oh, this is something that we should bring data to," I think that economics is generally valuable for a lot of different challenges and it's a useful perspective to add to things, especially in a business context and especially in how we want to simplify problems in a way that makes them feel tractable.

(00:08:00):
So I feel like that's been a benefit to me to have had that type of formal training and then bring that perspective or way of thinking to different roles. And so I don't know that many people at Netflix think of me as an economist, but I find it comes out in the way I think about things. So to the extent that that's true generally, I think it's useful in a lot of companies. And I feel like even since I made the switch towards tech, I've seen it become much, much more common to think about the value of having economists on teams.

Lenny (00:08:32):
Just to pull on that thread a little bit more, is there something very tactical or concrete that you can share that you find helpful with that background that you found helpful in your career?

Elizabeth Stone (00:08:42):
Other than the dismal dry science of it all? So one example would probably be in an understanding incentives and thinking about unintended consequences. I think that that is true both in terms of internal leadership, so being part of a management team that's thinking about how do we clarify priorities or motivate a company or define the problems we want to solve. And then part of it is more externally oriented. How do we want to think about what Netflix is to consumers and how we want to think about competition?

(00:09:24):
There can be a rational way of thought, which is one version of economics of shouldn't rational intelligent people behave in the following way. And then there's the, well, if given certain incentives, what might you see that we didn't think was optimal or we weren't expecting to happen but could be a consequence or repercussion here? And so I think that that type of framing, I don't know if it's unique to economics in a way because it has elements of psychology to it as well and planning ahead has become really useful for thinking through cause and effect. So that has come up in a lot of different spaces in Netflix and in other roles I've been in.

Lenny (00:10:08):
I was looking at your LinkedIn and looking at your career over the years. It seems like you've had a meteoric rise at four different companies. And I'll just walk through them briefly. So at your first job, you went from associate to vice president in three years. At the next company, Nuna, you went from manager of data science to COO in two years. At Netflix you went from VP to CTO in three years. I think that's really rare. I'm curious what is your secret sauce to being so successful at so many places and especially in the context of what advice can you share with folks earlier in their career?

Elizabeth Stone (00:10:46):
This is one of those questions that sparks the reflection that I wouldn't normally do, so that's great. I really don't think of it as a secret sauce, but maybe I can walk through some of the things that I think have been instrumental. As you listed that out, it sounds like the two to three year point is the real sweet spot, so maybe there's something about that timeline. But I think some things almost feel trite in how I would say them, which is I'm very dedicated to the work and to the teams I'm part of. It's been part who I am for a long time that I give everything I've got to the job that I'm in. And I think that dedication and that I get joy out of that has mattered. It matters because I enjoy what I'm doing. I do the best work I possibly can, less so for myself and my own ambition and more so because I think of myself as being part of a team and so I really need to deliver for that team.

(00:11:52):
I think that framing in my mind and that motivation has helped me in a few fronts, which is the way in which I build partnerships with people I work with that I really care about setting other people up for success and being someone that people want to work with, so I learn from them, they learn from me, and we get better outcomes for the business together, I have found that part of that is being someone that people can leverage to translate from technical to non-technical and non-technical to technical. So that I do think has been a relative advantage in my role. So while I was often sitting in more technically-oriented teams, a lot of the advancement in my career was to roles that required that type of communication fluency. It grew out of being able to partner with people across the businesses who didn't necessarily have the same background, but where we needed to really connect spaces so that we could be more effective.

(00:12:57):
That was something that I think really the training for that came from analysis group where it was a very quantitative set of work that we had to find a way to communicate to judges and juries for economic cases. So that was something that was trained in other roles and I think I've been able to leverage. I'm a relatively introverted only child, so I observe a lot, which means that I learned from other people. And in each of these roles I have tried really hard to watch what other people are doing, think about how could I learn something from them, whether it's the thing that I want to be able to do myself or it's the thing that I think, "Oh, that doesn't quite fit or feel authentic with my style." And I do a lot of that introspection. So I have been surrounded by amazing people in all these roles and I have a feeling that I learned a lot by osmosis and observation and then have been able to leverage that to be stronger in the roles I was sitting in.

Lenny (00:14:00):
I took a few notes here. A few things you mentioned is just like, dedication, essentially working really hard and taking your work seriously, being part of a team and setting other people up for success, translating complex tech language and problems to non-tech people, and then being really good at observing and learning from other people around you. Is there an example or two that you could share of some of these to make it even more concrete for people? Like dedication. Is that just like working many hours, being part of a team? Anything along those lines to share a story maybe to help people put this into practice.

Elizabeth Stone (00:14:35):
No, and it's a good clarification because the dedication piece really isn't about long working hours. It's more about how much I care about excellence, I guess. So giving it my best in those situations. And that might not mean that I work really wild hours or I work weekends or I'm the one who's willing to sacrifice the vacation. I've actually tried to avoid setting that as an expectation, but more that I hold myself to a very high standard.

(00:15:13):
So an example would be, especially as I've gotten more senior in roles, there can be an expectation that it's okay for other people to wait on me. So whether it's the timing for a meeting or providing input on something or reviewing a document or following through on something I said that I was going to do, and I really try to avoid that, which means that if someone sends me something, I try to be very responsive about it. If I know that I said I'm going to do something, I follow through on it in the timeline that I said I was going to do. If I have a meeting, I try to be on time to that meeting.

(00:16:01):
Those are all flavors of dedication to the work that show up in, "Oh, it seems like Elizabeth works really hard," but the motivation factor is other people are relying on me and I want to show up for them. And so that's when I say dedication and it's related to the second point around showing up well for the team, those would all be examples of I feel urgency in responding to people and doing high quality work.

(00:16:27):
For the other parts of technical to non-technical, I think a great example is actually a very timely one at Netflix, which is, we are making strides to offer live content types. So live events, live TV shows. We announced this week that we're going to be hosting WWE starting later this year and early next year, 2025. That is easier said than done. I know that there's a lot of entertainment companies that have live content. But Netflix has really been in the streaming content business, so live content is something new for us and it's something that's going to require a really close partnership between our content organization and our products and technology organization because there's a content strategy to it, there's a business strategy, there's a technology strategy to it. A big part of my role is, can I explain how we're going to approach those technical problems in a way that builds competence with the content team? Can I try to understand their content strategy in a way that sets the technical teams up for success and we understand what we need to be able to deliver on here in terms of requirements.

(00:17:46):
I don't think I'd be able to do my current role well if I wasn't able to do that type of translation for something that's going to be a big bet for the business and something we want to invest in jointly. And then to set my partners up for success in that. So I am going to do everything I can to make sure we deliver well for my content partners because I feel like that's what's best for Netflix in the business.

Lenny (00:18:09):
Amazing examples. In terms of life content, I think about the Love is Blind. I think it was for premier, whatever, reunion that we got sucked into that show. So good job. And I think there were some issues with that, right? That reunion streak.

Elizabeth Stone (00:18:24):
Well, yeah, that was about a little less than a year ago now. So the amazing thing about failure is you learn a lot. We learned a lot. We've taken notes on it and we had a couple successful events after that, including the Netflix Cup last October. And we've got some exciting events coming up. So I think that's something that strengthened us, but did reveal that we're tackling a hard problem.

Lenny (00:18:50):
Yeah, the Twitter feeds during that, Love is Blind premiere were hilarious. People are pissed.

(00:18:57):
Okay. And then in terms of the, keeping a high bar for yourself, I love that. I think about a quote that... There's a VC, Ann Miura-Ko, at Floodgate and she did this interview with Tim Ferris. She shared that her dad always asked her, "Are you doing a World-class job with this? Are you doing a world-class job with your homework? Are you doing a world-class job with your piano recital?" And that's the bar that he always had for her. And I feel like that's a really good way to think about work and life in general if you can.

Elizabeth Stone (00:19:28):
Yeah, my mother used to describe to me, probably still does, though it required more repeating when I was younger, that the last 5% is the 5% that really mattered. And so it is that framing of the extra effort you put into something to make it world-class or to make it excellent. And so I do like to push myself that way and I hope it sets a good example for other people too. It's very consistent with especially the company cultures that I tend to thrive in where that's the general expectation of the culture. So you don't feel like you're doing it alone, because then I think you can start to feel frustrated by that.

Lenny (00:20:15):
I know that this is a big part of Netflix culture and I want to get into it. But before that, I'm curious just what that looks like with people that report to you. How do you help them level up in this skill of having a really high bar? And an example I'll give as you think about maybe an example is the way I described this to my PMs was, you want to have this aura that you've got this that, "If you give Lenny something, he's got this. He's going to follow up, he's going to close the loop, he's going to get it done. If he can't get it done, he'll tell me, I feel like this thread will not disappear. He won't drop this ball." Is there anything that you've learned as a good way to help someone learn this kind of skill, understand why this is so important?

Elizabeth Stone (00:20:53):
It shows up for the people who report to me, is one part example setting. So if I don't do it, why would they do it? I treat that very seriously that we should all be held to the same standards.

(00:21:12):
And as a second thing, I give feedback when it's not up to the standard. So I think one of the things I've observed especially with people on my teams is that the expectations aren't always clear and you can't assume that they're clear if you don't share them. When something's not meeting expectations or really showing up as excellence, I think it's a combination of both giving the feedback on that and being direct about it and being specific about what would it take to get this to the bar that I am expecting or to show up in the way that I'm expecting.

(00:21:55):
And then the third and probably most important thing is help them fill that gap. So that would mean... Let's take an example. It certainly has happened frequently in many jobs. A document is okay, it's not great, it's not going to be easy for people to follow, it's not as crisp as it could be. There's things that would strengthen it. I can both give the feedback on that to make sure like, yes, it's going to take another round of iteration, yes, we're going to have to work another week on this and not be done with it, but pushing people to get there, and then jumping into the document and helping.

(00:22:32):
So I feel very strongly about, and that's kind of what I mean by setting an example of like, "Let's work on this together," and then through that, help people uplevel themselves so the next time around they know the expectations and they've had help getting there in the past. So that's probably happened a thousand times in my career where I jump in with both feet because something needs to be better and I think the teams are better for it afterwards, or I hope they are.

Lenny (00:23:00):
I think that's such a good framework just to kind of mirror back what you said, "Set expectations that the bar is going to be really high and here's what I'm expecting from you." Give them very specific feedback on where the gap is and then help them fill that gap. I think a lot of people may feel this and hear this and they're like, "Oh man, I don't want a manager that's like this high of an expectation person and it just feels really stressful." But I've had these managers and I feel like that's when I've learned the most and leveled up the most, is having someone that had really high expectations and then helped me understand, "Here's where you're not doing as well as you can. I know you can do better. Go back and work on this." I know that sounds annoying, but I think in practice it ends up helping you most in your career. I imagine you've seen a similar result.

Elizabeth Stone (00:23:45):
I think so. I mean you'd have to ask some of the people on my team. So I might look at it differently that they look at it.

Lenny (00:23:51):
[inaudible 00:23:52] differences.

Elizabeth Stone (00:23:53):
It's a hard skill because it's not always easy to give feedback, especially if you feel like you know someone's put a lot of effort into something. And so I give a lot of thought to how I deliver that feedback so it feels like we're on the same team and I'm trying to help them be successful, not to help encourage failure. And that's where I think that third piece of the framework of jumping in to help can make people feel like, "I'm in a safe space. My manager wants me to be successful. My manager's helping me here." I do often do that behind the scenes. So maybe that's another flavor of this, which is, I don't do it live in the big meeting in front of all the people where the presentation doesn't go very well. I do it afterwards where it feels like a safer space to say, "Here's a way this could have gone better. Let's think about this differently next time." So it gives people a little grace and a little bit of an ability to absorb that feedback without feeling like it's kind of on a stage.

Lenny (00:25:02):
Another thing someone may be feeling when they're hearing this is like, "Oh my god, it's going to take me so many hours to just get it to a place Elizabeth is happy with." And I know you said that this doesn't mean necessarily many hours. Do you have any advice or thoughts on just how to avoid burnout and working all the time, but also keeping this really high bar and high expectations?

Elizabeth Stone (00:25:21):
It truly is not about time. I even found myself in a meeting earlier today saying, "If we're clear on the objectives of something, it might be that the last 20% of polish on the document is a really bad use of time. So if we're going to come together to talk through..." Like quarterly business review was the example, what were the highlights? What were the low lights? What were the learnings from the quarter? Where are there places of misalignment? The reason we're doing the quarterly business review is to have a really candid conversation about how we think things are going, to have a debate about things where maybe we're stuck. It's not to have a perfectly polished document for that conversation.

(00:26:08):
So my feedback in that instance would be, I would much rather have someone spend the time thinking about what's the conversation we really want to have? "How do I tee that up?" Not, "Could I spend another 20 hours to make it look like everything's perfect in this document?" And so I think in that sense it's not just excellence, like you wrote the perfect document, I should probably be careful to not use that as the only example, but instead we really got to the outcome we wanted to get to because we were thoughtful about it and we put a lot of energy and time and iteration into making sure we got to that outcome.

Lenny (00:26:43):
And is this an example where you gave someone feedback that they spent too much time on the polish or is this earlier? And to give the pyramid of this framework you kind of shared of set expectations, give specific feedback, help them fill the gap and then do it in private, is this the expectation setting in this example or is this feedback you spend too much time on this?

Elizabeth Stone (00:27:01):
This is expectation setting. So one of the things in my new role is that there's some practices that the team has had where they're trying to understand, Are we still going to have those practices? What's going to be the same versus different about those things?" and get an understanding of my expectations. So it's great that people ask that question so that I can be clear about, "Oh wait, if you're on the last 20% of this polishing the dock, I'd rather spend time over here. And here's how I would like the conversation to go so we all get something out of it instead of it feeling like it's just a leadership reviewer on my behalf." So in this specific situation, it was setting expectations ahead of time so that we can set everyone up for success.

Lenny (00:27:44):
Awesome. Okay. So we've kind of been talking around this, but this is an important part of the Netflix culture. Just broadly, Netflix has a really special and unique culture. Even though it's been around for I think over 25 years now, it feels like the culture has come up many times. There's that initial culture deck that came out that blew everyone's minds. There's a recent book, No Rules Rules I think it's called. And it feels like Netflix has done a great job at maintaining its culture.

(00:28:10):
It feels to me there's these three important elements, and maybe there's more. One is very high talent density and a focus on high performers. Two is candor and being really direct. And then three is giving people freedom and responsibility and getting rid of useless processes like vacation time and things like that. So maybe just to dive into that first one of high talent density and this focus on high performance. I guess the question there is just like, what does this look like in Netflix? And I imagine part of it is hiring, part of it is performance reviews. And then just why is it so important? Why is this such a focus on Netflix? What happens when you have such a high talent density?

Elizabeth Stone (00:28:51):
It's just so intrinsic to who Netflix is as a company. And in some ways it's very reflective of Reed Hastings as founder of Netflix. So when he founded Netflix and grew the company over time, it was with a belief that there could be a different approach to building a company that would make it a place that people thrived in and loved being and would feel different than other places, both in the quality of that talent density, but even more importantly, the excellence and the outcomes and that that's where people would derive a lot of sense of fulfillment. So it is very deeply seated at Netflix from its original days.

(00:29:37):
A big piece of that talent density is definitely hiring. So who are the people coming in and joining the team? But a lot of it is, we can't really have any of the other aspects of the culture, including candor, learning, seeking excellence and improvement, freedom and responsibility if you don't start with high talent density.

(00:30:03):
And so in some ways it's not the end, it's the means to the end in what Reed and the rest of the leadership team has been trying to build. And so in order to do that, you have to really hold yourself to a lot of stuff that doesn't feel like natural human behavior. What I mean by that is giving the feedback, this gets into the second bucket. So giving feedback, being candid around your expectations when they're not being met, what could be better in helping people improve, and be able to receive that type of feedback yourself in order to keep talent density high? Because no one comes to Netflix as a perfect human being and stays a perfect human being the whole time. We all have ways that we could grow and improve. And so in order to keep that bar high, you have to be willing to have those types of very uncomfortable conversations. It's an uncomfortable amount of candor and feedback in order to keep that bar high.

(00:31:10):
And then the other piece of it is another thing that doesn't come naturally to humans, which is making a call in pretty timely fashion if someone's not able to meet the bar, and to say either, "I don't think the role you're sitting in is the right role, or I don't think that Netflix is the right place for you," and to make that something that is part of best practice to get to a point where you could make that decision. And that's where we refer to the keepers test, which is really just a mental framing to make sure we hold ourselves accountable for this. Where if I'm asking myself the question, "If this person on my team came to me and said, 'I'm leaving today. I have a different opportunity and I would like to take it,' would I do everything I could to keep them at Netflix?" If not, then I should be having that tough conversation about, "Should you really be here? Are you in the right role?", if I might be a little bit relieved if you said you were leaving.

(00:32:20):
The reason the keeper test and that question is useful is because no one wants to think that way. It's very hard to say to someone, "I think this isn't the right fit. I think you should move on from the company." So we have to introduce some of those reflections in order to encourage the behavior. And we also then want to get to a place where when you're having that tough conversation, people aren't surprised by it. That is easier said than done. But you can only get to that conversation around, "I don't think Netflix and you are the right fit for one another" if you've been giving feedback along the way. And so it feels like in its most ideal state, it's a mutual observation. In practice, it's not always that smooth. Obviously we are humans. But that all feeds on itself in order to make sure that we're really holding ourselves to what we say our behavioral norms as part of the culture.

Lenny (00:33:17):
How is that operationalized? Is that just mental model that you should have in mind? Or is it like every quarter you should go through this exercise? Is it part of the performance review process? How does that actually operationalize at Netflix?

Elizabeth Stone (00:33:29):
It's definitely a mental model. So when we talk to managers about what does it mean to be a manager at Netflix, it would mean you should be with some frequency asking yourself this about the people on your team. People ask me frequently, "Am I passing your keeper test?" So it becomes part of a regular manager direct report, one on one. And it is just another way of saying, "Am I meeting your expectations? What's going well? What's not going well? How are you thinking about things?" And that can sometimes be a very awkward conversation to have. So in the middle of a lot of like, "We have to talk about this project or that deliverable or this thing that's happening," to take the time to step back and just say, "How am I doing?", can feel loaded sometimes. And the keeper test, while it feels like a very heavy concept, creates a lightness around being able to have that conversation regularly. So we do operationalize it. A point that you made, I'll just clarify, we don't have performance reviews.

Lenny (00:34:33):
Oh, wow.

Elizabeth Stone (00:34:34):
So we don't have a practice that a lot of other companies do where we would think about reflecting on a rating of how things are going. We do have an annual cycle of 360 feedback where you request and receive feedback from a lot of people, but it's not an input to some output, it's just for the value of the feedback and to make sure we're keeping that muscle. And we have an annual compensation cycle where we reflect on how are people doing? And so you think about performance as part of both promotions and as part of compensation, but in that way it has to be part of the day-to-day and part of the operating rhythm because we don't create a process where that would come to the surface.

Lenny (00:35:20):
Interesting. I didn't know that. So the idea there is just ongoing, like the whole... So what many people dream of, no performance reviews, we'll give you ongoing real-time feedback. We don't have to wait six months. I feel like people talk about this but rarely do this, but that's how you guys operate.

Elizabeth Stone (00:35:36):
In ideal.

Lenny (00:35:37):
In ideal, yeah.

Elizabeth Stone (00:35:38):
In practice. It's like you have to keep reminding yourself, "This is our ideal" because it's really easy to rely on the annual 360 cycle. And all of a sudden I do get about 300 pieces of feedback. And some of those things are on things that happened six months ago and I think, "Oh, I wish you had told me this at the time, that would've been more living the Netflix culture." So we have to push ourselves to do it that way. But yeah, that is if working well, it's very timely direct feedback. The 360 site goal is sort of the annual check-in on, "Let me get the full picture. Let me be able to distill some themes. Let me tee it up for a conversation with my manager." And then it does remove the sort of crutch of an every six month performance review or something like that.

Lenny (00:36:31):
When you talked about this example of someone asking you often, "Am I meeting your keeper test?", it makes me feel like someone's just super nervous. They're like, "Am I passing your keeper test?" And it makes me feel like it could create a culture of just like a lot of stress and worry and this hunger games mentality of like, "I got to compete and worry and I might die or get fired any day." I'm guessing the solution to that is partly cultural. This is just the way we work. You don't need to stress all the time, but you may be let go if you're not meeting this keeper test. How do you avoid this just constant worry that you might be fired any day and that you may not be hitting the bar?

Elizabeth Stone (00:37:08):
In my personal experience, I have felt a lot more at ease by having these conversations than by not having them. So in many roles I've had, I haven't been sure how I was doing or things I could be doing better on, and I didn't quite know how to get that information. And that made me feel much more stressed or nervous or at risk than having it be part of the culture to have those conversations.

(00:37:45):
So the thing that I think can be nerve wracking, and I feel it myself, is the high bar for excellence at Netflix and if we're doing this while you're surrounded by amazing people. And that can feed a sense of, "Am I doing well enough compared to how everyone else is doing? I know the bar's high." For the most part, that can drive people and in a good way, but in some ways it makes people nervous. And that's where I think it's helpful to know we expect to have these conversations so you can just kind of let your shoulders relax a little bit of, "Yes, the expectations are high, but my manager says I'm doing a great job, or my manager says I'm not doing a great job, but they gave me concrete things that I could do better." And so I think knowing is better than not. And so in that sense, it's the culture combined with the conversations around performance I hope take a little bit of that stress out of it. But I've certainly heard it a lot that without that conversation, people can be nervous.

Lenny (00:38:49):
That's such a good point and such a good example that I feel like every company wants to have a high bar and have only high performers and keep the bar really high for every person they hire. I'm curious, I know this could be its own podcast and book, but just in terms of hiring people that are amazing and keeping this bar of excellence, is there anything you can point out that might be helpful to other companies hiring to help identify amazing people and make sure that bar stays high? One thing I know is you guys pay a top market for salary. I think that's one unique thing about Netflix, is we just pay people. So maybe that's an part of this answer, but just what advice do you have for people to keep a really high bar in their talent?

Elizabeth Stone (00:39:33):
Yeah, I mean on the compensation point, we pay what we call personal top of market, meaning we want to be highly competitive in the pay, but we don't want pay to be like the golden handcuffs of Netflix sets market rather than paying people a strongly competitive compensation. So I think that that's important for attracting and retaining talent and has been a big part of the culture, but almost more importantly, we hope we don't have to rely on that to want people to want to be at Netflix or for us to be able to assess whether people are going to thrive at Netflix.

(00:40:20):
The way that I've thought about hiring with that context is we know we're going to offer you very highly competitive compensation, but are you going to come to Netflix and help us identify the right problems to solve or new ways to solve existing problems? And that's a different way of hiring than you might think about, especially at scale where you're saying, "Does this person have this skill, this skill, this skill? Check they're going to fit in this box and they're going to deliver this work that I need them to do." I'm being intentionally simplistic. I recognize a lot of people don't hire actually that way. But at Netflix we try really hard to say we're looking for the new perspective or the person who's actually going to make us stronger as a team. So thinking about additive skills, additive perspectives, people who are going to push our thinking on something. That tends to help us with thinking about talent density because you're constantly introducing people to the team who uplevel.

(00:41:25):
So then the questions you have to ask in an interview might be different because yes, we're trying to assess do you have the baseline skills to be successful here, but we're also looking for the things that make people exceptional or even stronger than the team we've got. And then you think about making the magical teams comprised of all those amazing minds and what can you get out of that. And that feels like more that the talent density and practice.

Lenny (00:41:50):
Got it. So the advice there essentially is, don't look for someone just simply great. Look for someone that raises the bar for the whole team, brings in a whole new perspective.

Elizabeth Stone (00:41:58):
Yes. That's a great way to say it. Yeah, it's a good way to say it.

Lenny (00:42:00):
I think what's great about this idea of just maintaining excellence consistently is that the best people want to work with the best people. And as soon as there's one person that sucks and the company allows for that, it just brings everyone down because they know, "Hey, we can be okay. We'll stick or no one's going to do anything about it." And when you make it clear, we only want the best and only hire the best and only keep the best, it keeps the best there, right? I imagine that's part of the strategy.

Elizabeth Stone (00:42:29):
Yeah. It's definitely the goal. And I think understanding that having gaps in the team and people's skillsets or their behavior can be really toxic for other people on the team. So it's a cost.

Lenny (00:42:42):
This episode is brought to you by Xplo, a game changer for customer facing analytics and data reporting. Are your users craving more dashboards, reports, and analytics within your product? Are you tired of trying to build it yourself? As a product leader, you probably have these requests on your roadmap, but the struggle to prioritize them is real.

(00:43:01):
Building analytics from scratch can be time-consuming, expensive, and a really challenging process. Enter Xplo. Xplo is a fully white labeled embedded analytics solution designed entirely with your user in mind. Getting started is easy. Xplo connects to any relational database or warehouse. And with its low-code functionality, you can build and style dashboards in minutes. Once you're ready, simply embed the dashboard or report into your application with a tiny code snippet. The best part? Your end users can use Xplo's AI features for their own report and dashboard generation, eliminating customer data requests for your support team. Build and embed a fully white labeled analytics experience in days. Try it for free at xplo.co/lenny. That's E-X-P-L-O.co/lenny.

(00:43:54):
So I asked on Twitter what questions to ask you. And there's a great question that came in from Nan Yu. He's the head of product for Linear and he asks, "What practices does Netflix do that other companies should not attempt to do because their talent level is so much higher than other companies?"

Elizabeth Stone (00:44:15):
That is freedom and responsibility in a nutshell. So let me explain that. It's a good question. It's kind of related to what I was saying earlier, that talent density is a prerequisite for a lot of the other ways we operate. So if we want to create a work environment where we are not prescriptive about how people solve problems or the scope of problems that they could tackle, assuming they're highly impactful for the business, and we don't have a lot of process around that work, so think about being able to make large innovations to our engineering systems or introducing new ways to think about metrics and experimentation, we get a lot of those things because we give people the freedom and the space to explore and question things and experiment in a way with solutions. I think that that would be very hard if not dangerous if we didn't have a high talent density.

(00:45:32):
It's really not a top down do A, then B, then C. Even in how we go through some of our planning processes or thinking about how we think about priorities, there is a lot of room for contribution across all levels of the team and that requires talent density. And then there's things like you have to have amazing people if you're not going to have really strict guardrails that would influence the consumer experience or business stakeholders experience. We do give people a lot of responsibility on those things. So I think the lack of process and prescriptiveness is all hinging on we've got amazing people who are smart, but even better have strong judgment.

Lenny (00:46:18):
This is kind of what you always hear from people giving founders advice is, "Just hire amazing people, get out of their way and let them do their job," which is often not a successful experience. What are examples that either things that came out of this freedom, I don't know, products or features or ideas that came out of this or policies or processes you don't have that everyone else might have? So I know there's no vacation time, there's unlimited vacation time, I assume. Is that still a thing? Unlimited vacation time?

Elizabeth Stone (00:46:48):
Yeah.

Lenny (00:46:49):
Okay, cool. All right, great. And I know performance reviews, you talked about that. So I guess in either direction, is there an example of something that came out of this freedom or some process that which surprised people that you don't have or a framework or system?

Elizabeth Stone (00:47:05):
We've been able to deliver... I'll speak to my own team around innovations in our content delivery network or innovations in encoding or innovations in discovery and personalization. We're not driven by some leader saying, "I think this is a priority." They were driven in many cases by individual contributors who had great ideas for innovation. So a lot of the stuff that Netflix has succeeded in, came from creating space for people on the team. So there's probably thousands of examples of product features and things like that that came out of creating this space. And right now, the trick is finding the sweet spot so that we can operate efficiently at this type of scale without snuffing out some of that, what was kind of the core beauty of the culture.

Lenny (00:47:55):
Maybe a last question around just the culture. We talked about candor a bit. I'm just curious if there's an example that comes to mind of an example of candor that you recently saw or had to be the candid person that might be interesting to share where it's like, "Oh wow, that's what you mean when you say a culture of candor."

Elizabeth Stone (00:48:15):
There's a couple things that come to mind. I am generally a transparent leader, meaning I share information freely and openly. It's part of the culture to context, not control, which means part of my job is to make sure that people have the context they need to do their jobs well. And in practice, that means I take notes in leadership meetings and I share those notes with the whole organization. And that is sometimes it includes candor around reflections on things that aren't going well or problems we need to solve. Sometimes it's just letting people know, "Here's what leadership's talking about so that they have a sense of what's top of mind." But it's a version of transparency that I feel strongly about, doesn't exist a lot of other places. I think it's a version of candor too in being able to share... I can't always share every detail of everything that we're talking about, but I do try to share things that probably push the boundary a little bit in the team, feeling like they understand what's happening across the company and what I'm thinking about.

(00:49:22):
And then there's a second example that comes to mind, which is, until two years ago, individual contributors didn't have levels at Netflix. So all engineers were just senior engineers, all data scientists were senior data scientists, and we did not have a leveling system. We introduced IC levels two years ago almost exactly. And it was a big, big, big shift because it was seen as something that was sort of sacred of it. A lot of people came to Netflix because we didn't have it. We didn't have process around promotions. This is probably part of why we never had performance reviews, because promotions really weren't at play. And it gave people a sense of freedom of not having to worry about that type of structure. But when you get to a scale of an organization, we needed some type of scaffolding to say, "We want to talk about how we compose teams. When do we need the person who has 30 years of experience? When do we want to have a new grad?" Because that's what the work requires. We didn't have a language for it.

(00:50:27):
So I introduced Levels a couple of years ago and we had quite a change rollercoaster is the only way I can describe how it went.

Lenny (00:50:38):
That's a good phrase.

Elizabeth Stone (00:50:40):
Yeah, it was sort of like being the tumble dry machine for a few months, and so really talking through it with the team. That's just context and backdrop. For an example of candor recently, which is, we had kind of a postmortem or a retro on how has it gone with IC levels. So it's kind of like wells, not wells. And I would normally think in a lot of cultures it would be like, "Well, we got past that change. We're living that change." Don't reflect on it. Because that kind of opened some of that early debate. And I felt differently about it. I think it's a good example of being candid about, this was a big change for us. It hasn't all gone perfectly. There's a lot that we can do better in how we implement levels at Netflix. And I would rather share that information than pretend it's all gone swimmingly and we achieved every objective. So I think that I try to build examples like that because I do think that level of candor and reflection helps build the sense of community and trust across the team.

Lenny (00:51:44):
That's an awesome example. Kind of along the lines of that, but also this category of freedom and responsibility, something Netflix innovated long ago, and I'm curious if this is still a thing, is this idea of Chaos Monkeys, which essentially are a program that runs on your infrastructure that just kills random processes and things and just to see what breaks and make sure things are stable when things actually start falling apart. Is Chaos Monkeys... Was that what it's called? And then is that still a thing? Is there still some Chaos Monkeys running around the servers?

Elizabeth Stone (00:52:19):
Not unbridled Chaos Monkeys. No.

Lenny (00:52:22):
Okay. Contains chaos and niche.

Elizabeth Stone (00:52:24):
Bur no, we carry too much responsibility, speaking of freedom and responsibility for the member experience to inject pain, though we do do a lot of experiments to test resilience, and that does probably mean injecting things that we're not quite sure whether A is better than B. And so that happens across engineering systems really at scale. But it is not for pure chaos, it's for intentional learning and so we can avoid making bigger mistakes. And then as we go into new efforts like cloud games, we have a beta that's out now, Live would be another example. We do try to come up with intentionally low profile examples where we can test the bounds of our systems in a way that's unlikely to damage the member experience. But that's less randomness, more by design. And so we're doing that in a few places that feels mostly good engineering practice so we can understand when it's really showtime and we're going to really test our systems, will they be able to perform like we want them to.

Lenny (00:53:42):
RIP Chaos Monkey.

Elizabeth Stone (00:53:45):
Yeah.

Lenny (00:53:47):
So kind of along these lines of data, so data itself has always been at the heart of Netflix. My understanding is the way the data team and the insights team is structured has been one of the reasons Netflix has been so successful. And that's the team you led before you moved into this new role. Can you just talk about how these teams are structured and why this structure is so effective?

Elizabeth Stone (00:54:14):
Yeah. I certainly like to think of it as being special. It's unusual. I can explain why. So the scale of company that Netflix now is very often data oriented teams are embedded in other parts of the business. So it could either be they're embedded in a business line like ads or games, or they are organized more functionally separating data engineers from data scientists, from analytics engineers, from consumer researchers. We've resisted that and kept a centralized team that is both functionally diverse. So across all those types of functions that I just described and works on nearly every area of the business from within the team. I sort of understand why a lot of companies move away from this because it really does require basically extraordinary partnership that we would have people working on data problems that don't report into the teams that are relying on them.

(00:55:30):
But the benefit we get is we get to think about our functional expertise. So are we really world's best data engineers, world's best data scientists? And how do we continue to be ever better from a functional and technical perspective? It gives people better career paths because there's more mobility across the teams. It feels like a team that has a functional expertise with a lot of different problems to solve. And so I think it enables more cross-pollination of ideas in a way.

(00:56:03):
It also allows us to be really objective. That is probably the most important thing, that our job is not to tell the story that someone wants to hear with the data or to solve the problem that someone thinks is most important. It's for us to have our own perspective about things. I think that that uplevels the whole organization because it means that we're able to be truth tellers or to be curious in a way that might not fit if we had a different organizational structure. We have to balance, that would be a good partner, deliver on the things we agreed were priorities, be flexible with how we're spending our time, but it gives us agency and responsibility beyond that. And I feel like the team takes that very seriously. So I've seen examples of that in how we bring data to a lot of spaces, including how we partner with engineering on data-related topics or how we partner with content that I'm not sure we would've gotten to if not for having that kernel that's sort of a center of excellence around it.

Lenny (00:57:10):
And it's Data and Insights, that was the team that you ran. Insights, is that describing user research or what does that have function actually?

Elizabeth Stone (00:57:19):
So part of Data and Insights is a Consumer Insights team that includes a lot of different flavors of research really. So in some ways, consumer is even a misnomer because there's parts of the team that do internal research, for example, on tools and products for our studio productions. So that's more of a user research-oriented versus consumer. And then the parts of that team that are consumer-oriented do things all the way from content screenings to make titles the best version of themselves before they're on the service to more traditional UX research to think about how can we deliver the best title discovery experience or how can we think about things that improve accessibility? And then that team has a global remit. So there's also teams that are more local or regional expertise in understanding consumer needs and entertainment.

(00:57:12):
So Consumer Insights and a team, formerly known as still kind of known as a shorthand, data science and engineering, combined together to create data and insights probably about two years ago. That's another piece that's unusual. It becomes truly a full-stack data and research expertise. And so we could tackle a problem like, what's the right way to think about recommendations and how best to surface them in a way that combines attitudinal research, qualitative and quantitative with behavioral research on more of the data science, data engineering analytics side.

Lenny (00:58:51):
It's super cool because I think it's really rare that what people think of user research is within the data org. And I think that might be a solution to some of the backlash a lot of user research teams get where they're like, I don't know, what are you guys doing all this anecdotal evidence if it's under the same org. I feel like that leads to a lot more credibility and avoids this like, "Oh, data's telling me this thing. This user research team is telling me this thing. What should we do?"

Elizabeth Stone (00:59:17):
Yeah, I mean, Consumer Insights is one of the newer teams for me; it wasn't in my background to lead a team like that and not in my individual training, but they are critical for making sure we keep a consumer orientation, a member orientation on things. I have loved to watch the teams collaborate on problems because we talk about it as a superpower internally in combining those skill sets. So I think the Consumer Insights team at Netflix has had a lot of credibility in a certain area of expertise and we took it to the next level by combining it with other functional expertise. So it's not required in every problem space. So we try not to overdo it and say we need to be collaborating everywhere because that just feels like the wrong expectation, but we try to make the most of it in spaces where we really benefit. So yeah, it's worked out really well.

Lenny (01:00:12):
Awesome. Okay. I want to ask two more questions before we get to our very exciting lightning around. And they're both skills that [inaudible 01:00:08] have told me you're very good at. One is that you are very intentional and thoughtful about staying close to individual teams and individuals within the company, even though you're higher and higher in the org. I'm curious how you do that, how you actually practice this skill of staying really close to teams at the bottom of the ladder and individuals that are working on things on the ground basically?

Elizabeth Stone (01:00:45):
A lot of it is how I spend my time and fighting to preserve opportunities to connect with people. So examples would be, I still have biweekly office hours, people sign up for slots. It can feel a little like speed dating for 20 minute slots, but I get to meet a whole bunch of people and hear about work, hear what's top of mind. People book them out many months ahead and it's just an opportunity to stay in touch. And then I do Ask Me Anything sessions with teams of different sizes depending on how intimate we want it to feel, but truly anything is fair game as a way to get to know me as a person, for me to hear questions, to try to be candid about what I can answer or can't answer. And so those things have helped me maintain connection, but both of those examples are about making the time for it.

(01:01:50):
So what I have found as my role has changed is that it just wouldn't happen if I didn't make it a priority. And then through those types of sessions, I do think I become or I hope to become more approachable so people know, "You can send me a Slack message, you can send me an email. Like I mentioned earlier, I'm going to respond to you as quickly as I can because I want to hold myself to that bar." And so that builds a flow of communication between me and the team that I really value... I don't think I would want to do my job if I didn't have those points of connection, so that helps too.

Lenny (01:02:24):
And you also send that email to everyone after every leadership meeting, so they're like, "Oh yeah, Elizabeth."

Elizabeth Stone (01:02:28):
Yeah, they hear from me. Yeah.

Lenny (01:02:31):
Kind of related to this, so we have a mutual friend, that's how we got connected. Ali Rao, she was a data scientist at Airbnb, now she's at Uber. She had a question that she wanted me to ask, and it's about how good you are at being present. So her question is something she's noticed about. "Something I've noticed about her is how 100% present she is no matter who she talks to. Do you have any advice for people to get better at this? Because it's so hard in the day of email and iPhones and Slack." Her questions like, "When does she respond to stuff if not sometimes in meetings?"

Elizabeth Stone (01:03:05):
I actually think I'm the most present when I'm having conversations like this one. I do preserve a lot of time to have one-on-one conversations where I'm genuinely curious about how someone's doing, how I can help them, what they're excited about that's authentic. And so while my EA would probably cringe at saying I like to spend time doing a lot of those one-on-ones, it is relatively easier for me to say the human connection is part of what I enjoy about this. I think that's true for a lot of people in what we get out of work and life, but I try to live that in those meetings. I'm probably not as good when we're talking about meetings of 30 people and I'm multitasking, so I'll admit to doing that for sure. But I think the one-on-one conversations I treat as being pretty sacred.

(01:04:09):
One of the things I've noticed that helps me continue to invest in that and maybe is helpful for other people is some of my greatest friends and connections, including people like Ali, are people I met along the way professionally. So I worked very closely with Ally's husband, Keith Henwood, at multiple places, both Analysis Group and at Lyft. And that means that it's created opportunities and it's been points of connection. And so you get back what you give basically.

(01:04:45):
There are people in my life who are part of my life because I worked with them or because I crossed paths. And I like to think that if I can make a positive mark on them, it'll come back and be at some point too. So I think to distill that is that I truly enjoy it. It's what I get out of especially work. And then it's my community. And that's served me really well over time. And so I have given people advice of, "This is a small community, think about what you're investing in other people because that will matter down the line for yourself too" and I try to live that myself.

Lenny (01:05:22):
Yeah, that's such good advice. There's kind of two things that come to mind there. One is treat people the way you want to be treated. Someone once said that maybe. And I think you've come back to this a couple times, this idea of just pay attention to what gives you energy and that you're good at and just almost double down on that. Just make that more and more of a superpower.

Elizabeth Stone (01:05:41):
Yeah, that last part resonates. It's been a big part of my personal and professional practice to reflect on how I'm feeling, what I'm excited about, what I'm enjoying. I do think it helps me be more grounded, which maybe helps me be more present or helps me be a better manager or leader. That might be part of the secret sauce too, but it is part of my practice.

Lenny (01:06:11):
I can't help but ask, is this an actual practice? Do you do this on a regular basis or is this just something you think about like, "I should reflect back"?

Elizabeth Stone (01:06:18):
I wish I was so advanced to say I meditate and I create all this structure. It's more that I think I mentioned maybe I'm an introvert, so I do spend some time alone. That's how I recharge. And early mornings, especially people who know me sometimes are horrified at the time of day I send emails, but early mornings are a quiet time for me where I do try to have a daily check-in of just how are things going, why am I feeling anxious, why am I feeling excited. And it's kind of a muscle you build. So while I don't write in a journal, I don't have a meditation practice, I do have a time of day when I try to keep it protected from other things so that I can think for a second.

Lenny (01:07:05):
What I think about there is Jeff Bezos has this approach in the morning. He just calls, he putters around. He has no meetings until I think 10:10 or something. He just wants to putter around, read the newspaper, see what's going on in email, which I'm trying to do. I really like that. That feels really good. I'm just going to putter around. I have no responsibilities in the morning.

Elizabeth Stone (01:07:22):
I've never heard that. I'm going to adopt that language.

Lenny (01:07:27):
I'm just puttering and puttering. Elizabeth, is there anything else you wanted to touch on or leave listeners with before we get to our very exciting lightning round?

Elizabeth Stone (01:07:38):
No, I'm ready for the exciting lightning round.

Lenny (01:07:40):
Well, with that, we've reached our very exciting lightning round. First question, what are two or three books that you've recommended most to other people?

Elizabeth Stone (01:07:50):
It's probably a little recency bias, but I've been recommending What I Talk About When I Talk About Running by Murakami, which talks about introspection about the similarities between running and writing as sort of flow states and very meditative things. So I had read some of his fiction books and the autobiographical reflection on these types of either professions or hobbies I think is very insightful. So that's one. And then one of my longtime favorite books is A Fine Balance by Mistry. And that is just a great story of human complexity and challenge and relationships. So I'm drawn to both books and TV and film that are about humans.

Lenny (01:08:43):
Speaking of TV and film, this is maybe a high stakes question for someone that works in Netflix, do you have a favorite recent movie or TV show?

Elizabeth Stone (01:08:52):
I'm not going to name all Netflix. That feels too much like an advertisement. Film, Triangle of Sadness is phenomenal if you haven't seen it. And then I'll go Netflix for TV, Beef was I thought hysterical. I'm an Ali Wong fan, but also just a pretty unique storyline.

Lenny (01:09:18):
And I think they just won a bunch of Emmys.

Elizabeth Stone (01:09:20):
They did.

Lenny (01:09:21):
Amazing. Good picks. Next question. Do you have a favorite interview question that you like to ask candidates that you are interviewing?

Elizabeth Stone (01:09:29):
High talent density. I'm usually looking for the person who would be better in my role than I am in my role. So I often ask people what would their priorities be, what would they do differently if they had my job.

Lenny (01:09:45):
Next question, do you have a favorite product that you recently discovered that you really like?

Elizabeth Stone (01:09:52):
So while I carry the CTO title, I live a pretty analog life. So my most recent product is a Fellow pour-over coffee maker, which is actually part of my morning ritual, which I'll now call puttering around, where I take great lengths in my coffee-making process because I find it calming. And then it's not a recent find, but I have to shout out that my Peloton is probably the favorite product I own.

Lenny (01:10:22):
The bike or the treadmill?

Elizabeth Stone (01:10:24):
Bike. I'm a recovering outdoor cyclist, so it's also kind of questionable if I can even admit to this, but that's why I would admit to I love the Peloton despite being ideally an outdoor cyclist.

Lenny (01:10:39):
I have questions about your cycling, but before that question, do you have a favorite life motto that you often come back to or share with friends or family that you find useful either in work or in life?

Elizabeth Stone (01:10:50):
My mom said something to me that has stuck with me. I don't know if I live it very well, but the phrase was, "Something good happens every day." And the reason she said it was because she was encouraging me to be more mindful about enjoying the small things in the day-to-day rather than letting myself get caught up in the busyness.

Lenny (01:11:13):
Beautiful. Final question. You're a big biker and triathlete. I am curious what that sport and time has given you in your career or in life. What benefits have you found from spending so much time and energy, running, biking, being an athlete?

Elizabeth Stone (01:11:32):
Certainly by mental resilience. So while those sound like physical strength, I've found especially endurance sports are much more mental and how you go through the highs and lows and sustain and then coming back from challenge. So those sports have had their highs and lows and from the lows I've really learned how to recover and bounce back. So those feel like universally applicable skills.

Lenny (01:12:04):
You have such an interesting mix of athleticism and then Netflix, what a good balance for life. This is going to give me permission to go watch Netflix recording this on Friday afternoon. Elizabeth, you're awesome. Thank you so much for being here. Two final questions. Where can folks find you online if they want to reach out and maybe follow up on things? And how can listeners be useful to you?

Elizabeth Stone (01:12:24):
You can always find me on LinkedIn, so definitely reach out or ping me if you have questions or comments. I think the way the listeners can be useful to me is being maybe curious about how they can show up even better in their lives now that we've done this reflection on Netflix culture and how we show up for other people. I would like to ask listeners to pay that forward to people that they're working with and how they show up for them.

Lenny (01:13:02):
Amazing. I love that. If you end up doing this and you're listening, maybe leave a comment on YouTube or in Substack with something that you haven't covered about yourself. Elizabeth, thank you so much for being here.

Elizabeth Stone (01:13:16):
Thank you, Lenny. I hope you have a great weekend.

Lenny (01:13:18):
Same. Bye everyone.

(01:13:20):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.
