---
guest: Hamel Husain & Shreya Shankar
title: Why AI evals are the hottest new skill for product builders | Hamel Husain
  & Shreya Shankar
youtube_url: https://www.youtube.com/watch?v=BsWxPI9UM4c
video_id: BsWxPI9UM4c
description: Hamel Husain and Shreya Shankar teach the world’s most popular course
  on AI evals and have trained over 2,000 PMs and engineers (including many teams
  at OpenAI and Anthropic). In this conversatio...
duration_seconds: 6393.0
duration: '1:46:33'
view_count: 79329
channel: Lenny's Podcast
keywords:
- acquisition
- metrics
- analytics
- management
- vision
- market
- persona
- design
- ux
- ui
- prototype
- user experience
- startup
- platform
- ai
---

# Why AI evals are the hottest new skill for product builders | Hamel Husain & Shreya Shankar

## Transcript

Lenny Rachitsky (00:00:00):
To build great AI products, you need to be really good at building evals. It's the highest ROI activity you can engage in.

Hamel Husain (00:00:05):
This process is a lot of fun. Everyone that does this immediately gets addicted to it. When you're building an AI application, you just learn a lot.

Lenny Rachitsky (00:00:12):
What's cool about this is you don't need to do this many, many times. For most products, you do this process once and then you build on it.

Shreya Shankar (00:00:18):
The goal is not to do evals perfectly, it's to actionably improve your product.

Lenny Rachitsky (00:00:23):
I did not realize how much controversy and drama there is around evals. There's a lot of people with very strong opinions.

Shreya Shankar (00:00:28):
People have been burned by evals in the past. People have done evals badly, so then they didn't trust it anymore, and then they're like, "Oh, I'm anti evals."

Lenny Rachitsky (00:00:36):
What are a couple of the most common misconceptions people have with evals?

Hamel Husain (00:00:39):
The top one is, "We live in the age of AI. Can't the AI just eval it?" But it doesn't work.

Lenny Rachitsky (00:00:45):
A term that you used in your posts that I love is this idea of a benevolent dictator.

Hamel Husain (00:00:49):
When you're doing this open coding, a lot of teams get bogged down in having a committee do this. For a lot of situations, that's wholly unnecessary. You don't want to make this process so expensive that you can't do it. You can appoint one person whose taste that you trust. It should be the person with domain expertise. Oftentimes, it is the product manager.

Lenny Rachitsky (00:01:09):
Today, my guests are Hamel Husain and Shreya Shankar. One of the most trending topics on this podcast over the past year has been the rise of evals. Both the chief product officers of Anthropic and OpenAI shared that evals are becoming the most important new skill for product builders. And since then, this has been a recurring theme across many of the top AI builders I've had on. Two years ago, I had never heard the term evals. Now it's coming up constantly. When was the last time that a new skill emerged that product builders had to get good at to be successful?

(00:01:41):
Hamel and Shreya have played a major role in shifting evals from being an obscure, mysterious subject to one of the most necessary skills for AI product builders. They teach the definitive online course on evals, which happens to be the number one course on Maven. They've now taught over 2,000 PMs and engineers across 500 companies, including large swaths of the OpenAI and Anthropic teams along with every other major AI lab.

(00:02:07):
In this conversation, we do a lot of show versus tell. We walk through the process of developing an effective eval, explain what the heck evals are and what they look like, address many of the major misconceptions with evals, give you the first few steps you can take to start building evals for your product, and also share just a ton of best practices that Hamel and Shreya have developed over the past few years. This episode is the deepest yet most understandable primer you'll find on the world of evals. And honestly, it got me excited to write evals, even though I have nothing to write evals for. I think you'll feel the same way as you watch this.

(00:02:41):
If this conversation gets you excited, definitely check out Hamel and Shreya's course on Maven. We'll link to it in the show notes. If you use the code LENNYSLIST when you purchase the course, you'll get 35% off the price of the course. With that, I bring you Hamel Husain and Shreya Shankar.

(00:02:58):
This episode is brought to you by Fin, the number one AI agent for customer service. If your customer support tickets are piling up, then you need Fin. Fin is the highest-performing AI agent on the market with a 65% average resolution rate. Fin resolves even the most complex customer queries. No other AI agent performs better. In head-head bake-offs with competitors, Fin wins every time. Yes, switching to a new tool can be scary, but Fin works on any help desk with no migration needed, which means you don't have to overhaul your current system or deal with delays in service for your customers.

(00:03:31):
And Fin is trusted by over 5,000 customer service leaders and top AI companies like Anthropic and Synthesia. And because Fin is powered by the Fin AI engine, which is a continuously improving system that allows you to analyze, train, test, and deploy with ease, Fin can continuously improve your results too. So if you're ready to transform your customer service and scale your support, give Fin a try for only 99 cents per resolution. Plus, Fin comes with a 90-day money-back guarantee. Find out how Fin can work for your team at fin.ai/lenny. That's fin.ai/lenny.

(00:04:05):
This episode is brought to you by Dscout. Design teams today are expected to move fast, but also to get it right. That's where Dscout comes in. Dscout is the all-in-one research platform built for modern product and design teams. Whether you're running usability tests, interviews, surveys, or in-the-wild fieldwork, Dscout makes it easy to connect with real users and get real insights fast. You can even test your Figma prototypes directly inside the platform. No juggling tools, no chasing ghost participants. And with the industry's most trusted panel plus AI-powered analysis, your team gets clarity and confidence to build better without slowing down. So if you're ready to streamline your research, speed up decisions, and design with impact, head to dscout.com to learn more. That's dscout.com. The answers you need to move confidently. Hamel and Shreya, thank you so much for being here, and welcome to the podcast.

Hamel Husain (00:05:04):
Thank you for having us.

Shreya Shankar (00:05:05):
Yeah, super excited.

Lenny Rachitsky (00:05:07):
I'm even more excited. Okay, so a couple years ago, I had never heard the term evals. Now it's one of the most trending topics on my podcast, essentially, that to build great AI products, you need to be really good at building evals. Also, it turns out some of the fastest-growing companies in the world are basically building and selling and creating evals for AI labs. I just had the CEO of Mercor on the podcast. So there's something really big happening here. I want to use this conversation to basically help people understand this space deeply, but let's start with the basics. Just what the heck are evals? For folks that have no idea what we're talking about, give us just a quick understanding of what an eval is, and let's start with Hamel.

Hamel Husain (00:05:49):
Sure. Evals is a way to systematically measure and improve an AI application, and it really doesn't have to be scary or unapproachable at all. It really is, at its core, data analytics on your LLM application and a systematic way of looking at that data, and where necessary, creating metrics around things so you can measure what's happening, and then so you can iterate and do experiments and improve.

Lenny Rachitsky (00:06:22):
So that's a really good broad way of thinking about it. If you go one level deeper just to give people a very, even more concrete way of imagining and visualizing what we're talking about, even if you have a example to show would be even better, what's an even deeper way of understanding what an eval is?

Hamel Husain (00:06:36):
Let's say you have a real estate assistant application and it's not working the way you want. It's not writing emails to customers the way you want, or it's not calling the right tools, or any number of errors. And before evals, you would be left with guessing. You would maybe fix a prompt and hope that you're not breaking anything else with that prompt, and you might rely on vibe checks, which is totally fine.

(00:07:11):
And vibe checks are good and you should do vibe checks initially, but it can become very unmanageable very fast because as your application grows, it's really hard to rely on vibe checks. You just feel lost. And so evals help you create metrics that you can use to measure how your application is doing and kind of give you a way to improve your application with confidence. That you have a feedback signal in which to iterate against.

Lenny Rachitsky (00:07:44):
So just to make very real, so imagining this real estate agent, maybe they're helping you book a listing or go see an open house. The idea here is you have this agent talking to people, it's answering questions, pointing them to things. As a builder of that agent, how do you know if it's giving them good advice, good answers? Is it telling them things that are completely wrong?

(00:08:04):
So the idea of evals, essentially, is to build a set of tests that tell you, how often is this agent doing something wrong that you don't want it to do? And there's a bunch of ways you could define wrong. It could be just making up stuff. It could be just answering in a really strange way. The way I think about evals, and tell me if this is wrong, just simply is like unit tests for code. You're smiling. You're like, "No, you idiot."

Shreya Shankar (00:08:29):
No, that's not what I was thinking.

Lenny Rachitsky (00:08:31):
Okay. Okay, okay, tell me. Tell me, how does that feel as a metaphor?

Shreya Shankar (00:08:35):
Okay. I like what you said first, which is we had a very broad definition. Evals is a big spectrum of ways to measure application quality. Now, unit tests are one way of doing this. Maybe there are some non-negotiable functionalities that you want your AI assistant to have, and unit tests are going to be able to check that. Now, maybe you also, because these AI assistants are doing such open-ended tasks, you kind of also want to measure how good are they at very vague or ambiguous things like responding to new types of user requests or figuring out if there's new distributions of data like new users are coming and using your real estate agent that you didn't even know would use your product. And then all of a sudden, you think, "Oh, there's a different way you want to kind of accommodate this new group of people."

(00:09:24):
So evals could also be a way of looking at your data regularly to find these new cohorts of people. Evals could also be like metrics that you just want to track over time, like you want to track people saying, "Yes. Thumbs up. I liked your message." You want very, very basic things that are not necessarily AI-related but can go back into this flywheel of improving your product. So I would say, overall, unit tests are a very small part of that very big puzzle.

Lenny Rachitsky (00:09:56):
Awesome. You guys actually brought an example of an eval just to show us exactly what the hell we're talking about. We're talking in these big ideas. So how about let's pull one up and show people, "Here's what an eval is."

Hamel Husain (00:10:06):
Yeah, let me just set the stage for it a little bit. So to echo what Shreya said, it's really important that we don't think of evals as just tests. There's a common trap that a lot of people fall into because they jump straight to the test like, "Let me write some tests," and usually that's not what you want to do. You should start with some kind of data analysis to ground what you should even test, and that's a little bit different than software engineering where you have a lot more expectations of how the system is going to work. With LLMs, it's a lot more surface area. It's very stochastic, so you kind of have a different flavor here.

(00:10:47):
And so the example I'm going to show you today, it's actually a real estate example. It's a different kind of real estate example. It's from a company called Nurture Boss. I can share my screen to show you their website just to help you understand this use case a little bit, so let me share my screen. So this is a company that I worked with. It's called Nurture Boss, and it is a AI assistant for property managers who are managing apartments, and it helps with various tasks such as inbound leads, customer service, booking appointments, so on and so forth. It's like all the different sort of operations you might be doing as a property manager, it helps you with that. And so you can see kind of what they do. It's a very good example because it has a lot of the complexities of a modern AI application.

(00:11:40):
So there's lots of different channels that you can interact through the AI with like chat, text, voice, but also, there's tool calls, lots of tool calls for booking appointments, getting information about availability, so on and so forth. There's also RAG retrieval, getting information about customers and properties and things like that. So it's pretty fully fleshed in terms of an AI application. And so they have been really generous with me in allowing me to use their data as a teaching example. And so we have anonymized it, but what I'm going to walk through today is, okay, let's do the first part of how we would start to build evals for Nurture Boss. Why would we even want to do that?

