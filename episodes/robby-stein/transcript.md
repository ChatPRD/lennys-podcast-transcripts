---
guest: Robby Stein
title: 'Inside Google''s AI turnaround: AI Mode, AI Overviews, and vision for AI-powered
  search | Robby Stein'
youtube_url: https://www.youtube.com/watch?v=kOnsqqVbIeY
video_id: kOnsqqVbIeY
description: 'Robby Stein is VP of Product at Google, where he oversees the core products
  of Google Search—including the new AI Overviews, AI Mode, search ranking, Google
  Lens, and more. Previously, he...

  '
duration_seconds: 4898.0
duration: '1:21:38'
view_count: 27015
channel: Lenny's Podcast
keywords:
- growth
- retention
- metrics
- kpis
- roadmap
- hiring
- leadership
- management
- strategy
- vision
- mission
- positioning
- market
- jobs to be done
- design
---

# Inside Google's AI turnaround: AI Mode, AI Overviews, and vision for AI-powered search | Robby Stein

## Transcript

Lenny Rachitsky (00:00:00):
It feels like something has changed internally at Google. Just last week, Google Gemini hit the number one app in the App Store. I feel like nobody saw this coming.

Robby Stein (00:00:08):
Google's mission around have any information be universally accessible, this very enduring, very motivating thing, and it feels like with the AI moment, we can actually achieve that more than ever before. What I'm feeling now is just an incredible sense of focus and urgency. Things have hit a tipping point where these models are now truly able to deliver for consumers.

Lenny Rachitsky (00:00:26):
As ChatGPT emerged over the past couple of years, as Perplexity emerged, a lot of people were just like, "Google is dead. Nobody wants to sit through search results and click links."

Robby Stein (00:00:35):
The core Google search isn't really changing, in my opinion. We're not seeing that people come to search for just ridiculously wide set of things. They want a specific phone number, they want a price for something, they want to get directions. I think the vastness of that is underappreciated by many people. AI is expansionary. There's actually just more and more questions being asked and curiosity that can be fulfilled now with AI.

Lenny Rachitsky (00:00:54):
You've built a lot of very successful products. You used this phrase: embodying relentless improvement.

Robby Stein (00:00:59):
You need to be the physical manifestation of two pieces of things. One is just relentlessness, just complete effort that is always exerted in a direction of positive productivity. And then the second is make things better. You have to always make things better. You're never content.

Lenny Rachitsky (00:01:12):
You build and launch Stories at Instagram back in the day is quite controversial because it basically took what Snapchat was doing really well and then like, "Hey, let's bring it to Instagram."

Robby Stein (00:01:21):
Not every great thing is going to be invented by you. Facebook probably created the modern feed, but there's a feed for every single product. At the end of the day, you're just robbing your user base of the opportunity to have a better product.

Lenny Rachitsky (00:01:33):
Today my guest is Robby Stein, Robby's VP of Product for Google Search and is responsible for essentially the entire Google search experience, including the new AI Overviews, AI Mode, multimodal AI experiences like Google Lens, the ranking algorithm, and a lot more. He's at the forefront of one of the biggest shifts in Google's history, and has already made a massive dent in Google's trajectory. He's also made a massive dent in the trajectory of Instagram where he was head of product, and led the launch of Instagram Stories and Reels and Close Friends, and through that, grew Instagram to half a billion daily active users. He's also on the founding team of Artifact with Mike Krieger and Kevin Systrom. Started two companies of his own. Very few people have had this level of impact on two global consumer products at this scale. And Robby shares all of the biggest lessons that he's learned about building great and successful consumer products, along with a bunch of insights into where Google is headed in the world of AI.

(00:02:28):
A huge thank you to Bart Stein for suggesting topics for this conversation. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube, it helps tremendously. And, if you become an annual subscriber of my newsletter, you get a year free of 15 incredible products including Lovable, Replit, Bolt, n8n, Linear, Superhuman, Descript, Whispr Flow, Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, and Mobbin. Head on over to lennysnewsletter.com and click Product Pass. With that, I bring you Robby Stein.

(00:03:00):
My podcast guests and I love talking about craft and taste and agency and product market fit. You know what we don't love talking about? SOC 2. That's where Vanta comes in. Vanta helps companies of all sizes get compliant fast and stay that way with industry-leading AI automation and continuous monitoring. Whether you're a startup tackling your first SOC 2 or ISO 27001, or an enterprise managing vendor risk, Vanta's trust management platform makes it quicker, easier, and more scalable. Vanta also helps you complete security questionnaires up to five times faster so that you can win bigger deals sooner. The result? According to a recent IDC study, Vanta customers slashed over $500,000 a year and are three times more productive. Establishing trust isn't optional. Vanta makes it automatic. Get $1,000 off at vanta.com/lenny.

(00:03:54):
This episode is brought to you by Jira Product Discovery. The hardest part of building products isn't actually building products, it's everything else. It's proving that the work matters, managing stakeholders, trying to plan ahead. Most teams spend more time reacting than learning, chasing updates, justifying roadmaps, and constantly unblocking work to keep things moving. Jira Product Discovery puts you back in control. With Jira Product Discovery, you can capture insights and prioritize high-impact ideas. It's flexible, so it adapts to the way your team works and helps you build a roadmap that drives alignment, not questions. And because it's built on Jira, you can track ideas from strategy to delivery all in one place. Less chasing, more time to think, learn and build the right thing. Get Jira Product Discovery for free at atlassian.com/lenny. That's atlassian.com/lenny.

(00:04:49):
Robby, thank you so much for being here, and welcome to the podcast.

Robby Stein (00:04:53):
Thanks so much for having me.

Lenny Rachitsky (00:04:54):
This is such a cool week to be recording this podcast. So just last week, Gemini, Google Gemini hit the number one app in the App Store. I have it right here, it's still number one in the App Store. It's above ChatGPT. I feel like nobody saw this coming. I feel like everyone's always like, "Google, what have you guys been doing? You guys build all this amazing tech and why didn't you have anything working in consumer? Why is ChatGPT doing? Why are all these amazing companies doing better than Google?"

(00:05:20):
So first of all, let me just say congrats on, I know this isn't all you. I imagine you had some part in this, so just congrats.

Robby Stein (00:05:26):
Many, many more people, yes.

Lenny Rachitsky (00:05:28):
It feels like something has changed internally at Google. It feels like things are starting to really work, especially on the AI consumer side. So in terms of the growth, is Nano Banana the source of a lot of this recent growth or is there something else?

Robby Stein (00:05:40):
People are really excited about Nano Banana to be clear, very much so, but I think also people are recognizing that there's just so many cool things that you can do across the Google set of products and they've become quite powerful. I'm always shocked, even for things in search, people, we think they're very obvious. They sit right in the core search experience and then on X, I'll go look and like, "Oh, I just found out about this AI thing," and it seems very obvious, but I think a lot of people are just discovering quite how powerful these tools are.

Lenny Rachitsky (00:06:07):
Now. So to go one level deeper, to your point, there's been all this incredible tech. You guys wrote the original transformers paper that have powered so much of the innovation and it's just like, "Where's Google been? And actually, why aren't they building the thing that's winning?"

(00:06:20):
What has changed? Is it just like, okay, has there been major reorgs? Has there been new leaders put in place? Is there just a new philosophy in the past couple of years that have led to this moment where Gemini is now the top app in the world?

Robby Stein (00:06:32):
Yeah, I mean, look, I've been to Google now, this is my second time at Google, so I started at Google in 2007, done a bunch of things in between, and I've been back at Google now, so I can't speak to that whole period for many, many years back to today. But what I can tell you about what I'm feeling now is just an incredible sense of focus and urgency to deliver great products quickly. I think that that is in part leadership for sure. I think the people who are, we work very closely with our partners at DeepMind and Google DeepMind. We work very closely obviously across the organization and there's just an incredible group of people and also an incredible group of researchers and technical thinkers who've been thinking about this for a while. When you have that energy, and I think the product teams and the tech, the research groups are working really closely together, we're able to move and we're getting a lot done.

(00:07:19):
I don't think there's any one thing that has happened. I think that a lot of times people ascribe a lot of momentum to a one time change or a single person. I find a lot of this is actually this compounding effect when you think about just every month ruthlessly improving the product or the models and just every day getting better, and then it just hits this tipping point where people just like it, they use it more, they enjoy it. And that's more of the feeling that I've had is just we've had, I think the right investment and focus and then it just hit a moment where people are seeing the effects of that now.

Lenny Rachitsky (00:07:52):
As ChatGPT emerged over the past couple of years, as Perplexity emerged and all these other chatbots, a lot of people were just like, "Google is dead. Nobody wants to sit through search results and click links. Why not just get your answer right there?"

(00:08:06):
And it feels like that's not at all happening. It feels like you guys are doing just fine. What can you share about just the, I don't know, the state of Google search specifically, and then we'll talk about AI Mode. Just how is traffic going, how is search going considering all these things are out there, and just what are you seeing in the data since the launch of say ChatGPT?

Robby Stein (00:08:24):
Yeah. Well, what's interesting is people come to search for just ridiculously wide set of things, like all kinds of things. They want specific phone number, they want a price for something, they want to get directions, they want to find a payment web page for their taxes. Every possible thing you can imagine. I think the vastness of that is underappreciated by many people. And what we see is that it's not changing. AI hasn't really changed those foundational needs in many ways, and what we're finding is that AI is expansionary, and so there's actually just more and more questions being asked and curiosity that can be fulfilled now with AI. And so that's where you get the growth.

