---
guest: Marily Nika
title: AI and product management | Marily Nika (Meta, Google)
youtube_url: https://www.youtube.com/watch?v=qNPPoj1qUG0
video_id: qNPPoj1qUG0
description: 'Marily is a computer scientist and an AI Product Leader currently working
  for Meta’s reality labs, and previously at Google for 8 years. In 2014 she completed
  a PhD in Machine Learning. She...

  '
duration_seconds: 2882.0
duration: '48:02'
view_count: 71782
channel: Lenny's Podcast
keywords:
- growth
- retention
- activation
- metrics
- mvp
- iteration
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

# AI and product management | Marily Nika (Meta, Google)

## Transcript

Marily Nika (00:00):
There is something called the shiny object trap, and I'm always telling people, "Hey, don't do AI for the sake of doing AI." Make sure there is a problem there. Make sure there is a pain point that needs to be solved in a smart way. Once you have identified what that problem is and what that very, very high-level solution is, then reach out and try to figure out how to actually implement it.

Lenny (00:28):
Welcome to Lenny's podcast where I interview world-class product leaders and growth experts to learn from their hard one experiences building and scaling today's most successful companies. Today my guest is Marily Nika. Marily teaches the most popular course on Maven on AI and product management. She's currently product lead at Meta focusing on Metaverse, avatars and identity. Prior to Meta, she was at Google for over eight years working on Google Glass, computer vision and machine learning around speech recognition. In our conversation, we touch on what PMs should be paying attention to when it comes to what's happening in AI. We talk about a bunch of resources that'll help you get started in the world of AI. How AI tools available today can already help you do your job better as a PM.

(01:12):
We also get relatively technical into what exactly is a model, how are models trained, all kinds of fun stuff like that. Enjoy this conversation with Marily Nika after a short word from our wonderful sponsors.

Speaker 3 (01:26):
This episode is brought to you by Amplitude. If you're setting up your analytics stack but not using Amplitude, what are you doing? Anyone can sell you analytics while Amplitude unlocks the power of your product and guide you every step of the way. Get the right data, ask the right questions, get the right answers, and make growth happen. To get started with Amplitude for free, visit amplitude.com. Amplitude, power to your products.

Lenny (01:53):
This episode is brought to you by EPPO. EPPO is a next-generation AB testing platform built by Airbnb alums for modern growth teams. Companies like Netlify, Tenfold and Cameo rely on EPPO to power their experiments. Wherever you work, running experiments is increasingly essential, but there are no commercial tools that integrate with a modern growth in stack. This leads to waste of time building internal tools or trying to run your experiments through a clunky marketing tool. When I was at Airbnb, one of the things that I loved about our experimentation platform was being able to easily slice results by device, by country, and by user stage. EPPO does all that and more, delivering results quickly and avoiding annoying prolonged analytics cycles and helping you easily get to the root cause of any issue you discover.

(02:41):
EPO lets you go beyond basic clickthrough metrics and instead you turn north star metrics like activation, retention, subscriptions and payments. And EPPO supports test on the front end, the backend, email marketing and even machine learning clients. Check out EPPO at geteppo.com, get E-P-P-O.com and 10x your experiment velocity.

(03:06):
Marilee, welcome to the podcast.

Marily Nika (03:08):
Thank you. Hello, thank you for having me.

Lenny (03:10):
It's very much my pleasure. We've interacted a little bit on Twitter. We've never actually talked before just right now. I've seen your course just all over the place, your course on AI and PM. And so I just thought it'd be really fun to have you on and help us all understand what the hell is happening in AI and especially AI and product. So thanks again for being here.

Marily Nika (03:33):
Yes, thank you. I'm really excited.

Lenny (03:36):
I would love your help as a former full-time PM/everyone listening that is a current PM, to help us understand what is going on with AI and product tech in general and tools in general. Move really fast, if you're trying to pay attention to what's happening, it's really hard to stay up to date on where things are going and it feels especially hard in AI.

(03:57):
It feels like there's just something coming out every day. And so I have a bunch of questions along these lines. The first is just like what media do you pay attention to stay on top of what's happening and what's new and what's interesting in the world of AI and machine learning?

Marily Nika (04:11):
As you know very well, subscribing to newsletters is something that's really impactful. And of course, I subscribe to your newsletter, but I am a big, big, big fan of the download by MIT Ecology Review or Atelier. And they're not necessarily AI-centric, but what I'm advocating for and what I'm telling people is that in the future everything will be AI by default. So even if you have something that's technology focused, you'll see a lot of AI starting to get sprinkled in there.

Lenny (04:40):
I want to follow up on what you just said there, but maybe we'll save it a little bit. Maybe going in a different direction first, what do you think is overhyped in the space of AI right now? What do you think is under hyped and undervalued?

