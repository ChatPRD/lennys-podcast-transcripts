---
guest: Logan Kilpatrick
title: Inside OpenAI | Logan Kilpatrick (head of developer relations)
youtube_url: https://www.youtube.com/watch?v=XkMbkWG2ca4
video_id: XkMbkWG2ca4
description: 'Logan Kilpatrick leads developer relations at OpenAI, supporting developers
  building with the OpenAI API and ChatGPT. He is also on the board of directors at
  NumFOCUS, the nonprofit organization...

  '
duration_seconds: 4087.0
duration: '1:08:07'
view_count: 18284
channel: Lenny's Podcast
keywords:
- growth
- metrics
- okrs
- roadmap
- prioritization
- analytics
- conversion
- monetization
- subscription
- revenue
- hiring
- culture
- leadership
- vision
- mission
---

# Inside OpenAI | Logan Kilpatrick (head of developer relations)

## Transcript

Logan Kilpatrick (00:00:00):
Finding people who are high agency and work with urgency, if I was hiring five people today, those are some of the top two characteristics that I would look for in people because you can take on the world if you have people who have high agency and not needing to get 50 people's different consensus. They hear something from our customers about a challenge that they're having, and they're already pushing on what the solution for them is and not waiting for all the other things to happen that... People just go and do it and solve the problem, and I love that. It's so fun to be able to be a part of those situations.

Lenny (00:00:36):
Today my guest is Logan Kilpatrick. Logan is head of developer relations at OpenAI, where he supports developers building on open AI's, APIs and ChatGPT. Before OpenAI, Logan was a machine learning engineer at Apple and advised NASA on their open source policy. If you can believe it, ChatGPT launched just over a year ago and transformed the way that we think about AI and what it means for our products and our lives. Logan has been at the front lines of this change, and every day is helping developers and companies figure out how to leverage these new AI superpowers.

(00:01:10):
In our conversation, we dig into examples of how people are using ChatGPT and the new GPTs and other open AI APIs in their work and their life. Logan shares some really interesting advice on how to get better at prompt engineering. We also get into how OpenAI operates internally, how they ship so quickly, and the two key attributes they look for in the people that they hire, plus, where Logan sees the biggest opportunities for new products and new startups building on their APIs.

(00:01:38):
We also get a little bit into the very dramatic weekend that OpenAI had with the board and Sam Altman and all of that, and so much more. A huge thank you to Dan Shipper and Dennis Ing for some great questions, suggestions. With that, I bring you Logan Kilpatrick after a short word from our sponsors.

(00:01:56):
This episode is brought to you by Hex. If you're a data person, you probably have to jump between different tools to run queries, build visualizations, write Python, and send around a lot of screenshots and CSV files. Hex brings everything together. Its powerful Notebook UI lets you analyze data in SQL, Python or no code in any combination and work together with live multiplayer and version control. And now Hex's AI tools can generate queries and code, create visualizations, and even kickstart a whole analysis for you, all from natural language prompts. It's like having an analytics copilot built right into where you're already doing your work.

(00:02:34):
Then, when you're ready to share, you can use Hex's drag and drop app builder to configure beautiful reports or dashboards that anyone can use. Join the hundreds of data teams like Notion, All Trails, Loom, Mixpanel, and Algolia using Hex every day to make their work more impactful. Sign up today at hex.tech/lenny to get a 60-day free trial of the Hex team plan. That's hex.tech/lenny.

(00:02:59):
This episode is brought to you by Whimsical, the iterative product workspace. Whimsical helps product managers build clarity and shared understanding faster with tools designed for solving product challenges. With Whimsical, you can easily explore new concepts using drag and drop wire frame and diagram components, create rich product briefs that show and sell your thinking, and keep your team aligned with one source of truth for all of your build requirements. Whimsical also has a library of easy-to-use templates from product leaders like myself, including a project proposal one pager and a go to market worksheet. Give them a try and see how fast and easy it is to build clarity with whimsical. Sign up at whimsical.com/lenny for 20% off a Whimsical Pro plan. That's whimsical.com/lenny.

(00:03:52):
Logan, thank you so much for being here and welcome to the podcast.

Logan Kilpatrick (00:03:55):
Thanks for having me, Lenny. I'm super excited.

Lenny (00:03:57):
I want to start with the elephant in the room, which I think the elephant is actually leaving the room because I think this is months ago at this point, but I'm still just really curious. What was it like on the inside of OpenAI during the very dramatic weekend with the board and Sam and all those things? What was it like? And is there a story maybe you could share that maybe people haven't heard about what it was like on the inside, what was going on?

Logan Kilpatrick (00:04:20):
Yeah, it was definitely a very stressful Thanksgiving week. I think in broad context, OpenAI had been pushing for a really long time, since ChatGPT came out, and that was supposed to be one of the first weeks that the whole company had taken time away to actually reset and have a break. So very selfishly, I was super excited to spend time with my family, all that stuff. And then, yeah, Friday afternoon we got the message that all of the changes were happening, and I think it was super shocking because I think, and this is a perspective a lot of folks share, everybody had and continues to have such deep trust in Sam and Greg and our leadership team that it was just very surprising. And we're also a very, as far as company cultures go, very transparent and very open. So when there's problems or there's things going on, we tend to hear about them. And again, it was the first time that a lot of us had heard some of the things that were happening between the board and the leadership team, so very, very surprising.

(00:05:20):
I think my being someone who's not based in San Francisco, I was, again, very selfishly kind of happy that it happened over the Thanksgiving break because a lot of folks actually had gone home to different places. So it felt like I had a little bit of comfort knowing I wasn't the only one not in San Francisco, because everybody was meeting up in person to do a bunch of stuff and be together during that time. So it was nice to know that there was a few other folks who were sort of out of the loop with me.

(00:05:51):
I think the thing that surprised me the most was just how quickly everybody got back to business. I flew to San Francisco the next week after Thanksgiving, which I wasn't planning to do, to deal with the team in person and seeing, literally Monday morning, I was walking into the office being, like expecting, I don't know, something weird to be going on or happening. And really it was like people laser focused and back to work, and I think that speaks to the caliber of our team and everybody who's just so excited about building towards the mission that we're building towards. So I think that was, yeah, that was the most surprising thing of the whole incident. I think a lot of companies would've had the potential to truly be derailed for some non-trivial amount of time by this, and everybody was just right back to it, which I love.

Lenny (00:06:40):
I feel like it also maybe brought the team closer together. It feels like it was this kind of traumatic experience that may bring folks together because it was something they all shared. Is there anything along those lines that's like, "Wow, things are a little different now?"

Logan Kilpatrick (00:06:52):
One of my takeaways was I'm actually very grateful that this happened when it happened. I think today the stakes are... They're still relatively high. People have built their businesses on top of OpenAI. We have tons of customers who love ChatGPT, so if something bad happens to us, we definitely impact our customers. But on the world scale, somebody else will build a model if OpenAI disappeared and continue towards this progress of general intelligence. I think fast-forward five or 10 years, if something like this would've happened and we hadn't gone through the hopeful upcoming work transformation and all those changes that are going to happen, I think it would've been a little bit, or potentially much worse, of an outcome. So I'm glad that things happened when the stakes are a little bit lower.

(00:07:39):
And I totally agree with you. It's like the team has been growing so rapidly over the last year since I joined. It's been crazy to think about how many new folks there are, and I really think that this really brought people together because most folks, historically, many of the folks when I joined, what kind of banded us all together was the launch of ChatGPT, the launch of GPT-4, and for folks who weren't around for some of those launches, it was perhaps step day. For folks who are on for dev day, it was probably this event. So I think we've had these events that have really brought the company together cross-functionally, so hopefully all the future ones will be really exciting things like GPT five, whenever that comes, and stuff like that.