(00:09:00):
All the core Google search isn't really changing, in my opinion. We're not seeing that, but you're getting this expansion moment. What we're seeing is a few examples is you can now take a picture of something and ask about anything you see. And Google Lens, one of the fastest growing products out there, it's growing 70% year-over-year increase in visual searches, which is already at a massive scale. It's billions and billions and billions of searching in that way.

(00:09:24):
But you can take a picture of your shoes, say, "Where can I buy this?"

(00:09:27):
Or take a picture of your homework, say, "I'm stuck on question two."

(00:09:29):
And then just take a picture of your bookshelf and say, "What are the books I should get based on these books?" And AI can help you with those things now, just an example of I think why there's so much growth left and why we're so excited.

Lenny Rachitsky (00:09:41):
Okay, so you're not seeing the death of search.

Robby Stein (00:09:45):
No.

Lenny Rachitsky (00:09:45):
And along the same lines, you guys recently launched AI Mode, which I don't think enough people are talking about. I think you get there at google.com/ai, is that the right URL?

Robby Stein (00:09:53):
Yep.

Lenny Rachitsky (00:09:54):
Okay, cool. I've been playing with it as we were prepping for this conversation. It's really incredible. I asked it what is the best newsletter on product and growth and it's very smart. Said Lenny's Newsletter. So that's my eval.

Robby Stein (00:10:06):
Fantastic. Okay, one of one, perfect eval.

Lenny Rachitsky (00:10:10):
It's perfect. Also, just if you go to it, there's these recommendations for things to ask it that are just like, "Wait, how did you know I care about this stuff?" So it's like, "Help me switch to product management," just on the front page.

(00:10:21):
I'm like, "How did you know?" And it tells you that it's based on your Google activity. Talk about just what people should know about AI Mode, maybe what they don't really understand about the power of this thing.

Robby Stein (00:10:31):
I can tell you there's three big components to how we can think about AI search and the next generation of search experiences. One is obviously AI Overviews, which are the quick and fast AI you get at the top of the page many people have seen, and that's obviously been something growing very, very quickly. This is when you ask a natural question, you just put it into Google, you get this AI now, it's really helpful for people.

(00:10:51):
The second is around multimodal. This is visual search and lens. That's the other big piece. You go to the camera in the Google app and that's seeing a bunch of growth. And then really with AI Mode, it really brings it all together. It creates an end-to-end frontier search experience on state-of-the-art models to really truly let you ask anything of Google search. You can go back and forth, you can have a conversation and it taps into and is specially designed for search. What does that mean?

(00:11:16):
And one of the cool things that I think it does is it's able to understand all of this incredibly rich information that's within Google. There's 50 billion products in the Google shopping graph, for instance. They're updated 2 billion times an hour by merchants with live prices. You have 250 million places in maps. You have all of the finance information, and not to mention, you have the entire context of the web and how to connect to it so that you can get context but then go deeper. You put all of that into this brain that is effectively this way to talk to Google and get at this knowledge. And that's really what you can do now.

(00:11:52):
You can ask anything on your mind and it'll use all of this information to hopefully give you super high quality and informed information as best as we can, and you can use it directly at this google.com/ai. But it's also been integrated into our core experiences too. We announced you can get to it really easily if you can ask follow-up questions of AI Overviews right into AI Mode now. Same for the lens stuff. Take a picture takes you to AI Modes, you can have this back, you can ask follow-up questions and go there too. So it's increasingly integrated experience into the core part of the product.

Lenny Rachitsky (00:12:24):
I imagine much of this is wait and see how people use it, but what's the vision of how all these things connect? Is the idea continue having this AI Mode on the side, AI Overviews at the top and then this multimodal experience, or is there a vision of somehow pushing these together even more over time?

Robby Stein (00:12:40):
I think there's an opportunity for these to come closer together. I think that's what AI Mode represents, at least for the core AI experiences, but I think of them is very complimentary to the core search product. You should be able to not have to think about where you're asking a question ultimately, you just go to Google. Today, if you put in whatever you want, we're actually starting to use much of the power behind AI Mode right in AI Overviews. So you can just ask really hard, you could put a five sentence question right into Google search. You can try it and then it should trigger AI at the top. It's a preview, and then you can go deeper into AI Mode and have this back and forth. So that's how these things connect.

(00:13:15):
Same for your camera. So if you take a picture of something, "What's this plant?" Or, "How do I buy these shoes?" It should take you to an AI little preview. And then if you go deeper, again, it's powered by AI Mode. You can have that back and forth, so you shouldn't have to think about that. It should feel like a consistent simple product experience ultimately, but obviously this is a new thing for us, and so we wanted to start it in a way that people could use and give us feedback with something like a direct entry point like google.com/ai.

Lenny Rachitsky (00:13:41):
I recently had Brian Balfour on the podcast and he showed this quote that's really stuck with me that I think about as you talk about all this, it was by Alex Rampell, this idea that startups is a game of getting distribution before incumbents can innovate fast enough.

(00:13:55):
And it feels like you guys are finally there where it's like, "Oh man, now here comes Google." I don't know if I have a question here, but it just feels like there's been all this time for people to find distribution, and now it's like, okay, now Google is coming.

Robby Stein (00:14:07):
What we found is that people are asking these questions in Google. They're trying to get this out of Google. And so if you can just have an AI that's powerful enough to answer a really hard calculation someone's trying to figure out, or take a picture of multiple choice homework question for a chemistry question, people are doing this. And so now that you have this really sophisticated AI that's based on our frontier models, we can just handle increasingly more and more stuff for people and so hopefully that's the more natural on ramp here. And then we just need to make it easy enough for people to use, because these are new products, and people are used to using Google in a specific way.

(00:14:38):
They type in keywords, we call it sometimes keyword ease, but you can actually use natural language in Google. That's the biggest shift. We're seeing people asking real long, hard, complex questions. You just don't think, "Oh, I can go to Google and type in what's a great place for a date night? I already went to these four restaurants. I'm looking for outdoor dining and my friend has this allergy." You could put that into Google. And I think that's the kind of thing that we're excited to continue to make easy for people.

Lenny Rachitsky (00:15:03):
It's interesting, and we've come around to back in the day there was Ask Jeeves, which was this whole just ask a question as if you're asking a human and then it'll give you a really good answer.

(00:15:12):
And then we moved into Google just, "No, no, just type the thing you want and figure out how Google likes it."

(00:15:17):
And now we're back to, "Okay, just ask your question and it'll give you a really good answer."

Robby Stein (00:15:20):
Yeah, Ask Jeeves was surprisingly prescient on that, huh? They had material, they had something way before its time that we think looks to rally around now.

Lenny Rachitsky (00:15:29):
Oh, man. What's your take on this whole rise of AEO, GEO, which is this evolution of SEO? I'm guessing your answer is going to be just create awesome stuff and don't worry about it, but there's a whole skill of getting to show up in these answers. Thoughts on what people should be thinking about here?

Robby Stein (00:15:47):
Sure. I mean, I can give you a little bit of under the hood how this stuff works because I do think that helps people understand what to do, but when our AI constructs a response, it's actually trying to, it does something called query fan-out where the model uses Google search as a tool to find to do other querying. Maybe you're asking about specific shoes, it'll add up and append all of these other queries like maybe dozens of queries and start searching basically in the background. And it'll make requests to our data back end, so if it needs real time information, it'll go do that. And so at the end of the day, actually something searching, it's not a person, but there's searches happening and then each search is paired with content. And so if for a given search your web page is designed to be extremely helpful and you can look up Google's human rater guidelines and read, it's a very long document that's been thoughtfully crafted for decades now around what makes great information.

(00:16:40):
This is something Google has studied more than anyone, and it's like, do you satisfy the user intent, what they're trying to get? Do you have sources? Do you cite your information? Is it original or is it repeating things that have been repeated 500 times? And there's these best practices that I think still do largely apply because it's going to ultimately come down to an AI is doing research and finding information. And a lot of the core signals, is this a good piece of information for the question? They're still valid, they're still extremely valid and extremely useful, and that will produce a response where you're more likely to show up in those experiences now.

(00:17:14):
I think the only thing I would give advice to would be think about what people are using AI for. I mentioned this as an expansionary moment. It seems to be that people are asking a lot more questions now, particularly around things like advice, or how to, or more complex needs versus maybe more simple things. And so if I were a creator, I would be thinking, what kind of content is someone using AI for? And then how could my content be the best for that given set of needs now? And I think that's a really tangible way of thinking about it.

Lenny Rachitsky (00:17:45):
It's interesting your point about how it goes in searches. When you use it, it's searching a thousand pages or something like that. Is that just a different core mechanic to how other popular chatbots work because the others don't go search a bunch of websites as you're asking?

Robby Stein (00:18:00):
Yeah. This is something that we've done uniquely for our AI. It obviously has the ability to use parametric memory and thinking and reasoning and all the things a model does, but one of the things that makes it unique for designing it specifically for informational tasks, we wanted to be the best at informational needs, that's what's Google's all about, and so how does it find information? How does it know if information is right? How does it check its work? These are all things that we built into the model, and so there is a unique access to Google. Obviously, it's part of Google search, so it's Google search signals everything from spam, what's content that could be spam? And we don't want to probably use in a response all the way to, wow, this is the most authoritative helpful piece of information. We're going to link to it and we're going to explain, hey, according to this website, check out that information and then you're going to go probably go see that yourself. That's how we've thought about designing this.

Lenny Rachitsky (00:18:51):
You've worked on a lot of AI products at this point, and it's not just Google or Artifact and Instagram, you did a lot of AI stuff. What's something you've learned about building AI products that you find maybe people don't truly understand, maybe something that's surprised you by building successful AI products?

