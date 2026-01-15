---
guest: Chip Huyen
title: Al Engineering 101 with Chip Huyen (Nvidia, Stanford, Netflix)
youtube_url: https://www.youtube.com/watch?v=qbvY0dQgSJ4
video_id: qbvY0dQgSJ4
description: Chip Huyen is a core developer on Nvidia’s Nemo platform, a former AI
  researcher at Netflix, and taught machine learning at Stanford. She’s a two-time
  founder and the author of two widely...
duration_seconds: 4956.0
duration: '1:22:36'
view_count: 39648
channel: Lenny's Podcast
keywords:
- acquisition
- metrics
- conversion
- pricing
- subscription
- hiring
- strategy
- market
- persona
- design
- ui
- prototype
- user experience
- engineering
- architecture
---

# OpenAI researcher on why soft skills are the future of work | Karina Nguyen

## Transcript

Chip Huyen (00:00:00):
A question that get asked a lot and a lot is, "How do we keep up to date with the latest AI news?" Why do you need to keep up to date with the latest AI news? If you talk to the users who understand what they want or they don't want, look into the feedback, then you can actually improve the application way, way, way more.

Lenny Rachitsky (00:00:15):
A lot of companies are building AI products. A lot of companies are not having a good time building AI products.

Chip Huyen (00:00:19):
We are in an ideal crisis. Now, we have all this really cool tools to do everything from scratch and have new design. It can have you write code. You can have new website. So in theory, we should see a lot more, but at the same time, people are somehow stuck. They don't know what to build.

Lenny Rachitsky (00:00:33):
All this AI hype, the data is actually showing most companies try it, doesn't do a lot. They stop. What do you think is the gap here?

Chip Huyen (00:00:38):
It's really hard to measure productivity. So, I do ask people to ask their managers, "Would you rather give everyone on the team very expensive coding agent subscriptions or you get an extra head count?" Almost every one, the managers will say head count. But if you ask VP level or someone who manage a lot of teams, they would say, "Want AI assistant." Because as managers, you are still growing, so for you having one HR head count is big. Whereas for executives, maybe you have more business metrics that you care about. So you actually think about what actually drive productivity metrics for you.

Lenny Rachitsky (00:01:11):
Today, my guest is Chip Huyen. Unlike a lot of people who share insights into building great AI products and where things are heading, Chip has built multiple successful AI products, platforms, tools. Chip was a core developer on NVIDIA's NeMo platform, an AI researcher at Netflix. She taught machine learning at Stanford. She's also a two-time founder and the author of two of the most popular books in the world of AI, including her most recent book called AI Engineering, which has been the most read book on the O'Reilly platform since its launch.

(00:01:41):
She's also gotten to work with a lot of enterprises on their AI strategies, and so she gets to see what's actually happening on the ground inside a lot of different companies. In our conversation, Chip explains a lot of the basics like, what exactly does pre-training and post-training look like? What is RAG? What is reinforcement learning? What is RLHF? We also get into everything she's learned about how to build great AI products, including what people think it takes and what it actually takes. We talk about the most common pitfalls that companies run into, where she's seeing the most productivity gains and so much more.

(00:02:12):
This episode is quite technical, more technical than most conversations I've had, and is meant for anyone looking for a more in-depth conversation about AI. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. And if you become an annual subscriber of my newsletter, you get a year free of 16 incredible products, including Devin, Lovable, Replit, Bolt, n8n, Linear, Superhuman, Descript, Wispr Flow, Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, and Mobbin. Head on over to lennysnewsletter.com and click product pass. With that, I bring you Chip Huyen after a short word from our sponsors.

(00:02:47):
This episode is brought to you by Dscout. Design teams today are expected to move fast but also to get it right. That's where Dscout comes in. Dscout is the all-in-one research platform built for modern product and design teams. Whether you're running usability tests, interviews, surveys, or in the wild field work, Dscout makes it easy to connect with real users and get real insights fast. You can even test your Figma prototypes directly inside the platform. No juggling tools, no chasing ghost participants, and with the industry's most trusted panel, plus AI-powered analysis, your team gets clarity and confidence to build better without slowing down.So if you're ready to streamline your research, speed of decisions, and design with impact, head to dscout.com to learn more. That's D-S-C-O-U-T.com, the answers you need to move confidently.

(00:03:39):
Did you know that I have a whole team that helps me with my podcast and with my newsletter? I want everyone on my team to be super happy and thrive in their roles. Justworks knows that your employees are more than just your employees. They're your people. My team is spread out across Colorado, Australia, Nepal, West Africa, and San Francisco. My life would be so incredibly complicated to hire people internationally, to pay people on time and in their local currencies, and to answer their HR questions 24/7. But with Justworks, it's super easy. Whether you're setting up your own automated payroll, offering premium benefits or hiring internationally, Justworks offers simple software and 24/7 human support from small business experts for you and your people. They do your human resources right so that you can do right by your people. Justworks, for your people. Chip, thank you so much for being here, and welcome to the podcast.

Chip Huyen (00:04:34):
Hi, Lenny. I've been a big fan of the podcast for a while, so I'm really excited to be here. Thank you for having me.

Lenny Rachitsky (00:04:40):
I want to start with this table/chart that you shared on LinkedIn a while ago that went super viral, and I think it went super viral because it hit a nerve with a lot of people. Let me just read this and we'll show this on YouTube for people that are watching. So it's this very simple table you shared of what people think will improve AI apps and what actually improves AI apps. What people think will improve AI apps, staying up to date with the latest AI news, adopting the newest agentic framework, agonizing about what vector databases to use, constantly evaluating what model is smarter, fine-tuning a model. And then you have what actually improves AI apps, talking to users, building more reliable platforms, preparing better data, optimizing end-to-end workflows, writing better prompts. Why do you think this hit such a nerve with people? If you had to boil it down, what do you think people are missing about building successful AI apps?

Chip Huyen (00:05:30):
[inaudible 00:05:30] question that get asked a lot and a lot is that, "How do we keep up to date with the latest AI news?" I'm like, "Why? Why do you need to keep up to date with the latest AI news?" I know it sound very counter-intuitive, but there's just so much news out there. A lot of people also ask me questions like, "How do I choose between two different technologies?" Maybe like recently, MCP versus agent-to-agent protocol? And it was like, "Which one is better or this or that?" I think it's a [inaudible 00:05:59] question you should ask them is like, "First, how much of the improvement could you get from optimal solutions versus non-optimal solutions?" Right? And sometimes they were like, "Actually, it's not much." Right?

(00:06:10):
I was like, "Okay, if it's not much improvement, then why do you want to spend so much time debating something that doesn't make that much difference to your performance?" Another question they ask is like, "If you adopted a new technology, how hard it could be to switch that out to another?" And sometimes they will like, "Oh, I think it could be a lot of work switching it out." And I'm just like, "Hmm, let's say here's a new technology. It hasn't been tested by a lot of people, and if you would adopt it, you would be stuck with it forever. Do you actually want to adopt it?" Maybe you want to think twice about over commit to new technologies that hasn't been better tested.

Lenny Rachitsky (00:06:49):
I love your just broader advice is just simple like, to build successful AI apps, talk to users, build better data, write better prompts, optimize the user experience, versus just like, what is the latest and greatest? What's the best model to use right now? What's happening in AI? Let me follow this thread of this idea of fine-tuning and basically post-training. There's all these terms that people hear in AI, and I think this is going to be a really good opportunity for people to learn what we're actually talking about, since you actually do these things, you build these things, you work with companies doing these things. There's a few terms I want to sprinkle in through the conversation, but let's start with this one. What's the simplest way for someone to understand? What is the difference between pre-training and post-training and then just how fine-tuning fits into that, just what fine-tuning actually is?

Chip Huyen (00:07:34):
Chip disclaimer, I don't have full visibility on what this big secretive frontier labs are doing. But right from what I heard, so I think it's like one is, supervised fine-tuning when you have demonstration data, and you have a bunch of experts, "Okay, here's a prompt, and here is what the answer should be like." You just train it to emulate what the human expert could be like. That's also what a lot of people would like, so open-source models are doing as they do it by distillation. So instead of having human experts to write really great answers to prompts, they get very popular, famous good models to generate a response to it and getting this train smaller models to emulate.

(00:08:23):
Sometimes you see people just like... So, that's because I really appreciate open source community by the way, but going from being able to train models that can emulate a existing good model. It's very different from being [inaudible 00:08:38] trained good models, like an output for existing good model. So, it's a big step there. Yeah, we have my supervised fine-tuning, and another thing that's very big, I'm not sure you have guests talking about it already, but reinforcement learning is everywhere.

