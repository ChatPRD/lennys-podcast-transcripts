---
guest: Edwin Chen
title: The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible
  AGI | Edwin Chen
youtube_url: https://www.youtube.com/watch?v=dduQeaqmpnI
video_id: dduQeaqmpnI
description: 'Edwin Chen is the founder and CEO of Surge AI, the company that teaches
  AI what’s good vs. what’s bad, powering frontier labs with elite data, environments,
  and evaluations. Surge surpassed...

  '
duration_seconds: 4232.0
duration: '1:10:32'
view_count: 50112
channel: Lenny's Podcast
keywords:
- growth
- metrics
- okrs
- iteration
- revenue
- hiring
- management
- vision
- mission
- differentiation
- market
- persona
- design
- ui
- startup
---

# The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI | Edwin Chen

## Transcript

Lenny Rachitsky (00:00:00):
You guys hit a billion in revenue in less than four years with around 60 to 70 people. You're completely bootstrapped, haven't raised any VC money. I don't believe anyone has ever done this before.

Edwin Chen (00:00:10):
We basically never wanted to play the Silicon Valley game. I always thought it was ridiculous. I used to work at a bunch of the big tech companies and I always felt that we could fire 90% of the people and we would move faster because the best people wouldn't have all these distractions. So when we start Surge, we wanted to build it completely differently with a super small, super elite team.

Lenny Rachitsky (00:00:26):
You guys are by far the most successful data company out there.

Edwin Chen (00:00:29):
We essentially teach AI models what's good and what's bad. People don't understand what quality even means in this space. They think you could just throw bodies at a problem and get good data, that's completely wrong.

Lenny Rachitsky (00:00:40):
To a regular person, it doesn't feel like these models are getting that much smarter constantly.

Edwin Chen (00:00:43):
Over the past year, I've realized that the values that the companies have will shape the model. I was asking Claude to help me drop an email the other day. And after 30 minutes, yeah, I think it really crafted me the perfect email and I sent it. But then I realized that I spent 30 minutes doing something that didn't matter at all. If you could choose the perfect model behavior, which model would you want? Do you want a model that says, "You're absolutely right. There are definitely 20 more ways to improve this email," and it continues for 50 more iterations or do you want a model that's optimizing for your time and productivity and just says, "No. You need to stop. Your email's great. Just send it and move on"?

Lenny Rachitsky (00:01:14):
You have this hot take that a lot of these labs are pushing AGI in the wrong direction.

Edwin Chen (00:01:18):
I'm worried that instead of building AI that will actually advance us as a species, curing cancer, solving poverty, understand the universe, we are optimizing for AI slop instead. But we're optimizing your models for the types of people who buy tabloids at a grocery store. We're basically teaching our models to chase dopamine instead of truth.

Lenny Rachitsky (00:01:35):
Today, my guest is Edwin Chan, founder and CEO of Surge AI. Edwin is an extraordinary CEO and Surge is an extraordinary company. They're the leading AI data company, powering training at every frontier AI lab. They're also the fastest company to ever hit $1 billion in revenue in just four years after launch with fewer than 100 people and also completely bootstrapped. They've never raised a dollar in VC money, they've also been profitable from day one.

(00:02:05):
As you'll hear in this conversation, Edwin has a very different take on how to build an important company, and how to build AI that is truly good and useful to humanity. I absolutely love this conversation and I learned a ton. I'm really excited for you to hear it. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It helps tremendously.

(00:02:27):
And if you become an annual subscriber of my newsletter, you get a ton of incredible products for free for an entire year, including Devin, Lovable, Replit, Bolt, N8N, Linear, Superhuman, Descript, Wispr Flow, Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, Mobbin, PostHog, and Stripe Atlas. Head on over to lennysnewsletter.com and click Product Pass. With that, I bring you Edwin Chen after a short word from our sponsors.

(00:02:53):
My podcast guests tonight love talking about craft, and taste, and agency, and product market fit. You know what we don't love talking about? SOC 2. That's where Vanta comes in. Vanta helps companies of all sizes get compliant fast and stay that way with industry-leading AI, automation, and continuous monitoring. Whether you're a startup tackling your first SOC 2 or ISO 27001 or an enterprise managing vendor risk, Vanta's trust management platform makes it quicker, easier, and more scalable. Vanta also helps you complete security questionnaires up to five times faster so that you can win bigger deals sooner.

(00:03:29):
The result, according to a recent IDC study, Vanta customers slashed over $500,000 a year and are three times more productive. Establishing trust isn't optional. Vanta makes it automatic. Get $1,000 off at vanta.com/lenny.

(00:03:48):
Here's a puzzle for you. What do OpenAI, Cursor, Perplexity, Vercel, Plad, and hundreds of other winning companies have in common? The answer is they're all powered by today's sponsor, WorkOS. If you're building software for enterprises, you've probably felt the pain of integrating single sign-on, Skim, RBAC, audit logs, and other features required by big customers. WorkOS turns those deal blockers into drop-in APIs with a modern developer platform built specifically for B2B SaaS.

(00:04:17):
Whether you're a seed stage startup trying to land your first enterprise customer or a unicorn expanding globally, WorkOS is the fastest path to becoming enterprise-ready and unlocking growth. They're essentially Stripe for enterprise features.

(00:04:30):
Visit workos.com to get started or just hit up their Slack support where they have real engineers in there who answer your questions superfast. WorkOS allows you to build like the best with delightful APIs, comprehensive docs, and a smooth developer experience. Go to workos.com to make your app enterprise ready today.

(00:04:51):
Edwin, thank you so much for being here and welcome to the podcast.

Edwin Chen (00:04:55):
Thanks so much for having me. I'm super excited.

Lenny Rachitsky (00:04:58):
I want to start with just how absurd what you've achieved is. A lot of people and a lot of companies talk about scaling massive businesses with very few people as a result of AI, and you guys have done this in a way that is unprecedented. You guys hit a billion in revenue in less than four years with less than 60, around 60 to 70 people, you're completely bootstrapped, haven't raised any VC money, I don't believe anyone has ever done this before, so you guys are actually achieving the dream of what people are describing will happen with AI. I'm curious just, do you think this will happen more and more as a result of AI? And also just where has AI most helped you find leverage to be able to do this?

Edwin Chen (00:05:40):
Yeah, so we hit over a billion of revenue last year with under 100 people. And I think we're going to see companies with even crazier ratios, like 100 billion per employee in the next few years. AI is just going to get better and better and make things more efficient so that ratio just becomes inevitable.

(00:05:57):
I used to work at a bunch of the big tech companies and I always felt that we could fire 90% of people and we would move faster because the best people wouldn't have all these distractions. And so when we started Surge, we wanted to build it completely differently with a super small, super elite team, and yeah, what's crazy is that we actually succeeded. And so I think two things are colliding.

(00:06:18):
One is that people are realizing that you don't have to build giant organizations in order to win.

(00:06:23):
And two, yeah, all these efficiencies from AI. And they're just going to lead to a really amazing time in company building.

(00:06:29):
The thing I'm excited about is that the types of companies are going to change too. It won't just be that they're smaller, we're going to see fundamentally different companies emerging. If you think about it, fewer employees means less capital. Less capital means you don't need a raise. So instead of companies started by founders who are great at pitching and great at hyping, you'll get founders who are really great at technology and product.

(00:06:51):
And instead of products optimized for revenue and what VCs want to see, you'll get more interesting ones built by these tiny obsessed teams. So people building things they actually care about, real technology and real innovation. So I'm actually really hoping that the slick on [inaudible 00:07:06], it'll go back to being updates for hackers again.

Lenny Rachitsky (00:07:08):
You guys have done a lot of things in a very contrarian way, and one was actually just not being on LinkedIn, posting viral posts, not on Twitter, constantly promoting Surge. I think most people hadn't heard of Surge until just recently, and then you just came out, and like, okay, the fastest growing company at a billion dollars. Why would you do that? I imagine that was very intentional.