Robby Stein (00:19:07):
I think the most recent one, and this is true, something even within the last week or two, is that it's so obvious how human-like the interface is becoming with how you can communicate and steer AI. I think it used to be even just months back that you had to do a lot of work to get the AI to do the thing you're trying to get it to do, right? You had to do these incantations, you had to prompt in a really specific way. People would have all these hacks like, "Hey, act like you're a coach and you do these things," and you have to really push it, or to use a tool more on the technical side. You had to do post-training, you had to take this foundational model and you had to show it data, you had to train it and actually update its weights to do more sophisticated things.

(00:19:51):
Tell it, "Hey, here's documentation for an API. If you ever have a problem, ping this API. Here's the data," as if it's an engineer that you had that you could talk to and it would have no idea what to do with that, or it would have some idea and wouldn't really do it.

(00:20:05):
But increasingly, you can just use language. Almost if you were to write up an order, you could be like, "Wow, I'm a new startup. Here's my data internally. Here are the APIs to it. Here's the schema and the URL. Here's when to use it. By the way, make sure that if you get this kind of a question, you really make sure to get it right." And that'll end up doing a lot in the model.

(00:20:28):
The model's been now encoded to be able to say, "Okay, I'm going to use more reasoning or thinking budget for that kind of a question."

(00:20:35):
Or, "I'm going to use tools or code, use code execution in order to connect to this API I'm told about." That's a relatively new thing. So I think it's going to open up a lot of this democratization of accessing these models and building incredible things because you don't even need to do a lot. To get the most sophisticated outcomes increasingly, I don't think you need to do a lot of this heavy duty fine-tuning.

Lenny Rachitsky (00:20:58):
It makes me think about, I had this recent guest, Nesrine Changuel, on the podcast. She was a PM at Google, she worked on Google Meet, she was a delight PM working on at making products more delightful. And she talked about the reason Google Meet did so well and is now feels like it's killing Zoom is they compared the experience of Google meet to a human meeting versus making it the best possible video conference, make this as good as a human experience. And that's interesting what you're talking about, how that's almost the goal here with AI is just make you feel like you're just talking to a person.

Robby Stein (00:21:27):
Exactly.

Lenny Rachitsky (00:21:28):
Might be obvious, but think about that. Okay, let me zoom out and talk about, and let's talk about just broader lessons you've learned over the course of your career. You've built a lot of very successful products, which I've shared in the intro at this point.

Robby Stein (00:21:44):
Many also on the other side of the spectrum, we got the whole portfolio.

Lenny Rachitsky (00:21:48):
Okay, perfect. We'll talk about some of that. I asked you as we were getting ready for this conversation, what's one thing you wanted to get across in this conversation? What's something you think would be really helpful for product builders to hear to help them build more successful products? And you used this phrase: embodying relentless improvement. Can you just talk about that? What does that mean? Why is this so important?

Robby Stein (00:22:08):
Of course, I mean, I think that you need to be the physical manifestation of two pieces of things. One is just relentlessness, just complete effort, but is always exerted in a direction of positive productivity. And then the second is make things better. You have to always make things better, you're never content. And I think this actually came out of a story, a little bit of a funny story where I was at Instagram at the time doing a big all team meeting, one of my first, and they had this icebreaker, what's one word to describe yourself?

(00:22:35):
And so in the backstage area, I texted my wife really quick. I was like, "Hey, just one word to describe me, first thing that comes to your mind."

(00:22:42):
And she just wrote back, "Dissatisfied."

(00:22:45):
I was chuckling in the back room because I was first of all kind of offended because I was like, "It's not loving, caring, something good?" And then I saw her little bubble thing.

(00:22:56):
She's like, "Okay, there's more." And then she wrote me this really thoughtful thing that was like, "It's not that you're just unhappy. It's like you want the world to be better. You're driven out of a deep desire. It's that you feel this sense of dissatisfaction with what the world gives you. You want to make it better, and you're pushed and motivated to do that."

(00:23:17):
And I thought about that after. And it wasn't until we built a bunch of products, some that didn't do well, some that have had a lot of really large success now, billions of people use them, where it felt like one of the big differences, obviously a lot of it is just the conditions of the product and a little bit of luck here and there too. But for the things that went well, there was always this spirit of just we're going to get it eventually if we just make two more moves to make it better. And then eventually, as I talked about before earlier in our conversation, you get this tipping point where it just tips over into being net useful to people because of just that amount of compounding effort that you put into something because you're just always so... You're the harshest critic and the most dissatisfied person in the room about your own work basically.

(00:23:56):
And I think that's really meaningful. And there's this other incredible story that Tony Fadell told on a TED Talk 10 years ago. You can look it up. I think it's something around Think Younger as a title. And he talks about what it means that as we grow up in age and become grownups, I have two little kids so that's something I think about a lot. We habituate to everything. We accept and we tolerate what the world gives us everywhere, and we just go, "Oh, that kind of sucks. Oh, well," we shrug our shoulders and we move on.

(00:24:27):
But if you don't do that and you ask, "Why? This sucks, why am I tolerating this and how do I make it better?" He has this incredible story about going grocery shopping, and he goes on for 10 minutes about this story almost it felt like where he talks about getting a piece of fruit like a plum or a peach, and how it has that sticker on it and it's got that sticker and who put that sticker there?

(00:24:51):
And then when you get home, you take your fruit out of your bag, you're ready to eat it, you're all excited, you stick your thumb under the sticker, it punctures the flesh. He goes into just incredible detail about how it punctures the flesh of the fruit. The sticker comes off now, the fruit's bleeding, then you flick the sticker. The sticker misses the garbage, you bend over and pick it up, you put the sticker back in.

(00:25:17):
And I was like, "Wow, that is embodying this mentality of just why is this here? How can this be better?" And I think the best product people, the best thinkers in the space, that's how they think, in my opinion.

Lenny Rachitsky (00:25:32):
I imagine there are many examples of you doing this in the many products you worked on. Is there one that comes to mind as a good example of this inaction of this actually working really well and delivering something really huge?

Robby Stein (00:25:44):
I mean, honestly, a big thing is working on AI Mode. I think a lot of it was we saw in AI Overviews that people were trying to ask harder questions and we weren't able to answer a bunch of them, or AI Overviews just didn't show up. And so a bunch of us sat around and we're like, "Why can't you just do this for everything?"

(00:26:04):
Instead of saying, "Oh, we don't need to solve for that," or, "That's not something that's in the most addressable next thing."

(00:26:12):
It's like we actually saw people in the query stream putting the words AI at the end of their queries because they're trying to get the AI to do the thing. We would look at that and be like, "This is ridiculous. We need to build something here."

(00:26:27):
And that was one of the big motivations, was actually identifying that user problem, being very disgruntled on behalf of the user. We're just failing the user every day. We are not helping them actually get their thing better understood, and we're going to go build a whole thing because of it, because that's hard to do by the way, to build all of that. But it just was so obvious that that's what we needed to do.

Lenny Rachitsky (00:26:52):
There's two buckets of people. Let's say hypothetically, one bucket is just make things better, make amazing experiences, you're going to do great. There's another bucket that's like drive metrics, drive goals, hit our KPIs. I know what you're not saying is just work on things, just make things better, relentlessly, make things better. How do you just think about, I guess that overlap of okay, makes things better, but also here's what we really, here's the strategy, here's the vision. How do you think?

Robby Stein (00:27:18):
Yeah, I don't think of them as an or. I think they have to be intersected because basically the way I think about it is you actually start with a problem or the inverse of that, which is a vision, but they're connected. Most great companies, most great products come out of a problem, but out of the problem becomes like, "Here's a better way." What if instead of this crappy thing or way of living or thing that we all tolerate and accept, some entrepreneur comes up and says, "What if we did this other thing?" So it comes out of this dissatisfaction and this sense of better that you need to make things better, but then you're going to build, and at the end of the day, you need your instrumentation to know if you're on the right track.

(00:27:58):
And that's where you bring tools like, okay, you build your first version of the product, do people like it? And then each product goes through its journey. The way understand that people like it is you scrutinize. Typically, you talk to people, but you also add some analytical tools there. You might look at something like a J-curve. This is the retention, the percentage of people still using the product day seven, day 30, day 90, and does it flatten or do people just drip out of there? Over time, it's just not exciting people. And that would go to zero if on a long enough timeline, no one's going to use it. You don't get past that, you toast right then. Okay, some people are doing it, okay, great. We need more people to do it, and it needs to be good enough that people talk about it and then it grows. And so that's another gate.

(00:28:44):
And then there's another one which is, well, how big can this get actually, is it a small thing? Is it a medium thing? And I think most companies, you have an aspiration of being big, but you can't start big. Everyone's got to go through that journey. No product has started big. Even ones that get big really quickly, even a week quickly, they had something. And then even internally, they started small. They started small with a hundred to 100 people, and so you have to be metrics focused, I think in order to know if you're doing the right thing.

(00:29:09):
And then the other thing is, on the other side of the spectrum, you're running a big thing, and there, you need metrics to be your guide. If your product, let's say, let's say our core metrics down 5% this week, it's like, well, what's going on? And so you be really close to root cause analysis there and say, "Well, actually it turns out that it's an issue. Is it in a region? Is it on a device? Is it in a demographic? Is it in a use case? Where does my problem lie?"

(00:29:33):
And then when you get to it, you understand the problem and then this improvement thing comes back where it's like, "Okay, I'm going to fix that thing. What's the treatment for that disease?" And then you're back to growth again, and so you need this and you always are looking at what's the system that I'm working on and what are my instruments? I'm a pilot to know if this thing is going and flying correctly, but then it doesn't tell you exactly what to do, you have to thank for yourself how to make it better. I can just show you a little bit of the way.