Lenny (00:08:20):
Awesome. We're going to talk about GPT-5. Going in a totally different direction, what is the most mind-blowing or surprising thing that you've seen AI do recently?

Logan Kilpatrick (00:08:31):
The things that are getting me most excited are these new interfaces around AI, like the Rabbit R-1. I don't know if you've seen that, but consumer hardware device, this company called TL Draw. I don't know if you've seen TL Draw.

Lenny (00:08:44):
I think. You sketch something and then it makes it as a website?

Logan Kilpatrick (00:08:48):
And that's only a small piece of what TL Draw is actually working on, but there's all of these new interfaces to interact with AI, and I think I was having a conversation with the TL Draw folks a couple of days ago, really blows my mind to think about how chat is the predominant way that folks are using AI today. And I actually think, and this is my bulk case for the folks at TL Draw, I'm super excited for them to build what they're building, but they're sort of building this infinite canvas experience and you can imagine how, as you're interacting with an AI on a daily basis, you might want to jump over to your infinite canvas, which the AI has filled in all the details and you might see a reference to a file and to a video and all of these different things.

(00:09:30):
And it's such a cool way. It actually makes a lot more sense for us as humans to see stuff in that type of format than, I think, just listing out a bunch of stuff in chat. So I'm really, really excited to see more people. I think 2024 is the year of multimodal AI, but it's also the year that people really push the boundaries of some of these new UX paradigms around AI.

Lenny (00:09:53):
It's funny. I feel like Chatbots, as a PM for many years, it feels like every brainstorming session we had about new features, it's like, "Hey, we should have built a Chatbot to solve this problem." It's like the perennial like, "Oh, Chatbot," or, "Someone's going to suggest we do a Chatbot," and now they're actually useful and working and everyone's building Chatbots, a lot of them based on OpenAI APIs.

(00:10:12):
There's not really a question there, but maybe the question, I was going to get to this later, is just when people are thinking about building a product like, say, TL Draw, what should they think about? Where OpenAI is not going to go versus here's what OpenAI is going to do for us. We shouldn't worry about them building a version of TL Draw in the future. What's the way to think about where you won't be disrupted essentially by OpenAI, knowing also they may change their mind?

Logan Kilpatrick (00:10:36):
That's a great question. I think we're deeply focused on these very, very general use cases like the general reasoning capabilities, the general coding, the general writing abilities. I think where you start to get into some of these very vertical applications... And I think a great example of this is actually Harvey. I don't know if you've seen Harvey, but it's this legal AI use case where they're building custom models and tools to help lawyers and people at legal firms and stuff like that. And that's a great example of our models are probably never going to be as capable as some of the things that Harvey's doing because our goal and our mission is really to solve this very general use case and then people can do things like fine-tuning and build all their own custom UI and product features on top of that.

(00:11:17):
I have a lot of empathy and a lot of excitement for people who are building these very general products today. I talk to a lot of developers who are building just general purpose assistants and general purpose agents and stuff like that. I think it's cool and it's a good idea. I think the challenge for them is they are going to end up directly competing against us in those spaces and I think there's enough room for a lot of people to be successful, but to me you shouldn't be surprised when we end up launching some general purpose agent product because, again, we're sort of building that with GPTs today and versus we're not going to launch some of these varied verticalized products. We're not going to launch an AI sales agent. That's just not what we're building towards. And companies who are and have some domain specific knowledge and they're really excited about that problem space, they can go into that and leverage our models and end up continuing to be on the cutting edge without having to do all that R&D effort themselves.

Lenny (00:12:16):
Got it. So the advice I'm hearing is get specific about use cases, and that could be either models that are tuned to be especially useful for a use case like sales or make an interface or experience solving a more specific problem.

Logan Kilpatrick (00:12:30):
And I think if you're going to try and solve this very general, if you're going to try to build the next general assistant to compete with something like ChatGPT, it has to be so radically different. People have to really be like, "Wow, this is solving these 10 problems that I have with ChatGPT, and therefore I'm going to go and try your new thing." Otherwise we're just putting a ton of engineering efforts and research effort into making that an incredible product, and it's just going to be the normal challenges of building companies. It's just hard to compete against something like that.

Lenny (00:12:59):
Awesome. Okay, that's great. I was going to get to that later, but I'm glad we touched on that. I imagine that's on the minds of many developers and founders. Kind of along the same lines, there's a lot of talk about how ChatGPT and GPTs and many of the tools you guys offer are going to make a company much more efficient. They don't need as many engineers, data scientists, PMs, things like that, but I think it's also hard for companies to think about what can we actually do to make our company more efficient. I'm curious if there's any examples that you can share of how companies have taken built a, say, a GPT internally to do something so that they don't have to spend engineering hours on it or generally just used OpenAI tooling to make their business internally more efficient?

Logan Kilpatrick (00:13:42):
Yeah, that's a great question. I wonder if you can put this in the show notes or something like that, but there's a really great Harvard Business School study about... And I forgot which consulting firm they did it with. Maybe it was like Boston Consulting or something like that, but it might've been one of the other ones. And they talk about the order of magnitude of efficiency gain for those folks who are using AI tools, I think it was chat GPT specifically in those use cases that they were using, comparatively against folks who aren't using AI. I'm really excited, also, just as just more time passes between the release of this technology, for us to get more empirical studies. I feel just for myself, as somebody who's an engineer today, I use ChatGPT and I can ship things way faster than I would be able to.

(00:14:26):
I don't have any good metrics for myself to put a specific number on it, but I'm guessing people are working on those studies right now. I think engineering is actually one of the highest leverage things that you could be using AI to do today and really unlocking, probably on the order of at least a 50% improvement, especially for some of the lower hanging fruit software engineering tasks. The models are just so capable at doing that work. And it's crazy to think... And I'm guessing, actually, GitHub probably has a bunch of really great studies they publish around copilots and you could use those as an analogy for what people are getting from ChatGPT as well. But those are probably the highest leverage things.

(00:15:07):
I think now with GPTs, people are able to go in and solve some of these more tactical problems. I think one of the general challenges with ChatGPT is it gives a decent answer for a lot of different use cases, but oftentimes it's not particular enough to the voice of your company or the nuance of the work that you're doing. And I think now with GPTs and people who are using the teams in ChatGPT and Enterprise in ChatGPT, they can actually build those things, incorporate the nuance of their own company, and make solving those tasks much, much more domain specific. So we literally just launched GPTs a couple of months ago, so I don't think there's been any good public success stories, but I'm guessing that success is happening right now at companies, and hopefully we'll hear more about that in the months to come as folks get super excited about sharing those case studies.

Lenny (00:15:58):
I'll share an example. So I have this good friend, his name's Dennis Yang, he works at Chime, and he told me about two things that they're doing at Chime that seem to be providing value. One is he built a GPT that helps write ads for Facebook and Google just gives you ideas for ads to run, and so that takes a little load off the marketing team or the growth team. And then he built another GPT that delivers experiment results, kind of like a data scientist, with here's the result of this experiment. And then you could talk to it and ask for like, "Hey, how much longer do you think we should run this for," or, "What might this imply about our product," and things like that. And I think it's really-

Logan Kilpatrick (00:15:58):
I love that.

Lenny (00:16:35):
Like you said. Is there anything else that comes to mind? Just things you've heard people do just like, "Wow, that was a really smart way of... " So I get there's engineering, co-piloting type tooling. Is there anything else that comes to mind? Just to give people a little inspiration of like, "Wow, that's an interesting way I should be thinking about using some of these tools."