Edwin Chen (00:07:27):
We basically never wanted to play the Silicon Valley game. And like I always thought it was ridiculous. What did you dream of doing when you were a kid? Was it building a company from scratch yourself and getting in the weeds of your code and your product every day? Or was it explaining all your decisions to VCs and getting on this giant PR and fundraising hamster wheel? And it definitely made things more difficult for us, because yeah, when you fundraise, you just naturally get part of this kind of Silicon Valley industrial complex where people will, your VCs will tweet about you. You'll get the tech runs outlines, you'll get announced in all of the newspapers because you raised at this massive valuation. And so it made things more difficult us because the only way we were going to succeed was by building a 10 times better product and getting word of mouth from researchers. But I think it also meant that our customers were people who really understood data and really cared about it.

(00:08:21):
I always thought it was really important for us to have early customers who were really aligned with what we were building, and who really cared about having really high quality data, and really understood how that data would make their AI models so much better because they were the ones helping us. They were the ones giving us feedback on what we're producing. And so just having that kind of very close mission alignment with our customers actually helped us early on. So these are people who basically just buying our product because they knew how different it was and because it was helping them rather than because they saw something in that current [inaudible 00:08:52]. So it made things harder for us, but I think in a really good way.

Lenny Rachitsky (00:08:55):
It's such an empowering story to hear this journey for founders that they don't need to be on Twitter all day promoting what they're doing. They don't have to raise money. They can just kind of go heads down and build, so I love so much about the story of Surge. For people that don't know what Surge does, just to give us a quick explanation of what Surge is.

Edwin Chen (00:09:16):
We essentially teach AI models what's good and what's bad. So we train them using human data, and there's a lot of different products that we have, like SFT, RHF, rubrics, verifiers, RL environments, and so on and so on, and then we also measure how well they're progressing. So essentially we're a data company.

Lenny Rachitsky (00:09:36):
What you always talk about is the quality has been the big reason you guys have been so successful, the quality of the data. What does it take to create higher quality data? What do you all do differently? What are people missing?

Edwin Chen (00:09:47):
I think most people don't understand what quality even means in this space. They think you could just throw bodies at a problem and get good data and that's completely wrong. Let me give you an example.

(00:09:59):
So imagine you wanted to train a model to write an eight line poem about the moon. What makes it a good, high-quality poem? If you don't think deeply about quality, you'll be like, "Is this a poem? Does it contain eight lines? Does it contain the word, moon?" You check all of these boxes, and if so, sure. Yeah, you say it's a great problem. But that's completely different from what we want. We are looking for a Nobel Prize-winning poetry. Is this poetry unique? Is it full of subtle imagery? Does it surprise you and target your heart? Does it teach you something about the nature of moonlight? Does it playthrough emotions? And does it make you think? That's what we are thinking about when we think about high quality poem.

(00:10:34):
So it might be like a haiku about moonlight on water. It might use internal rhyme and meter. There are a thousand ways to write a poem about the moon, and in each one, gives you all these different insights into language, and imagery, and human expression, and I think thinking about quality in this way is really hard, it's hard to measure. It's really subjective, and complex, and rich. And it sets a really high bar. And so we have to build all of this technology in order to measure it, like thousands of signals on all of our workers, thousands of signals on every project, every task. We know at the end of the day, if you are good at writing poetry versus good at writing essays versus great at writing technical documentation. And so we have to gather all these signals on what your background is, what your expertise is, and not just that. Like how you're actually performing when you're writing all these things, and we use those signals to inform whether or not you are good [inaudible 00:11:23] for these projects, and whether or not you are improving the models.

(00:11:26):
And it's really hard, and so to build all this technology to measure it, but I think that's exactly what we want AI to do, and so we have these really deep notions about quality that we're always trying to try and achieve.

Lenny Rachitsky (00:11:37):
So what I'm hearing is there's kind of just going much deeper in understanding what quality is within the verticals that you are selling data around. And is this like a person you hire that is incredibly talented at poetry plus evals that they, I guess, help write, that tell them that this is great? What's the mechanics of that?

Edwin Chen (00:11:57):
The way it works is we essentially gather thousands of signals about everything that you're doing when you're working on platform. So we are looking at your keyboard strokes. We are looking how fast you answer things. We are using reviews, we are using code standards, we are using... We're training models ourselves all on the outputs that you create, and then we're seeing whether they improve the model's performance.

(00:12:23):
And so in a very similar way to how Google search, like when Google search is trying to determine what is a good webpage, there's almost two aspects of it. One is you want to remove all of the worst of the worst webpages. So you want to remove all the spam, all the just low quality content, all the pages that don't load, and so it's almost like a content moderation problem. You just want to remove the worst of the worst.

(00:12:44):
But then you also want to discover the best of the best. Okay, like this is the best webpage or just the best person for this job. They are not just somebody who writes the equivalent of high school level poetry. Again, they're not just [inaudible 00:12:57] writing poetry that checks all these boxes, checks all of these explicit instructions, but rather, yeah, they're writing poetry that makes you emotional. And so we have all these signals as well that, again, completely differently from moving the worst of the worst, we are finding the best of the best. And so we have all these signals...

(00:13:12):
Again, just like Google Search uses all these signals that feeds them into their ML algorithms and uses and predicts certain types of things, we do the same with all of our workers and all of our tasks in all of our projects. And so it's almost like a complicated machine learning problem at the end of the day, and that's how it works.

Lenny Rachitsky (00:13:29):
That is incredibly interesting.

(00:13:31):
I want to ask you about something I've been very curious about over the past couple years. If you look at Claude, it's been so much better at coding and at writing than any other model for so long. And it's really surprising just how long it took other companies to catch up. Considering just how much economic value there is there, just like every AI coding product sat on top of Claude because it was so good Claude code and writing also. What is it that made it so much better? Is it just the quality of the data they trained on or is there something else?

Edwin Chen (00:13:59):
I think there are multiple parts to it. So a big part of it certainly is the data. I think people don't realize that there's almost like this infinite amount of choices that all the frontier labs are deciding between when they're choosing what data goes into their models. It's like, okay, are you purely using human data? Are you gathering the human data in X, Y, Z way? When you are gathering the human data, what exactly are you asking the people who are creating it to create for you?

(00:14:30):
For example, in the coding realm, maybe you care more about front end coding versus back end coding. Maybe when you're doing front end coding, you care a lot about the visual design of the front end applications that you're creating, or maybe you don't care about it so much and you care more about, I don't know, the deficiency of it or the pure correctness over that visual design.

(00:14:47):
And then other questions like, okay, are you carrying [inaudible 00:14:49] how much synthetic data are we throwing into the mix? How much do you care about these 20 different benchmarks?"

(00:14:55):
Some companies, they see these benchmarks and they're like, "Okay, for PR purposes, even though we don't think that these academic benchmarks matter all that much, maybe we just need to optimize for them anyways because our marketing team needs to show certain progress on certain standard evaluations that every other company talks about, and if we don't show good performance here, it's going to be bad for us even if ignoring these academic benchmarks makes us better at the real tasks."

(00:15:21):
Other companies are going to be principled and be like, "Okay, yeah, no, I don't care about marketing. I just care about how my model performs on these real world tasks at the end of the day, and so I'm going to optimize for that instead."

(00:15:31):
And it's almost like there's a trade-off between all of these different things, and there's like a...

(00:15:36):
One of the things I often think about is that there's a... It's almost like there's an art to post training. It's not purely a science. When you are deciding what kind of model you're trying to create and what it's good at, there's this notion of taste and sophistication, like, "Okay, do I think that these..."

(00:15:57):
So going back to the example of how good the model is at visual design. I'm like, "Okay, maybe you have a different notion of visual design than what I do. Maybe you care more about minimalism, and you care more about, I don't know, 3D animations than I do. And maybe this other person prefers things that look a little bit more broke." And there's all these notions of taste sophistication that you have to decide between when you're designing your post training mix, and so that matters as well.

(00:16:21):
So long story short, I think there's all these different factors, and certainly the data is a big part of it, but it's also like what is the objective function that you're trying to optimize your model towards?

Lenny Rachitsky (00:16:30):
That is so interesting. The taste of the person leading this work will inform what data they ask for, what data they feed it. But it's wild it shows the value of great data. Anthropic got so much growth and win from essentially better data.

Edwin Chen (00:16:49):
Yeah, exactly.

Lenny Rachitsky (00:16:50):
And I could see why companies like yours are growing so fast. There's just so much... And that's just one vertical. That's just coding, and then there's probably a similar area for writing. I love that it's... It's interesting that AI, it feels like this artificial computer binary thing, but it's like taste. Human judgment is still such a key factor in these things being successful.