Lenny Rachitsky (00:30:05):
I love that you just gave a master class on just how to prioritize and pick what to work on. I want to go on a quick tangent. Speaking of products that have done really well and become really big, Stories, you build and launched Stories at Instagram. It's quite an infamous product launch back in the day, it was quite controversial because it basically took what Snapchat was doing really well and then, "Hey, let's bring it to Instagram," and it was not great for Snapchat. Now that it was so long ago and just, it's so far in the past, I'm so curious just to hear about that time reflecting on just that decision, what you guys talked about, how you decided to go ahead with that and anything just, I don't know, you think about looking back at that.

Robby Stein (00:30:47):
I think there's a couple of really important lessons from that launch. And I mean we went on afterwards to launch Reels, a bunch of updates to direct messaging, we had feed rank game. There was just a huge era there when I was there between 2016 and 2021 or so where just so many new products got built. I think an interesting lesson in all of those, and particularly in Stories was you have to really understand why someone uses your product and know when something is actually an existential question because there's just a better format or a different way of doing something that has worked and works and you need to figure out what that might mean for you, because not every great thing is going to be invented by you. But I think that a lot of these things are, they can become formats that you can make your own and you need to learn from the world and what's happening out there in order for your product to always give the best thing to its users.

(00:31:41):
And so for Stories, we looked at Instagram like, what's the point of Instagram? It is sharing your life and connecting with people ultimately. And if there's a way to do that, that lowers the pressure because it doesn't have likes or it's just ephemeral format and it's optimized well for mobile because it's this full screen experience. It's a really great format and kudos to Snapchat for inventing it. We didn't think of that as a deterrent, that we had to go make Instagram photo clock. And actually, there were early versions of this idea where you try to take the core Instagram feed and make it ephemeral. And whenever you try to mix a core product that's very cemented in someone's mind and physically looks a specific way and you're trying to make, contort it to do something new, it's usually a bad recipe. And so we knew we needed to do something new and then it was so clearly was critical to the core essence of what the product could do, could fit in naturally.

(00:32:39):
But the question was how do we make it our own? And how do we build on this? And so if you think, there were a bunch of things that we did that made it Instagram. For example, it had different creative tools and it had things like neon drawing and these really sophisticated filters that people loved. We also looked at this talk about being dissatisfied. People took, a lot of times they want their main camera to take a picture of something and then they want to upload it to Instagram because they want to save it and they want it to be in a very high quality, high resolution photo, because it's a memory. And Snapchat at the time didn't allow you to upload photos, it was like you have to use the Snap camera. And so we made a bunch of decisions like that where why don't you just let people upload their photo? This is back to the dissatisfied point, that's frustrating.

(00:33:22):
Or there's another example where you couldn't pause if you were consuming a story. You couldn't pause it, it just would go through and be done because it was this ephemeral thing and you wanted to create safety. Why can't you just pause? It goes by too fast. So we added this pause, it's such a small thing, but you put your finger down to pause the story now. And so there were a whole set of those things that were shipped that made Stories feel Instagram. It wasn't like you just had some other thing. And then it turns out that worked incredibly well, and so much to the fact that someone on the team mentioned that they always felt like at the time, they didn't realize it, but it was almost like it was missing the story size holes at the top of the page and it completed the product in some weird way for them. And so that was, I think an important lesson.

Lenny Rachitsky (00:34:05):
Instagram definitely got a lot of hate for that moment from a lot of founders. It was just like, "Hey, you guys just stole this idea and that sucks."

(00:34:13):
How did you guys just deal with that internally? It was just this is, "We got to do this. We got to focus on our shareholders and grow this thing," and that's how it goes sometimes?

Robby Stein (00:34:19):
I mean, I think it's more that we're focused on our users and the people who are loving Instagram and it's denying them the opportunity to have an easy way to just share a photo and have the thing go away. I mean, that's ultimately what we were trying to add. At the end of the day, that is a format that people adopt. In the same way that you think about feeds, I think we talked about this at the time too when we shipped it. Facebook probably created the modern feed, but there's a feed for every single product. There's a LinkedIn feed and there's a feed for DoorDash.

(00:34:53):
These things become core primitives quickly and formats, and then at the end of the day, you're just robbing your user base of the opportunity to have a better product if you're not making the best possible product for your use cases. And for Instagram, it's used differently. People use Instagram differently than they use other products. And it turns out that there were these experiences in WhatsApp and in Messenger and in many other social products over time, and they all were used differently actually, which is fascinating.

Lenny Rachitsky (00:35:21):
Something else I want to talk about is you came into two products that were already doing really well, Instagram and Google. And on the Instagram side, a transformative growth and improvement. Google is happening, we're in the middle of the improvement and growth you're driving. Not a lot of people get to do this where they go into an existing product, make it grow significantly. A lot of people want to do this. They have a product that's been around for a long time. Hey, how do we make this grow and be more successful? Is there anything specifically that you've learned about just coming into an existing product, figuring out where the big opportunities are and then just hockey-sticking growth? Because this is what everyone wants to do.

Robby Stein (00:35:57):
There's a couple lessons here. And I think, by the way, the first lesson is to be humble always because it's extremely incredible to be able to work on products that have such impact on people. I view product like golf, you're always one stroke away from shanking. And as soon as you think you're good, you're not, you don't know anything. The world changes quickly. You have to always be a servant to your user base and the people that are out there and learn from them. The first thing I always do and think about is you get in touch in terms of why are people using this product, and where are the areas of growth? And so usually even in a big product or a mature in a complex system, there's a part of it that's growing. There's a part of it that's mature, there could be a part of it that's declining or isn't growing as much.

(00:36:42):
Certainly in Instagram, there's been a big shift over the years of sharing into public very large broadcast posts and feed into these more lightweight formats like Stories and DM actually private sharing as well. And so you have to observe that because every month, every year, the world changes, people's needs change. First thing you do is you get a sense of what do people want out of this product? What's its true essence? I think a lot about this job to be done framework, which is one of the things that I'm a big fan of and Clayton Christensen's book on Competing Against Luck is one of my favorite books on this topic where you have to really be a student of causation. Why is someone using this product? What are they doing with it and what are they trying to get done with it?

(00:37:26):
And that usually leads you to do bigger next stage ideas, and it removes this belief that you need to solve the problem with the current tools. In the Instagram version, it was like you have to make a square photo do more for people. That would be how you increment the product. Or in Google's example, there's something very specific with the core search experience that needs to change, it's a subtle tweak. You have to think, well, what's the big thing? Someone's trying to ask a really hard question out of Google? What's the best way to do that for them? And so it makes you think more first principled and that's the first basis of this.

(00:38:04):
And then once from first principles, you're like, "Oh, this newer thing." And it could be a shift, it could be a new form. In many ways, the AI version of Google and Stories and Reels, they're all similar in that they're new formats in the world that people are expecting and wanting more of.

(00:38:18):
And by adding them, it becomes complementary, not replacement. And in both cases, Stories didn't replace Instagram, it expanded in the same way we're seeing for AI. And so what's interesting is then you think, well, how do I bring that into my world? You have this big mature product. The best way I've seen is by making it complimentary, having it be a core part of the experience, but clearly defined as a distinctive thing that has its own attributes associated with it because people think spatially. So if you have a feed and you have holes with pictures, they expect those holes to do things. And so if you make one of those holes with a little clock and that one goes away the next day or you can't like it or it operates differently than the other parts of your feed, it's going to be super confusing for people. It sucks.

(00:38:59):
And so you have to add product carefully, but it needs to feel coherent but different. Stories, it has similar aesthetic. It obviously uses your camera roll in the same way it works that you can share it in DM, it works in the system, but it has a different primitive in the same way Google AI, it's a full page experience that you can pop out now. You can have follow up conversation with it. People have a set of expectations you need to snap to for those use cases. And then you are constantly learning how to best make these new products work within your world.

(00:39:31):
You never just want to snap in something that's working, you have to make it work for your users, your expectations, and what people are trying to do with your product. It's actually one of the things I see people fail on the most is they assume something working for one system will work in your world, but someone else's system is on totally the types of users they have with the consumer expectation of that product, that's totally different set of expectations. You have to respect that and say, "What can we learn from that," and bring it here. I guess if you were to talk about the method that I've seen now or twice, I guess that's how these products have developed.

Lenny Rachitsky (00:40:09):
I love this topic. It makes me think about just this balance. People always try to find between optimizing something they've already got versus trying to take a big bet on something. You've had so many examples where you've taken a big bet on something totally new and it's worked out incredibly well. Do you have just a heuristic in how you structure teams and prioritize across, okay, we have amazing Google experience today, what percentage of resources go into improving that versus trying something totally new?

Robby Stein (00:40:35):
That's one where I actually do feel like the more analytical, systematic thinking helps a lot because you're trying to produce value in the world, you want to quantify it some way. And so if you're seeing this growth curve and you're trying to understand, wow, people are using it more and more to liken this product. And when products are young, they grow, and then eventually things mature. You can break out product suites and different features of products all along the same way. Certain features that are growing fast, other features that are not. You get to these points of just diminishing marginal return in every system where it feels like you could put 50 people on this project, it's just not going to dramatically move the needle. Part of it is this bottoms up thing with your own team being really thoughtful about what is the expected value of that investment, and knowing when it's starting to approach zero or diminishing marginal return.

(00:41:23):
And then when that happens, these are these moments that usually coincide with something fundamental changing. Either people's expectations, externally, market saturation, there's something happening where you need to adjust. You then find your next growth driver or set of drivers. That's where you need to go more first principled and try these new things more. Then when you land a new thing that creates this new little growth engine and then you put people on it and you optimize it because each change is like 10% win, 20% win, 4% win.