Lenny Rachitsky (00:08:52):
Let's pause on that because I definitely want to spend time on that, and that's such cool topic that's merging more and more in my conversations. But just to even summarize the things you just shared, which I think is really, really important stuff. So, the idea here is a model, essentially this algorithm piece of code that someone writes and say the frontier models are feeding it just like the entire internet of content, and basically, it's trying to test itself on predicting across all that data the next word, essentially. Token is the correct way of thinking about it, but a simpler way to think about it is the next word in text. As it gets it wrong, it adjusts these things called weights, essentially. Just like, is that a simple way to think about it, even that's just very surface level?

Chip Huyen (00:09:35):
So, I think of language modeling as a way of encoding statistical information about language, right? So, let's say that we both speak English, so we get a sense of what is more statistically likely. If I say my favorite color is, then you would say, "Okay, that should be another color." The word blue would be much more likely to appear than the word like [inaudible 00:09:59], right? Because statistically, blue is more likely to [inaudible 00:10:02] my favorite color is. So, it's a way of encoding statistical information.

(00:10:07):
So when language modeling, when you train a large amount of data, you see a lot of languages, a lot of domains. So it can tell, okay, your basic size is standard. Then the user do the prompts and it could come with the next most likely token. So by the way, it's not a new idea actually. So it's the idea comes very, very old, from the 1951 papers like English entropy. I think it's by Claude Shannon, it's a great paper. And I think it reveals a story I really like is from... Did you read Sherlock Holmes by the way?

Lenny Rachitsky (00:10:39):
Yeah, I read a few Sherlock Holmes books. Yeah.

Chip Huyen (00:10:41):
Yeah. So this is story of when Sherlock Holmes says using this statistical information to help solve a case. So this is his story. There is somebody left a message with a lot of stick figures. So Sherlock Holmes was like, okay, he knows that in English, the most common letter is E. Then the most common stick figure must be E. And then he goes, he stopped like that, [inaudible 00:11:07]. So the code... So I think there's language. So in a way, it's simple language modeling, but instead of at a work level, he does this as character level and token is something in between, right? A token is not quite a word, but it's bigger than a character. So let's say we say token because it would help us reduce vocabulary because which character is smallest amount of vocabulary right now. So alphabet has 26 character, but words can have millions and millions, right? Whereas tokens, you can be able to get the sweet spot between the two.

(00:11:44):
So let's say that we have the new word, how to say it, like podcasting, right? Let's say it's a new word, but it can divide a podcast and ing. So people understand, okay, podcast, we know the meaning. We know that ing is a verb, gerund, whatever it is. So we even know the word podcasting so that's why the token comes in. But yeah, the pre-tuning is basically encoding statistical informations of language to have you predict what is most likely. I think that most likely is the most simple way of doing it because it's more building a distribution of, okay, so the next token could be more 90% of the the time it could be a color, 10% of the time could be something else. So it basically distribution so language could pick, depending on your sampling strategy. Do you want it to always pick the most likely token or do you want it to pick something more creative? So I think my sampling strategy, I think is something extremely important. It can have you boost a performance in a huge way and very, very underrated.

Lenny Rachitsky (00:12:49):
Okay, awesome. So essentially, a model is just code with this whole set of weights, essentially the statistical model that has learned to predict what comes next after certain words and phrases?

Chip Huyen (00:13:03):
Yeah.

Lenny Rachitsky (00:13:03):
And then post-training and fine-tuning, specifically, is doing that same thing. So pre-training you get GPT5. Fine-tuning is someone taking GPT5 and doing the same sort of thing, adjusting these weights a little bit for specific use cases on data that they find is necessary to do their very specific use case. Is that a simple way to think about it?

Chip Huyen (00:13:24):
Yeah, I think weights is functions, right? So let's say you have... Maybe it has a functions of maybe Lenny's height is maybe 1X plus something or 2X [inaudible 00:13:38] and plus something is the weights, right? So you change it until you fit the correct data, which is my height and your height. So you can think it's a weight, as just a weight, say function. So you train, adjust the weights so they can fit the data, which is the training data.

Lenny Rachitsky (00:13:54):
Awesome. Okay. So we're talking about pre-training, post-training, fine-tuning. Is there anything else here that's important to share about just what this is exactly? What people need to understand about these parts of training?

Chip Huyen (00:14:06):
So the vast majority of time, we don't touch on pre-training model. As users, we don't use it at all.

Lenny Rachitsky (00:14:12):
Right. It's already done for us.

Chip Huyen (00:14:13):
Yeah. So I think my [inaudible 00:14:15] is a bit of fun process when my friend's training model is they try to play with their pre-training model and they're horrendous. They're saying things like [inaudible 00:14:23] "Oh, my gosh." Yeah, it's crazy. So it's very interesting to look at how much of post-training can change the model behavior and I think that's where a lot of time, is a lot of people are spending energy on nowadays, their frontier lab, is on post-training. Because pre-training, I think... So pre-training have been used to increase the general capacity of capabilities of a model. And it needs a lot of data and model size to increase the model capabilities. And at some point, we are actually have kind of maxed out on the internet data. And people text data max out. I think a lot of people are doing with other data like audios and videos, and everyone's trying to think of what is the new source of data, but where like post-trading, but middle course of this is more of everyone have very similar pre-training data, is that post-training is where they make a big difference nowadays.

Lenny Rachitsky (00:15:21):
This is a good segue to, you talked about supervised learning versus unsupervised learning. I love, we're getting into this, by the way. This is super interesting. So you talk about labeled data. Basically, supervised learning is AI learning on data that somebody has already labeled and told it, here's correct versus incorrect. For example, this is spam versus not spam. This is a good short story. This is not a good short story. We've had the CEOs of a lot of these companies that do this for labs, Mercor and Scale, Handshake, there's Micro, there's a few others. So is that essentially what these companies are doing for labs, giving them labeled data, high-quality data to train on?

Chip Huyen (00:15:57):
It is in a way, but I think it's more like a product of big equations. So there are a lot more different components than that. So that's why I was talking about reinforcement learning. I'm not sure if your CEO [inaudible 00:16:09] interview bring up that term. So the idea is that once you [inaudible 00:16:14]... So let's say you have a model, give the model a prompt and it produce an output. You want to buy, once you reinforce, encourage the model to produce an output that is better. So now it comes to how do we know that the answer is good or bad? So usually, people relies on signals. So one way to get a first one good or bad is human feedback. They happen to be have two responses. You can, okay, this one one's better than the other. And we do that is because as humans, we tend to, it's very hard to give a concrete score, but it's easier to do comparisons.

(00:16:53):
If you ask me, okay, give this song a score, I'm not a musician and don't know how hard it is. It's like yeah, I don't know what, out of 10 I going to remove six. And if you ask me again a month from now and I completely forgotten, okay, maybe now seven, only four, I don't know. But then if you ask me, okay, here are two songs and which one would you prefer to play for the birthday party? I was like, "Okay, I can prefer this song." So comparisons a lot easier. So [inaudible 00:17:18] have a human, you have human feedback and then you use this human feedback to treat a reward model to tell which and then the reward model help you like, okay, it's a model that produce this response.

(00:17:28):
It's [inaudible 00:17:30] can score, is this good or bad? And you try to bias toward producing better model, the better responses. Another ways you can, instead of using a human, so you can use AI because the response and say good or bad, right? Or in fact the thing is that people are very big on nowadays, verifiable rewards, which it's natural. So basically, they give it a math problem and then math solutions is a model app a solution. Okay, it's expected response should be 42 and if it doesn't provide 42, then it's wrong. Now it's not a good response. So yes, a lot of time, people using this human laborer, human laborers should produce, how to say, expert questions and I say expected answers and in the ways that [inaudible 00:18:16] systems that verifiable so that the models can be trained on. Yeah.

Lenny Rachitsky (00:18:19):
Okay, I'm really glad you went there. This is essentially RLHF reinforcement learning with human feedback, which is exactly what I wanted to also talk about, right?

Chip Huyen (00:18:29):
Yeah. So I think it's general, it's a way of learning. It's training is [inaudible 00:18:33] learning and whether it learn from human feedback or AI feedback or verifiable rewards, I think I say it's just different way of collating signals.

Lenny Rachitsky (00:18:44):
Awesome. Yeah. We had the CEO of Anthropic on the podcast and he talked about their version of RLHF, which is AI driven reinforcement learning. I love the way you phrased it where basically you want to help the model, you want to reinforce correct behavior and correct answers, and this is the method to do it, whether it's say an engineer seeing an output from a model being like, "No, here's how I would code it differently." And it's training a different model that the original model works with to tell it, am I correct or not correct? Is that right, roughly?

Chip Huyen (00:19:15):
Yeah.

Lenny Rachitsky (00:19:16):
Okay.

