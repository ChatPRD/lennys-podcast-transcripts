---
guest: Kevin Weil
title: OpenAI’s CPO on how AI changes must-have skills, moats, coding, startup playbooks,
  more | Kevin Weil
youtube_url: https://www.youtube.com/watch?v=scsW6_2SPC4
video_id: scsW6_2SPC4
description: 'Kevin Weil is the chief product officer at OpenAI, where he oversees
  the development of ChatGPT, enterprise products, and the OpenAI API. Prior to OpenAI,
  Kevin was head of product at Twitter,...

  '
duration_seconds: 5501.0
duration: '1:31:41'
view_count: 202940
channel: Lenny's Podcast
keywords:
- growth
- onboarding
- roadmap
- iteration
- a/b testing
- experimentation
- conversion
- monetization
- hiring
- management
- strategy
- vision
- competition
- market
- persona
---

# OpenAI’s CPO on how AI changes must-have skills, moats, coding, startup playbooks, more | Kevin Weil

## Transcript

Kevin Weil (00:00:00):
The AI models that you're using today is the worst AI model you will ever use for the rest of your life, and when you actually get that in your head, it's kind of wild. Everywhere I've ever worked before this, you kind of know what technology you're building on, but that's not true at all with AI. Every two months, computers can do something they've never been able to do before and you need to completely think differently about what you're doing.

Lenny Rachitsky (00:00:21):
You're chief product officer of maybe the most important company in the world right now. I want to chat about what it's just like to be inside the center of the storm.

Kevin Weil (00:00:29):
Our general mindset is in two months, there's going to be a better model and it's going to blow away whatever the current set of limitations are. And we say this to developers too. If you're building and the product that you're building is kind of right on the edge of the capabilities of the models, keep going because you're doing something right. Give it another couple months and the models are going to be great, and suddenly the product that you have that just barely worked is really going to sing.

Lenny Rachitsky (00:00:51):
Famously, you led this project at Facebook called Libra.

Kevin Weil (00:00:56):
Libra is probably the biggest disappointment of my career. It fundamentally disappoints me that this doesn't exist in the world today because the world would be a better place if we'd been able to ship that product. We tried to launch a new blockchain. It was a basket of currencies originally. It was integration into WhatsApp and Messenger. I would be able to send you 50 cents in WhatsApp for free. It should exist. To be honest, the current administration is super friendly to crypto. Facebook's reputation is in a very different place. Maybe they should go build it now.

Lenny Rachitsky (00:01:27):
Today my guest is Kevin Weil. Kevin is chief product officer at OpenAI, which is maybe the most important and most impactful company in the world right now, being at the forefront of AI and AGI and maybe someday super intelligence. He was previously head of product at Instagram and Twitter. He was co-creator of the Libra Cryptocurrency at Facebook, which we chat about. He's also on the boards of Planet and Strava and the Black Product Managers Network and the Nature Conservancy. He's also just a really good guy and he has so much wisdom to share. We chat about how OpenAI operates, implications of AI and how we will all work and build product, which markets within the AI ecosystem, companies like OpenAI won't likely go after and thus are good places for startups to own. Also, why learning the craft of writing evals is quickly becoming a core skill for product builders, what skills will matter most in an AI era and what he's teaching his kids to focus on and so much more.

(00:02:24):
This is a very special episode and I am so excited to bring it to you. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. If you become an annual subscriber of my newsletter, you get a year free of Perplexity Pro, Linear, Notion Superhuman and Granola. Check it out at lennysnewsletter.com and click bundle. With that, I bring you Kevin Weil. This episode is brought to you by Eppo. Eppo is a next-generation A/B testing and feature management platform built by alums of Airbnb and Snowflake for modern growth teams. Companies like Twitch, Miro, ClickUp and DraftKings rely on Eppo to power their experiments. Experimentation is increasingly essential for driving growth and for understanding the performance of new features and Eppo helps you increase experimentation velocity while unlocking rigorous deep analysis in a way that no other commercial tool does.

(00:03:18):
When I was at Airbnb, one of the things that I loved most was our experimentation platform where I could set up experiments easily, troubleshoot issues, and analyze performance all on my own. Eppo does all that and more with advanced statistical methods that can help you shave weeks off experiment time and accessible UI for diving deeper into performance and out-of-the-box reporting that helps you avoid annoying prolonged analytic cycles. Eppo also makes it easy for you to share experiment insight with your team, sparking new ideas for the A/B testing flywheel. Eppo powers experimentation across every use case, including product, growth, machine learning, monetization, and email marketing. Check out Eppo at geteppo.com/lenny and 10X your experiment velocity. That's geteppo.com/lenny.

(00:04:06):
This episode is brought to you by Persona, the adaptable identity platform that helps businesses fight fraud, meet compliance requirements, and build trust. While you're listening to this right now, how do you know that you're really listening to me, Lenny? These days, it's easier than ever for fraudsters to steal PII, faces and identities. That's where Persona comes in. Persona helps leading companies like LinkedIn, Etsy, and Twilio securely verify individuals and businesses across the world. What sets Persona apart is its configurability. Every company has different needs depending on its industry, use cases, risk tolerance and user demographics. That's why Persona offers flexible building blocks that allow you to build tailored collection and verification flows that maximize conversion while minimizing risks. Plus Persona's orchestration tools automate your identity process so that you can fight rapidly shifting fraud and meet new waves of regulation. Whether you're a startup or an enterprise business, Persona has a plan for you. Learn more at withpersona.com/lenny. Again, that's withpersona.com/lenny. Kevin, thank you so much for being here and welcome to the podcast.

Kevin Weil (00:05:23):
Thank you so much for having me. We've been talking about doing this forever and we made it happen.

Lenny Rachitsky (00:05:27):
We did it. I can't imagine how insane your life is, so I really appreciate that you made time for this and we're actually recording this the week that you guys launched your new image model, which is a happy coincidence. My entire social feed is filled with ghiblifications of everyone's life and family photos and everything, so good job.

Kevin Weil (00:05:45):
Yep, mine too. My wife, Elizabeth, sent me one of hers, so I'm right there with you.

Lenny Rachitsky (00:05:51):
Let me just ask, did you guys expect this kind of reaction? It feels like this is the most viral thing that's happened in AI, which a high bar since, I don't know, ChatGPT launched. Just like, did you guys expect it to go this well? What does it feel like internally?

Kevin Weil (00:06:04):
There have been a handful of times in my career when you're working on a product internally and the internal usage just explodes. This was true by the way when we were building stories at Instagram. More than anything else in my career, we could feel it was going to work because we were all using it internally and we'd go away for a weekend. Before it launched we were all using it and we'd come back after a weekend and we would know what was going on and be like, "Oh, hey, I saw you were at that camping trip, how was that?" You were like, "Man, this thing really works." ImageGen was definitely one of those, so we'd been playing with it for, I don't know, a couple months and when it first went live internally to the company, there was kind of a little gallery where you could generate your own, you could also see what everyone else was generating and it was just nonstop buzz. So yeah, we had a sense that this was going to be a lot of fun for people to play with.

Lenny Rachitsky (00:06:58):
That's really cool. That should be a measure of just confidence into something going well that you're launching is internally everyone's going crazy for it.

Kevin Weil (00:07:05):
Yeah. Especially social things because you have a very tight network as a company socially, so you know each other and you're experts in your product hopefully. And so there's some sense in which if you're doing something social and it's not taking off internally, you might question what you're doing.

Lenny Rachitsky (00:07:23):
Yeah, and by the way, the Ghibli thing, is that something you guys seeded or how did that even start? Was that an intentional example?

Kevin Weil (00:07:29):
I think it's just the style people love and the model is really capable at emulating style or understanding what... It's very good at instruction following. That's actually something that I think people... I'm starting to see people discover with it, but you can do very complex things. You can give it two images, one is your living room and the other is a whole bunch of photos or memorabilia or things you want and you say, "Tell me how you would arrange these things." Or you can say, "I'd like you to show me what this will look like if you put this over here and this thing to the right of that and this one to the left of this, but under that one." And the model actually will understand all of that and do it. It's incredibly powerful. So I'm just excited about all the different things people are going to figure out.

Lenny Rachitsky (00:08:11):
Yeah. All right. Well, good job. Good job team OpenAI. Let's get serious here and let's zoom out a little bit. The way I see it is you're chief product officer of maybe the most important company in the world right now. Just not to set the bar too high, but you guys are ushering in AI, AGI at some point, super intelligence at some point. No big deal. I have more questions for you than I've had for any other guest. Actually put out a call-out on Twitter and LinkedIn and my community just like what would you want to ask Kevin? And I had over 300 well-formed questions and we're going to go through every single one. So let's just get started. I'm just joking.

Kevin Weil (00:08:45):
Cool.

Lenny Rachitsky (00:08:46):
I picked out the best and there's a lot of stuff I'm really curious about.

Kevin Weil (00:08:48):
Well, it's 1 PM here. It doesn't get dark for a while, so let's do it.

Lenny Rachitsky (00:08:53):
Okay, here we go. Okay, so first of all, I'm just going to take notes here. When is AGI launching? When in December?

Kevin Weil (00:08:58):
I mean, we just launched a good ImageGen model. Does that count?

Lenny Rachitsky (00:09:03):
It's getting there. It's getting there.