Marily Nika (04:52):
I would like to discuss strategy between, which is both under hyped and over hyped at the same time. I was reading this article this morning where there are writers complaining and they're very, very fearful and they think, "Oh, writing online is going to die. Everything we've studying for is going to be replaced. They're going to take our jobs and so on." And I'm just like, "No, no, no. Charging PT and technology is enhancing our work. It's enhancing us. It does not steal from us." So that's what comes across right now. And there are other things that are under hype, but obviously ChatGPT is amazing. I'm using it day to day, but there are other things AI can do in an amazing manner.

(05:34):
I was reading a research article the other day that said that AI can now detect place. So lie detection, whether I is for security reasons or at work or anything like that is now possible. So I encourage people to go to these newsletters and go to these online blogs, 10 prints and so on, and just read what's happening. It's not all about chat reading, there's more, there's more about AI, but you should read a lot.

Lenny (05:58):
You mentioned that you use ChatGPT in your work life. Talk about that. What are you actually using it for?

Marily Nika (06:04):
Even when I'm at work and I am trying to come up with a nice mission statement, when we're PMs will come up with mission statements, it's just crucial part and it's where the core begins. You want to get people excited, you want to get people inspired. There is nothing I can write that's going to be as good as what ChatGPT looks like. So what I do is I literally go to ChatGPT and I say rewrite this mission statement from me and even the first try produces something which is fantastic, so that.

(06:34):
Number two, it helps me create user segments in a fantastic way. It will think of user segments that your mind wouldn't even go there, it just wouldn't go there. And it will provide the motivations, it will provide the pinpoints and you just come up with ideas as you read it. And then the last thing that it does is it provides ideas for you whether AI enhanced. So I just use a day-to-day, even [inaudible 00:07:00] day-to-day workflow, but I'm not making it do my job for me, I'm asking it after I have already had a mission in my head and what it is I want to do.

Lenny (07:10):
So is the way you're approaching it is you just put in, come up with a better mission statement then and then you give it your version of the mission statement?

Marily Nika (07:18):
Exactly.

Lenny (07:19):
Interesting. And you're saying that that comes up with a better mission statement than the one you had?

Marily Nika (07:25):
It's better because the mission statement is going to be read by all disciplines. It's not just going to be read by PMs that already have a lot of context and understand. It's going to be read by leadership, by junior people, by stakeholders, by other departments, by competitors. And you needed to be on Orient ending the words that are meant to be understood by everyone. Even a kid could understand and they would get inspired by you as well.

Lenny (07:49):
And then you also said he use it for personas. How do you actually frame that prompt with ChatGPT?

Marily Nika (07:55):
Let's say you're working for a specific product area and you know want to create some fitness band, so you would say something like, who would be interested in the fitness band that doesn't have a screen? And it will provide a bulleted list all of people like, hey, young professionals are that they're interested but don't have enough time. People that do not want to charge their wearables every day. Then the list goes on. It's just fantastic.

Lenny (08:24):
You were talking about how you think the future of AI is, it's the default and is what you mean there that it's basically baked into every product we use and it helps the user do better things, it helps the product work better. Is that what you mean or is it something else?

Marily Nika (08:39):
I believe that ballpark managers will be AI product managers in the future. And this is because we see all products needing to have a personalized experience, a recommender system that is actually good. I mean you cannot watch to Netflix, you cannot even watch a movie without needing that. After you watch White Lotus or Stranger Things, you will want something similar to watch. You're not going to want a romantic thing to be suggested or recommended to you.

(09:06):
Also, automation is another thing. We need to keep improving on society. We need to keep making technological advancements. You're not going to be able to do that if you don't have an AI centric view in every sector that you're working on.

Lenny (09:20):
When you say that every PM will be an AI PM is your thinking that you'll be using AI tools in your job as a PM or that you'll be building AI into everything you're building with? How do you think about that?

Marily Nika (09:35):
I think it's that you will need to get comfortable with having a partner that's a research scientist and you will need to understand that these people can produce a smart model. They'll be able to do some automation, some personalization, some recommendations on. In a lot of people, truly uncomfortable, a lot of people don't know how to approach the researchers. A lot of people don't like the uncertainty that research has. A lot of PMs are very, very used to, "Okay, I'm going to do this, I'm going to launch, I'm going to do this, I'm going to launch." Whereas when you're working with research, it's more like we're going to try this and then in a year if it doesn't work out we're going to shut the written down and repeated completing [inaudible 00:10:17]. So I feel that if people get more used to uncertainty and research, things are going to be good in the end for them.

Lenny (10:28):
I thought you were comparing ChatGPT as a researcher you're working with, but you're actually saying people will have PhD researchers on their teams helping them build models into their product to make their product better. Is that what you're saying?

Marily Nika (10:43):
Correct. This is exactly what I'm-

Lenny (10:45):
Interesting.

Marily Nika (10:47):
And from a product perspective I can imagine like three bubbles in my head. So you want to find the intersection both something that's desirable by users, something that is going to be a viable business and something that is going to be feasible from a research scientist and technical perspective. And then when you have that, it's just going to be a capacity product for desktop launch that you can run with. So yeah, whenever I say researcher, research scientist that can produce an AI machine learning model.

