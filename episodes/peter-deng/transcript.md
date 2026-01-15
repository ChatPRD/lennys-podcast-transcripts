---
guest: Peter Deng
title: Peter Deng
youtube_url: ''
video_id: ''
description: ''
duration_seconds: 0
duration: 0:00
view_count: 0
channel: Lenny's Podcast
keywords:
- growth
- retention
- metrics
- user research
- mvp
- experimentation
- analytics
- pricing
- hiring
- team building
- culture
- leadership
- management
- strategy
- vision
---

# Peter Deng

## Transcript

Lenny Rachitsky (00:00:00):
You built and led Facebook news feeds. You shipped the Messenger app as its own app. You launched ChatGPT Enterprise. What's an important lesson you've learned about what it takes to succeed building something from idea to one to billions?

Peter Deng (00:00:12):
You have to plan your chess moves out in advance. You have to really think before you act and build systems that were going to let you go sustainably faster.

Lenny Rachitsky (00:00:21):
What's the most counterintuitive lesson you've learned?

Peter Deng (00:00:24):
Sometimes your product actually doesn't matter. At Uber, I learned this because, really, the price and the ETA at Uber was the product. Looking at it from a holistic perspective, we humans consume the entirety of the product. It's not to say that you shouldn't fix the bug, but it doesn't have as much of an impact as something that is more important to people.

Lenny Rachitsky (00:00:42):
What's one specific thing you think will change in a big way with AI that people don't think enough about?

Peter Deng (00:00:47):
Education is going to change. My son, he was nine at the time, built a custom GPT that you can type in any topic and it would give you a sentence that had every letter of the English alphabet. Isn't that mind-blowing? I can already see his brain rewiring.

Lenny Rachitsky (00:01:00):
What's one thing you look for in people you hire?

Peter Deng (00:01:03):
In 6 months, if I'm telling you what to do, I've hired the wrong person. It helps me and the person operate on a different level where the goal is not, did you hit this OKR? The Meta goal becomes, are we calibrating enough? Are we actually getting into a spot where in 6 months you're the one telling me what needs to be done?

Lenny Rachitsky (00:01:20):
What's something you've learned about what it takes to be a great product person?

Peter Deng (00:01:23):
I think there are five different types of product managers. Number one is-

Lenny Rachitsky (00:01:27):
Today my guest is Peter Deng. Peter is maybe the most under the radar impactful Product Leader that you have never heard of. I often say that the best product people are not the people on Twitter and LinkedIn sharing advice, but the people who don't have time to do that because they're too busy doing the work. Peter is the epitome of this. He was VP of product at OpenAI where he oversaw product design and engineering for ChatGPT and helped ship ChatGPT Enterprise, voice, memory, desktop, custom GPTs and more. He also oversaw and built their first growth team. He was the first Head of Product at Instagram where he worked closely with Mike and Kevin, and oversaw all product development, including on content sharing, ads, growth, even helped build out their design and user research functions. He was also a Head of the Rider product team at Uber where he oversaw everything in the Rider app, including big improvements to pickups and drop-offs at Uber Pool and airports.

(00:02:18):
He also helped the team launch new products including Uber Reserve, which is now approaching a $5 billion a year business. He also spent nearly 10 years at Facebook as their 4th ever Product Manager where he built and led the team behind the current Newsfeed product, the standalone Messenger app, also photos, and groups, and homepage, and profiles. He was also Chief Product Officer at Airtable where he helped the company systemize how they built products and transitioned to Enterprise. He also led product management at Oculus. These days he is General Partner at Felicis where he is able to bring everything he's learned to more founders as an investor. He has never done a podcast before or shared any of these lessons or stories publicly. So, you are in for a real treat.

(00:02:56):
A huge thank you to Eric Antonow, Nick Turley, Lauren Motomati, Joanne Jain, and Sundeep Jain for contributing questions and topics. This conversation, if you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become an annual subscriber of my newsletter, you get a year free of a bunch of amazing products including Bolt, Linear, Superhuman, Notion, Perplexity and Granola. Check it out at lennysnewsletter.com and click bundle. With that, I bring you Peter Deng. Many of you are building AI products, which is why I am very excited to chat with Brandon Foo, founder and CEO of Paragon. Hey Brandon.

Brandon Foo (00:03:29):
Hey Lenny. Thanks for having me.

Lenny Rachitsky (00:03:31):
So, integrations have become a big deal for AI products. Why is that?

Brandon Foo (00:03:35):
Integrations are mission-critical for AI for two reasons: First, AI products need contacts from their customer's business data such as Google Drive files, Slack messages or CRM records. Second, for AI products to automate work on behalf of users, AI agents need to be able to take action across these different third-party tools.

Lenny Rachitsky (00:03:54):
So, where does Paragon fit into all this?

Brandon Foo (00:03:56):
Well, these integrations are a pain to build, and that's why Paragon provides an embedded platform that enables engineers to ship these product integrations in just days instead of months across every use case from RAG data ingestion to a Agentic actions.

Lenny Rachitsky (00:04:10):
And I know from firsthand experience that maintenance is even harder than just building it for the first time.

Brandon Foo (00:04:15):
Exactly. And we believe product teams should focus engineering efforts and competitive advantages, not integrations. That's why companies like U.COM, AI21 and hundreds of others use Paragon to accelerate their integration strategy.

Lenny Rachitsky (00:04:29):
If you want to avoid wasting months of engineering on integrations that your customers need, check out Paragon at useparagon.com/lenny. This episode is brought to you by Pragmatic Institute, the trusted leader in product expertise. Pragmatic Institute helps product professionals turn ideas into impact through proven courses, workshops and certifications designed for real-world success. For over 30 years, they've trained more than 250,000 product leaders at companies like Google, Microsoft and Salesforce. Equipping them with practical strategies to build and scale market-winning products.

(00:05:05):
Pragmatic's full-time instructors each bring over 25 years of hands-on leadership experience, teaching strategies proven to deliver real-world results. And it's not just about what you learn, it's also about who you learn it with. Completing a course connects you to an active community of over 40,000 product professionals. You'll engage in meaningful conversations, collaborate with peers and mentors, and gain direct instructor access to refine your strategies and stay ahead of trends. Get 20% off with Code LENNY20 at pragmaticinstitute.com/lenny. Peter, thank you so much for being here and welcome to the podcast.

Peter Deng (00:05:45):
Thank you. I'm so thrilled to be here, really honored. Looking forward to having a great time here.

Lenny Rachitsky (00:05:50):
As we were preparing for this conversation, we were jamming on what we should focus on. There's so much that we're going to talk about. But something that you said was really interesting and I'm really excited to start with this, which is that, you've always felt that you haven't been able to say all the things you really think and feel because you've been within corporations, PR people keeping you on message, and this is the first time that you feel free to share.

Peter Deng (00:06:11):
First time.

Lenny Rachitsky (00:06:12):
Okay, so first of all, just how does that feel? Second of all, tell us something that you've been wanting to share or that you can finally talk about.

Peter Deng (00:06:19):
Well, it feels really good. So, let me ask... I love it that you're starting with a spicy question here and let me share some more context behind it. I'm here to speak more freely, but it's not really what you think. I'm not here to divulge any secrets from the companies. But naturally I'm kind of a storyteller, I'm kind of an introvert. So, this podcast, I feel like I have the ability to go deeper with you on any topic and kind of add the context. Because I think without some of the context, some of my spicy takes or whatnot might be taken out of context, and just not having the time pressure, not feeling like there's some PR message I have to hit, is just really freeing. So, it feels awesome, really anything that is on your mind that you should find interesting to your listeners, I'm here for it and yeah, I'm excited.

Lenny Rachitsky (00:07:07):
Something I always tell guests, and I don't want people to take this out of context also, but I always describe myself as a reverse journalist where I want the guests to be the best version of themselves. I never want to catch people off guard or just say something they never meant to say. So-

Peter Deng (00:07:21):
That's great.

Lenny Rachitsky (00:07:22):
... it's a safe space. Okay. But still, is there anything that you want to share or that might be interesting to share that you've been wanting to share that you haven't been able to? Is there anything along those lines?

Peter Deng (00:07:31):
I mean, I always get this question around sort of, AGI, is it coming? Is it going to solve everything?

Lenny Rachitsky (00:07:38):
What have you seen?

Peter Deng (00:07:40):
I mean, it's so interesting because when I was at OpenAI, it was around the time that people were really scared of AI and, "Oh, it's going to get rid of humans or it's going to do all these things." But with every technology, I think everyone's been just kind of taking some time to acclimate to it. And I think with AGI it's a similar thing, which is it's so far out that everyone's like, "Well, what's our world going to be like?" And the real answer is none of us really know. But in terms of solving problems, I think some people believe AGI is going to solve everything, but I don't think so. AGI is just necessary but not sufficient. A lot of the value is still going to require a bunch of hustle from a lot of builders to really turn that new source of energy and channel it into something that we humans want to use that solves some of our problems. And that hustle is going to be required, that elbow grease is going to be required to really make AGI something useful.

Lenny Rachitsky (00:08:38):
Your point is that people think AGI hits, all of a sudden all jobs are gone, AGI is doing everything. Because I think this is a optimistic message that things will be okay if AGI, basically AGI being, and I'm curious if you have a clear definition, but AGI being, AI being just basically as smart as humans-

Peter Deng (00:08:56):
Look, I won't-

Lenny Rachitsky (00:08:56):
... generally.

Peter Deng (00:08:57):
... claim to be an expert on this at all, but I think that with every technology that's come out, we've been able to harness it and it takes a lot of harnessing. I think I'm going to use that word very deliberately. I'll use something really basic. What seems obvious today is that, there was a time when databases were all the rage. It's like, "Oh my goodness, you can store a bunch of data and you can query it really quickly and imagine all the possibilities." And I think that a lot of amazing entrepreneurs and builders built some really great products on top of databases.

Lenny Rachitsky (00:09:30):
That's right.

Peter Deng (00:09:30):
In fact, that's kind of the basis of all the stuff that we're seeing today. And it seems so obvious today, but I don't know, maybe in 10 years, 15 years when we look back, it's like, "Of course it made sense that we have this super intelligent thinking machine." But it requires the product builders to be able to go in there and say, "How do we channel this energy to make it something that we as humans love to use and want to use?"

Lenny Rachitsky (00:09:55):
I love the optimism around this. It's just like things will not go crazy once computers are as generally intelligent as humans.

Peter Deng (00:10:03):
I think that's exactly what I'm trying to say. And I think that again, every technology people have this fear. And I remember watching a documentary once and they were talking about how when the bicycle came out, people were like, "Oh my goodness, this is going to be the end of all things." And again, it sounds silly today. Because you're like, "bicycles, really?" But then if you put yourself in the context and the mindset of a previous generation, which the next generation will be looking back at this podcast in that previous generation, I think that again, I think optimistically, things are going to be okay, we're going to adapt. And this was actually one of the things that I talked about with my friend Josh Constine at South by Southwest, is this idea that humans will always co-evolve with technology. And I think that that co-evolution is already happening.

(00:10:55):
If you take a look at, there was a lot of a fear of AI just when ChatGPT came out, but when you start to get familiar with it things, that kind of things change and then you are able to evolve from being fearful to familiar and to go all the way to having this mastery of this thing of like, "Oh my goodness, look at all the startups that are happening now. All the things that we can build. And just over 18 months." I would say we look back and there's been an attitude shift. And so I guess part of my optimism comes from, if you look back 18 months and you look forward 18 months, might it be the same thing for something that we're chasing now?

Lenny Rachitsky (00:11:35):
Well, let me follow this AI thread a little bit more and then we can move on to other things. I feel like every conversation, there's a time to AI conversation and then it's like, okay, there's other things that also matter. So, let me ask you this, the question, what's one specific thing you think will change in a big way with AI that people don't think enough about?