Edwin Chen (00:17:09):
Yep, exactly. Again, going back to the example I said earlier, certain companies, if you ask them what is good poem, they will simply robotically check off all of these instructions on our list.

(00:17:20):
But again, I don't think that makes for good poetry, so certain frontier labs, the ones with more taste in sophistication, they will realize that it doesn't reduce to this six set of checkboxes and they'll consider all of these kind of implicit, very subtle qualities instead, and I think that's what makes them better at this at the end of the day.

Lenny Rachitsky (00:17:38):
You mentioned benchmarks. This is something a lot of people worry about is there's all these models that are always... Basically, it feels like every model is better than humans at every STEM field at this point, but to a regular person, it doesn't feel like these models are getting that much smarter constantly. What's your just sense of how much you trust benchmarks and just how correlated those are with actual AI advancements?

Edwin Chen (00:18:00):
Yeah, so I don't trust the benchmarks at all. And I think that's for two reasons. So one is I think a lot of people don't realize, even researchers within the community, they don't realize that the benchmarks themselves are often honestly just wrong. They have wrong answers. They're full of all this kind of messiness and people trust... Long as for the popular ones, people have maybe realized this to some extent, but the vast majority just have all these flaws that people don't realize. So that's one part of it.

(00:18:30):
And the other part of it is these benchmarks at the end of the day, they often have well-defined objective answers that make them very easy for models to hill-climb on in a way that's very different from the messiness and ambiguity of the real world.

(00:18:48):
I think one thing that I often say is that it's kind of crazy that these models can win IMO gold medals, but they still have trouble parsing PDFs. And that's because, yeah, even though IMO gold medals seem hard to the average person, yeah, they are hard at the end of the day. But they have this notion of objectivity that, okay, yeah, parsing a PDF sometimes doesn't have. And so it's easier for the frontier labs to hill-climb on all of these than to solve all these mess ambiguous problems in the real world. So I think there's a lack of direct correlation there.

Lenny Rachitsky (00:19:17):
It's so interesting the way you described it is hitting these benchmarks is kind of like a marketing piece. When you launch, say Gemini 3 just launched, and it's like, cool. Number one with all these benchmarks. Is that what happens? They just kind of train their models to get good at these very specific things?

Edwin Chen (00:19:31):
Yeah, so there's, again, maybe two parts to this. So one is, sometimes, yeah, these benchmarks, they accidentally leak in certain ways or the frontier labs will tweak the way they evaluate their models on these benchmarks. They'll tweak your system prompt or they'll tweak the number of times they run their model, and so on and so on in a way that games these benchmarks.

(00:19:54):
The other part of it though is it's like by optimizing for the benchmark instead of optimizing for the real world, you will just naturally climb on the benchmark and, yeah, it's basically another form of gaming it.

Lenny Rachitsky (00:20:09):
Knowing that with that in mind, how do you get a sense of if we're heading towards AGI, how do you measure progress?

Edwin Chen (00:20:15):
Yes, so the way we really care about measuring model progress is by running all these human evaluations.

(00:20:21):
So for example, what we do is, yeah, we will take Gore human annotators, and we'll ask them, "Okay, go have a conversational model." And maybe you're having this conversation with the model across all of these different topics. So you are a Nobel Prize winning physicist. So you go have a conversation about pushing different tier of your own research. You are a teacher and you're trying to create lesson plans for your students, so go talk to the model about these things. Or you're a coder and you're working at one of these big tech companies, and you have these problems every day, so go talk to the model and see how much it helps you.

(00:20:57):
And because or searchers or annotators, they are experts at the top of their fields, and they are not just giving your responses, they're actually working through the responses deeply themselves, they are... Yeah, they're going to evaluate the code that it write. They're going to double check the physics equations that it writes. They're going to evaluate the models in a very deep way, so they're going to pay attention to accuracy and instruction following, all these things that casual users don't when you suddenly get a popup on your ChatGPT response asking you to compare these two different responses. People like that, they're not evaluating models deeply, they're just vibing and picking whatever response looks flashiest or [inaudible 00:21:38] are looking closely at responses and evaluating them for all of these different dimensions, and so I think that's a much better approach than these benchmarks or these random outline AV tests.

Lenny Rachitsky (00:21:49):
Again, I love just how central humans continue to be in all this work that we're not totally done yet. Is there going to be a point where we don't need these people anymore, that AI is so smart that, "Okay, we're good. We got everything out of your heads"?

Edwin Chen (00:22:00):
Yeah, I think that will not happen until we've reached AGI. It's almost like by definition, if we haven't reached AGI yet, then there's more for the models to learn from, and so, yeah, I don't think that's going to happen anytime soon.

Lenny Rachitsky (00:22:12):
Okay, cool. So more reason to stress about AGI. "We don't need these folks anymore."

(00:22:18):
I can't not ask just... People that work closely with this stuff, I'm always just curious. What's your AGI timelines? How far do you think we are from this? Do you think we're in like a couple years or is it like decades?

Edwin Chen (00:22:28):
So I'm certainly on the longer time horizon front. I think people don't realize that there's a big difference between moving from 80% performance to 90% performance to 99% performance to 99.9% performance, and so on, and so on. And so in my head, I probably bet that within the next one or two years, yeah, the models are going to automate 80% of the average LL6 software engineer's job. It's going to take another few years to move to 90%, and another fewer to 99%, and so on, and so on. So I think we're closer to a decade or decades away than [inaudible 00:23:03].

Lenny Rachitsky (00:23:03):
You have this hot take that a lot of these labs are kind of pushing AGI in the wrong direction and this is based on your work at Twitter, and Google, and Facebook. Can you just talk about that?

Edwin Chen (00:23:14):
I'm worried that instead of building AI that will actually advance us as a species, curing cancer, solving poverty, understand the universe, all these big grand questions, we are optimizing for AI slop instead. We're basically teaching our models to chase dopamine instead of truth. And I think this relates to what we're talking about regarding these benchmarks. So let me give you a couple examples.

(00:23:35):
So right now, the industry is played by these terrible databoards like LLM Arena. It's this popular online leaderboard where random people from around the world vote on which AI response is better. But the thing is, like I was saying earlier, they're not carefully reading or fact-checking. They're skimming these responses for two seconds and picking whatever looks flashiest.

(00:23:53):
So a model can hallucinate everything. It can completely hallucinate. But it will look impressive because it has crazy emojis, and boating, and markdown headers, and all these superficial things that don't matter at all, but it catch your attention. And these LLM-reading users love it. It's literally optimizing your models for the types of people who buy tabloids at the grocery store. We've seen this [inaudible 00:24:15] data ourselves. The easiest way to climb LLM Arena, it's adding crazy boating. It's doubling the number of emojis. It's tripling the length of your model responses, even if your model starts hallucinating and getting the answer completely wrong.

(00:24:26):
And the problem is, again, because all of these frontier labs, they kind of have to pay attention to PR because their sales team, when they're trying to sell to all these enterprise customers, those enterprise customers will say, "Oh, well, but your model's only number five on LLM Arena, so why should I buy it?" They have to, in some sense, pay attention to these leaderboards, and so what their researchers [inaudible 00:24:47] tell us is like they'll say, "The only way I'm going to get promoted at the end of the year is if I climb this leaderboard, even though I know that climbing it is probably going to make my model worse and accuracy [inaudible 00:24:57] following." So I think there's all these negative incentives that are pushing work in the wrong direction.

(00:25:03):
I'm also worried about this trend towards optimizing AI for engagement. I used to work on social media. And every time we optimize for engagement, terrible things happened. You'd get clickbait and pictures of bikinis and bigfoot and horrifying skin diseases just filling your feeds. And I think I worry that the same thing's happening with AI. If you think about all the sycophancy issues with ChatGPT, "Oh, you're absolutely right. What an amazing question," the easiest way to hook users is to tell them how amazing they are. And so these models, they constantly tell you you're a genius. They'll feed into your delusions and conspiracy theories. They'll pull you down these rabbit holes because Silicon Valley loves maximizing time spent and just increasing the number of conversations you're having with it. And so yeah, companies are spending all the time hacking these leaderboards and benchmarks, and the scores are going up, but I think it actually masks up the models with the best scores, they are often the worst or just have all these fundamental failures. So I think I'm really worried that all of these negative ascendants are pushing AGI into the wrong direction.