(00:12:36):
So let's go through the very beginning stage, what we call error analysis, which is, let's look at the data of their application and first start with what's going wrong. So I'm going to jump to that next, and I'm going to open an observability tool. And you can use whatever you want here. I just happen to have this data loaded in a tool called Braintrust, but you can load it in anything. We don't have a favorite tool or anything in the blog post that we wrote with you. We had the same example but in Phoenix Arize, and I think Aman, on your blog post, used Phoenix Arize as well. And there's also LangSmith. So these are kind of like different tools that you can use.

(00:13:29):
So what you see here on the screen, this is logs from the application, and let me just show you how it looks. So what you see here is, and let me make it full screen, this is one particular interaction that a customer had with the Nurture Boss application, and what it is is a detailed log of everything that happened. So it's called a trace, and it's just the engineering term for logs of a sequence of events. The concept of a trace has been around for a really long time, but it's especially really important when it comes to AI applications.

(00:14:12):
And so we have all the different components and pieces and information that the AI needs to do its job, and we are logged all of it and we're looking at a view of that. And so you see here a system prompt. The system prompt says, "You are an AI assistant working as a leasing team member at Retreat at Acme Apartments." Remember, I said this is anonymized, so that's why the name is Acme Apartments. "Your primary role is to respond to text messages from both current residents and prospective residents. Your goal is to provide accurate, helpful information," yada, yada, yada. And then there's a lot of detail around guidelines of how we want this thing to behave.

Lenny Rachitsky (00:14:56):
Is this their actual system prompt, by the way, for this company?

Hamel Husain (00:14:58):
It is. Yes, it is.

Lenny Rachitsky (00:14:58):
Amazing. That's so cool.

Hamel Husain (00:14:59):
It's a real system prompt.

Lenny Rachitsky (00:15:01):
That's amazing because it's rare you see a actual company product's system prompt. That's like their crown jewels a lot of times, so this is actually very cool on its own.

Hamel Husain (00:15:08):
Yeah. Yeah, it's really cool. And you see all of these different sort of features that are different use cases, so things about tour scheduling, handling applications, guidance on how to talk to different personas, so on and so forth. And you can see the user just kind of jumps in here and asks, "Okay, do you have a one-bedroom with study available? I saw it on virtual tours." And then you can see that the LLM calls some tools. It calls this get individual's information tool, and it pulls back that person's information. And then it gets the community's availability. So it's querying a database with the availability for that apartment complex.

(00:16:01):
And then finally, the AI responds, "Hey, we have several one-bedroom apartments available, but none specifically listed with a study. Here are a few options."

(00:16:12):
And then it says, "Can you let me know when one with a study is available?"

(00:16:16):
And then it says, "I currently don't have specific information on the availability of a one-bedroom apartment."

(00:16:23):
User says, "Thank you."

(00:16:25):
And the AI says, "You're welcome. If you have any more questions, feel free to reach out." Now, this is an example of a trace, and we're looking at one specific data point. And so one thing that's really important to do when you're doing data analysis of your LLM application is to look at data. Now, you might wonder, "There's a lot of these logs. It's kind of messy. There's a lot of things going on here. How in the hell are you supposed to look at this data? Do you want to just drown in this data? How do you even analyze this data?"

(00:17:07):
So it turns out there is a way to do it that is completely manageable, and it's not something that we invented. It's been around in machine learning and data science for a really long time, and it's called error analysis. And what you do is, the first step in conquering data like this is just to write notes. Okay? So you got to put your product hat on, which is why we're talking to you, because product people have to be in the room and they have to be involved in sort of doing this. Usually a developer is not suited to do this, especially if it's not a coding application.

Lenny Rachitsky (00:17:47):
And just to mirror back, why I think you're saying that is because this is the user experience of your product. People talking to this agent is the entire product essentially, and so it makes sense for the product person to be super involved in this.

Hamel Husain (00:17:59):
Yeah. So let's reflect on this conversation. Okay, a user asked about availability. The AI said, "Oh, we don't really have that. Have a nice day." Now, for a product that is helping you with lead management, is that good? Do you feel like this is the way we want it to go?

Lenny Rachitsky (00:18:30):
Not ideal.

Hamel Husain (00:18:32):
Yes, not ideal, and I'm glad you said that. A lot of people would say, "Oh, it's great. The AI did the right thing. It looked, it said, 'We didn't have available,' and it's not available." But with your product hat on, you know that's not correct. And so what you would do is you would just write a quick note here. You would say, "Okay." You might pop in here, and you can write a note. So every observability application has ability to write notes, and you wouldn't try to figure out if something is wrong. In this case, it's kind of not doing the right thing, but you just write a quick note, "Should have handed off to a human."

Lenny Rachitsky (00:19:19):
And as we watch this happening, it's like you mention this and you'll explain more. You're doing this, this feels very manual and unscalable, but as you said, this is just one step of the process and there's a system to this. That was just the first one.

Hamel Husain (00:19:30):
Yeah, and you don't have to do it for all of your data. You sample your data and just take a look, and it's surprising how much you learn when you do this. Everyone that does this immediately gets addicted to it and they say, "This is the greatest thing that you can do when you're building an AI application." You just learn a lot and you're like, "Hmm, this is not how I want it to work. Okay." And so that's just an example.

(00:19:58):
So you write this note, and then we can go on to the next trace. So this is the next trace. I just pushed a hot key on my keyboard. Let me go back to looking at it.

Lenny Rachitsky (00:20:09):
And these tools make it easy to go through a bunch and add these notes quickly.

Hamel Husain (00:20:13):
Yes. And so this is another one. Similar system prompt. We don't need to go through all of it again. We'll just jump right into the user question. "Okay, I've been texting you all day." Isn't that funny? And the user says, "Please." Okay, yeah, this one is just like an error in the application where this is a text message application, sorry, the channel through which the customer is communicating is through text message, and you're just getting really garbled. And you can see here that it kind of doesn't make sense. The words are being cut off like, "In the meantime," and then the system doesn't know how to respond, because you know how people text message, they write short phrases. They split their sentence across four or five different turns. So in this case-

Lenny Rachitsky (00:21:16):
Yeah, so what do you do with something like that?

Hamel Husain (00:21:18):
Yeah, so this is a different kind of error.

Lenny Rachitsky (00:21:19):
Mm.

Hamel Husain (00:21:19):
This is more of, "Hey, we're not handling this interaction correctly. This is more of a technical problem," rather than, "Hey, the AI is not doing exactly what we want." So we would write that down too.

Lenny Rachitsky (00:21:20):
Which is still really cool.

Hamel Husain (00:21:20):
Yeah.

Lenny Rachitsky (00:21:31):
It's amazing you're catching that, too, here. Otherwise, you'd have no idea this was happening.

Hamel Husain (00:21:35):
Yeah, you might not know this is happening, right? And so you would just say, "Okay." You would write a note like, "Oh, conversation flow is janky because of text message."

Lenny Rachitsky (00:21:51):
And I like that, I like that you're using the word janky. It shows you just how informal this can be at this stage.

Hamel Husain (00:21:56):
Yeah, it's supposed to be chill. Just don't overthink it. And there's a way to do this. So the question always comes up, how do you do this? Do you try to find all the different problems in this trace? What do you write a note about? And the answer is, just write down the first thing that you see that's wrong, the most upstream error. Don't worry about all the errors, just capture the first thing that you see that's wrong, and stop, and move on. And you can get really good at this. The first two or three can be very painful, but you can do a bunch of them really fast.

(00:22:38):
So here's another one, and let's skip the system prompt again. And the user asks, "Hey, I'm looking for a two- to three-bedroom with either one or two baths. Do you provide virtual tours?"

(00:22:51):
And a bunch of tools are called and it says, "Hi Sarah. Currently, we have three-bedroom, two-and-a-half-bathroom apartment available for $2,175. Unfortunately, we don't have any two-bedroom options at the moment. We do offer virtual tours. You can schedule a tour," blah, blah. It just so happens that there is no virtual tour, right?

Lenny Rachitsky (00:23:16):
Mm-hmm. Nice.

Hamel Husain (00:23:16):
So it is hallucinating something that doesn't exist. Then you kind of have to bring your context as an engineer, or even product content, and say, "Hey, this is kind of weird. We shouldn't be telling a person about virtual tour when it's not offered."

(00:23:32):
So you would say, "Okay, offered virtual tour," and you just write the note. So you can see there's a diversity of different kinds of errors that we're seeing, and we're actually learning a lot about your application in a very short amount of time.

Shreya Shankar (00:23:55):
One common question that we get from people at this stage is, "Okay, I understand what's going on. Can I ask an LLM to do this process for me?"

Lenny Rachitsky (00:24:04):
Mm, great question.

Shreya Shankar (00:24:04):
And I loved Hamel's most recent example because what we usually find when we try to ask an LLM to do this error analysis is it just says the trace looks good because it doesn't have the context needed to understand whether something might be bad product smell or not. For example, the hallucination about scheduling the tour, right? I can guarantee you, I would bet money on this, if I put that into chat GPT and asked, "Is there an error?" it would say, "No, did a great job."

(00:24:34):
But Hamel had the context of knowing, "Oh, we don't actually have this virtual tour functionality," right? So I think, in these cases, it's so important to make sure you are manually doing this yourself. And we can talk a little bit more about when to use LLMs in the process later, but number one pitfall right here is people are like, "Let me automate this with an LLM."

Lenny Rachitsky (00:24:55):
Do you think we'll get to a place where an agent can do this, where it has that context?

Shreya Shankar (00:24:58):
Oh, no. No, no, no. Sorry. There are parts of error analysis that an LLM is suited for, which we could talk about later in this podcast. But right now, in this stage of free form, note-taking is not the place for an LLM.

Lenny Rachitsky (00:25:13):
Got it. And this is something you call open coding, this step?

Shreya Shankar (00:25:14):
Yes, absolutely.

Lenny Rachitsky (00:25:17):
Cool. Another term that you used in your posts that I love and that fits into this step is this idea of a benevolent dictator. Maybe just talk about what that is, and maybe, Shreya, cover that.

Shreya Shankar (00:25:27):
Yeah, so Hamel actually came up with this term.

Lenny Rachitsky (00:25:29):
Okay, maybe Hamel cover that, actually.

Hamel Husain (00:25:33):
No problem. And we'll actually show the LLM automation in this example, because we're going to take this example, we're going to go all the way through.

Lenny Rachitsky (00:25:40):
Amazing.

Hamel Husain (00:25:41):
And so benevolent dictator is just a catchy term for the fact that when you're doing this open coding, a lot of teams get bogged down in having a committee do this. And for a lot of situations, that's wholly unnecessary. People get really uncomfortable with, "Okay, we want everybody on board. We want everybody involved," so on and so forth. You need to cut through the noise. And a lot of organizations, if you look really deeply, especially small, medium-sized companies, you can appoint one person whose tastes that you trust. And you can do this with a small number of people and often one person, and it's really important to make this tractable. You don't want to make this process so expensive that you can't do it. You're going to lose out.

(00:26:36):
So that's the idea behind benevolent dictator, is, "Hey, you need to simplify this across as many dimensions as you can." Another thing that we'll talk about later is when it goes to building an LLM as a judge, you need a binary score. You don't want to think about, "Is this like a 1, 2, 3, 4, 5?" Like, assign a score to it. You can't. That's going to slow it down.