Peter Deng (00:11:52):
I think education is going to change in a big way. And I think a lot about this because I'm involved in my kid's school quite a bit, and that's something I've done after I left OpenAI. And what's fascinating to me is that watching my son who got to dog food, a bunch of the OpenAI stuff before it was public, I think I can safely say that, that seems okay. And when he was playing with ChatGPT and some of the latest models and he was nine at the time, I can already see his brain rewiring. He was starting to ask questions and he never heard the word prompt before, but he's like, just this is how awesome the human mind is, because he was exposed to this technology at an early age, some things just are unlocked. And I think that you're able to think differently. And I'll give you a specific example of what I mean here.

(00:12:51):
He goes to Python class and he's coding. Now, I don't actually think he's going to have to code when he grows up. I think that's going to be a solved problem. But it's a very valuable skill because I think learning to program is learning how to think in a structured way, in a systematic way. And he was prompting ChatGPT with some really crazy things that I never even thought of. And one of the things was, "Hey, ChatGPT, can you give me a sentence that has every letter in the alphabet along the theme of oceans or along the theme of space?"

(00:13:32):
And the reason this kind of blew my mind is because in traditional programming you couldn't write that program. You can't say in Python like, "Oh, write a function that goes and formulate." I mean, it's a really difficult function to write. But for him to be able to think of that prompt, which is really cool because he built a custom GPT that you can type in any topic and it would give you a sentence that had every letter of the English alphabet, kind of like the quick brown fox jumped over the lazy dog. Isn't that mind-blowing?

(00:14:08):
At age nine he could think about that, whereas being at age nine, I was playing with Legos and maybe QBasic. And so this idea of how young human's brains will evolve because of this new tool we have is going to change the way I think we're going to do education. And I'll be very honest, I'm not an expert in education, but I just thought a lot about it. And one thing I think is going to be really important in the future is being able to figure out how to ask the right questions. We humans are inherently inquisitive. But being inquisitive and turning that into the right questions to prompt or ask AI, which is going to be again, something that everyone's going to have access to is going to be a differentiator for what kind of work can be done.

(00:14:56):
The analogy I'll draw is, when the calculator was invented people didn't stop doing Math, they just did higher level Math. And it frees the mind up to do other things and think more at a higher level of abstraction. And I think we got to prepare our kids on thinking about, "Well, how do you think at a higher level of abstraction?" And this has happened before. I think Google has made memory kind of obsolete. You don't have to memorize facts anymore, you can just Google it. And the next phase will be something around, "Well code will just appear if you summon it." So, what are the things that people will think about and the skills we have to develop that are at the next level of abstraction, that tap into our creativity, that tap into our curiosity? That's going to be really interesting. So, I think education is going to change dramatically, just like how progressive education in the past switch from memorization of multiplication tables into something that's a little bit more kind of higher level, higher level thinking. And I think that's going to be one of those big areas.

Lenny Rachitsky (00:16:12):
This makes me think about an NPR story I was just listening to where they were following professors using ChatGPT to create their curriculum. There was a lot of talk of students using ChatGPT, cheating, having ChatGPT write their essays. But teachers are using ChatGPT in a big way. And then students are raiding professors badly because they noticed they're using ChatGPT for their curriculum. So, it's kind of this arms race.

Peter Deng (00:16:35):
But it's also interesting because then that it goes further, it show further though. The whole system has to change. Because again, I still believe that human brains are inherently inquisitive and that we still need development in some way. But how that's going to develop, I'm fascinated to watch how that plays out.

Lenny Rachitsky (00:16:53):
I want to get back to product, but first of all, I know something that you think a lot about along these lines. This came up in many conversations I had with folks that you worked with. Is your emphasis on the power and importance of language, being really good at thinking about the words you use both in writing and speaking. Just talk about how you think about that, just the importance and power of language as a leader.

Peter Deng (00:17:14):
I remember taking this class that really stuck with me in college. It was called Language and Thought. And it was taught by Herbert Clark. And he had this thesis that kind of blew my mind, which is that, "Language actually affects the way you think." That's one of the parts of the thesis. And once I heard that and read that in his book and listened to the lecture, I couldn't stop thinking about that because it just rang so true. I grew up speaking Chinese and I think that there's a lot of things of just the Chinese language that I feel like I noticed, I thought differently when I learned English. And there were some studies around this too, I think that there's, I think in, I'm not sure exactly, I just have to go check up on this. But I think in Russian there are two different words for blue, there's a greenish blue and a bright blue or something.

Lenny Rachitsky (00:18:11):
I speak Russian but it's like... I moved to the U.S. when I was 6 and so my Russian is not great. So, I'm trying to think of this as you say it, but keep going.

Peter Deng (00:18:17):
Well, so then this is great. So, I need to get a way to validate this. But from what I remember, because there were these two different words for these different shades of blue Russian speakers who then learned English had an easier time distinguishing between these two shades of blue than, and a faster time doing so than people who had just grown up speaking English. So, I read some studies over there. And also there's some other languages that don't actually have a word for blue, I think. And then that's actually really hard for them to distinguish over time. So, that really stuck with me and I think that it's kind of rings true. So, when I, how I put it in practice, is that when I make slide decks, I gave a presentation to a class a couple of weeks ago and there were probably a total of 20 words on the entire slide deck.

(00:19:07):
And I spent hours obsessing over them because I really wanted to make sure I captured the right essence of what I was trying to say. And I think that crafting is really important when you're working in product, because if you're sitting down and you're writing a vision doc or you're writing a PRD, and if you don't pay attention to the words you use, and you're not intentional about it, those have downstream effects. People might misinterpret things, the connotations may not actually come through. And so I really am very careful about it because I think that there's a multiplicative effect and a downstream effect for using the wrong word. And I really believe in that kind of language affecting thought thesis which is why I've just really, really paid attention to that.

Lenny Rachitsky (00:19:54):
Mm-hmm. Yeah. And I feel like AI can help you with that too.

Peter Deng (00:19:56):
Yes. Exactly.

Lenny Rachitsky (00:19:56):
We had an episode-

Peter Deng (00:19:58):
Well, actually, speaking of AI, actually that's a really interesting point. I think it's really interesting and kind of poetic and fitting that the breakthrough in artificial intelligence came from large language models. It's interesting to me because there is, with every word in every sentence so much of the knowledge is encapsulated and shaped. And when ChatGPT does something really interesting, I tell people it's oftentimes just writing Python code and interpreting it. And Python is a language yet again. So, I think that there's something really interesting where like the condensation of human thought in language is related to the LLMs and the advancement scenario that we have today.

Lenny Rachitsky (00:20:41):
I think it was Ilya on a Dwarkesh's podcast where he was talking about, you may think LLMs are just like, "Oh, just predicting the next word, what's the big deal?" But in order to do that, it has to understand the universe and everything in the world that has ever happened and existed and everything anyone's ever written to predict the next word.

Peter Deng (00:21:00):
Yeah, love it.

Lenny Rachitsky (00:21:02):
Yeah. Okay. So, let me zoom out a little bit and shift a little bit to just product in general.

Peter Deng (00:21:07):
Sure.

Lenny Rachitsky (00:21:07):
You've worked at and built some of those iconic products in history. You worked at OpenAI, Facebook, Uber a Head of Product at Instagram. So, let me just ask you this question and see where this goes. What's the most counterintuitive lesson you've learned about building products or leading teams that goes against common wisdom?

Peter Deng (00:21:26):
I think one thing that, it's a really hard lesson that I learned at Uber, which is sometimes your product actually doesn't matter. And by product I mean the pixels you put on the screen or things that you build in your mobile app. And at Uber, I learned this because, it pains me to say this, but really the price and the ETA at Uber was the product. And I think a lot of times people at tech companies think of the product as just this digital manifestation, but looking at it from a holistic perspective, we humans consume the entirety of the product. And I think that was one of the things that I learned, the lessons that I learned that was really kind of hard hitting, that sometimes the pixels don't matter as much as you think. And you fix a certain bug, it's not to say that you shouldn't fix the bug, but it doesn't have as much of an impact as something that is more important to people like a price or ETA.

(00:22:29):
And this happens a lot in B2B products where it's not just about how... It's great that your product is well-loved by its end users, but does it make good business sense? Is one of those hard lessons I learned as a very bright-eyed, bushy tailed sort of design-based product manager going into Uber. I think the other insight that I had or other thought I had the other day was just the idea that so many of the tech companies today, this is kind of counterintuitive, so many of the tech companies that are most valuable today didn't really start with any technological breakthrough. They were built on some kind of technological breakthrough and they ended up building a lot more technology. But really a lot of these companies, like Facebook for example, just put in the hard work, the elbow grease, especially in the early stages, to take essentially a database of human connections and build something valuable on top of it.

(00:23:31):
And that keep on polishing and iterating that product and coming up with new ones like newsfeed and photo tagging just kind of came out of just really paying attention to what people wanted. And some of the ideas are super simple and it's not something that came out of the lab. So, Uber for example, took the fact that everyone had these GPS devices in their pockets, and they didn't invent the GPS device, but they were able to take that and the fact that people had cars, and people wanted to get around, and there was a human need, and they just connected the dots, and put everything together.

(00:24:11):
And eventually, built a ton of tech to predict the right marketplace and pricing et cetera. But largely that's a very valuable tech company. But it's largely an operations company. And I want to give a huge shout-out to my colleagues there who run Uber Eats and Uber Rides from operations perspective. Because truly that was one of the biggest business model hacks that I've seen. And so I think that it's Silicon Valley it gets lost a lot. It's like, "Oh, this is a new tech company." Oftentimes some of the most valuable ones are just the ones that are just building what people need on top of existing tech.

Lenny Rachitsky (00:24:55):
There's so much to say here. I love it. And this is coming from someone that led the Uber Rider product team and worked at Facebook and a Head of Product at Instagram. It means a lot coming from someone like you, not someone that's not in product especially.

Peter Deng (00:25:10):
Yeah, I mean, just to go further on the Instagram part, the idea was super simple. It was showing photos and visual sharing. But the craft that Mike and Kevin had in putting in the hard work to get the product just right, that's what made it really take off. That's a great example. I had forgotten about Instagram, but how could I? But it wasn't anything that any other company couldn't have done, but it was that product taste that Kevin and Mike had and conviction that there's a certain sort of vibe, if you will, that people wanted, and building that and iterating, and look at it now, it's a core part of our lives. Visual sharing, they really solved it.

Lenny Rachitsky (00:25:54):
Yeah, I just had Mike Krieger on the podcast. So, it's interesting, there's two tensions here. One is just the product doesn't matter in a lot of really successful companies. It's secondary to the cars, the drivers, the GPS and the phone. And then on the other hand, there doesn't need to be a technological breakthrough to build a huge business. It's almost like if there's no technological breakthrough, then the product matters. Facebook is an example. Basically, it's like a database of connections, but what allowed an Instagram, what allowed them to breakthrough, and there's classically competitors at the time. Was the experience, was it a lot better? And then maybe on the flip side, if the experience doesn't matter, then it's the breakthrough is on the operations and other... Does that resonate? Is that kind of what you're saying?

Peter Deng (00:26:42):
It does resonate. I think both have to be true. But also I would say that even if you did found a company that has a huge technological breakthrough. Very shortly, I think that the product experience will start mattering, because how long does that technological advantage last before humans wisen up to be like, "Well, this is not the product I want to use. I use it a little bit differently and this is more ergonomic for me?" Et cetera. So, I think that what you said is a beautiful summary. I also think that a point in time in a company's history will also determine what is going to be more important.

Lenny Rachitsky (00:27:20):
This is, especially, interesting for companies building on top of LLMs and AI infrastructure, where you're essentially saying, you don't need to have some kind of technological breakthrough to build something valuable if you can create a really special, unique experience that unlocks the potential of this super intelligence.

Peter Deng (00:27:37):
I think that's right. And I have some more thoughts on just sort of the companies that are building on top of LLMs that are just... That's a slightly different thing I would say. I think that for them, having the right data, and that right data flywheel's is so important.

Lenny Rachitsky (00:27:50):
Like proprietary data especially.

Peter Deng (00:27:52):
Exactly. And the flywheel part is just, you can start with proprietary data, but the flywheel is really just sort of how do you continue to maintain that and generate that. And the second thing is, again, it's the workflow. So, it's the ergonomics of how does it actually integrate into people's lives? And that is going to be more and more important.

