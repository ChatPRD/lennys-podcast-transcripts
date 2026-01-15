---
guest: Shaun Clowes
title: Why great AI products are all about the data | Shaun Clowes (CPO at Confluent)
youtube_url: https://www.youtube.com/watch?v=yVS1gTAQYSU
video_id: yVS1gTAQYSU
description: 'Shaun Clowes is the chief product officer at Confluent and former CPO
  at Salesforce’s MuleSoft and at Metromile. He was also the first head of growth
  at Atlassian, where he led product for...

  '
duration_seconds: 4895.0
duration: '1:21:35'
view_count: 17562
channel: Lenny's Podcast
keywords:
- growth
- retention
- acquisition
- activation
- onboarding
- churn
- roadmap
- user research
- data-driven
- analytics
- funnel
- conversion
- pricing
- subscription
- revenue
---

# Why great AI products are all about the data | Shaun Clowes (CPO at Confluent)

## Transcript

Lenny Rachitsky (00:00:00):
I love that you have very strong opinion about this, which is just the state of the product management career and how most PMs are not that great.

Shaun Clowes (00:00:08):
Why is it that product management is still such a relatively undeveloped discipline? We're like 15 to 20 years into this, and so there's something about the current state of product management that isn't getting at the truly important things, the truly value-added things. If we were doctors, you'd be like, "That's totally unacceptable."

Lenny Rachitsky (00:00:24):
What's the answer, Shaun? How do we solve this problem?

Shaun Clowes (00:00:26):
In everything always talk from the customer's perspective, from the market's perspective, from the competitor's perspective, the very small number of PMs do that. They get dragged into internal politics, they get dragged into scrum management or scrum execution or product delivery, and you just can't win that way.

Lenny Rachitsky (00:00:40):
You kind of have this hot take that the way AI will most impact product management is data management.

Shaun Clowes (00:00:45):
Well, you've got this synthesis machine, which is this LLM thing that's going to help you do synthesis, but if it hasn't got all that data to do synthesis on top of, it's got nothing. And so that means that LLMs can only be as good as the data they are given and how recent that data is.

Lenny Rachitsky (00:00:58):
In the future, if you can easily clone a B2B SaaS app like Salesforce or Atlassian, what happens to these businesses long-term? Do they just become, are they all in trouble?

Shaun Clowes (00:01:06):
People really underestimate where the value is created in these applications and they just kind of get it completely wrong.

Lenny Rachitsky (00:01:17):
Today my guest is Shaun Clowes. Shaun is chief product officer at Confluent. Previously he was chief product officer at MuleSoft, which is a billion-dollar business within Salesforce. Before that, he was chief product officer of Metromile, a public auto insurance technology company. And prior to that he spent six years at Atlassian where he ran the Jira agile and also built the first ever B2B growth team. He also created two of the most popular Reforge courses, one on retention and engagement and one on data for product managers. Shaun is awesome because he's both very tactical in execution oriented, while also being very philosophical and insightful about the craft of product and growth. In our conversation, Shaun shares why most PMs are not good, what it takes to become a good or great product manager, how he thinks about his career, like a Bingo card and why he indexes towards finding very different roles for every new job that he takes.

(00:02:12):
Why good data is the most important ingredient in AI tools and for product managers working with AI. Also, how to build a great B2B growth team, what he's learned about doing B2B growth and his really interesting take on how AI will and won't disrupt SaaS tools out in the wild. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It's the best way to avoid missing feature episodes and it helps the podcast tremendously. With that I bring you Shaun Clowes. This episode is brought to you by Enterpret. Enterpret unifies all your customer interactions from Gong calls to Zendesk tickets, to Twitter threads, to app store reviews and makes it available for analysis. It's trusted by leading product orgs like Canva, Notion, Loom, Linear, Monday.com, and Strava to bring the voice of the customer into the product development process, helping you build best-in-class products faster.

(00:03:07):
What makes Enterpret special is its ability to build and update customer-specific AI models that provide the most granular and accurate insights into your business, connect customer insights to revenue and operational data in your CRM or data warehouse, to map the business impact of each customer need and prioritize confidently, and empower your entire team to easily take action on use cases like win-loss analysis, critical bug detection, and identifying drivers of churn with Enterpret's AI systems Wisdom. Looking to automate your feedback loops and prioritize your roadmap with confidence like Notion, Canva and Linear, visit E-N-T-E-R-P-R-E-T.com/lenny to connect with the team and to get two free months when you sign up for an annual plan. This is a limited-time offer. That's enterpret.com/lenny.

(00:03:54):
This episode is brought to you by BuildBetter.ai. Back in 2020 when AI was just a toy, BuildBetter bet that it could cut down on a product team's operational BS. Fast-forward to today, 23,000 product teams use purpose-built AI in BuildBetter every day. First, BuildBetter uses custom models to turn unstructured data like product and sales calls, support tickets, internal communications, and surveys into structured insights. It's like having a dedicated data science team. Second, BuildBetter runs those structured insights into workflows, like weekly reports about customer issues, contacts to where PRDS, and user research documents with citations, it even turns stand-ups into action items that automatically get assigned and shared into your tools. Plus, with unlimited seat pricing on all plans, BuildBetter ensures everyone at your company has access to this knowledge, truly no data silos. In a world of AI demos over-promising and under-delivering, see why BuildBetter has a 93% subscription retention. Get a personalized demo and use code Lenny for $100 credit if you sign up now at buildbetter.ai/lenny. Shaun, thank you so much for being here and welcome to the podcast.

Shaun Clowes (00:05:12):
Thank you, Lenny. It's really awesome to be here.

Lenny Rachitsky (00:05:14):
I've had you on my radar for a long time and I am really excited to finally have you here and big bonus points for having a very beautiful, sultry Australian accent that always helps with the ratings, I think. I don't know if it's causal, but it's correlative.

Shaun Clowes (00:05:28):
I'm glad to be a bit of a curiosity.

Lenny Rachitsky (00:05:31):
So I want to start with something I totally believe and I love that you have very strong opinion about this, which is just the state of the product management career and how most PMs are not that great and how there's a big opportunity to level up. You just talk about what you've seen there and you're just thinking here.

Shaun Clowes (00:05:51):
Yeah, it's honestly a big conundrum for me. I think it's actually part of... It's grandiose to say so, a bit of my life's work. Why is it that product management is still such a relatively undeveloped discipline? We're 15 to 20 years into this thing. You would've thought that it would be less random than it is. The outcomes are random, the behaviors are random, individual performance is random, seemingly. And so there's something about the current state of product management that isn't getting at the truly important things, the truly value-added things, the right way to think about problems, the right way to think through problems, the abstract reasoning that's needed, there's something that isn't working about it. I spent a long time trying to put my finger on it and then be like, "How do you reproducibly reproduce that?" Reproducibly produce people who can really be really great product managers.

(00:06:39):
The thing is that if you think all the way back to it, I spent a long time as an engineer and people always talk about 10 times engineers and I wanted to be a 10 times engineer. I'll leave it to others to decide to tell you whether or not I was or I wasn't, but certainly I wanted to be and I tried to be a really great engineer. And it must be true that if there's 10 times engineers, and I would argue they definitely are, they must be 10 times product managers too. But at the same time, those 10 times product managers, because product management is ultimately about leverage, so it's about helping other people have dramatically more impact than they would if they were unorganized that they didn't have somebody to organize the goals and what we're trying to achieve, then that means that a 10 times product manager has 100 times return or more because they're 10 timesing the return on 10 times resources.

(00:07:23):
So the outcomes are so wild, like wildly distributed and the benefits are so good that you would've thought that it would've behooved us. There would've been a way that this had evolved and improved and really gotten way crisper than it has, but here we are. I'm not saying that we haven't gotten better, we 100% have, but I think we could all say that we're not reliably producing 10 times product managers every day of the week.

Lenny Rachitsky (00:07:49):
I love this point and it's especially painful that when someone works with a PM that's not great. There's just this meme of why do I need PMs? PMs are useless, PMs suck, and it just creates that no one's ever like, "Engineers are useless or designers are useless." But there's so many people are like, "I don't need product managers on our team. Never hire a PM," and it just sets the whole profession back.

Shaun Clowes (00:08:12):
When I first started out in PM somebody, it's obviously a chestnut, but he pointed out that realistically when you're a product manager, your job is to say no to 90% of things that get brought your way. And so that kind of makes you the bad person pretty much from the start. And so you're saying no to 90%, so you can say yes to 10% and that kind of puts you behind the eight-ball right at the very beginning, and so you have to very quickly get runs on the board. You have to prove to have the right insights, to have the right data, to make the right decisions or you don't get another go, you don't get another swing at it. So it makes sense that product managers are the easiest to single out and criticize, but that is also what makes it the funnest thing.