Lenny Rachitsky (00:26:59):
Just to make sure this benevolent dictator point is really clear, basically, this is the person that-

Lenny Rachitsky (00:27:00):
Make sure this benevolent dictator point is really clear. Basically, this is the person that does this note-taking, and ideally they're the expert on the stuff. So if it's law stuff, maybe there's a legal person that owns this, it could be a product manager. Give us advice on who this person should be?

Hamel Husain (00:27:16):
Yeah. It should be the person with domain expertise. So in this case, it would be the person who understands the business of leasing, apartment leasing, and has context to understand if this makes sense. It's always a domain expert, like you said. Okay. For legal, it would be a law person. For mental health, it would be the mental health expert, whether that's a psychiatrist or someone else.

Lenny Rachitsky (00:27:41):
Cool.

Hamel Husain (00:27:42):
Though oftentimes, it is the product manager.

Lenny Rachitsky (00:27:44):
Cool. So the advice here is pick that person. It may not feel so super fair that they're the one in charge and they're the dictator, but they're benevolent. It's going to be okay.

Hamel Husain (00:27:52):
Yeah. It's going to be okay. It's not perfection. You're just trying to make progress and get signal quickly so you have an idea of what to work on because it can become infinitely expensive if you're not careful.

Lenny Rachitsky (00:28:07):
Yeah. Okay, cool. Let's go back to your examples.

Hamel Husain (00:28:09):
Yeah, no problem. So this is another example where we have someone saying, "Okay. Do you have any specials?" And the assistant or the AI responds, "Hey, we have a 5% military discount." User responds, and it switches the subject, "Can you tell me how many floors there are? Do you have any one-bedrooms available or one-bedrooms on the first floor?" And the AI responds, "Yeah, okay. We have several one-bedroom apartments available." And then the user wants to confirm, "Any of those on the first floor and how much are the one-bedrooms?" And then also, it's a current resident, so they're also asking, "I need a maintenance request."

(00:28:56):
You could see the messiness of the real world in here, and the assistant just calls a tool that says transfer call, but it doesn't say anything. It just abruptly does transfer call, so it's pretty jank, I would say. It's just not-

Lenny Rachitsky (00:29:13):
Another jank.

Hamel Husain (00:29:14):
Another kind of jank, a different kind of jank. So when you write the open note, you don't want to say jank, because what we want to do is we want to understand, and when we look at the notes later on, we want to understand what happened.

(00:29:24):
So you just want to say, "Did not confirm call transfer with user." And it doesn't have to be perfect. You just have to have a general idea of what's going on.

Lenny Rachitsky (00:29:39):
Cool.

Hamel Husain (00:29:39):
So, okay. So let's say we do, and Shreya and I, we recommend doing at least 100 of these. The question is always, "How many of this do you do?" And so there's not a magic number. We say 100 just because we know that as soon as you start doing this, once you do 20 of these, you will automatically find it so useful that you will continue doing it.

(00:30:07):
So we just say 100 to mentally unblock you, so it's not intimidating. It's like, "Don't worry, you're only going to do 100." And there is a term for that, so the right answer is, "Keep looking at traces until you feel like you're not learning anything new." Maybe Shreya should talk about-

Shreya Shankar (00:30:30):
Yeah. So there's actually a term-

Hamel Husain (00:30:31):
... that.

Shreya Shankar (00:30:31):
... in data analysis and qualitative analysis called theoretical saturation. So what this means is when you do all of these processes of looking at your data, when do you stop? It's when you are theoretically saturating or you're not uncovering any new types of notes, new types of concepts, or nothing that will materially change the next part of your process.

(00:30:57):
And this kind of takes a little bit of intuition to develop, so typically, people don't really know when they've reached theoretical saturation yet. That's totally fine. When you do two or three examples or rounds of this, you will develop the intuition. A lot of people realize, "Oh, okay. I only need to do 40, I only need to do 60. Actually, I only need to do 15." I don't know. Depends on the application and depends on how savvy you are with error analysis for sure.

Lenny Rachitsky (00:31:25):
And your point about you're going to want to do a bunch. I imagine it's because you're just like, "Oh, I'm discovering all these problems. I got to see what else is going on here."

Shreya Shankar (00:31:33):
Exactly.

Lenny Rachitsky (00:31:34):
Is that right?

Shreya Shankar (00:31:34):
And promise, at some point, you're not going to discover new types of problems.

Lenny Rachitsky (00:31:39):
Yeah. Awesome. So let's say you did 100 of these, what's the next step?

Hamel Husain (00:31:42):
Yeah. Okay. So you did 100 of these. Now you have all these notes. So this is where you can start using AI to help you. So the part where you looked at this data is important, like we discussed. You don't want to automate this part too much.

Lenny Rachitsky (00:31:59):
Humans will still have jobs. This is the takeaway here. That's great.

Hamel Husain (00:32:02):
Yes.

Lenny Rachitsky (00:32:02):
Just reviewing traces. At least there's one job left for now. Great.

Hamel Husain (00:32:06):
So, yeah. Exactly. And so, okay. You have all these notes. Now, to turn this into something useful, you can do basic counting. So basic counting is the most powerful analytical technique in data science because it's so simple and it's kind of undervalued in many cases, and so it's very approachable for people.

(00:32:33):
And so the first thing you want to do is take these notes, and you can categorize them with an LLM, and so there's a lot of different ways to do that. Right before this podcast, I took three different coding agents or AI tools in how to categorize these notes. So one is, "Okay, I uploaded into a cloud project, I uploaded a CSV of these notes, and I just exported them directly from this interface." There's a lot of different ways to do this, but I'm showing you the simple, stupid way, the most basic way of doing things.

(00:33:13):
And so I dumped the CSV in here and I said, "Please analyze the following CSV file." And I told it there's a metadata field that has a note in it, but what I said is I used the word open codes, and I said, "Hey, I have different open codes," and that's a term of art. LLMs know what open codes are and they know what axial codes are because it is a concept that's been around for a really long time, so those words help me shortcut what I'm trying to do.

Lenny Rachitsky (00:33:46):
That's awesome. And the end of the prompt is telling it to create axial codes?

Hamel Husain (00:33:50):
Yes. Creating axial codes, so what it does is-

Shreya Shankar (00:33:54):
So maybe it's worth talking about what are axial codes or what's the point here? You have a mess of open codes, and you don't have 100 distinct problems. Actually, many of them are repeats, but because you phrased them differently, and that you shouldn't have tried to create your taxonomy of failures as you're open coding. You just want to get down what's wrong and then organize, "Okay, what's the most common failure mode?"

(00:34:19):
So the purpose, axial code basically is just a failure mode. It's the label or category. And what our goal is, is to get to this clusters of failure modes and figure out what is the most prevalent, so then you can go and run and attack that problem.

Lenny Rachitsky (00:34:36):
That is really helpful. Basically, just synthesizing all these-

Shreya Shankar (00:34:36):
Absolutely.

Lenny Rachitsky (00:34:39):
... into categories and themes. Super cool. And we'll include this prompt in our show notes for folks so they don't have to sit there and screenshot it and try to type it up themselves.

Hamel Husain (00:34:49):
Yeah. Great idea. And so Claude went ahead and analyzed the CSV file and decided how to parse it, blah, blah, blah. We don't need to worry about all that stuff, but it came up with a bunch of axial codes. Basically, axial codes are categories, like Shreya said. So one is, okay, capability limitations, misrepresentation, process and protocol violations, human handoff issues, communication, quality. It created these categories.

(00:35:18):
Now, do I like all the categories? Not really. I like some of them. It's a good first stab at it. I would probably rename it a little bit because some of them are a bit too generic. Like what is capability limitation? That's a little bit too broad. It's not actionable. I want to get a little bit more actionable with it so that if I do decide it's a problem, I know what to do with it, but we'll discuss that in a little bit. So you can do this with anything, and this is the dumbest way to do it, but dumb sometimes is a good way to get started, so-

Lenny Rachitsky (00:35:49):
And this is what LLMS are really good at, taking a bunch of information and synthesizing it.

Shreya Shankar (00:35:53):
Absolutely. Synthesizing for us to make sense of, right? Note that it's not automatically proposing fixes or anything, that's our job, but now, we can wade through this mess of open codes a lot easier.

(00:36:05):
Another thing that's interesting here in this prompt to generate the axial codes is you can be very detailed if you want, right? You can say, "I want each axial code to actually be some actionable failure mode," and maybe the LLM will understand that and propose it, or, "I want you to group these open codes by what stage of the user story that it's in." So this is where you can be creative or do what's best for you as a product manager or engineer working on this, and that will help you do the improvement later.

Lenny Rachitsky (00:36:40):
So there's no definitive prompt of, "Here's the one way to do it"?

Shreya Shankar (00:36:42):
Absolutely.

Lenny Rachitsky (00:36:43):
You're saying you can iterate, see what works for you?

Shreya Shankar (00:36:46):
Absolutely.

Lenny Rachitsky (00:36:46):
It's interesting the tools don't do this, or do they try and they just don't do a great job?

Shreya Shankar (00:36:50):
No, I don't think they do it. We've been screaming from the rooftops, "Please, please-"

Lenny Rachitsky (00:36:54):
Oh, wow.

Shreya Shankar (00:36:55):
"... do this." I do think it's a little bit hard, right? Part of this whole experience with the eval scores Hamel and I are teaching are a lot of people don't actually know this, so maybe it's that people don't know this and they don't know how to build tools for it. And hopefully, we can demystify some of this magic.

Lenny Rachitsky (00:37:13):
And just to double-click on this point, this is not a thing everyone does or knows. This is something you two developed based on your experience doing data analysis and data science at other companies?

Shreya Shankar (00:37:23):
Well, I want to caveat that we didn't invent error analysis. We don't actually want to invent things. That's bad signal. If somebody is coming to you with a way to do something that's entirely new and not grounded in hundreds of years of theory and literature, then you should, I don't know, be a little bit wary of that.

(00:37:42):
But what we tried to do was distill, "Okay, what are the new tools and techniques that you need to make sense of the LLM error-out analysis?" And then we created a curriculum or structured way of doing this. So this is all very tailored to LLMs, but the terms open coding, axial coding, are grounded in social science.

Lenny Rachitsky (00:38:04):
Amazing. Okay. What's funny about you guys doing this is I just want to go do this somewhere. I don't have any AI product to do this on, but it's just like, "Oh, this would be so fun." Just sit there and find all the problems I'm running into and categorize them and then try to fix them.

Shreya Shankar (00:38:18):
I love that.

Lenny Rachitsky (00:38:19):
Hamel pulled up a video. What do you got going on here?

Hamel Husain (00:38:22):
Yeah. So I pulled up a video just to drive home Shreya's point. We are not inventing anything, so what you see on the screen here is Andrew Ng, one of the famous machine learning researchers in the world who have taught a lot of people, frankly, machine learning. And you can see this is an eight-year-old video, and he's talking about error analysis.

(00:38:45):
And so this is a technique that's been used to analyze stochastic systems for ages, and it's something that it was just using the same machine learning ideas and principles, just bringing them into here, because again, these are stochastic systems.

Lenny Rachitsky (00:39:01):
Awesome. Well, one thing, we're working on getting Andrew on the podcast, we're chatting, so that will-

Shreya Shankar (00:39:01):
Nice.