Lenny Rachitsky (00:28:11):
Well, let's actually spend more time there because a lot of people are thinking about this. It feels like everybody's trying to start a company these days with AI enabling so much more. And so I think a lot of people are just curious, where should they spend time? And so I think this is actually really interesting. So, what I'm hearing here is two things to think about to create any kind of moat, defensibility against, say, foundational models coming to your lunch or in other companies. What sort of data can you acquire that is proprietary and create a flywheel to generate more of that data? And then the other piece is how do you fit into a very specific, basically, vertical that you understand really well that fits into their existing workflow? Is that...? I'm probably right.

Peter Deng (00:28:52):
Yeah. Well, it's, again, this is something we can unpack for a long time. Because with any product that you want to build, there's going to be incumbents that have distribution advantages. But I do have this thesis that there are certain-

Peter Deng (00:29:03):
... have distribution advantages, but I do have this thesis that there are certain products that will be able to break through those advantages of the distribution of the other companies, but you have to overcome a pretty high bar of your product has to be so much better. I think that's one thing.

(00:29:18):
But yeah, I think that data flywheel thing is really interesting because the models will get really good at whatever data you show it, and that's one of the things that people just think that AI is such a magic wand. But no, it's like if it's been trained on the right data, it's going to do the thing that it's been trained on. It's very malleable.

(00:29:36):
Being very mindful of the data that you have access to to start your flywheel going and what you can do to keep on going with that flywheel is going to be a critical thing for anyone who's starting a company today.

Lenny Rachitsky (00:29:50):
Let's make that even more specific. When you talk about this, I think about... The CEO of Windsurf was on the podcast and we talked a lot about how they've all this really unique data about which recommendations of code snippets people accept and reject and they actually launched their model I think based on that. Is that example? Any other examples to make this real?

Peter Deng (00:30:08):
That's a perfect example.

(00:30:10):
There's some companies I've invested in that aren't public yet that have their own take on that, which is really interesting to be able to take whatever activity is in their product to get smarter at the thing that they are doing, again, which is why I think the data flywheel and the workflow goes so hand in hand together, because if you are solving something actually valuable for businesses, for people, and there's a lot of that attention that's being paid to, a lot of work is being done through it, you're going to have that edge.

(00:30:45):
This is where I see again startups in very different markets who have this insight, who understand this very deeply, and are not just trying to zero shot everything and be like, "No, no, no. This is how we're going to build it to make the product genuinely useful so that it can get genuinely more useful over time."

(00:31:02):
That is going to be amazing because as a consumer of any of these products, we're going to benefit.

Lenny Rachitsky (00:31:08):
What I'm hearing here is also if you don't have proprietary data or unique data, you can still have a chance by building this flywheel where you collect that data through your usage.

(00:31:18):
For example, Windsurf, if they all built on Claude 3.5 and then now they have all this unique data and now they're launching their models.

Peter Deng (00:31:25):
That's exactly right.

(00:31:26):
This goes back to something I might've mentioned briefly, but you got to have grit when you're building anything. You got to be able to have that vision, have that clear direction, and be able to really go chase that. I think that's really important.

Lenny Rachitsky (00:31:38):
To make your example of distribution being overcomable, a great example I think a lot about, and we had CPO, turns out there's many CPOs at Microsoft, I didn't realize how many CPOs they had, and I asked her about, "Why didn't Copilot..." The fastest growing companies in the world, Cursor, Windsurf, Lovable, Bolt, all these guys. Copilot was so ahead of these companies and these companies broke through.

(00:32:05):
While Microsoft has distribution, amazing talent, infrastructure, all the things, early first mover advantage and it's to your point, they were just building products that were much better, Cursor, Windsurf, all these, Lovable, Bolt.

Peter Deng (00:32:17):
I do believe there is a level of product craft that will make it so that it's just worth it to switch or try something else. There are a few products out there that I see with this. I think Granola is one of them.

(00:32:31):
There's so many distribution advantages that Google Meet has, that Google, Facebook started off, Microsoft Teams has, Zoom has, but they're just these tiny little product craft delightful things that I really appreciate myself of like, "Yeah, they got it."

(00:32:50):
They have these little edges, set it down just right, and they've really figured out a way to really make it so delightful that it's like, "Yeah, I will install this piece of software. Yes, 100% I will talk to my friends about this because it is so life-changing."

(00:33:08):
We're starting to see that now. Again, before, I would say 18 months ago, it's like, "Oh, well, who has the best model?" But then coming forward, it's like really who has the best workflow and who has the best product, and we humans are just demanding. We want the best. And so when someone is going to come out and produce something that's so well-crafted, I think people are going to pay attention.

Lenny Rachitsky (00:33:28):
A couple of takeaways here is if you're trying to build an AI startup, a few things you should be thinking about that gives you a better chance of breaking through and winning is what are your data flywheels where you collect proprietary unique data, how do you build something the craft comes through and people are wowed and want to tell their friends about it.

(00:33:47):
Granola is a great example. Clearly, Cursor, Lovable, Bolt, Rep, all these guys did that and then it feels like they just understand a vertical workflow really well and someone's problem and solve that in a really unique way.

Peter Deng (00:33:59):
Yeah. I couldn't have put it better myself.

Lenny Rachitsky (00:34:01):
Awesome.

(00:34:02):
Let me ask you, this came up in my chat with Mike at Anthropic and it's along these lines. I was thinking about just what is product doing at Anthropic.

(00:34:10):
They're building this basically a gigabrain super intelligence thing that's going to know everything and maybe build its own experience in the future. And then there's this product team building this layer on top to interact with this super intelligence gigabrain.

Peter Deng (00:34:24):
What is the point? What is the value of that layer?

Lenny Rachitsky (00:34:27):
You spoke to it a bit here of just there's value in the experience and feeling native, but I guess let me just ask you that. Just where do you think product goes at a company like Anthropic, OpenAI where there's just the super intelligence that the team is working on and there's this UX on top?

Peter Deng (00:34:41):
I think those companies have just such an advantage because you get to work in the same building as the researchers. I think that there's that really symbiotic relationship, close partnership between post training and product where, again, more and more it's going to be less about the raw intelligence, it's going to be about the fine tuning of what the model can do that really resonates with people and what people want and also what the product trajectory is going to be. I think that you're going to see that more and more.

(00:35:15):
I think this is less about Anthropic but more about OpenAI. I think OpenAI made a great move.

(00:35:21):
I am a huge Fidji fan. As soon as that news leaked that she was going to join, I texted her. I was like, "This is great. Amazing. Congratulations."

(00:35:29):
I'm thrilled for her, for the company, for all of my friends still at OpenAI because it's just going to be this amazing leader coming in.

(00:35:36):
I'm also thrilled as a consumer because some great products are going to come out.

(00:35:39):
I think really that close, tight-knit relationship at any of these large model companies between post training and product is going to produce some really incredible stuff.

Lenny Rachitsky (00:35:50):
First of all, Mike actually said very similar things that the more-

Peter Deng (00:35:54):
I promise you I did not watch that podcast.

Lenny Rachitsky (00:35:56):
It hasn't even come out yet so I believe you.

(00:35:59):
Yeah. He had this interesting finding where he put product people on UX product experience front-facing product and then he put PMs on the research teams and building models, helping models get better, helping researchers build things, and he found that all the leverage and wins came from the PMs working with the researchers, much less so on the product experience. And so he puts more and more PMs with that team.

Peter Deng (00:36:25):
I'm so thrilled to hear that because that's a little bit... It's very validating because that's what we did at OpenAI too. We were very closely tied to the post training team and it was because of that tight collaboration that you see some of the advances of ChatGPT getting better at so many things. It's great. It's awesome that we independently came to the same conclusion.

Lenny Rachitsky (00:36:44):
Yes. It's a good sign.

(00:36:46):
Okay, so we're talking about startups, building new companies. I want to follow this thread a little bit.

Peter Deng (00:36:51):
Sure.

Lenny Rachitsky (00:36:52):
I feel like you've built more products from zero to one to scale than maybe most anyone else across all the companies that you've worked at. I'm going to do a quick rundown of some of the things you've done and I'm going to miss a bunch but let's see.

(00:37:06):
You built and led the Facebook Newsfeed, the current version of it. You built the new groups experience chat and messages. You shipped the Messenger app as its own app. That was one of your projects.

(00:37:16):
You led UberPool low-cost rides. You launched ChatGPT Enterprise. You shipped voice and vision, memory, custom GPTs, just refreshing the whole design of ChatGPT. Many more things.

(00:37:31):
A lot of work at Airtable obviously. Also, Oculus.

(00:37:35):
These are just some examples in the intro. I'm going to try to go through all these things.

(00:37:39):
All that to say, I feel like you've seen a lot of what works and doesn't work, building from idea from zero essentially to one to scale. So let me just ask you this question, what's an important lesson you've learned about what it takes to succeed building something from idea to one to billions?

Peter Deng (00:37:57):
Yeah. Thank you. That was a good trip down memory lane too when you read that off.

(00:38:04):
I think the first thing I would say, going from zero to one is different going from one to 100. When you are in the one to 100 phase, which is a lot of the time that I spent is the one to 100 phase, we quadruple Instagram usage in two years, that was very much a fun ride and there's a bunch of other examples at other companies.

(00:38:31):
But when you go to one to 100, I think one of the things that you really got to take into account is that you have to plan your chess moves out in advance. You have to really think before you act and build systems that are going to let you go sustainably faster, because the zero to one is you're trying to find that product market fit and then when you get to one to 100, you're trying to make sure you can get to hyperscale as fast as you can.

(00:38:59):
I've been very fortunate to be along the ride of many of these products as they were going through that hyperscale. And the analogy I always like to use is that when you do that, you feel the G-forces. Some people are like, "Oh, yeah, I'm a pilot, I can fly at 35,000 feet." But feeling the G-forces of takeoff of a rocket is very different.

(00:39:19):
One thing that I've learned there doing that a few times is you got to build the systems that help you move sustainably faster, and sometimes, you have to go slow to go fast.

(00:39:29):
Here's an example.

(00:39:31):
In building the Newsfeed, the current version that we have today, it really hasn't changed much from the time that we built it, I don't even know, it was like 12 years ago or something, I don't know the reason why it hasn't changed much.

(00:39:43):
But I like to think that it's because we put a lot of time and craft into thinking about the whole sharing loop and what are the key pieces of it and how is it architected, what's the information architecture, and what does that whole flow look like, how does it go from posting something at the top of the page to showing up in the newsfeed to someone clicking like and then that notifications thing lighting up red and then that repeating over and over again.

(00:40:11):
I like to think that Newsfeed has stood the test of time, the current version of it, because we thought very carefully about how people wanted to interact and how people wanted to consume information and also, that whole loop. When that happens, then I think things are built to last. I think this is a case at a lot of different companies.

(00:40:33):
When I was at Uber, we had a bit of a spaghetti string code situation on the writer app, but taking a step back and re-architecting things of what are the core components and how do you actually make it so that the product selector can scale around the world.

(00:40:48):
Here's a little known fact. Talk about grit and elbow grease.

(00:40:53):
Uber's not just as simple as finding a ride. If you've ever been to another country, like in India, sometimes, there are no street signs, so you have to pick up in front of this mini mart or whatever it might be. There's a whole team that worked on pickup and drop-offs. This was a large effort.

(00:41:08):
It sounds so boring but it was so critical to Uber being able to scale because pickup and drop-offs team thought about, "Well, how do you do it for venues?" That venues and finding that right abstraction means that you can have a scalable way to do pickups at airports and configure different venues.

(00:41:26):
Those systems when you take the time to build them in the one to 100 phase help you speed up massively and that's how you get 4x users in two years.

(00:41:37):
Or on Messenger, we put a lot of thought into the infrastructure around push notifications, etc. We grew that product from zero to 4.7 billion messages sent per day in about two and a half years. I think it really requires that forethought in building the right systems.

Lenny Rachitsky (00:41:56):
Let me follow that thread real quickly because that's really interesting.