Kevin Weil (00:09:05):
There's this quote I love, which is "AI is whatever hasn't been done yet" because once it's been done, when it kind of works, then you call it machine learning, and once it's kind of ubiquitous and it's everywhere, then it's just an algorithm. So I've always loved that we call things AI when they still don't quite work and then by the time it's like an AI algorithm that's recommending you follow, oh, that's just an algorithm, but this new thing, like self-driving cars, that's it. I think to some degree we're always going to be there and the next thing is always going to be AI and the current thing that we use every day and is just a part of our lives, that's an algorithm.

Lenny Rachitsky (00:09:46):
It's so interesting because in the Bay Area you see self-driving cars driving around and it's so normal now when four years ago and three years ago, you would've seen this and you'd be like, "Holy shit, what is... We're in the future." And now we're just so take it for granted.

Kevin Weil (00:10:01):
I mean there's something like that with everything. If I showed you... When GPT-3 launched, I wasn't at OpenAI then. I was just a user, but it was mind-blowing. And if I gave you GPT-3 now I just plugged that into ChatGPT for you and you started using it, you'd be like, "What is this thing?" It's like mess.

Lenny Rachitsky (00:10:22):
Flop, flop.

Kevin Weil (00:10:24):
I had the same experience when I first got into a Waymo, your very first ride, at least my very first ride, my first 10 seconds in a Waymo, it starts driving and you're like, "Oh my God, watch out for that bike." You're holding onto whatever you can. And then five minutes in, you've calmed down and you realize that you're getting driven around the city without a driver and it's working. You're just like, "Oh my God, I am living in the future right now." And then another 10 minutes, you're bored, you're doing email on your phone, answering Slack messages, and suddenly this miracle of human invention is just an expected part of your life from then on. And there is really something in the way that we all are adapting to AI that's kind of like that. These miraculous things happen and computers can do something they've never been able to do before and it blows our mind collectively for a week and then we're like, oh, yeah. Oh, now it's just machine learning on its way to being an algorithm.

Lenny Rachitsky (00:11:23):
The craziest thing about what you just shared actually is, I don't know, ChatGPT, which is now feels terrible. 3.5 was a couple years ago, and imagine what life will be like in a couple years from now. We're going to get to that, where things are going, what you think is going to be the next big leap. But I want to start with the beginning of your journey at OpenAI. So you worked at Twitter, you worked at Facebook, you worked at Planet, Instagram. At some point you got recruited to go and come work at OpenAI. I'm curious just what that story was like of the recruiting process of joining OpenAI as CPO. Is there any fun stories there?

Kevin Weil (00:12:01):
If I'm remembering the timeline right, we communicated at Planet I was leaving and I was planning to just go take some time. I wasn't going to stop working, but I was also happy to take the summer. This was maybe April or something. I was like, cool, I'm going to have the summer with my kids. We're going to go to Tahoe or something and I'll actually get to hang out rather than what I usually do going up and down and all that. And then Sam and I had known each other lightly for a bunch of years and he's always involved in so many interesting things like companies building fusion and all these things. So he'd always been somebody that I would call occasionally if I was starting to think about my next thing because I like working on big tech forward, sort of next wave kind of things.

(00:12:49):
And so I called him and I think Vinod also helped to put us in touch again. And this time it wasn't like, "Oh, you should go talk to these guys working on fusion." He said, "Actually, we're thinking about something, you should come talk to us." I was like, "Okay, that sounds amazing. Let's do it." And it goes really fast, really, really fast. I met most of the management team in a brief period of time, a few days, and they were telling me, 'Look, we're basically going to move as fast as we want to move. And if you talk to everyone, everyone likes you, you're ready to go." Sam came over for dinner and we had a great evening together just talking about OpenAI in the future and getting to know each other better. And at the end I was like, I was going to go in the next day for a bigger round of interviews and Sam was saying, "Hey, it's going really well. We're really excited."

(00:13:52):
And I said, "Cool. So how do I think about tomorrow?" And he said, "Oh, you'll be fine. Don't worry about it. And if it goes well, we're basically there." And so I go in the next day, meet a bunch of people, have a great time. I really enjoyed everybody I met with. In any interview, you can always second guess yourself like, oh, I shouldn't have said that thing or that thing I gave a bad answer on I wish I could redo, but I came away feeling like I think that went pretty well. And I was expecting to hear that weekend basically because they sort of set expectations as soon as if this goes well, we're ready to go. And I didn't hear anything. And then it was like Monday, Tuesday, Wednesday, I still didn't hear anything and I reached out to folks on the OpenAI side a couple of times, still nothing.

(00:14:45):
And I was like, "Oh my God, I screwed it up. I don't know where I screwed it up, but I totally screwed it up. I can't believe it." And I was going back to Elizabeth, my wife and being like, "What did I do? Where do you think I..." Getting all crazy about it and then it's still nothing. And finally it was like nine days later, they finally got back to me and it turned out there was a bunch of stuff happening internally and this, that and the other thing, and there's just a million things happening. And they finally were like, "Oh yeah, that went well. Let's do this." And I was like, "Oh, okay, cool, let's do it." But it was nine days of agony and they were just super busy on some internal stuff and there I was fretting every single day and re-going over every line of our interview process.

Lenny Rachitsky (00:15:33):
It makes me think about when you're dating someone and you've texted them and you're not hearing anything back, you assume something is wrong.

Kevin Weil (00:15:40):
Yeah, totally.

Lenny Rachitsky (00:15:41):
They might just be busy.

Kevin Weil (00:15:42):
I have a hard time about it still.

Lenny Rachitsky (00:15:47):
That's wild. I love that it worked out. And I guess the lesson there is don't jump to conclusions.

Kevin Weil (00:15:55):
Yeah. Have a little bit of chill.

Lenny Rachitsky (00:15:59):
Speaking of that, I want to chat about what it's just like to be inside the center of the storm. Again, you work at a lot of, let's say traditional companies even though they're not that traditional, Twitter and Instagram and Facebook and Planet, and now you work at OpenAI. I'm curious, what is most different about how things work in your day-to-day life at OpenAI?

Kevin Weil (00:16:19):
I think it's probably the pace. Maybe it's two things. One is it's the pace. The second is everywhere I've ever worked before this, you kind of know what technology you're building on. So you spend your time thinking about what problems are you solving? Who are you building for? How are you going to make their lives better? How are you going to... Is this a big enough problem that you're going to be able to change habits? Do people care about this problem being solved? All those good product things. But the stuff that you're building on is kind of fixed. You're talking about databases and things and I bet the database you used this year is probably 5% better than the database you used two years ago, but that's not true at all with AI. It's like every two months computers can do something they've never been able to do before and you need to completely think differently about what you're doing.

(00:17:10):
There's something fundamentally interesting about that makes life fun here. There's also something we will maybe talk about evals later, but it also really, in this world of... Everything we're used to with computers is about giving a computer very defined inputs. If you look at Instagram for example, there are buttons that do specific things and you know what they do. And then when you give a computer defined inputs, you get very defined outputs. You're confident that if you do the same thing three times, you're going to get the same output three times. LLMs are completely different than that. They're good at fuzzy subtle inputs. Then all the nuances of human language and communication, they're pretty good at. And also they don't really give you the same answer. You probably get spiritually the same answer for the same question, but it's certainly not the same set of words every time. And so you're much more, it's fuzzier inputs and fuzzier outputs. And when you're building products, it really matters whether there's some use case that you're trying to build around.

(00:18:16):
If the model gets it right 60% of the time, you build a very different product than if the model gets it right 95% of the time versus if the model gets it right 99.5% of the time. And so there's also something that you have to get really into the weeds on your use case and the evals and things like that in order to understand the right kind of product to build. So that is just fundamentally different. If your database works once, it works every time. And that's not true in this world.

Lenny Rachitsky (00:18:45):
Let's actually follow this thread on evals. I definitely wanted to talk about this. We had this legendary panel at the Lenny & Friends Summit. It was you and Mike Krieger and Sarah Guo moderating.

Kevin Weil (00:18:58):
That was fun.

Lenny Rachitsky (00:18:58):
So fun. The thing that I heard that kind of stuck with people from that panel was a comment you made where you said that writing evals is going to become a core skill for product managers, and I feel like that probably applies further than just product managers. A lot of people know what evals are. A lot of people have no idea what I'm talking about. So could you just briefly explain what is an eval and then just why do you think this is going to be so important for people building products in the future?

Kevin Weil (00:19:23):
Yeah, sure. I think the easiest way to think about it is almost like a quiz for a model, a test to gauge how well it knows a certain set of subject material or how good it is at responding to a certain set of questions. So in the same way you take a calculus class and then you have calculus tests that see if you've learned what you're supposed to learn. You have evals that test how good is the model at creative writing? How good is the model at graduate level science? How good is the model at competitive coding? And so you have these set of evals that basically perform as benchmarks for how smart or capable the model is.

Lenny Rachitsky (00:20:04):
Is it a simple way to think about it, like unit tests for model?

Kevin Weil (00:20:07):
Yeah, unit tests, tests in general for models. Totally.

Lenny Rachitsky (00:20:10):
Great, great. Okay. And then why is this so important for people that don't totally understand what the hell's going on here with evals? Why is this so key to building AI products?

Kevin Weil (00:20:20):
Well, it gets back to what I was saying. You need to know whether your model is going to... There are certain things that models will get right. 99.95% of the time and you can just be confident. There are things that they're going to be 95% right on and things they're going to be 60% right on. If the model's 60% right on something, you're going to need to build your product totally differently. And by the way, these things aren't static either. So a big part of evals is if you know you're building for some use case. So let's take our deep research product, which is one of my favorite things that we've released maybe ever. The idea is with deep research for people who haven't used it, you can give ChatGPT now an arbitrarily complex query. It's not about returning you an answer from a search query, which we can also do.