Lenny Rachitsky (00:39:05):
... be really fun. Two, I love that my podcast episode just came out today is in your feed there, and it's standing out really well in that feed, so I'm really happy about that [inaudible 00:39:13].

Hamel Husain (00:39:13):
Very nice. Yeah. The recommendation algorithm is quite good.

Lenny Rachitsky (00:39:15):
Yes. Here we go. Hope you click on that. Don't screw my algorithm. Okay, cool. So we've done some synthesis. I know we're not going to go through the entire step. This is you have a whole course that takes many days to learn this whole process. What else do you want to share about how to go about this process?

Hamel Husain (00:39:31):
Okay. So you can do this through anything, and the same thing works just fine in ChatGPT, the same exact prompt. You can see it made axial codes. I really like using Julius AI. It's one of my favorite tools.

(00:39:45):
Julius is kind of this third-party tool that uses notebooks. I personally like Jupiter notebooks a lot, and so it's more of a data science thing, but a lot of product managers that are kind of learning notebooks nowadays, and it's kind of cool. It's like a fun playground where you can write code and look at data. But we don't have to go deeply into that. Just wanted to mention, you can use a lot. AI is really good at this.

(00:40:10):
So let's go to the fun part. Here we go. So now we have these axial codes. So the first thing I like to do, I have these open codes, and I have the axial codes, let's say, that we assigned from the cloud project or the ChatGPT. And so what I do is I collect them first and I take a look, like, "Does these axial codes make sense?" And I look at the correspondence between the different axial codes and the open codes, and I go through an exercise and I say, "Hmm. Do I like these codes? Can I make them better? Can I refine them? Can I make them more specific?" Instead of being generic, I make them very specific and actionable.

(00:40:59):
So you see the ones that I came up with here are tour scheduling, rescheduling issues, human handoff or transfer issue, formatting error with an output, conversational flow. We saw the conversational flow issue with the text messages. Making follow-up promises not kept.

(00:41:18):
And so basically, what I can do, what you can do now is you have these axial codes, and so I just collect them into a list, so this is an Excel formula. Just collect these codes into a list, and now we have a comma-separated list of these codes. And then what you can simply do is you could take your notes that you have, those open codes, and you can tell an AI, and this is using Gemini and AI just for simplicity, this is, again, we're trying to keep it simple, categorize the following note into one of the following categories as always.

Lenny Rachitsky (00:41:56):
For folks watching, I like all these different prompts and formulas you're sharing. This is the Google Sheets AI prompt.

Shreya Shankar (00:42:04):
Huge fan.

Hamel Husain (00:42:07):
And so basically, what you could do is you can categorize your traces into one of the buckets, and that's what we have here. We have categorized all those problems that we encountered into one of these things.

Shreya Shankar (00:42:22):
And this is automatic, which is very exciting. I mean, the AI is doing it. So this also drives home the point that your open codes have to be detailed, right? You can't just say janky because if the AI is reading janky, it's not going to be able to categorize it. Even a human wouldn't, right? It would have to go and remember why you said janky, so it's important to be somewhat detailed in your open code.

Lenny Rachitsky (00:42:45):
Okay. So avoid the word janky. It's a good rule of thumb.

Shreya Shankar (00:42:48):
Yeah. Or have it with 10 other words.

Lenny Rachitsky (00:42:48):
Oh, okay. What is-

Hamel Husain (00:42:48):
Yeah. I was being funny.

Lenny Rachitsky (00:42:52):
Yeah, okay. What are some of those other words that people often use that you think are not good?

Shreya Shankar (00:42:57):
I don't think it's specific words. I think it's just people are not detailed enough in the open code, so it's hard to do the categorization.

Lenny Rachitsky (00:43:04):
Great. And by the way, the reason you have to map them back is because, say, Claude or ChatGPT gave you suggestions and you change them and iterated on them, so you can't just go back and say, "Cool, whatever," in each bucket?

Hamel Husain (00:43:16):
Yeah, yeah.

Lenny Rachitsky (00:43:17):
Great.

Hamel Husain (00:43:17):
That's a really good question, actually. It's good to iterate and think about it a little bit like, "Do I like these open codes? Do these actually make sense to me?" Just like anything that AI does, it's really good to kind of put yourself in the middle just a little bit.

Lenny Rachitsky (00:43:32):
It's in the loop. Still space for us. Great.

Shreya Shankar (00:43:34):
One of the things that I like to do with this step if I'm trying to use AI to do this labeling, is also have a new category called none of the above. So an AI can actually say, "None of the above," in the axial code, and that informs me, "Okay, my axial codes are not complete. Let's go look at those open codes, let's figure out what some new categories are or figure out how to reword my other axial codes."

Lenny Rachitsky (00:44:00):
Awesome. And what's cool about this is you don't need to do this many, many times.

Shreya Shankar (00:44:03):
No.

Lenny Rachitsky (00:44:04):
For most products, you do this process once, and then you build on it, I imagine, and you just tweak it over time?

Shreya Shankar (00:44:09):
Absolutely. And it gets so fast. People do this once a week, and you can do all of this in 30 minutes, and suddenly your product is so much better than if you were never aware of any of these problems.

Lenny Rachitsky (00:44:23):
Yeah. It's absurd to feel like you wouldn't know this is happening. Watching this happening, I'm like, "How could you not do this to your product?"

Shreya Shankar (00:44:31):
A lot of people have no idea.

Lenny Rachitsky (00:44:31):
Most people. Yeah. We'll talk about that. There's a whole debate around this stuff that we want to talk about. Okay, cool. So you have the sheet. What comes next?

Hamel Husain (00:44:40):
Okay. So here's sort of the big unveil. This is the magic moment right now. So we have all these codes that we applied, the ones that we like on our traces. Now, you can do the ta-da, you can count them.

(00:44:56):
So here's a pivot table, and we just can do pivot table on those, and we can count how many times those different things occurred. So what do we find? Find on these traces that we categorized? We found 17 conversational flow issues. And I really like pivot tables because you can do cool things. You can double-click on these. You can say, "Oh, okay. Let me take a look at those," but that's going into an aside about pivot tables, how cool they are.

(00:45:25):
But now, we have just a nice, rough cut of what are our problems? And now, we have gone from chaos to some kind of thinking around, "Oh, you know what? These are my biggest problems. I need to fix conversational issues, maybe these human handoff issues." It's not necessarily the count is the most important thing. It might be something that's just really bad and you want to fix that, but okay. Now, you have some way of looking at your problem, and now you can think about whether you need evals for some of these.

(00:46:07):
So there might be some of these things that might be just dumb engineering errors that you don't need to write an eval for because it's very obvious on how to fix them. Maybe the formatting error with output, maybe you just forgot to tell the LLM how you want it to be formatted, and you didn't even say that in the prompt. So just go ahead and fix the prompt maybe, and we can decide, "Okay, do you want to write an eval for that?" You might still want to write an eval for that because you might be able to test that with just code. You could just test the string, does it have the right formatting potentially? Without running an LLM.

(00:46:53):
So there's a cost-benefit trade-off to evals. You don't want to get carried away with it, but you want to usually ground yourself in your actual errors. You don't want to skip this step. And so the reason I'm kind of spending so much time on this is this is where people get lost. They go straight into evals like, "Let me just write some tests," and that is where things go off the rails.

(00:47:24):
Okay. So let's say we want to tackle one of these things. So for example, let's say we want to tackle this human handoff issue, and we're like, "Hmm, I'm not really sure how to fix this. That's a kind of subjective sort of judgment call on should we be handing off to a human? And I don't know immediately how to fix it. It's not super obvious per se. Yeah. I can change my prompt, but I'm not sure. I'm not 100% sure."

(00:47:56):
Well, that might be sort of an interesting thing for an LLM as a judge, for example. So there's different kinds of evals. One is code-based, which you should try to do if you can because they're cheaper. LLM as a judge is something, it's like a meta eval. You have to eval that eval to make sure the LLM that's judging is doing the right thing, which we'll talk about in a second.

(00:48:25):
So, okay. LLM as a judge, that's one thing. Okay. How do you build an LLM as a judge?

Lenny Rachitsky (00:48:31):
Before we get into that actually, just to make sure people know exactly what you're describing there, these two types of evals. One is you said it's code-based and one is LLM as judge. Maybe Shreya, just help us understand what code-based eval even is? It's essentially a unit test? Is that a simple way to think about it?

Shreya Shankar (00:48:46):
Yeah. Maybe eval is not the right term here, but think automated evaluator. So when we find these failure modes, one of the things we want is, "Okay. Can we now go check the prevalence of that failure mode in an automated way without me manually labeling and doing all the coding and the grouping, and I want to run it on thousands and thousands of traces, I want to run it every week." That is, okay. You should probably build an automated evaluator to check for that failure mode.

(00:49:12):
Now, when we're saying code-based versus LLM-based, we're saying, "Okay. So maybe I could write a Python function or a piece of code to check whether that failure mode is present in a trace or not." And that's possible to do for certain things like checking the output is JSON, or checking that it's markdown, or checking that it's short. These are all things you can capture in code or you could approximately capture in code.

(00:49:38):
When we're talking about LLM judge here, we're saying that this is a complex failure mode and we don't know how to evaluate in an automated way. So maybe we will try to use an LLM to evaluate this very, very narrow, specific failure mode of handoffs.

Lenny Rachitsky (00:49:56):
So just to try to mirror back what you're describing, you want to test what your, say, agent or AI product is doing. You ask it a question, it gets back with something.

(00:50:05):
One way to test if it's giving you the right answer is if it's consistently doing the same thing, that you could write a code to tell you this is true or false. For example, will it ever say there's a virtual tour? So you could ask it.

Shreya Shankar (00:50:18):
Yes.

Lenny Rachitsky (00:50:18):
"Do you provide virtual tours?" It says yes or no, and then you could write code to tell you if it's correct based on that specific answer.

(00:50:27):
But if you're asking about something more complicated and it's not binary, in one world, you need a human to tell you this is correct. The solution to avoid humans having to review all this every time automatically is LLMs replacing human judgment, and you'd call it an LLM as judge. The LLM as being the judge if this is correct or not.

Shreya Shankar (00:50:47):
Absolutely. You nailed it.

Lenny Rachitsky (00:50:48):
Great.

Shreya Shankar (00:50:49):
So people always think, "Oh, this is at least as hard as my problem of creating the original agent." And it's not, because you're asking the judge to do one thing, evaluate one failure mode, so the scope of the problem is very small and the output of this LLM judge is pass or fail. So it is a very, very tightly scoped thing that LLM judges are very capable of doing very reliably.

Lenny Rachitsky (00:51:18):
And the goal here is just to have a suite of tests that run before you ship to production that tell you things are going the way you want them to? The way your agent is interacting is correct?

Shreya Shankar (00:51:28):
The beautiful thing about LLM judges, you can use them in unit tests or CI, sure, but you could also use it online for monitoring, right? I can sample 1000 traces every day, run my LLM judge, real production traces, and see what the failure rate is there. This is not a unit test, but still now we get an extremely specific measure of application quality.

Lenny Rachitsky (00:51:53):
Cool. That's a really great point because a lot of people just see evals for being this not-real-life thing. It's a thing that you test before it's actually in the real world. And what's actually happening in the real world, you're saying you should actually do exactly that?