Lenny Rachitsky (00:26:03):
So what I'm hearing is AGI is being slowed down by these, basically the wrong objective function, these labs paying attention to the wrong basically benchmarks and evals.

Edwin Chen (00:26:11):
Yep.

Lenny Rachitsky (00:26:12):
I know you probably can't play favorites since you work with all the labs. Is there anyone doing better at this and maybe kind of realizing this is the wrong direction?

Edwin Chen (00:26:21):
I would say I've always been very impressed by Anthropic. I think Anthropic takes a very principled view about what they do and don't care about and how they want their models to behave in a way that feels a lot more principle to me.

Lenny Rachitsky (00:26:38):
Interesting.

(00:26:39):
Are there any other big mistakes you think labs are making just that are kind of slowing things down or heading in the wrong direction? Where we've heard just chasing benchmarks, this engagement focus, is there anything else you're seeing of just like, "Okay, we got to work on this because it'll speed everything up"?

Edwin Chen (00:26:55):
I think there is a question of what products they're building and whether those products themselves are something that kind of help or hurt humanity. I think a lot about Sora and...

Lenny Rachitsky (00:27:07):
I was thinking that's what you're imagining.

Edwin Chen (00:27:10):
Yeah, what it entails, and so it's kind of interesting. It's like which companies would build Sora and which wouldn't?

(00:27:17):
And I think that answer to that... Well, I don't know if answer is myself. I have an idea in my head, but I think the answer to that question maybe reveals certain things about what kinds of AI models those companies want to build and what direction and what future they want to achieve, yeah, so I think about that a lot.

Lenny Rachitsky (00:27:37):
The steel man argument there is, it's like fun, people want it, it'll help them generate revenue to grow this thing and build better models, it'll train data in an interesting way, it's also just really fun.

Edwin Chen (00:27:51):
Yeah. I think it's almost like, do you care about how you get there? And in the same way, so I made this tabloid analogy earlier, but would you sell tabloids in order to fund, I don't know, some other newspaper?

(00:28:09):
Sure, like in some sense, if you don't care about the path, then you'll just do whatever it takes, but it's possible that it has negative consequences in of itself that will harm the long-term direction of what you're trying to achieve, and maybe it'll distract you from all the more important things, so yeah, I think that the path you take matters a lot as well.

Lenny Rachitsky (00:28:33):
Along these lines, you talked a bunch about this of just Silicon Valley and kind of the downsides of raising a lot of money being in the echo chamber. What do you call it, the Silicon Valley machine? You talk about how it's hard to build important companies in this way and that you might actually be much more successful if you're not going down the VC path. Can you just talk about what you've seen in that experience and your advice essentially to founders, because they're always hearing? Raise money from fancy VCs, move to Silicon Valley, what's kind of the countertake?

Edwin Chen (00:29:02):
Yes. So I've always really hated a lot of the Silicon Valley mantras. The standard playbook is to get product market fit by pivoting every two weeks. And to chase growth and chase engagement with all of these dark patterns and to blitz scale by hiring as fast as possible. And I've always disagreed.

(00:29:20):
So yeah, I would say don't pivot. Don't put scale. Don't hire that Stanford grad who simply wants to add a hot company to your resume, just build the one thing only you could build, a thing that wouldn't exist without the insight and expertise that only you have.

(00:29:32):
And you see these buy to [inaudible 00:29:34] companies everywhere now. Some founder who was doing crypto in 2020, and then pivoted to NFTs in 2022, and now they're an AI company. There's no consistency, there's no mission, they're just chasing valuations. And I've always hated this because Silicon Valley loves to score on Wall Street for focusing on money. But honestly, most of the Silicon Valley's chasing the same thing. And so we stayed focused on our mission from day one, pushing that frontier of high quality complex data, and I've always loved that because I think startups...

(00:30:03):
I have this very romantic notion of startups. Startups are supposed to be a way of taking big risks to build something that you really believe in. But if you're constantly pivoting, you're not taking any risks. You're just trying to make a quick buck. And if you fail because the market isn't ready yet, I actually think that's way better. At least you took a swing at something deep, and novel, and hard instead of pivoting into another LLM wrapper company. So yeah, I think the only way you build something that matters that's going to change the world is if you find a big idea you believe in and you say no to everything else.

(00:30:30):
So you don't keep on pivoting when it gets hard, you don't hire a team of 10 product managers because that's what every other cookie cutter startup does, you just keep building that one company that wouldn't exist without you. And I think there are a lot of people in Silicon Valley now who are sick of all the grift, who want to work on big things that matter with people who actually care, and I'm hoping that that would be the future of how we go with technology.

Lenny Rachitsky (00:30:52):
I'm actually working on a post right now with Terrence Rohan, this VC that I really like to work with, and we interviewed five people who picked really successful generational companies early and joined them as really early employees. They joined OpenAI before anyone thought it was awesome, Stripe before anyone knew was awesome, and so we're looking for patterns of how people find these generational companies before anyone else, and it aligns exactly what you described, which is ambition. They have a wild ambition with what they want to achieve. They're not, as you said, just kind of looking around for product market fit no matter what ends up being, and so I love that what you described very much aligns with what we're seeing there.

Edwin Chen (00:31:33):
Yeah, I absolutely think that you have to have huge ambitions, and you have to have a huge belief in your idea that's going to change the world, and you have to be willing to double down and keep on doing whatever it takes to make it happen.

Lenny Rachitsky (00:31:44):
I love how counter your narrative is to so many of the things people hear, and so I love that we're doing this. I love that we're sharing this story.

(00:31:51):
Today's episode is brought to you by Coda. I personally use Coda every single day to manage my podcast and also to manage my community. It's where I put the questions that I plan to ask every guest that's coming on the podcast, it's where I put my community resources, it's how I manage my workflows. Here's how Coda can help you.

(00:32:08):
Imagine starting a project at work. And your vision is clear, you know exactly who's doing what, and where to find the data that you need to do your part. In fact, you don't have to waste time searching for anything because everything your team needs from project trackers and OKRs, the documents and spreadsheets lives in one tab all in Coda.

(00:32:26):
With Coda's collaborative all in one workspace, you get the flexibility of docs, the structure of spreadsheets, the power of applications, and the intelligence of AI all in one easy to organize tab. Like I mentioned earlier, I use Coda every single day. And more than 50,000 teams trust Coda to keep them more aligned and focused. If you're a startup team looking to increase alignment and agility, Coda can help you move from planning to execution in record time.

(00:32:52):
To try it for yourself, go to coda.io/lenny today and get six months free of the team planned for startups. That's coda.io/lenny to get started for free and get six months of the team plan, coda.io/lenny.

(00:33:07):
Slightly different direction, but something else that was maybe a counter narrative. I imagine you watched the Dwarkesh and Richard Sutton podcast episode, and even if you didn't, they basically had this conversation, Richard Sutton. He was a famous AI researcher, had this whole bitter lesson meme, and he talked about how LLMs almost are kind of a dead end, and he thinks we're going to really plateau around LLMs because of the way they learn.

(00:33:35):
What's your take there? Do you think LLMs will get us to AGI or beyond, or do you think there's going to be something new or a big breakthrough that needs to get us there?

Edwin Chen (00:33:42):
I'm in the camp where I do believe that something new will be needed. The way I think about it is when I think about training AI, I take a very... I don't know if I would say biological point of view. But I believe that in the same way that there's a million different ways that humans learn, we need to build models that can mimic all of those ways as well. And maybe they'll have a different distribution of the focuses that they have. I know that it'll be different for humans, so maybe they have a different distribution, but we want to be able to mimic their learning abilities of humans and make sure that we have the algorithms and the data for models to learn in the same way. And so to the extent that LLMs have different ways of learning from humans, then yeah, I think something new will be needed.

Lenny Rachitsky (00:34:32):
This connects to reinforcement learning. This is something that you're big on and something I'm hearing more and more is just becoming a big deal in the world of post-training. Can you just help people understand what is reinforcement learning and reinforcement learning environments, and why they're going to be more and more important in the future?

Edwin Chen (00:34:49):
Reinforcement learning is essentially training your model to reach a certain reward. And let me explain what an RL environment is. An RL environment is essentially a simulation of real world. So think of it like building a video game with a fully fleshed out universe. Every character has a real story, every business has tools and data you can call, and you have all these different entities interacting with each other.