(00:08:52):
If you think about why do we do this? Somebody once asked me, "Would you retire? Why do people do what they do?" Because certainly at some point it isn't just about the money and at the end of the day product management is so damn fun because it's about trying to figure out an edge. It's like trying to look at the world, find the portion of the chessboard that isn't occupied, but that is valuable and find a way to get into it, invade it and destroy it. It's decisions under uncertainty and that makes it unbelievably fun. Really, really painful and very frustrating and very hard to convince people, but very, very fun. So in equal measures basically.

Lenny Rachitsky (00:09:33):
What's the answer, Shaun? How do we solve this problem? I know you said it's your life's work. What do you find actually helps most in helping PMs level up and become say 10 X PMs?

Shaun Clowes (00:09:43):
I think the most important thing and the chestnut that I repeat to everybody is that at the end of the day, the time you spend looking inside the building doesn't really benefit you very much at all. And Steve Blanken, people used to talk about you should be spending 80% of your time thinking about things going on outside the building. You might not be outside the building, but you should spend 80% of your time thinking outside the building. And I would say that very small number of PMs do that. They get dragged into internal politics, they get dragged into scrum management or scrum execution or product delivery, like elements of the delivery thing and you just can't win that way. You just can't win that way. You can never get an A because you're fundamentally not solving the job. The job is not about execution or anything, it's about finding reliable, differentiated value that you can uniquely deliver into the market.

(00:10:33):
So I would say if there's one thing, two things I would say actually that I generally guide product managers to do, one is to always start from the point of view outside the building in every document in everything, always talk from the customer's perspective, from the market's perspective, from the competitor's perspective, and the people who listen to me on that I would say get better almost immediately because they're starting from a place that's easier to understand and then secondarily be data informed.

(00:10:58):
They use all of that view of the world, but don't just make up a bunch of statements, support that statements with anecdotes and bits of data. It doesn't have to be a treatise, but convince everybody of what the world really looks like and what the opportunities ahead of the company looks like and good things happen to you. And all of a sudden you go from a world where nobody wants to help you get anything done to where everybody wants you to win. They want you to win and they may not give you everything you want, but they certainly will try because they're like, "Well, of all the bets we could make, this is a good one."

Lenny Rachitsky (00:11:30):
I imagine many people listening to this are thinking, "Oh, I am that person. I talk to customers all the time. I'm always interacting, looking at research, putting data together." And what you're saying is you're probably not doing that enough. Is there anything that you could help someone recognize of, "No, you're actually not doing this enough and you think you are but you're not."

Shaun Clowes (00:11:50):
It's one thing to say you're spending a lot of time looking outside the building. It's a whole other thing to hear from the places you don't normally hear from. So avoid availability or confirmation bias. Most of the time people go talk to the people they always talk to and they learn nothing particularly new. They don't synthesize the results that they got from that conversation. They don't seek out the counterfactual, they don't seek out the proof that they're wrong. They don't analyze what their competitors are doing and figure out what that must tell you about the market. They don't bring back the data of how their product is actually being used versus how people say it's being used. It's like all data and no analysis is not very useful. Everyone can bring back an omnibus edition of random stuff I heard on a Tuesday, but the competitive advantage is extracted out of figuring out what other people don't see, figuring out where we are wrong, figuring out where a well-placed bet could have dramatically outlandish returns.

(00:12:49):
And so I think firstly, people often say that they do a lot of this stuff, but they actually don't because they don't have any structured way of doing it. So what they really mean is every now and then I get in a customer call or every now and then I get stuck into an escalation. And so they're kind of conveniently bucketing it. So firstly they don't do it in a very structured way, then they don't bring back analysis, they get true insights from that thing, so they don't really gain very much at all. It's just more activity, no outcomes. People do far too much activity with not enough outcomes and there just isn't enough time in the day to do that to be successful.

Lenny Rachitsky (00:13:24):
You as a product leader is at the Venn diagram center of the sweet spot of where this podcast has been going recently, which is product and growth and how AI helps you with all these things. And so to follow a thread there with synthesizing and understanding what people are saying, user research and surveys and all these things, have you found any tools that you and your team have found really useful to help you do this more efficiently versus traditionally just manually going through all the stuff and finding patterns?

Shaun Clowes (00:13:55):
Yeah, so firstly, stepping back a little bit just into the motherhood and apple pie portion of qualitative research or whatever, I find that most people don't even understand or don't start with a rigorous foundation in what they're going to need to do to get the answers that they want. So for example, your listeners have probably heard about the Nielsen number before, but basically the idea is that once you interview between 7 and 14 people, you stop learning new things. Less than 7, you don't learn enough, more than 14, you start learning anything new. And so if you interviewed two people, you probably don't have enough data. If you interviewed 22, you probably had too much, so they don't even right size their efforts. So that's a problem. So they don't start that way. Then they go into these conversations asking leading questions, which really are designed to get the customer to say what they already want to be true, which is so they haven't done enough research or they've done too much and then they've blown up all of the results before they've even heard anything.

(00:14:48):
If you don't right size your research and you don't set this up to learn, then you're going to lose. No amounts of applying LLMs or any type of kind of structured reasoning is going to help you. Because you just basically you're reading back what you want to hear or some weird summarized version of what you want to hear. But stepping back from all of that, what I like to do specifically getting to LLMs is I think that we live in just the most amazing time for product managers right now in terms of being able to analyze vast quantities of information and see the common threads. And so let me give you few examples of that. One might be you can do a bunch of customer interviews, you can put a bunch of customer interviews into ChatGPT and you can say, "Hey, ChatGPT, this is my strategy. Tell me where my strategy does not fit what these customers talked about."

(00:15:40):
It's all about the not, not where it does, where it does not. People spend far too much time looking for what they're hoping to see, not for what they're not looking to see. So you can literally ask ChatGPT to help you find where the customer is probing at the edges of what you're trying to do, where it's wrong, where what you're saying is not what they believe. And you can ask it questions like that. You can ask it what your customers are saying would better fit what your competitors are saying. So you can basically say, you can copy and paste one of your competitor's positioning documents into ChatGPT and say, "Is this a better fit for what they have said than my thing?" Which is you can summarize your own strategy, you can take your competitors but public documents and you can ask it to summarize what their strategy probably is.

(00:16:22):
And it's actually supposedly good at that because mostly your public documents are actually a summary or at least they're derivative of what your strategy is. So it will give you crazy insights into what other people's, literally their product strategy at times creepy like, "Oh, they will probably do this, they will probably do that. It's more likely they would do this than they would do that." And so normally that type of insight was hard one, it took a lot of sweat work. You basically get to read a lot of stuff. You kind of had to use your brain as this big summarization machine and eventually you knew what you felt about all the things you had read, but you couldn't summarize why. LLMs let you get to that really, really, really quickly in a very structured way, but only if you push at the edges, provoke the answers you don't want to hear, provoke the problems, try and prove to yourself that you are wrong, I think is the easiest way to start trying to use some of these tools.

Lenny Rachitsky (00:17:15):
I love that. And it sounds like in your experience you're just using straight-up OpenAI, ChatGPT, Claude, not any specific tool for user research for this specific use case.

Shaun Clowes (00:17:26):
No, mostly I find that the straight-up LLMs themselves are good enough and we do have some internal tooling that we built around, I don't know if you've ever had Sachin Rekhi on the show, you may have. He was a product leader pretty well known in the gross community, and he was a leader at LinkedIn for a long time and he used to call this concept a Feedback River, and he basically said that really smart product managers are constantly swimming at a Feedback River. They set out to surround themselves by Feedback River and I really deeply believe in that. It's like, "Okay, how can I surround myself with user interview data, with direct customer feedback, with NPS data, with competitor information?" Like I'm always trying to wash myself over with information. And where I'm going with this is that LLMs and tooling based on it can be exceptionally good for this.

(00:18:20):
So for example, at Confluent we get a ton of inbound customer requests, as you can imagine coming from the field or directly from customers. We use LLMs to take in those asks to summarize what they're about, to find other asks that are like that one, really in a compelling way, a real way, like a semantic way, not other words, exactly the same, are these the same concept? So that we can look across all of the inbound demand on us and say, "Well, the most popular idea is this one and is getting more popular. The least popular idea is this one. It is getting less popular." In a really deep rich way, even across hundreds or thousands of pieces of inbound feedback. I think it's a really great time to be a product manager if you can put these types of tools to work, but they don't do the job for you, they just help you do these things that are intricate in that job of finding the gaps, finding the opportunities, finding the common threads without necessarily having to do all of it just inside your wear-wear, just inside your brain.

Lenny Rachitsky (00:19:21):
I'm going to stay in this AI river that we're in right now and ask a couple more AI-related questions. And this may be what you just said, but I'm curious if there's more here. You kind of have this hot take that the way AI will most impact product management is data management and data versus models you're building or anything else. Can you talk about what you've seen there?