Logan Kilpatrick (00:16:50):
I've seen some interesting GPTs around the planning use cases, like you want to do OKR planning for your team or something like that. I just actually saw somebody tweet it literally yesterday. I've seen some cool venture capital ones of doing diligence on a deal flow, which is kind of interesting, and getting some different perspectives. I think all of those horizontal use cases where you can bring in a different personality and get perspective on different things I think is really cool. I've personally used a GPT, the private GPT that I use myself that helps with some of the planning stuff for different quarters, and just making sure that I'm being consistent in how I'm framing things like driving back to individual metrics, stuff that, when people do planning, they often miss in our data, and then it's been super helpful for me to have a GPT to force me to think about some of those things.

Lenny (00:17:43):
Wait, can you talk more about this? What does this GPT do for you and what do you feed it?

Logan Kilpatrick (00:17:48):
Yeah, I forgot what article I saw online, but it was some article that was talking about what are the best ways to set yourself up for success in planning. And I took a bunch of the... I'll see if I can make it public after this and send you a link, but took a bunch of the examples from that and went in and put some of those suggestions into the GPT, and then now when I do any of my planning of I want to build this thing, I put it through and have it generate a timeline, generate all the specifics of what are the metrics and success that I'm looking for, who might be some important cross-functional stakeholders to include in the planning process, all that stuff, and it's been helpful.

Lenny (00:18:25):
Wow, that is very cool. That would be awesome if you made it public. And if you do, we'll link to it and we'll make it the number one most popular GPT in the store.

Logan Kilpatrick (00:18:35):
I love it.

Lenny (00:18:35):
Going in a slightly different direction, there's this whole genre of prompt engineering. It feels like it's one of these really emerging skills. I actually saw a startup hiring a prompt engineer, one of the startups I've invested in, and I think that's going to blow a lot of people's minds that there's this new job that's emerging. And I know the idea is this won't last forever, that in theory AI will be so smart you don't need to really think about how to be smart about asking it for things you need it to do. But can you just describe this idea of what is prompt engineering, this term that people might be hearing? And then even more interestingly, just what advice do you have for people to get better at writing prompts for, say, ChatGPT or through the API in general?

Logan Kilpatrick (00:19:13):
Yeah, this is such an interesting space, and I think it's another space where I'm excited for people to do more scientific empirical studies about, because there's so much gut feeling, best practices that maybe aren't actually true in a certain way. I think the reason that prompt engineering exists and comes up at all is because the models are so inclined, because of the way that they're trained, to give you just an answer to the question that you ask. Crap in crap out. If you ask a pretty basic question, you're going to get a pretty basic response. And actually the same thing is true for humans, and you can think of a great example of this. When I go to another human and I ask, "How's your day going," they say, "It's going pretty good."

(00:19:53):
Literally, absolutely zero detail, no nuance, not very interesting at all versus, again, if you have some context with a person, if you have a personal relationship with them and I ask you, "Hey Lenny, how's your day going? How did the last podcast go," et cetera, et cetera, you just have a little bit more context and agency to go and answer my question. I think this is prompt engineering.

(00:20:13):
My whole position on this is prompt engineering is a very human thing. When we want to get some value out of a human, we do this prompt engineering. We try to effectively communicate with that human in order to get the best output. And the same thing is true of models. And I think it's like, again, because we're using a system that appears to be really smart, we assume that it has all this context, but it's really like imagine a human level intelligence but literally no context. It has no idea what you're going to ask it. It's never met you before. It has no idea who you are, what you do, what your goals are. And it's the reason that you get super generic responses sometimes is because people forget they need to put that context in the model.

(00:20:57):
So I think the thing that is going to help solve this problem, and we already kind of do this in the context of Dali, so when you go to the image generation model that we have, Dali, and you say, "I want a picture of a turtle," what it does is it actually takes that description. It says, "I want a picture of a turtle," and it changes it into this high fidelity, like generate a picture of a turtle with a shell, with a green background and lily pads in the water and all this other. It adds all this fidelity because that's the way that the model is trained. It's trained on examples with super high fidelity. This will happen with text models.

(00:21:35):
You can imagine a world where you go into ChatGPT and you say, "Write me a blog post about AI." It automatically will go and be like, "Let me generate a much higher fidelity description of what this person really wants, which is generate me a blog post about AI that talks about the trade-offs between these different techniques and some example use cases and references some of the latest papers," and it does all that for you, and then you at the user will hopefully be able to be like, "Yep, this is kind of what I wanted. Let me edit this. Let me edit this here."

(00:22:02):
And again, the inherent problem is we're lazy as humans. We don't want to type all... We don't really want to type what we mean, and I think AI systems are actually going to help solve some of that problem.

Lenny (00:22:12):
So until that day, what can people do better when they're prompting, say ChatGPT? And I'll give you an example. Tim Ferris suggested this really good idea that I've been stealing, which is when you're preparing for an interview, you go to chat GPT. And so I did this for you. I was like, "Hey, I'm interviewing Logan Kilpatrick, he is head of developer relations at OpenAI, on my podcast. Give me 10 questions to ask him in the style of Tyler Cowen," who I think is the best interviewer. He is so good at just very pointed original questions. So what advice would you have for me to improve on that prompt to have better results? The questions were fine. They're great. They're interesting enough, but they weren't like, "Holy, these are incredible." So I guess what advice would you give me in that example?

Logan Kilpatrick (00:22:57):
Yeah, that's a great example where thinking in context of who it is that you're asking questions about. I'm probably not somebody who has enough information about me on the internet where the model actually has been trained and knows the nuances of my background. I think there's probably much more famous guests where it might be that there's enough context on the internet to answer the questions. You actually have to do some of that work. You need to, say if you're using browse with Bing, for example, you could say, "Here's a link to Logan's blog and some of the things that he's talked about. Here's a link to his Twitter. Go through some of his tweets, go through some of his blogs and see what his interesting perspectives are that we might want to surface on the blog," or something like that.

(00:23:36):
It's, again, giving the model enough context to answer the question. I think, again, that prompt actually might work really well for somebody who has it, if you were interviewing Tom Cruise or something like that, somebody who has a lot of information about them on the internet. It probably works a little bit better.

Lenny (00:23:52):
So the advice there is just give more context. It doesn't tell you, "Hey, I don't actually know that much about Logan, so give me some more information." It's just like, "Here you go. Here's a bunch of good questions."

Logan Kilpatrick (00:24:00):
Exactly. It wants to. It so deeply wants to answer your question. It doesn't care that it doesn't have enough context. It's the most eager person in the world you could imagine to answer the question, and without that context it's just hard to do, to give anything a value. If we got t-shirts printed, they should say, "Context is all you need. Context is the only thing that matters." It's such an important piece of getting a language model to do anything for you.

Lenny (00:24:26):
Any other tips? Just as people are sitting there, maybe they have ChatGPT open right now as they're crafting a prompt, is there anything else that you'd say would help them have better results?

Logan Kilpatrick (00:24:37):
We actually have a prompt engineering guide, which folks should go and check out. It has some of the examples. It depends on the order of magnitude of how much performance increase you can get. There's a lot of really small silly things, like adding a smiley face, increases the performance of the model. I'm sure folks have seen a lot of these silly examples, but telling the model to take a break and then answer the question, all these kinds of things. And again, if you think about it, it's because the corpus of information that's trained these models is the same things that humans have sent back and forth to each other. So you telling a human, "When I go take a break and then I come back to work, I'm fresher and I'm able to answer questions better and do work better," so very similar things are true for these models. And again, when I see a smiley face at the end of someone's message, I feel empowered that this is going to be a positive interaction and I should be more inclined to give them a great answer and spend more effort on the thing that they asked me for.