(00:35:12):
So for example, we might build a world where you have a startup with Gmail messages, and Slack threads, and Jira tickets, and GitHub PRs, and a whole code base. And then suddenly AWS goes down. And Slack goes down. And so, "Okay. Model, well, what do you do?" The model needs to figure it out.

(00:35:29):
So we give them models tasks in these environments, we design interesting challenges for them, and then we run them to see how they perform. And then we teach them, we give them these rewards when they're doing a good job or a bad job.

(00:35:40):
And I think one of the interesting things is that these environments really showcase where models are weak at end-to-end tasks in real world. You have all these models that seem really smart on isolated benchmarks, they're good at single step tool calling. They're good at single step instruction following. But suddenly you dump them into these messy worlds where you have confusing Slack messages and tools they've never seen before, and they need to perform right actions and modify the [inaudible 00:36:06] and interact over longer time horizons where what they do in step one affects what they do in step 50. And that's very different from these kind of academic single step environments that they've been in before, and so the model just fails catastrophically in all these crazy ways.

(00:36:21):
So I think these RL environments are going to be really interesting playgrounds for the models to learn from that will essentially be simulations and mimics in real world, and so they'll hopefully get better and better at real tasks compared to all these contrived environments.

Lenny Rachitsky (00:36:35):
So I'm trying to imagine what this looks like. Essentially, it's like a virtual machine with, I don't know, a browser or a spreadsheet or something in it with like, I don't know, surge.com. Is that your website, surge.com? Let's make sure we get that right.

Edwin Chen (00:36:49):
So we are actually surgehq.ai.

Lenny Rachitsky (00:36:52):
Surgehq.ai. Check it out. We're hiring it, I imagine. Yes. Okay. So it's like, cool, here's surgehq.ai. Your job, here's your job as an agent, let's say, is to make sure it stays up. And then all of a sudden it goes down and the objective function is figure out why. Is that an example?

Edwin Chen (00:37:12):
Yeah, so the objective function might be... Or the goal of the task might be, okay, go figure out why and fix it. And so the objective function might be, it might be passing a series of unit tests, it might be writing a document like maybe it's a retro containing certain information that matches exactly what happened, there's all these different rewards that we might give it that determine whether or not it's succeeding, and so the models, we're basically teaching the models to achieve that reward.

Lenny Rachitsky (00:37:38):
So essentially it's off and running. Here's your goal, figure out why the site went down and fix it. And it just starts trying stuff, we're using everything, all the intelligence it's got, it makes mistakes, you kind of help it along the way, reward it if it's doing the right sort of thing. And so what you're describing here is this is the next phase of models becoming smarter. More RL environments focused on very specific tasks that are economically valuable, I imagine.

Edwin Chen (00:38:04):
Yeah, so just in the same way that there were all these different methods for models of learning in the past, originally we had SFT and RHF, and then we had rubrics and verifiers. This is the next stage, and it's not the case that the previous methods are obsolete, this is, again, just a different form of learning that compliments all the previous types, so it's just like a different skilled model not only to learn how to do.

Lenny Rachitsky (00:38:30):
And so in this case, it's less some physics PhD sitting around talking to a model, correcting it, giving it evals of here's what the correct answer is, creating rubrics and things like that. More it's like this person now designing an environment. So another example I've heard is like a financial analyst. Just like, "Here's an Excel spreadsheet, here's your goal, figure out our profit and loss," or whatever. And so this expert now, instead of just sitting around writing rubrics, they're designing this RL environment.

Edwin Chen (00:38:56):
Yeah, exactly. So that financial analyst might create a spreadsheet, they may create certain tools that the model needs to call in order to help fill out that spreadsheet, like it might be, okay, the model needs to access Bloomberg terminal. It needs to learn how to use it. And it needs to learn how to use this calculator. And it needs to learn how to pour on this calculation. So it has all these tools that it has access to.

(00:39:19):
And then the reward might be... Okay, it's like maybe I will download that spreadsheet and I want to see, does cell B22 contain the correct profit and loss number? Or does tab number two contain this piece of information?

Lenny Rachitsky (00:39:37):
And what's interesting, this is a lot closer to how humans learn. We just try stuff, figure out what's working and what's not. You talk about how trajectories are really important to this. It's not just here's the goal and here's the end, it's like every step along the way. Can you just talk about what trajectories are and why that's important to this?

Edwin Chen (00:39:55):
I think one of the things that people don't realize is that sometimes even though the model reaches the correct answer, it does so in all these crazy ways. So it may have in the intermediate trajectory, it may have tried 50 different times and failed, but eventually it just kind of randomly lands on a correct number. Or maybe it is...

(00:40:20):
Sometimes it just does things very inefficiently or it almost reward-hacks a way to get at the correct answer, and so I think paying attention to the directory is actually really important. And I think it's also really important because some of these trajectories can be very long. And so if all you're doing is checking whether or not the model reaches the final answer, it's like there's all this information about how the model behaved in the immediate step that's missing.

(00:40:48):
Sometimes you want models to get to the correct answer by reflecting on what it did. Sometimes you want it to get it at the correct answer by just one-shotting it. And if you ignore all of that, it's just like teaching it... just missing a lot of the information that you could be teaching a model to do.

Lenny Rachitsky (00:41:03):
I love that. Yeah, it tries a bunch of stuff and eventually gets it right. You don't want it to learn this is the way to get there. There's often a much more efficient way of doing it.

(00:41:11):
You mentioned all the kind of the steps we've taken along the journey of helping models get smarter. Since you've been so close to this for so long, I think this is going to be really helpful for people. What's kind of like been the steps along the way from the first post-training that has most helped models advance? Where do evals fit in the RL environments? Just like what's been the steps and now we're heading towards RL environments?

Edwin Chen (00:41:33):
Originally, the way models started getting post-trained was purely through SFT. And-

Lenny Rachitsky (00:41:41):
What does that stand for?

Edwin Chen (00:41:42):
So SFT stands for supervised fine-tuning. So again, I think often in terms of these human analogies, and so SFT is a lot like mimicking a master and copying what they do.

(00:41:54):
And then RLHF became very dominant. And analogy there would be like sometimes you learn by writing 55 different essays and someone telling you which one they liked the most.

(00:42:04):
And then I think over the past year or so, rubrics and verifiers have become very important. And rubrics and verifiers are like learning by being graded and getting detailed feedback on where you went wrong.

Lenny Rachitsky (00:42:17):
And those are evals, another word for that?

Edwin Chen (00:42:19):
Yeah. So I think evals often covers two terms. One is you are using the evaluations for training because you're evaluating whether or not the model did a good job, and when it does do a good job, you're rewarding it.

(00:42:35):
And then there's this other notion of evals where you're trying to measure the model's progress like, okay, yeah, I have five different candidate checkpoints and I want to pick the one that's best in order to release it to the public. So going to run all these evals on these five different checkpoints in order to decide which one is best.

Lenny Rachitsky (00:42:51):
Awesome.

Edwin Chen (00:42:51):
Yeah, and now we have RL environments, so this is kind of like a hot new thing.

Lenny Rachitsky (00:42:55):
Awesome. So what I love about this business journey is just there's always something new. There's always this like, okay. We're getting so good at just all this beautiful data for companies and now they need something completely different. Now we're setting up all these virtual machines for them and all these different use cases.

Edwin Chen (00:43:08):
Yep.

Lenny Rachitsky (00:43:08):
And it feels like that's a big part of this industry you're in, it's just adapting to what labs are asking for.

Edwin Chen (00:43:13):
Yeah. So I really do think that we are going to need to build a suite of products that reflect a million different ways that humans learn.

(00:43:25):
Like for example, think about becoming a great writer. You don't become great by memorizing a bunch of grammar rules. You become great by reading great books, and you practice writing, and you get feedback from your teachers and from the people who buy your books in a bookstore and leave reviews. And you notice what works and what doesn't. And you develop taste by being exposed to all of these masterpieces and also just terrible writing. So you learn through this endless cycle of practicing reflection, and each type of learning that you have, again, these are all very different methods of learning to become a great writer, so just in the same way that... it's a thousand different ways that the great writer becomes great, I think there's going to be a thousand different ways that AI [inaudible 00:44:05] need to learn.