Shreya Shankar (00:52:04):
Yeah.

Lenny Rachitsky (00:52:04):
Test your real thing running in production? And it's a daily, hourly sort of thing you could be running?

Shreya Shankar (00:52:09):
Totally.

Lenny Rachitsky (00:52:10):
Awesome. Okay. Hamel's got an example of an actual LLM as a judge eval here, so let's take a look.

Hamel Husain (00:52:16):
I love how Shreya really teed it up for me, so thank you so much. So what we have is a LLM as a judge prompt for this one specific failure. Like Shreya said, you would want to do one specific failure and you want to make it binary because we want to simplify things. We don't want, "Hey, score this on a rating of one to five. How good is it?" That's just in most cases, that's a weasel way of not making a decision. Like, "No, you need to make a decision. Is this good enough or not? Yes or no?"

(00:52:50):
It can be painful to think about what that is, but you should absolutely do it. Otherwise, this thing becomes very untractable, and then when you report these metrics, no one knows what 3.2 versus 3.7 means, so.

Shreya Shankar (00:53:03):
Yeah. We see this all the time also, and even with expert-curated content on the internet where it's like, "Oh, here's your LLM judge evaluator prompt. Here's a one-to-seven scale."

(00:53:15):
And I always text Hamel like, "Oh, no. Now, we have to fight the misinformation again because we know somebody is going to try it out and then come back to us and say, 'Oh, I have 4.2 average,'" and we're going to be like, "Okay."

Lenny Rachitsky (00:53:31):
It's wild how much drama there is in the evals space. We're going to get to that. Oh, man.

(00:53:37):
This episode is brought to you by Mercury. I've been banking with Mercury for years, and honestly, I can't imagine banking any other way at this point. I switched from Chase, and holy moly, what a difference. Sending wires, tracking spend, giving people on my team access to move money around, so freaking easy. Where most traditional banking websites and apps are clunky and hard to use, Mercury is meticulously designed to be an intuitive and simple experience.

Lenny Rachitsky (00:54:00):
Meticulously designed to be an intuitive and simple experience, and Mercury brings all the ways that you use money into a single product, including credit cards, invoicing, bill pay, reimbursements for your teammates and capital. Whether you're a funded tech startup looking for ways to pay contractors and earn yield on your idle cash, or an agency that needs to invoice customers and keep them current, or an e-commerce brand that needs to stay on top of cash flow and access capital, Mercury can be tailored to help your business perform at its highest level. See what over 200,000 entrepreneurs love about Mercury. Visit mercury.com to apply online in 10 minutes. Mercury is a fintech, not a bank. Banking services provided through Mercury's FDIC insured partner banks. For more details, check out the show notes.

Hamel Husain (00:54:45):
Okay, so this is your judge prompt. There's no one way to do it. It's okay to use an LLM to help you create it, but again, put yourself in the loop. Don't just blindly accept what the LLM does, and in all of these cases, that's what we did. With the axial codes, we iterated on this. You can use an LLM to help you create this prompt, but make sure you read it, make sure you edit it, whatever. This is not necessarily the perfect prompt. This is just the stupid, keeping it very simple just to show you the idea. It's like, "Okay, for this handoff failure," I said, "Okay, I want you to output true or false," it's a binary judge. That's what we recommend. Then I just go through and say, "Okay, when should you be doing a handoff?" And I just list them out.

(00:55:33):
Okay, explicit human requests ignored or looped, some policy-mandated transfer, sensitive resident issues, tool data, unavailability, same day walk-in or tour requests. You need to talk to a human for that, so on and so forth. The idea is, now that I know that this is a failure from my data, I'm interested in iterating on it, because I know this is actually happening all the time. Like Shreya said, it would be nice to have a way not only to evaluate this on the data I have, but also on production data, just to get a sense of, what scales is this happening? Let me find more traces, let me have a way to iterate on this. We can take this prompt and I'm going to use the spreadsheet again. The first step is, okay, when I'm doing this judge... I wrote the prompt.

(00:56:28):
Now, a lot of people stop there and they say, "Okay, I have my judge prompt. We're done. Good, let's just ship it," and the prompt says... If the judge says it's wrong, it's wrong. They just accept it as the gospel, be like, "Okay, the LLM says it's wrong, it must be wrong. Don't do that, because that's the fastest way that you can have evals that don't match what's going on, and when people lose trust in your evals, they lose trust in you. It's really important that you don't do that, so before you release your LLM as a judge, you want to make sure it's aligned to the human. How do you do that? You have those axial codes and you want to measure your judge against the axial code, and say like, "Hey, does it agree with me? My own judge, does it agree with me?" Just measure it.

(00:57:18):
What we have here is, okay, I say, "Assess this LLM trace." Again, I'm using just spreadsheets here, "Assess this LM trace according to these rules," and the rules are just the prompt that I just showed you. I ask it, "Okay, is there a handoff error, true or false?" Then this column, let me just zoom in a bit. Column H, I have, "Okay, did this error occur?" Column G is whether I thought the error occurred or not. You can see-

Lenny Rachitsky (00:57:53):
You're going through manually, you do that.

Hamel Husain (00:57:55):
Yeah, yeah, which we already did. We already went through it manually. It's not like we have to do it again, because we have that cheat code from the axial coding, we already did it. You might have to go through it again if you need more data, and there's a lot of details to this on how to do this correctly. You want to split your data and do all these things, so that you're not cheating, but I just want to show you the concept. Basically, what you can do is measure the agreement. Now, one thing you should know, as a product manager, is a lot of people go straight to this agreement. They say, "Okay, my judge agrees with the human some percentage of the time."

(00:58:41):
Now that sounds appealing, but it's a very dangerous metric to use, because a lot of times, errors, they only happen on the long tail and they don't happen as frequently, so if you only have the error 10% of the time, then you can easily have 90% agreement by just having a judge say it passes all the time. Does that make sense? 90% agreement look good on paper, but it might be misleading.

Lenny Rachitsky (00:59:15):
It's rare, it's a rare error. Yeah.

Hamel Husain (00:59:18):
As a product manager or someone, even if you're not doing this calculation yourself, if someone ever reports to you agreement, you should immediately ask, "Okay, tell me more." You need to look into it. They give you more intuition, here is like a matrix of this specific judge in the Google sheet, and this is, again, a pivot table, just keeping it dumb and simple. "Okay, on the rows I have, what did the human think? What did I think? Did it have an error, true or false? Then did my judge have an error, true or false?"

Shreya Shankar (00:59:56):
The intuition here is exactly what Hamel said, where you need to look at each type of error. When the human said false, but the judge said true, or vice versa, so those non-green diagonals here, and if they're too large, then go iterate on your prompt, make it more clear to the LLM judge, so that you can reduce that misalignment. You want to get to a point where most... You're going to have some misalignment, that's okay. We talk about in our course, also how to code correct that misalignment, but in this stage, if you're a product manager and the person who's building the LLM judge eval has not done this, they're saying like, "It agrees 75% of the time, we're good." They don't have this matrix and they haven't iterated to make sure that these two types of errors have gone down to zero, then it's a bad smell. Go and ask them to go fix that.

Lenny Rachitsky (01:00:52):
Awesome. That's a really good tip, what to look for when someone's doing this wrong.

Shreya Shankar (01:00:56):
Yeah.

Lenny Rachitsky (01:00:56):
Actually, can you take us back to the LLM as judge prompt? I just want to highlight something really interesting here. I've had some guests on the podcast recently who've been saying, "Evals are the new PRDs," and if you look at this, this is exactly what this is. Product managers, product teams, here's what the product should be, here's all the requirements, here's the how it should work. They built a thing and then they test it. Manually, often. What's cool about this is this is exactly that same thing, and it's running constantly. It's telling you, "Here's how this agent should respond," and it's very specific ways. "If it's this, this, this, do that. If it's this, this, that, do that." It's exactly what I've been hearing again and again, you could see right here. This is the purest sense of what a product requirements document should be, is this eval judge that's telling you exactly what it should be, and it's automatic and running constantly.

Shreya Shankar (01:01:45):
Yeah, absolutely. It's derived from our own data, so of course, it's a product manager's expectations. What I find that a lot of people miss is they just put in what their expectations are before looking at their data, but as we look at our data, we uncover more expectations that we couldn't have dreamed up in the first place, and that ends up going into this prompt.

Lenny Rachitsky (01:02:05):
That is interesting. Your advice is not skip straight to evals and LLM as judge prompts before you build the product, still write traditional one-pagers PRDs to tell your team what we're doing, why we're doing it, what success looks like. But then at the end, you could probably pull from that and even improve that original PRD if you're evolving the product using this process.

Shreya Shankar (01:02:28):
I would go even further to say you're going to improve... It's going to change. You're never going to know what the failure modes are going to be upfront, and you're always going to uncover new vibes that you think that your product should have. You don't really know what you want until you see it with these LLMs, so you got to be flexible, have to look at your data, have to... PRDs are a great abstraction for thinking about this. It's not the end all, be all. It's going to change.

Lenny Rachitsky (01:02:58):
I love that, and Hamel's pulling up some cool research report. What's this about?

Hamel Husain (01:03:04):
This is one of the coolest research reports you can possibly read if you want to know about evals. It was authored by someone named Shreya Shankar.

Shreya Shankar (01:03:13):
Oh, my God.

Hamel Husain (01:03:15):
And her collaborators. It's called "Who Validates the Validated?"

Lenny Rachitsky (01:03:20):
That's the best name for a researcher.

Shreya Shankar (01:03:21):
Thank you, thank you.

Hamel Husain (01:03:24):
I should let Shreya talk about this. I think one of the most important things to pay attention in this paper are the criteria drift, and what she found.

Shreya Shankar (01:03:35):
We did this super fun study when we were doing user studies with people who were trying to write LLM judges or just validate their own LLM outputs. I think this was before evals was extremely popular, I feel like, on the internet. We did this project late 2023 was when we started it. But then the thing that really was burning in my mind as a researcher is like, "Why is this problem so hard? We've been having machine learning and AI for so long, it's not new, but suddenly, this time around, everything is really difficult." We just did this user study with a bunch of developers and we realized, "Okay, what's new here is that you can't figure out your rubrics upfront. People's opinions of good and bad change as they review more outputs, they think of failure modes only after seeing 10 outputs they would never have dreamed of in the first place," and these are experts. These are people who have built many LLM pipelines and now agents before, and you can't ever dream up everything in the first place. I think that's so key in today's world of AI development.

Lenny Rachitsky (01:04:50):
That is a really good point. That's very much reinforcing what we were just talking about and that's why I'll pull this up, is just... Okay-

Shreya Shankar (01:04:56):
The research behind it.

Lenny Rachitsky (01:04:58):
Yeah, okay, great. You still got to do product the same way, but now you have this really powerful tool that helps you make sure what you've built is correct. It's not going to replace the PRD process. Cool. How many, say, I don't know, LLM as judge prompts, do you end up with usually say... I don't know. I know, obviously, depends complexity to the product, but what's a number in your experience?

Shreya Shankar (01:05:19):
For me, between four and seven.

Lenny Rachitsky (01:05:22):
That's it.

Shreya Shankar (01:05:23):
It's not that many, because a lot of the failure modes, as Hamel said earlier, can be fixed by just fixing your prompt. You just didn't think to put it in your prompts, so now you put it in your... You shouldn't do an eval like this for everything, just the pesky ones that you've described your ideal behavior in your agent prompt, but it's still failing.