Chip Huyen (00:19:16):
I think that's a way of looking into it. I think that's a space is so exciting nowadays because there are so many domain expert task that the model developers want models to do well on, right? Let's say you're accountant. Maybe you want to use a model to have accounting task and need a lot of accounting data examples from accountant. So you need to hire a lot of them, should I do it or everyone [inaudible 00:19:41] physics problems, everyone should do, I don't know, legal questions and stuff or engineering questions or somebody was telling me they want to do, using coding to source scientific problems and not just coding to build product, which is another different whole realm of things. And I also using very specific toolings. I'm not sure what apps you use, but maybe like a [inaudible 00:20:04] app or QuickBooks or Google Excel. They have very specific tools, specific expertise. So you want the model [inaudible 00:20:13] learn.

(00:20:13):
So they need a lot of humans expert in this area should create data to train them and it's a massive thing people because everyone wants a lot of data and wants [inaudible 00:20:25] unlimited budget. But whether, I think this is also a little bit of low-key, interesting economics. I'm not sure you've talked to the guests about, I thought it's very interesting [inaudible 00:20:35] think about because it's very lopsided, right? Because they're only a very small numbers of frontier labs and they want a lot of data and there's a massive amount of startups or company providing related data. So you can see these companies like this startup doing data labeling. They have maybe some massive AR, but if you ask them, "Okay, so how many customers you have?" And they could be very small numbers, I'm not sure. I'm not sure you... I saw you smiling.

Lenny Rachitsky (00:21:03):
Yeah, yeah, yeah, we chatted about that.

Chip Huyen (00:21:05):
Yeah, so I'm a little bit like [inaudible 00:21:08] uneasy. I have a company's growing crazy, but it's heavily dependent on two or three companies. And at the same time, if I was this company, frontier labs, what could be the right economical things for me to do? Now I want a lot of startups. I want to have a lot of providers so I can pick and choose, and as this providers can also to compete each other to lower the price and it's so dependent on [inaudible 00:21:34] regardless. So I feel like, yeah, so this whole economics is very interesting to me and I'm curious to see and how it plays out.

Lenny Rachitsky (00:21:42):
What I'm hearing is you're bearish on the future of these data labeling companies because as you said, they don't have a lot of leverage over pricing because they have so few customers and there's so many people getting into the space. So basically, even though there's some of the fastest growing companies in the world, you're feeling like there's a challenge up ahead.

Chip Huyen (00:22:00):
I'm not sure if I'm bearish on it. I think I'm curious because I think things has a way of work out in ways that I don't expect. So I think that maybe these companies, they have a lot of data, maybe they wouldn't be able to use that to have some insight that helps them stay ahead of the curve. So I don't know.

Lenny Rachitsky (00:22:22):
A very fair answer. Okay, while we're on this topic, I want to chat about evals, which is a very recurring topic in this podcast. This is the other piece of data content these companies share that AI labs really need. Can you just talk about what an eval is, the simplest way to understand it and then how this helps models get smarter?

Chip Huyen (00:22:41):
So I think people approach eval, I think they're two very different problems. One is a app builder and can I say have an app that do maybe a chatbot? Very simple answer first thing that came to my mind and I want you to know if chatbot is good or bad. So it needs to come away with evaluate the chatbot. Another thing is, I think of this as a task-specific eval design. So let's say I'm a model developer and I want to make my model better at code writing. And it was like, "Okay, but how do I even measure code writing?"

(00:23:19):
So I need someone to understand code writing and think about what makes a story good and then design the whole dataset and then criteria to evaluate code writing. So yeah, I think there's that. I think it's more like eval design that is very interesting [inaudible 00:23:39] work criteria, [inaudible 00:23:42] work guidelines, how to do it and then also train people how to do it effectively. So I guess, [inaudible 00:23:49], I think eval is really, really fun because it's extremely creative. I was looking at different eval people built and it was like, "Wow." It's not dry at all. It's just super, super, super fun.

Lenny Rachitsky (00:24:01):
We had a whole podcast on evals with Hamel and Shreya. That's exactly what they talked about is just, it's actually really fun to create evals for companies, especially. So let's still dig into that one a little bit more. There's this kind of debate online that, I don't know how big of a deal this debate is, but it feels like people spend a lot of time thinking about this, this idea of, do we need evals for AI products? Some of the best companies say they don't really do evals, they just go on vibes. They're just like, "Is this working well? Can I feel it or not?" What's your take on just the importance of building evals and the skill of evals for AI apps, not the model companies?

Chip Huyen (00:24:39):
You don't have to be absolutely perfect, I think, to win. You just need to be good enough and being consistent about it. Okay, this is not a philosophy I follow, but I have worked with enough companies to see that play out. So when I say, why a company don't eval? Let's say you are an executive and you want to have a new use case. So here's a use case you started out, built and it's like it works well. The customers are somewhat happy. You don't have the exact metric for it.

(00:25:05):
So the traffic keeps increasing, people seem happy, people keep buying stuff and now here's our engineer coming like, "Okay, we need eval for it." And it was like, "Okay, how much effort do we need to go into eval?" And they were like, "Okay, maybe two engineers, this much, this much." And it could maybe would improve that and it was like, "Okay, so how much expected gain can I get from it?" And the engineer would be like, "Oh, maybe you can improve it from 80% to 82%, 85%."

(00:25:33):
And it was like, "Okay, but [inaudible 00:25:35] that two engineers and we going to launch a new feature, then it could give me so much more improvement." So I think it's one of them is eval. Sometimes people think of eval as like okay, this is good enough, just don't touch it. If you do spend a lot of energy on eval, it would only incremental improvement where it spends the energy on another use case and maybe [inaudible 00:25:55] good enough that you can vibe check it.

(00:25:57):
So I do think maybe that's a debate is about. I do think that a lot of time people just get things to the place where it's like, okay, good enough, people run. But in the end, but of course there's a lot of risk associated with it because if you don't have a clear metric, you have a good visibility to [inaudible 00:26:17] applications or models performing it might do something very dumb or it can cause you, I know something crazy can happen. So yeah, so I do think eval is very, very important if you have, if you operate a scale and where failures can have catastrophic consequences.

(00:26:38):
Then you do need to be very tyrannical about what you put in front of the users, understand different failure modes, what could go wrong and also maybe in a space when that it's a feature, the product is a competitive advantage. You want to be the best at it. So you want to have a very strong understanding of where you are and where you are with the competitors. But it's just something that's more a low-key, okay, this is like something is like, okay, that's not the core but it helps with our users.

(00:27:04):
Then maybe you don't need to be so obsessed or theoretical about it. It's like, okay, that's good enough for now and if it fails, then it fails. Okay, I know it's so terrifying. But yeah, I think it's all about the question of return investment. I'm a big fan of eval, I love reading eval. And I says, I understand why some people would choose to not focus on eval right away and choose bringing on new functionalities instead.

Lenny Rachitsky (00:27:32):
Awesome. That is a really pragmatic answer. What I'm hearing is evals are great, very important, especially if you're operating at scale, but pick your battles. You don't need to write evals for every little feature. Something that Hamel and Shreya shared is that people need just, I don't know, five or seven evals for the most important elements of their product. Is that what you see or do you see a lot more in production that people build and need?

Chip Huyen (00:27:54):
I don't think of just a fixed number on the evals. What was the goal of eval? The goal of eval is to guide the product development. So you see eval, because I think I'm a big fan of eval, is that it helps you uncover opportunities where the progress are doing well. So sometimes, we've seen a very obvious [inaudible 00:28:15] where you look at the eval and we realize it's like, okay, it performed really poorly on this specific segment of users and then we look into it's like, okay, what's wrong with it? And it turns out, it's like we just don't have a good messaging to it. So people should just focus on the things that we're doing poorly, can improve significantly. Yeah, so I kind of like the number of eval is really depends. We have seen product with hundreds of different metrics.

Lenny Rachitsky (00:28:40):
Oh, wow.

Chip Huyen (00:28:41):
People going crazy, this is because that product is general, have different names, have one eval for, I don't know, verbosity, have one eval for user sensitive data and another is for length but has a number of, okay, let's just give a good example, concrete example, like deep research. So you have the application, you have views and model to do deep research for you. Okay, have a prompt. Let me say, okay, do me a comprehensive research on only Lenny's Podcast and help me propose, show me report on what kind of topics he's interested in, what kind of videos could get the most views or what topics that he's missing on that he should be covering, right? Have that prompt. Then how do you evaluate the result? I don't think there's one metrics that would help. Maybe it's like maybe you have a hundred, I think somebody has a benchmark and is get a hundred expert, write a bunch of prompts and they go through, on the answers on AI and do it. And it's extremely costly and slow.