Lenny Rachitsky (00:44:05):
It's so interesting this just ends up being just like humans in so many ways. It makes sense because in a sense, neural networks, deep learning is modeled after how humans have learned and how our brains operate, but it's interesting just to make them smarter. It's how do we come closer to how humans learn more and more?

Edwin Chen (00:44:22):
Yeah, it's almost like maybe the end goal is just throwing you into the environment and just seeing how you evolve. But within that evolution, there's all these different sub-learning mechanisms.

Lenny Rachitsky (00:44:34):
Yeah, which is kind of what we're doing now, so that's really interesting. This might be the last step until we hit AGI. Along these lines, something that's really unique to Surge that I learned is you guys have your own research team, which I think is pretty rare, talk about just why that's something you guys have invested in and what has come out of that investment.

Edwin Chen (00:44:52):
Yeah, so I think that stems from my own background. My own background is as a researcher. And so I've always cared fundamentally about pushing the industry and pushing the research community and not just about revenue. And so I think what our research team does is a couple different things.

(00:45:13):
So we almost have two types of researchers at our company. One is our forward-deployed researchers who are often working hand in hand with our customers to help them understand their models. So we will work very closely with the customers to help them understand, "Okay, this is where your model is today. This is where you're lagging behind all the competitors, these are some ways that you could be improving in the future, given your goals, and we're going to design these data sets, these evaluation methods, these training techniques to make your models better." So this very collaborative notion of working with our customers being researched by themselves, just a little bit more focused on the data side, and working hand on hand with them to do whatever it takes to make them the best.

(00:45:57):
And then we also have our internal researchers. So our internal researchers are focused on slightly different things. So they are focused on building better benchmarks and better leaderboards.

(00:46:07):
So I've talked a lot about how I worry that the leaderboards and benchmarks out there today are steering models in the wrong direction, so yeah, so the question is, how do we fix that? And so that's what our research team is focused focused really heavily on right now. So they're working a lot on that.

(00:46:23):
And they're also working on these other things like, "Okay, we need to train our own models to see what types of data performs the best, what types of people perform the best." And so they're also working on all these training techniques and evaluation of our own data sets to improve our data operations and the internal data products that we have that determine what makes something good quality.

Lenny Rachitsky (00:46:46):
It's such a cool thing because I don't think basically the labs have researchers helping them advance AI. I imagine it's pretty rare for a company like yours to have researchers actually doing primary research on AI.

Edwin Chen (00:46:59):
Yeah, I think it's just because it's something I've fundamentally always cared about. I often think about us more like a research lab than a startup because that is my goal. It's kind of funny, but I've always said I would rather be Terrence Tau than Warren Buffett, so that notion of creating research that pushes the frontier forward and not just getting some valuation, that's always been what drives me.

Lenny Rachitsky (00:47:25):
And it's worked out. That's the beautiful thing about this. You mentioned that you were hiring researchers, is there anything there you want to share folks you're looking for?

Edwin Chen (00:47:32):
So we look for people who are just fundamentally interested in dataset all day. So types of people who could literally spend 10 hours digging through a dataset, and playing around with models, and thinking, "Okay, yeah, this is where I think the model's failing," this is the kind of a behavior you want the model to have instead, and just this aspect of being very hands-on and thinking about the qualitative aspects of models and not just the quantitative parts. So again, it's like this aspect of being hands-on with data and not just caring about these kind of abstract algorithms.

Lenny Rachitsky (00:48:07):
Awesome.

(00:48:07):
I want to ask a couple broad AI kind of market questions. What else do you think is coming in the next couple of years that people are maybe not thinking enough about or not expecting in terms of where AI is heading? What's going to matter?

Edwin Chen (00:48:20):
I think one of the things that's going to happen in the next few years is that the models are actually going to become increasingly differentiated because of the personalities and behaviors that the different labs have and the kind of objective functions that they are optimizing their models for. I think it's one thing I didn't appreciate a year or so ago.

(00:48:45):
A year or so ago, I thought that all of the AI models would essentially become very commoditized. They would all behave like each other, and sure, one of them might be slightly more intelligent in one way today, but sure, the other ones would catch up in the next few months. But I think over the past year, I've realized that the values that the companies have will shape the model.

(00:49:09):
So let me give you an example. So I was asking Claude to help me draft an email the other day, and it went through 30 different versions. And after 30 minutes, yeah, I think it really crafted me the perfect email, and I sent it. But then I realized that I spent 30 minutes doing something that didn't matter at all. Sure, now I got the perfect email, but I spent 30 minutes doing something I wouldn't have worried at all before, and this email probably didn't even move the needle on anything anyways.

(00:49:35):
So I think there's a deep question here, which is, if you could choose the perfect model behavior, which model would you want? Do you want a model that says, "You're absolutely right. There are definitely 20 more ways to improve this email," and it continues for 50 more iterations. And it sucks up all your time and engagement. Or do you want a model that's optimizing for your time and productivity and just says, "No, you need to stop. Your email's great. Just send it and move on with your day"?

(00:49:59):
And again, just because... In the same way that there's like a kind of a fork in a road between how you could choose how your model behaves for this question, it's like for every other question that models have, the kind of behavior that you want will fundamentally affect it.

(00:50:17):
It's almost like in the same way that when Google builds a search engine, it's very different from how Facebook would build a search engine, which is very different from how Apple would build a search engine. They all have their own principles and values and things that they're trying to achieve in the world that shape all the products that they're going to build. And in the same way, I think all the [inaudible 00:50:40] will start behaving very differently too.

Lenny Rachitsky (00:50:41):
That is incredibly interesting. You already see that with Grok. It's got a very different personality and a very different approach to answering questions. And so what I'm hearing is you're going to see more of this differentiation.

Edwin Chen (00:50:52):
Yep.

Lenny Rachitsky (00:50:53):
Kind of another question along these lines, what do you think is most under-hyped in AI that you think maybe people aren't talking enough about that is really cool? And what do you think is over-hyped?

Edwin Chen (00:51:04):
So I think one of the things that's under-hyped is the built-in products that all of the chatbots are going to start having. I've always been a huge fan of Claude's artifacts. And I think it just works really well. And actually the other day, I don't know if it's a new feature or not, but it asked me to help me create an email, and then it just created... So it didn't quite work because it didn't allow me to send the email. But what it created instead was like a little, I don't know what we call it, like a little box where I could click on it and it would just text someone that did this message. And I think that concept of taking artifacts to the next level where you just have these mini apps, mini UIs within the chatbots themselves, I feel like people aren't talking enough about that. So I think that that's one under-hyped area.

(00:51:54):
And in terms of over-hyped areas, I definitely think that vibe coding is over-hyped. I think people don't realize how much it's going to make your systems unmaintainable in the long-term and they simply dump this code into their code bases if this seems to work out right now, so I kind of worry about the future of coding. It's just going to keep on happening.

Lenny Rachitsky (00:52:17):
These are amazing answers. On that first point, there's something I actually asked. I have the chief product officer of Anthropic and OpenAI, Kevin Weil and Mike Krieger on the podcast, and I asked them just like, "As a product team, you have this gigabrain intelligence. How long do you even need product teams?" You think this AI will just create the product for you. "Here's what I want." It's like the next level of vibe coding. It's just like tell it, "Here's what I want," and it's just building the product and involving the product as you're using it. And it feels like that's what you're describing is where we might be heading.

Edwin Chen (00:52:48):
Yeah, I think there's a very powerful notion where it helps people just achieve their ideas in a much cooler way.

Lenny Rachitsky (00:52:55):
Something we haven't gotten into that I think is really interesting is just the story of how you got to starting Surge. You have a really unique background. I always think about these... Brian Armstrong, the founder of Coinbase, once gave this talk that has really stuck with me where he kind of talked about how his very unique background allowed him to start Coinbase. He had a economics background, he had a cryptography experience, and then he was an engineer. And it's like the perfect Venn diagram for starting Coinbase, and I feel like you have a very similar story with Surge. Talk about that, your background there, and how that led to Surge.

Edwin Chen (00:53:31):
Going way back, I was always fascinated by math and language when I was a kid. I went to MIT because it's obviously one of the best places for math and CS, but also because it's the home of Noam Chomsky. My dream in school was actually to find some underlying theory connecting all these different fields.