(00:21:10):
It's here's a thing that if you were going to answer it yourself, you'd go off and do two hours of reading on the web and then you might need to read some papers and then you would come back and start writing up your thoughts and realize you had some gaps in your thinking. So you go out and do more research. It might take you a week to write some 20 page answer to this question. You can let ChatGPT just like chug for you for 25, 30 minutes. It's not the immediate answers you're used to, but it might go work for 25, 30 minutes and do work that would've taken you a week. So as we were building that product, we were designing evals at the same time as we were thinking about how this product was going to work and we were trying to go through hero use cases.

(00:21:57):
Here's a question you want to be able to ask. Here's an amazing answer for that question. And then turning those into evals and then hill climbing on those evals. So it's not just that the model is static and we hope it does okay on a certain set of things, you can teach the model. You can make this a continuous learning process. And so as we were fine-tuning our model for deep research to be able to answer these things, we were able to test is it getting better on these evals that we said were important measures of how the product was working? And it's when you start seeing that and you start seeing performance on evals going up, you start saying, "Okay, I think we have a product here."

Lenny Rachitsky (00:22:35):
You made a kind of a comment along these same lines around evals that AI is almost capped in how amazing it can be by how good we are at evals. Does that resonate? Any more thoughts along those lines?

Kevin Weil (00:22:48):
I mean, these models are their intelligences and intelligence is so fundamentally multidimensional so you can talk about a model being amazing at competitive coding, which may not be the same as that model being great at front-end coding-

Kevin Weil (00:23:00):
... may not be the same as that model being great at front-end coding or back-end coding or taking a whole bunch of code that's written in COBOL and turning it into Python. And that's just within the software engineering world. So I think there's a sense in which you can think of these models as incredibly smart, very factually aware intelligences, but still most of the world's data, knowledge, process is not public. It's behind the walls of companies or governments or other things. And same way, if you were going to join a company, you would spend your first two weeks onboarding. You'd be learning the company-specific processes. You'd get access to company-specific data. The models are smart enough, you can teach them anything, but they need to have the raw data to learn from.

(00:23:58):
So there's a sense in which I think the future is really going to be incredibly smart, broad-based models that are fine-tuned and tailored with company-specific or use case-specific data so that they perform really well on company-specific, or use case-specific things. And you're going to measure that with custom evals. So what I was referring to is just like these models are really smart, you need to still teach them things if the data's not in their training set, and there's a huge amount of use cases that are not going to be in their training set because they're relevant to one industry or one company.

Lenny Rachitsky (00:24:40):
I'm just going to keep following the thread that you're leading us down, but I'm going to come back because I have more questions around some of these things. So you came to a space that I think a lot of AI founders are thinking about is just, where's OpenAI not going to come squash me in the future? Or one of the other foundational models. So it's unclear to a lot of people just like, "Should I build a startup in this space or not?" Is there any advice you have or any guidance for where you think OpenAI, or just foundational models in general likely won't go and where you have an opportunity to build a company?

Kevin Weil (00:25:10):
So this is something that Ev Williams used to say back at Twitter that's always stuck with me, which is, "No matter how big your company gets, no matter how incredible the people are, there are way more smart people outside your walls than there are inside your walls." And that's why we are so focused on building a great API. We have 3 million developers using our API. No matter how ambitious we are, how big we grow, by the way, we don't want to grow super big, there are so many use cases, places in the world where AI can fundamentally make our lives better. We're not going to have the people. We're not going to have the know-how to build most of these things.

(00:25:55):
And I think, like I was saying, the data is industry-specific, use case-specific, behind certain company walls, things like that. And there are immense opportunities in every industry and every vertical in the world to go build AI-based products that improve upon the state of the art. And there's just no way we could ever do that ourselves. We don't want to. We if we did want to, and we're really excited to power that for 3 million-plus developers and way more in the future.

Lenny Rachitsky (00:26:24):
Coming back to your earlier point about the tech changing constantly and getting faster, not exactly knowing what you'll have by the time you launch something in terms of the power, the model. I'm curious what allows you to ship quickly and consistently in such great stuff? And it sounds like one answer is bottoms-up empowered teams versus a very top-down roadmap that's planned out for a quarter. What are some of those things that allow you to ship such great stuff so often, so quickly?

Kevin Weil (00:26:53):
Yeah. I mean, we try and have a sense of where we're trying to go, point ourselves in a direction so that we have some rough sense of alignment. Thematically, I don't for second, and we do quarterly roadmapping. We laid out a year-long strategy. I don't for a second believe that what we write down in these documents is what we're going to actually ship three months from now, let alone six or nine. But that's okay. I think it's like an Eisenhower quote, "Plans are useless. Planning is helpful," which I totally subscribe to, especially in this world. It's really valuable. If you think about quarterly road roadmapping for example, it's really valuable to have a moment where you stop and go, "Okay. What did we do? What worked? What went well? What didn't go well? What did we learn and now what do we think we're going to do next?"

(00:27:44):
And by the way, everybody has some dependencies. You need the infrastructure team to do the following things, partnership with research here. So you want to have a second to check your dependencies, make sure you're good to go and then start executing. We try and keep that really lightweight because it's not going to be right. We're going to throw it out halfway because we will have learned new things. So the moment of planning is helpful even if it's only partially.

(00:28:12):
So I think just expecting that you're going to be super agile and that there's no sense writing a three month roadmap, let alone a year long roadmap because the technology's changing underneath you so quickly. We really do try and go very strongly bottoms up, subject to our overall directional alignment. We have great people. We have engineers and PMs and designers and researchers who are passionate about the products they're building and have strong opinions about them and are also the ones building them. So they have a real sense of what the capabilities are too, which is super important.

(00:28:49):
So I think you want to be more bottoms up in this way. So we operate that way. We are happy making mistakes. We make mistakes all the time. It's one of the things I really appreciate about Sam. He pushes us really hard to move fast, but he also understands that with moving fast comes, we didn't quite get this right or that we launched this thing, it didn't work. We'll roll it back. Look at our naming. Our naming is horrible.

Lenny Rachitsky (00:29:14):
That was a lot of questions people had for you. Model names, yeah.

Kevin Weil (00:29:18):
It's absolutely atrocious and we know it, and we will get around to fixing it at some point, but it's not the most important thing and so we don't spend a lot of time on it.

Lenny Rachitsky (00:29:27):
But it also shows you how it doesn't matter. Again, ChatGPT the most popular, fastest growing product in history, it's the number one AI, API and model. So clearly it doesn't matter that much.

Kevin Weil (00:29:39):
And we name things like o3 mini high.

Lenny Rachitsky (00:29:46):
Man, I love it. Okay. So you talked about roadmapping and bottoms up and I'm really curious, is there a cadence or a ritual of aligning with you or Sam or you review everything that's going out? Is there a meeting every week or every month where you guys see what's happening?

Kevin Weil (00:30:03):
On key projects. So we do product reviews and things like that, like you would expect. There isn't a ritual because there isn't... I would never want us to be blocked on launching something, waiting for a review with me or Sam, if we can't get there. If I'm traveling or Sam's busy or whatever, that's a bad reason for us not to ship. So obviously for the biggest, most high priority stuff, we have a pretty close beat on it, but we really try not to, frankly. We want to empower teams to move quickly, and I think it's more important to ship and iterate.

(00:30:42):
So we have this philosophy, we call iterative deployment, and the idea is we're all learning about these models together. So there's a real sense in which it's way better to ship something even when you don't know the full set of capabilities and iterate together in public. And we co-evolve together with the rest of society as we learn about these things and where they're different and where they're good and bad and weird. I really like that philosophy.

(00:31:12):
I think the other thing that ends up being a part of our product philosophy is the sense of model maximalism. The models are not perfect. They're going to make mistakes. You could spend a lot of time building all kinds of different scaffolding around them. And by the way, sometimes we do because sometimes there are kinds of errors that you just don't want to make, but we don't spend that much time building scaffolding around the parts that don't match that because our general mindset is in two months there's going to be a better model and it's going to blow away whatever the current set of limitations are.

(00:31:52):
So if you're building, and we say this to developers too, if you're building and the product that you're building is right on the edge of the capabilities of the models, keep going, because you're doing something right because you give it another couple months and the models are going to be great, and suddenly the product that you have that just barely worked is really going to sing. And that's how you make sure that you're really pushing the envelope and building new things.

Lenny Rachitsky (00:32:19):
I had the founder of Bolt on the podcast, StackBlitz is the company name, and he shared this story that they've been working on this product for seven years behind the scenes and it was failing. Nothing was happening. And then all of a sudden it was, sorry to mention a competitor, but Claude came out or a Sonnet 3.5 came out and all of a sudden everything worked and they've been building all this time and finally it worked. And I hear that a lot with YC, just like things that never were possible now are just becoming possible every few months with the updates to the models.

Kevin Weil (00:32:48):
Yeah, absolutely.

Lenny Rachitsky (00:32:50):
Let me actually ask this, I wasn't planning to ask this, but I'm curious if you have any quick thoughts just why is Sonnet so good at coding, and thoughts on your stuff getting as good and better at actual coding?