Lenny (11:15):
Wow. Didn't think about how every cross-functional team might end up with a research scientist. Interesting, interesting. For PMs who are curious about learning how to do this stuff, what are a couple things that PMs today who have no experience with AI, what can they do to start learning how to build AI tooling into their products, understand what the hell's happening in the space of AI?

Marily Nika (11:40):
This is a good question and I guess the message I want to pass is you shouldn't be overwhelmed by these technologies if you don't have a technical background because you can learn these things and as a PM you'll never need to actually train or code. Also, even if you want to train, there are no code approaches for training models. But to answer the question, if you're working on any product, you can always sprinkle in a smarter feature. So you can make it more secure, you can personalize it, you can enhance it with fraud detection, you can make it more ethical. If it's healthcare, you can make it faster, you can make it more accurate. If it's shopping, you can create better accommodations. Basically anything where you can get data behind the behavior with users can be improved with AI.

(12:30):
So I guess it's all about changing the mindset of PMs. Taking a step back and just thinking about, okay, I have all this data that's just lying and sitting around what is it that I can do with it? I've been meeting PMs that said, "Oh, we're not collecting any data, we're [inaudible 00:12:46] dashboard." So even that is a huge first step towards AI. And then just start thinking about it, where you could deal, get a data science intern and just see what they are going to do. There's just so much people can do.

Lenny (13:00):
So say you want to start investing in some sort of model, some sort of AI within your team, you're saying maybe hire data scientists who can help you start to build something that you can start integrating. Is that your advice on the first step of once you start, you want to start getting serious about building some sort of AI component.

Marily Nika (13:19):
There is something called the shiny object trap and I'm always telling people, "Hey, don't do AI for the sake of doing AI". Make sure there is a problem there. Make sure there is a pain point that needs to be solved in a smart way. Once you have identified what that problem is and what that very, very high level solution is, then reach out and try to figure out how to actually implement it. And there's a definition I like giving. I usually say that the generalist PM helps their team and their company build and ship the right product. But the AI PM helps their team or company solve the right problem. So if you want to get into AI PM figure out what the problem is that you will get a data scientist to create a model for solving, but there needs to be a problem, there needs to be audience, there needs to be a user and a pin going for it.

Lenny (14:11):
What are signs that AI may not be a good approach to solving a problem? You said that, and this happened on a lot of my teams, oh we're going to build a really cool model, it's going to do something really smart in this case and it often ended up being a very low ROI investment and took six months to a year before you even knew what the hell what was happening. Do you have any thoughts on signs that maybe this isn't a place you should be putting a lot of time into AI versus this is definitely an opportunity. Yes, we should do this, invest a lot of time into this.

Marily Nika (14:42):
Don't do it for your MVP. It makes zero sense. Do not waste time of data scientists that can train models with using powerful machines that are going take weeks to train. This is because if you have an MVP and you just want to get buy-in for an idea or feature that may use AI in the future, take it, create a little figma prototype and just show it some users, just fake what the AI is going to be doing. So a lot of young early stage entrepreneurs reach out to me and they say, "Oh, should train this model to do this and that because we want to prove that there is a market." "No, do not use AI. You should use AI where you think you already have some data or data from an adjacent product that you feel you can leverage for your own product to create something that's meaningful, recommendation automation, what we talking about. But not for an MVP. Please people, this is my advice.

Lenny (15:46):
How much data do you think you need for AI ML to have a chance to contribute? You have a heuristic of if you have anything less than this, it's not going to work at all.

Marily Nika (15:59):
This is a good question and it honestly depends on what I'm what I'm trying to do. If you're trying to classify, if the photo is a category dog, obviously even if you have, I don't know like 15, 20 labeled photos, what's going to work. But if you want to create voice recognizers or complicated NLP applications, you're going to need thousands of [inaudible 00:16:19] of data. And this what's making this not be easy? AI systems are not easy to develop. There is a life cycle of a machine learning project and after scoping you need to figure out, "Oh god, how much data do we need? Where do I find this data as well, how much data?" Sometimes I've seen people synthesizing their own fake data just so that they can have something to train with and test their models. But the exact amount is hard to be defined, especially from a [inaudible 00:16:50]. I'm sure data scientists have a different opinion.

Lenny (16:53):
Yeah, my guess is most startups are going to have nowhere near enough data to build their own model and make it something really interesting. So do you have a thought on when it makes sense to try to build your own model, try to train your own GPT type thing versus use something that's already out there like say GPT or aJourney or all those guys.

Marily Nika (17:17):
If you are a big tech company and you're offering a service that is going to do speech or permission or then it's going to have their own tragedy, you want to use more data and more diverse data to train and retain and train because if you don't then your quality is going to be the same as every other companies. There are agencies that are selling data, packages of data, that are ready so you can get them and train your models. But the question is if everyone takes that exact dataset, then the quality that every single company is producing is going to be the exact same. So you do want to diversify, you do want to collect your own data. And I guess a good question from my prem perspective is when is the quality of your product good enough to lunch?