(00:29:46):
But [inaudible 00:29:47] might have something else. First of all, one way I was thinking about it, I was talking to a friend about it and one way it's like, how would you produce the result of the summary? At first you need to, what you do, gather informations and to gather informations you need to do a lot of search queries. You gather, grab the search results and then some of the search results you aggregate and then maybe say, okay, I'm still missing on this. You have to go another route and on another route, [inaudible 00:30:17] have the summary. So every step of the way, you need evaluations. You don't [inaudible 00:30:21] end-to-end. Maybe it was a search query in my first thing about, okay, now I write five search queries. I might look into how good are the search queries? Do they as they similar to each other because you need five search queries are very similar? Okay, Lenny Podcast, Lenny Podcast last month, Lenny Podcast two months ago.

(00:30:39):
It's not very exciting. But if the query is a podcast, the keywords are more diverse and then look at the results of the search query and then say you enter the search query. Lenny Podcast data labeling and they come up with 10 pages, 10 results. And then you come up with like, oh, Lenny Podcast on, I don't know, frontier labs, and you have 10 results. [inaudible 00:31:06] different webpages. Okay, how much of them overlapping... Are we doing both the breadth, getting a lot of page, but also, do we have depth and also do you have relevance because if we come up with a search query, it's completely irrelevant to the original prompt. So I feel like every aspect of it, it would need a way of evaluating. So I don't think it's how many eval should I get, but how many eval do I need to get a good coverage, a high confidence in my application's performance and also to help me understand where it is not performing well so that I can fix it.

Lenny Rachitsky (00:31:43):
Awesome. And I'm hearing also just especially for the very core use case, the most common path people take in your product is where you want to focus.

Chip Huyen (00:31:51):
Yeah, yeah.

Lenny Rachitsky (00:31:54):
Okay. There's one more term I want to cover and I want to go a somewhat different direction. RAG? People see this term a lot, R-A-G. What does it mean?

Chip Huyen (00:32:04):
So RAG stands for Retrieval-Augmented Generations [inaudible 00:32:08] not a specific true generative AI. So the idea is just for a lot of questions, we need context to answer. So I think it came pretty, I think it's from the paper 2017. So someone was like, so they realized it's for a bunch of benchmark. When the question answering benchmarks, they realized it's like, okay, if we give the model informations about the questions, the next answer can be much, much better. So what they do with that is try to retrieve information from Wikipedia. So for question [inaudible 00:32:39], just retrieve that and then put it into the context and answer. It does much better. So I feel like it sounds like a no-brainer, right? I mean, obviously. So I think that's what RAG is, as a simplest sense, it's just providing the model with a relevant context so that it can answer the questions. And it's where things get really more interesting because traditionally, when it started out, RAG is mostly text.

(00:33:03):
So we talk about a lot of way of how to prepare data so that the model can retrieve effectively. Let's say that not everything is a Wikipedia page. A Wikipedia page is pretty contained and you know, okay, everything about it is about a topic. But a lot of time, you have documents of like [inaudible 00:33:19] and they have a weird way of structures of documents. Let's say that you had documents about Lenny Podcast and in the future, in the beginning a document it's like, from now on, podcast wouldn't refer to Lenny's Podcast. So let's say somebody in the future is like, "Okay, tell me about Lenny. Lenny's work." And because as a [inaudible 00:33:40] document does not have the term Lenny, you just don't know, you might not retrieve it. And if the document is long enough that it's chunked into a different part, so the second part doesn't have the word Lenny, so you cannot reach it. So you have to find a way to process data. So that makes sure it's like... It can retrieve, the information is just relevant to the query even though it might not immediately obvious that it's related.

(00:34:02):
So people come up with only thing of, I think, contextual visual, like giving X chunk of the data, the relevant, maybe in a summary metadata so that it knows or some people use as hypothetical questions. It's very interesting for even the chunk of documents, I must generate a bunch of questions that the chunks can help answer so that when I have a query, it's like okay, does it match any of the hypothetical questions? It can fetch it. So it's very interesting approach. Okay, so maybe before I go to the next thing, I just want to say this data preparations for RAG is extremely important. And I would say this in a lot of the companies that I have seen, that's the biggest performance, in their RAG solutions coming from better data preparations, not agonizing over what [inaudible 00:34:51] databases to use because [inaudible 00:34:53] database, of course is very important to care about things like latency or if you have very specific access patterns like read-heavy or write-heavy, of course, it's like it matters. But in term of pure quality answers, I think the data preparation is just [inaudible 00:35:07].

Lenny Rachitsky (00:35:06):
When you say data preparation, what's an example to make that real and concrete for us to understand?

Chip Huyen (00:35:16):
So one way is mentioned as in you have chunks of data. So we have think about how big of each chunk should be. Because if it's sort of think about it's a context you want to maximize, maybe you can, it's very simple example. You want to retrieve a thousand words. So if a data chunk is long, then it's more likely to contain more relevant metadata so it can retrieve more. But if it's too long then you have a thousand word. And so chunk is like a thousand words, you can reach one chunk. So it's not very useful. But if it's too short, then you can retrieve more relevant information also. It can retrieve a wider range of documents and chunks, but at the same time each chunk is too small to contain relevant information.

(00:36:02):
So we have very nice chunk design, how big each chunk should be. You add contextual informations like summary, metadata, hypothetical questions. Somebody was telling me just a very big performance they got is that from rewriting their data in the question-answering format. Instead of having... So they have a podcast instead of just chunking the podcast, you just reframe, rewrite it into here's a question, here's answers and produce a lot of them. It can use AI for that as well. So that's one example of data processing. A lot of example I see is for people helping, using AI to help specific [inaudible 00:36:40] use and documentations. And we write documentation. Usually a lot of documentation today is written for human reading and AI reading is different because it's different because humans, we have common sense and we kind of know what it is. So one things are, even for human experts, they have the context that AI doesn't quite have.

(00:36:59):
So somebody told me that what's a big change they have is let's say, that you have a function. The documentation for this, maybe the library. As a library said okay, the output of this one is maybe talking for, I don't know, some crazy term, maybe some temperature or something on the graph. It should be like one zero or minus one. And as a human expert maybe understand the scale, what one in the scale mean, but for AI, just really doesn't understand what that means. So actually, have another annotation layer for AI. It's like, okay, good temperatures equal one means like that. It's not like it's a actual temperature. It's associated with the scale over there. So just saving all this data processing to make it easier for AI to retrieve the relevant information to answer the questions.

Lenny Rachitsky (00:37:45):
This episode is brought to you by Persona, the verified identity platform, helping organizations onboard users fight fraud and build trust. We talk a lot on this podcast about the amazing advances in AI, but this can be a double-edged sword. For every wow moment, there are fraudsters using the same tech to wreak havoc, laundering money, taking over employee identities and impersonating businesses. Persona helps combat these threats with automated user business and employee verification. Whether you're looking to catch candidate fraud, meet age restrictions or keep your platform safe, Persona helps you verify users in a way that's tailored to your specific needs. Best of all, Persona makes it easy to know who you're dealing with without adding friction for good users. This is why leading platforms like Etsy, LinkedIn, Square and Lyft trust Persona to secure their platform. Persona is also offering my listeners 500 free services per month for one full year. Just head to withpersona.com/lenny to get started. That's withpersona.com/lenny. Thanks again to Persona for sponsoring this episode.

(00:38:51):
Awesome. Okay. So you've talked a bit about how you work with companies on these sorts of things, on their AI strategies, on their AI products, how they build, which tools they build, all these things. I want to spend a little time here because a lot of companies are building AI products. A lot of companies are not having a good time building AI products. Let me ask a few questions along these lines of what you've learned working with companies that are doing this well. One is just, I guess, in terms of AI tool adoption and adoption in general within companies, there's all this talk recently of just all this AI hype. The data is actually showing most companies try it. Doesn't do a lot, they stop. And so there's all this just maybe this isn't going anywhere. So in terms of just adoption of tools in AI within companies, what are you seeing there?

Chip Huyen (00:39:32):
For GenAI in company, I think there are two types of GenAI toolings that have been, I've seen ones is to internal productivity, like have coding tools, Slack chatbot, internal knowledge. A lot of big enterprises have some a wrapper around models, so with access to maybe some different type of a RAG solution. I think we talk about data or kind of like text-based RAG. We haven't talked about agentic RAG or I haven't talked about multi-modal RAG yet. But this, yes, it's a whole very exciting area around that. So basically, it should allow the employee to access internal document. Somebody ask, okay, I'm having a baby. What could be the maternal or paternal policy or am I having these operations with the health benefit cover that or I want you to interview, I want to refer my friend. What will be the process for that? So a lot of this having chatbot, internal chatbot to help with internal operations.