Shaun Clowes (00:19:40):
Yeah, I mean, I think there's two implications for people as they're building products based on AI and as they're thinking about AI in their workflow. So let's start with the first one, because that's how product managers do product management things. You just asked this question of should it be specific tools built to make AI easier for product managers to use? Or is it in fact more general models being put to work? At the end of the day, these models are very, very, very smart, but they're also insanely dumb and everyone knows that, insanely dumb. In other words, they really only know what they were trained on or what you bring to them right at that moment. In that millisecond, and then they will forget it immediately. And it's very easy to convince yourself that isn't true, but it is actually what really matters. And let me add one extra piece that makes that really important.

(00:20:28):
At the end of the day, information has a decay rate. So think about customer feedback, it has a decay rate or what your competitors are doing has a decay rate. So any new piece of data decays in its value to your decision-making very, very quickly, very, very quickly. You can plot your own decay chart if you want to, but the answer is very, very quickly. And so when you think about the job which is synthesizing all of this very complicated information to make good decisions, what does that mean? Well, you've got this synthesis machine, which is this LLM thing that's going to help you do synthesis, but if it hasn't got all that data to do synthesis on top of, it's got nothing. And so that means that LLMs can only be as good as the data they are given and how recent that data is. They're ultimately like information shredders.

(00:21:11):
They are limitless information eaters. You can never have enough information to give to an LLM to truly gain its value. The more things you give it, the better it gets. Broadly speaking, that's just not perfect, but that's close enough. And so what that means is as an internal product leader or putting LLMs to work, you need to figure out how to bring as much information about customers or their asks or your competitors, all of it. How much can you find all of it and bring it together and give it to the LLM either in your tooling or even in just copying and pasting or whatever your flow is going to be, that's one thing. But then if you take it beyond that and you go, "Okay, well now I'm a product leader and I'm building an app and I want to put AI in my app, what will make my AI experience really great?"

(00:21:57):
It's definitely not going to be the models because these models are mostly going to be somewhat replaceable. And you could say, "Okay, well, is it going to be the prompts?" Maybe, but certainly good prompts are better than others, and that's kind of an ongoing investment you'd probably want to make to ask better questions to get the LLM to deliver better answers. But it's obvious that the real answer is the context, all the context you're going to give it, all the data you're going to copy and paste. And so if you think about, let's say I'm building a, I have no relationship to this, but let's say I was trying to build a human capital like a HCM bot, like an AI bot. Let's say I was working at Workday and I was trying to bring an AI bot. It's pretty obvious that the smarts of the bot would really be related to all of the employee information, but not just that, it would be the benefit's information, it would be the legal situation in the country where that person is currently working.

(00:22:47):
It would be the company's policies and procedures that apply to it. So you get what I mean, by about these kind of the jumps of logic and the jumps of data and the way data is all linked together. If you want to have a smart AI experience, you'll convince yourself that all I really need to do is get a model and wire it in and I'll build a little pipeline that will suck some data in and it will whack it into the LLM. And if you think that way, you're going to be very sad, very, very sad for a very long time because you are constantly going to be wrestling with how do I get data to this thing? How do I get good data to this thing? How do we get timely data to this thing? How do I get well-structured data to this thing?

(00:23:21):
And so it's a data management problem. It's getting access to good data, getting access to high quality data, getting access to timely data and getting it to the LLM to get the LLM to make a smart decision. That's where 90% of the calories go. Maybe it's a bit like Einstein's thing, "It's 10% inspiration, 90% perspiration." Nobody wants to hear it. Everybody wants to just think about what these really cool models and how smart they are, and the next one will be even smarter. But really it's just the hard work of getting really good data to the LLMs to get them to do good things.

Lenny Rachitsky (00:23:51):
It sounds really obvious as you make this case. It makes me think about at the Lenny and Friends Summit, Mikey Krieger talked about how he had the two types of PM groups within Anthropic. One was focusing on user experience product and the other was working on the model research side, and they realized that all of the success came from the model research work, like making the model and the data they provided the model was where all the value came from, not just optimizing the user experience and they're just putting more and more of their product team on just that versus tweaking UX and buttons and things like that.

Shaun Clowes (00:24:27):
Yeah, exactly right.

Lenny Rachitsky (00:24:29):
Something sort of related, I'm just going to ask one more AI question. I don't want every talk to end up being just all AI, but something that's kind of been a meme recently, and I know you have a perspective on this, is that AI makes it really easy to build products. So in the future, if you can easily clone, say, a B2B SaaS app like Salesforce or Atlassian or whatever your favorite B2B SaaS app, what happens to these businesses long-term? Do they just become, are they all in trouble? Are there going to be 100 Salesforce competitors? What's your sense and prediction on what might happen there?

Shaun Clowes (00:25:03):
Yeah, I think it's really weird. I think people really underestimate where the value is created in these applications and they just kind of get it completely wrong, and I'm not sure why that is. So if you think you bet. So I spent a long time at Atlassian, so I worked a lot on Jira, which many people know, and I spent a long time at Salesforce, so I spent a lot of time in the CRM ecosystem, the marketing ecosystem and all the rest of it. If you want it to be not charitable, you'd step back and you'd look at all those applications and you'd say, "They're all just forms on databases." You'd say, "The Jira is a form on a database, Workday is form on a database, so Salesforce." They're all forms on databases, all vertical SaaS or business SaaS is ultimately forms on databases. And you're be like, "Well, how hard can that be to replicate?"

(00:25:45):
And the answer is unbelievably hard, unbelievably hard. And people just think, "You totally get it wrong." Because it's not actually just about the data model. So if you think about, if it formed some databases, it's these beautiful user experiences that sit on top of data models. So whatever the object is, it might be a customer object or a campaign object or an employee object, you could say that, "Well, there's some elements of lock-in in the object, the object itself, like the fields of the object." I'm like, "Pretty boring. That's not very interesting." But sure, maybe. Certainly there's some value in being the system of record like the default that everybody uses. There's definitely some value in the UX. Like, "Well, I want to be the best HR-facing applications for working employee data." Yeah, there's some value there, but the real thing just staring at everybody in the face is it's all about the business rules.

(00:26:35):
That is what drives the lock-in because why do you buy Workday? You don't buy Workday for its out-of-the-box configuration. You buy Workday because you want to configure it to be Lenny Inc's HR processes. It becomes Lenny Inc's Workday. It's not Shaun Inc's Workday, it's Lenny Inc's Workday. And actually the longer you have the software, the more it becomes that, the more it becomes less and less like Workday and more and more like your specific company. Which makes sense because it was built to be configured to meet the needs of any specific company, and every company is their own precious snowflake. And as that happens, those configuration pieces, the bit that makes the application native and a fit for your organization makes it a fit for nobody else's organization and also makes it a black box to the point that you don't even understand how it works anymore.

(00:27:20):
If you went to, for example, Salesforce and you said, "Hey, could you define all of the processes by which software was sold inside Salesforce?" They couldn't tell you that without reading the code of their Salesforce instance. That's not a proprietary secret. That's obviously true because over time, that's literally how sales happened. There is no other way to do a sale other than through their internal tooling. And so what that means is that it's not the UI that matters and it's not the data model that matters, although those are both very useful. It's the years and years and years of evolution of the underlying workflows of the product to support the customers, but also the customers evolving those workflows to make them work the way they do. And so how does that impact AI companies? You could say, "It's easier than ever to build forms on a database application."

(00:28:09):
And so I'm like, "Yeah, okay, that presumably drives the incremental value of every new one of those to zero, right?" So probably leads to more power to the existing winning systems of record because there'll just be a gazillion competitors who would just more form some databases. So like, "How would you ever choose between them? You may as well just go with the winner. Nobody ever gets fired for buying Salesforce or whatever. You may as well start from the kind of the premier vendor." That's one element. You could go the other way and you could say, "I've heard a few people mount this argument," which I think is really interesting that at the end of the day, agents are going to take away most of the use of that user interface.

(00:28:44):
So let's say for example, your Salesforce with Service Cloud, I've heard people say, "Well, a lot of those service agents might end up being replaced with agentic workflows. That will mean that there is no person operating the UI. If the UI doesn't even exist anymore, then why do you even need Salesforce? We may as well just have raw database tables on who even needs forms of databases, you can literally just have databases." But that also doesn't make any sense either because the agents have to operate against the rules of the system and the rules are defined by the business processes. So think about Salesforce without a head. Imagine Salesforce had no UI, it would still have those business rules that I was talking about. And those business rules are what define what the agent should do. They're almost telling the agent what it should do and how the world can operate, what is possible, what is allowed. And so from my perspective, this idea that this just completely destroys the differentiation of these kind of business process SaaS applications just seems like a fantasy, a crazy fantasy.

(00:29:42):
The only way I could really believe it is if you said, "Well, you could have a new startup that introspected all of the rules that are configured into a Salesforce to try and reverse engineer what your actual business processes are and then kind of operate on top of that." But the best place people to do that would be Salesforce themselves or Atlassian in Atlassian's case or Workday in Workday's case. I just can't see a world in which this... I think one of two things could happen. All this moving to AI makes those applications even better, even more unassailable, they basically get stronger. It makes us stronger or it could enable some new level of applications that come from a more platform based thing, so less a domain specific thing like you ACM or ERP or engineering or less of the domain specific stuff.