Lenny (00:25:34):
Wow, wait. So that's a real thing. If you had a smiley face, it might give you better results.

Logan Kilpatrick (00:25:39):
Again, it's like the challenge with all this stuff is it's very nuanced and it's also it's a small jump in performance. You could imagine on the order of one or 2%, which for a few sentence answer might not even be a discernible difference. Again, if you're generating an entire saga of texts, the smiley face could actually make a material difference for you, but for something small and textual it might not.

Lenny (00:26:03):
Okay, good tip. Amazing. Okay, we've talked about GPTs I think maybe might be helpful to describe what is this new thing that you guys launched, GPTs, and I'm curious just how it's going. This is a really big change and element of OpenAI now with this idea that you could build your own mini, and I'm almost explaining it, your mini open ChatGPT and then people can... I think you can pay for it. You can charge for your own GPT or is it all free right now?

Logan Kilpatrick (00:26:29):
It's ll free right now. It's all free.

Lenny (00:26:31):
Okay. In the future I imagine people will be able to charge. So there's this whole store now. Basically it's the whole app store that you guys have launched. How's it going? What's happening? What surprised you there? What should people know?

Logan Kilpatrick (00:26:42):
Yeah, it's going great, and again, historically the thing that you would have to do, let's say for example, you have a really cool ChatGPT use case, what you would have to do to share it with somebody else is actually go in and start the conversation with the model, prompt it to do the things that you wanted to, and then you would share that link with somebody else before the action has actually happened and be like, here now you can essentially finish this conversation with ChatGPT that I started.

(00:27:08):
So GPT kind of changes this where you take all that important context, you put it into the model to begin with, and then people can go and chat with essentially a custom version of ChatGPT. And the thing that's really interesting is you can upload files, you can give it custom instructions, you can add all these different tools. Like a code interpreter is built in, which allows you to do math. Essentially you have browsing built in, image generation built in. You can also, for more advanced use cases if you're a developer, you can connect it to external APIs so you can connect it to the Notion API or Gmail or all these different things, and have it actually take actions on your behalf.

(00:27:44):
So there's so many cool things that people are unlocking. And what's been most exciting to me, actually, is the non-developer persona is now empowered to go and solve these really, really, really more challenging problems by giving the model enough context on what that problem is to be able to solve it. Going back to context is all you need, this is very true in the context of GPTs, and if you give it enough context, you can solve much more interesting problems.

(00:28:11):
There's so many things that I'm excited about with this. I think monetization, when it comes to the store later this quarter, I think is going to be extremely exciting when people can get paid based on who's using their GPT. That's going to be a huge unlock and open a lot of people's eyes to the opportunity here. I also think continuing to push on making more capabilities accessible to GPTs for people who can't code is really exciting. Even for me as someone who is a software engineer, it's not super easy to connect the Notion API or the Gmail API to my GPT, and really I'd love to just be able to one click sign in with Gmail and then all of a sudden it's like my Gmail is accessible, or someone else can sign in with their Gmail and make it accessible. So I think over time all those types of things will come, but today it's really custom prompts is essentially one of the biggest value adds with GPTs.

Lenny (00:29:03):
Awesome. I have it pulled up here on different monitor and Canva has the top GPT currently, and I was trying to play with it as you're chatting just to see. I was going to make a big banner that said, "It's the context stupid," and it doesn't. I'm not doing something right, but I'm not paying that much attention to it because we're talking, but this is very cool. Just maybe a final question there. Is there a GPT that you saw someone built that was like, "Wow, that's amazing. That's so cool," something that surprised you? And I'll share one that was very cool, but is there anything that comes to mind when I ask that?

Logan Kilpatrick (00:29:33):
I think my instinct is the Zapier. All of the stuff that Zapier has done with GPTs is the most useful stuff that you could imagine. You can go so far with what... And I don't know how it's packaged for Zapier's GPT right now, but you can actually, as a third party developer, integrate Zapier without knowing how to code into your GPT. So they're pushing a lot of this stuff, and then basically all 5,000 connections that are possible with Zapier today, you can bring into your GPT and essentially enable it to do anything. So I'm incredibly excited for Zapier and for people who are building with them so many things that you can unlock using that platform. So I think that's probably the most exciting thing to me for people who aren't developers.

Lenny (00:30:20):
Awesome. Zapier's always in there, getting in there connecting things.

Logan Kilpatrick (00:30:23):
Yeah, they're great.

Lenny (00:30:25):
So the one that I had in mind, so I had a buddy of mine, [inaudible 00:30:28], who's the CEO of a company called Runway built this thing called Universal Primer which helps you learn. It's described as, "Learn everything about anything," and basically, I think, it's kind of this Socratic method of helping you learn stuff. So it's like, "Explain how transformers work in LMs," and then it just kind goes through stuff and then asks you questions, I think, and helps you learn new concepts. And I think it's the number two education GPT.

Logan Kilpatrick (00:30:53):
I love that. [inaudible 00:30:53] is incredible, so...

Lenny (00:30:54):
Yes, it's true. Let me tell you about a product called Arcade. Arcade is an interactive demo platform that enables teams to create polished, on-brand demos in minutes. Telling the story of your product is hard and customers want you to show them your product, not just talk about it or gate it. That's why Product Four teams such as Atlassian, Carta and Retool use Arcade to tell better stories within their homepages, product change logs, emails and documentation.

(00:31:23):
But don't just take my word for it. Quantum Metric, the leading digital analytics platform created an interactive product tour library to drive more prospects. With Arcade, they achieved a 2X higher conversion rate for demos and saw five times more engagement than videos. On top of that, they built the demo 10 times faster than before. Creating a product demo has never been easier. With browser-based recording Arcade is the no-code solution for building personalized demos at scale.

(00:31:50):
Arcade offers product customization options, designer approved editing tools and rich insights about how your viewers engage every step of the way. Ready to tell more engaging product stories that drive results? Head to arcade.software/lenny and get 50% off your first three months. That's arcade.software/lenny.

(00:32:11):
I want to talk about just what it's like to work at OpenAI and how the product team operates and how the company operates. So you worked at... Your two previous companies were Apple and NASA, which are not known for moving fast. And now you're at OpenAI, which is known for moving very fast, maybe too fast for some people's taste, as we saw it with the whole board thing. And so what I'm curious is just what is it that OpenAI does so well that allows them to build and ship so quickly and at such a high bar? Is there a process or a way of working that you've seen that you think other companies should try to move more quickly and ship better stuff?

Logan Kilpatrick (00:32:48):
Yeah, there's so many interesting trade-offs and all of this tension around how quickly companies can move. I think for us, again, if you think about Apple as an example, if you think about NASA as an example, just older institutions, lots of... Over time, the tendency is things slow down. There's additional checks and balances that are put in place, which drags things down a little bit. So we're young and a new company, so we don't have a lot of that institutional legacy barriers that have been put in place.

(00:33:18):
I think the biggest thing, and there's a good Sam tweet somewhere in the ether about this from, I think, 2022 or something like that, but finding people who are high agency and work with urgency is one of the most... If I was hiring five people today, those are some of the top two characteristics that I would look for in people because you can take on the world if you have people who have high agency and not needing to either get 50 people's different consensus, because you have people who you trust with high agency and they can just go and do the thing, I think, is one of the most... It is the most important thing, I'm pretty sure, if you were to distill it down.

(00:34:04):
And I see this in folks that I work with. Folks are so high agency. They see a problem and they go and tackle it. They hear something from our customers about a challenge that they're having and they're already pushing on what the solution for them is and not waiting for all the other things to happen that I think traditional companies are stuck behind because they're like, "Oh, let's check with all these seven different departments to try to get feedback on this." People just go and do it and solve the problem. And I love that. It's so fun to be able to be a part of those situations.