(18:08):
And that is a really interesting point because it's totally your responsibility as a PM to decide, "Okay, the recognition of whether this folder is a category dog is good enough for the users, it's like 70% accurate, 80% accurate, where is the bar, where do we launch?" And that's why I'm like the AI PM role is so cool because you have problems like that to solve that no one else was tackled before. So it's all on you.

Lenny (18:34):
We've thrown out these words model and we talk about training models. Do you have a good succinct explanation for what a model is for folks that aren't that technical and then just the general idea of training a model. What is a simple way to think of, here is what a model is.

Marily Nika (18:52):
So I have a three-year-old girl and I'm teaching hear about life and everything. So I was recently teaching her about the animals and you explain things to her once or twice, what the mammals is or rhino and so on. But you will end up training your kids brain by repeating the same information again. So you will say, "Hey, here's what the rhino looks like, here's what an elephant looks like, here's what the rhino looks like, here's what an elephant looks like." And once you've done this enough times, then your kid will see an animal on the street and they'll be able to recognize and say, "Oh yeah, that's like rhino what we're talking about." This is exactly what a model is. The model is like a kid's brain. It has the ability to take an input, which means it has the ability to take an image and say, "Oh I recognize what this is. That looks like a rhino. But I'm 70% sure about this." So you will output the probability as well of the certainty.

Lenny (19:51):
And you said image, but it could be text for say in ChatGPT. In the future I imagine video there's also voice like whisper. That's an awesome explanation. Basically it's like trying to recreate the human brain is a nice way of thinking about it. And then training a model, can you talk about what that means?

Marily Nika (20:08):
The problems of training the model for example is providing a lot of images that are legal and say, "Hey, here's what card looks like, here's what it all looks like," and we're talking about thousands and thousands of data sets for this. And once you do this, there's a process where the model is just processing this information and it's learning, it's finding patterns through it and the patterns are not in the form of, oh if this is gray then this means this. No, it just learns in the smart brain how to identify specific things that we don't even understand. And then it's able to output the probability of whether photo is going to contain the cutter and top.

Lenny (20:49):
Just conceptually what is the output of the training? Is it code that is auto-generated with these decision trees and weights and things like that? Is it a database of weight? Just conceptually what is the output of a training that becomes a model? What's the simplest way to think about that?

Marily Nika (21:05):
So it's what it speaks. Speech is a great example. For example, I'm talking to a device which is like a home system and I say, "Hey, what is the weather like today?" This is going to take my folies and audio and it's going to process it and the output is going to be a transcription. So it's literally going to be text that corresponds to what I sent to it.

Lenny (21:24):
Thinking about the stuff you've worked on at Google, at Meta, anywhere else you've worked on, side projects even, what are some of the cooler applications of AI machine learning that you've worked on, contributed to, or even seen that you can talk about? I imagine there's a lot of sensitive stuff too going on.

Marily Nika (21:40):
One thing I want to talk about is the team I used to work for, Google, which was then the RVR team and they were working on an air glass and actually they had a video on last year's Google IO. They were able to have the Google glass on someone that spoke one language and then this other person was sat in front of them that spoke a different language and the glass will take as an input that audio that came from that other person and it will transcribe it, it will translate it and show it on the screen for that person in their language. So we're talking about the ability for this devices to unlock the borders of communication and that is not science fiction. This is what amazing and mind-blowing, there's no science fiction anymore. These things are real, the technology is here, it's just a matter of connecting the pieces to the puzzle in order to see them coming to life. So I think that one was one of the most impactful things I've ever seen.

Lenny (22:46):
I remember that demo and it was pretty incredible. Okay, so thinking a little more broadly, do you think ChatGPT or just say GPT four or GPT five, GPT six, do you think at some point this will replace product managers? Something I see on Twitter a lot. People are like, "Oh my god, product managements done. This thing made my product requirements document for me." Or you talked about how it makes your mission statement better. Do you think there's a place where PMs aren't necessary anymore?

Marily Nika (23:13):
Oh, absolutely not. As I said, it makes everything better. If anything it's going to free out time for me to do other things that are less tedious. For example, I am running so many projects and they only their peer [inaudible 00:23:27] and the peer [inaudible 00:23:28] have all these areas that are common across all of them. If I had a system that can actually write the continuous stuff for me so that I can focus on more strategic side of things, that would be incredible. It will make us smarter. If [inaudible 00:23:42], you will unlock new areas of product management that we haven't realized that, but are there.

Lenny (23:48):
Are there areas, do you think with your kind of vision of all PMs will be AI PMs, are there areas that you think PMs should invest more skill-wise or areas they should less focus on invest because say some machine learning model is going to do that for them.