(00:40:35):
And another things, another category is more customer facing or partner facing. So product customers support chatbot is a big one. If you're a hotel chain, you might have a booking chatbot, which is somehow massive. A lot of booking chatbot because I guess it's... I do have this theory of a lot of applications companies pursue because they can't measure the concrete outcome. And I feel like booking or a sales chatbot, it's very clear. There was a conversion rate right now with that chatbot with human operators and what could be conversion rate with a chatbot and certain, somehow I think it's very clear outcomes and companies are easier to buy into these solutions. So a lot of companies have that customer facing chatbot.

(00:41:20):
So that is another category of tool and I think that for customers or external facing tools, because people are driven to choose applications with clear outcomes. So the questions of adopting them is really based on whether they see the outcome or not. Of course, it's not perfect because sometimes the outcome can be bad not because the idea or the application's idea [inaudible 00:41:52] is bad. It's just because the process of building it is not that great. Yeah. So it's tricky. For the internal adoptions of toolings or internal productivities, that's where it gets tricky. I would say a lot of companies [inaudible 00:42:08] think of AI strategy. I think of AI strategies usually have two key aspects. It's like use cases and the second is talent. You might have great data for great use cases, but you don't have talents and you cannot do it.

(00:42:23):
So a lot of time at the beginning with GenAI and sometimes I'm really admire a lot of companies for that, it's just like [inaudible 00:42:28] was like, okay, we need our employees to be very GenAI aware, very AI literate. So what I do is I start maybe adopting a bunch of tools for the team to use. They have a lot of up-skilling workshops, they encourage learning and then it's a really, really good thing. And it's also willing to spend a lot of money into adopting, giving people chargeability, subscriptions, purchase subscriptions, [inaudible 00:42:56] subscriptions to get the employees to be more AI literate. And that's the thing is a lot of... There's a [inaudible 00:43:05] may say, okay, we spend a ton of money on this tooling, but then we don't see because you can see the usage, but people don't seem to use them as much and what is the issue. So yeah, so I think that is tricky. Yeah.

Lenny Rachitsky (00:43:20):
What do you think is the issue? Is it just they don't know how to use them? What do you think is the gap here? Do you think we'll get to a place of just like, wow, work is completely different because of AI for a lot of companies?

Chip Huyen (00:43:32):
The main thing is it's really hard to measure productivity again. So I talk to a lot of people on their website. First of all, [inaudible 00:43:40] is coding. A lot of companies not using coding agents or coding [inaudible 00:43:45] coding. And I was asking, I was like, "Do you think that it helps with your productivity?" And a lot of times, the questions are very [inaudible 00:43:56] okay, I feel like it's [inaudible 00:43:59] better. And I said, okay, because we have more PRs, we see more code and then immediate [inaudible 00:44:04]. Okay, but of course, code, number of live code is not a good metric for that. So it's really, really tricky and it's something funny. So I do ask people to ask their managers because I work with usually VP level, so they have multiple teams under them. So I asked them, okay, do you ask some managers, okay, would you rather have access...

(00:44:28):
Would you rather give everyone on the team very expensive coding agent subscriptions or you get an extra headcount? Let's say maybe and almost everyone could say the managers could say headcount. But if you ask VP level or someone who manage a lot of teams, they would say just like [inaudible 00:44:48] good one, AI, a system as tools. And the reason is that we could say okay, because as manager is right, because you are still growing. You're not as a level when you manage hundreds of thousands of people. So for you, having one HR headcount is big. So you want that not for productivity reasons, but because you just want to have more people working for you. Whereas for executives, you care more about, maybe you have more business metrics that you care about. So you actually think about what actually drive productivity metrics for you. So it is tricky and I think that the question of productivity. I'm not sure it's fundamentally is the [inaudible 00:45:32] more productive, but it's just like we don't have a good way of measuring productivity improvement.

(00:45:37):
Another thing is also very [inaudible 00:45:40]. And I think it's like people do tell me that they notice different buckets of employees, different reactions to AI assist tools. First of all, I keep going back to coding because coding is big and it's easier to reason somehow. So it says I have different reports. One team would tell me that... One of people tell me, okay, amongst on his engineers, he thinks senior engineers would get the most output, would be more productive because it's like, okay, so that person's very interesting. So he actually divided his team to three buckets, but he didn't tell them, obviously. He was like, okay, here's more currently best performing, average performing and lowest performing. And then there's a randomized trial. So they give half of each group access to Cursor. And then [inaudible 00:46:31] noticed over time it was like, okay, something funny. The group that get the biggest performance boost, in his opinion, he was very close to his team.

(00:46:39):
The biggest performance boost [inaudible 00:46:41] the senior engineer, the highest performing. So the highest performing engineer get the biggest boost out of it. And then the second group is the average performing. So his opinion is like, okay, the highest performing engineers is also normal practice. They also know how to solve problems. So they have some solved problem better. Whereas the people who have the lowest performing, they only don't care much about work. So it's easier to just go on autopilot, get it to generate that code and just do it or just don't know how to do it. Another company, however, they tell me just actually, senior engineers are the one most resistant to using AI as this tooling because they said it's like, okay, but AI, because they are more opinionated and they have very high standard. It was like, okay, but AI code, [inaudible 00:47:30] code just sucks. So just very, very resistant in using it. So I don't know, I haven't quite been able to reconcile very different reports on that yet.

Lenny Rachitsky (00:47:39):
This is so interesting. So just to make sure I'm hearing what the story, so there's a company you work with, that did a three bucket test with their engineering team where they created three sorts of groups, the highest performing engineers, mid-performing engineers, lowest performing engineers, and gave some of them, so they gave some of them access to say, Cursor. Was it Cursor or what did they give them access to? It was Cursor, right?

Chip Huyen (00:48:03):
I think it was Cursor.

Lenny Rachitsky (00:48:04):
Okay, cool. And so within-

Chip Huyen (00:48:05):
I didn't work with them. This is more like a friend company.

Lenny Rachitsky (00:48:08):
Okay. It's a friend's company.

Chip Huyen (00:48:09):
Yeah.

Lenny Rachitsky (00:48:09):
So did they give half of the higher performing engineers Cursor and half not or how did they do the split there?

Chip Huyen (00:48:14):
Yeah, so they give half of the entire company but half of each bucket. Yeah.

Lenny Rachitsky (00:48:18):
Whoa.

Chip Huyen (00:48:19):
And then they observe the difference in productivity.

Lenny Rachitsky (00:48:21):
I see. So how do they even do that? They're just like, "Okay, you get cursor, you don't get cursor." How did they do that? That's so interesting.

Chip Huyen (00:48:31):
Yeah, I didn't get into the mechanics of it, but I was like, "I respect you for doing a randomized trial on that."

Lenny Rachitsky (00:48:33):
That is so cool.

Chip Huyen (00:48:33):
Yeah. Yeah.

Lenny Rachitsky (00:48:34):
Okay. Wow. How large was this engineering team? Was it like hundreds of people?

Chip Huyen (00:48:38):
It's not that large. It's about maybe 30 to maybe 40. Yeah.

Lenny Rachitsky (00:48:43):
30 to 40. Okay.

Chip Huyen (00:48:44):
Yeah.

Lenny Rachitsky (00:48:44):
Wow. Okay. So they found that the highest performing engineers had the most benefit from using AI tools and then behind them was the middle tier engineers and the worst performers or the lowest performers. Okay.

Chip Huyen (00:48:59):
But it's also not the same everywhere.

Lenny Rachitsky (00:48:59):
Right. Right. Right, right.

Chip Huyen (00:48:59):
Some companies are different.

Lenny Rachitsky (00:49:03):
Right. This other example you shared of just senior engineers in this one example are most resistant to changing the way they work, which I get. I do feel like the most valuable people right now other than ML researchers and AI researchers like yourself, are senior engineers because it feels like junior engineers are just, so much of this is now done by AI, but an engineer that knows what they're doing that understands how things work at a large scale with AI tools, just basically infinite junior engineers doing their bidding, feels like an extremely valuable and powerful asset.

Chip Huyen (00:49:39):
Yeah, I definitely really appreciate, as you see companies, we appreciate engineers who have a good understanding of the whole systems and be able to have good problem solving skill are thinking holistically instead of locally. Or when our company have seen the way they work, as they told me is we're completely different now. So they actually restructured engineering org so that they get more senior engineers should be more in the peer review because they get writing guidelines on what is a good engineering practices, what is the process would be like.

(00:50:12):
Or maybe like okay, so they write a lot of processes on how to work well. And then they have more junior engineers just produce code and submit PR, but senior engineer more in the reviewing case. So I think it might be prepared for the future. So another company actually told me something very similar. So preparing for the future once they only need a very small group of very, very strong engineers to create processes and reviewing code to get into production but get AI or junior engineers to produce code. But then the question becomes just like, how does one become a very strong senior engineer.