(00:30:36):
It could enable a more platform like play where you have more business objects and business objects have rules. And you could imagine a world in which there's kind of a whole evolution of new more platform like SaaS applications that do more than one business function worth of the business rules and the way things move around in the enterprise, but that doesn't exist today. So you could say that that could exist and it could say it could be way better than we've ever thought of because of AI. Or you could say that the rich are going to get richer. The most likely outcome is that the currently dominant companies are going to get more dominant, but I don't think this idea that it would just cause a spring up of a whole bunch of new apps that will more easily challenge the incumbents makes any particularly, it's not straightforward to me how that would happen basically.

Lenny Rachitsky (00:31:18):
Wow, that was extremely fascinating and there's so much there. I can go in so many directions. One is I thought you would actually go in this direction, which is distribution advantages become even more important if it's easy to... Like today, I could sit there and hire team clone. Salesforce might take a while, but I could copy it, but by the time I'm done, they've evolved, they're moving, they're adding features, they're ahead, right? You're skating to where the puck was. And so if that's the case, one of the advantages, one of the ways to get anywhere is to have some kind of distribution advantage. It's one thing to have Salesforce as a product clone, another to get anyone to know about it, to adopt it, to sell it, procurement, all that stuff. Do you have a sense of distribution advantages being even more valuable in that world?

Shaun Clowes (00:32:05):
Yeah, I mean, it certainly makes sense. Ultimately, at the end of the day, distribution is always an advantage because the hardest problem is to even be in the consideration set for any given problem. The world is full of problems. It's just when people have that problem, they firstly don't think they're going to solve it at all. And when they do think of solving it, they don't think of you. So distribution is always an incredible advantage. But again, in the world of AI, it seems like distribution is more likely to get hard than easy. So if you think about, for example, diminishing returns on cold email because cold email is getting easier and easier to send even worse spam, it sounds better, but it's effectively causing everybody to become desensitized to everything. I don't know if you've noticed, half the LinkedIn charts now are all basically clearly LLM generated spam.

(00:32:50):
I mean, to some degree it's actually worsening the signal-to-noise ratio. And so I think that a lot of the breakthrough distribution mechanisms that startups often use seem to be getting more crowded just in general and more expensive. That doesn't bode well for, "I'm the not as good Salesforce," "I'm the not as good Salesforce, but I'm cheaper." It has to be something different. There has to be some angle upon which you are materially better. And what I saw happening and what I've been seeing happening, and I think it's been really interesting is a lot of modern next-gen applications bringing data as a first-class citizen into the workflow. And I think that that's pretty compelling. So if you look at the next-generation of applicant management products that deal with inbound job applicants, a lot of them now like the latest core ones, they include your time to fill data, they include outcome data of who's got the best hiring outcomes, who over what period of time has the worst attrition, literally all the way back to the interviewers and where the interviews were in the interview cycle.

(00:33:58):
So basically embeds data into the whole life cycle. So I think that there are these ways in which startups can bring these experience benefits by just bringing a different approach to the world that does enable them to capitalize on traditional disruptive innovation. At the end of the day, this is just disruptive innovation. It means that most companies have overshot the utility like the average utility, so you can win by meeting the average utility and being different, meet the bar and be different. Meet the bar and be different is the way to cut through. So that makes sense if that's a half decent playbook. But even for those companies, now they're going to have all these AI competitors who are using AI to engineer faster, to build a competitor just like them as quickly as possible and start jamming it into the channel. And it's going to be interesting to see how this whole thing evolves. It kind of got race to the bottom characteristics around it. You're probably right, the distribution is still the hardest part in software, particularly when you're getting started.

Lenny Rachitsky (00:35:00):
So if you have some kind of clever and fair advantage, it feels like that becomes even more powerful. Say have a platform of an audience or something like that. You mentioned this ATS product they really like. Is there one you want to give some love to that you think is really cool that you like or you want to keep it anonymous?

Shaun Clowes (00:35:16):
Yeah, it's Ashby. It's the one all the cool kids are talking about now. And it's funny because people literally talk about it in comparison to all, even the last generation of modern SaaS ATSs or whatever, and they talk about it in glowing ways because of the way they put data inside the actual workflow. So the actions and its outcomes are directly tieable to each other in the application you're doing the work in. I think that's a pretty compelling user experience.

Lenny Rachitsky (00:35:41):
So just to maybe close this thread before I move in a different direction, this point you're making about how valuable data is and how that's at the core of being successful and differentiating in the future, especially with AI tooling and products, any advice you'd give to someone that wants to do that? Is it just make sure you have a, is it half proprietary data? Is it like make it a first-class citizen? What's the advice you'd give to founders who are trying to do this, which you're suggesting?

Shaun Clowes (00:36:08):
Yeah, I, think at the end of the day, it's kind of all of those things, isn't it? If you have first-party data but you can't bring it to bear, then it's not very much use. If you have third-party data and you bring it to bear in interesting ways, the problem with data is we're all surrounded by data all the time. So the data's everywhere. What really matters is the right data at the right time in the right place because we're all humans. And so to me, there are obviously data advantages and there are even data network effects if you can end up in a situation where you have very valuable first-party data. But in any case, it's still about being able to bring the right data at the right place, at the right time for those users, for them to be able to get advantage from it.

(00:36:48):
A little kind of segue I guess on that one is I know I spent a lot of my career, weirdly, actually I've been a product person for a long time, but weirdly I've ended up inheriting data teams. So I've actually run data teams at a lot of different companies, which is weird because product managers don't normally own data teams. I think I have just a really massive affinity for data. I used to call myself data-driven, it was kind of my jam. And in hindsight, I look back and I think data is the opposite. Data is more like a compass than a GPS. If you look at data as a way of giving you the answer, you're always wrong. You're always wrong or you're slow. Wrong or slow or sometimes both, because mostly data doesn't give you the answer. It just tells you if what you just said is ridiculous or there's potentially something there.

(00:37:44):
So it's more like about disproving whatever you think and you end up being slow because if you try and use data for everything, your brain is ultimately a data sifter or whatever. So the reason your intuition tells you something is because you've seen a ton of data that tells you that this is the most likely answer. And so being data-driven, being data obsessed is it's something you can easily overdo very, very easily overdo. So it's about right-sizing data, having the right data at your fingertips, having the right kind of view on data rather than trying to expect data to give you the answer or trying to use data as a weapon or trying to use data as a way to force people to believe you or to go in your direction. But data is kind of at the center of everything and about how to influence and be successful in products you're building and arguments you're mounting internally and everything else.

Lenny Rachitsky (00:38:34):
I love that you went there. I definitely wanted to spend time on here. It's interesting you say that, there used to be data-driven, [inaudible 00:38:44] data-driven. You created the Reforge course, data for product managers and also retention, engagement course and Reforge. And by the way, we'll link to these. You're still helping with these courses. By the way, they're still running. They're awesome. People love them.

Shaun Clowes (00:38:56):
Yeah.

Lenny Rachitsky (00:38:56):
Great. So we'll point people to those. I love that you're also saying you're like, I think the way you described it to me before, this is your reform data-driven PM. A lot of people say this, they're like, "Don't just do what data tells you to do. Use your intuition, use it as a guide." It's hard on the ground to operationalize that advice. Say to your PMs and your teams when they have data telling them, "Hey, this experiment is a huge success, or there's a huge onboarding conversion opportunity here." I guess just like what's your tactical advice to folks that have data telling them one thing and maybe something else telling them something else?

Shaun Clowes (00:39:35):
I think the first thing I always encourage people to do is to look at a piece of data. If you're looking at a piece of data and the result tells you something that your intuition tells you is insanely wrong, like they probably not right. First, believe your intuition and go and prove yourself right. Don't just take it at first glance because most of the time it's like Occam's razor. The most likely explanation for something that is insanely not intuitive is that it's just wrong, that there's a problem somewhere. Now, occasionally, sometimes you actually will be right. Now those will be paid dirt moments. Those are the moments that make it all worth it. There are times when you do find the negative goal, you're like, you're staring at it and like, "This is it. This was the problem. This was the thing we were looking for this whole time."

(00:40:18):
But you have to be very diligent about following it through, really understanding what you're looking at. Is this data representative? Is this data a good sample of the audience we care about? Is it already subject to some sort of selection bias? Oftentimes when I see analysis from different product leaders or even data teams, you can drive a truck through it, literally drive a truck through it. And if you present data with authority and that data is ridiculous or the analysis is just full of holes, you don't just not get benefit for that. You lose a whole bunch of brownie points. It would be better not to show up with an analysis that isn't clear than it would be to show up with an analysis that's dumb. And I see people self emulate on this actually relatively regularly because they just bring a knife to a gunfight or whatever, they did bring in an analysis that is just not, it doesn't hold water and they present it and then get shot down live, which is nobody's idea of a good time.