Marily Nika (24:04):
I'd like to see people being less overwhelmed, less intimidated, less afraid to start learning how to code, how to train a little model on their own. This is because even if ChatGPT or this no code applications may be able to do this for us, it gives you a different approach, a different mindset, a different if you want confidence to know how things work. And here's a silly example, I was learning how to play the piano when I was young and when my teacher came in I was like, "Oh, I want to learn how to play this cool song." There were some songs that I really liked. And she said, "No, you need to start with a classical music," and I just hated it all the time. And I said, "Why do I have to do this?" Because she said, "If you learn the fundamentals and how you know where things started and the beginning of music, it's going to help you along the way to create music on your own if you want to." And she was right. I just loved it.

(25:00):
So it's the same with coding. I encourage people to just take an online course, understand more, get your hands dirty, pair up with someone else that's in the same boat as you because this is going to give you the skillset to understand how that tool that's going to help you in your day-to-day was even created in the first place instead of blindfoldedly distrusted to do your job.

Lenny (25:23):
This episode is brought to you by Pando, the always on employee performance platform. How much do you love the performance review process? Yeah, it's time consuming, subjective, bias and there's rarely any transparency. With the rapid shift to distributed work, it's a struggle to create the structure and transparency that you want to help your employees have the highest impact and growth in their careers. Pando is disrupting the old paradigm of performance management including a continuous employee-centric approach. So employees stay engaged, see their progression in real time and know exactly when and how they can level up. With Pando managers can leverage competency-based frameworks to effectively coach and develop their teams and align on consistent growth standards resulting in higher quality feedback and higher performing teams. Visit pando.com/lenny for more info and get a special discount when you sign up and reference this podcast. That's pando.com/lenny.

(26:21):
For someone that actually wants to do that and learn to code, which I love that advice, do you have any resources, places that you point people to for learning to code, getting started down that path?

Marily Nika (26:31):
It depends on what type of learner you are. There are some people that learn offline, so just go to Coursera, there are so many courses. There is an amazing one actually introduction to AI by Stanford that they're going to encourage people to take a look at. But I know that a lot of people don't like, don't have the time, don't have the discipline to actually take time off or after work, after they put their kids to sleep to just do it. So if you enjoy learning with others, if you enjoying being part of a team, if you enjoy going through a journey together, then I recommend these resources. So there is something called Career Foundry, which is a fantastic on coding school, General Assembly and then Coding Dojo.

(27:13):
I was actually give a talk, Ages of God Coding Dojo [inaudible 00:27:17] by Python, and all it takes is just a few weeks of your time and passion and just for you to roll up your sleeves and just realize that this is not intimidating and realize the benefits you can get by learning.

Lenny (27:31):
Awesome, thanks for sharing those. We'll include links in the show notes. Going back to a PM trying to become better in AI. If you think about a PM that's early in their career and wants to become a very strong AI PM. I know you have a whole course about this, which we can talk about now or later, whatever is easier, what should that PM be doing? We talked a bit about learn to code, maybe start playing with tools. What else do you suggest PMs that want to become really strong AI PMs do now and invest in?

Marily Nika (28:02):
So I do have a course that's coming up on February 6th on [inaudible 00:28:06], which is for current and aspiring product managers that want to build AI products. But I also have offline recordings. I have the same course on an offline basis on my website. I'd be happy to talk to you here, you already chat to me about this. What I feel people should understand is what it takes to manage an AI product. Of course people are very familiar with the stages of product development in general, but AI product development is different. As I mentioned before, sometimes you're actually managing the problem and not the product and you're trying to secure out if there is a problem that makes sense to be answered by a smart solution.

(28:45):
So it's a very interesting and more complicated process than regular product management. So number one, figure out how it differs from general product management. Number two, if you're already at the company that is actually having AR researchers and AI research scientists, I encourage people to just maybe talk to them and shadow them and spend an hour of their week just talking to them and experiencing what they're doing. This is going to open your mind, this is going to give you so much context as to what it is and the endless potential that you can identify there.

Lenny (29:22):
Awesome. And is there anything else you want to share from your course that you think might be interesting to folks?

Marily Nika (29:30):
So we talked about why it's awesome to be an AI PM, but I do want to call out that there are a few challenges that people need to be aware of. Number one, and I kind of mentioned it before, is the uncertainty. You may have been working on all of these incredible research and ideas in hypothesis, but then when you actually train the model, the results you may be getting may not be optimal, may not be answering the questions or the hypothesis that you actually had in mind. So that's number one. You need to be able to encourage the teams throughout this process because you're like the captain of the ship, you need to be the one that's cheerleading the team, making sure everyone keeps going.

(30:10):
Number two, you are going to have to [inaudible 00:30:15]. You are going to have to change the action in managing this from a leadership perspective can be tricky and it can be challenging.

(30:22):
Number three, we talked about data, but getting good data is hard. You may need to be creative, figure out ways for data collection that you never thought you'll do. You may get on the street and ask for people to actually contribute data for what it is you're doing. You need to be able to and willing to do everything. And the last thing is from a career trajectory, usually product managers get ahead the more they launch. But if you're in a research or if you're not going to launch as often, so you need to make sure to clarify with the hiring managers early on, "Hey, what does progress mean? How am I going to get a sense in a research work which is different than what I've been doing so far." So it's challenging but I always encourage people to flex different muscles and this is the zero to one muscle. The other thing is this crucial when it comes to product management.