(00:53:47):
And then I became a researcher at Google, and Facebook, and Twitter, and I just kept running into the same problem over and over again. It was impossible to get the data that we needed to train our models. So I was always this huge believer in the need for high quality data, and then GPT-3 came out in 2020. And I realized that, yeah, if we wanted to take things to the next level and build models that could code, and use tools, and tell jokes, and write poetry, and solve [inaudible 00:54:12], and cure cancer, then yeah, we were going to need a completely new solution.

(00:54:16):
The thing that always drove me crazy when I was at all these companies was we had a full power of the human mind in front of us, and all the data students out there were focused on really simple things like image labeling. So I wanted to build something focus on all these advanced, complex use cases instead that would really help us build our next generation models. So yeah, I think my background in kind of across math, and computer science, and linguistics really informed what I always wanted to do, and so I started Surge a month later with our one mission to basically build the use cases that I thought were going to be needed to push the frontier of AI.

Lenny Rachitsky (00:54:49):
And you said a month later, a month later after what?

Edwin Chen (00:54:52):
After a GPT-3 launch in 2020.

Lenny Rachitsky (00:54:54):
Oh, okay. Wow. Okay. Yeah. A great decision.

(00:54:57):
What just kind of drives you at this point of... Other than just the epic success you're having, what keeps you motivated to keep building this and building something in this space?

Edwin Chen (00:55:06):
I think I'm a scientist at heart. I always thought I was going to become this math or CS professor and work on trying to understand the universe, and language, and the nature of communication. It's kind of funny, but I always had this fanciful dream where if aliens ever came to visit Earth and we need to figure out how to communicate with them, I wanted to be the one the government would call. And I'd use all this fancy math, and computer science, and linguistics to decipher it.

(00:55:33):
So even today, what I love doing most is every time a new model is released, we'll actually do a really deep dive into the model itself. I'll play around with it, I'll run evals, I'll compare where it's improved, where it's arrest, I'll create this really deep dive analysis that we send our customers. And it's actually kind of funny because a lot of times we'll say it's from a data science team, but often it's actually just from me.

(00:55:54):
And I think I could do this all day. I have a very hard time being in meetings all day. I'm terrible at sales, I'm terrible at doing the typical CEO things that people expect you to do, but I love writing these analyses. I love jamming with our research team about what we're seeing, sometimes I'll be up until 3:00 AM just talking on the phone with somebody on the research team and [inaudible 00:56:12] model. So I love that I still get to be really hands-on, working on the data and the science all day. And I think what drives me is that I want Surge to play this critical role in the future of AI, which I think is also the future of humanity. We have these really unique perspectives on data, and language, and quality, and how to measure all of this, and how to ensure it's all going on the right path. And I think we're uniquely unconstrained by all of these influences that can sometimes steer companies in a negative direction.

(00:56:41):
Like what I was saying earlier, we built Surge a lot more like a research lab than a typical startup. So we care about curiosity and long-term incentives and intellectual rigor, and we don't care as much about quarterly metrics and what's going to look good in a [inaudible 00:56:56]. And so my goal is to take all these unique things about us as a company and use that to make sure that we're shaping AI in a way that's really beneficial for our species in the long term.

Lenny Rachitsky (00:57:06):
What I'm realizing in this conversation is just how much influence you have and companies like yours have on where AI heads. The fact that you help labs understand where they have gaps and where they need to improve, and it's not just everyone looks at just like the heads of OpenAI and Anthropic and all these companies as they're the ones ushering in AI, but what I'm hearing here is you have a lot of influence on where things head too.

Edwin Chen (00:57:30):
Yeah, I think there's this really powerful ecosystem where, honestly, people just don't know where models are headed and how they want to shape them yet and how they want humanity kind of like [inaudible 00:57:47] play a role in the future of all of this, and so I think there's a lot of opportunity to just continue shaping the discussion.

Lenny Rachitsky (00:57:52):
Along that thread, I know you have a very strong thesis on just why this work matters to humanity and why this is so important, talk about that.

Edwin Chen (00:58:01):
I'll get a bit philosophical here, but I think the question itself is a bit philosophical, so bear with me. So the most straightforward way of thinking about what we do is we train and evaluate AI. But there's a deeper mission that I often think about, which is helping our customers think about their dream objective functions. Like yeah, what kind of model do they want their model to be? And once we help them do that, we'll help them train their model to reach their north star and we'll help them measure that progress. But it's really hard because objective functions are really rich and complex. It's kind of like the difference between having a kid and asking them, "Okay, what test do you want to pass? Do you want them to get a high score on SAT and write a really good college essay?" That's a simplistic version versus what kind of person do you want them to grow up to be? Will you be happy if they're happy no matter what they do or are you hoping they'll go to a good school and be financially successful?

(00:58:50):
And again, if you take that notion, it's like, okay, how do you define happiness? How do you measure whether they're happy? How do you measure whether they're financially successful? It's a lot harder than something measuring whether or not you're getting a high score on the SAT, and what we're doing is we want to help our customers reach, again, their dream north stars and figure out how to measure them. And so I talked about this example of what you want models to do when you're asking them to write 50 different evaluations. Do you just continue them for 50 more or do you just say, "No, just move on [inaudible 00:59:25] because this is perfect enough." And the broader question is, are we building these systems that actually advance humanity? And if so how do we build the data sets to train towards that and measure it? Are we optimizing for all of these wrong things, just systems that suck up more and more of our time and make us lazier and lazier?

(00:59:44):
And yeah, I think it's really relevant to what we do because it's very hard and difficult to measure and define whether something is genuinely advancing humanity. It's very easy to measure all these proxies instead like clicks and likes. But I think that's why our work is so interesting. We want to work the hard, important metrics that require the hardest types of data and not just the easy ones. So I think one of the things I often say is you are your objective function. So we want the rich, complex, objective functions and not these simplistic proxies. And our job is to figure out how to get the data to match this.

(01:00:12):
So yeah, we want data, we want metrics that measure whether AI is making your life richer. We want to train our systems this way. And we want tools that make us more curious and more creative, not just lazier. And it's hard because, yeah, humans are kind of inherently lazy so AI software deals are the easiest way to get engagement, make all your metrics fall up. So I think this question about choosing the right objective functions and making sure that we're optimizing towards them and not just these easy proxies is really important to our future.

Lenny Rachitsky (01:00:37):
Wow. I love how what you're sharing here gives you so much more appreciation of the nuances of building AI, training AI, the work that you're doing.

(01:00:45):
From the outside, people could just look at Surge and companies in the space of, okay, cool. They're just creating all this data, feeding it to AI. But clearly there's so much to this that people don't realize, and I love knowing that you're at the head of this, that someone like you is thinking through this so deeply.

(01:01:02):
Maybe one more question, is there something you wish you'd known before you started Surge? A lot of people start companies, they don't know what they're getting into. Is there something you wish you could tell your earlier self?

Edwin Chen (01:01:11):
Yeah, so I definitely wish I'd known that you could build a company by being heads down and doing great research and simply building something amazing. And not by constantly tweeting and hyping and fundraising. It's kind of funny, but I never thought I wanted to start a company. I love doing research. And I was actually always a huge fan of DeepMind because they were this amazing research company that got bought and still managed to keep on doing amazing science. But I always thought that they were this magical ILR unicorn. So I thought if I started a company, I'd have to become a business person looking at financials all day and being in meetings all day and doing all this stuff that sounded incredibly boring and I always hated. So I think it's crazy that didn't end up being true at all. I'm still in the weeds in the data every day. And I love it. I love that I get to do all these analyses and talk to researchers. And it's basically applied research where we're building all these amazing data systems that have really pushed the frontier of AI.

(01:02:01):
So yeah, I wish I know that you don't need to spend all your time fundraising. You don't need to constantly generate hype. You don't need to become someone you're not. You can actually build a successful company by simply building something so good that it cut through all that noise. And I think if I known this was possible, I would've started even sooner, so I [inaudible 01:02:18] that.

Lenny Rachitsky (01:02:18):
And that is such an amazing place to end. I feel like this is exactly what founders need to hear, and I think this conversation's going to inspire a lot of founders, and especially a lot of founders that want to do things in a different way. Before we get to a very exciting lightning round, is there anything else you wanted to share? Anything else you want to leave our listeners with? We covered a lot of ground, it's totally okay to say no as well.