(00:41:58):
Essentially, what you're saying is there's a phase of once you find product market fit, and I want to actually ask you this before you start planning, when you're starting to scale going from one to a hundred, your advice here is basically don't move fast and break things. Don't ship MVPs. This is the time to really think many chess moves ahead about what you're going to need to get this to, say, a billion users.

Peter Deng (00:42:21):
Yeah, yeah. It's building the systems and then that systems thinking will carry you really far, or at least that's been my experience and hopefully, you can find the same way but your biology may vary. But yeah, that's exactly right.

Lenny Rachitsky (00:42:34):
What's your guidance on just when to do that? Because you build something, okay, well it's working, there's also this just like, "Okay, let's just keep it going, let's scale it as far as we can." In your experience, is it... Just what's the guidance on when to really step back and really think years and years ahead?

Peter Deng (00:42:49):
Great question.

(00:42:50):
The first thing I'll say is that it's not a binary switch. It's actually a ramp rate.

(00:42:56):
When I've led teams, I've always believed strongly in this portfolio approach. Famously, Google had the 70-20-10 portfolio approach. That may be the right thing for a more mature company, maybe it's 50/50 if you're a startup, but you have to think about this in a non-binary way and in a way, that's about scaling up and when do you need to put more resources behind that.

(00:43:20):
Every startup is going to be different. Every product that you're launching is going to be different. And then thinking about your portfolio approach and how much you allocate your time that would be my advice. It's really dependent on the stage that you're in.

(00:43:35):
I think that actually is a nice dovetail to my second thing, if I may, which is when you're going from that stage of maybe one to five or one to 10, so not just fully one to 100, one thing I found to be very helpful is to measure everything.

(00:43:54):
This sounds, again, very simple but just like how you wouldn't fly a plane without instruments, why would you run your products without understanding the instrumentation and how it's doing.

(00:44:06):
One of the things I did in pretty much all the teams that I led, whether it was Instagram, Uber, Airtable, was all about... ChatGPT too.

(00:44:15):
One of the first things I did was always to build a growth team.

(00:44:19):
Building a growth team is really interesting because it actually is a simple razor, it's a simple thing to think about. It's like, "I'm going to build a growth team," but then you're going to uncover a lot of things.

(00:44:29):
You're going to uncover how much stuff you have not yet logged and how non-rigorous you've been looking at your entire product.

(00:44:38):
It's so funny because I've seen this movie so many times, the same movie so many times that every one of these companies where I remember walking into Instagram and I think asking Kevin and Mike, "So how many users do we have?" It's like, "Well, we don't really know." And so it's like, "Well, there are a lot and we don't really know."

(00:44:56):
When you build a growth team and you hire the right growth leader, I've had the pleasure of working with George Lee at Instagram, some of the early growth folks at Facebook, Andrew Chen at Uber, Airtable. I had the privilege of working with Lauryn, who is currently now leading growth at Notion. I've been very fortunate to work with some really amazing people on my team.

(00:45:20):
When you hire the right person, they start asking all the right questions because when the archetype of person who is a growth PM will be like, "Well, wait. Why is this happening? And let's get the data on X, Y and Z thing." That's when you realize you don't have X, Y, and Z thing logged and after you have X, Y, and Z thing logged, you look at the data, you're like, "Wait. Well, why is that happening?" And then you're forcing yourself to go deeper into the analysis of doing some analysis of like, "Well, what's correlated with what and what are some hypotheses?"

(00:45:49):
Because growth leaders, growth product leaders are so into this experimentation side, it actually is this really easy thing to do is when you start building a growth team, it just begets all of the right questions being asked and then it starts turning into all the right behaviors of taking something you've been building, which seems like it's working into a more rigorous system.

(00:46:12):
That's zero, sorry, the one to 10 phase I would say that really sets you up for the 10 to 100.

Lenny Rachitsky (00:46:19):
What I like about this growth team advice is that a lot of people think of a time to hire a growth team to we need to drive growth. What you're saying is there's a lot of second order benefits, which is they help you figure out what the hell's going on and inform a lot of other things that are happening, people just actually understanding how things are going.

Peter Deng (00:46:37):
Totally.

(00:46:38):
I think that the reason why growth team is the advice I would go with rather than to build an analytics team is because if you build an analytics team or a data science team, it's possible that no one's going to listen to them. It's like, "Oh, I have these insights." It's like, "Well, no one really cares."

(00:46:53):
But if you hire a growth leader, they are now tied to outcomes of driving growth, so they're going to be the ones who are listening and asking more questions and really partnering with that data science team to make your entire product and business more rigorous. That just changes the DNA of your entire team.

Lenny Rachitsky (00:47:12):
I want to talk about hiring, but is there anything else along these lines that you want to share of building new products, scaling products?

Peter Deng (00:47:19):
I guess the last thing I would say is I want to make sure that sometimes in the pursuit of numbers, product folks lose sight of the importance of taste and craft. Maybe this is actually the dovetail into building teams, but you got to have the counterbalances.

(00:47:39):
It's really important to give two people on your team different charges. One is like go grow the product and the other one is wait, maintain that design, that beautiful aesthetic, the craft that your product is known for. That tension is extremely healthy. I've seen this at Facebook. I've seen this in Instagram. I helped create this at Instagram, this healthy tension. Airtable, same thing, but just having... ChatGPT, same exact thing.

(00:48:11):
You have to have that push and pull on both sides to really stretch the gamut.

Lenny Rachitsky (00:48:16):
That begs the question, how do you actually do that? You could talk about it, you could be like, "Okay, we need to make sure the experience is awesome but also grow this number. Here's your goal." How do you operationalize that? Is it a performance review? Attribute thing? Is it culture or something else?

Peter Deng (00:48:29):
As a leader, you have to set up your team the right way. You have to really think about your team as a product and what are the various pieces you need to really stretch the gamut of what you're thinking about.

(00:48:47):
The teams that I've helped build are... The most successful ones are a team of Avengers that are just very different, have very different superpowers, but together you as the leader are the one who's helping adjudicate any differences or any disagreements but you know you're getting the best outcome when everyone's pulling and obsessing over a different thing. And that's important.

(00:49:11):
It's important to create your balance and really increase the space that you're looking at and create those healthy debates.

(00:49:20):
I think a lot of people overlook that. I think some people think of people on a team as warm bodies to do a job, but my philosophy has always been to think about, "Well, what does the company need to be successful and who's the best person who spikes at that one thing and how do I make sure that we get that person and how do we make sure we get the other person and the other person?"

(00:49:43):
It's almost like you're playing an RPG where everyone has different sliders and you have to create this super team where everyone actually spikes in different ways.

(00:49:52):
That is something that I've had a lot of success with in terms of when you create that environment and you create that vibe, you're going to get a lot of mileage out of that team.

Lenny Rachitsky (00:50:03):
That is a really interesting answer. It's not one I've heard before. Essentially, it's not create the right incentives, it's hire people that naturally see the world in a certain way and that creates a balance and a healthy tension between say a PM and a designer and an engineer.

(00:50:22):
That is really interesting because that feels a lot more sustainable than like, "Here's your goal. But also when your goal is make sure the experience is great and people support tickets are down." It's just like naturally, they need to want this to happen.

Peter Deng (00:50:34):
Totally.

(00:50:34):
Actually, I have a framework around... I think there are five different types of product managers that has held true.

(00:50:45):
This is a framework that just came out of a random jam at Uber when I was talking to some of my colleagues there. We formulated this in terms of helping with hiring practices.

(00:50:55):
Everywhere I've gone, I've also been best friends with the recruiters because honestly my whole thing is got to build the right team. So we have to really partner very deeply.

(00:51:03):
At Uber, we developed these five archetypes of a PM. To this day, I still think it's actually exactly true and it still holds true to this day, but is that interesting? You want me to go into that?

Lenny Rachitsky (00:51:19):
Absolutely. I'm so excited to hear what these are.

Peter Deng (00:51:22):
These are the five that I've found to be most enduring and actually the most different.

(00:51:27):
When you talk about... I love the way you put this, Lenny, which is when you hire the right people and they're naturally motivated by different things. These are the five that we came up.

(00:51:37):
Number one is the consumer PM. This is the person that's half designer, half product person, really obsessed over the details. "Is it delightful? Is it crafted enough? Oh my goodness, this is three pixels off. I can't stand it. This is driving me nuts. Why is this so complex?" These are the people that you think of as sometimes the criticism PM is the consumer PM, but that's just one type.

(00:52:08):
Another type, just on the other side we've talked about before, is the growth PM. These people are half data scientist, half product person, they are wired to think numbers first and they have this air about them that's like the best ones do, which is like, "I'm really skeptical. Show me the data. Let's run a test and prove it. I don't believe you." I start with these two in the framework because they're actually really different. One, it's like, "I have vibe, I feel the vibe, this is better," and the other one's like, "No. I don't believe you. We should test this and prove it." That's a really healthy tension.

(00:52:44):
I love having two people in a room debating that. I'm like, "Great. We are going to get some good things done and we're going to move the product forward."

(00:52:52):
The third type is what I call the GM PM or the business PM. These are half MBA, half product person. These are folks that are naturally wired to start with the business model and think about, "What are the margins? What are the opportunities? Where's the value being created?"

(00:53:11):
We had a lot of these at Uber and they were the marketplace PMs and they're just like...

(00:53:15):
I loved working with them because their minds just worked differently. They just thought about problems from like, "Well, what is the incentive here?" This is a fascinating type of mind to work with.

(00:53:26):
Another one I found, it's actually more nuanced than you think, is there's a certain archetype that I call the platform PM, which is someone who's really deeply wired to build tools for other people.

(00:53:42):
At Uber, we had internal platforms for messaging or for building internal tools.

(00:53:48):
Oftentimes, these folks are overlooked but it's actually a really deep wiring, because these are the people that are going to build the systems that are going to make you go faster. And that's what they love doing.

(00:53:58):
The last one, I would say, I used to call it an algorithms PM, but now in the world of AI, I'm going to rename this to research PM. These are half researcher, half engineer, half product person. These minds are amazing.

(00:54:16):
Basically, they think traditional Google search algorithm PM but nowadays, it's like who are the people who really have that product taste but deeply understand the tech and the way the models are trained to go and affect that and build the most amazing product.

(00:54:33):
Those are the five.

(00:54:34):
I still think to this day these hold true, and we might have been onto something the day that we brainstormed this at Uber but, yeah, I'm curious to hear your feedback.

Lenny Rachitsky (00:54:42):
This is great. As you're talking, I'm just like, "Here's that person, here's that person. Okay, they fit here." This super resonates.

(00:54:49):
This episode is brought to you by Contentsquare, the analytics platform that helps companies build better digital experiences.

(00:54:56):
Ever wonder why customers drop off before converting or why some pages perform better than others?

(00:55:02):
Contentsquare takes the guesswork out of digital experiences, giving you real-time insights into how users interact with your site or app. With AI-powered analytics, automatic frustration detection, and clear visualizations, you'll know exactly what's working and what's holding your customers back. Whether you're optimizing an e-commerce checkout, refining a B2B lead flow, or improving a mobile app experience, Contentsquare pinpoints exactly what needs fixing and why.

(00:55:28):
Contentsquare powers better customer journeys across 1.3 million websites and apps. Discover the insights you've been missing at contentsquare.com/lenny.

(00:55:40):
Just to summarize, there's consumer PMs, growth PMs, business/GM PMs, platform PMs and research PMs.

Peter Deng (00:55:47):
Yes.

Lenny Rachitsky (00:55:47):
A lot of people call them AI PMs now. I feel like that's the term that's really [inaudible 00:55:51] now.

Peter Deng (00:55:51):
You have to evolve with the times. Yeah.

(00:55:53):
But also the other part of the framework I find interesting is that everyone has a primary one and a secondary one.

(00:56:00):
It's like one of those personality tests. Maybe we did this just because it was hard to pigeonhole people and I myself don't think I was pigeonholable, but I do think that people lead with one type of thinking and then also have the secondary thing that keeps them in balance.

(00:56:17):
If you believe that and you apply it to your team, I'm curious to hear from your listeners if this does resonate or not. Maybe this framework will help you realize that you're missing someone that you should be not missing.