Lenny (00:34:35):
That is so cool. I really like these two characteristics because I haven't heard this before. Those are the two, maybe the two most important things you guys look for, high agency, high urgency. To give people a clear sense of what these actually look like when you're hiring, you shared maybe this example of customer service. Someone's hearing a bug and then going to fix it. Is there anything else that can illustrate what that looks like, high agency? And then a similar question on urgency other than just move, move, move, ship, ship, ship.

Logan Kilpatrick (00:35:01):
I think the assistants API that we released for dev day, we continue to get this feedback from developers that people wanted these higher levels of abstraction on top of our existing APIs, and a bunch of folks on the team just came together and were like, "Hey, let's put together what the plan would look like to build something like this," And then very quickly came together and actually built the actual API that now powers so many people's assistant applications that are out there. And I think that's a great example of it wasn't this top down, oh, someone's sitting there being like, "Oh, let's do these five things," and then like, "Okay, team, go and do that." It's like people really seeing these problems that are coming up and knowing that they can come together as a team and solve these problems really quickly. And I think the assistants API, and there's like 1,001 other examples of teams taking agency and doing this, but I think that's a great one at the top of my head

Lenny (00:35:55):
That makes me want to ask. Just how does planning work at OpenAI? So in this example is just like, "Hey, we think we need to build this. Let's just go and build it." I imagine there's still a roadmap and priorities and goals and things that that team had. How does road mapping and prioritization and all of that generally work to allow for something like that?

Logan Kilpatrick (00:36:14):
I think this is one of the more challenging pieces at OpenAI. There's so many. Everyone wants everything from us, and today, especially, in the world of ChatGPT and how large and well-used our API is, people will just come to us and say, "Hey, we want all of these things." I think there's a bunch of core guiding principles that we look at. One, going back to the mission, is this actually going to help us get to AGI? So there's a huge focus on there's this potential shiny reward right in front of us, which is optimize user engagement, or whatever it is. And is that really the thing? Maybe the answer is yes. Maybe that is what is going to help us get to AGI sooner, but looking at it through that lens I think is always the first step of deciding any of these problems.

(00:37:03):
I think, on the developer side, there's also these core tenets of reliability like, "Hey, it would be awesome if we had additional APIs that did all these cool things like new endpoints, new modalities, new abstractions, but are we giving customers a robust and reliable experience on our API?" And that's often the first question. And I think there have been times where we've fallen short on that, and there was a bunch of other things that we've been thinking about doing and really bringing the focus and priority back to that reliability piece because, at the end of the day, nobody cares if you have something great if they can't use it robust and reliably.

(00:37:37):
So there's these core tenets. And I think, again, we have very, other than all the principles about how we're making the decision, I think the actual planning process is pretty standard. We come together. There's H1 Q1 goals. We all sprint on those. I think the real interesting thing is how stuff changes over time. You think we're going to do these very high level things and new models, new modalities, whatever it is. And then as time goes on, there's all of this turmoil and change, and it's interesting to have mechanisms to be like, "Hey, how do we update our understanding of the world and our goals as everything the ground changes underneath of us as is happening in the craziness of the AI space today?"

Lenny (00:38:22):
It's interesting that it sounds a lot like most other companies. There's H1 planning. There's Q1 planning. Are there metrics and goals like that that you guys have OKRs or anything like that? Or is it just, Here we're going to launch these products?"

Logan Kilpatrick (00:38:33):
I think it's much higher level. I actually don't think OpenAI is a big OKR company. I don't think teams do OKRs today and I don't have a good understanding of why that's the case, whether or not. I don't even know if OKRs are still the industry. You're probably talking to a lot more folks about who are making those decisions. So I'm curious. Is that something that you're seeing from folks? Is it still common for people to do OKRs?

Lenny (00:38:55):
Yeah, absolutely. Many companies use OKRs, love OKRs. Many companies hate OKRs. I'm not surprised that OpenAI is not an OKR driven company. Along those lines, I don't know how much you can share about all this stuff, but how do you measure success for things that you launch? I know there's this ultimate goal, AGI. Is there some way to track we're getting closer? What else do you guys look at when you launch, say DPT Store or assistants or anything that's like, "Cool, that was exactly what we're hoping for." Is it just adoption?

Logan Kilpatrick (00:39:20):
Yeah, adoption is a great one. I think there's a bunch of metrics around revenue, number of developers that are building on our platform, all those things. And a lot of these, and I don't want to dive... I'll let Sam or someone else on our leadership team go more into details, but I think a lot of these are actual abstractions towards something else. Even if revenue is a goal, it's like revenue is not actually the goal. Revenue is a proxy for getting more compute, which is then actually what helps us get towards getting more GPUs so that we can train better models and actually get to the goal. So there's all these intermediate layers where even if we say something is the goal, and you hear that in a vacuum and you're like, "Oh, well OpenAI just wants to make money," and it's like, "Well, really money is the mechanism to get better models so that we can achieve our mission." And I think there's a bunch of interesting angles like that as well.

Lenny (00:40:12):
I don't know if I've heard of a more ambitious vision for a company, to build artificial general intelligence. I love that. I imagine many companies are like, "What's our version of that?" Before we leave this topic, is there anything else that you've seen OpenAI do really well that allows it to move this fast and be this successful? You talked about hiring people with higher agency and high urgency. Is there anything else that's just like, "Oh wow, that's a really good way of operating?" I imagine part of it's just hiring incredibly smart people. I think that's probably an unsaid thing, but yeah, anything else?

Logan Kilpatrick (00:40:45):
I think there's a non-trivial benefit to using Slack, and I think maybe that's controversial and maybe some people don't like Slack, but OpenAI has such a slack heavy culture and it really... The instantaneous real time communication on Slack is so crucial. And I just love being able to tag in different people from different teams and get everybody coalesced. So everybody is always on Slack, so even if you're remote or you're on a different team or in a different office, so much of the company culture is ingrained in Slack, and it allows us to really quickly coordinate where it's actually faster to send someone a Slack message sometimes than it would be to walk over to their desk because they're on Slack and they're going to be using it.

(00:41:27):
And I saw, if you saw, the recent Sam and Bill Gates interview, but Sam was talking about how Slack is his number one most used app on his phone and, "I don't even look at the time thing on my phone anymore because I don't want to know how long I'm using Slack," but I'm sure the Salesforce people are looking at the numbers and they're like, "This is exactly what we wanted."

Lenny (00:41:46):
I also love Slack. I'm a big promoter Slack. I think there's a lot of Slack hate, but such a good product. I've tried so many alternatives and nothing compares. I think what's interesting about Slack for you guys is one of the... You don't know if someone in there is just an AGI, that is not actually a person that's just there working at the company.

Logan Kilpatrick (00:42:01):
I know there are real people. There is no AGIs yet. But I think, yeah, even Slack is building a bunch of really cool AI tools, which I'm excited to... And that's why there's so much cool AI progress. And at the end of the day, it's so exciting, from being a consumer of all these new AI products. Google's a great example. I'm so happy that Google is doing really cool AI stuff because I'm a Google Docs customer and I love using Google Docs. I like a bunch of their other products, and it's awesome that people are building such useful things around these models.

Lenny (00:42:33):
How big is the OpenAI team at this point, whatever you can share? Just to give people a sense of the scale.

Logan Kilpatrick (00:42:38):
Yeah, I think the last public number was something around like 750 near the end of last year, 780 or something like that near the end of last year. And we're still growing so quickly, so I won't be the messenger to share the specific updated numbers, but the team is growing like crazy and we're also hiring across all of our engineering teams and PM teams, so folks who are interested, would love to hear from folks who are curious about joining.