Lenny Rachitsky (01:05:43):
Got it. Say you found a problem, you fixed it. In traditional software development, you'd write a unit test to make sure it doesn't happen again. Is your insight here is, "Don't even bother writing an eval around that if it's just gone"?

Shreya Shankar (01:05:54):
I think you can if you want to, but the whole game here is about prioritizing. You have finite resources and finite time, you can't write an eval for everything, so prioritize the ones that are the more pesky areas.

Lenny Rachitsky (01:06:07):
Probably the ones that are most risky to your business if they say something like Mecha Hitler, Grok.

Shreya Shankar (01:06:07):
Yikes.

Lenny Rachitsky (01:06:15):
Cool. Okay, so that's very relieving, because this prompt was a lot of work to really think through all these details.

Shreya Shankar (01:06:21):
But it's a lot of one-time cost. Right now, forever, you can run this on your application.

Hamel Husain (01:06:30):
Okay, data analysis is super powerful, is going to drive lots of improvements very quickly to your application. We showed the most basic kind of data analysis, which is counting, which is accessible to everyone. You can get more sophisticated with the data analysis. There's lots of different ways to sample, look at data. We made it look easy in a sense, but there's a lot of skills here to do to it well. Building an intuition and a nose for how to sort through this data. For example, let's say I find conversational issues, this conversational flow issues. Maybe if I was trying to chase down this problem further, I would think about ways to find other conversational flow issues that I didn't code. I would maybe dig through the data in several ways, and there's different ways to go about this. It's very similar, if not almost exactly similar as traditional analytics techniques that you would do on any product.

Lenny Rachitsky (01:07:41):
Give us just a quick sense of what comes next and then let's talk about the debate around evals and a couple more things.

Shreya Shankar (01:07:48):
What comes next after you've built your LLM judge? Well, we find that people just try to use that everywhere they can, so they'll put the LLM judge in unit tests and they will build, "Here are some example traces where we saw that failure, because we labeled it. Now we're going to make those part of unit tests and make sure that, every time we push a change to our code, these tests are going to pass." They also use it for online monitoring. People are making dashboards on this, and I think that's incredible. I think the products that are doing this, they have a very sharp sense of how well their application is performing, and people don't talk about it, because this is their moat. People are not going to go and share all of these things, because it makes sense. If you are an email-writing assistant, and you're doing this and you're doing it well, you don't want somebody else to go and build an email-writing assistant and then get you out of business.

(01:08:41):
I really want to stress the point that it's try to use these artifacts that you're building wherever possible online, repeatedly use them to drive improvements to your product. Oftentimes, Hamel and I will tell people how to do this up to this very point, and it clicks for people and then they never come back again. Either they have, I don't know, quit their jobs, they're not doing AI development anymore, or they know what to do from here on out. I think it's the latter, but I think it's very powerful.

Lenny Rachitsky (01:09:15):
Just watching you do this really opened my eyes to what this is and how systematic the process is. I always imagine you just sit on a computer, "Okay, what are the things I need to make sure work correctly?" What you're showing us here is it's a very simple step-by-step based on real things that are happening in your product, how to catch them, identify them, prioritize them, and then catch them if they happen again and fix them.

Shreya Shankar (01:09:38):
Yeah, it's not magic. Anyone can do this, you're going to have to practice the skill, like any new skill, you have to practice, but you can do it. I think what's very empowering now is that product managers are doing this and can do this, and can really build very, very profitable products with this skill set.

Lenny Rachitsky (01:09:57):
Okay, great segue to a debate that we got pulled into that was happening on X the other day. I did not realize how much controversy and drama there is around evals. There's a lot of people with very strong opinions. How about Shreya? Give us just a sense of the two sides of the debate around the importance and value of evals, and then give us your perspective.

Shreya Shankar (01:10:19):
Yeah. All right, I'll be a little bit placating and I say I think everyone is on the same side. I think the misconception is that people have very rigid definitions of what evals is. For example, they might think that evals is just unit tests or they might think that evals is just the data analysis part and no online monitoring or no monitoring of product-specific metrics, like actually number of chats engaged in or whatnot. I think everyone has a different mindset of evals going in, and the other thing I will say is that people have been burned by evals in the past. I think people have done evals badly. One concrete example of this is they've tried to do an LLM judge, but it has not aligned with their expectations. They only uncovered this later on and then they didn't trust it anymore, and then they're like, "I'm anti evals."

(01:11:14):
I 100% empathize with that, because you should be anti Likert scale LLM judge. I absolutely agree with you, we are anti that as well. A lot of the misconception stems from two things, like people having a narrow definition of evals and then people not doing it well and then getting burned and then wanting to avoid other people making that mistake. Then, unfortunately, X or Twitter is a medium where people are misinterpreting what everybody is saying all the time, and you just get all these strong opinions of, "Don't do evals, it's bad. We tried it, it doesn't work. We're Claude Code," or whatever other famous product, "And we don't do evals." There's just so much nuance behind all of it, because a lot of these applications are standing on the shoulders of evals. Coding agents is a great example of that, Claude Code. They're standing on the shoulders of Claude base model... Not base, but the fine-tuned Claude models have been evaluated on many coding benchmarks. Can't argue against that.

Lenny Rachitsky (01:12:24):
Just to make clear exactly what you're talking about there, one of the heads, I think maybe the head engineer of Claude Code, went on a podcast and he's like, "We don't do evals, we just vibe. We just look at vibes," and vibes meaning they just use it and feel if it's right or wrong.

Shreya Shankar (01:12:37):
I think that works. There's two things to that, right? One is they're standing on the shoulders of the evals that their colleagues are doing for coding.

Lenny Rachitsky (01:12:45):
Of the Claude foundational model.

Shreya Shankar (01:12:47):
Absolutely, right? We know that they report those numbers, because we see the benchmarks, we know who's doing well on those. The other thing is they are actually probably very systematic about the error analysis to some extent. I bet you that they're monitoring who is using Claude, how many people are using Claude, how many traps are being created, how long these chats are. They're also probably monitoring in their internal team, they're dogfooding. Anytime something is off, they maybe have a cue or they send it to the person developing Claude Code, and this person is implicitly doing some form of hair error analysis that Hamel talked about. All of this is evals, right? There's no world in which they're just being like, "I made Claude Code, I'm never looking at anything," and unfortunately, when you don't think about that or talk about that, I think that the community...

(01:13:39):
Most of the community is beginners or people who don't know about evals and want to learn about it, and it sends the wrong message there. Now, I don't know what Claude Code is doing, obviously, but I would be willing to bet money that they're doing something in the form of evals.

Hamel Husain (01:13:53):
We'll also say that coding agents are fundamentally very different than other AI products, because the developer is the domain expert, so you can short circuit a lot of things, and also, the developer is using it all day long, so there's a type of dogfooding and type of domain expertise that is... You can collapse the activities, you don't need as much data, you don't need as much feedback or exploration, because you know, so your eval process should look different.

Lenny Rachitsky (01:14:31):
Because you're seeing the code, you see the code it's generating. You can tell, "This is great, this is terrible."

Hamel Husain (01:14:35):
Yeah, yeah. I think a lot of people had generalized coding agents, because coding agents are the first AI product released into the wild, and I think it's a mistake to try to generalize that at large.

Shreya Shankar (01:14:51):
The other thing is, yeah, engineers have a dogfooding personality. There are plenty of applications where people are trying to build AI in certain domains and they don't have dogfooding for doctors, for example, or not out there trying to get all the most incorrect advice from AI and be tolerant and receptive to that. It's very important to keep, I think these nuanced things in mind.

Lenny Rachitsky (01:15:16):
What I'm hearing from you, Shreya, interestingly, is that if humans on the team are doing very close data analysis, error analysis, dogfooding like crazy, and essentially, they're the human evals and you're describing that as that's within the umbrella of evals. You could do it that way if you have time and motivation to do that, or you could set these things up to be automatic.

Shreya Shankar (01:15:40):
Absolutely, it's also about the skills. People who work at Anthropic are very, very highly skilled. They've been trained in data analysis or software engineering or AI, and whatnot. You can get there, anyone can get there, of course, by learning the concepts, but most people don't have that skill right now.

Hamel Husain (01:16:02):
Dogfooding is a dangerous one, only because a lot of people will say they're dogfooding. They're like, "Yeah, we dogfooded," but are they, really? A lot of people aren't really dogfooding it at that visceral level that you would need to close that feedback loop. That's the only caveat I would add.

Lenny Rachitsky (01:16:24):
There's also this, feels like, straw man argument of evals versus A-B tests. Talk about your thoughts there, because that feels like a big part of this debate. People are having like, "Do you need evals if you have A-B tests that are testing production level metrics?"

Shreya Shankar (01:16:38):
A-B tests are, again, another form of evals ,I imagine, right? When you're doing an A-B test, you have two different experimental conditions and then you have a metric that quantifies the success of something, and you're comparing the metric. Again, an eval in our mind is systematic measurement of quality, some metric. You can't really do an A-B test without the eval to compare, so maybe we just have a different weird take on it.

Lenny Rachitsky (01:17:06):
Yeah, okay. What I'm hearing is you consider A-B tests as part of the suite of evals that you do. I think when people think A-B tests, it's like we're changing something in the product, we're going to see if this improves some metric we care about. Is that enough? Why do we need to test every little feature? If it's impacting a metric we care about as a business, we have a bunch of A-B tests that are just constantly running.

Shreya Shankar (01:17:27):
This is now a great point. I think a lot of people prematurely do A-B tests, because they've never done any error analysis in the first place. They just have hypothetically come up with their product requirements and they believe that, "We should test these things," but it turns out, when you get into the data, as Hamel showed, that the errors that you're seeing are not what you thought what the errors might be. They were these weird handoff issues or, I don't know, the text message thing was strange. I would say that, if you're going to do A-B tests and they're powered by actual error analysis as we've shown today, then that's great, go do it. But if you're just going to do them, which we find that people try to do, just want to do them based on what you hypothetically think is what is important, then I would encourage people to go and rethink that and ground your hypotheses.

Lenny Rachitsky (01:18:23):
Do you have thoughts on what Statsig is going to do at OpenAI? Is there anything there that's interesting? That was a big deal, a huge acquisition. A- B test company people are like, "A-B test, the future." Thoughts?

Hamel Husain (01:18:34):
Just to add to the previous question a little bit, why is there this debate, A-B testing versus evals? I think, fundamentally, evals is... People are trying to wrap their head around how to improve their applications and fundamentally need to do... Data science is useful in products. Looking at data, doing data analytics. There's many different suite of tools, and you don't need to invent anything new. Sure, you don't need necessarily the whole breadth of data science, and it looks slightly different, just slightly, with LLMs. Your tactics might be different, so really what it is is using analytic tools to understand your product. Now, people say the word "Evals," trying to carve out this new thing, and saying evals and then A-B testing, but if you zoom out, it's the same data science as before, and I think that's what's causing the confusion is, "Hey, we need data science thinking," and AI product is helpful to have that thinking in AI products like it is in any product is my take on that.

Lenny Rachitsky (01:19:50):
That's a really good take, I think just the word "Evals" triggers people now.

Shreya Shankar (01:19:53):
Yeah.