Kevin Weil (00:33:01):
Yeah. I mean, kudos to Anthropic. They've built very good coding models. No doubt. We think that we can do the same. Maybe by the time this podcast has shipped, we'll have more to say, but either way, all credit to them. I think intelligence is really multi-dimensional and so I think the model providers... It used to be that OpenAI had this massive model lead, 12 months or something ahead of everybody else. That's not true anymore. I like to think we still have a lead. I'd argue that we do, but it's certainly not a massive one. And that means that there are going to be different places where the Google models are really good or where Anthropic models are really good, or where we're really good and our competitors are like, "We got to get better at that." And it actually is easier to get better at a certain thing once someone's proved it possible than it is to forge a path through the jungle and doing something brand new.

(00:34:03):
So I just think as an example, it was like nobody could break 4 minutes in the mile, and then finally somebody did and the next year 12 more people did it. I think there's that all over the place and it just means that competition is really intense, and consumers are going to win and developers are going to win and businesses are going to win in a big way from that. It's part of why the industry moves so fast, but all respect to the other big model providers. Models are getting really good. We're going to move as fast as we can and I think we've got some good stuff coming.

Lenny Rachitsky (00:34:36):
Exciting. This makes me also think about, in many ways other models are better at certain things, but somehow ChatGPT is the... If you look at all the awareness numbers and usage numbers, it's like no matter where you guys are in the rankings, people seem to just think of AI ChatGPT almost as the same. What do you think you did right to win in the consumer mindset, at least at this point and awareness in the world?

Kevin Weil (00:35:02):
I think being first helps, which is one of the reasons why we're so focused on moving quickly. We like being the first to launch new capabilities. Things like deep research. Our models, they can do a lot of things. So they can take real-time video input, you have speech to speech, you can do speech to text and text to speech. They can do deep research. They can operate on a canvas, they can write code. So ChatGPT can be this one- stop-shop where all the things that you want to do are possible. And as we go forward in it, we have more agentic tools like Operator where it's browsing for you and doing things for you on the web, more and more you're going to be able to come to this one place to ChatGPT, give it instructions and have it accomplish real things for you in the world. There's something fundamentally valuable in that. So we think a lot about that. We try to move really fast so that we are always the most useful place for people to come to.

Lenny Rachitsky (00:36:04):
What would you say is the most counterintuitive thing that you've learned after building AI products or working at OpenAI, something that's just like, "I did not expect that?"

Kevin Weil (00:36:14):
I don't know, maybe I should have expected this, but one of the things that's been funny for me is the extent to which you're trying to figure out how some product should work with AI, or even why some AI thing happens to be true, you can often reason about it the way you would reason about another human and it works. So maybe a couple examples. When we were first launching our reasoning model, we were the first to build a model that could reason, that could, instead of giving you just a quick system one answer right away to every question you asked, it was the third Emperor of the Holy Roman Empire, here's an answer.

(00:36:59):
You could ask it hard questions and it would reason. The same way that if I asked you to do a crossword puzzle, you couldn't just snap fill in everything. You would be, "Well, okay. On this one across, I think it could be one of these two, but that means there's an A here. So that one has to be this, away, back track, step-by-step build up from where you are." Same way you answer any difficult logistical problem, any scientific problem. So this reasoning breakthrough was big, but it was also the first time that a model needed to sit and think. And that's a weird paradigm for a consumer product. You don't normally have something where you might need to hang out for 25 seconds after you ask a question.

(00:37:40):
So we were trying to figure out what's the UI for this? With deep research where the model's going to go and think for 25 minutes sometimes, it's actually not that hard because you're not going to sit and watch it for 25 minutes. You're going to go do something else. You're going to go to another tab or go get lunch or whatever, and then you'll come back and it's done when it's like 20, 25 seconds or 10 seconds, it's a long time to wait, but it's not long enough to go to do something else.

(00:38:09):
So you can think, if you asked me something that I needed to think for 20 seconds to answer, what would I do? I wouldn't just go mute and not say anything and shut down for 20 seconds and then come back. So we shouldn't do that. We shouldn't just have a slider sitting there. That's annoying. But I also wouldn't just start babbling every single thought that I had. So we probably shouldn't just expose the whole chain of thought as the model's thinking, but I might go like, "That's a good question. All right." I might approach it like that and then think. You're maybe giving little updates and that's actually what we ended up shipping.

(00:38:49):
You have similar things where you can find situations where you get better thinking sometimes out of a group of models that all try and attack the same problem, and then you have a model that's looking at all their outputs and integrating it and then giving you a single answer at the end. I mean, sounds a little bit like brainstorming. I certainly have better ideas when I get in a room and brainstorm with other people because they think differently than me. So anyways, there's just all these situations where you can actually reason about it like a group of humans or an individual human and it works, which I don't know, maybe I shouldn't have been surprised but I was.

Lenny Rachitsky (00:39:27):
That is so interesting because when I see these models operate, I never even thought about you guys designing that experience. To me, it just feels like this is what the LLM does. It just sits there and tells me what it's thinking. And I love this point you're making of let's make it feel like a human operating and well, how does a human operate? Well, they just talk aloud. They think, here's the thing I should explore. And I love that deep sequence to the extreme of that where they're just like, "Here's everything I'm doing and thinking." And people actually like that too, I guess. Was that surprising to you, "Maybe that could work too. People seem to like everything?"

Kevin Weil (00:40:02):
Yeah. We learned from that actually because when we first launched it, we gave you the subheadings of what the model was thinking about, but not much more. And then deep seek launched and it was a lot and we went, I don't know if everyone wants that. There's some novelty effect to seeing what the model's really thinking about. We felt that too when we were looking at it internally. It's interesting to see the model's chain of thought, but it's not... I think at the scale of 400 million people, you don't want to see the model babble a bunch of things.

(00:40:34):
So what we ended up doing was summarizing it in interesting ways. So instead of just getting the subheadings, you're getting one or two sentences about how it's thinking about it and you can learn from that. So we tried to find a middle ground that we thought was an experience would be meaningful for most people, but showing everybody three paragraphs is probably not the right answer.

Lenny Rachitsky (00:40:57):
This reminds me of something else you said at the summit that has really stuck with me, this idea that chat, people always make fun of chat is not the future interface for how we interact with AI, but you made this really interesting point that may argue the other side, which is, as humans we interface by talking and the IQ of a human can span from really low to really high and it all works talking to them and chat is the same thing and it can work on all kinds of intelligence levels. Maybe I just shared it, but I guess anything there about just why chat actually ends up being such an interesting interface for LLMs?

Kevin Weil (00:41:30):
Yeah. I don't know, maybe this is one of those things I believe that most people don't believe, but I actually think chat is an amazing interface because it's so versatile. People tend to go, "Chat. Yeah. We'll figure out something better." And I think it's incredibly universal because it is the way we talk. I can talk to you verbally like we're talking now. We can see each other and interact. We can talk on WhatsApp and be texting each other, but all of these things is this unstructured method of communication and that's how we operate.

(00:42:12):
If I had some more rigid interface that I was allowed to use when we spoke, I would be able to speak to you about far fewer things and it would actually get in the way of us having maximum communication bandwidth. So there's something magical. And by the way, in the past it never worked because there wasn't a model that was good at understanding all of the complexity and nuances of human speech, and that's the magic of LLMs. So to me, it's like an interface that's exactly fit to the power of these things. And that doesn't mean that it always has to be just like I don't necessarily always want to type, but you do want that very open-ended, flexible communication medium, it may be that we're speaking and the model's speaking back to me, but you still want the very lowest common denominator, no restrictions way of interacting.

Lenny Rachitsky (00:43:04):
That is so interesting. That's really changed the way I think about this stuff is that point that chat is just so good for this very specific problem of talking to superintelligence basically.

Kevin Weil (00:43:13):
By the way, I think it's not that it's only chat either. If you have high volume use cases where they're more prescribed and you don't actually need the full generality, there are many use cases where it's better to have something that's less flexible, more prescribed, faster to specific task, and those are great too, and you can build all sorts of those. But you still want chat as this baseline for anything that falls out of whatever vertical you happen to be building for. It's like a catch-all for every possible thing you'd ever want to express to a model.

Lenny Rachitsky (00:43:51):
I'm excited to chat with Christina Gilbert, the founder of OneSchema, one of our long-time podcast sponsors. Hi, Christina.

Christina Gilbert (00:43:58):
Yes. Thank you for having me on, Lenny.

Lenny Rachitsky (00:44:00):
What is the latest with OneSchema? I know you now with some of my favorite companies like Ramp, Vanta, Scale and Watershed. I heard that you just launched a new product to help product teams import CSVs from especially tricky systems like ERPs?

Christina Gilbert (00:44:15):
Yes. So we just launched OneSchema FileFeeds, which allows you to build an integration with any system in 15 minutes as long as you can export a CSV to an SFTP folder. We see our customers all the time getting stuck with hacks and workarounds, and the product teams that we work with don't have to turn down prospects because their systems are too hard to integrate with. We allow our customers to offer thousands of integrations without involving their engineering team at all.

Lenny Rachitsky (00:44:37):
I can tell you that if my team had to build integrations like this, how nice would it be to be able to take this off my roadmap and instead, use something like OneSchema and not just to build it, but also to maintain it forever.

Christina Gilbert (00:44:49):
Absolutely, Lenny. We've heard so many horror stories of multi-day outages from even just a handful of ad records. We are laser-focused on integration reliability to help teams end all of those distractions that come up with integrations. We have a built-in validation layer that stops any bad data from entering your system, and OneSchema will notify your team immediately of any data that looks incorrect.

Lenny Rachitsky (00:45:08):
I know that importing incorrect data can cause all kinds of pain for your customers, and quickly lose their trust. Christina, thank you for joining us. And if you want to learn more, head on over to oneschema.co. That's oneschema.co.