(00:41:21):
So if I give you a little bit of additional tactical things about that, it'd be okay if I'm looking at a piece of data, what was upstream of this piece of data and does that look normal? So this thing happened or whatever, which you're very, very excited about, what happened before that? And does that match what you think should have been right? So what happened before this momentous situation? And then, okay, for that thing that you're looking at, what happened after? If you have an idea of what happened before and after, that gives you some idea of whether or not this thing, is it all worth interesting to talk about? And then go one click above this data that you're looking at. So it's like, these things, let's say I'm looking at onboarding success. Let's say I'm looking at onboarding success to second week retention or something like that.

(00:42:05):
I'm like, "I have found this thing that totally crushes it. This intervention crushes it." If you go upstream and you find out that this intervention only applies to 2% of the inbound onboarding stream, it's meaningless. It's most likely just a random aberration. But even if it was not a random aberration, it's not a useful tool. And so you've got to go up and then you might go downstream and you might find, yep, they last for two in the second week, but in the third week they all churn. They're basically pointless. Why are we even talking about this? Or then you might step all the way back and go, "Okay, yes, those people do get retained for longer, but their average ASP is smaller." Because what we really care about, we do care about engagement and we care about more customers, but we want to keep the customers at a high ASP to reach a certain revenue goal.

(00:42:46):
The final goal is happy customers paying us money. So that's what I mean about going a click up. If you go a click to the left, a click to the right, so before and after and then a click up and you still see the thing that tells you the story that you want to tell, then now you've got something that's very compelling because people want to hear about that. They want to hear, "Well, what did happen before? What did happen after? And why is that outcome happening?" But you have to really do your homework and really be rigorous about it to avoid fighting fool's gold.

Lenny Rachitsky (00:43:15):
I love that advice. ASP, what does that stand for by the way?

Shaun Clowes (00:43:19):
Oh, average sale press, [inaudible 00:43:22] MRR or some other revenue metric.

Lenny Rachitsky (00:43:25):
Got it. This point you made about how a lot of times experiments show positive and then they end up not being anything, I had the head of growth from Shopify on the podcast, and they do this really cool thing where they keep holdouts for years of cohorts and then it auto emails them I think a year or two later, "Hey, check this and see if these cohorts, this is still higher or not." And 40% of the time, it turns out neutral after a positive experiment long term.

Shaun Clowes (00:43:50):
Interesting. It's really funny because the last time we did something similar, we had a global holdout group actually that was held out of all experiments. The experiment platform couldn't target that group at all. So 10% of all people never saw anything ever. So that's be really, really helpful because you can always compare them against whatever the experience was for any of the same vintage of cohort. I agree with you. But the other thing is I don't really love some of that thinking process just in general.

(00:44:14):
It's like, "Hey, let's say an experiment does show a temporary benefit. If an experiment shows a temporary benefit, but that benefit does not persist forever, does that mean the temporary benefit was never worth it? Or does that just mean the temporary benefit was an opportunity to reach another level you just didn't capitalize on?" I don't think there's a perfect answer, is what I'm trying to say. I don't think that the fact that a benefit doesn't last forever means that you failed. But I agree with you that not trying to understand, well, what has the net benefit been, what has the net lift been is also really important too. That's why growth is so hard. Growth is part of product is so especially hard.

Lenny Rachitsky (00:44:49):
Marketers, I know that you love TLDRs, so let me get right to the point. Wix Studio gives you everything you need to cater to any client at any scale, all in one place. Here's how your workflow could look. Scale content with dynamic pages and reusable assets effortlessly, fast-track projects with built-in marketing integrations like Meta, CPI, Zapier, Google Ads and more, A/B test landing pages in days, not weeks with intuitive design tools, connected tracking and analytics tools like Google Analytics and Semrush can capture key business events without the hassle of manual setup, manage all your client's social media and communications from a unified dashboard, then create, schedule and post content across all their channels. If you're working on content rich sites, Wix Studio with no code CMS lets you build and manage without touching the design. And when you're ready for more, Wix Studio grows with you, add your own code, create custom integrations with Wix made APIs or leverage robust native business solutions. Drive real client growth with Wix Studio. Go to wixstudio.com. So you built the first B2B growth team when you were Atlassian, correct?

Shaun Clowes (00:45:56):
Yes. Yeah, it makes me feel like an old person, but yes, it was a very long time ago.

Lenny Rachitsky (00:46:00):
Slash maybe it's a new thing.

Shaun Clowes (00:46:01):
Yeah.

Lenny Rachitsky (00:46:03):
It's either a long time ago or it's just recently figured out this is a thing that you could do in a B2B is focus on growth.

Shaun Clowes (00:46:11):
Yeah, it is. So that was around about 2012, and at that time growth hacking was a thing. People don't really use that term anymore, but in B2C it was a very big deal because people could see Facebook doing their 10 friends in seven days and they could see this kind of thing that was working for people. And they're like, "Man, that's amazing." And at Atlassian we set out to go, "Okay, well, do those techniques work in B2B?" And also, it's kind of obvious now that a lot of them do and that it's worth doing. But at the time it wasn't that obvious because for a lot of B2B companies, I mean, you summarized it earlier, Lenny, distribution covers all faults. Almost all ills can be filled in by really great distribution.

(00:46:52):
If you have a really good marketing, a really good ground game, and you're kind of jamming your product into the channel, you're jamming your product in front of people and you're papering over the ugly parts with customer success people and services and consulting and whatever, that people will buy almost any software or you can certainly be successful with a lot of different software. But back in 2012, it wasn't clear of like, okay, which instead you went at this differently and you've heard them in software that sell itself, is the juice worth the squeeze? And now I would say that it's pretty clear that the juice is worth the squeeze to the point that lots of think about this all the time, but it was a bit of an interesting time at that time.

Lenny Rachitsky (00:47:34):
And that was essentially the beginnings of product-led growth. Is that a simple way to think about it?

Shaun Clowes (00:47:38):
Basically it's now called PLG, but yeah, at that time we didn't even know what to call it exactly.

Lenny Rachitsky (00:47:42):
Just growth. So based on that experience, a lot of B2B companies now have growth teams through investing in growth, what makes a great growth team in B2B? Any pitfalls you often find folks fall into that you think they should try to avoid?

Shaun Clowes (00:47:57):
Ultimately, a lot of these types of endeavors are a matter of balance. So what I mean by that is growth teams tend to go through a set of phases. Their first phase is proving their value at all. So call that the gold rush phase. This thing's probably not worth even doing. Why are we doing this, merry band of people out there trying to prove that there's some growth effect somewhere? So that's the proof of phase. And so the advantage of that phase is life's good because there's usually a lot of growths to be found because nobody's gone looking before, so life's good. But it's pretty random because you're just literally searching across a random search phase going, "Have we tried X? Have we tried Y? Have we tried Z?" Then once you get that model going, then it starts to be, "Okay, how do we scale this thing? Is this just a flash in the pan? Do we just find a little bit of low hanging fruit and there's nothing else here, there? Is this just a project we should have done rather than an ongoing thing?"

(00:48:52):
So you have to make it a system. You have to prove that it can be repeated, and then you have to scale it. It has to become a thing. It has to become part of your DNA. You have to be taking a PLG lens to everything you do, all the way from paid acquisition to activation, retention, engagement, cross product expansion, upsells, I mean, you name it, all the different ways you can grow a product by revenue or engagement. There's many different ways to go about that. And so you end up having to scale out and be able to do all of those different things. And then you have to figure out how you fit in with the rest of the organization because there's other people who build products all day every day.

(00:49:27):
There's other people who sell that product all day, all day. There's other people who market that product all day, all day. And so growth organizations are in this interesting space, they're in between everybody else. They're in everybody else's sandpit in a little bit, in a little way, and they're kind of at the edge of everybody's full-time job and they are very valuable, but they can be complicated because of all those relationships, and because of the way they sit amongst all of the other parts of the organization. So many organizations fail because they don't really find much the wins or when they do find wins, it just seems totally random. Or they do find a lot of wins, but they all can't understand them because they seem like they're just a random walk through a bunch of potential opportunities. There's many different ways to fail to fit as you go through your growth phase from trying the ideas to success, to scaling, to operationalizing.

Lenny Rachitsky (00:50:18):
One of the biggest memes along these lines is a lot of companies claim there's like just PLG rarely ever works. You always, either you try it and it just doesn't work or it eventually just peters out, I guess. Any thoughts on just what are signs that your product has a chance to work, peel product-led growth versus just go straight to sales immediately and don't even worry about this?