Lenny (00:43:03):
Maybe one last question here. So you're growing, maybe getting to 1,000 people, clearly still very innovative and moving incredibly fast. Is there anything you've seen about what OpenAI does well to enable innovation and not slow down new big ideas?

Logan Kilpatrick (00:43:19):
Yeah, there's a couple of things, one of which is the actual research team, who seed most of the innovation that happens at OpenAI, is intentionally small. Most of the growth that OpenAI has seen is around our customer facing roles, our engineering roles to provide the infrastructure for ChatGPT and things like that. The research team is, again, intentionally kept small and there's all of this talk. And it's really interesting. I just saw this thread from one of our research folks who was talking about how in a world where you're constrained by the amount of GPU capacity that you have as a researcher, which is the case for open AI researchers, but also researchers everywhere else, each new researcher that you add is actually a net productivity loss for the research group unless that person is up-leveling everyone else in such a profound way that it increases the efficiency.

(00:44:12):
If you just add somebody who's going to go and tackle some completely different research direction, you now have to share your GPUs with that person and everyone else is now slower on their experiments. So it's a really interesting trade-off that research folks have that I don't think product folks... If I add another engineer to our API team or to some of the ChatGPT teams, you can actually write more code and do more. And that's actually a net beneficial improvement for everybody. And that's always not the case in the case of researchers, which is interesting, in A GPU constrained world, which hopefully we won't always be in.

Lenny (00:44:46):
I want to zoom out a bit and then there's going to be a couple follow-up questions here. Where are things heading with OpenAI? What's in the near future of what people should expect from the tools that you guys are going to have in launch?

Logan Kilpatrick (00:44:58):
Yeah, new modalities. I think ChatGPT continuing to push all of the different experiences that are going to be possible. Today, ChatGPT is really just text in, text out or, I guess three months ago, it was just text in, text out. We started to change that with now you can do the voice mode and now you can generate images and now you can take pictures. So I think continuing to expand the way in which you interface with AI through ChatGPT is coming.

(00:45:24):
I think GPTs is our first step towards the agent future. Again, today when you use A GPT, it's really you send a message, you get an answer back almost right away, and that's kind of the end of your interaction. I think as GPTs continue to get more robust, you'll actually be able to say, "Hey, go and do this thing and just let me know when you're done. I don't need the answer right now. I want you to really spend time and be thoughtful about this."

(00:45:48):
And again, if you think back to all these human analogies, that's what we do as humans. I don't expect somebody, when I ask them to do something meaningful for me, to do it right away and give me the answer back right away. So I think pushing more towards those experiences is what is going to unlock so much more value for people.

(00:46:06):
And I think the last thing is GPTs as this mechanism to get the next few hundred million people into ChatGPT and into AI. So I think if you've had conversations with people who aren't close to the AI space, oftentimes you talk about, even if they've heard of ChatGPT... A lot of people haven't heard of ChatGPT, but if they have, they show up in ChatGPT and they're like, "I don't really know what I'm supposed to do with this blank slate. I can kind of do anything. It's not super clear how this solves my specific problem."

(00:46:35):
But I think the cool thing about GPTs is you can package down like, "Here's this one very specific problem that AI can solve for you and do it really well," and I can share that experience with you and now you can go and try that GPT, have it actually solve the problem and be like, "Wow, it did this thing for me. I should probably spend the time to investigate these five other problems that I have to see if AI can also be a solution to those." So I think so many more people are going to come online and start using these tools because very narrow vertical tools are what's going to be a huge unlock for them.

Lenny (00:47:07):
So in that last case, a classic horizontal product problem where it does so many things and people don't know what exactly it should do for them. So that makes a ton of sense. Just being a lot more template oriented, use case specific, helping people onboard makes tons of sense. A common problem for so many SaaS products out there. The other ones you mentioned, which was really interesting, basically more interfaces to more easily interact with OpenAI voice. You mentioned audio and things like that. That makes tons of sense. And then this agents piece where the idea is, instead of just it's a chat, it's like, "Hey, go do this thing for me."

(00:47:42):
Kind of along those lines, GPT-5, we touched on this a bit. There's a lot of speculation about the much better version. People just have these wild expectations, I think, for where GPT is going. GPT-5 is going to solve all the world's problems. I know you're not going to tell me when it's launching and what it's going to do, but I heard from a friend that there's kind of this tip that when you're building products today, you should build towards a GPT-5 future, not based on limitations of GPT-4 today. So to help people do that, what should people think about that might be better in a world of GPT-5? Is it just faster? It's just smarter? Is there anything else that might be like, "Oh wow, I should really rethink how I'm approaching my product?"

Logan Kilpatrick (00:48:22):
If folks have looked through the GPT-4 technical report that we released back in March when GPT-4 came out, GPT-4 was the first model that we trained where we could reliably predict the capabilities of that model beforehand based on the amount of computes that we were going to put into it. We did a scientific study to show like, "Hey, this is what we predicted and here is what the actual outcome was." So it'll be, one I think, just as somebody who's interested in technology, but interesting to see does that continue to hold for GPT-5, and hopefully we'll some of that information whenever that model comes out.

(00:48:56):
I also think you can probably draw a few observations. One of them, which is GPT-4 came out. The consensus from the world is, "Everything is different. All of a sudden everything is different. This changes the world. This changes everything." And then slowly but surely, we come back to reality of like, "This is a really effective tool and it's going to help solve my problems more effectively."

(00:49:21):
And I think that is the, undoubtedly, the lens in which people should look at all of these model advancements, like GPT-5 is surely going to be extremely useful and solve some whole new echelon of problems. Hopefully it'll be faster. Hopefully It'll be better in all these ways, but fundamentally, the same problems that exists in the world are still going to be the same problems. You now just have a better tool to solve those problems.

(00:49:44):
And I think going back to vertical use cases, I think people who are solving very specific use cases are just now going to be able to do that much more effectively. I don't think that's going to... People have these unrealistic expectations that GPT-5 is going to be doing back flips in the background in my bedroom while it also writes all my code for me and talks on the phone with my mom or something like that.

(00:50:06):
I'm like, "That's not the case." It's just going to be this very effective tool, very similar to GPT-4, and it's also going to be become very normal very quickly. And I think that is actually a really interesting piece. If you can plan for the world where people become very used to these tools very quickly, I actually think that's an edge, and assuming that this thing is going to absolutely change everything, and in many ways I think it's actually a downside, is the wrong mental framing to have of these tools as they come out.

Lenny (00:50:39):
Kind of along these lines, you guys are investing a lot into B2B offerings. I think half the revenue, last I heard, was B2B and then half is B2C. I don't know if that's true, but that's something I heard. What is it that you get if you work with opening AI as a company, as a business? What does it unlock? Is it just called OpenAI Enterprise? What's it called and what do you get as a part of that?

Logan Kilpatrick (00:51:01):
Yeah, so I think a lot of our B2B customers are using the API to build stuff. So I think that's one angle of it. I think if you're a ChatGPT B2B customer, we sell Teams, which is the ability to get multiple subscriptions of ChatGPT packaged together. We also have an enterprise version of ChatGPT. There's a bunch of enterprise-y things that enterprise companies want, around SSO and stuff like that, related to ChatGPT Enterprise.

(00:51:25):
I think the coolest thing is actually being able to share some of these prompt templates and GPTs internally. So again, you can make custom things that work really well for your company with all of the information that's relevant to solving problems at your company and share those internally. And to me, that's like you want to be able to collaborate with your teammates on the cool things you create using AI. So that's a huge unlock for companies. I think that those are the two biggest value adds. There's higher limits and stuff like that on some of those models, but I think being able to share your very domain specific applications is the most useful thing.