Lenny (31:15):
This actually is a great segue to a question I definitely wanted to ask, which is around getting buy-in for investment at a company for ML. So there's sometimes all this energy for a zero to one, let's just try something, sometimes not, so maybe there's a two part question here. Do you have any advice on just getting buy-in for we want to try something with ML. It's going to take us six months to figure out if it's worth the effort, but we think there's something here. And then sometimes there's a lot of energy initially and then you get some win, like your search ranking's smarter and it's great.

(31:48):
But then maintaining that, having all these really expensive people working and just tweaking this model and continuing to make it smarter and a little more efficient, often it's hard to continue to get buy-in for that sort of team. Do you have any advice on initial buy-in, let's try something here, and then down the road just keeping a team going, trying to make this thing smarter and smarter.

Marily Nika (32:09):
People should know that there is an excellent source of inspiration and something that could kind of de-risk things, which is adjacent products. Maybe the company has already launched the product that has been successful, those AI firsts. And whenever I try to convince leadership about something that I want to do that's a big bet, I always use examples and I'm like, "Hey, this seemed crazy at the time, here's how they work. What I'm proposing is very similar to this crazy thing. And then I propose a little contingency plan, like hey, if that doesn't work out, here's the rollback plan, here's the maximum impact it will have done in a negative way, which is not going to be too much. And you kind of take it all on [inaudible 00:32:55].

(32:55):
And it's interesting because the more you work on this specific company, the more trust you get. And if the culture is such, then failing is going to be welcome. So a lot companies that welcome pain because you can just go ahead and do this sort of thing.

Lenny (33:09):
Do tell me if I'm wrong, but I feel like most investments in ML are not successes and often not great uses of time. I'm curious if that changes with more tooling and more public models that people can plug into without having to build their own. I wonder if it becomes like, "Oh okay look we're put in three weeks, we'll get something really useful."

Marily Nika (33:27):
Exactly. And also the other thing, and I wanted to add on the question you asked before about hey how do you keep updated about new niche tech? We shouldn't underestimate academia and research blogs and there's a website called Archive where you can see new papers come up, because this is where... ChatGPT and [inaudible 00:33:49] used to be there for a long time, there was a lot of information on this sort thing. But it's now recent where we see that research scientists and research orgs are not as siloed as they used to be. So the more companies invest on staffing, this layer between productionizing and research, academic research, the more PMs you're going to add there, then the more you're going to see this bridge creating goods, products, [inaudible 00:34:20]. So sometimes you have amazing ideas by research scientists but you need a PM to take it and actually figure out ways to also monetize it.

(34:28):
That's the other thing, if you're a PM you need to come up with ways to actually be able to monetize and ChatGPT is now free for everyone. But I don't know if you saw, there was a signup forum that was coming around saying, "Hey, would you pay for this? What would be the minimum you pay? What would the maximum you pay? What would you like to see if you paid?" So having PMs breached the tap is crucial for companies to be able to take the research and actually come up with meaningful use cases for users.

Lenny (34:56):
I think they actually started charging the other day. I think it's like $40, $42 a month to start using it. I think people have been talking about on Twitter, I don't know if that's live yet. And then you talked about research papers, when I think that, I always think of Tyler Cohen, he has this awesome blog marginal revolution and he is really good at sharing insights from research papers that he's reading. So that's another place for folks to check out. He's just this really smart dude. He's really excited about AI and GPT in general and so he shares a lot of really interesting insights about it all. Segueing a little bit to your course, I have a couple questions about it. One is can you just talk about the broad framework of your course? How long is it, what do you learn, what are the workshops broadly? And then I have a couple follow up questions.

Marily Nika (35:39):
My course is three week long. It's meant for people that are either aspiring or current PMs that want to understand how to sprinkle in AI solutions or they wanted a full-time AI course. Week one is more about introduction, what the product development lifecycle is for regular products and how it differs for AIPN specifically. And then we talk about idea creation. How on earth do you come up with ideas? And I love what Steve Job said where he used to say, "Well, users don't know what they want until you show it to them." And that's exactly the mindset I want to invite two people and say, "Hey, people don't know how on earth you use AI." People will never have imagined ChatGPT can be what it is.

(36:26):
And then we take that and we dive deep and we talk about how on the earth do you productionize something like this? What are the different partners you're working with? What is a research scientist and how on the earth do you collaborate and how do you partner with them? How do you convince them what you have in mind for their precious research to be converted into a product? How on earth do you convince them to trust you and how do you influence them? And then at the end we're talking about how you actually will be able to pave your pathway PM all the way from interviewing for this role, from what resumes look like, and doing some mock interviews because the more you practice the better it is.