Shaun Clowes (00:50:44):
First let's examine the counterfactual, right? So let's start with the opposite of your question and say, "Hey, how would the world be sadder if we all just gave up on PLG?" We just said, "Hey, there's no point in doing it in B2B SaaS." The problem is that there is not a natural force that pulls companies towards thinking about the end user's enjoyment and success early in their journey. There is no natural force, there's no natural kind of a link force. Why is that? I mean, 101, the buyer is the most important person. The economic bar is the most economic person. Their needs are the number one thing. They're usually the person driving the RFP. They're usually the person dealing with the sales organization. So the needs of the person who you hear are usually all feature-driven and they're not from the end users.

(00:51:34):
And so you're kind of sowing a seed of your own demise if you don't think about that end user. But it's one thing to say that you should think about the end user, it's a whole other thing to have a system by which you do that because people pay lip service to all sorts of things. But I'm sure you've heard this one before, but in economics, people only do what their incentives told them to do. Broadly speaking, that is what they do, that is what happens. You get what you set out to measure. You get what you give people incentives to do. If there is nobody in the organization whose true incentive is to measure their end user success, their enjoyment, their happiness, their retention, their engagement early on, it will not happen. Or at best it will be a hobby. And so then by extension, if I start from there, then I say, "Okay, let's say it doesn't exist, PLG doesn't exist and therefore it's a hobby and therefore there will be a bunch of hobby people who care about this."

(00:52:23):
Then you ask yourself, "Okay, will that mean that there will be many products for which those experiences really suck? And does that mean that that will be an opportunity for competitors of those products to be better at that? And is that a differentiated competitive advantage?" Yeah, I'd say it is. I'd say it is. And so I just work my way backwards and I go, "Okay, you can say that your PLG investment might be too high." You could be like, "Well, if I invest more, I won't get any more juice. I can't spend my life just experimenting in the onboarding. That's not the only thing that matters." And that's very, very true, but it's very hard to argue it should be turned to zero.

(00:52:59):
And so to me, therefore it's about the balance. It's about, "Okay, how does PLG fit with the other different ways that I grow in my business?" At Confluent, for example, we have a PLG function. We do grow with self-serve signups. People who sign up, literally their credit card, lots of them sign up and they're very successful, never speak to us. We also have an enterprise sales team that sells directly to very big companies, some of the biggest banks in the world, the people you would definitely know of. I don't think it has to be one or the other. I think that it's about a balance. It's about getting the motions to work and for really sophisticated companies, the people who really nail this, it's about making both motions work together. If you can get a PLG motion work to feed your sales team and a sales team motion work to feed your PLG funnel when the sales leads aren't ready yet and you can get those motions into playing with each other, you can make a lot of money.

(00:53:52):
It can be an extremely successful way to go to build a very resilient business. Why? Because you get a lot of customers and you get a lot of revenue. You can't be that successful as a company if you have a lot of revenue, but a small number of customers because you're captive, everyone knows that. You can't be that successful as a company if you have a lot of customers, but not enough revenue because you shouldn't have enough money to sustain operations. So the magic is in having both, a very large number of customers and a very large amount of revenue, it's very hard to knock over a company like that. If I look back on my time at Atlassian, and I think that they shared their most recent numbers, I can't remember what it was, but it was in the public data or whatever, something 80,000 or 100,000 customers, something like that.

(00:54:30):
That's a lot of customers. That's a lot of customers. Let's say you're going up against Jira and you're like, "Yeah, man, I'm going to pick off 1,000 customers from Atlassian." That's a lot, right? That's a lot. Obviously 1,000 customers is a lot. You only have 19, sorry, it's going to be 89,000 to go or 79,000 to go, or however many it is to go. I can't remember their exact number of customers, but it's very hard to assail a company which has a very large number of customers and a very large amount of revenue. And so that's why I think that PLG as a mechanism is incredibly important for almost any type of company, if you can make the motion work. Obviously there are companies for whom the motion just isn't relevant, but for those where it does matter, it seems like the juice is worth the squeeze.

Lenny Rachitsky (00:55:18):
That was an awesome answer. I looked up last year and they have 300,000 customers.

Shaun Clowes (00:55:23):
Oh man, I'm so far off. When I left it must have been 80,000 customers.

Lenny Rachitsky (00:55:28):
They've done good work since then. Also, you're talking about incentives and how the power of incentives. Charlie Munger has this great quote I looked up just to make sure I get it right. "Show me the incentive and I'll show you the outcome."

Shaun Clowes (00:55:40):
Yeah, exactly right. I've seen cases where a sales team was people trying to get a sales team to do a PLG motion, and you can beat them over the head as much as you like, you can get into a meeting and tell them that you really, really want them to do this, but at the end of the day, they're not going to do it. And the same is true for every other kind of function. It's just the nature of things.

Lenny Rachitsky (00:56:02):
I have some newsletter posts around the stuff of folks want to dig deeper. Also, Elena Verna had an awesome podcast episode talking about product-led sales and kind of the combination of these two things that we'll point to.. Just a whole other topic we can go deep, deep on, but we're not going to do that in this episode. Maybe just one more question. So you mentioned all the companies you worked at, so you've been at Salesforce, chief product officer, MuleSoft, specifically within Salesforce, Metromile, Atlassian, Confluent now, a lot of really interesting and different roles. How do you choose where to go work and how do you choose which opportunities to take? I imagine you have many options.

Shaun Clowes (00:56:42):
I have to think of my career. So in hindsight, looking at it this way, Lenny, so I don't know if forward-looking was obvious to me this way. But looking back, my career has been a little bit like a bingo card. I've always been looking to fill in boxes I didn't have filled because I felt like that would make me a better professional. It's like if I didn't know anything about that specific type of sales model or that type of marketing or that type of product management or that type of product or that layer in the stack or that kind of thing is like, well, if I learn about that thing, I will become more versatile. So actually two things, it's fun, it's fun to learn something new. It's fun to prove to yourself that you can do those new things and then it makes you more versatile because it means that any given problem you go up against, you've seen something that pattern matches to it.

(00:57:29):
It kind of feels like you end up bringing a gun to a knife fight in a way because every problem you look at, you're like, "Oh, I have seen this from the other side. I've seen this from some other angle, and so I know that this is likely to work and this is unlikely to work." And so when I joined early on in my career, I was working for a big enterprise software company, sorry, small enterprise software company that sold to the Fortune 100. When I joined Atlassian, and like I shared with you, we had no sales force at all actually at all. Literally nobody to sell the software. It sold itself or it didn't get sold at all. And we grew to have 80,000 customers. It was just pure product. They had growth and just an incredible company. Then it was at Metromile, which was a consumer company that got acquired, made an insurance product for end consumers.

(00:58:13):
So they got nothing to do with technology products, like literally a complicated Internet of things device you installed in your car, but ultimately it's an insurance product that you'd sell to grandmothers in Florida as much as you would ever millennials. And then at MuleSoft to totally back end software that's used by IT organizations and a consulate infrastructure that's used by developers everywhere to build really interesting data-driven applications, data powered applications to do all sorts of things in real-time. And you look at across all that and you go, "It's all a bit random." But I didn't see it that way because I learned, I actually was in sales for a bit, so I ran a pre-sales engineering group, went around the world selling software. So when I joined Atlassian, I wanted to kind of understand what it was to sell software at massive scale with no sales team, can it even be done?

(00:59:01):
And so I learned a lot in my time at Atlassian. When I went to Metromile, I'm like, "Well, I've never built a consumer product before." I can say that I've actually built a product that's touched many millions of people because Jira has, so I felt pretty good about that, but I'd never built one that I could say, "Yep, a consumer, your average consumer can use this thing. It's so simple. Even my grandma can use it." I'd never built a product like that. So I got that experience at Metromile, which is really fun. I'd never worked inside an organization as big as Salesforce or an organization with as good a sales motion. You talked about distribution earlier. Salesforce is an absolutely insane distribution machine, just an incredible company with just an amazing distribution network and a fantastic marketing approach that it's like a PhD in marketing.

(00:59:44):
When you spend your time at Salesforce, you're like, "This company is just one of a kind. It's a one of kind, and it's so outlandishly good at one specific thing." And so looking back, all of these jobs have been, when I say bingo card, I've just got an outlandish education in these areas that are not obvious at all. And once you've seen them, they're like superpowers. They're superpowers to be able to bring that same experience to bear on things. And so one thing that I really I'm trying to figure out is why often people don't do that. And oftentimes people stay in a very specific domain. They prefer to stay in a domain or they prefer to stay in a specific kind of type of company or a role that works in a certain way, like companies that have the same operating model or they plan the same way or they try to stay with things that are pretty similar. But it seems obvious that the most likely way to really grow is the opposite.

(01:00:41):
It's to constantly be choosing things that are either outside that, not totally outside the lines. Don't jump out of a plane if you've never parachuted before. Obviously you want them to be in some way and adjacency, that you want them to have something in common with what you know, but you want them to stretch you and change you. I had a really transformative experience many, many years ago when I was at Atlassian and a guy called Tom Kennedy, he was our general counsel, so chief legal officer basically, and a lifelong lawyer, very smart guy. I liked him very, very much. But just a lawyer. Just a lawyer, corporate lawyer, corporate counsel, I'm sure you know what they're like. And really great guy. And I remember, so mostly in our meetings he didn't talk that much except about legal things. But I remember in one meeting we were having this vigorous debate about a product strategy question about what we should do. Should we go left or should we go right?