(00:41:57):
It's clearly still has so much value in headroom and to make it better for people, and you can see that in the data. And so that becoming, I talked about this instrumentation, it becomes your guide for knowing if you're making good calls. Otherwise, if you don't know where you're headed and you don't have a goal of what you're trying to do more quantitatively, it's really hard to know if the thing you're doing is mattering to anyone. I think I made the product better, but is anyone using it? Does anyone care? Or are we just congratulating ourselves? Ultimately you want to have impact on people and that's what matters.

Lenny Rachitsky (00:42:29):
So it says essentially tracking S-curves on every product and understanding if you're in the plateau and if it's time to invest heavily somewhere else.

Robby Stein (00:42:36):
Yes.

Lenny Rachitsky (00:42:37):
This episode is brought to you by Orkes, the company behind open source Conductor, the orchestration platform powering modern enterprise apps and agentic workflows. Legacy automation tools can't keep pace. Siloed low-code platforms, outdated process management, and disconnected API tooling falls short in today's event-driven AI powered agentic landscape. Orkes changes this. With Orkes Conductor, you gain an agentic orchestration layer that seamlessly connects humans, AI agents, APIs, microservices, and data pipelines in real time at enterprise scale, visual and code first development built in compliance, observability, and rock solid reliability, ensure workflows evolve dynamically with your needs. It's not just about automating tasks, it's orchestrating autonomous agents and complex workflows to deliver smarter outcomes faster. Whether modernizing legacy systems or scaling next gen, AI driven apps, Orkes accelerates your journey from idea to production. Learn more and start building at orkes.io/lenny. That's O-R-K-E-S dot I-O slash Lenny.

(00:43:39):
Maybe it would be helpful to talk about the journey of AI Mode, just how it emerged and the steps that you took to now it's just such a big part of the Google search experience. When did this start? How did you decide this is worth betting on? And then what are the steps to get it further and further rolled out?

Robby Stein (00:43:55):
I mean, I think it probably started earlier on with AI Overviews actually, which was the first way we brought generative AI to search. And in that world, we noticed that people were asking these questions and many people were actually trying to put natural language questions into search. And so how can you provide helpful context links to go deeper and make an AI that made sense for Google? That was our first version of these models that could do this for people. And then by building into that and seeing this observation around people wanting more of it, direct access to it, and then being able to ask follow-up questions. You need a new modality. It's going to be really hard to build all of that within the construct of the core search experience. And so that led us to have form a small team of folks, a few people that were technical leaders, a couple designers very small to just prove out what if there was on, almost blank screen, delete, make a little fresh doc with a blinker.

(00:44:53):
What if there's a new page and you can ask the question, you can ask whatever you want of it. You can tap right into the AI that was originally powering this top of the experience in search. But we invested in making it much more powerful in the ways I described before was in it could search for you. It had reasoning as a part of its model capability, it had multi turn context, so if you had a conversation with it could keep track of that context so it had some unique pieces to it. And what would happen if we tried that quickly. And we basically got, I mean, this was probably five to 10 people worth of people originally.

Lenny Rachitsky (00:45:29):
And how long ago was this team formed?

Robby Stein (00:45:31):
This was probably over the last year, last summer basically, into the fall.

Lenny Rachitsky (00:45:34):
Wow, so about a year ago.

Robby Stein (00:45:37):
Yeah, maybe about a year ago. It was where maybe it started. We were really plugging away on it, and then we saw this little version of it emerge that wasn't very good, but it had this moments of brilliance. It's actually, again, it's kind of like golf where you hit the perfect shot and you're like, "Oh my God." You get that feeling where it's just everything worked. And I asked it a question about, I forget, I was doing something with my daughter and I was planning an experience and it found all this incredibly useful information about park information. It had links to go to the site and confirm a bunch of things. It had Google Maps information that for my daughter, you could walk up, it was walkable. There was early examples like this where it just, it blew me away of what it could find and how helpful it was.

(00:46:27):
It gave us conviction that we should go and go further. And obviously there's lots of people involved in this type of a decision, tons of support from leaders across the organization. But it just says a little working team that initially, you got to build something and then you have to feel it yourself and it is very entrepreneurial in that way. And then when you see it tangibly, you're like, "What's a version of that? That's good and that could work?" And that gave you hope. And so then we basically built it out and built the first version that launched in Labs basically.

Lenny Rachitsky (00:47:01):
So the first big milestone was this is working. It was just a qualitative experience of, "Oh wow, this has really, there's magic here."

Robby Stein (00:47:09):
Yes, it's working. And then we did bring it before labs actually to trusted tester group. There were maybe 500 people externally that we added onto it, and we had pings with them. Some of them were, we actually had friends and family. We tried to treat it a little more like a startup where, because we feel like you got to have people test it to tell you the truth, and tell you when it sucks, because it probably does.

(00:47:27):
And then they'd message you. So I had a friend who was loving it, but also hating it for lots of good reasons and would just be messaging me all the time, screenshots, "This broke, this broke, this makes no sense."

(00:47:37):
We had that for a while, and then we got to a point where it was feeling good, the trusted testers were liking it, reporting good stuff, and then we it to this Labs moment where anyone could turn it on and then we used that to make it better with real query data. We could actually see what people were using it for at more scale and so that could tune it to make it better. And then we launched it out to everyone, or at least in the US, and then we've now been on this journey to expand it to all countries and languages and have more people be able to access it.

Lenny Rachitsky (00:48:05):
It's incredible that Google went roughly in a year from idea to a significant change to the search experience that's AI powered. I think this is not what people imagine Google is like, and it feels like things are different and things have changed in how you guys operate. What has allowed this to happen so quickly? What's changed? Is it just top-down leadership, we need to get shit done, or is there something more?

Robby Stein (00:48:30):
No, I mean I think it's interesting how organizations change. I think when you feel like there is a moment in time that is clearly critical to deliver for people, people are trying to get information from Google. We are not able to answer certain things or help people in certain ways and there's this technology that can do it, that creates urgency, and obviously there's lots of people building lots of things and the market's crazy and there's lots of things shipping all the time.

(00:48:56):
There's a really exciting and healthy moment for us to build and build quickly and I think it's just exciting to be able to capture that opportunity because I think people believe, and I certainly believe that the next year or so of product is going to establish how people use the next wave of products for many years. And so at least I can only speak for myself, I feel this obligation to our users to give them the best version of Google that's powered by AI and that gives them the full knowledge of everything Google knows about the world and information to people and accessible with AI. That's driving a lot of the excitement.

Lenny Rachitsky (00:49:34):
Yeah, it's such a good point that people are building their new habits. It's wild how many people just now rely on ChatGPT and how quickly that happened. And I could see Google being worried that, oh, shit, everyone's changing their habit from searching Google to searching ChatGPT. And the fact that now Gemini is number one. I was actually looking at the list of top, so in the top 15 apps, Google is I think five of them, a third. It's out of control, killing it. When people look at AI Mode versus ChatGPT or Claude or let's even say Perplexity, what's the way you think about the positioning of AI Mode versus these other tools? Is it trying to be a direct competitor or is it just like, "No, it's actually pretty different and here's what it's for?"

Robby Stein (00:50:15):
Yeah, I mean AI Mode's a way to ask search anything you want. It's designed and specially created for information. And so really, it should give incredible helpful responses for the things that people come to Google for. Think about you're planning a trip, you're trying to buy something, you're working through a question for your research project. It needs information and that's really, it's less focused on things like creativity, although there's things that can do that are nice there. It can help you. Just like any kind of core AI product, you can ask it to rewrite something for you, it'll do that. But we are less focused on creativity, productivity, upload a spreadsheet and output graphs for me, we're not focused on that.

(00:50:57):
We're really focused on what people use Google for, and making an AI for that so that you can come to Google, ask whatever you want and get effortless information about that and context and links to then also verify, dig in and go to the authoritative sources ultimately that people want, and we hear from people. So those ends up becoming the distinct qualities of this product versus more of a chatbot. Maybe you would talk to it like you maybe even have a bit of a, "Hey, how are you doing today," with that chatbot that we have some of that, we see that a little bit, but people are usually coming for information. They're trying to learn something and we focused our product on that.

Lenny Rachitsky (00:51:30):
Got it. Okay, AI Mode is not your therapist. Maybe zooming out again a little bit and reflecting on all the amazing products you've worked on, all the places you've worked, if you had to pick two or three just core product principles or philosophies that have helped you build such amazing and successful products, what would those be? What comes to mind?

Robby Stein (00:51:53):
I mean, there's typically three things I think about. If I were to write a book about how to build great products, there'd be three chapters. I mean there'd probably more than that, but three chapters.

Lenny Rachitsky (00:52:08):
I love that. I love how short that would be. That's the ideal book.

Robby Stein (00:52:08):
I've thought about these three areas now for a while and it's like they're always consistently the three things. The first is deeply understand people, and I think we talked about this a little bit with the jobs to be done point and Clayton Christensen's book, which I loved around Competing Against Luck. It really helps you be a student of why someone ends up, in his words, hiring a product. Don't think of users as using your product. Think of users as hiring you to do something for them.

(00:52:35):
There's this famous quote, I think it's Theodore Levitt had, "People don't want a quarter inch drill, they want a quarter inch hole." So what is someone trying to do? You have to understand that deeply and then you can build an amazing product. And also by the way, when you go back, why someone not using your product?

(00:52:57):
And so it focuses on these techniques to extract causation. So he actually talks a lot about this interview. He calls it an interrogation where you talk to a user like, "Hey, why do you use my product? Where were you? Were you in bed? Were you at work? What were you doing?"