Lenny (37:03):
How many workshops are there through the course?

Marily Nika (37:05):
Nine workshops.

Lenny (37:06):
Nine workshops. Of the nine workshops, which of them are you finding is the most exciting, game-changing for someone, most interesting?

Marily Nika (37:15):
So throughout the duration of all these workshops, people have homework and they actually take home an exercise where they need to create and develop their own AI product end to end, and they can pair up with each other. By the way, there was this two students pair up and actually where I would raise funding, which is mind blowing to me, which is really great.

Lenny (37:15):
That's awesome.

Marily Nika (37:35):
But to continue, the most exciting part is when everyone at the great end are actually presenting their work and they're actually asking questions and getting feedback and they're just really excited and proud for what they created.

Lenny (37:48):
That's a good reminder of a lot of the learning that you do is just doing it, not just reading about it and following Twitter. Can you share any examples of stuff people built after the course?

Marily Nika (37:57):
Someone was able to actually, and I kid you not, create a little model that was able to take us an input x-rays that they found online and was able to tell us what was wrong if something was wrong with that patient. And it's just crazy to think that you can do that within three weeks. Obviously it was just by photos we were able to crawl online for x-rays. But the concept is there that you can build something like that, you can create it. And to take it a bit further, they wanted to create a lower recommender system and say, "Hey, we think this is what's wrong with you, here are the steps you should follow." Obviously we're not trying to play doctors or to pretend that or medical in any way, but being able to see that actually functioning is just, it's very impactful.

Lenny (38:48):
That's amazing. Do they already know how to code, do this team that built this thing?

Marily Nika (38:51):
They did not, but part of the course is to teach people the basics that you are going to need, prove it PM lens. And there are some no click tools as I mentioned that are going to allow you to drive and drop and train these models and input photos in it and be able to do it.

Lenny (39:07):
Can you mention those tools again because that is really interesting and it's just like a peek at your course, but if someone wanted to start building something like this, what are some of these tools they could check out?

Marily Nika (39:16):
One of the tools I would like to recommend to people is actually Auto ML. This is offered by World of Cloud and essentially it allows you to train high quality custom machine learning models, which minimal effort, you don't need to be able to code anything like that. You need to have a lot of photos and images that you have already corrected but it's not going to do the collection for you. And a great application I had to seen, there is actually a YouTube video about this. There was this company that actually had a lot of winter banks and what they did is in order to maintain these, they will actually have people manually have huge ladders and go take a look and see if everything was okay. So eventually they just [inaudible 00:39:59] drones and they had these drones fly on all of these machines and take photos of everything. And then they downloaded all these photos and they uploaded on Auto ML and they were able to see which ones needed maintenance and which did not.

(40:12):
And I think they reduced time from three weeks of work to a few hours of knowing which needed maintenance and just be able to send people there. So it's this type of thing that you can do on your own by applying this sort of tools.

Lenny (40:25):
Saying that tool is called Auto ML?

Marily Nika (40:28):
Yes, Auto ML.

Lenny (40:28):
Amazing. We'll link to that in the show notes. Coming back to your course and maybe just a couple more questions. Can you just talk about what it takes to build a course like the course you built, how much time did it take you? How much work did it take? Anything that you want to share.

Marily Nika (40:43):
It treated creating like course like a product. This is what I did is, I came up with some hypothesis as to who the audience was and as to what they were looking to get out of it. And I started reaching out to people and I started saying, "Hey, first of all, would you like to learn from me? Second of all, what would you like to learn? What are the specific questions that you would need answered?" Because these are people that are working, people [inaudible 00:41:09] that have families. In order to take a break from all that you need to provide something to them that is meaningful. And there were quite a few activations. In the beginning I was focusing the course more for software engineers that wanted to become AI product managers. But then I realized, no, there are a lot of PMs that want to become AI product managers.

(41:31):
So I did a little online shift there. So what it takes is make sure you find the right audience, make sure to figure out what that audience wants, make sure to have the right duration. One week I find it too short. Two weeks, it'll still be rushed. Three weeks is excellent because you give the opportunity to everyone to present and to keep to know each other on an offline discord community, which is another important part. And then the last thing, you need to have a personal relationship with everyone. So I've messaged everyone, I've seen everyone's application. I met with some people as well just to make sure to answer any questions and concerns because I wanted to make sure that people were comfortable just trusting a stranger like me and paying them to provide knowledge for their course. So it took quite a few iterations, but I was able to get there and now I'm very, very happy about it and I recorded it offline as well for people.

Lenny (42:27):
Has anything had to change in this course? Maybe it's just as the last question, things are moving so fast. Is there anything you've had to rethink, redo since you first built it?

Marily Nika (42:35):
I actually added bonus sections and one bonus section was [inaudible 00:42:38] and how it was trained. This is because I started this new cohort in December and on day one the question I got is, what is this? How did it start? What is going on? How did they train it? So I added the dedicated section for it and I point people to it.

Lenny (42:52):
Amazing. Anything else that you'd like to share before we get to our very exciting lightning round?