Lenny Rachitsky (00:56:31):
What was your archetype when you were a PM?

Peter Deng (00:56:35):
That's the other thing with personality types is the ones you hear. You're like, "This is me. I own this."

(00:56:39):
There's no doubt about it. I am a consumer PM and also a growth PM. That's my primarily consumer... I can't...

(00:56:48):
This is what I told you about the other products I've loved. I can see the details that people put into it and I so appreciate that. But at the end of the day, it's like, "We got to measure things." That's what I am. But again, everyone's different.

Lenny Rachitsky (00:57:03):
I love your point about how a lot of people think of PM. They hear that first example and like, "Oh, I guess that's what I need to be, because that's what everyone talks about when they're amazing product managers." But you're saying there's many other ways to be a successful PM.

(00:57:14):
We did a personality test at Airbnb when I was there, and one of the biggest takeaways was it's like this color test and you get a color green or yellow, red, and the team was all over the spectrum. It was a really good reminder just you can be a different type of person and still be really successful in this role of PM.

(00:57:32):
It's probably because of these different archetypes and different needs and roles of PMs. There's this word product manager but there's many things that PMs do.

Peter Deng (00:57:40):
Also, as an investor now, it's really important to see the fit of the founder to the market because if you put a consumer PM into a really boring regulated industry, they're probably going to get frustrated and they're probably not going to see it through. Whereas there's people that you look at the pitch and you're like, "Wow. You are really passionate about this-"

Peter Deng (00:58:03):
... pitch and you're like, "Wow, you are really passionate about this problem, and you really care about building tools for others, and this is exactly," this is the Twilio PM or whatever it might be. "You're a perfect fit for this business and that's awesome," right? So I think, yeah, I love what you just said in the summary, because I think there's no one way to be a PM, and I think this is, hopefully this framework will give people a little bit more space to express who they really are.

Lenny Rachitsky (00:58:27):
I'm curious if other functions also have these sort of archetypes, like designers and engineers, but we don't need to get into that. How about if you're listening to this on YouTube, leave a comment of which of these archetypes you think you might be. What's your primary and secondary? I'll read them again. Consumer PM, growth PM, business/GM PM, platform PM, research/AI PM?

Peter Deng (00:58:47):
Love it.

Lenny Rachitsky (00:58:47):
Okay. I want to talk about hiring. So this actually came up a lot when I was chatting with folks that you've worked with, especially Nick Turley, who's head of product at ChatGPT, who we're trying to get on the podcast. Because-

Peter Deng (00:58:57):
Yes.

Lenny Rachitsky (00:58:58):
... that's an-

Peter Deng (00:58:59):
He's awesome.

Lenny Rachitsky (00:59:00):
That's what I've heard. So he told me that the current head of engineering, the lead product engineer, the head of design and head of marketing at ChatGPT are people that you hired. Also, many of the people you hired have gone on to do incredible things. You've shared a few of those names, many of them have been on the podcast, which is the ultimate measure of success. So let me just ask you this, what's one thing you look for in people you hire that you think people sleep on, that you think people aren't paying enough attention to, that helps you find amazing stars?

Peter Deng (00:59:33):
That's really flattering to hear that from Nick. Nick is one of the best people I've worked with, period. In fact, I want to just do a quick shout out. Folks at OpenAI are pretty much the best people I've ever worked with in my career. When I took the job, I told the team, "This is going to be my last operating role, and I'm going to leave it all on the field, and I'm just going to go all out.: And basically I spent probably as much time, if not more time on recruiting and building the team as I did thinking about the product. And this is going back to what I said earlier about, I think you got to bring the right people together to have a huge impact. And oftentimes leaders overlook this and they're like, "Ah, it's just a warm body," but truly, people who have strengths in certain areas compliment others with strengths in other areas. And when you build that team, amazing things happen. It's the best investment you can make. It's going to pay off so many dividends.

(01:00:27):
So I think that's my opening salvo in terms of you got to get ... Everyone who's listening out there, you got to make sure you look at everyone in your team, you look at what you need, and you have to get the best in each. And truly, in my farewell dinner at OpenAI, I think I closed with just, "Look, I don't even know what I would do after this, because all the best people I've worked with are here." We have Ian Silber running design there, Thomas Dimson, Joey Flynn, Ryan O'Rourke. Nick Turley was an amazing I met there. Joanne, I mean I have so many people I'm missing, but Coley on product marketing, Antonow on the marketing comms side, [inaudible 01:01:07], the list goes on. Product operations is stellar. I'm so proud of, honestly, the team that I built there more than the products. So I just wanted to say that it's a big thing that I really care about, and I hope more leaders think about that too, is really be mindful of putting your team together, and thinking about that as a product. And you have to really craft that. You have to really care about the team. So-

Lenny Rachitsky (01:01:31):
Just to double down on that point, actually, before you get to the next tip here, I just love this answer, which is, if I were to ask someone, "What's your hiring vice? What do you look for that people may not be looking for enough?" Most of it would be like in that person, here's what you need to focus on, and here's the interview question. But kind of your broad answer so far is it's not actually about the person, so much as what is the team going to look like, and where do we need spikes? Where do we need to balance out the composition of this Avengers that we're building?

Peter Deng (01:02:03):
Totally, totally. That's exactly right. And so that being said, I guess I have, I guess, on brand, I have two things I want to share about hiring the right team. I have this saying, I actually have this doc that I've taken around various companies called the PXD API, which is like, "Here's how to work with me." And in it, there's a saying that I have, which is what I really optimize for for everyone that I support and everyone I hire, which is in six months, if I'm telling you what to do, I've hired the wrong person. And it's just kind of served me really well on three different levels. Number one, it's a reminder for myself when I'm either hiring, or looking for the person, is to keep my bar super high and just not settle. Because if I do, most likely in six months, it would not be true that I would be able to let this person run, and I would still be telling them what to do, which is not what I want. That is not my desire.

(01:03:07):
The second sort of effect of that is that it's ... I say that to people when they come on the team or as we're making the hire, because it communicates to them that that's my bar, and that's how they know they'll be successful, and something to kind of work towards.

(01:03:26):
And the third thing is kind of a joint thing for both of us, which is it kind of gives us, it helps me and the person operate on a different level, where the goal is not did you hit this OKR, did you hit this goal? The meta goal becomes, hey, are we calibrating enough? Are we actually getting to a spot where in six months, you're the one telling me what needs to be done? Are we getting there, right?

(01:03:55):
Because then, if that's the framing, every mistake that is made or whatever on either of our parts becomes a learning opportunity in terms of like, well, how do we grow from this to where we want to be in six months? And how is it possible that I, as a manager, can do the right things to set this person up for success, so that I don't have to be involved in six months?

(01:04:20):
And I think that those three things, and being able to have that second-order effect of this simple razor, in six months, if I'm telling you what to do, I've hired the wrong person, it puts pressure on me, it puts pressure on the person, and it creates this really interesting environment and this kind of safe space to really think about, are we heading towards that goal? And again, every place I've been at, as much as I've loved building the product, I've taken so much pride in building the team, and it's just been so much of a pleasure. And I think this is one of the two secrets that I have here.

Lenny Rachitsky (01:04:56):
This is so good. I have a follow-up question, but just to point out why I think this is so genius is that there's kind a assumption here of this person, you can trust them. So there's like, do I trust this person? Do I feel like they're going to be proactive? Do I feel like they're going to have correct insights, essentially taste and gut feeling? It's like the layer below this question, which is great. And also just this autonomy, it feels like autonomy almost implies so many important traits of somebody that you want to hire. And I love just how simple this question is for both you and them to [inaudible 01:05:35]-

Peter Deng (01:05:36):
Thank you. And really with that autonomy, I love what you said about autonomy. Because truly, as a leader, as a manager, your goal is to scale. And if this simple statement is not true, how are you able to build the best company, the best product?

Lenny Rachitsky (01:05:55):
So here's the follow-up question. Is this mostly for leaders, like say a head of product at ChatGPT, say, someone's not a CPO, they're just like, I don't know, a manager of a PM team, is there a version of this that you think might be useful to them, or is this mostly for leaders?

Peter Deng (01:06:09):
I think this is for everyone. I think it's for everyone who is a manager. Because if you're going to be a successful manager at any company, or a leader at any company, and if you're starting as a line manager, or whatnot, and you're kind of wanting to grow, or even just wanting to ... If you're early at a company, you have so much institutional knowledge. And so getting more leverage in terms of being able to pass on the wisdom that you've learned is so crucial into being successful that I think every manager should approach their reports with this. Because truly, it's just good for everyone. It's good for the company to have more kind of leverage and scale. It's good for the person who is being brought onto the team, because they know what success looks like, and it gives them a path to keep on growing. And it's great for you as a leader, as a manager, to be able to basically scale up the entire expertise of your team.

Lenny Rachitsky (01:07:17):
I imagine you don't even need to plan to not tell them what to do. It's just a good lens into, are they going to be amazing? Even if you plan to be telling them sort of what to do.

Peter Deng (01:07:31):
Yeah, exactly. The other thing is, again, in your interview process, you kind of end up looking for these insights, and you look for the behaviors of like, oh, are they actually going to be potentially able to achieve this in six months? And that's going to give you a really good lens on the picking side, not just the development side as well.

Lenny Rachitsky (01:07:47):
Peter, what's your second secret? This is one-for-one.

Peter Deng (01:07:51):
Yeah. Okay. The second one I'd say is, I feel really strongly about this, which is the area that I look for most is growth mindset. And I actually came to this some point in my management career at Facebook, where I did make a mistake and hired someone who just didn't quite have that growth mindset. And it was really difficult, because the way I say it's like, "Look, I don't have time to sugarcoat any feedback," and frankly, the best people I've worked with are the people who come into one-on-ones with me and yell at me and tell me I'm messing up. I love that, because there's nothing left unsaid, and we're able to kind of move the ball forward of, "Hey, how do we get better from this?" And I feel like growth mindset's one of those things, Lenny, that it feels really hard to teach at a certain age. And this is really important to me and my family, I expect growth mindset of myself, of my kids, my colleagues at work.

(01:08:50):
Because I think it just creates this environment where everyone is open to what's the one thing I can get better at? And that whole get 1% better every day can become true. And it's funny, whenever I go to teams like ChatGPT or Uber, when I'm always the final interview for someone in my org, and I partner with recruiting on developing the rubric, I always insist on doing the last interview. And I do ... not product sense, I don't do design, I don't do execution, I don't do metrics. I only do growth mindset.

(01:09:22):
And it's kind of like, well that's crazy. What about all of these other attributes? I'm like, "Well, I'm pretty sure I can trust the other people to assess the other attributes." But I think the growth mindset thing is so important to me, that we build a org where people are self-reflective, and want to get better, and take that feedback, and give that feedback. And it just is this meta unlock that I found to be true. And really, if you don't have growth mindset, and you're not open to feedback, and you're not open to learning, then that's the meta blocker. At that point, it's hard to get feedback, it's hard to onboard to a new skill. It's hard to develop in any sort of meaningful way. And so I found that to be the really critical piece.

Lenny Rachitsky (01:10:07):
That's a big deal what you just said there, that essentially as the CPO, head of product, big product leader at a company, your interview is not like, "Are you an amazing product manager? Do you have products taste," things like that. It's a growth mindset.

Peter Deng (01:10:24):
And I just want to clarify, it's because all the other things have been interviewed by the designer, by the engineering lead, et cetera. And that's where the previous principle comes into play as well, in terms of, I do trust my team to go and assess those people, but the one thing that I care so much about is growth mindset. And that's kind of the thing. And to be honest, I do do a little bit of a sweep. So if we got weak signal on one of those areas, I'll do it. But the pure focus of my last interview is going to be on growth mindset.

Lenny Rachitsky (01:10:54):
Okay, well I need to ask you what that looks like. But before I do, when you talk about growth mindset, I have this image of Mark Benioff on the podcast, and I asked him, just like there's so much changing all the time. It's such a crazy world to be leading a company in this world, where just, everyone's disrupting each other, AI's changing everything. It's just moving so fast, every day there's a new breakthrough, and you have to keep track, and just like, how do you deal with that? And he's like, "You should be thinking, 'Good. This is amazing. This is the best time to be building. There's so much opportunity, so exciting. This is what we want.'"