(00:53:11):
"Oh, I was talking to my wife in the morning."

(00:53:13):
"Okay, well, what brought it up?"

(00:53:15):
"Well, I guess I was reading the newspaper."

(00:53:16):
"Okay, well why?"

(00:53:17):
And then you have this aha moment like that when they first decide to use your product, he calls it the big hire. That is information that you obtain ends up becoming the most critical because that is what caused someone to use your product. And if you can study that and understand it, you'll be much more on your way than just building things that sound cool. And so that's the first chapter is deeply understand people.

(00:53:37):
Second is really around analytical rigor and understanding your problems. You have to understand your problems. And this got is a little bit of what we were talking about about root cause analysis and understanding, okay, the metrics are dropping. Why? If someone's not using your product, why? And really being able to dissect that to get to true root causes. It's like, well, they went all the way to the end and then bailed, and then you understand what turns out that it was most, we actually learned about this and there's a story in Close Friends at Instagram where it just totally failed at first in a bunch just when we shipped it. And it turned out that we looked at the data and people were only adding one close friend to their list because it was mistranslated as best friend in many markets. So people just put one person and then the probability that person saw it and wrote back to you was zero. It's a product which is broken. So it's like you got to understand your problems.

(00:54:30):
And then the third one's around really designing for clarity instead of cleverness. A lot of people are like, "Oh, we're going to differentiate the design," and we talked about this a little bit with Stories. We're going to make a new version of something, but if something's a standard and people understand it, if you lean into it, you're going to get so much leverage than if you reinvent it, and you have to be really thoughtful around when you reinvent and where you don't.

(00:54:54):
And I think on this one, there's this great, Don Norman's book. Obviously, Design of Everyday Things is a big one, but he has this incredible chapter in there about doors, and why is it that after all of these years you walk up to a door, and based on how they're designed at times, people still don't know if you should pull or push that door because if you try to build the as beautiful symmetric two handles on each side on a glass door, it doesn't communicate in for any information to you.

(00:55:20):
And there's lots of, I've seen all the time we've designed new icons when we could have used global icons like, "Oh, wouldn't it be so cool if we used a camera that's kind of a camera but is mostly an AI looking thing and then is mostly, but then has this dots in it that connects it to this other product?"

(00:55:37):
And you're like, people just, it's a camera. Just put the camera in. Maybe you could add a little thing to it, and that's how you get people to use your products. And if you do those three things, I think you typically can do well.

(00:55:49):
And then, sorry, the fourth one would be more of the coda is be humble. Constantly and always question yourself. Listen to others, listen to users and be open to being wrong.

Lenny Rachitsky (00:56:00):
I love these. On that third point, I feel like AI Mode as the name is such a good example of clarity. What is this? This is AI Mode.

Robby Stein (00:56:07):
We talked about it internally. If you look at it in the tab, it's like everyone know, it's like you see it and you'll know what it is or we could call it something random, but then what is that? And now you're working against yourself.

Lenny Rachitsky (00:56:20):
If I were to reflect back these three pieces of basically this is the book you would write to help people build more successful products, it's understand the problem you're solving for people deeply. What's the job they're hiring you to do? I love the, it's lowercase jobs to be done. It's not like the rigorous whole thing that everyone-

Robby Stein (00:56:41):
Exactly. Lowercase for sure.

Lenny Rachitsky (00:56:41):
Okay. This is just like why are people hiring your product to solve a problem for them? What problem are they solving? So it's like basically figure out what problem they're having then very, through data, understand the problem and whether you are solving it. And then it's just keep it really simple. Clarity over cleverness essentially.

Robby Stein (00:57:02):
Exactly, yes. And be humble.

Lenny Rachitsky (00:57:05):
And be humble. Yes. Okay, important. Is there an example that we haven't talked about that shows this in action of just, cool, here's the problem we found. Here's how we figured out this is the solution and if we're succeeding, and then here's a very simple way of solving it?

Robby Stein (00:57:19):
I mean honestly, this Close Friends example, I can give you more from Instagram days was really wild. It took two or three years to get Close Friends to work, and I think people, it totally failed originally. This is the product that lets you add a private list of people and then you can post to your story and then only those people see it. It's like this very exclusive private space so you can feel really comfortable sharing maybe more.

Lenny Rachitsky (00:57:39):
Oh, green circle.

Robby Stein (00:57:40):
Green circles, yes. It's one of the most popular, at least when I was there, was one of the most popular features of Stories and did really well, but it totally failed. And I think what we found out was that you actually used a bunch of these techniques here. So one was we first thought about it as an overall system problem and you could add a Close Friends post for anything. So you could do a feed post or a Stories post, and you also had a close friend's profile. You could see, if Lenny went to Robby's page, we were Close Friends, you would just be like, "Oh, you get to see extra stuff from me on my profile too."

(00:58:18):
So we shipped it, we thought it would be great. This is the be humble part, wasn't great, had a bunch of, it was just super confusing. You would see this really beautiful photo and then in the feed right after it, this blurry, very vulnerable moment someone's trying to share with their friends, just felt so out of place and weird for the reason people use feed. And then it was just confusing because it had an extra little green thing on it, but it was like that got a green thing and the Stories one didn't. If you open the story, it had a green thing inside the story, and people were just so confused.

(00:58:49):
And it had this other issue with the list where you're like, "Okay, the list doesn't work because it's mistranslated and people don't get it." I think it was actually called originally favorites, I want to say, and that encouraged people to just do two people on it. But then the way that it worked was, so this gets to the framework, I guess. So deeply understand people. What are people trying to do with this?

(00:59:10):
What they're trying to do is share a vulnerable thing and be like, "Hey, I'm lonely. Hey, what's going on? Are people up?" And it feels very much like a friend group thing.

(00:59:18):
And if you only have two people on it, the job that we're doing is actually connecting you to your friends. And if you don't get a DM back, it's broken. And so really what we're doing is getting you a DM and we're getting you connection. We're getting you a sense of being connected to your Close Friends. That is the job.

(00:59:33):
It's actually everything Clayton Christensen talked about in the book is there are utility jobs and there are emotional jobs. People usually discount the emotional ones a lot. This was really an emotional thing as much as it was utility one, and so product's broken, right? And people don't even know that it's a close friend story, they just see the little head because you have to click on it to see the thing. And so it just, people stopped using it.

(00:59:56):
We went through and we did these revs where we would simplify it and we would update it and we would go through this change list. Okay, take this out, take this out, change the name, here. And then we saw it was that it was working really well for people who added 20 to 30 people to their list. Because what would happen is you put 30 people on your list and then two of them would write back to you on DM and now you have closed the loop and you feel connected to those people. It's a winning thing. And so we designed the whole system around that, and also only worked in Stories. We were looking at the data, we were trying to understand where it was working and where it was failing, and then we updated the name to Close Friends so it didn't feel like favorites. So it wasn't three people, it's 20.

(01:00:34):
In the list, we built this list builder where we recommended a set of people based on some cool algo that was created by an engineer. And then we updated the design to put the green ring on the outside of the story so that this was the design for clarity. We were being cute. We thought, I think at the time it was like, "Oh, it's a secret story or something, and if you open it, you see it."

(01:00:56):
It just was not clear to people. And so we put the green ring on the outside so that users would see it in the tray and be like, "Ooh, what's that little green guy?"

(01:01:04):
And then they'd click on it and be like, "Oh, this is a private story for me." That system worked and did incredibly well, and that was the process we followed from a total flop to something that was very successful.

Lenny Rachitsky (01:01:16):
That is an awesome example. And this took two or three years, you said this process?

Robby Stein (01:01:19):
Yeah, it took a while. That was actually one of the longest projects we worked on, but that actually came, the reason we did it was when we asked people to understand people like, "Why aren't you posting to your story? What's preventing you from doing it?"

(01:01:32):
And everyone had some version of, "Well, my ex is on it. I have a teacher on it. Oh, a friend that kind of is judgy is on it."

(01:01:39):
It was like this commonality was audience problem. Someone had an issue with people watching them. And so that gave us conviction to go this hard at it for so long because we knew that that was a core problem with the product.

Lenny Rachitsky (01:01:51):
Was this connected to the Finsta, Rinsta trend also?

Robby Stein (01:01:55):
It was actually. I think that informed us. Everyone had a Finsta and there was a Binsta.

Lenny Rachitsky (01:01:58):
Was is a Binsta?

Robby Stein (01:02:00):
Best friend Insta.

Lenny Rachitsky (01:02:03):
I see.

Robby Stein (01:02:03):
Different, it's this layering of people 20 Finstas down to your partner, Pinsta, and then it's basically like, I made that up. I don't know if it's true, but I'm sure it was out there somewhere. We were like, "Wow. People clearly are trying to hack Instagram basically to create these private smaller group settings, and so we should just make a product."

Lenny Rachitsky (01:02:23):
How did you actually do this testing? Was it rolled out to some percentage? Was it rolled out in New Zealand or whatever?

Robby Stein (01:02:27):
Yeah, we rolled it out in a few other countries, exactly.

Lenny Rachitsky (01:02:29):
Okay,

Robby Stein (01:02:29):
Got it. We had a basket of countries that we tried it in and then we would do research. I think it was Australia was one of the first ones for that one.

Lenny Rachitsky (01:02:37):
Okay. I was going to ask if you can share the country. So Australia.

Robby Stein (01:02:40):
I think that was one of the earlier ones, yeah, but every time you ship something there's a slightly different reason why.

Lenny Rachitsky (01:02:46):
Oh, interesting. So it's not always Australia gets all the new stuff.