Marily Nika (42:58):
It was someone that recommended, I actually did a course and in the beginning I laughed and I said, "Wait, people would want to learn from me. Really?" And of course they did. And I'm teaching so many people. So what I want to tell people is don't underestimate this. Try creating your own courses as well. People may want to learn what you take for granted. For them it may be game changing, it can be life changing. So building courses is an amazing thing and we're living in the full [inaudible 00:43:30]. So the course is content, so go try this.

Lenny (43:33):
I find that teaching and at least crystallizing thoughts is one of the best ways to learn it yourself. I imagine you learned a lot about AI much more than even came into it with just putting it together into a course.

Marily Nika (43:44):
Absolutely. And I got some uncomfortable questions that I had no idea how to tackle. People on day one were like, how do I assess the tradeoffs between these two different months? And I had to figure out how to answer these things and how to incorporate them in my course. So learning from the students, learning from the course, learning from explaining is just so viable. So skills that we can get.

Lenny (44:07):
Well with that, we've reached our very, very exciting lightning round. I've got five questions for you. I'm going to go through them pretty quick. Whatever comes to mind, share. We'll see how it all goes. Sound good?

Marily Nika (44:18):
Sounds good.

Lenny (44:19):
Two or three books that you recommend most to other people.

Marily Nika (44:22):
Inspired. It's all about how to create tech products people love.

Lenny (44:28):
Marty Kagan, right?

Marily Nika (44:29):
Yes, that's the one. Great.

Lenny (44:34):
Cool. Anything else? Or that's the one that comes to mind.

Marily Nika (44:35):
You Look Like a Thing and I Love You and I have it right here. It's a great thing, super, super cool. It's about how AI works and why it's making the world a weirder place. It's actually a very fun book. And there's one more, which is a book, a workbook I originally launched with Alana Karen and it's a workbook for women in tech trying to navigate working in tech. It's called Adventures of Women in Tech Workbook. So that's another thing that they want to shamelessly plug in.

Lenny (45:02):
Ah, that's a great choice to plug. Where can folks find that? Is that on Amazon?

Marily Nika (45:06):
Yeah, Amazon.

Lenny (45:07):
Amazing. What's a favorite other podcast that you like to listen to?

Marily Nika (45:11):
I like Boz's podcast. I don't know if you're aware of it. Boz is the CEO of Facebook. He has a great podcast.

Lenny (45:19):
I have not heard it. I do know of Boz. I'll check that out. I didn't know he had a podcast. He had some great writing over the years. Maybe that's why he doesn't write it anymore. He has his podcast. What is a favorite recent movie or TV show that you've loved?

Marily Nika (45:30):
Oh my God, The White Lotus. People were talking about this thing. I ended up just trying it out and me and my husband, we just binge watched the whole thing. Is just so different, so mind blowing, get you excited about going to Hawaii again. It's just really good.

Lenny (45:45):
Have you seen the second season?

Marily Nika (45:46):
I've seen it and it's so much better than the first, which is rare.

Lenny (45:50):
I agree. Awesome. Love that show. What is a favorite interview question you like to ask, and bonus point if it's AI related.

Marily Nika (45:57):
I love to ask people, how would you explain a database to a three year old? And I know it's kind of an AI, not everyone say ai, but I love asking it because people are thinking the [inaudible 00:46:11], like what did you just ask me? But it's so important to be able to explain things in a simple ring and have the storytelling to convince a kid and really explain technical terms to non-technical people.

Lenny (46:23):
Favorite AI based tool that you think people should check out.

Marily Nika (46:27):
Talk about ChatGPT, now I have this on ChatGPT, this is what comes to mind. Well, the Lensa app was pretty cool too, right? We all plugged in our [inaudible 00:46:36] and we're able to see what they would look like as fantastic heroes. I have to say, I tried being the mail version because it was so much cooler than the KingL version, so that's when I recommend to people, try the mail version.

Lenny (46:48):
That's fun. And they actually have pets now. That's what got me the download and pay for it. You can take pictures of your pets and they look so fun. That's like a killer feature right there. Good job Lensa. And the app is Lensa, right?

Marily Nika (47:01):
Yeah. [inaudible 00:47:02]

Lenny (47:02):
Amazing. Marily, thank you so much for spending time with me, sharing your wisdom. Two final questions, where can folks find you online if they want to learn more and reach out and how can listeners be useful to you?

Marily Nika (47:12):
Thank you so much. People can find me on Instagram. I also have a product channel on YouTube that you can check out. I just started it. I'm getting used to the whole process. I'm also kicking off a newsletter, just any social reach out and you'll see all my links.

Lenny (47:28):
How do they find the YouTube channel? How do they find the newsletter?

Marily Nika (47:31):
Typing Marily Nika.

Lenny (47:32):
Marily, thank you again for being here.

Marily Nika (47:34):
Thank you so much, Lenny. It was a pleasure.

Lenny (47:38):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