Lenny Rachitsky (00:50:54):
Right. That's right. That's right. That's the problem. Yeah.

Chip Huyen (00:50:57):
Yeah. So I don't know what's the process I was thinking about, yeah.

Lenny Rachitsky (00:51:01):
No one's thinking about it. It's a problem. We won't have any more in 10, 20 years. There'll be no more engineers because no one's hiring junior engineers. Although I could make the case. Junior engineers, people just getting into computer science right now, are just AI native. And in theory, you could argue they will become really good really fast if they're curious, aren't just delegating, learning and thinking to AI, but learning how to actually, using it to learn how to code well and architect correctly. You could argue they'll be the most successful engineers in the future.

Chip Huyen (00:51:33):
I do think that what I mentioned said relating to architect. I think I grouped that in my system thinking. I do think it's very important skill because I think AI can help automate a lot of disjointed skills, but knowing how to utilize the skills together to solve problems is hard. So that's a webinar between Mehran Sahami who is one my favorite professors. He was a chair of the curriculum at the CS Department at Stanford. So he spent a lot of time thinking about CS educations, what should students learn nowadays in the area of AI coding. And then the other person is Andrew Ng, which is of course, is a legend in the AI space. And Mehran Sahami, Professor Sahami, said something very interesting. He said a lot of people think that CS is about coding, but it's not. Coding is just a means to an end.

(00:52:27):
CS is about system thinking, using coding to solve actual problem and problem solving will never go away because what AI can automate more stuff. The problem is just get bigger. But as a process of understanding what caused the issue and how to design step-by-step solution to it, will always be there. So I think an example of, I actually have a lot of issues with AI for in the way of it's debugging. So I'm not sure you use a lot of AI for coding, but something I have noticed and also seen from my friends, it's like it is pretty good when you have very clear, well-defined tasks. Maybe write documentations, fix specific features or build an app from scratch. Doesn't have to interact with a large access in code base, but you added something a little bit more complicated, maybe required interaction with other components and stuff. It's usually not that good.

(00:53:21):
And for example, I was using AI to deploy an applications and it was testing out a new hosting service I was not familiar with. It was like, okay. Usually they inform me, so working AI does give me is confidence to try a new tool. Before what AI is like trying new tools has written, not documentations for the beginning, but I was like, okay, just try it out and learn. So I was testing out this new hosting service and it kept getting a bug, so was very, very annoying. And it was like, okay, I asked [inaudible 00:53:51], fix it. And it kept changing the way, maybe change the environment variable, fix the code, maybe not change from the function to this function, maybe change the language, maybe it doesn't process JavaScript, I don't know, whatever. And it didn't work. And it was like, okay, that's it.

(00:54:07):
I'm just going to read documentation myself and see what's wrong. And it turns out, it's like I'm on another tier, the [inaudible 00:54:16] I want did not, is not available in this tier, right? So I feel like, okay, so the issue with [inaudible 00:54:22] was just trying to focus on fixing things from a different component versus the issue is from a different component. So I think of, okay, be understanding how different components work together and where the source of issue might come from. You need to give a holistic view of it. And it's made think is like, okay, how do we teach AI system thinking that I have all the human experts having very much [inaudible 00:54:46] scaffold just like, okay, for this kind of problem, look into this, look into that, look into that, and then stuff. So [inaudible 00:54:53] that could be one way, but that's also made me think is, how do we teach humans, system thinking? Yeah. So yeah, I think it's very interesting skill. I do think it's very important.

Lenny Rachitsky (00:55:04):
That's exactly the same insight Bret Taylor shared on the podcast. He's the co-founder of Sierra. He created Google Maps. He was CEO of Salesforce, Quip, a few other things. And I asked him just like, should people learn to code? And his point is exactly what you said, which is taking computer science classes is not about learning Java and Python. It's learning how systems work and how code operates and how software works broadly, not just, here's a function to do a thing.

(00:55:32):
One thing that I wanted to help people understand, you wrote this book called AI Engineering, which is essentially helping people understand this new genre of engineer and you have this really simple way of thinking about the difference between an ML engineer and an AI engineer, which has a really good corollary to product managers now, of just an AI product manager versus a non-AI product manager. The way you describe it and fill in what I'm missing is just ML engineers built models themselves. AI engineers use existing models to build products. Anything you want to add there?

Chip Huyen (00:56:05):
One thing I really dislike about writing books is that it has to define this and I think it's like no definitions would be perfect because they always be edge cases. But yeah, in general, I think it's just like GenAI as a service, more as a service, when somebody build the models for you and the base model performance is a pretty [inaudible 00:56:26]. So it's like it's enabled people to just like, okay, now I want to integrate AI into my product. I don't need to learn [inaudible 00:56:34] even though knowing that could really help. But yeah, it makes an entry barrier really low for people who want to use AI to build product and at the same time, AI capabilities are so strong. It's also increased the possibilities, the type applications that AI can be used for. So I think yes, both entry barriers' is super low and a demand for AI applications a lot bigger. So it feels, it's very, very exciting. It's opens up a whole new ball of possibilities.

Lenny Rachitsky (00:57:04):
Yeah. It's like now you don't have the time, now you don't have to spend time building this AI brain. Now you can just use it to do stuff, such an unlock. Okay. Maybe just a final question. You get to see a lot of what's working, what's not working, where things are heading. I'm curious just if you had to think about in the next two or three years, just where things are heading, how do you think building products will be different? How do you think companies working will be different if you had to think of maybe the biggest change we expect to see in the next few years, in terms of how companies work?

Chip Huyen (00:57:40):
I think in a lot of organizations they don't move that fast, but at the same time, they move faster than I expected because again, I think it's like bias and don't work with dinosaur companies who don't care. I think a lot of executives who come to me are very forward-looking. So maybe for me, I'm very biased towards organizations is move fast. So yeah, I think one big change I see just in organizational structure. I think this a lot of value plays in... So before we have a lot of disjointed teams. We have very clear engineering team, product team, but then there's a question of who should write eval? Who should own the metrics? And it turns out, eval, it's not a separate problem. It's a system problem because you need to look into different components, how they interact with each other. You need user behaviors because you need to know what users care about so that you can write eval reflect what users care about.

(00:58:44):
So all of that you can sort it from you look into different component architectures, place guardrails and stuff. So it's just engineering, but understanding users is what product. So because of a lot of things and eval is extremely important. So the kind of bring product team and engineering team, even marketing team like user acquisition, very close to each other. So yes, since in a ways if people are structuring, so that's more communications between previously very distinct functions. Another thing is I also see as teams, of course, I think about what can be automated in the next few years and what work cannot be automated. And I seen that people already shedding, actually it's a little bit scary to think about it, but I also think it's the teams, they would've told me, it's just like okay, this is good and you and me, but we have got rid of these functions for a lot of things like previously outsourced, for example.

(00:59:37):
Traditionally, it's a business outsourcing that's not core to them and can be in a more systematized. So with that, you can actually use AI to automate a lot of that. And so as a separation people thinking more of what is the value of junior engineers or senior engineers, how should we restructure engineering org for that? Yeah, so I do definitely think that is one thing to successful organization. People are just moving pieces around and thinking about use cases, whether you need to spin out new use cases and who would lead a new effort. That is one big change. Another thing in terms of AI, I think there's, I'm not sure how true this is. I guess, I'm also on the camp of thinking that it has merit, is a camp of okay, base models we have probably not quite maxed out, but we're unlikely to see really, really strong, crazily strong model.

(01:00:44):
So you remember when we have GPT, right? And then GPT2, which is a big step up, an [inaudible 01:00:49] better than GPT and then GPT3, which much, much bigger than GPT4, much, much bigger. And then of course, GPT5, but it's GPT5, that scale of much bigger step jump compared to the previous, I think it's debatable. So I think that we had disappointment, the base model performance improvement is not going to be mind-blowing. It was in the last three years. So I think there's a lot of improvements when I see in the post-training phase, in the application building phase. And yes, also I think that's where I feel I would see a lot of improvement there. I also very interest in multimodality. So we've seen a lot of text base, but I think there's a lot of audio, videos use cases that is very, very exciting.

(01:01:45):
And I think audios is not quite as solved. Well, I think because I do work with a couple of voice startups and when it comes to, think about voice, it's an entirely different beast. So let's say have chatbot. We go from a text chatbot to voice chatbot. It's like the consoles are completely different because now with voice chatbot, we need to think about latency because I think multiple steps, first have voice to text, text to text, text question into text answer and then text to voice answer. So you have multiple hops and latency become very important. And there's a question, what does it make you sound natural? So for example, people think of in AI and humans, when humans talk to each other, if I say, you try to interrupt me and say, Chip [inaudible 01:02:36]. I would pause and I try to hear you out.