(01:01:39):
And as usual, he's there and he's mostly just staying silent. And then eventually the conversation's been going on for 15 minutes and he is like, "Hey, everybody, a year ago we talked about X, Y and Z," and he proceeds to lay out our product strategy at that time, and he's like, "Just recently we said the following things, and that was a product strategy, whatever. Now you are saying this. Isn't it obvious that isn't this? What you guys are saying is not congruent with that, and if you really meant what you said back then we should be doing X." And again, the room went silent, everybody kind of turned to him, kind of nodded, and then everyone went, "Yeah, okay, I guess we probably should be doing it differently." And so the meeting stopped when the GCE randomly mentioned that he deeply understood our product strategy and he knew enough to be able to contribute in that way.

(01:02:24):
And so the life-changing part for me about that was just this realization that if I'm going to be a really great professional, the type of professional I want to be is that type of person. The type of person who can contribute to the whole company in all sorts of ways, doesn't spend all of their time in everybody else's business, but understands the business and has the mental horsepower and the experience to be dangerous in all sorts of, and I mean, that in a compliment way. I don't mean that in a negative way, but to be dangerous in all sorts of situations. I think that when you have leaders like that behind you and with you, then you're just unstoppable. You're an unstoppable force in business when you have that motion happening.

Lenny Rachitsky (01:03:06):
Wow, that was an awesome story and an awesome perspective. It's similar to the advice I always give PMs of people always wondering, "Should I go deep on a specific subject? Should I just try different things?" And I find just variety, especially earlier in your career is really powerful, not just to help you discover the thing you like, but also to your point, just using insights from all these different parts of the product and internal tools and trust and safety and platform and consumer product side and growth and just core stuff. The more of that you have, the stronger you get. And I feel like another benefit of your approach is if you work at just B2B SaaS companies, if you have too many of that on your resume, it's very hard to get hired a consumer company. And so just having it creates a huge optionality for you if you do, which you did.

Shaun Clowes (01:03:57):
Yeah, it's interesting because people used to talk about people who are T-shaped or whatever, and I've never really loved the analogy because it's more like people are scribble shaped. I mean, there's the really best people you've worked with, they're more like scribbles than they are T-shaped because of course you want to be horizontally capable, so you want to be broad and you do want to be deep, but you actually want to be deep in way more than one thing. Now obviously when I say deep, I don't mean I'm not able to do the job of our finance function all day every day, but I'm 100% good enough to go three clicks below the simple financial analysis. I can go reasonably deep in our financials because I want to and because it's partly it matters. It's important to be able to do that. And so maybe a different way to think about that bingo card is I've rarely regretted going deep in something that isn't quite my job.

(01:04:51):
I've rarely regretted it. The worst case scenario is I've learned something new that I will never use, which I guess at least that made my brain slightly more agile. I don't know, there must be some potential benefit of that. But the very best case scenario is that when I least suspect it at some point in the future it will turn out to be the thing that matters. It will be the tool that I need, but I'm facing some important problem and I will be like, "Oh my god, this was worth every cent." And so if you think about it on an ROI basis, doing things that aren't in your wheelhouse, that aren't the things directly in front of you, the ROI can really be outlandish. It can be off the charts great, but I guess it's speculative. Because you don't know you're going to need it tomorrow. You don't know if it's going to be something that's going to be a regular tool you use.

Lenny Rachitsky (01:05:33):
What's interesting is the bingo card is the analogy. Is there a bingo moment at the end of this? Is there retirement?

Shaun Clowes (01:05:41):
Oh, you mean you've got everything. You've got the collectible Pokemon?

Lenny Rachitsky (01:05:45):
Yeah, you collect them all.

Shaun Clowes (01:05:46):
Yeah, I was working with somebody at Salesforce and he'd been there a long time, very, very, very successful person. Honestly didn't need to work anymore. And he said something that I found really useful. He's like, "Well, now I'm at the point of my life where I want to work at the intersection of things that I am good at and things that will be valuable to the company to do." So basically it feels like the reward of completing your Bingo card is actually to just get to spend more time doing things that are leverage, that you enjoy and that are high leverage. And so that seems like a good outcome to me. I don't think most people are going to work and hopefully have some sort of great financial outcome and then go, "Well, that's it. I'm picking up stumps, I'm retiring." I think for most people, achieving some sort of financial outcome or some sort of independence or whatever is really just another stage. At that point it will be, "Okay, well now what do I do? What do I do with my life?"

(01:06:49):
And so that was why I said earlier that at the end of the day, product management is at times the worst job in the world and at times easily the best. And it's both and it can be both. And so it's hard for me to think about if I think about the things that are the intersection of what I'm good at and are valuable to the world, product management is a pretty fun one to do and it's different every day. So I think we're pretty privileged. For those of you who listen, I mean, obviously your podcast reaches a lot of product people. I think we're pretty privileged to be able to operate at that intersection, but it's not easy because you got to show value. It's a very complicated job to show value in and to demonstrate value to the world, and it's constantly being attacked, like you mentioned, but it's still amazing when it all goes right. When a product is very successful in the market, it's hard to describe the joy you get from that.

Lenny Rachitsky (01:07:46):
Kind of along those lines to close out our conversation before a very exciting lightning round, I want to take us to failure corner. People listen to these podcast episodes and everyone's always just sharing all these wins, everything's always going great. The CPO of this, CPO of that, just moving on up and people will want to hear times when things didn't go right. Because those are stories people don't share as often. Can you share a story when something didn't go right, when you maybe had a failure in the course of your career? And if you learned something from that experience, what you learned.

Shaun Clowes (01:08:18):
I mean, there's a lot of things that didn't go exactly to plan, Lenny. Very early on in my career, I was still a developer and I accidentally deleted one of the core systems of the company that I was working at. So that's going to go down in infamy, but luckily that one's far in the rear-view mirror. That-

Lenny Rachitsky (01:08:38):
That wasn't Atlassian?

Shaun Clowes (01:08:41):
No, that was far pre-Atlassian, but very bad. Yeah, the one I like to talk about, I wasn't directly responsible for it, but I feel responsible for it. I was at a company and we launched a product. That was one of those products that in hindsight should have been really obvious it was going to fail, but for some reason we were all blinded by the potential. It was a product that was about, it was basically to measure the environmental impact of your company and to help you reduce the environmental impact of your company by doing, think about it as a power management, building power management, managing the power drawer of computers, managing the power drawer of AC and all of that stuff. That was the vision basically. It's like a manage your environmental impact of your business. The idea was pretty cool at the time, and also it was the right time for that, and it's still a thing.

(01:09:33):
It's still an area of active research and investment or whatever, but it was one of those things, talk about the wrong company, wrong place, wrong time, wrong distribution. We had literally no right to win, no right to play, just absolutely no business in hindsight being in that business. And I feel really bad because I, again, good idea, wrong company. And at the end of the day, we launched the product. We actually kept the product in market for two years, and the final straw was weird. The final straw was actually when a customer finally wanted to pay for it. It had been in market for two years, and we found ourselves with a customer who wanted to pay millions of dollars for it. They were ready to sign on the dotted line, and that was actually the moment we decided to kill the product because we were like, "If this person signs this piece of paper, we are stuck with this forever. This one customer will be bound by contracts for however long or whatever."

(01:10:29):
So we actually ended up killing it. At the moment after two years of failure when somebody wanted to pay his money for it. And I look back on that and I'm just like, "Man, that was a really big..." I feel really bad because I'm like, "It should have been obvious. It was obvious and we should have been able to call a spade a spade and I guess speak truth to power." But instead it kind of got through to the keeper and turned out to be a real accidental drain on resources for years and just a big mistake.

Lenny Rachitsky (01:10:58):
So is the lesson there, just be real with yourself? I like that you have this forcing function of like, "Okay, this is getting for real now." Is it like, "I wish we had an earlier forcing function to force us to make a decision?"

Shaun Clowes (01:11:11):
Yeah. I think if I could do it differently, I might not have necessarily been able to 100% change the decision, but I should have tried. I mean, it was pretty obvious after six months, this thing was a bit of a zombie product walking, and the least I could have done is said, "This thing is dead." We could have called it dead way earlier, but instead we proceeded for another year and a half investing in it. And so that's the bit that makes me feel like real bummer about it.

Lenny Rachitsky (01:11:39):
It reminds me a recent episode with Raaz who is the CMO at Wiz, and she joined us the first PM and a few weeks into it with doing tons of calls with customers she's like, "I think I need a quick... Because I don't really understand what we were building. I don't get it." And everyone's like, "I don't either." And it just, yeah, the founders just had a vague idea what they're doing, but they didn't really have an idea. And that just sparked a, "Okay, wait, no one actually does. Let's actually get more concrete." And it helped them pivot. And now, I don't know if you know about Wiz, but they ended up being the fastest growing startup in history.