Lenny Rachitsky (01:19:53):
If you just call it, "We're just doing error analysis, doing data science to understand where our product breaks and just setting up tests to make sure we know-"

Shreya Shankar (01:20:00):
That's boring, sounds boring. No, no, no. We need a mysterious term, like "Evals," to really get the momentum going. Your question about Statsig, I think it's very exciting. To be honest, I don't know much about it, because I just imagine that they're this company that... There's a tool that many people use, and maybe it just so happened that OpenAI acquired them. I'm sure they've been using them in the past, I'm sure OpenAI's competitors are using Statsig as well, so maybe there is something strategic in that acquisition. I have no idea, I don't know anything there, but I think those are really the bigger questions for me than, "Is this fundamentally changing A-B testing or making evals more of a priority?" I think they've always been a priority, I think OpenAI has always been doing some form of them, and OpenAI has gone so far, historically speaking, as to go and look at all the Twitter sentiment and try to do some retrospective on that, and then tie that back to their products. Certainly, they're doing-

Shreya Shankar (01:21:00):
Then, tie that back to their products. Certainly, they're doing some amount of evals before they ship their new foundation models, but they're going so much beyond and being like, "Okay, let's find all the tweets that are complaining about it, all the Reddit threads that are complaining about it, and go try to figure out what's going on." It goes to show that evals are very, very important. No one has really figured it out yet. People are using all the available sources signal that they can to improve their products.

Hamel Husain (01:21:26):
What I'll say is I'm really hopeful that it might shift or create a focus within OpenAI, hopefully. Up until now, a lot of the big labs understandably focused on general benchmarks like MMLU score, human eval, things like that, which are very important for foundation models. Those not very related to product specific evals, like the ones we talked about today, but handoff and stuff like that, they tend not to correlate.

Shreya Shankar (01:22:01):
Yeah, they don't correlate with math problem-solving, sorry to say.

Hamel Husain (01:22:06):
Exactly. If you look at the eval products, let's say the ones up until recently that some of the big labs have, they don't have error analysis. They have a suite of generic tools, cosine similarity, hallucination score, whatever, and that doesn't work. It's a good first stab at it. It's okay. At least you're doing something, getting people, maybe it's like getting people look at data. But eventually, what we hope to see is, okay, a bit more data science thinking in this eval process. That's hopefully the tools we'll get to.

Shreya Shankar (01:22:44):
Yeah, Pamela and I should not be the only two people on the planet that are promoting a structured way of thinking about application specific evals. It's mind-boggling to me. Why are we the only two people doing this the whole world? What's wrong? I hope that we're not the only people and that more people catch on.

Lenny Rachitsky (01:23:04):
The fact that your course on Maven is the number one highest grossing course in Maven, clearly there's demand and interest, and there's more people I think on your side. Interestingly, just as an example you've been sharing on Twitter that I think is informative, everyone's been saying how cloud code doesn't care about evals. They're all about vibes, and everyone's like, and they're the best coding agent out there, so clearly, this is right. More recently, there's all this talk about Codex, OpenAI Codex being better and everyone's switching and they're so pro evals.

Shreya Shankar (01:23:33):
I know.

Lenny Rachitsky (01:23:34):
Yeah.

Shreya Shankar (01:23:38):
It gets me every time. The Internet's so inconsistent. My favorite thing was yesterday, I believe, a couple of lab mates and I were out getting dessert or something, and somebody said like, "Oh, do you like Codex or Claude better or whatever?" The other person said, "Oh, I like Claude." Then, someone else said, "But the new version of Codex is better." Then, the first person said, "Oh, but the last I checked was two days ago, so maybe my thoughts, maybe I'm not up-to-date." I was like, "Oh, my God."

Lenny Rachitsky (01:24:14):
So true, so true. This is the world we live in. Oh, my God. Okay. I want to ask about just top misconceptions people have with evals and top tips and tricks for being successful. Maybe just share one or two each of each. Let me just start with misconceptions, and maybe I'll go to the Hamel first. Just what are a couple of the most common misconceptions people have with eval still?

Hamel Husain (01:24:31):
The top one is, "Hey, I can just buy a tool, plug it in, and it'll do the eval for you. Why do I have to worry about this? We live in the age of AI. Can't the AI just eval it?" That's the most common misconception, and people want that so much that people do sell it, but it doesn't work. That's the first one.

Lenny Rachitsky (01:24:55):
Shoot, many humans are still great. I think that's great news.

Hamel Husain (01:25:00):
The second one that I see a lot is, "Hey, just not looking at the data." In my consulting, people come to me with problems all the time, and the first thing I'll say is, "Let's go look at your traces." You can see their eyes pop open and be like, "What do you mean?" I'm like, "Yeah, let's look at it right now." They're surprised that I am going to go look at individual traces, and it always 100% of the time learn a lot and figure out what the problem is. I think people just don't know how powerful looking at the data is like we showed on this podcast.

Shreya Shankar (01:25:48):
I would agree with that.

Lenny Rachitsky (01:25:50):
Those are the top two? Okay.

Shreya Shankar (01:25:51):
Yes.

Lenny Rachitsky (01:25:51):
Is there anything else or those are the ones solve those problems.

Shreya Shankar (01:25:55):
Oh, those are definitely... Then, I guess the third one I would add is, there's no one correct way to do evals. There are many incorrect ways of doing evals, but there are also many correct ways of doing it. You got to think about where you are at with your product, how much resources you have, and figure out the plan that works best for you. It'll always involve some form of error analysis as we showed today, but how you operationalize those metrics is going to change based on where you're at.

Lenny Rachitsky (01:26:28):
Amazing. Okay. What are a couple of just tips and tricks you want to leave people with as they start on their eval journey or just try to get better at something they're already doing?

Shreya Shankar (01:26:37):
Tip number one is just don't be alarmed or don't be scared of looking at your data. The process, we try to make it as structured as possible. There are inevitably questions that are going to come up. That's totally fine. You might feel like you're not doing it perfectly. That's also fine. The goal is not to do evals perfectly, it's to actionably improve your product. We guarantee you, no matter what you do, if you're doing parts of these process, you're going to find ways of actionable improvement, and then you're going to iterate on your own process from there.

(01:27:14):
The other tip that I would say is, we are very pro-AI. Use LLMs to help you organize any thoughts that you have throughout this entire process. This could be everything ranging from initial product requirements. Figure out how to organize them for yourself. Figure out how to improve on that product requirements doc based on the open codes that you've created. Don't be afraid to use AI in ways that present information better for you.

Lenny Rachitsky (01:27:44):
Sweet, so don't be scared. Use LLMs as much as you can throughout the process.

Shreya Shankar (01:27:48):
But not to replace yourself.

Lenny Rachitsky (01:27:51):
Right. Okay, great. There's still jobs. It's great. Hamel.

Hamel Husain (01:27:55):
Yeah. Let me actually share my screen, because I want to show something. To piggyback of what Shreya said is, if you heard any phrase in this podcast, you've probably heard look at your data more than anything else. It's so important that we teach that you should create your own tools to make it as easy as possible. I showed you some tools when we're going through the live example of how to annotate data. Most of the people I work with, they realize how important this is and they vibe code their own tools, or we shouldn't say vibe code. They make their own tools, and it's cheaper than ever before because you have AI that can help you.

(01:28:40):
AI is really good at creating simple web applications that can show you data, that can write to a database. It's very simple. For the Nurture Boss use case, we wanted to remove all the friction of looking at data. What you see here is just some screenshots of what the application that they created looks like. It's just, "Okay, they have the different channels, voice, email, text. They have the different threads, they hid the system prompt by default." Little quality of life improvements. Then, they actually have this axial coding part here where you can see in red the count of different errors. They automated that part in a nice way and they created this within a few hours. It's really hard to have a one size fits all thing for looking at your data. You don't have to go here immediately, but something to think about is make it as easy as possible because, again, it's the most powerful activity that you can engage in. It's the highest ROI activity you can engage in. With AI, yeah, just remove all the friction.

Lenny Rachitsky (01:29:56):
That's amazing. Again, I think that ROI piece is so important. We haven't even touched on this enough. The goal here is to make your product better, which will make your business more successful. This isn't just a little exercise to catch bugs and things like that. This is the way to make AI products better because the experience is how users interact with your AI.

Hamel Husain (01:30:16):
Absolutely. If any, we teach our students, "Hey, when you're doing these evals, if you see something that's wrong, just go fix it." The whole point is not to have evals, a beautiful eval suite, where you can point at it, edit it and say, Oh, look at my evals." No, just fix your application, make it better. If it's obvious, do it. Totally agree with you.

Lenny Rachitsky (01:30:38):
Amazing. A question I didn't ask, but this is I think something people are thinking about. How long do you spend on this? How long does it usually take to do? The first time

Shreya Shankar (01:30:45):
I can answer for myself for applications that I work with. Usually, I'll spend three to four days really working with whoever to do initial rounds of error analysis. A lot of labeling, feel like we're in a good place to create the spreadsheet that Hamel had and everyone's on-board and convinced, and even a few LLM judge evaluators. But this is one-time cost. Once I figured out how to integrate that in unit tests, or I have a script that automatically runs it on samples and I'll create a Cron Job to just do this every week. I would say it's like, I don't know, I find myself probably spending more time looking at data because I'm just data hungry like that. I'm so curious.

(01:31:23):
I'm like, I've gained so much from this process and it's put me above and beyond in any of my collaborations with folks, so I want to keep doing it, but I don't have to. I would say maybe 30 minutes a week after that.

Lenny Rachitsky (01:31:41):
It's a week essentially, a week essentially upfront, and then 30 minutes to keep improving on adding to your suite?

Shreya Shankar (01:31:47):
Yeah, it's really not that much time. I think people just get overwhelmed by how much time they spend up front and then thinking that they have to keep doing this all the time.

Lenny Rachitsky (01:31:56):
Amazing. Is there anything else that you wanted to share or leave listeners with? Anything else you wanted to double down as a point before we get to a very exciting lightning round?

Hamel Husain (01:32:06):
I would say this process is a lot of fun, actually. It's like, okay, you're looking at data. Oh, it sounds like you're annotating things. Okay. Actually, I was just looking at a client's data yesterday, the same exact process. It's a application that sends emails, recruiting emails to try to get candidates to apply for a job. We decided to start looking at traces. We jumped right into it. "Hey, let's look at your traces." We looked at a trace, the first thing I saw was this email that is worded, "Given your background, blah, blah, blah, blah, blah." I asked the person right away, and this is where putting your product hat on and just being critical, and this is where the fun part is.

(01:32:55):
I said, "You know what? I hate this email. Do you like the email, given your background?" When I receive a message given your background, comma, I just delete that. I'm like, "What is this, given your background with machine learning and blah blah?" I'm like, "This is a generic thing." I asked the person like, "Hey, can we do better than this? This sounds like generic recruiting." They're like, "Oh, yeah, maybe." Because they were proud of it, they're like, "The AI is doing the right thing, it's sending this email with the right information, with the right link, with the right name, everything." That's where the fun part is, is put your product hat on and get into, is this really good?

Lenny Rachitsky (01:33:38):
Something I want to make sure we cover before we get to a very exciting lightning round is, this is just scratching the surface of all the things you need to know to do this well. I think this is the best primer I've ever seen on how to do this well.