Robby Stein (01:02:49):
No, although it sometimes is. Australia and Canada get a lot of stuff just because easier for the teams to see feedback from them.

Lenny Rachitsky (01:02:57):
Yeah, speak English.

Robby Stein (01:02:59):
Yeah, exactly.

Lenny Rachitsky (01:03:00):
Awesome, okay, let me go in a different direction and talk about something that you have a hot take on. There's a lot of talk these days about lean teams, small teams, just creating limited resources, not hiring at all. You have an opposite perspective of you actually need a lot of resources to build really big breakthroughs. Talk about your experience there.

Robby Stein (01:03:19):
Yeah, I mean I think there's obviously, depends on what you're trying to build and there's been famously small teams building big impact products, but I think there's this cult of lean, scrappy, fast, throw away your product quickly, keep moving. And I think at some level it's true for internal conviction, but to build a product that works for a lot of people that is based on a technological breakthrough. A lot of times, I see teams just give up to early or under invest in the product, and obviously the space matters. And if you're building a single product that is a way to, I don't know, do something with a digital app that's fairly straightforward, that's going to be different than building a robotics company. So what you're building does change.

(01:04:02):
But even for software, I mean I think for really hard technical problems, think about the amount of time and effort it took for teams to build a foundational model, and how many years and hundreds and hundreds of people that were needed for that to happen. And you think about these large companies that have had huge impacts on people, and I think particularly for bigger companies internally, something I've seen is it's almost too scrappy because it never gets enough momentum. The product never gets good enough internally and then it just dies on the vine. Whereas if you put more people on it, you have to be careful not to put too many too soon. But I see the opposite more true where people hold on to small teams too long and then you, either takes forever to get to the thing you're looking for.

(01:04:46):
This Close Friends example I mentioned this actually was a small team. One of the reasons it took us forever was it kept the team so small and scrappy. That loop cycle was so short and by a startup age you'd be dead probably. So you can maybe do that in a bigger company, but as a startup, I don't know if you have that leisure. And so I think you need to actually think what is the group I need to build a version that's great. And from first principles, really think about it instead of just embracing blindly, okay, we're going to be the two of us until this thing has escaped velocity market fit, which it's not always true.

Lenny Rachitsky (01:05:19):
This is definitely counter to the narrative we see on Twitter. Anything you can share about just the heuristic you use to decide here's how long to keep it small? I know there's not going to be this step 1, 2, 3, but just like what I'm hearing is start small to prove out the concept designer PM engineer maybe. When do you find that makes sense to go big?

Robby Stein (01:05:40):
Yeah, I think that it's mostly when you've hit the conviction moment. I think there's two big milestones. There's internal conviction. For yourself, do you believe in it? And you believe in it because there's some external validation, your friends, you put 20 friends on it. And by the way, I found out very quickly building startups that if you put 20 friends on something, they're not going to do you that many favors. They're not going to use a product every single day because they're your friend 30 days in, 60 days in, 90 days in. They're not using your product unless you're doing something that's useful to them. And so you get all of this feedback and you're seeing people really enjoy it. You get to that moment.

(01:06:17):
And then I think that's not a product that would win externally because if you were to ship it, it's broken, doesn't work great. And then you need to, I think invest enough to make the best version of it or as good a version as you can to get it out the door and to ship it. And I think that that, it's like you want to build the right product eventually is the mentality and you can only really do that with the right group.

Lenny Rachitsky (01:06:39):
I'm going to take us to a recurring segment on the podcast that I call AI Corner.

Robby Stein (01:06:43):
Okay.

Lenny Rachitsky (01:06:44):
What's some way that you've found use for AI in your work, in your life that is really interesting, really helpful, maybe other people can be inspired by?

Robby Stein (01:06:53):
I think one of the coolest trends ever is how AI is affecting multimodal visual and inspirational needs for people. And we're early in this and I think this is something that I'm actually working on as a project as well, but right now if you think about what AI has done in large part, it was born and grew up in this text modality, it was chat. And so for a long time, if you were to ask it to help you, what's a cool way to redecorate your bookshelf behind you? It's going to describe that to you in text, because that's what it knows. But increasingly, AI is going to be liberated to help in every possible modality.

(01:07:29):
This is something that we've seen a lot with this explosive use of Google Lens and our image search and image features and with this deep understanding, and what I'm actually starting to use internally and some things that we're excited about more coming up that we actually announced at I/O that we're going to going to be building more of was how AI can help with inspiration, how AI can help with shopping and helping you really get things done that are more in the inspiring bucket of needs versus these core utilities like code, math, homework side of things.

(01:08:04):
And I'm really excited for things that are coming where you can ask it for inspirational tasks and it's starting to do really fascinating things in terms of what I'm seeing and hopefully we'll share more on that soon. But I think the one thing I can share is there's a visual version of AI Mode that basically we talked about at I/O, and so you can reference some of those keynotes, but that's in the process of being rolled out.

Lenny Rachitsky (01:08:34):
Mysterious.

Robby Stein (01:08:34):
And so you're going to be able to now ask what's a mid-century modern beautiful office design with dark themes? It'll be able to produce this image board that's inspirational and you can do multi-turn with it. And so you'll be able to go and say, "Actually, I want more of a light theme, more creamy, more California, more coastal vibe." And it'll do that and it'll understand that and it'll actually see the images and be able to turn with you in the way that text works, which is going to be really cool. So I think that's going to be one of the more exciting things that will be new to AI soon.

Lenny Rachitsky (01:09:10):
What I'm hearing is Nano Banana integrated into AI Mode. Recipe for success.

Robby Stein (01:09:14):
Well, it's a little different than Nano Banana because Nano Banana is an image editor. This is more like helping you find images on the web, so it's a little bit more like AI inspiration, AI image search, and allowing you to then talk with two effectively visual responses with natural language. So that's going to I think, be a little bit different than edit this photo so that it changes it. Although potentially an interesting idea too, to have an ability to take a picture of your living room. And I think AI will help with that too ultimately.

Lenny Rachitsky (01:09:48):
Pinterest is in trouble, feels like this is what people use Pinterest for. Here's all the inspiration. Now it's just AI doing it all. By the way, Nano Banana, where does this name come from?

Robby Stein (01:09:58):
I don't actually, I forget that. There's a story somewhere. I forget it now honestly. But the team I think came from a scrappy, fun group of people building this and they wanted to go for something fun for folks to-

Lenny Rachitsky (01:10:13):
Yeah, it feels like that's a part of the reason things have started to work. There's just more fun and delight and random crazy stuff coming out.

Robby Stein (01:10:20):
It does. It feels a little more like when I was at Google the first time through right now where you just have so much stuff and this kind of fun curiosity happening where people want to try things and ship things and yeah, hopefully that continues.

Lenny Rachitsky (01:10:31):
Yeah, it feels like Veo 3 would be even more successful if it had a wacky name. And I like that this is the opposite of your advice of clarity. I don't know what Nano Banana is, but it worked.

Robby Stein (01:10:42):
Yeah, it's the other thing. No advice is right universally, right? But yeah, Nano Banana.

Lenny Rachitsky (01:10:49):
Robby, is there anything else that you wanted to share? Anything else you want to leave listeners with as a final nugget of wisdom before we get to a very exciting lightning round?

Robby Stein (01:10:58):
This concept: be curious. I think of embodying everything as like it's really about curiosity. It's about wanting to know why everything is the way it is. Why is someone doing something? Why does someone have a different opinion than I do? Why might this not be working? And the people who really have that level of intense curiosity and they chase things down until they know, I think you're well served by that. That would be my only parting thought.

Lenny Rachitsky (01:11:20):
Let me follow that thread actually, because it's maybe the most trending term on the podcast over the past few months is curiosity. It comes up a lot when I ask people, what are you teaching your kids and embracing with the rise of AI and curiosity comes up all the time. Is there anything that helps you? Is it just like I am good at this and I am curious innately and I'm just, "This is valuable." Is there anything you can share that helps you or others around you embody that and actually be curious?

Robby Stein (01:11:48):
Well, I mean AI is obviously the ultimate curiosity engine, and that's what's so cool is you can now ask anything and just get information. And so I find that people just appreciate just how much they can learn about whatever they want. But also, I think that a lot of this also comes down to studying what you want to know about, and knowing where the branches of knowledge live there. A lot of times I'll read old papers and PDFs that are free online on a statistics thing if I want to learn about that and I think people under appreciate those. There's analog old school great learning and AI can help you discover them. I'm using AI, I'm particularly at Google to help discover all these cool links and things to read, but I find that that is an interesting hybrid where it's not just AI but really going to original sources more. I find that these books I mentioned on the chat here, I find that you need a blend of all of those things to ultimately really get to the bottom of things ultimately.

Lenny Rachitsky (01:12:46):
Actually reading the thing, not just reading the summary of the thing.

Robby Stein (01:12:48):
Yes.

Lenny Rachitsky (01:12:49):
Let me actually ask you this question I've been asking all these people that are at the cutting edge of AI. You have kids, is there anything you're thinking about and leaning into helping them learn, develop as AI emerges and becomes a big part of the world?

Robby Stein (01:13:04):
The biggest thing I'm doing, I have younger kids, so the biggest thing I'm doing is they're using live versions of AI that they just talk to now much more. And so funny enough, we actually just launched search live actually out of Labs this week. And so you can talk to search in a live AI setting, which is conversational voice. Voice on when you're driving, you can just talk all the knowledge I talked about where you can do with Google, you can talk to it in a normal conversation with your voice. And I found that to be incredibly accessible for kids.

(01:13:31):
And I hear all my kids come home, they're like, "Can I talk to Google about something?"

(01:13:34):
"What do you need? What do you need to say?"