Shaun Clowes (01:12:19):
Yes. Isn't that amazing, right? It doesn't mean it's permanently fatal, but asking that question and going through that reckoning turns out that came out stronger.

Lenny Rachitsky (01:12:29):
Scary, but it turns out it's for the best often. Before we get to very exciting lightning round, is there anything else that you want to mention or leave listeners with maybe a last nugget, something that you think might be helpful before we wrap?

Shaun Clowes (01:12:41):
Maybe a couple of different things that I think are sometimes well understood, but just repeating them I guess because they're very valuable to me. One is that if you let your calendar rule you, then nothing good will happen. I know people talk about that a lot, but it's surprisingly common in product management in particular that people end up ruled by their calendar. And so it's related to that whole look at spend 80% of your time thinking about things going on outside the business. Easy said, very hard to do, and if you don't do it, no one's going to do it for you. And so it is really hard to be successful unless you find a way to force that to happen. So to repeat that, also, somebody said this to me, I never looked up the quote, but apparently Colin Powell said that if you're making a decision with less than 30% of the available data, you're making a big mistake.

(01:13:32):
If you're making a decision only after you have 70%, either the 70% or 77%, I can't remember the exact number, when you have 77% of all the available data, you have waited far too long. And I've always found that very insightful and it relates a little bit to what we're talking about about data earlier, but at the end of the day, we get paid in product management to make decisions, good decisions, paid to make good decisions that will deliver business benefit. And a decision with too little data is fatal. A decision that takes too long and collects too much data is also fatal. So everything, it's about trying to find the balance of all of these different things to try and deliver business advantage.

Lenny Rachitsky (01:14:07):
A great way to circle back to all the things we've been talking about. With that, we've reached our very exciting lightning round. Are you ready?

Shaun Clowes (01:14:15):
Yes. Let's do it.

Lenny Rachitsky (01:14:17):
Let's do it. What are two or three books that you have recommended most to other people?

Shaun Clowes (01:14:23):
Yeah, they oldies but goodies, is probably going to be The Lean Startup that I still find actually really good. And the key lessons in there I still think are very applicable to a lot of people, particularly the cohort analysis bit, which for some reason I still don't see people do anywhere near enough cohort analysis. So there you go, that's my little tip. And then INSPIRED: How to build products that people love by Marty Kagan and the Silicon Valley product group. That's an oldie but a goodie. I think it's got a lot of the key lessons of product management in it, even though it's been around for a long time.

Lenny Rachitsky (01:14:53):
Those are some classics. Very cool. Do you have a favorite recent movie or TV show you really enjoyed?

Shaun Clowes (01:14:58):
I'm watching a program. I don't get to watch very much TV, mostly at night. I like to watch things that are extremely light, that just don't at all inspire any element of stress and that are very short. So basically short and funny is basically my thing. And there's a new program on Netflix, I think it's called Detroiters.

Lenny Rachitsky (01:15:18):
Oh, I've been watching that.

Shaun Clowes (01:15:20):
Yeah, it's really funny. I really like that. It's so ridiculous, but very funny. So I like that.

Lenny Rachitsky (01:15:24):
The main guy, he's so funny. I forget his name. Tim Sweeney or something like that. Yeah, he's so good. Good one. I've been watching that, I'm loving it. It's very quirky. I think the New York Times quote on there is "Very weird," the quote.

Shaun Clowes (01:15:38):
It's so weird. In the first episode I'm like, "What is this show?" It's not even clear what time it set in, and it's very weird. It's really cool.

Lenny Rachitsky (01:15:44):
Yes. Well, good way to describe it. Next question, do you have a favorite product you've recently discovered that you really love?

Shaun Clowes (01:15:50):
Yeah, this one, some of your listeners might be using it, but Glean, it's a pretty well-known startup now. They recently raised a ton of money. We've been using Glean at Confluent for a long time and it's just amazing. It's just amazing. I can't describe how good it is. And I don't say this lightly because I think search, like business search is probably one of the hardest problems in computing. Actually getting it right is one of the hardest problems in computing. Amazing. It's not often I use a product and I'm like, "This thing is 10 times better than anything that's come before it." It's one of those for me.

Lenny Rachitsky (01:16:25):
What's the simplest way to understand what it does for you?

Shaun Clowes (01:16:28):
It searches all of our organization's knowledge. So the thing you were just saying before, you're like, "What does AST mean?" If I had that in a meeting, I just open my new tab, it'll automatically take over my new tab or just like, "What does AST mean?" And it will summarize back to me what AST means and it'll give me a link to all the documents inside our company that just grab what AST means and then it will tell me who the expert in AST at our company is. It's like having a second brain. It's an insanely cool organization searching.

Lenny Rachitsky (01:16:59):
Great tip. Okay, two more questions. Do you have a favorite life motto that you come back to share with folks, find useful and work during life?

Shaun Clowes (01:17:07):
I think about this one a lot. When I started off in my career, I was an engineer's engineer. I used to very much about technical correctness and what computers were capable of, and technical righteousness, the right answer rather than there is only one right answer and whatever. It's a long-winded way of saying that I often think about this phrase, which is people don't care what you know until they know that you care. And so I've realized that really being able to influence people, it doesn't matter about whether or not you're right or whether or not you're wrong. And at the end of the day, it's first about trust and about relationships and caring about what each other's outcomes are, what their incentives are, and all good things sit on top of that. Once you have those kind of foundations, then you can build really good partnerships and that's where good progress comes from.

Lenny Rachitsky (01:17:55):
Wow, that is so good. It connects with Radical Candor, similar in theory of just caring. People need to feel like you care deeply about them before they take your advice. And it also connects with this parenting book I'm reading called Listen, that a previous guest recommended, which is all about how your kids have problems when they feel like your connection to them is weak. And so the solution is to build a stronger connection for them to know that you cared deeply about them. So this is really, connected so much of what I've been reading.

Shaun Clowes (01:18:26):
Yeah, exactly.

Lenny Rachitsky (01:18:26):
Great one. Final question. You were born in Sydney, folks can maybe guess by your accent. If someone were to visit Sydney, any tips, anything you think they should check out, favorite thing in Sydney?

Shaun Clowes (01:18:38):
Yeah, Sydney is a really beautiful city and it's kind of famous for its beaches and it's basically a metropolitan city. People probably be very surprised when you visit it. It's a very big city, very metropolitan, a little bit like New York, but New York with really beautiful beaches, if you want to think about it that way, it's kind of crazy. But there's actually a ton of really cool nature and beautiful things all around Sydney. And so if you want to do something like off the beaten path, you can actually go to, there's an area called the Blue Mountains, which is like an hour and a half drive from Sydney, and you can abseil down a waterfall, which is, well actually firstly you go canyoning through a canyon full of water, and then you abseil off a waterfall at the end. And if you're looking for just a really beautiful, fun kind of adventure like thing, an hour and a bit away from a massive metropolitan city, that's my sort of happy place. Really beautiful outdoors stuff while also next to a beautiful city.

Lenny Rachitsky (01:19:31):
And you said you sail, what sort of sail off a waterfall?

Shaun Clowes (01:19:34):
Abseil. You might think of it as rappelling. Rappelling, I think. Yeah, lowering yourself down on a rope or...

Lenny Rachitsky (01:19:41):
Got it. Because when I hear sail, I'm thinking a boat just jumps through over the waterfall.

Shaun Clowes (01:19:47):
Oh, no, abseiling which is also, I think in the States you guys call it rappelling.

Lenny Rachitsky (01:19:51):
Rappelling, yeah. Wow. Very cool. Shaun, you're awesome. This was extremely cool. Thank you so much for being here. Two final questions. Where can folks find you online if they want to reach out? Also point folks to your Reforge courses that you created. And final question, how can listeners be useful to you?

Shaun Clowes (01:20:07):
Sure. Yeah, so my Reforge courses, you can check them all out at reforge.com, as you mentioned, the retention, engagement course and the data for product managers course, so love to see folks get some value from that. Lots of people have been through those courses already and I really get a lot of value from it because like I said, one of my goals is to help all of us be better product people. I think our leverage could be massive. Where you can get in touch with me, obviously on LinkedIn, but also ShaunMClowes on X, if you want to get in touch. And in terms of being useful to me, I mean, broadly speaking, I'm always open to new ideas. If people have ideas about how to do better B2B, PLG, better B2B product-led sales, for example, better ways of going about distribution and product-led sales and product-led growth inside enterprise companies, hey, I'm open to learn myself. We're all in one big journey learning how to do this better.

Lenny Rachitsky (01:21:01):
So true. Shaun, thank you so much for being here.

Shaun Clowes (01:21:05):
Awesome, thank you very much, Lenny. It was great.

Lenny Rachitsky (01:21:07):
Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at LennysPodcast.com. See you in the next episode.