(01:02:38):
But sometime even if I just like say some word, like acknowledge when I, mm-hmm, mm-hmm, that I shouldn't stop. It's just continue. So the question of forced interruption and whether it's, should I stop or not, it's a big in what perceived as natural conversations. And that's also regulations because a lot of time, people want to build AI chatbot, voice chatbots that sound like humans, try to trick users into thinking that they're talking to humans, but also maybe potential regulation saying okay, you have to disclose to users when you talk, if the bot is talking to is human or AI. So I think this a whole space, I think it's not quite as solved as you think. But it's not quite like an AI foundation model problem because a human interruption detection, it's actually a classical machining problem.

(01:03:32):
It's a different framing, but you can give classifier for that. Or the question of latency, actually a massive engineering challenge, not an AI challenge. Of course, it can be an AI challenge because people are trying to build voice-to-voice model. So instead of having to firstly transcribe the voice from me into text and then get a model [inaudible 01:03:54] text answer and get another model should turn from text to speech, you can just do voice-to-voice directly. So that is something we're working on, but it's very hard. Yeah. So yeah, so even audio, I think of it's the easier than video because video have both image and voice. It's already pretty hard. So I think there's a lot of challenges in that space.

Lenny Rachitsky (01:04:16):
That was an awesome list of things. Let me mirror them back real quick. So what you're predicting in the next few years, things that will change in the way we work, and these actually resonate with so many conversations I've had on this podcast. So says, just kind of doubling down on where things are heading. One is the blurring of lines between different functions instead of just design engineering. Everyone's going to be doing a lot of different things now. Two is, just more of work being automated with agents and all these AI tools and just in theory, productivity going up. Third is, a shifting from pre-training models to post-training, fine-tuning and things like that because to your point, models maybe are slowing down in how smart they're getting.

(01:04:57):
Although, I'll point folks to the, I had a chat with the co-founder of Anthropic. He made a really good point here. He's like, we're really bad at understanding what exponentials feel like when we're in the middle of that. And also, models are being released more often. So the difference between them we may not notice because they're just happening more often versus GPT3 came out a year before after GPT2. Maybe true, maybe not. And then the fourth point you made is this idea of multimodal, investing in multimodal experiences. I cannot wait for ChatGPT voice mode to get better at interruption, exactly what you're saying. I'm just talking to it and then someone makes a little sound and it's like [inaudible 01:05:33]. Okay. And then you have to, and then it's like, and then it stops talking. It's so annoying.

Chip Huyen (01:05:36):
I'm shocked that we don't have better voice assistant at home yet. I think I have been testing out a bunch, honestly. I keep hoping, oh my God, that could be the one and then I know how many of them I just had to give away because they're not that good.

Lenny Rachitsky (01:05:49):
I think it's coming. I hear it's coming. Anthropic's working with someone that, I don't know if it's launched or not yet.

Chip Huyen (01:05:54):
Yeah, [inaudible 01:05:55] want to bring back to what you mentioned about your guest from Anthropic, mentioned about the performance improvement. I think there's a big change, I think this difference between a model-based capability. So I'm talking about the pre-trained model versus the perceived performance perform. So let's say, I'm not sure you thought about, are you familiar with the term test time compute?

Lenny Rachitsky (01:06:20):
I don't think so. Help us understand.

Chip Huyen (01:06:26):
So this idea is like okay, you have a fixed amount of compute. So you're going to spend a lot of compute on pre-training or training the model. Pre-training and then I've spent a lot of some compute fine-tuning and the ratio of pre-training to the post-training compute is crazy, varies between different lab. And also, since then has a spend compute on generate inference. When I have a trends and fine-tuning model and now you want to serve it to users. So I might type a question in a prompt and if generate, do inference and that requires a compute. And I guess, I feel about discussion of should I spend more compute on pre-training or fine-training or inference because inference and people thought I was just like test time compute. So spending more compute on inference is like calling test time compute as a strategy of just allocating more resources, compute resource to generate inference when I shouldn't bring better performance and how does that do it?

(01:07:22):
Let's say you have a math questions and maybe instead of just generate one answer again generate four different answers and say okay, whichever is the best according to some standard or okay, I have four answers and then maybe three of them say 42 and one of them says 20. You say okay, three of them in agreement. So the answer should be 42. So just people shouldn't generate a bunch of it. Or another thing is a lot of time like reasoning, thinking, it just be able to generate more thinking tokens, like spend more time thinking before showing the final answers. It's like require more compute but also give more better performance. So yeah, so I think it's like from the ease of perspective when the model spend more time exploring different potential answers, thinking longer, it can give you much better final answers. But the base model itself does not change.

Lenny Rachitsky (01:08:16):
Awesome.

Chip Huyen (01:08:17):
Does it make sense?

Lenny Rachitsky (01:08:18):
Yes, that does. Absolutely.

Chip Huyen (01:08:18):
Yeah?

Lenny Rachitsky (01:08:19):
That is a good corollary to Ben Man's point.

Chip Huyen (01:08:23):
Yeah.

Lenny Rachitsky (01:08:23):
Chip, we covered a lot of ground. I've gone through everything I was hoping to learn and more. Before we get to a very exciting lightning round, is there anything else that you wanted to share? Anything else you want to leave listeners with?

Chip Huyen (01:08:34):
So I do work with a few companies that does these things of they want employees to come up with ideas. So there's a big debate on what is a better way for AI strategy, should they be top out or bottom up, should executives come up with one or two killer use case and everyone allocate resource to that, should you give engineers and PMs and smart people come up with ideas. And I think it's a mixture of both. So some companies it was like, okay, we hire a bunch of smart people, let's see what they come up with and they organize more hackathons or internal challenge to get people to build product. And one thing that I noticed, a lot of people just don't know what you built. And it shocked me why I feel like we are in some kind of an idea crisis, right?

(01:09:21):
Now, we have all this really cool tools to have. You do everything from scratch, can have you design, it can have you write code, it can build website. So in theory, we should see a lot more, but at the same time, people are somehow stuck. They don't know what to build. And I think it's like, maybe you see a lot of had to do with maybe society expectations because we have gone into this phase of specializations, people very highly specialized and people are supposed to focus on one thing really well instead of being a big picture. And we don't have a big picture view. It's hard to come up with ideas of what you build.

(01:09:58):
So I know what, when I work with this company on this hackathon, we do work on come up with a guideline, how to come up with ideas. And usually what we think of is like, okay, one tip is go look from the last week. For a week, just pay attention to what you do and what frustrates you. And when something frustrates you, think about, is there anything we can do? Can it be done a different way? So it's not frustrating and you can talk, people can swap to accept [inaudible 01:10:27] or teams, and I even see they come on frustrations. Maybe there's something you can think about just to build something around that. So yeah, so I feel like just notice how we work, thinking of ways, constantly ask questions, how can this be better? And then I just build something to address the frustrations, I think it's a good way to learn and adopt AI.

Lenny Rachitsky (01:10:46):
I think people have felt exactly what you're describing every time they open up one of these vibe coding tools where you could just describe anything you want. I'm like, "I don't know, what do I want?" And I love this very tactical piece of advice, just like what frustrates you, just pay attention to where you're frustrated. For example, I just built a very cool little vibe coded app. I was working on a newsletter post inside Google Docs and I pasted all these images into the Google Doc, from screenshots and stuff and then I forgot, oh yeah, you can't take images out of Google Docs. It's like this Hotel of California experience where you can paste stuff into it, very hard to get images back out. So I just went to all the vibe coded tools and just built an app that I can give you a Google Doc URL and it let me download all the images automatically. And it worked amazingly well and I made it really cute. And I'll link to it in the show notes.

Chip Huyen (01:11:33):
OH, I would love to see that. I'm very bullish on using AI, just create micro tools. It's just something just make your life a bit easier.

Lenny Rachitsky (01:11:41):
A hundred percent. I feel like that's one of the main ways people are using these tools, just a little niche problem they have. With that, Chip, we've reached our very exciting lightning round. I've got five questions for you. Are you ready?

Chip Huyen (01:11:54):
Yeah, always. No, no, no. It depends on how hard the questions are.

Lenny Rachitsky (01:11:58):
They're very consistent across every guest. So I imagine you've heard them before. First question, what are two or three books that you find yourself recommending most to other people?

Chip Huyen (01:12:10):
I'm really terrified of book recommendations because I feel like what books [inaudible 01:12:15] you should read really depends on what they want and where they're in life and where they want to get to. But just several books that I do think's have really changed the way I think and see the world. So one thing is The Selfish Gene, that's to understand, it actually helped me with the question whether I want to have kids or not because it's understanding more of a lot of our functions, the way we operate is the functions of our genes and genes want to do one thing, to procreate.