Peter Deng (01:11:30):
Exactly.

Lenny Rachitsky (01:11:30):
"Good." I just remember saying like, "Good."

Peter Deng (01:11:33):
I love that.

Lenny Rachitsky (01:11:34):
And I feel like that's the epitome of growth mindset.

Peter Deng (01:11:36):
Yep, absolutely.

Lenny Rachitsky (01:11:37):
Okay, so let me ask you just how do you tease out a strong growth mindset? What are some ways?

Peter Deng (01:11:43):
Well, good thing I'm not an operator anymore, because I'm going to give away my interview questions, so no one can cheat on this. I feel like this is another reason why this is such a great time to do this podcast. The question I asked has been the same one I've asked for years. And you can really kind suss it out from this, which is I asked them, think about one of the biggest mistakes you've made, truly, the more painful the better. And tell me what the mistake was. Describe to me the situation, and tell me actually how you actually think differently now, work differently as a result. How has that turned into a core principle of yours, et cetera.

(01:12:25):
And I give them a moment to think about it. Sometimes I even share some of my mistakes, if need be. And it's interesting, because I've asked this question so many times, I can smell the BS if they're not being authentic.

(01:12:41):
It's kind of like, "oh, I've worked too hard," or, "I did this thing." And they're really not being that ... You can tell the vulnerability that people are willing to express. And I reciprocate with that, if they ask me what mine is, I will tell them what it is. And then that's the vibe.

(01:12:56):
But what ends up happening is there's multiple reasons why this is really interesting. One, you get to get a sense of how reflective they are. And there's one woman, I was chatting with them, we actually went on for an hour, because she was just educating me on this amazing problem that she had made this mistake on, and how it changed the way that she worked, and the company worked. It was just incredible. And you can sense the passion, you can sense what's genuine. And then there are always, once in a while those things that people are just very, a little bit more defensive and not willing to open up. And it's safe. It's a one-on-one setting, so it's a safe space. And it's also, I don't think it actually selects for or against introverts or extroverts. I think at that point it's really genuine. And the second sort of order effect there is, if they end up coming on the team, you've already had that moment. You've already had that moment where you've just already said, "Hey, this is where I really messed up." And guess what? It's all okay. It's not a loss, it's a lesson. And so it just sets a different tone for your working relationship. So again, I've never A-B tested this, so I can't tell you if this actually, works or not, but I found it to be very helpful in the style that I work in, to be able to have that level of connection, whether it's with a direct report or somebody in New York.

Lenny Rachitsky (01:14:19):
What I love about this answer is it's very much like Fail Corner, which is a recurring segment on this podcast, and I might tweak Fail Corner to be even closer to this question. Okay, so let me summarize these essentially two questions that you've found to be really helpful in finding these superstars that you've hired over the years. One is you ask people in six months, "If I'm telling you what to do, I've hired the wrong person." Or I guess, how do you say it when you say it to someone? Just like, "You're probably the wrong person for this?"

Peter Deng (01:14:48):
Well, it's actually framed a little bit differently. So there's five different part of my API, or just how to work best with me. There's five attributes of people that are most successful who work with me and I love working with. And one of them is framed as that you're telling me what to do, not the other way around.

Lenny Rachitsky (01:15:09):
Six months after joining.

Peter Deng (01:15:10):
Right, right. And then I follow up with, "In six months, if I'm still telling you to do, I've hired the wrong person."

Lenny Rachitsky (01:15:15):
Got it.

Peter Deng (01:15:15):
I think, that's how I frame it.

Lenny Rachitsky (01:15:18):
Okay. By the way, you should open source this PXD API doc.

Peter Deng (01:15:24):
I would love to. I think now I got nothing to hide. I'm just like, "Here, I'm an open book." So maybe we'll do that at some point. You'll make me brave enough to do that, maybe after this podcast.

Lenny Rachitsky (01:15:33):
So you may find a link in the show notes for this podcast to the doc.

Peter Deng (01:15:36):
If I'm brave enough.

Lenny Rachitsky (01:15:37):
Okay. And then the other question you ask is, "Tell me essentially a story of when you failed, a product that you launched failed, and how that changed how you behave, how you think about product, how you operate."

Peter Deng (01:15:50):
Yeah.

Lenny Rachitsky (01:15:51):
Amazing. Okay, great. Okay, let's talk about management.

Peter Deng (01:15:56):
Sure.

Lenny Rachitsky (01:15:56):
So this came up, so I talked to a bunch of people that have worked with you, and interestingly, one of the most recurring themes, it wasn't about AI, or ... Hiring came up a bit, but it was actually mostly about how skilled you are as a manager. And this all has already come through in a lot of the things we've talked about. So I want to talk about a couple things here.

Peter Deng (01:16:14):
Sure.

Lenny Rachitsky (01:16:15):
One is someone that you worked with at OpenAI, Joanna Jang? Or is it Yang-

Peter Deng (01:16:20):
Joanne? Joanne.

Lenny Rachitsky (01:16:21):
Joanne. Joanne Jang, or Yang?

Peter Deng (01:16:24):
Yeah, Jang.

Lenny Rachitsky (01:16:24):
Jang. Okay, cool. You worked with her at OpenAI, and she shared a couple things that I think are really interesting. One is that you had a profound impact on her career by teaching her how to manage up more effectively. And you did that by teaching her a really simple phrase that she just says and uses. First of all, do you remember what that phrase is?

Peter Deng (01:16:44):
I've said a lot of stuff, and I've kind of forgotten. I tend to forget what I say, so you might have to remind me.

Lenny Rachitsky (01:16:49):
Okay, so she said "Say you'll do the thing, do the thing, say you did the thing," as a skill of managing up. So just talk about that, just the power of that and what that's all about.

Peter Deng (01:16:59):
I mean, look, I learned this from my time at Uber, from Jill who runs PR, comms, and policy there, and she used to have this saying, which is like, "Repetition doesn't spoil the prayer." It's just a natural thing where people are busy. So whether you think about managing up or even managing the entire org, if you don't repeat what your goals are, if you don't repeat what your vision is, if you don't repeat the thing that you feel strongly about what you're doing, whether it's maybe to your manager, one, I think you might lose sight of the thing that's important. And I think this is where it's a little bit about behavior. This is another language affecting thought thing. By giving this phrase to Joanne, maybe it was just like, "Hey, let's just be very intentional about what we build." That becomes a constant reminder.

(01:17:55):
And it also has this other effect, where if you're saying, "This is what I'm doing," and then that's a thing that your manager's like, "Wait, we don't need to do that anymore," you can have a conversation about that. As opposed to just doing the thing and not saying that you're doing it.

(01:18:10):
So let me take a step back. So one, say what you're going to do. And then in that exercise you're going to be able to calibrate with your manager, again, with anyone, what is it that we're going to do? And I think the words are really important here, going back to what I said earlier, so figuring out what is that goal, and crafting that to really pack the most punch and the densest of concepts. And then you're telling them that you're doing it, which that's the second phase, which is like, in your one-on-ones or in your team all hands, you're saying, "This is what we're doing."It's a great time to reaffirm you're doing or invite the conversation that this is no longer the thing to do.

(01:18:51):
And you got to tell them you did it. So just close the loop, just be like, "Okay, great, this is now done." And I think that's, again, it's one of those really pithy phrases that has so many second-order effects that are behavioral, almost. And this is a little bit of a hack in terms of helping people. It's funny that Joanne thought of it as managing up, which it is, but in my mind it's almost like this is how we operate, and this is how we're successful to stay on task, stay on goal, and be able to revisit the goals that we've set when they no longer are relevant.

Lenny Rachitsky (01:19:24):
So the phrase again is say you'll do the thing, do the thing, and then say that you did the thing.

Peter Deng (01:19:30):
Sorry, one more time. The way I would say it is, say you're going to do the thing, say that you're doing the thing, and then say that you did it.

Lenny Rachitsky (01:19:40):
This also works for presentation advice. So this came up, I don't if it was Guy Kawasaki or someone, had a very similar phrase that was for how to present well, which is tell them what you're going to tell them, tell them, and then tell them what you just told them.

Peter Deng (01:19:55):
It's possible that I might've incepted it from there. So I take no ownership over this phrase. I will just say that yes, I did repeat it.

Lenny Rachitsky (01:20:03):
This is great. And I love that this isn't just managing up advice, it's just operating advice for everyone. And there's an implication of, the last part is just make sure people know what you did, almost make sure that you get some credit, and people understand the impact you've had.

Peter Deng (01:20:19):
Which is important. I think there's a lot of people who are kind of introverted, and don't want to draw attention, and don't have the hero complex. And I think that those people tend to get lost in organizations. So if that describes you, just remember to say what you did.

Lenny Rachitsky (01:20:34):
There's another management trait that Joanne shared that I want to spend a little time on, which is you're very good at helping people understand that they can lean into their strengths, and not feel like they need to fit into a certain box. She shared that you basically helped her create almost a new role within OpenAI that wasn't even a thing before. So just maybe share that example, and then just talk about why this is important, how you think about this.

Peter Deng (01:20:56):
Well, I love that we're talking about things that Joanne are telling you, because Joanne's really special. I got to just take a moment to give her a giant shout out. She is the only person that I've worked with that has as much technical depth as she does have product taste. And I just want to pause there. It's just truly special. I feel entirely privileged to have the chance to cross paths with her at OpenAI. I learned so much from her. Again, talk about not telling you what to do after six months. She was telling me what to do from day two, and I loved it, because she was so technical, and she has this taste and those two things are very rare to find together. And with Joanne, because she was so special in that way, and I spotted that, I was like, "Wow, I've worked with so many PMs and just like, this is very unique."

(01:21:44):
It felt like we had to find a way to craft this. And sure enough, I was like, "Hey, can you just write up a job description of what is this thing? Because there's something magical here, but I don't fully understand it." I don't think any other person really thinks of things this way, and think this might be a big superpower for OpenAI. Let's codify it." And again, going back to my language being a really important thing, I think the exercise sometimes of writing things down, of things that you intuitively feel, give you an artifact that can kind of communicate with somebody else. So in this case, Joanne writing down some of the things that she got really excited about, helped me really understand that. And I was luckily in a position where I can basically say, "Look, let's create this role. Let's create this role and have you lead it. And I think this is going to be great for the product if we're able to codify it."

(01:22:43):
So I don't think I did anything special. I was just following my instincts, and just following her lead. Again, I'll be clear, I did not author that document. My recollection, she did that. So she did all the hard work in all of this thing, and I don't want to take any credit for it. The only thing I did was just gave her a little nudge of, " I think there's something here. Can you just take a moment to go and write this down?" And when she did, it was just like, "Okay, this has got to be a role and you have to be the leader for this function."

Lenny Rachitsky (01:23:11):
What is the actual role she ended up in? I think that'd be really interesting to share.

Peter Deng (01:23:12):
The role was model designer, and it was just a really interesting way that she framed it. And I know this role probably exists in some incarnation in other foundational model companies, but the way that she described it, and the things that she found to be the spikes required, led us to hire our first two model designers after running a search. And they were just perfect fits for the team. And that, I think, is largely a big secret as to why, at least, I'm biased. I love ChatGPT so much, and the way the model comes off, and the vibe of the model, is largely because of this technical plus taste role that she has created and she's leading.

Lenny Rachitsky (01:23:56):
I love one of the interesting takeaways from this is as a leader is just pay attention to what people are really, really excited about, and then take the step of, let them try to describe it very clearly in a doc. Coming back to your point about the power of language and words is just like, "Okay, tell me exactly what you're thinking and let's jam on it, because maybe there's something here."

Peter Deng (01:24:16):
Yeah.

Lenny Rachitsky (01:24:17):
Is there anything broader here about just leaning into strengths that you find just ... There's a lot of people, there's all this debate of should I just work on the things I'm terrible at and that'll make me better, or should I find the things I'm amazing at and just get better at those things? Any thoughts there?