(00:45:23):
I want to come back to that you talked about researchers and their relationship with product teams. I imagine a lot of innovation comes from researchers just like having an inkling and then building something amazing and then releasing it, and some ideas come from PMs and engineers. How do those teams collaborate? Does every team have a PM? Is it a lot of research-led stuff? Give us a sense of just where ideas and products come from mostly.

Kevin Weil (00:45:49):
It's an area where we're evolving a lot. I'm really excited about it, frankly. I think if you go back a couple of years when ChatGPT was just getting started, obviously, I wasn't in OpenAI, but...

Kevin Weil (00:46:00):
Obviously I wasn't an Open AI, but... We were more of a pure research company at the time. Chat GPT, if you remember, was a low-key research preview.

Lenny Rachitsky (00:46:14):
For many years.

Kevin Weil (00:46:15):
Yeah. It wasn't a thing that the team launched thinking it was going to be this massive product.

Lenny Rachitsky (00:46:19):
Oh, Chat GPT. Yeah.

Kevin Weil (00:46:21):
And it was just a way that we were going to let people play with and iterate on the models. So we were primarily a research company, a world-class research company, and as ChatGPT has grown and as we've built our B-to-B products and our APIs and other things, now we're more of a product company than we were. I still think we can't... Open AI should never be a pure product company. We need to be both a world-class research company and a world-class product company, and the two need to really work together, and that's the thing that I think we've been getting much better at over the last six months. If you treat those things separately and the researchers go do amazing things and build models and then they get to some state and then the product and engineering teams go take them and do something with them, we're effectively just an API consumer of our own models.

(00:47:17):
The best products though are going to be, it's like I was talking about with deep research, it's a lot of iterative feedback. It's understanding the products you're trying to sell or the problems you're trying to solve, building evals for them, using those evals to go gather data and fine-tune models to get them to be better at these use cases that you're looking to solve. It's a huge amount of back and forth to do it well. And I think the best products are going to be ENG product design and research working together as a single team to build novel things. So that's actually how we're trying to operate with basically anything that we build. It's a new muscle for us because we're kind of new as a product company, but it's one that people are really excited about because we've seen every time we do it, we build something awesome, and so now every product starts like that.

Lenny Rachitsky (00:48:07):
How many product managers do you have at Open AI? I don't know if you share that number, but if you do.

Kevin Weil (00:48:11):
Not that many, actually. I don't know, 25. Maybe it's a little more than that. My personal belief is that you want to be pretty PM light as an organization just in general. I say this with love because I am a PM, but too many PMs causes problems. We'll fill the world with decks and ideas versus execution. So I think it's a good thing when you have a PM that is working with maybe slightly too many engineers because it means they're not going to get in and micromanage. You're going to leave a lot of influence and responsibility with the engineers to make decisions. It means you want to have really product-focused engineers, which we're fortunate to have. We have an amazingly product focused, high agency engineering team. But when you have something like that, you have a team that feels super empowered, you have a PM that's trying to really understand the problems and gently guide the team a little bit but has too much going on to get too far into the details, and you end up being able to move really fast. So that's kind of the philosophy we take.

(00:49:23):
We want Product ENG leads and product engineers all the way through. We want not too many PMs, but really awesome, high quality ones, and so far that seems to be working pretty well.

Lenny Rachitsky (00:49:36):
I imagine being a PM at Open AI is a dream come true for a lot of people. At the same time, I imagine it's not a fit for a lot of people. There's researchers involved, very product minded engineers. What do you look for in the PMs that you hire there for folks that are like, "Maybe I shouldn't go work there. I shouldn't even think about that."

Kevin Weil (00:49:54):
I think, I've said this a few times, but high agency is something that we really look for, people that are not going to come in and wait for everyone else to allow them to do something, they're just going to see a problem and go do it. It's just a core part of how we work. I think people that are happy with ambiguity, because there is a massive amount of ambiguity here, it is not the kind of place, and we have trouble sometimes with more junior PMs because of this, because it's just not the place where someone is going to come in and say, "Okay, here's the landscape, here's your area, I want you to go do this thing." And that's what you want as an early career PM. I mean, no one here has time and the problems are too ill-formed and we're figuring them all out as we go. And so high agency, very comfortable with ambiguity, ready to come in and help execute and move really quickly. That's kind of our recipe.

(00:50:55):
And I think also happy leading through influence because... I mean it's usual as a PM, people don't report to you, your team doesn't report to you, et cetera, but you also have the complexity of a research function, which is even more sort of self-directed and it's really important to build a good rapport with the research team. I think the EQ side of things is also super important for us.

Lenny Rachitsky (00:51:24):
I know at most companies, a PM comes in and they're just like, "Why do we need you?" And as a PM you have to earn trust and help people see the value, and I feel like at Open AI it's probably a very extreme version of that where they're like, "Why do we need this person? We have researchers, engineers, what are you going to do here?"

Kevin Weil (00:51:40):
Yeah, I think people appreciate it done right, but you bring people along. I think one of the most important things a PM can do well is be decisive. So there's a real fine line. You don't want to be making... I mean it's kind of like, I don't love the PM as the CEO of the product illusion all the time, but just like Sam in his role would be making mistakes if he made every single decision in every meeting that he was in. And he would also be making mistakes if he made no decisions in any meetings that he was in, right? It's understanding when to defer to your team and to let people innovate. And when there is a decision to be made that people either don't feel comfortable with or don't feel empowered to make, or a decision that has too many different disparate pros and cons that are spread out across a big group and someone needs to be decisive and make a call, it's a really important trait of a CEO.

(00:52:41):
It's something Sam does well, and it's also a really important trait of a PM kind of at a more microscopic level. So because there's so much ambiguity, it's not obvious what the answer is in a lot of cases, and so having a PM that can come in and... And by the way, this doesn't need to be a PM, I'm perfectly happy if it's anybody else, but I kind of look to the PM to say, if there's ambiguity and no one's making a call, you better make sure that we get a call made and we move forward.

Lenny Rachitsky (00:53:07):
This touches on a few posts I've done of just, where is AI going to take over work that we do versus help us with various work? So let me come at this question from a different direction of just how AI impacts product teams and hiring, things like that. So first of all, there's all this talk of LM's doing our coding for us, and 90% of code is going to be written by AI in a year. Dario at Anthropic said that. At the same time, you guys are all hiring engineers like crazy, PM's like crazy. Every function is dead, but you're still hiring every single one. I guess just, first of all, let me just ask this, how do you and the team, say engineers, PMs, use AI in your work? Is there anything that's really interesting or things that you think people are sleeping on in how you use AI in your day-to-day work?

Kevin Weil (00:53:52):
We use it a lot. I mean, every one of us is in Chat GPT all the time summarizing docs, using it to help write docs with GPTs that write product specs and things like that, all the stuff that you would imagine. I mean talk about writing evals, you can actually use models to help you write evals and they're pretty good at it. That all said, I'm still sort of disappointed by us, and I really mean me, in, if I were to just teleport my five-year-old self leading product at some other company into my day job, I would recognize it still. And I think we should be in a world, certainly a year from now, probably even more now, where I almost wouldn't recognize it because the workflows are so different and I'm using AI so heavily, and I'd still recognize it today. So I think in some sense, I'm not doing a good enough job of that.

(00:54:46):
Just to give an example, why shouldn't we be vibe coding demos right, left and center? Instead of showing stuff in Figma, we should be showing prototypes that people are vibe coding over the course of 30 minutes to illustrate proofs of concept and to explore ideas. That's totally possible today, and we're not doing it enough. Actually, our chief people officer, Julia, was telling me the other day, she vibe coded an internal tool that she had at a previous job that she really wanted to have here at Open AI and she opened, I don't know, Windsurf or something, and vibe coded it. How cool is that? And if our chief people officer is doing it, we have no excuse to not be doing it more.

Lenny Rachitsky (00:55:34):
That's an awesome story. And some people may not have heard this term vibe coding. Can you describe what that means?

Kevin Weil (00:55:40):
Yeah, I think this was Andrej's term.

Lenny Rachitsky (00:55:45):
Karpathy. Yeah.

Kevin Weil (00:55:46):
Andrej Karpathy. Yeah. So you have these tools like Cursor and Windsurf and GitHub Copilot that are very good at suggesting what code you might want to write. So you can give them a prompt and they'll write code and then as you go to edit it, it's suggesting what you might want to do. And the way that everyone started using that stuff was, give it a prompt, have it do stuff, you go edit it, give it a prompt, and you're kind of really going back and forth with the model the whole time. As the models are getting better and as people are getting more used to it, you can kind of just let go of the wheel a little bit. And when the model's suggesting stuff, it's just like, tap, tap, tap, tap, tap. Keep going. Yes, yes, yes, yes, yes.

(00:56:29):
And of course the model makes mistakes or it does something that doesn't compile, but when it doesn't compile, you paste the error in and you say, go, go, go, go, go. And then you test it out and it does one thing that you don't want it to do, so you enter in an instruction and say, go, go, go, go, go, and you just let the model do its thing. And it's not that you would do that for production code that needed to be super tight today yet, but for so many things, you're trying to get to a proof of concept, you're getting to a demo and you can really take your hands off the wheel and the model will do an amazing job, and that's vibe coding.

Lenny Rachitsky (00:57:05):
That's an awesome explanation. I think the pro version of that, which is, I think, the way Andre even described it as you talk, there's a step like whisper or super whisper or something like that where you're talking to the model, not even typing.