Lenny (00:52:00):
I think if you're a company listening and you think a lot of employees are using ChatGPT, basically the simplest thing you could do is just roll it up into a business account with single sign-on and that probably saves you money and makes it easier to coordinate and administer.

Logan Kilpatrick (00:52:14):
Yeah, there's also a bunch of security stuff too, like if you want to control. You don't want people to use certain GPTs from the GPT store because you're worried about security or privacy and stuff like that. You don't want your private data going in places. It makes a lot of sense to sign up for that so that you have a little bit more control over what's happening.

Lenny (00:52:29):
Okay, got it. There's a launch happening tomorrow, I think, after we're recording this. Can you talk about what is new, what's coming out? I think this is going to come out a couple weeks after recording, but just what should people know that's new that's coming out from OpenAI tomorrow in our world?

Logan Kilpatrick (00:52:45):
Yeah, updated, so there's a few different things. A couple of quick ones are updated GPT-4 Turbo model, updated the preview model that we released that dev day. There's an updated version of that. It fixes this, if folks have seen online people talking about this sort of laziness phenomenon in the model. We improve on that and it fixes a lot of the cases where that was the case. So hopefully the model will be a little bit less lazy. The big thing is the third generation embeddings model. So we were talking off-camera before recording about all of the cool use cases for embedding. So if folks have used embeddings before, it's essentially the technology that powers many of these question and answering with your own documentation or your own corpus of knowledge. And like you were saying, you actually have a website where people can ask questions about recordings of the podcast.

Lenny (00:53:34):
Lennybot.com. Check it out.

Logan Kilpatrick (00:53:35):
Yeah, lennybot.com. And my assumption was that lennybot.com is actually powered by embedding. So you take all of the corpus of knowledge. You take all the recordings, your blog post. You embed them, and then when people ask questions, you can actually go in and see the similarity between the question and the corpus of knowledge and then provide an answer to somebody's question and reference an empirical fact, something that's true from your knowledge base. And this is super useful and people are doing a ton of this. It's like trying to ground these models in reality, in what they know to be true. We know all the things from your podcast to be at least something that you've said before and to be true in that sense, and we can bring them into the answer that the model is actually generating in response to a question. So that'll be super cool.

(00:54:20):
And these new V3 embeddings models, again, state-of-the-art performance, the cool thing is actually the non-English performance has increased super significantly. I think historically, people really were only using embeddings for... It only worked really well for English, and I think now you can use it across so many new languages because it's just so much more performant across those languages and it's five times cheaper as well, which is wonderful. There's no better feeling than making things cheaper for people. I love it. I think now it's like you can embed, I'm pretty sure, it was like 62,000 pages of text for $1, which is very, very cheap. So lots of really cool things that you can do with embeddings and exciting to see people invent more stuff.

Lenny (00:55:07):
What a deal. Final question before we get to a very exciting lightning round. Say you're a product manager at a big company, or even a founder, what do you think are the biggest opportunities for them to leverage the tech that you guys are building, GPT-4, all the other APIs? How should people be thinking about, "Here's how we should really think about leveraging this power in our existing product," or new product, whichever direction you want to go.

Logan Kilpatrick (00:55:34):
Yeah, I think going back to this theme of new experiences is really exciting to me. I think consumers are just going to be... You are going to have an edge on other people if you're providing AI that's not accessible in a Chatbot. People are using a ton of chat and it's a really valuable service area. It's clearly valuable because people are using it. But I think products that move beyond this chat interface really are going to have such an advantage. And also, thinking about how to take your use case to the next level. I've tried a ton of chat examples that are very, very basic and providing a little bit of value to me, but I'm like, "Really this should go much further and actually build your core experience from the ground up."

(00:56:20):
I've used this product that allows you to essentially manage or view the conversations that are happening online around certain topics and stuff like that. So I can go and look online. What are people saying about GPT-4? And what I just said out loud, "What are people saying about GPT-4," is the actual question that I have. And in a normal product experience today, I have to go into a bunch of dashboards and change a bunch of filters and stuff like that. And what I really want is just ask my question. What are people doing? What are people saying about GPT-4? Get an answer to that question in a very data grounded way.

(00:56:55):
And I've seen people solve part of this problem where, oh, they'll be like, "Oh, well here's a few examples of what people are saying and, well, that's not really what I want. I want this summary of what's happening." And I think it just takes a little bit more engineering effort to make that happen. But I think it's like that is the magical unlock of like, "Wow, this is an incredible product that I'm going to continue to use," instead of like, "Yeah, this is kind of useful, but I really want more."

Lenny (00:57:21):
Awesome. I'll give a shout-out to a product. I'm not an investor, but I know the founder, called visualelectric.com, which I think is doing exactly this. It's basically a tool specifically built for creatives, I think specifically graphic design, to help them create imagery. So there's like Dali, obviously, but this takes it to a whole new level where it's kind of this canvas, infinite canvas, that you could just generate images, edit, tweak them, and continue to rate until you have the thing that you need. Visualelectric.com.

Logan Kilpatrick (00:57:48):
I'm going to try that out. Is it similar to Canva?

Lenny (00:57:50):
It's even more niche, I think, for more sophisticated graphic design, I think, is the use case. But I'm not a designer, so I'm not the target customer. But I will say my wife is a graphic designer. She had never used AI tools. I showed her this and she got hooked on it. She paid for it without even telling me that she was going to become a paid customer, and she created imagery of our dog and all this art. And now it's like on our TV. The art she created is now sitting... It's like we have a frame TV, and that's the image on our TV. So anyway...

Logan Kilpatrick (00:58:21):
I love that. What was it called again?

Lenny (00:58:23):
Visualelectric.com. Anyway, anything else you wanted to touch on or share before we get to a very exciting lightning round?

Logan Kilpatrick (00:58:31):
I've made this statement a few times online and other places, but for people who have cool ideas that they should build with AI, this is the moment. There are so many cool things that need to be built for the world using AI. And again, if I or other folks on the team at OpenAI can be helpful in getting you over the hump of starting that journey of building something really cool, please reach out. The world needs more cool solutions using these tools, and would love to hear about the awesome stuff that people are building.

Lenny (00:59:01):
I would've asked you this at the end, but how would people reach out? What's the best way to actually do that?

Logan Kilpatrick (00:59:06):
Twitter, LinkedIn. My email should be findable somewhere. I don't want to say it and then get slammed with a bunch of email. You should be able to sign my email, if you need it, online somewhere. But yeah, Twitter and LinkedIn is usually the easiest place.

Lenny (00:59:18):
And how do they find you on Twitter?

Logan Kilpatrick (00:59:21):
It's just Logan Kilpatrick, or I think my name shows up as Logan.GPT or-

Lenny (00:59:21):
Logan.GPT?

Logan Kilpatrick (00:59:26):
Or official Logan K.

Lenny (00:59:28):
Yeah. Awesome. Okay. And we'll link into it in the show notes. Amazing. Well Logan, with that, we've reached a very exciting lightning round. Are you ready?

Logan Kilpatrick (00:59:34):
I'm ready.

Lenny (00:59:35):
First question, what are two or three books that you've recommended most to other people?

Logan Kilpatrick (00:59:39):
I think the first one is one that I read a long time ago and came back to recently, is the One Room Schoolhouse by Sal Khan. Incredible. Yeah, I don't want... It's the lightning round so I won't say too much, but incredible story and AI is what is going to enable Sal Khan's vision of a teacher per student to actually happen. So I'm really excited about that. And the other one is, that I always come back to, is Why We Sleep. Sleep science are so cool. If you don't care about your sleep, it's one of the biggest up-levels that you can do for yourself.