Shreya Shankar (01:33:51):
Nice.

Lenny Rachitsky (01:33:51):
But I think we did it. But you guys teach a course that goes much, much deeper for people that really want to get good at this and take this really seriously. Share what else you teach in the course that we didn't cover, and what else you get as a student being part of the course you teach at Maven.

Shreya Shankar (01:34:07):
Yeah, I can talk about the syllabus a little bit, and then Hamel can talk about all the perks. We go through a lifecycle of error analysis, then automated evaluators, then how to improve your application, how do you create that flywheel for yourself? We also have a few special topics that we find pretty much no one has ever heard of or taught before, which is exciting. One is, how do you build your own interfaces for error analysis? We go through actual interfaces that we've built and we also live code them on the spot for new data. We show how we use Claude code cursor, whatever we're feeling in the moment that day to build these interfaces.

(01:34:49):
We also talk about broadly cost-optimization as well. A couple of people that I've worked with, they get to a point where their evals are very good, their product is very good, but it's all very expensive because they're using state-of-the-art models. How can we replace certain uses of the most expensive GPT-5, with 5-nano, 4-mini whatnot and save a lot of money, but still maintain the same quality? We also give some tips for that. Hamel, you're on. We also have many perks.

Lenny Rachitsky (01:35:23):
Yeah. Talk about the perks.

Hamel Husain (01:35:24):
Okay, the perks. My favorite perk is there's 160 page book that's meticulously written, that we've created, that walks through the entire process in detail of how to do evals that supplement the course. You don't have to sit there and take all these notes. We've done all the hard work for you and we have documented it in detail and organize things. That is really useful. Another really interesting thing, and something that I got the idea from you, Lenny, is, okay, this is an AI course. Education shouldn't be this thing where you are only watching lectures and doing homework assignments. Students should have access to an AI that also helps them. What we have done is we've, just like there's the LennyBot that you have.

Lenny Rachitsky (01:36:19):
Dot com.

Hamel Husain (01:36:20):
Yeah, lennybot.com, we have made the same thing with the same software that you're using, and we have put everything we've ever said about evals into that. Every single lesson, every office hours, every Discord chat, any blogs, papers, anything that we've ever said publicly and within our course, we've put it in there. We've tested it with a bunch of students and they've said it's helpful. We're giving all students 10 months free unlimited access to that alongside the course.

Lenny Rachitsky (01:36:56):
Amazing. Then, you'll charge for that later down the road?

Hamel Husain (01:37:01):
I have no idea. I just take one month at a time. I don't know where we're going with that.

Lenny Rachitsky (01:37:04):
Eight months and then we'll have to figure it out. I was thinking this whole interview should have just been our bots talking to each other.

Shreya Shankar (01:37:09):
That's amazing. I would watch that, only for 10 minutes then I don't know what they're talking about.

Lenny Rachitsky (01:37:14):
Yeah, maybe 30 seconds. Do you guys train it on the voice mode, by the way? That's my favorite feature of Delphi's product. If not, you should do that.

Hamel Husain (01:37:22):
Oh, I think, I can't remember, I should look at it.

Lenny Rachitsky (01:37:26):
You definitely should. Now that we have this podcast episode, you could use this content to train it. It's 11Labs powered. It's so good. Okay, so how do they get to... I guess that's okay. They get to that once they become, enter your course.

Shreya Shankar (01:37:38):
Yeah, sign up for the course and then you'll get a bunch of emails. Everything will be clear, hopefully.

Lenny Rachitsky (01:37:43):
Amazing. Okay.

Shreya Shankar (01:37:44):
We also have a Discord of all the students who have ever taken the class. That Discord is so active. I can't go on vacation without getting notified on the plane.

Lenny Rachitsky (01:37:55):
Bittersweet, bittersweet. Incredible. Okay. With that, we've reached our very exciting lightning round. I've got five questions for you. Are you ready?

Shreya Shankar (01:38:04):
Yes. Let's go.

Lenny Rachitsky (01:38:05):
Let's do it. Okay. I'm going to bounce between you two. Share something if you want. You can pass if you want. First question, Shreya, what are two or three books that you find yourself recommending most to other people?

Shreya Shankar (01:38:17):
I like to recommend a fiction book because life is about more than evals. Recently, I read Pachinko by Min Jin Lee. A really great book. Then, I also am currently reading Apple in China, which the name of the author is slipping my mind, but this is more of an exposition, written by a journalist on how Apple did a lot of manufacturing processes in Asia over the last couple, several decades. Very eye-opening.

Lenny Rachitsky (01:38:49):
Amazing. Hamel.

Hamel Husain (01:38:52):
Yeah, I have them right here. I'm a nerd. Okay, so I'm not as cool as Shreya is. I actually have textbooks, which are my favorite. This one is a very classic one, Machine Learning by Mitchell. Now, it's theoretical, but the thing I like about it is it really drives home the fact that Occam's razor is prevalent not only in science, but also in machine learning and AI. A lot of times the simplest, and also engineering, so a lot of times the simpler approach generalizes better. That's the thing I internalize deeply from that book. I also really like this one. Another textbook. I told you I'm a nerd. This is also a very old one, and this is Norvig algorithms. I really like it because it's just human ingenuity and it's lots of clever useful things in computing.

Shreya Shankar (01:39:49):
They're down the street, him and Berkeley.

Lenny Rachitsky (01:39:54):
The people that did that research?

Shreya Shankar (01:39:57):
Yeah, textbook authors.

Lenny Rachitsky (01:39:58):
Super cool. Oh, man, nerds, I love it. Okay, next question. Favorite recent movie or TV show? I'll jump to Hamel first.

Hamel Husain (01:40:06):
Okay, so I'm a dad of two parents. I have two parents. Sorry, two kids. Yeah, I'm a dad of two kids, and I don't really get the time to watch any TV or movies, so I watch whatever my kids are watching. I've watched Frozen three times in the last week.

Lenny Rachitsky (01:40:25):
Only three? Oh, okay. In the last week. Okay.

Hamel Husain (01:40:30):
That's my life.

Lenny Rachitsky (01:40:30):
Great, Hamel. Frozen. I love it. Okay, Shreya.

Shreya Shankar (01:40:32):
Yeah, I don't have kids, so I can give all these amazing answers. Actually, so my husband and I have been watching The Wire recently. We never actually saw it growing up, so we started watching it and it's great.

Lenny Rachitsky (01:40:46):
I feel like everyone goes through that. Eventually in their life they decide, I will watch The Wire.

Shreya Shankar (01:40:51):
I know, so we are in that right now.

Lenny Rachitsky (01:40:51):
It's like a year of your life. It's great. It's such a great show. Oh, man. But it's so many episodes and everyone's an hour long.

Shreya Shankar (01:40:58):
I know. I know.

Lenny Rachitsky (01:40:58):
It's such a commitment.

Shreya Shankar (01:40:59):
We get through two or three a week, so we're very slow.

Lenny Rachitsky (01:41:03):
Worth it. Okay, next question. Do you have a favorite product you've recently discovered that you really love? We'll start with Shreya.

Shreya Shankar (01:41:10):
Yeah. I really like using Cursor, honestly. Now, Claude Code. I'll say why. I'm a researcher more so than anything else. I write papers, I write code, I build systems, everything, and I find that a tool... I'm so bullish on AI assisted coding because I have to wear a lot of hats all the time. Now, I can be more ambitious with the things that I build and write papers about, so I'm super excited about those. Cursor was my entry point into this, but I'm starting to find myself always trying to keep up with all these AI assisted coding tools.

Lenny Rachitsky (01:41:48):
Hamel?

Hamel Husain (01:41:49):
Yeah, I really like Claude Code and I like it because I feel like the UX is outstanding. There's a lot of love that went into that. It's just really impressive as a terminal application that is that nice.

Lenny Rachitsky (01:42:04):
Ironic that you two both love Claude Code when it's just built on vibes.

Shreya Shankar (01:42:09):
I think it's false. It's not just built on vibes.

Lenny Rachitsky (01:42:13):
There we go. Okay, two more questions. Hamel, do you have a favorite life motto that you find yourself using in coming back to in work or in life?

Hamel Husain (01:42:21):
Keep learning in. Think like a beginner.

Lenny Rachitsky (01:42:26):
Beautiful. Shreya?

Shreya Shankar (01:42:27):
I like that. For me, it's to always try to think about the other side's argument. I find myself sometimes just encountering arguments on the internet, like this race to eval debates and really think, "Okay, put myself in their shoes. There's probably a generous take, generous interpretation." I think we're all much stronger together than if we start picking fights. My vision for evals is not that Hamel and I become billionaires. It is that everyone can build AI products, and we're all on the same page

Lenny Rachitsky (01:42:59):
Slash everyone becomes billionaires.

Shreya Shankar (01:43:02):
Yes.

Lenny Rachitsky (01:43:04):
Amazing. Final question. When I have two guests on, I always like to ask this question and I'll start with Hamel. What's something about Shreya that you like most? What do you like most about Shreya? I'm going to ask her the same question in reverse.

Hamel Husain (01:43:18):
Yeah. Shreya is one of the wisest people that I know, especially for being so young relative to me. I feel like she's much wiser than I am, honestly, seriously. She's very grounded and has a very even perspective on things. I'm just really impressed by that all the time.

Lenny Rachitsky (01:43:18):
Shreya?

Shreya Shankar (01:43:43):
Yeah. My favorite thing about Hamel is his energy. I don't know anybody who consistently maintains momentum and energy like Hamel does. I often think that I would start carrying much less about evals, if not for Hamel. Everyone needs a Hamel in their life, for sure.

Lenny Rachitsky (01:44:06):
Well, we all have a Hamel in our life now. This was incredible. This was everything I'd hoped it'd be. I feel like this is the most interesting in-depth consumable primer on evals that I've ever seen. I'm really thankful you two made time for this. Two final questions. Where can folks find you? Where can they find the course and how can listeners be useful to you? I'll start with Shreya.

Shreya Shankar (01:44:29):
Yeah, you can reach me via email. It's on my website. If you Google my name, that is the easiest way to get to my website. You can find the course if you Google AI Evals for engineers and product managers, or just AI Evals course, you'll find it. We'll send some links hopefully after this, so it's easy. How to be helpful? Two things always for me. One is ask me questions when you have them. I'll try to get to the respond as soon as I can. The other one is tell us your successes. One of the things that keeps us going is somebody tells us what they implemented or what they did, a real case study. Hamel and I gets so excited from these and it really keeps us going, so please share.

Hamel Husain (01:45:16):
Yeah, it's pretty easy to find me. My website is Hamel.dev. I'll give you the link. You can find me on social media, LinkedIn, Twitter. The thing that's most helpful is to echo what Shreya said, we would be delighted if we are not the only people teaching evals. We would love other people teach evals. Any kind of blog posts, writing, especially that as you go through this and learn this that you want to share, we would be delighted to help re-share that or amplify that.

Lenny Rachitsky (01:45:54):
Amazing. Very generous. Thank you two, so much for being here. I really appreciate it, and you guys have a lot going on, so thank you.

Shreya Shankar (01:46:01):
Thanks, Lenny, for having us and for all the compliments.

Lenny Rachitsky (01:46:05):
My pleasure. Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at Lennyspodcast.com. See you in the next episode.