(01:13:36):
And then they go to my app, they hit the live button and they just start talking to it. They want to know about animals, they want to know about certain, I don't know, history things. They learn about something in school, and it's so natural to learn in that way that I think that that's helping them become much more AI native than any other thing I'm doing.

Lenny Rachitsky (01:13:56):
Life as a parent is going to be way too easy now whenever kids have questions, "Just go talk to the AI," but I don't think that's bad. So this is within the Google search app. There's a live, how do you access this?

Robby Stein (01:14:07):
Yeah, that's exactly right. You go to Google app, so there's one of the apps in the App Store you mentioned. You open Google and there's a button now that's live on it, right on the home screen. And if you tap on, it's a live version of AI Mode that you can just talk to. It's a full screen experience, and we'll say start talking.

Lenny Rachitsky (01:14:22):
In the show notes, I'm going to link to this project that somebody built, Eric Antonow, which I love. It basically shows you how to put a little speaker into a little stuffed animal and you connect the speaker to, it could be Google Live or it could be ChatGPT, whatever you like, in voice mode. And you put it on your shoulder, you get a little magnet that attaches, and your kids could talk to this parrot, for example, and you could tell it, "Talk in a pirate voice," and so they're talking to his pirate.

Robby Stein (01:14:49):
Oh, that's really funny. Okay, that's really cute.

Lenny Rachitsky (01:14:51):
It takes 15 minutes. You could get an X-Acto knife and sew it and stuff and it's fun. I made one for my nephew and he was looking for treasure with this parrot.

Robby Stein (01:14:59):
That's really adorable, I'm definitely going to look into that.

Lenny Rachitsky (01:15:02):
Robby, with that, we've reached our very exciting lightning round. I've got five questions for you. Are you ready?

Robby Stein (01:15:07):
All right, I'm ready.

Lenny Rachitsky (01:15:08):
What are two or three books that you find yourself recommending most to other people?

Robby Stein (01:15:11):
I mean, definitely the two I mentioned here. Clayton Christensen, Competing Against Luck. Don Norman, Design of Everyday Things. But I also really love this for fiction, Aurora, which is this book David Koepp wrote. It's about electromagnetic pulse in the sun that knocks out, it's fiction for just fun. And it was a really fun beach read and apparently it was going to be made into a Netflix show, it didn't work out. I don't know. It was sad to see that fall apart, but so it's a really fun book.

Lenny Rachitsky (01:15:39):
There's a book along those lines that I love, they're making a movie of it right now called Hail Mary.

Robby Stein (01:15:43):
Oh, I'm in the middle of reading that right now.

Lenny Rachitsky (01:15:45):
Okay, awesome.

Robby Stein (01:15:46):
Yes.

Lenny Rachitsky (01:15:46):
Of the same mind.

Robby Stein (01:15:48):
Yes.

Lenny Rachitsky (01:15:48):
Yeah, they're making a movie of it. How about that?

Robby Stein (01:15:50):
In the middle of reading it. It's getting wacky where I am right now, but I'm excited to see where it goes.

Lenny Rachitsky (01:15:54):
It gets wackier. The ending especially wacky.

Robby Stein (01:15:55):
Oh, really? Okay.

Lenny Rachitsky (01:15:56):
Just prepare yourself.

Robby Stein (01:15:57):
Okay.

Lenny Rachitsky (01:15:59):
What is a recent movie or TV show you've really enjoyed?

Robby Stein (01:16:02):
I love The Bear. I think that's just absolutely awesome show. Dune, of course. And I thought the new Top Gun is a little old now, but I think the new Top Gun was so fun and awesome.

Lenny Rachitsky (01:16:13):
Is there a product you've recently discovered that you really love? It cannot be AI Mode.

Robby Stein (01:16:17):
I'm going to use a non-digital product.

Lenny Rachitsky (01:16:19):
Perfect.

Robby Stein (01:16:20):
I'm super into this new pillow that I got called Purple Pillow, and I've been recommending it to everyone at work. We're on a pillow chat now. It's a thing. It's like you talk about what pillows we're getting, but it's this really cool thing where it's got this new technology of this honeycomb polymer that's inside and so it supports you and it has these little micro holes so it doesn't get hot. It's really cool. Big fan. Strongly recommend Purple Pillow.

Lenny Rachitsky (01:16:50):
I've never heard of this thing, I am excited. I recently got an avocado pillow, focusing on low toxins.

Robby Stein (01:16:57):
Oh, those are good. I've heard good things about those too, yeah.

Lenny Rachitsky (01:17:00):
Okay, I got to join this pillow. Pillow talk is a great name for it by the way.

Robby Stein (01:17:04):
You're into pillows too. That's great.

Lenny Rachitsky (01:17:05):
Huge.

Robby Stein (01:17:06):
I love bedding.

Lenny Rachitsky (01:17:06):
No, I'm just joking.

Robby Stein (01:17:07):
Yeah, great.

Lenny Rachitsky (01:17:08):
But I did upgrade my pillow. This is not Mr. Pillow, whatever that guy is, right? Is that guy that, there's like a controversial pillow guy. Okay.

Robby Stein (01:17:17):
No.

Lenny Rachitsky (01:17:17):
Okay. Purple Pillow. I'm going to ask AI Mode.

Robby Stein (01:17:20):
Yeah, you should.

Lenny Rachitsky (01:17:20):
This.

Robby Stein (01:17:20):
Definitely.

Lenny Rachitsky (01:17:22):
Next question. Do you have a favorite life motto that you find yourself coming back to in life?

Robby Stein (01:17:28):
This is be curious. I think I almost named a company Curious. I just think it's a really awesome, there's one thing in life. It's that in terms of getting things done, in terms of understanding the world, people, your kids, your family. You always just want to know more and question things outside yourself, not feel like you have all the answers. I think that's really important.

Lenny Rachitsky (01:17:49):
I love that. Final question, okay, so speaking of startups, you started a company called Stamped back in the day, it got acquired by Yahoo. I hear there's a story where you got Justin Bieber on your app and that was a big deal and a big inflection in the success of the app. Can you just tell that story?

Robby Stein (01:18:06):
Yeah, it's a wild story. Just to scene set a little bit. I was 25 right after Google being an IC PM in New York with some Google friends building this company. So very early on, and maybe in a good way and no idea what I was doing. But basically we decided that the concept of Stamped was to put your stamp on your favorite things, get recommendations from friends and from people that you trust. And so you think of a Twitter feed, but it's all stuff that people think is cool.

Lenny Rachitsky (01:18:34):
Which products.

Robby Stein (01:18:35):
It's like books, restaurants, food. Products, exactly.

Lenny Rachitsky (01:18:37):
Pillows, possibly.

Robby Stein (01:18:37):
Pillows could be on there. I would totally stamp this pillow and then you could discover it. And one of the cold star problems was obviously you want a group of people that are on it that are already using it, that could have some tastemaker type folks. We had a bunch of people that were chefs and we had people who were literary folks. And then we wanted to get a couple people that were more musicians, artists, and these influential folks.

(01:19:00):
My co-founder and I just basically got the contact of Scooter Braun, who's Justin's manager, and we just sent out an email and we were like, "Hey, we're in New York. We're going to be in LA tomorrow." I think we said something, I don't remember all the details, but it was something like tomorrow.

Lenny Rachitsky (01:19:15):
And you were not going to be in LA tomorrow.

Robby Stein (01:19:16):
No, no.

Lenny Rachitsky (01:19:17):
Okay.

Robby Stein (01:19:17):
"Do you happen to be there?"

(01:19:19):
And he just wrote back some one line thing like, "Meet me at this hotel for breakfast at something."

(01:19:25):
And we're like, "Oh, okay."

(01:19:28):
We literally went immediately to the airport. I just remember just basically going straight to the airport, flying to LA meeting with him. We gave him the whole pitch, we showed him the product, and then he was like, "Okay, I think this would be super cool. We can be involved and maybe you can help be an advisor."

(01:19:44):
And we ended up going back and meeting with Justin and showing him the product and even filming some little clips with him. It was actually really funny and it was a really fun moment. And obviously he was using it to stamp his favorite stuff. And so people would go, "Oh, Justin's into this song, or he is into this stuff," and would post that.

(01:20:02):
It was one of the ways that we got lots of people to try out and see what we were doing. That's a little extra scrappy moment in time, but I think it embodies a good lesson. Just do it now, be scrappy, be immediate. Intense urgency usually wins over thinking about it for a long time, and that's certainly proved to be true on that one.

Lenny Rachitsky (01:20:20):
Incredible story, thank you for sharing that. So many lessons to take away. Two final questions, where can folks find online if they want to reach out, maybe learn more about what you're doing and how can listeners be useful to you?

Robby Stein (01:20:31):
Yeah, I think on X @rmstein is probably the best single place. And then to be helpful, send me feedback. DM me, just mention me, ping me, let me know problems with Google products, with AI in general, but also just anything. As I said before, you have to always listen to people understand their experiences, so ping the ideas and feedback. That's the best way to be helpful.

Lenny Rachitsky (01:20:52):
Wow. What an onslaught you're about to receive of feedback on the search experience.

Robby Stein (01:20:56):
No problem. Yes, please do.

Lenny Rachitsky (01:20:58):
"Robby, why is this link second? Why is my site not at the top?" I can only imagine the kind of stuff people complain about. Robby, thank you so much for being here.

Robby Stein (01:21:08):
Thank you, it was great.

Lenny Rachitsky (01:21:09):
It was great. Bye, everyone.

Robby Stein (01:21:11):
Take care.

Lenny Rachitsky (01:21:13):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating, or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcasts.com. See you in the next episode.