Lenny (01:00:14):
What is a favorite recent movie or TV show that you really enjoyed?

Logan Kilpatrick (01:00:18):
I'm a sucker for a good inspirational human story. So I watched, with my family recently over the holidays, this Gran Turismo movie, and it's a story about someone who, a kid from London, who grew up doing SIM racing, which is a virtual race car, and did this competition, ended up becoming a real professional race car driver through some competition. And it's just really cool to see someone go from driving a virtual car to driving a real car and competing in the 24-hour Le Mans and all that stuff.

Lenny (01:00:50):
I used to play that game and it was a lot of fun, but I don't think I have any clue how to drive a real car, race car. So that's inspiring. Do you have a favorite interview question that you'd like to ask candidates that you're interviewing?

Logan Kilpatrick (01:01:03):
Yeah, I'm always curious to hear what people's... The thing that they so strongly believe that people disagree with them on.

Lenny (01:01:12):
What do you look for in an answer that seems like, Wow, that's a really good signal?"

Logan Kilpatrick (01:01:17):
Oftentimes, it's just an entertaining question to ask in some sense, but it's also... It's interesting to see what somebody's deeply held strong belief is, I think. And not to judge whether or not I believe in that, but just curious to see why people feel that way.

Lenny (01:01:35):
What is a favorite product that you've recently discovered that you really like?

Logan Kilpatrick (01:01:38):
On the narrative of sleep, I have this really nice sleep mask from this company called... Not being paid. I just say this, but it's called Manta Sleep or something like that. It's a weighted sleep mask and it feels incredible when I... I don't know. Maybe I just have a heavy head or something like that, but it feels good to wear a weighted sleep mask at night. I really appreciate it.

Lenny (01:02:01):
I have a competing sleep mask that I highly recommend. I'm trying to find it. I've emailed people about it a couple of times in my newsletter for gift guides.

Logan Kilpatrick (01:02:09):
Yeah.

Lenny (01:02:09):
Okay. My favorite is called the Waoaw Sleep Mask, W-A-O-A-

Logan Kilpatrick (01:02:15):
What do you like about it?

Lenny (01:02:16):
W-A-O-A-W. I'll link to it in the show notes. It makes a lot of room. It's very large and there's space for your eyes, so your eyelashes and whatever eyes aren't pressed on, and it just fits really nicely around the head. And my wife, we both wear eye masks at night. It just, speaking of sleep, really helps us sleep. [inaudible 01:02:37] It doesn't have the weight-ness piece, so it might be worth trying, but everyone I've recommended this to is like, "That changed my life. Thank you for helping me sleep better." And so we'll link to [inaudible 01:02:51].

Logan Kilpatrick (01:02:17):
Look at that.

Lenny (01:02:50):
Look at us. So adult. Two more questions. Do you have a favorite life motto that you often come back to share with friends or family, either in work or in life?

Logan Kilpatrick (01:02:58):
Yeah, I've got it. It's on a Post-It note that I... Right behind my camera and it's "Measure in hundreds." I love this idea of measuring things in hundreds, and it's for folks who are at the beginning of some journey. I talk to people all the time, they're like, "Yeah, I've tried this thing and it hasn't worked." And if your mental model is to measure in hundreds, "I measure in hundreds," the five times that you failed at something, you failed and tried zero times. And I love that. It's such a great reminder that everything in life is built on compounding and multiple attempts at stuff. And if you don't try enough times, you're never going to be successful at it.

Lenny (01:03:38):
I love that. I could see why you are successful at OpenAI and why you're a good fit there. Final question. So I asked ChatGPT for a very silly question. "Give me a bunch of silly questions to ask Logan Kilpatrick, head of developer relations at OpenAI," and I went through a bunch. I have three here, but I'm going to pick one. If an AI started doing standup comedy, what do you think would be its go-to joke or funny observation about humans?

Logan Kilpatrick (01:04:06):
I think today, I think if you were to do this, I think the go-to question would be something along the, "So an AI walks into a bar," and likely because, again, it's trained on some distribution of training data, and that's the most common joke that comes up, and that's probably... I wonder if you came up with a joke right now, whether or not that would show up in one of the examples.

Lenny (01:04:31):
I love it. What would be the joke though? We need the joke. We need the punchline. I'm just joking. I know you can't come up with amazing-

Logan Kilpatrick (01:04:37):
That's what we have ChatGPT for.

Lenny (01:04:41):
We're already irrelevant. Amazing. Logan, thank you so much for being here. Two final questions, even though you've already shared this information, but just for folks to remind them. Where can folks find you if they want to reach out and ask you more questions? And how can listeners be useful to you?

Logan Kilpatrick (01:04:55):
Yeah, Twitter and LinkedIn, Logan Kilpatrick or Logan.GPT on Twitter. Please shoot me messages. I get a ton of DMs from people and it's always really, really interesting stuff. I think the thing that I would love to have help on is if people find bugs and things that don't work well in ChatGPT, I oftentimes see people be like, "This thing didn't work really well." And the key, and I think we as OpenAI need to do a better job of messaging this to people, but having shared chats or actual, tangible, reproducible examples, are the two things that we need in order to actually fix the problems that people have. The model laziness was a good example where it was hard to figure out what was going on because people would be like, "Oh, the model's lazier," but it's hard to figure out what were the prompts they were using. What was the examples, all that stuff? So send those examples as you come up on things that don't work well and we'll make stuff better for you.

Lenny (01:05:49):
Amazing. And I'll also just remind people, if you're listening to this and you're like, "Oh, okay, cool. A lot of cool ideas for OpenAI and ChatGPT," what you need to do is actually just go to chat.openai.com and try this stuff out. There's a lot of just theorizing, but I think once you actually start doing it, you start to see things a little differently. And at this point, every day I'm in there doing something, like asking for ideas for questions, doing research on a newsletter post, and it's just a tab I'm always coming back to. And I know there's a lot of people just talking about this sort of thing, and I just want to remind people. Just go. Sign in. Play with it. Ask it questions on something you're working on and just see how it goes and keep coming back to it. Is there anything else you want to share along those lines to inspire people to give this a shot?

Logan Kilpatrick (01:06:34):
I love it. I think the phrase of people being worried about humans being replaced by AI, and I've seen this narrative online, that it's not AI that's going to replace humans. It's other humans that are being augmented and using AI tools that are going to be more competitive in a job market and stuff like that. So go and try these AI tools. This is the best time to learn. You're going to be more productive and empowered in your job and the things that you're excited about. So yeah, excited to see what people use ChatGPT for.

Lenny (01:07:01):
And then you can expense your account. I think it's 10 or 20 bucks a month. A lot of companies are paying for this for you, so ask your boss if you can just have it expensed and make sure you use the latest version. Anyway, Logan, thank you again so much for being here.

Logan Kilpatrick (01:07:16):
This is awesome, Lenny. Thanks for having me in. Thoughtful questions. Hopefully those weren't all from ChatGPT.

Lenny (01:07:20):
Nope, only the last one. I did have a bunch of others I had in the belt or in the pocket. I don't know what the metaphor is. In the back pocket, that's the metaphor, but I did not get to them because we had enough great stuff. So no, that was all me. Human AI.

Logan Kilpatrick (01:07:35):
Thank you.

Lenny (01:07:36):
Thanks, Logan.

Logan Kilpatrick (01:07:37):
Lenny.ai.

Lenny (01:07:39):
I love it. Lennybot.com, check it out. Okay, thanks Logan. Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