Kevin Weil (00:57:17):
Yeah, totally.

Lenny Rachitsky (00:57:19):
Oh man. So let me just ask, I guess, when you look at product teams in the future, you talked about how you guys should be doing this more, instead of designs, having prototypes, what do you think might be the biggest changes in how product teams are structured or built? Where do you think things are going in the next few years?

Kevin Weil (00:57:36):
I think you're definitely going to live in a world where you have researchers built into every product team. And I don't even mean just at foundation model companies because I think the future... Actually, frankly one thing that I'm sort of surprised about about our industry in general is that there's not a greater use of fine-tuned models. A lot of people... These models are very good, so our API does a lot of things really well, but when you have particular use cases, you can always make the model perform better on a particular use case by fine-tuning it. It's probably just a matter of time. Folks aren't quite comfortable yet with doing that in every case. But to me, there's no question that that's the future. Models are going to be everywhere just like transistors are everywhere, AI is going to be just a part of the fabric of everything we do, but I think there are going to be a lot of fine-tuned models because why would you not want to more specifically customize a model against a particular use case?

(00:58:37):
And so I think you're going to want sort of quasi researcher machine learning engineer types as part of pretty much every team because fine-tuning a model is just going to be part of the core workflow for building most products. So that's one change that maybe you're starting to see at foundation model companies that will propagate out to more teams over time.

Lenny Rachitsky (00:58:57):
I'm curious if there's a concrete example that makes that real, and I'll share one that comes to mind as you talk, which is, when you look at Cursor and Windsurf, something I learned from those founders is that they use a Sonnet, but then they also have a bunch of custom models that help along the edges that make the specific experience that's not just generating code even better like auto-complete and looking ahead to where things are going. So is that one or any other examples of which you... What is a fine-tuned model? Do you think teams will be building with these researchers on their teams?

Kevin Weil (00:59:29):
Yeah. I mean, so when you're a model, you're basically giving the model a bunch of examples of the kinds of things you want it to be better at. So it's, "Here's a problem, here's a good answer. Here's a problem, here's a good answer," Or, "Here's a question, here's a good answer times a thousand or 10,000." And suddenly you're teaching the model to be much better than it was out of the gate at that particular thing. We use it everywhere internally. We use ensembles of models much more internally than people might think. So it's not, "I have 10 different problems. I'll just ask baseline GPT four oh about a bunch of these things." If we have 10 different problems, we might solve them using 20 different model calls, some of which are using specialized fine-tuned models, they're using models of different sizes because maybe you have different latency requirements or cost requirements for different questions.

(01:00:32):
They are probably using custom prompts for each one. Basically you want to teach the model to be really good at... You want to break the problem down into more specific tasks versus some broader set of high level tasks. And then you can use models very specifically to get very good at each individual thing. And then you have an ensemble that tackles the whole thing. I think a lot of good companies are doing that today. I still see a lot of companies giving the model single, generic, broad problems versus breaking the problem down, and I think there will be more breaking the problem down using specific models for specific things, including fine tuning.

Lenny Rachitsky (01:01:15):
And so in your case, because this is really interesting, is that you're using different levels of Chat GPT, like a 1 0 3 and stuff that's earlier because it's cheaper.

Kevin Weil (01:01:24):
There'll be parts of our internal stack. I'll give you an example. Customer support, with 400 plus million weekly active users, we get a lot of inbound tickets. I don't know how many customer support folks we have, but it's not very many, 30, 40, I'm not sure, way smaller than you would have at any comparable company, and it's because we've automated a lot of our flows. We've got most questions using our internal resources, knowledge base, guidelines for how we answer questions, what kind of personality, et cetera. You can teach the model those things and then have it do a lot of its answers automatically, or where it doesn't have the full confidence to answer a particular question, it can still suggest an answer, request a human to look at it and then that human's answer actually is its own sort of fine tuning data for the model. You're telling it the right answer in a particular case.

(01:02:29):
We're using... At various places. Some of these places, you want a little bit more reasoning, is not super latency sensitive, so you want a little more reasoning, and we'll use one of our O series models. In other places, you want a quick check on something and so you're fine to use four oh mini, which is super fast and super cheap. In general, it's like specific models for specific purposes and then you ensemble them together to solve problems. By the way, again, not unlike how we as humans solve problems, a company is arguably an ensemble of models that have all been fine tuned based on what we studied in college and what we have learned over the course of our careers. We've all been fine tuned to have different sets of skills and you group them together in different configurations and the output of the ensemble is much better than the output of any one individual.

Lenny Rachitsky (01:03:20):
Kevin, you're blowing my mind. That sounds exactly correct. And also, different people, you pay them less, they cost less to talk to, some people take a long time to answer, some people hallucinating. This is...

Kevin Weil (01:03:38):
I'm telling you. This is a mental model but really does work in thinking...

Lenny Rachitsky (01:03:41):
Oh, right. Yeah. This is great. Some people are visual, they want to dry out their thinking, some people want to talk word cell. Wow, this is a really good metaphor. So again, coming back to your advice here because I love that we circled back to it, you're finding a really good way to think about how to design great AI experiences and LMs, I guess, specifically is think about how a person would do this.

Kevin Weil (01:04:01):
Well, it's maybe not always the answer is to think about how a person would do it, but sometimes to gain intuition for how you might solve a problem, you think about what an equivalent human would do in those situations and use that to at least gain a different perspective on the problem.

Lenny Rachitsky (01:04:18):
Wow, this is great.

Kevin Weil (01:04:22):
Because some of this really is talking to a model. There's a lot of prior art because we talk to other humans all the time and encounter them in all sorts of different situations, and so there's a lot to learn from that.

Lenny Rachitsky (01:04:34):
Okay, so speaking of humans, I want to chat about the future a little bit. So you have three kids, and a community member asked me this hilarious question that I think it's something a lot of people are thinking about. So this is Patrick [inaudible 01:04:47]. I worked with him at Airbnb. He says ask what he's encouraging his kids to learn to prepare for the future. I'm worried my 6-year-old by the year 2036 will face a lot of competition trying to get into the top roofing or plumbing programs and need a backup plan.

Kevin Weil (01:05:02):
That's funny. So our kids, we have a 10 year old and eight year old twins, so they're still pretty young. It's amazing how AI native they are. It's completely normal to them that there are self-driving cars. That they can talk to AI all day long. They have full conversations with Chat GPT and Alexa and everything else. I don't know, who knows what the future holds? I think things like coding skills are going to be relevant for a long time, who knows? But I think if you teach your kids to be curious, to be independent, to be self-confident, you teach them how to think, I don't know what the future holds, but I think that those are going to be skills that are going to be important in any configuration of the future. And so it's not like we have all the answers, but that's how Elizabeth and I think about our kids.

Lenny Rachitsky (01:06:02):
And do you find that AI... There's a lot of talk about AI tutoring. Is that something you guys are doing? I know they're using Chat GPT, I love all the photos you post where they're playing with prompts and stuff, but I guess is there anything there you're experimenting with or you think is going to become really important?

Kevin Weil (01:06:16):
This is something that... It's maybe the most important thing that AI could do. Maybe that's a grand statement. There are lots of important things that AI can do, including speeding up the pace of fundamental science research and discovery, which maybe is actually the most important thing AI can do. But one of the most important things would be personalized tutoring. And it kind of blows my mind that there is still... I know there are a bunch of good products out there. Khan Academy does great things. They're a wonderful partner of ours. Vinod Khosla has a non-profit that's doing some really interesting stuff in this space and is making an impact. But I'm kind of surprised that there isn't a 2 billion kid AI personalized tutoring thing because the models are good enough to do it now, and every study out there that's ever been done seems to show that when you have... Like, education is still important, but when you combine that with personalized tutoring, you get multiple standard deviation improvements in learning speed.

(01:07:31):
And so it's uncontroversial, it's good for kids, it's free. Chat GPT is free, you don't need to pay, and the models are good enough. It still just kind of blows my mind that there isn't something amazing out there that our kids are using and your future kids are using, and people in all sorts of places around the world that aren't as lucky as our kids to be able to have this sort of built-in, solid education. Again, Chat GPT is free. People have Android devices everywhere. I really just think this could change the world and I'm surprised it doesn't exist and I want it to exist.

Lenny Rachitsky (01:08:08):
This kind of touches on something I want to spend a little time on, which is a lot of people also worry a lot about AI, where it's going, they worry about jobs it's going to take, they worry about the super intelligence squashing humanity in the future. What's your perspective on that and just the optimistic case that I think people need to hear?

Kevin Weil (01:08:27):
I mean, I'm a big technology optimist. I think if you look over the last 200 years, maybe more, technology has driven a lot of the advancements that have made us the world and the society that we are today. It drives economic advancements, it drives geopolitical advancements, quality of life, longevity advancement. I mean, technology's at the root of just about everything, so I think there are very few examples where this is anything but a great thing over the longer term. That doesn't mean that there aren't...

Kevin Weil (01:09:00):
... a great thing over the longer term. That doesn't mean that there aren't temporary dislocations or where there aren't individuals that are impacted, and that matters too. So it can't just be that the average is good. You've got to also think about how you take care of each individual person as best you can.

(01:09:18):
It is something that we think a lot about and as we work with the administration, as we work with policy, we try and help wherever we can. We do a lot with education. One of the benefits here is that ChatGPT is also perhaps the best reskilling app you could possibly want. It knows a lot of things. It can teach you a lot of things if you're interested in learning new things.