(01:12:46):
So yes, in a way, the book also proposed another thing is so everyone wants to live forever and maybe it's not consciously, but subconsciously, we do want that. And there are two ways. One is via genes. Genes [inaudible 01:13:00] want to continue forever, but [inaudible 01:13:03] two ideas. I think there's something [inaudible 01:13:05]. It's just like being able, if you have some ideas out there and then it's last for a long time, it's going to live on. I know it's a little bit abstract, but I thought it's very interesting.

(01:13:16):
The other books I really, really like is from the book from Singaporean previous, I think he is [inaudible 01:13:24] as a Father of Singapore, I don't know, Lee Kuan Yew. I'm not sure what's the title is, but he was the one who led Singapore from, he's changed Singapore from a Third World country to a first world country within 25 years. And I have never seen any country leaders spent so much effort into putting down his thought of how to build a country like that.

(01:13:47):
And as I talk a lot about public policy, how to create policies that encourage people to do the right things that is good for the nations and also talking about foreign affairs, foreign policies, the liberation of the country, but other. So it's a really good book to think about. For me, it's a system thinking, but it's a different kind of system which a country, which a lot of us don't get a chance to ever experiment in our life. So it's good to learn about that.

Lenny Rachitsky (01:14:13):
What was the name of that second book?

Chip Huyen (01:14:15):
It's called From Third to First World. Actually, I think I have it somewhere here. Yeah.

Lenny Rachitsky (01:14:20):
There it is.

Chip Huyen (01:14:21):
It's a very heavy book.

Lenny Rachitsky (01:14:21):
Show and tell.

Chip Huyen (01:14:23):
Yeah.

Lenny Rachitsky (01:14:23):
That's awesome. I definitely want to read that. That's a really good [inaudible 01:14:26]. I've heard a lot about just the impact he's had and I've seen all these videos on Twitter of just his really wise insights into how to build a thriving society. And clearly, it works.

Chip Huyen (01:14:34):
Yeah. Can you believe, how does he time to write such a thick book? It's insane.

Lenny Rachitsky (01:14:39):
That is. Claude, please summarize. I'm just joking. By the way, Selfish Gene, I also absolutely love that book. That is such a good choice. It's such an under the radar kind of book that really changed the way I see the world as well. So really good pick. Okay, next question. Do you have a favorite recent movie or TV show you really enjoyed?

Chip Huyen (01:14:56):
So I watched a lot of movie and TV shows as a research because I working on my first novel and I recently sold it. So I'm interested what makes, it's a drama. It's not a science fiction or anything that tech people usually read. So it very, I know it's a very out of left field and very, so it's almost like reading, watching TV to see what kind of stories become popular, trying to understand the trope and stuff like that. So I'm not sure if the audience will like...

Lenny Rachitsky (01:15:28):
Well, what's one? What's one that taught you something about writing?

Chip Huyen (01:15:35):
I think like Yanxi Palace. It's a Chinese TV show.

Lenny Rachitsky (01:15:37):
Cool. Okay. I haven't heard that one on the podcast before. Okay, cool.

Chip Huyen (01:15:37):
Yeah.

Lenny Rachitsky (01:15:43):
Next question. Do you have a life motto that you often think about, come back to when you're dealing with something hard, whether it's in work or in life?

Chip Huyen (01:15:51):
This sounds very nihilist. I think to say, in the end, nothing really matters. Usually, I think of in the grand scheme of things, in a billion years, nothing will, no one would ever be there. I think okay, someone will argue with me about that. [inaudible 01:16:05]. So my theory's like, in a billion years, none of us would ever exist. So whatever messy things, like crazy things we do or how bad we do it, I mean, no one would be remember, wouldn't be there to remember it. And I think in a way, it sounds scary, but it's very liberating because it just allows me say, okay, let's just try things out, right? Why does it matter? And there's a story of recently, so I have some family member who passed away recently. And I was talking to my dad because I couldn't be home for that.

(01:16:36):
I was asking my dad like, "Okay, os there anything I can do to make the person..." Something like comfort. So anything that you can get the persons. And my dad was just like, "What can he possibly want at this moment?" It just made me feel at the end of life, there's nothing that can bring you, like material can bring you joy. There's no money, no product, nothing. And in way, it makes me feel like, okay, what really do I really care about at the end of the day? So I guess it's like I think about it. It's just like, okay, maybe I fail it, maybe I don't get that contract. Maybe those things, but in the end of life, I don't think that actually really matters. So in a way, it's quite liberating.

Lenny Rachitsky (01:17:15):
I know you said it might be nihilistic. This is what Steve Jobs shared too in one of his most famous speeches. Just we all die someday day, so don't take things so seriously and it is freeing. Absolutely. It just makes you appreciate every moment, every day you have. Just like, yeah, let's just do something hard and scary. Okay, final question. You talked about how you're writing a novel. Most people in tech have never written something creative and fiction. What's just one thing you learned in the process about how to write better stories, better fiction?

Chip Huyen (01:17:46):
A lot of time when we read, we get tripped up by some small things. So I think I want to do creative writing because I just want to go a better writer and it tells us maybe try a different audience could have me become better at anticipating what this different type of audience would want to hear and what they care about. So it's a way for me to get a... So I think if I write it or even any kind of content creations is about predicting the user's reactions, right?

Lenny Rachitsky (01:18:14):
The next token.

Chip Huyen (01:18:15):
You do a podcast.

Lenny Rachitsky (01:18:15):
Just kidding.

Chip Huyen (01:18:17):
Yeah. Yeah, so you do a podcast, it's like, okay, what kind things that the users could find engaging, right? And I find this a little bit and a lot of companies you have launch a product, you have a narrative coming out and say, okay, how do we position this product in a way that users would want? So I feel like I have done technical writing for a while and I felt like I had some experience trying to predict what engineers would want to hear or care about. But then I don't have any experience like this, completely different type of audience. So that's what I want to, creative writing, writing a story. And that's why I was doing a lot of research [inaudible 01:18:55]. I mean, doing research [inaudible 01:18:56] enjoyed a lot, watching a lot of dramas. I just see what people like. So one thing that I care about is, I think I learned what emotional journey was from a editor.

(01:19:05):
So when we write something we care about how users would feel across a story. We want something in the beginning, we want something, we need to have a hook so that people continue reading. But we also don't want too much of drama because we'll get too tired because you're emotionally exhausted because it's like you're being emotionally manipulated a lot of time. So it gave a emotional journey, maybe have some climax or something more chill, maybe like... And also care about another thing I didn't realize is, for me, for technical writing, you entirely focus on the content, the argument. It's very impersonal. For example, people like ML compilers, doesn't matter if they like the person telling them about compiler or not because it's just objective [inaudible 01:19:56]. But for a novel, people care about character likeability.

(01:20:00):
So in the first version of my story, it makes the characters a little bit more, very logical, very rational, and just does everything just very rationally. And then the feedback I got is, I have a very good friend read it and he was like, he's an amazing person, he's a great person. And he was like, "Chip, I'll be honest, I hate that person." So it doesn't matter as a story, it's just like the person is so unlikeable, that's why he doesn't want to continue. So is a second version. It makes that person, the character more likable. How she makes that character more likable is that you put in some vulnerability sometimes it's like okay maybe it's person have setback because sometimes we can relate to it. So in a lot of ways, it's very interesting. A lot of it is about understand the emotional bit, like how the users feel, not just about the story but also about the characters.

Lenny Rachitsky (01:20:50):
That is so interesting. Wow. I learned a lot more there than I thought. That was awesome. Really good example. Chip, two final questions. Where can folks find you online, if they want to reach out and maybe work with you or maybe even just share the stuff that you offer if folks want to reach out. And then how can listeners be useful to you?

Chip Huyen (01:21:08):
I'm on social media, LinkedIn, Twitter. I don't post a lot, but I keep telling myself that I should do more because I kind of like the conversation with readers. So I'm actually about to I start a Substack. So I have a placeholder for Substack right now and I'm thinking of doing it for more system thinking because I think it's a very interesting skill. I'm also thinking of doing a YouTube channel on book reviews and basically books than help you think better. So I think it's the first book I'm a review is probably like this book because it's my favorite book growing up and I've been keep on reading it. So yeah, so how can you be helpful? Send me books that you like, books that help you have changed the way you think or change you the way you do anything. So I would appreciate it.

Lenny Rachitsky (01:22:00):
Amazing. I'm excited to read that book.

Chip Huyen (01:22:02):
Mm-hmm.

Lenny Rachitsky (01:22:03):
Chip, thank you so much for being here.

Chip Huyen (01:22:05):
Thank you so much, Lenny, for having me.

Lenny Rachitsky (01:22:07):
Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