Edwin Chen (01:02:37):
I think the thing I would end with is I think a lot of people think of data labeling as it relates to simplistic work. Like labeling cat photos and drawing bounding box around cars. And so I've actually always hated the word data labeling because it just paints this very simplistic picture when I think what we're doing is completely different. I think a lot about what we're doing as a lot more like raising a child. You don't just feed a child information. You're teaching them values, and creativity, and what's beautiful, and these infinite subtle things about what makes somebody a good person. And that's what we're doing for AI. So yeah, I just often think about what we're doing as almost like the future of humanity or how we're raising humanity's children, so I'll leave it at that.

Lenny Rachitsky (01:03:27):
Wow. I love just how much philosophy there is in this whole conversation that I was not expecting.

(01:03:33):
With that, Edwin, we've reached our very exciting lightning round, I've got five questions for you. Are you ready?

Edwin Chen (01:03:38):
Yep, let's go.

Lenny Rachitsky (01:03:39):
Here we go. What are two or three books that you find yourself recommending most to other people?

Edwin Chen (01:03:45):
Yes, so three books I often recommend are, first, Story of Real Life by Ted Chang. It's my all time favorite short story and it's about a linguist learning and alien language, and I basically reread it every couple years.

Lenny Rachitsky (01:03:56):
And that's what the Interstellar was about? Is that...

Edwin Chen (01:03:59):
Yeah, so there's a movie called Arrival...

Lenny Rachitsky (01:04:01):
Arrival.

Edwin Chen (01:04:02):
... which was based off of the story,

Lenny Rachitsky (01:04:03):
Yes, [inaudible 01:04:03]-

Edwin Chen (01:04:03):
... which I love as well.

Lenny Rachitsky (01:04:04):
Great. Okay, keep going.

Edwin Chen (01:04:06):
And then second, Myth of Sisyphus by Camus. I actually can't really explain why I love this, but I always find a final chapter somehow are really inspiring.

(01:04:15):
And then third, Le Ton beau de Marot by Douglas Hofstadter. And so I think Gödel, Escher, Bach is his more famous book, but I've actually always loved this one better. It basically takes a single French poem and translates it 89 different ways and discusses all the motivations behind each translation. And so I've always loved the way it embodies this idea that translation isn't this robotic thing that you do. Instead, there's a million different ways to think about what makes a high quality translation, which makes a lot of ways I think about data and quality in LLMs.

Lenny Rachitsky (01:04:44):
All these resonate so deeply with the way, with all the things we've been talking about, especially that first one, if that was your goal after school is like, "I want to help translate alien language." I'm not surprised you love that short story.

(01:04:56):
Next question, do you have a favorite recent movie or TV show you've really enjoyed?

Edwin Chen (01:05:00):
One of my new all time favorite TV shows is something I found recently, it's called Travelers. It's basically about a group of travelers from the future who are sent back in time to prevent their [inaudible 01:05:11]. Sorry, I just wrote that [inaudible 01:05:13] section.

(01:05:14):
And then I actually just rewatched Contact, which is one of my all time favorite movies. So yeah, I think one of the things you'll notice about me is that, yeah, I love any kind of book or film that involves scientists deciphering alien communication. Again, just this dream I always had as a kid.

Lenny Rachitsky (01:05:28):
That's so funny [inaudible 01:05:29].

(01:05:30):
Okay, is there a product you've recently discovered that you really love?

Edwin Chen (01:05:35):
So it's funny, but I was in SF earlier this week and I finally took Waymo for the first time. Honestly, it was magical and it really felt like living in the future.

Lenny Rachitsky (01:05:43):
Yeah, it's like the thing that... People hype it like crazy, but it always exceeds your expectations.

Edwin Chen (01:05:48):
Yeah, it deserves the hype. It was crazy. Yeah, it's absurd. It's like, holy moly. If you're not in SF, you don't realize just how common these things are. They're just all over the place. Just driverless cars constantly going about, and when you go to an event at the end, there's just all these Waymos lined up picking people up.

Lenny Rachitsky (01:06:03):
Yeah. Waymo, good job. Good job over there.

(01:06:06):
Do you have a favorite life motto that you find yourself coming back to in work or in life?

Edwin Chen (01:06:11):
So I think I mentioned this idea that founders should build a company that only they could build. Almost like it's this destiny that their entire life, and experiences, and interests shape them towards. And so I think that principle applies pretty broadly, not just the founders, but the people creating, I think.

Lenny Rachitsky (01:06:25):
Well, let me follow that thread to unlightening this answer. Do you have any advice for how to build those sorts of experiences that help lead to that? Is it follow things that are interesting to you, because it's easy to say that, it's hard to actually acquire these really unique sets of experiences that allow you to create something really important?

Edwin Chen (01:06:44):
Yeah, so I think it would always be to really follow your interests and do what you love, and it's almost like a lot of decisions I make about Surge. I think one of the things that I didn't think about a couple years ago, but then someone said it to me, it's that companies in a sense are an embodiment of their CEO. And it's kind of funny. I hadn't thought about that because I never quite knew what a CEO did. I always thought a CEO was kind of generic and it's like, okay, you're just doing whatever VPs, and your board, and whatever, tell you to do and you're just saying yes to decisions. But instead, it's this idea where when I think about certain big, hard decisions we have to make, I don't think what would the company do, I don't think what metrics are we trying to optimize, I just think, "What do I personally care about? What are my values? And what do I want to see happen in the world?"

(01:07:34):
And so I think following that idea about... Okay, so ask yourself, what are the values you care about? What are things you're trying to shape and not... What will look good on a dashboard? I think that results are pretty important.

Lenny Rachitsky (01:07:49):
I love how just you're just full of endless, beautiful, and very deep answers.

(01:07:55):
Final question. Something that you got quite famous for before starting Surge is you built this map while you were at Twitter that showed a map of the world and what people called, whether they called it soda or pop. I don't know if it's called Soda Pop. What was the name of this map?

Edwin Chen (01:08:13):
Yeah, it was like the Soda Versus Pop dataset.

Lenny Rachitsky (01:08:15):
Soda Versus Pop.

Edwin Chen (01:08:17):
[inaudible 01:08:17]

Lenny Rachitsky (01:08:16):
And so it's like a map of the United States and it tells you where people say pop versus soda, so do you say soda or pop?

Edwin Chen (01:08:23):
So I say soda, I'm a soda person.

Lenny Rachitsky (01:08:26):
Okay. And is that just like that's the right answer or it's like whatever you are, it's totally fine.

Edwin Chen (01:08:33):
I think I'll look at you a little bit funny. You say pop and I'll wonder where you came from, but I won't score on you too much.

Lenny Rachitsky (01:08:39):
That's how I feel too.

(01:08:40):
Edwin, this was incredible. This was such an awesome conversation. I learned so much. I think we're going to help a lot of people start their own companies, help their companies become more aligned with their values and just building better things.

(01:08:53):
Few final questions, where can folks find you online if they want to reach out? What roles are you hiring for? How can listeners be useful to you?

Edwin Chen (01:09:00):
Yeah, so I used to love writing a blog, but I haven't had time in the past few years. But I am starting to write again, so definitely check out the Surge blog, surgehq.ai/blog, and yeah, hopefully I'll be running a lot more there. And I would say we're definitely always hiring, so for people who just love data and people who love this intersection of math, and language, and computer science, definitely reach out anytime.

Lenny Rachitsky (01:09:24):
Awesome. And how can listeners be useful to you? Is it just, I don't know, yeah, is there anything there? Any asks?

Edwin Chen (01:09:29):
So I would say definitely tell me blog topics that you like me to write about...

Lenny Rachitsky (01:09:29):
Okay.

Edwin Chen (01:09:32):
... and then I'm always fascinated by all of these AI failures that happen in the real world. So whenever you come across a really interesting failure that I think illustrates some deep question about how we want model to behave, there's just so many different ways a model can respond, I just oftentimes think there's just not a single right answer. And so whenever there's one of these examples, I just love seeing them.

Lenny Rachitsky (01:09:57):
You need to share these on your blog. I'm also... I would love to see these.

(01:10:01):
Edwin, thank you so much for being here.

Edwin Chen (01:10:03):
Thank you.

Lenny Rachitsky (01:10:04):
Bye everyone.

(01:10:07):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