Peter Deng (01:24:29):
I genuinely believe that fit is a two-way street. And so what you are passionate about, what your strengths are, you got to really find the right company, the right role for you. And I think there's a lot of force fitting that people want to do is to fit into a certain archetype. I'm glad we talked about the PM archetypes. Hopefully that frees people up to really lean into what they love. Because life's pretty short. It'd be great if everyone would find the thing that they really wanted to do, and be able to lean in and do that. And I think the optimist to me is also why I'm so excited about the time and age that we're in right now, because there's so many different companies popping up. So there's something that really resonates with people.

(01:25:13):
I mean, take a look at just what we're doing here, it's like, podcasting was not a thing 20 years ago. It was not a thing. But now, we are able to have these amazing tools and platforms that allow people to really express themselves, and really, what really truly brings them joy and makes them happy, and also brings a ton of value to the world. So I think that, yeah, I definitely believe in leaning in strengths, and I think that as hard as it may be, sometimes you got to look at where you are right now, and is this the thing that you really want to do? Or is there something else that's drawing your attention and drawing you towards that?

Lenny Rachitsky (01:25:52):
There's another management oriented question I want to ask you. This came from Eric Antonell, who apparently has worked with you for 17 years across a bunch of different-

Peter Deng (01:26:00):
Yeah, off and on for 17 years. One of my biggest mentors and friends, he's amazing.

Lenny Rachitsky (01:26:05):
Okay. So he's like, "You need to ask this question." So the way he put it is you've hired, managed, mentored many, many, many product people, some junior, some senior, across so many different cultures, and he's just like, "We need to learn something from your experience doing that," in terms of what you've learned about what it takes to be a really successful product person, whether it's being successful in building product or career-wise, what's just a nugget that you learned from seeing so many different types of people, and cultures, and seniority.

Peter Deng (01:26:38):
I think for a product person specifically, it's really important to obsess over the details of craft. Because ultimately, you're crafting a product. It's important to obsess about the details of craft, while simultaneously having the perspective and wisdom of which details don't actually matter. I'm going to pause there and just kind of try to-

Peter Deng (01:27:03):
I'm going to pause there and just try to unpack this a little bit because at the core of being a product person, you're like, oh, I want to build something that people love and that's the job and that's what draws people to be product people is that you have this desire to build. And I think that I've been involved in enough teams where I, myself, and when I was really young and coming up as a product person, I would just get obsessed over these little details and I realized afterwards that we've just wasted a bunch of time on something that didn't actually matter. So I think that dichotomy is somewhat interesting and beautiful to me because it capsulates both the core of what the ethos of a successful product person is, which is you really have to care and you have to give a crap about the product that you're building, but you also have to have the perspective and business know-how to understand where do you apply your time and where do you apply the care there?

(01:28:06):
And I myself feel like I've gone through cycles. Everything that I've done, I've gone super deep and really obsessed and then I take a step back and I'm like, wait, actually I was missing something and this other thing was more important, right? I'll give you an example. I'll use the Uber example here as what I said that the digital product didn't really matter and it's all about the price, the ETA, one of the products that I've built at Uber, which is Uber Reserve, right? It's the simplest of things. Going back to what I said before, sometimes the best products is the simplest of things. But the problem that we were trying to solve is that everyone has this. You have a 6 AM flight, and are you really going to wake up at 4 AM and request an Uber and hope that there's enough Ubers and the person's going to come?

(01:28:58):
Because if you do that, you're not going to sleep well and you're going to wake up every two hours and you're probably going to miss your flight anyway because you're going to fall asleep or whatever. And so there was this insight of like, okay, there's a whole mismatch between what people really want, which is the peace of mind that their car is going to be there and guess what? I'm willing to pay for that. And so we built Uber Reserve, which it was the simplest thing, which is like, oh, just go ahead and say what time your flight is and we'll work backwards or even just tell us when you want to get picked up and everything about that product we crafted what really mattered for the user, which was the peace of mind. So if you go there and you say what time your flight is and your pick-up time or whatever, I think that the product is... It hasn't changed that much since I was there.

(01:29:44):
It would tell you, oh, this is cutting it really close. You may not make your flight. It's like, wow. Again, that was put in there because of the principle of peace of mind. And on the other side it's like, well, what do drivers need? They need to know you're not going to cancel and all this other stuff. So you've got to think about the driver incentives too. So it was a simple idea, really proud of the team for figuring out all the intricate details, did some testing, and last I heard from folks internally, this is a $5 billion a year business now and one of the highest margin ones, and I'm really proud of this because it came from the idea of let's focus on what actually matters, which is that peace of mind and how many people really need it in that moment. So I think that's the best story I can tell.

Lenny Rachitsky (01:30:24):
That's an awesome story. It connects so many of the things you've talked about. One is just it may not be the product that really matters, and micro-optimizing the experience is not going to move the needle when there's something else that's more operationally oriented, but there's always going to be a product component if you're building it for freezers. The other piece that I think is interesting here is... Well, there's two. One is just it connects back to your point about the importance of autonomy of product people is just I feel like you're like, here's the team, here's what I'm told to work on. And then you're like, oh, but this thing is actually the problem we need to solve and let's just build a new product around it. And then there's a whole story I imagine of you getting buy-in and all that stuff.

(01:31:04):
The other thing this connects to, we just had the CPO of Uber, the current CPO of Uber on the podcast, and he had a few episodes before this one. It was all about dog fooding and basically exactly discovering these problems. He's done seven to 800 rides as an Uber driver to discover these problems. He had this great quote about, it's one thing to watch, just build an app for drivers sitting in your office making it look really pretty. It's another to be driving 60 miles an hour with this phone a few feet away from you trying to figure things out.

Peter Deng (01:31:34):
A hundred percent. Oh, I remember that I took two weeks off before I joined Uber. And in that time I've been obsessed with user research for the longest of times, and this is more relevant back then when you wanted to really understand how the wide massive users were using your product. And I remember I actually leased a car to drive for Uber those two weeks. So it was a little white VW something or another. I put an Uber sticker on it, I turned on the app and it just started driving and there's no better way to learn than to dog food, and I'll just build on what... Sachin is the person you had on the podcast? Yeah, he's an amazing, amazing guy. And so I'll just build on what he said there. I think that what really stuck with me in terms of framework that I learned back in school because I was brought up with the IDEO way of design thinking and I was at the design school at Stanford where before we literally were in trailers. That's how early it was.

(01:32:44):
But I remember the framework that really stuck with me is what IDEO preached, which is there are five stages to great design thinking. Number one is empathize, two is to define, three is to ideate, four is a prototype, and five is to test. And what I love about this framework, and I really hope this doesn't get lost because I don't know how much it's being preached nowadays in design thinking is that it has the right words associated with it. The first thing is empathizing. You've got to really feel the pain of your customers. It's not just about theoretically understanding what the problems are. It's really empathizing, which is why user research was so important to me is to understand that, or even like Sachin said, just taking those rides but also flying around the world. And when I was working at Uber to figure out, well, what are the various conditions?

(01:33:43):
And so empathize is a really powerful word. The define is also a really powerful word because it forces you to articulate what the problem is. And this is, again, going back to the language thing of you have to be very intentional about defining the problems that you want to solve and then ideate, we all know it's brainstorming and prototyping and tests are self-explanatory, but the first two stages I think are really insightful and it talks directly to what Sachin was saying. You've got to dog food because you really have to empathize and the great products are when you really feel the pain and you really empathize with what people are experiencing.

Lenny Rachitsky (01:34:21):
That's a great connection to another podcast episode that came to mind as you were talking, the head of product at Linear, Nan, had this really great concept that's exactly what you're saying, which is as a product person, you want to feel the pain of your customer the same way they do. You shouldn't stop asking questions to understand what they're telling you until you feel the pain that they feel and that'll help you. Basically, that's like how to operationalize empathizing. It's just do you feel the suffering?

Peter Deng (01:34:48):
Yeah, and I really do hope product people still do this to this day because I think there's so many shortcuts that if people take, you're going to miss the point, right? I still remember distinctly flying down to LA with Kevin Systrom to go do a user research study, and it was a one-way glass thing where we listened to people talk about Instagram and how they use Instagram, and there's no substitute for that. I think that to anyone out there who's doing user interviews and then saying, hey ChatGPT, summarize the takeaways, you're missing the point. You can't empathize with the summary. You have to be in the room fully immersed, no phones, just actually hearing the words and the intonation. That's how you're going to get the full color.

Lenny Rachitsky (01:35:33):
It makes me think Jeff Bezos has this great quote, if you have an anecdote and data and they're telling you different things, trust the anecdote. Oh, man. So many lessons. Okay, so to start to kind of wrap up our conversation, we covered a lot of ground, I want to ask you about Facebook real quick. So you joined Facebook very early. Eric Antonow, who I've mentioned previously, told me that it was very strange that you left Google to join Facebook at that stage. Google was killing it, on top of the world. You had such a strong career path, things were going great, but you decided to take a big leap joining Facebook. What did you see? Because I think there's something interesting here that we can learn about what you saw that may help other people decide where to go work.

Peter Deng (01:36:21):
I've always been enamored with this idea of understanding us as fundamentally human and how we're wired. And I remember at the time talking to the folks at Facebook and seeing it, and this was back when people were like, oh, this is just a college site, and that was the vibe back then. But what I saw was that the team and Mark and others really understood the fundamental human desires that people had to connect and feel lonely and to share, and they really got the right articulation of the problem they were trying to solve, which was to make the world more open and connected. And this really resonated with me because again, I study a lot in college like psychology, and I was really enamored with this idea of how are we as humans fundamentally wired? And it felt to me like a no-brainer to go work at Facebook because they saw how people were wired and how to actually build products that complement how people are wired.

(01:37:33):
And it wasn't that they were trying to force fit something into something that was unnatural. It was almost like how do we build technologies and products that actually augment our fundamental desire to stay connected? And this goes back to why I think the power of wars is so important is because you take a look at some of the mission statements for Friendster or MySpace, I don't even know if they had mission statements or what they were, they were kind of vapid and they didn't really speak to the fundamental humanity of what Facebook was striving to build and that just deeply resonated with me. And so I remember spending time with Eric being like, "Hey, what should I do? Should I take this offer from Facebook or should I stay at Google?" But ultimately it was just that deep resonance with my values of building things that were fundamentally human. And ultimately I think that for any startup out there, anyone building product, the more that you can get a good impedance match between what you're building and what humans fundamentally want and need, the more successful you're going to be.

(01:38:39):
So that's my big answer. I think the secondary answer, I've always optimized for learning in my career, and this is a huge thing that I say to a lot of people because they look at sort of like, oh, you've been at all these companies, what's your secret? I'm like, well, I've just figured out that I want to go to the place where I can learn the most. And for me, that wasn't really Google, but I had so much I wanted to learn from operating at Facebook. And at Facebook I would say, yeah, I was there for nine and a half years, but I always jumped around every two and a half or so when I feel like there was something new to learn. And that's it.

(01:39:27):
I mean, I don't know if it's a secret or not, I got lucky and I was able to have opportunities to learn different things and different skills, and that served me quite well. And regardless of any outcome, I would say that's just a great way to live your life personally is just to optimize for learning and those experiences and for me, moving to Facebook was that I saw so much learning that could have happened and it ultimately did happen. So I feel like that was a good outcome too.

Lenny Rachitsky (01:39:55):
[inaudible 01:39:55] did it. So a couple takeaways here for folks that are maybe trying to decide between a couple roles, maybe deciding if they should leave and do something new is one, are you feeling like you're learning enough/is the new place you're thinking about going to help you learn a lot more? Two, is what they're building aligned with human behavior? Almost this impedance match that you described. It feels like there's another element you shared, which is do they have a really unique insight about how things work? And also do you really care about this? Is this also how you see the world? So you're talking about a Facebook, they have this really unique insight about human behavior and that was really important to you, and so it was a really good fit.