(01:09:43):
These are very real issues. I'm super optimistic about the long run, and we're going to need to do everything we can as a society to ensure that we make this transition as graceful and as well-supported as we can.

Lenny Rachitsky (01:09:59):
To give people a sense of where things might be going. That's a big question in a lot of people's minds. So someone asked this question that I love, which is, "AI is already changing, creative work in a lot of different ways, writing and design and coding, what do you think is the next big leap? What should we be thinking is the next big leap in AI-assisted creativity specifically, and then just broadly, where do you think things are going to be going in the next few years?"

Kevin Weil (01:10:23):
Yeah. This is also an area where I'm a big optimist. If you look at Sora, for example. I mean we talked about ImageGen earlier and the absolute fount of creativity that people are putting across Twitter and Instagram and other places. I am the world's worst artist like the worst. Maybe the only thing I'm worse at than art is singing. Give me a pencil and a pad of paper and I can't draw better than our eight-year-old. But give me ImageGen and I can think some creative thoughts and put something into the model and suddenly have output that I couldn't have possibly done myself. That's pretty cool.

(01:11:09):
Even you look at folks that are really talented. I was talking to a director recently about Sora, someone who's directed films that we would all know, and he was saying, for a film that he's doing, take the example of some sort of sci-fi-ish, think of Star Wars, and you've got some scene where there's a plane zooming into some Death Star-like thing. And so you've got the plane looking at the whole planet, and then you want to cut to a scene where the plane's kind of at the ground level, and all of a sudden you see the city and everything else. How are we going to manage that cut scene? And that transition?

(01:11:51):
And he was saying, "In the world of two years ago, I would have paid a 3D effects company a hundred grand and they would've taken a month, and they would've produced two versions of this cut scene for me. And I would've evaluated them. We would've chosen one, because what are you going to do? Pay another 50 grand and wait another month. And we would've just gone with it. And it would be fine. Movies are great. I love them. And there've been..."

(01:12:25):
Obviously, we can do great things with the technology that we've had, but you now look at what you can do with Sora. And his point was, "Now, I can use Sora, our video model, and I can get 50 different variations of this cut scene just me brainstorming into a prompt and the model brainstorming a little bit with me. I've got 50 different versions. And then of course, I can iterate off of those and refine them and take different ideas. And now I'm still going to go to that 3D effects studio to produce the final one, but I'm going to go having brainstormed and had a much more creative approach with an outcome that's much better. And I did that assisted by AI."

(01:13:08):
My personal view on creativity in general is that it's no one's going to... You don't type into Sora like, "Make me a great movie." It requires creativity and ingenuity, and all these things, but it can help you explore more. It can help you get to a better final result. So, again, I tend to be an optimist in most things, but actually, I think there's a very good story here.

Lenny Rachitsky (01:13:31):
I know Sam Altman, I think it was him who tweeted recently, the creative writing piece that you guys are working on where it's... He is very bad at writing creative stuff, and he shared an example where it's actually really good. I imagine that's another area of investment.

Kevin Weil (01:13:43):
Yeah, there's some exciting stuff happening internally with some new research techniques. We'll have more to say about that at some point. But yeah, Sam sometimes likes to show off some of the stuff that's coming, which is smart. By the way, it's very indicative of this iterative deployment philosophy. We don't have some breakthrough and keep it to ourselves forever, and then bestow it upon the world someday. We kind of just talk about the things we're working on and share when we can and launch early and often, and then iterate in public. I really like that philosophy.

Lenny Rachitsky (01:14:22):
I love all these hints that a few things coming. I know you can't say too much. You talked about how there might be a coding leap coming in the near future maybe by the time this comes out. Is there anything else people should be thinking about, might be coming in the near future? Any things you can tease that are interesting? Exciting?

Kevin Weil (01:14:38):
Man, this hasn't been enough for you?

Lenny Rachitsky (01:14:41):
Only everything is getting better every day.

Kevin Weil (01:14:44):
Yeah. I'm like, man, I hope we get some of this stuff out before the episode launches so-

Lenny Rachitsky (01:14:49):
This is your new timebox.

Kevin Weil (01:14:50):
... I don't piss people off. The amazing thing to me is we were talking earlier about how far models have come in just a couple of years. If you went back to GPT-3, you'd be disgusted by how bad it was, even though Lenny of two years ago was mind-blown by how good these were. And for a long time, we were iterating every six to nine months on a new GPT model. It was like GPT-3, GPT-3.5, 4, and now with this o-series of reasoning models, we're moving even faster. Every roughly three months, maybe four months, there's a new o-series model, and each of them is a step up in capability.

(01:15:41):
And so the capabilities of these models are increasing at a massive pace. They're also getting cheaper as they scale. You look at where we were even a couple of years ago. I think the original, I don't know, what was it, GPT-3.5 or something was like 100 x the cost of GPT-4o mini today in the API. A couple of years, you've gone down two orders of magnitude in cost for much more intelligence. And so I don't know where there's another series of trends like that in the world. Models are getting smarter, they're getting faster, they're getting cheaper, and they're getting safer too. They hallucinate less every iteration.

(01:16:27):
And so the Morse Law and transistors becoming ubiquitous. That was a law around doubling the number of transistors on a chip every 18 months. If you're talking about something where you're getting 10 x every year, that's a massively steeper exponential. And it tells us that the future is going to be very different than today. The thing I try and remind myself is, the AI models that you're using today is the worst AI model you will ever use for the rest of your life. And when you actually get that in your head, it's kind of wild.

Lenny Rachitsky (01:17:08):
I was going to actually say the same thing, and that's the thing that always sticks with me when I watch this thing. You're talking about Sora, and I imagine many people hearing that are like, "No, no. It's not actually ready. It's not good enough. It's not going to be as good as a movie I see in the theater." But the point is what you just made that this is the worst it's going to be. It will only get better.

Kevin Weil (01:17:25):
Yeah, model maximalism. Just keep building for the capabilities that are almost there, and the model's going to catch up and be amazing.

Lenny Rachitsky (01:17:35):
Escape to where the puck is going to be.

Kevin Weil (01:17:36):
Yeah.

Lenny Rachitsky (01:17:38):
This reminds me, I was just using... I was duplifying everything the other day and I was just like, "What is taking so long."

Kevin Weil (01:17:38):
As one does.

Lenny Rachitsky (01:17:43):
Just like cut... What was that?

Kevin Weil (01:17:45):
I said, as one does.

Lenny Rachitsky (01:17:46):
As one does these days. I was just like, "It's taking a minute to generate this image of my family in this amazing way." Come on, what's taking so long. You just get so used to magic happening in front of you.

Kevin Weil (01:17:57):
Yeah, totally.

Lenny Rachitsky (01:17:59):
Okay, final question. This is going to go in a completely different direction. A lot of people asked about this. So famously, you led this project at Facebook called Libra, which is now called Novi. A lot of people always wondered, "What happened there? That was a really cool idea." I know some people have a sense there's regulation challenges, things like that. I don't know if you've talked about this much. So I guess, could you just give people a brief summary of just what is Libra? This project you working on, and just what happened, and how you feel about it?

Kevin Weil (01:18:26):
Yeah. I mean, David Marcus led it, and I happily work for him and with him. I think he's a visionary and also a mentor and a friend. Honestly, Libra is probably the biggest disappointment of my career. When I think about the problems we were solving, which are very real problems. If you look at, for example, the remittance space, people sending money to family members in other countries, it is maybe... I mean it's incredibly regressive, right? People that don't have the money to spend are having to pay 20% to send money home to their family. So outrageous fees, it takes multiple days, you have to go then pick up cash from... It's all bad.

(01:19:11):
And here we are with 3 billion people using WhatsApp all over the world, talking to each other every day, especially friends and family, and exactly the kind of people who'd send money to each other. Why can't you send money as immediately, as cheaply, as simply as you send a text message? It is one of those things when you sit back and think about it, that should just exist. And that was what we set out to try and do.

(01:19:41):
Now, I don't think we played all of our cards perfectly. If I could go back and do things, there are a bunch of things I would do differently.

(01:19:50):
We tried to get it all at once. We tried to launch a new blockchain. It was a basket of currencies originally. It was integration into WhatsApp and Messenger, and I think the whole world kind of went like, "Oh my God, that's a lot of change at once." And it happened also to be at the time that Facebook was at the absolute nadir of its reputation. And so that didn't help. It was also not the Messenger that people wanted for this kind of change. We knew all that going in, but we went for it.

(01:20:21):
I think there are a bunch of ways that we could do that that would've introduced the change a little bit more gently, maybe still gotten to that same outcome, but fewer new things at once and introduced the new things one at a time. Who knows? Those were decisions we made together. So we all own them. Certainly, I own them. But it fundamentally disappoints me that this doesn't exist in the world today because the world would be a better place if we'd been able to ship that product. I would be able to send you 50 cents in WhatsApp for free. It would settle instantly. Everybody would have a balance in their WhatsApp account. We'd be transact... I mean, it should exist.

(01:21:03):
I don't know. To be honest, the current administration is super friendly to crypto. Facebook's reputation, Meta's reputation is in a very different place. Maybe they should go build it now.

Lenny Rachitsky (01:21:13):
I was looking at the history of it, and apparently, they sold the tech to some private equity company for 200 million bucks.

Kevin Weil (01:21:19):
Yeah, yeah, and-

Lenny Rachitsky (01:21:21):
They had to buy it back.