Peter Deng (01:40:35):
A hundred percent. Yeah. I think the insight thing, thank you for summarizing that and drawing that out because it's also what I look for and what I want to partner with companies and startups now is do you have that unique insight? Are you teaching me something that I really don't know? And that usually is a good indicator of a strong point of view, and having a strong point of view is really important because there's a saying that Mike and Kevin had at Instagram which is we may not be right, but at least we're not confused. I think it's a beautiful phrase I thought because sometimes you've just got to go and do the thing that you think is right and the indecision is going to be one of the things that really gets you and bites you. So that for me is something as I look for folks who have a strong conviction, whether it's the founders I support when I go join and be an operator at the company or the founders I support in my current role.

Lenny Rachitsky (01:41:35):
That's so interesting. Tomer Cohen, the CPO of LinkedIn, that's a famous phrase that he often uses too.

Peter Deng (01:41:41):
Really?

Lenny Rachitsky (01:41:42):
So I think he borrowed it from those guys. Yeah. That was one of his mottos. We may not be right, but we're not confused.

Peter Deng (01:41:48):
Wow, I didn't know that. So I did talk him at one point. I don't remember if that's something we talked about, but again, it could just be like great minds think alike, and we just had different great folks with Mike and Kevin and Tomer feeling the same vibes.

Lenny Rachitsky (01:42:02):
I love just how many episodes this conversation has referenced. Okay, so speaking of learning, final question before we get to our very exciting lightning round, I'm going to take us to Fail Corner, which is very aligned with your growth mindset question. So the idea of this segment is people come on this podcast, they share all these amazing stories of everything's working out, I had so much success, worked at all these incredible companies, everything worked, but in reality, things don't often work out. Most people go through a lot of failed initiatives, projects, career hits, so the question is just what's a product that you built and launched that was just a big failure? And I'll ask it the way you ask it, how did that change the way you think and operate?

Peter Deng (01:42:47):
One example is, since we were talking about Instagram before, we tried to build a kind of camera first app at Instagram. It was called Bolt and it didn't work and the great levels of craft and design and the premise was essentially can we make it so it reduces the pressure to share, and you can open to a camera, you can just send some things to folks and you get some good feedback and you go from there. And it was obviously the Instagram design team, so it was top-notch. The app was designed really well. It was really fast because it's the Instagram engineering team and they were just really good at making performant mobile apps. It had all of the advantages that we had talked about that we valued at Instagram, but we launched it and I believe it was New Zealand or Australia and it didn't work.

(01:43:43):
And I remember the reason we knew this is as we were looking at sort of the retention graphs and retention is the key indicator in any product that you build, it's not the number of users, not the volume, it's actually retention and cohorted retention, you can [inaudible 01:44:00] the line and if it asymptotes, then you're in a good spot because that means that people over X period of time will continue to stay on the app and that just didn't happen. And I think the learning here was that you can really have the best team in the world with the best product taste and you can't really predict what's going to hit on the first go.

(01:44:24):
And failure is okay, you're just going to up and learn from that and nobody wallowed over that. We actually had some technology that we built there that we were able to port over to the main app, which was really helpful, but to quote the great american poet Sean Carter, "It ain't a loss, it's a lesson." And I think it's really important that you see that as a product person is that you don't see it as failure, you see it as kind of great. Now I'm that much smarter. And this is something that I've just collected. There's other examples as well, but I think this is a good example of sort of something that's somewhat counterintuitive, that you have the best team, you're going to provide those hits over and over, but sometimes you can't predict those hits and you just have to have the wisdom to be like, okay, let's see what we can learn here, see what we can save here, and then move on.

Lenny Rachitsky (01:45:20):
I absolutely remember that product in launch or heard about it, but I also don't ever think about it. And so I think it's a good reminder. Because Instagram launching a new product that's trying to rethink the way you do your camera, that's a big deal. And so I could see that being a really big deal for it not to work out. At the same time, nobody remembers that really.

Peter Deng (01:45:41):
Exactly. Yeah.

Lenny Rachitsky (01:45:43):
Peter, we've gone for two hours at this point. I feel like we could do two hours more. We'll save that for another conversation.

Peter Deng (01:45:49):
Great.

Lenny Rachitsky (01:45:50):
Before we get to our very exciting lightning round, is there anything else you either wanted to share or want to leave listeners with to maybe double down on a point you made that you think might be helpful? Otherwise, we'll just jump right in.

Peter Deng (01:46:03):
I think we should jump right in because I feel like you've extracted every little ounce of what wisdom I had here and you did a great job here just helping me remember these stories and recounting stuff, so I'm ready to jump in.

Lenny Rachitsky (01:46:17):
That's my goal, although I know there is much more that I haven't even started to tap, but with that, we reached our very exciting lightning round. Are you ready?

Peter Deng (01:46:27):
I'm ready.

Lenny Rachitsky (01:46:28):
Question one. What are two or three books that you find yourself recommending most to other people?

Peter Deng (01:46:32):
This is easy for me. Number one is Sapiens. If you're a product person, you have to understand our own humanity if you want to build products for people, straight up. That's a beautiful book. I read it before it was called Sapiens, it was called From Animals to Gods, and it was just republished in a different name, but it has really stuck with me and I remember, it's a very short, easy read, so I'd recommend that. The second book I think for product folks is a classic one, which is The Design of Everyday Things by Don Norman. This may seem outdated and old, but I promise you it's not. It really helps you understand physical product design, which is again, things that mold and shape to humanity. I think it gives you a good sense of that.

(01:47:16):
Third book is something I'm reading right now it was recommended by a friend of mine and I can't put it down. It's called The Silk Roads by Peter Frankopan. And basically this is a recounting of history through the lens of The Silk Road and the Middle East and how that's evolved. It's so fascinating because one of the things I love, Lenny, is seeing things from different perspectives. This is why travel's fun, this is why user research is fun for me, and it really helps you see the events of world history that we've all been experiencing through a very western viewpoint in a different way. And it kind of connects a bunch of things that are like, there's Western thought, there's Eastern thought, but if you see the connection between them, it's super fascinating. I'm only two, three or maybe four chapters in, but definitely something I would recommend off the bat.

Lenny Rachitsky (01:48:07):
What is a favorite recent movie or TV show that you've really enjoyed?

Peter Deng (01:48:11):
Maybe it's not as recent, but the one that always comes back to me is The Wire, HBO's The Wire. And I guess there's just so many TV shows now that I'm still processing, do I want to put it in my all-time greats? But the storytelling there and the various different sort of consistent characters, but the fact that there's the beautiful writing of The Wire is something that's unparalleled.

Lenny Rachitsky (01:48:33):
I'm now curious what's in your all-time greats list, but I'm not going to go there. We're going to keep going. What's a favorite product you've recently discovered that you really love?

Peter Deng (01:48:40):
I'm just going to go with Granola because I think that we talked about this before, but this has been a superpower for me and I have a lot of commute time now. What I do is I just do a single player mode. I go up and I start thinking about and brainstorming about sort of ideas or theses I have for investing or whatnot, and I get to where I'm going and boom, they're organized in a more cogent way and oftentimes ways that I didn't even think about articulating them. So it goes through the process of forming words, but it also helps with that assistance and I think it's a beautiful product on many different levels.

Lenny Rachitsky (01:49:17):
Wow. Granola's killing it at this category recently, and I'll give a shout-out, you get a year free of Granola if you become a yearly subscriber of my newsletter, which is not just for you, but your entire team, they gave an incredible deal.

Peter Deng (01:49:30):
Is that true? I didn't know that.

Lenny Rachitsky (01:49:31):
A hundred percent true.

Peter Deng (01:49:32):
Okay, well I'll tell you, I was not compensated for that little pitch there, that's genuine right there.

Lenny Rachitsky (01:49:36):
I'm also not compensated. Yeah. If you go to lennysnewsletter.com and click bundle, you'll see a way to get it. Love the product, use it all the time. I should be using it for these interviews and then I could have a whole summary ready to go. Okay, next question. Do you have a favorite life motto that you often come back to in work or in life?

Peter Deng (01:49:53):
Yes. This is actually something that my dad taught me. It's a saying that is in Chinese. It actually rhymes in Chinese but kind of almost rhymes in English. And it goes something like this in English which is if you move a tree, it dies, but if you move a person, he thrives. And I think it's a really interesting thing I keep on coming back to, and this goes back to why for me it's just the joy of learning and trying new experiences and being at different companies that I've been very fortunate to be at. I really think that that's how you should live life is just to kind of experience these different experiences. And it's kind of poetic to be like, yeah, unfortunately for trees, you can't really move them after a while. But for humans, I think that you move them around and we get different travel experiences and we get different life experiences when we go to different jobs, and I think that makes life really worth living.

Lenny Rachitsky (01:50:47):
I always think about what I would answer to this question, and there's a few, but one is something I always come back to when my wife and I are deciding to do something is choose adventure. Similar sentiment. Final question. So you've now moved from product leader to investor, so I just want to give you a chance to tell people what kind of stuff you're looking for. So you moved [inaudible 01:51:11] now, investing in startups. What sort of startups are you looking for? Who should reach out if they're interested in-

Peter Deng (01:51:17):
Well, I appreciate that opportunity. Look, for me, I think it's been very clear. I just love working with great people and for me, investing is just the ability to support more amazing founders. I've always been drawn to the founder archetype, like working closely with Zach or with Travis or Howie, Brendan at Oculus, and folks at Opening Eye, I think there's this amazing sort of visionary person that I love supporting in one way or another. And I've supported them mainly from the inside as a product leader, but for me it's just finding those amazing founders. In this current role, I get to work with many founders at the same time. And just two days ago I had meaningful calls, product jams with three different founders in three different industries, and that kind of keeps my mind super alive. So that's kind of why I'm doing what I'm doing now, and I would love to find some more of those amazing thought partners and people that I can just help out if I can.

Lenny Rachitsky (01:52:21):
Okay. Stage and market, anything there for folks of like, okay, he's a fit, not a fit.

Peter Deng (01:52:27):
Absolutely. So I would say early stage seed, seed plus and A is where I really get excited. I feel like I am able to help folks see the next stage. I've seen a lot of movies in my life in my career, so it's like, oh, great, I can definitely see this extrapolating out. You'd have to convince me of the future, and then it's really fun to be able to jam and help support if I can in how you scale from the one to 10 and 10 to a hundred. So that's really big.

(01:52:53):
And then in terms of what I look for it's the two things I said before, in this day and age, there's so many amazing things that's going to be built. One is do you have unique data and do you have a data flywheel? Two, do you have a really crafted workflow that you can really get after? And I guess third, do you have that insight of what product things actually matter and also which ones don't? And then how do you actually go and expand upon that? So yeah, really excited to meet a bunch more founders, whether it comes from here or somewhere else.

Lenny Rachitsky (01:53:23):
Okay, so final question and it's how do folks reach out if they want to actually talk to you about this and how can listeners be useful to you?

Peter Deng (01:53:28):
Thank you for the question. I am an introvert, so I'm really kind of silent on a lot of social media. I have accounts on X and Threads, but really I think LinkedIn is the network of choice for me. I want to be able to passively consume and learn about what's happening. How listeners can be helpful, I just want to learn. What are you all thinking about? What are some of the insights you're seeing? One of the analogies I have about AI in this day and age is that it's this really interesting new element that humanity has discovered. And what's awesome is that humanity is also very creative. And so what humanity does with this new element, I'm fascinated by, and you can tell the founders who've actually played with this element because they have this innate sense of what this thing can do and can't do, and I'm just looking to be inspired by the creativity of all you all out there.

Lenny Rachitsky (01:54:24):
Wow, that's such a cool way of thinking about it. It's going to change my perspective on AI a little bit. Peter, this was incredible. I really appreciate you taking the time to share so much wisdom. I know this is the first time you've done anything like this. I feel like this is going to help a lot of people in a lot of different ways. I feel like we covered everything I wanted to cover, so just again, thank you for-

Peter Deng (01:54:46):
Well, thank you for having me. This has been a real pleasure and hopefully some folks out there can get some learnings from this and find it useful, but that was my goal is to be able to share some things and hopefully it'll be helpful to some folks out there. So thank you. Thank you for the opportunity.

Lenny Rachitsky (01:55:00):
Thank you, Peter. Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