Kevin Weil (01:21:23):
There are a couple of current blockchains that are built on the tech because the tech was open-sourced from the beginning. Aptos and Mistin are two companies that are built off of this tech. So at least all of the work that we did, did not die and lives on in these two companies, and they're both doing really well. But still, we should be able to send each other money in WhatsApp, and we can't today.

Lenny Rachitsky (01:21:49):
Hear, hear. Well, thanks for sharing that story, Kevin. Is there anything else you want to share or maybe a last negative advice or insight before we get to our very exciting lightning round?

Kevin Weil (01:21:58):
Ooh, the lightning round. Let's just go do that.

Lenny Rachitsky (01:22:01):
Let's do it. With that, Kevin, we reached our very exciting lightning round. Are you ready?

Kevin Weil (01:22:05):
Yeah.

Lenny Rachitsky (01:22:06):
Let's do it. Okay. What are two or three books that you find yourself recommending most to other people?

Kevin Weil (01:22:12):
Co-Intelligence by Ethan Mollick, a really good book about AI and how to use it in your daily life as a student, as a teacher. He's super thoughtful. Also, by the way, a very good follow on Twitter. The Accidental Superpower by Peter Zion. Very good if you're interested in geopolitics and the forces that sort of shape the dynamics happening. And then I really enjoyed Cable Cowboy, I don't know who the author is, but the biography of John Malone. Just fascinating. If you like business, especially if you want to get into... I mean the man was an incredible dealmaker and shaped a lot of the modern cable industry. So that was a good biography.

Lenny Rachitsky (01:22:53):
These are all first-time mentions, which is always a great,

Kevin Weil (01:22:56):
Oh, good.

Lenny Rachitsky (01:22:56):
Next question. Do you have a favorite recent movie or TV show that you really enjoyed?

Kevin Weil (01:23:02):
I wish I had time to watch a TV show, so I'm-

Lenny Rachitsky (01:23:06):
Just Sora videos.

Kevin Weil (01:23:07):
Yeah, right. I don't know. When I was a kid, I read the Wheel of Time series and now Amazon has it as they're in the third season of it, so I want to watch that. I haven't yet. Top Gun 2 was an awesome movie. I think that's no longer new.

Lenny Rachitsky (01:23:28):
That shows when the last time you watched a movie was.

Kevin Weil (01:23:31):
But I like the idea. I want more Americana. I want more being proud of being strong. And I thought Top Gun 2 did a really good job of that. Pride and patriotism, I think the US could use more of that.

Lenny Rachitsky (01:23:48):
Is there a favorite product that you've recently discovered that you really love, other than your super intelligence internal tool that you all have access to? I'm just joking.

Kevin Weil (01:23:56):
That's right. Internal AGR.

Lenny Rachitsky (01:23:57):
Yeah, that's right.

Kevin Weil (01:24:01):
Well, I think vibe coding with products like Windsurf is just super fun. I'm having a great time doing that. I still just love that our chief people officer vibe coded some tools. Maybe the other one is Waymo. Every chance I get, I'll take a Waymo. It's just a better way of riding, and it still feels like the future. So they've done an amazing job.

Lenny Rachitsky (01:24:24):
That's awesome. By the way, I had the founder of Windsurf on the podcast. It might come out before this or after this. And also Cursor's CEO is coming on the podcast either before or after this.

Kevin Weil (01:24:32):
Oh, cool. I have a ton of respect for what those guys are doing. Those are awesome products.

Lenny Rachitsky (01:24:36):
Just changing the way everyone builds product. No big deal.

Kevin Weil (01:24:38):
Yeah.

Lenny Rachitsky (01:24:40):
A couple more questions. Do you have a favorite life motto that you often repeat yourself, find really useful in work or in life?

Kevin Weil (01:24:47):
Yeah. So actually, this is interestingly enough, it is more of a philosophy, but then I thought Zuck encapsulated it one time on a Facebook earnings call. So I actually had this made into a poster. It sits in my room. But somebody was asking Mark. This is literally on an earnings call, so it's like an analyst on an earnings call asking him. It was some quarter when Facebook had grown a lot. This was back in the 20 teens sometime, I think. But he's like, "So what did you do? What was it that you launched? What was the one thing that drove all this growth for you?" And he said something to the effect of, "Sometimes it's not any one thing, it's just good work consistently over a long period of time." And that's always stuck with me.

(01:25:33):
And I think it is. I mean I run ultra marathons. It's like it's just about grinding. I think people too often look for the silver bullet when a lot of life and a lot of excellence is actually showing up day in and day out, doing good work, getting a little bit better every single day, and you may not notice it over a week or even a month. And a lot of people then kind of get dismayed and stop. But actually, you keep doing it. The gains keep compounding. And over the course of a year, two years, five years, it adds up like crazy. So good work consistently over a long period of time.

Lenny Rachitsky (01:26:13):
I love that. I got to make a poster of this now. That is-

Kevin Weil (01:26:15):
We'll get you one.

Lenny Rachitsky (01:26:15):
I so resonate with that. Okay, I'll take it. That is so good. Okay, final question. I'm going to ask if you have any prompting tricks, and I'm going to set it up first. But think about if you have a trick that you could recommend to people for prompting LLMs better. I had a guest, Alex Komorowski, come on the podcast. He's from Stripe and writes his weekly reflections on what's happening in the world. A lot of them are AI-related.

(01:26:36):
And he once described an LLM as a zip file of all human knowledge. All the answers are in there, and you just need to figure out the right question to ask to get the answer to every problem basically. And so it just reminded me how important prompt engineering is and knowing how to prompt well. You're constantly prompting ChatGPT. What's one tip, one trick that you found to be helpful in helping you get what you want?

Kevin Weil (01:27:00):
Well, I'll say, first of all, I want to kill the idea that you have to be a good prompt engineer. I think if we do our jobs, that stops being true. It's just one of those sharp edges of models that experts can learn. But then, just over time, you shouldn't need to know all that. The same way you used to have to get deep into, "What's your storage engine in MySQL? Are you using InnoDB 4.1?" There's still use cases for that if you're at the deep edge of MySQL performance. But most people don't need to care. And you shouldn't need to care about minute details of prompting if AI is really going to become broadly adopted.

(01:27:39):
But today, we're not totally there. I think by the way, we are making progress there. I think there is less prompt engineering than there had to be before. But in line with some of the fine-tuning stuff I was talking about and the importance of giving examples, you can do effectively poor man's fine-tuning by including examples in your prompt of the kinds of things that you might want and a good answer. So like, "Here's an example and here's a good answer. Here's an example, and here's a good answer. Now, go solve this problem for me." And the model really will listen and learn from that.

(01:28:15):
Not as well as if you do a full fine-tune, but much more than if you don't provide any examples. And I think people don't do that often enough.

Lenny Rachitsky (01:28:24):
That's awesome. One tip that I heard, I'm curious if this works is you tell it, "This is very, very important to my career." Make it really understand like, "Someone will die if you don't answer me correctly." Does that work?

Kevin Weil (01:28:36):
It's really weird. There's probably a good explanation for this. But you can also say things. So, yes, I think there is some validity to that. You can also say things like, "I want you to be Einstein. Now, answer this physics problem for me," or, "You are the world's greatest marketer, the world's greatest brand marketer. Now here's a naming question." And there is something where it sort of shifts the model into a certain mindset that can actually be really positive.

Lenny Rachitsky (01:29:10):
I use that tip all the time actually. I always... When I'm coming up with questions for interviews and I use it occasionally to come up with things I haven't thought of, I actually type, "You're the world's best podcast interviewer."

Kevin Weil (01:29:21):
Right.

Lenny Rachitsky (01:29:21):
I have Kevin Weil coming on the pod... Yeah, it actually works.

Kevin Weil (01:29:25):
By the way, back to our other point that we made a few times. You do do that sometimes with people. You sort of put them... You frame things, you get them into a certain mindset, and the answer is completely different. So I think there are human analogs of this one more time.

Lenny Rachitsky (01:29:42):
Kevin, this was incredible. I was just thinking about a way to end this. The way I feel like... I feel like not only are you at the cutting edge of the future. You and the team are kind of actually the edge that is creating the future. And so it's a real honor to have you on here and to talk to you and to hear where you think things are going and what we need to be thinking about, so thank you for being here, Kevin.

Kevin Weil (01:30:07):
Oh, thank you so much for having me. I get to work with the world's best team, and all credit to them, but really appreciate you having me on. It's been super fun.

Lenny Rachitsky (01:30:17):
I forgot to ask you the two final questions. Where can folks find you if they want to reach out, and how can listeners be useful to you?

Kevin Weil (01:30:24):
I am @kevinweil, K-E-V-I-N-W-E-I-L on pretty much every platform. I'm still a Twitter DAU after all these years. I guess an X DAU, LinkedIn, wherever. And I think the thing I would love from people, give me feedback. People are using ChatGPT. Tell me where it's working really well for you and where you want us to double down. Tell me where it's failing. I'm very active and engaged on Twitter. I love hearing from people, what's working and what's not, so don't be shy.

Lenny Rachitsky (01:30:56):
And I learned following you helps you figure out all the stuff that you're launching. You share all the things that are going out every day, or week, month, so that's also a benefit. And by the way, 400 million weekly active users all emailing you feedback. Here we go.

Kevin Weil (01:31:08):
Yes, let's do it.

Lenny Rachitsky (01:31:09):
It's going to work out great. Okay. Well, thank you, Kevin. Thanks for being here.

Kevin Weil (01:31:12):
All right, man, thanks so much. See you soon.

Lenny Rachitsky (01:31:13):
Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

