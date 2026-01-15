---
guest: Brendan Foody
title: Why experts writing AI evals is creating the fastest-growing companies in history
  | Brendan Foody
youtube_url: https://www.youtube.com/watch?v=ja6fWTDPQl4
video_id: ja6fWTDPQl4
description: 'Brendan Foody is the CEO and co-founder of Mercor, the fastest-growing
  company in history to go from $1M to $500M in revenue (in just 17 months!). At 22,
  he is also the youngest American unicorn...

  '
duration_seconds: 4028.0
duration: '1:07:08'
view_count: 28965
channel: Lenny's Podcast
keywords:
- product-market fit
- growth
- retention
- churn
- metrics
- roadmap
- prioritization
- revenue
- hiring
- culture
- leadership
- management
- strategy
- vision
- mission
---

# Why experts writing AI evals is creating the fastest-growing companies in history | Brendan Foody

## Transcript

Brendan Foody (00:00:00):
The wealthiest companies in the world are willing to spend whatever it takes to improve model capabilities.

Lenny Rachitsky (00:00:05):
We are entering the era of evals.

Brendan Foody (00:00:07):
We started working with all of the top AI labs. What the labs need is labor marketplace. They actually need extraordinary professionals that can measure model capabilities.

Lenny Rachitsky (00:00:17):
They found this pocket, maybe the biggest business opportunity in history.

Brendan Foody (00:00:20):
We grew from 1 to 400 million in revenue run rate in 16 months, fastest ascent in history.

Lenny Rachitsky (00:00:27):
Why is this so valuable?

Brendan Foody (00:00:29):
The market is bound by the amount of things where humans can do something that models can't. The lab's primary bottleneck to improve models is how they can effectively have some way of measuring what success looks like for the model.

Lenny Rachitsky (00:00:43):
There's this tweet that you retweeted. "If you really think about it, we were put on Earth to create reinforcement learning training data for labs."

Brendan Foody (00:00:49):
It's highly likely that the entire economy will become an aural environment machine, building out all of these worlds and contexts. And I think the narrative in AI over the last three years has almost entirely been one of job displacement, but very few companies and people have talked about this new category of jobs that's being created.

Lenny Rachitsky (00:01:08):
I talked to a lot of people about what should I be studying? Where should I be getting better?

Brendan Foody (00:01:12):
How can they leverage this technology to do so much more? We'll give people interviews where we say, "Use whatever tools are available to build a website and let's see what product you're able to build in an hour."

Lenny Rachitsky (00:01:24):
Today, my guest is Brendan Foody, CEO and co-founder of Mercor. Mercor is the fastest-growing company in history to go from 1 to $500 million in revenue. They did this in 17 months, less than a year and a half. Brendan is also the youngest unicorn founder ever. They just raised $100 million at $2 billion valuation. Mercor, if you haven't heard of them, helps AI labs and AI companies hire experts to help them train their models using AI. They've never had a customer churn, their net retention is over 1,600%, and they're on a nine-figure revenue run rate.

(00:01:59):
In our conversation, we talk about the increasing value and importance of evals, the landscape of AI training companies like Mercor, and why they've become so important and valuable, how Brendan discovered this opportunity, his insights on what product market fit looks like, the core tenets he's instilled within his organization that have allowed him to build the fastest growing company in history, what people writing evals for labs are actually doing day to day, which skills and jobs are going to last the longest with the rise of AI, why he doesn't think we'll see AGI or superintelligence anytime soon, and so much more. This episode is incredible. You need to hear this.

(00:02:33):
If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It helps tremendously. Also, if you become an annual subscriber of my newsletter, you get 15 incredible products for free for one year, including Lovable, Replit, Bolt, N8N, Linear, Superhuman, Descript, Whisperflow, Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, and Mobbin. Check it out at lennysnewsletter.com and click Product Pass. With that, I bring you Brendan Foody.

(00:03:01):
This episode is brought to you by WorkOS. If you're building a SaaS app, at some point your customers will start asking for enterprise features like SAML authentication and SCIM provisioning. That's where WorkOS comes in, making it fast and painless to add enterprise features to your app. Their APIs are easy to understand so that you can ship quickly and get back to building other features. Today, hundreds of companies are already powered by WorkOS, including ones you probably know, like Vercel, Webflow, and Loom.

(00:03:32):
WorkOS also recently acquired Warrant, the fine fine-grained authorization service. Warrant's product is based on a groundbreaking authorization system called Zanzibar, which was originally designed for Google to power Google Docs and YouTube. This enables fast authorization checks at enormous scale while maintaining a flexible model that can be adapted to even the most complex use cases. If you're currently looking to build role-based access control or other enterprise features like single sign-on, SCIM, or user management, you should consider WorkOS. It's a drop-in replacement for auth zero and supports up to one million monthly active users for free. Check it out at workos.com to learn more. That's workos.com.

(00:04:18):
You fell in love with building products for a reason, but sometimes the day-to-day reality is a little different than you imagined. Instead of dreaming up big ideas, talking to customers, and crafting a strategy, you're drowning in spreadsheets and roadmap updates and you're spending your days basically putting out fires. A better way is possible.

(00:04:38):
Introducing Jira Product Discovery, the new prioritization and roadmapping tool built for product teams by Atlassian. With Jira Product Discovery, you can gather all your product ideas and insights in one place and prioritize confidently, finally replacing those endless spreadsheets. Create and share custom product roadmaps with any stakeholder in seconds. And it's all built on Jira, where your engineering team's already working so true collaboration is finally possible. Great products are built by great teams, not just engineers. Sales, support, leadership, even Greg from finance, anyone that you want can contribute ideas, feedback, and insights in Jira Product Discovery for free. No catch. And it's only $10 a month for you. Say goodbye to your spreadsheets and the never-ending alignment efforts. The old way of doing product management is over. Rediscover what's possible with Jira Product Discovery. Try it for free at atlassian.com/lenny. That's atlassian.com/lenny.

(00:05:42):
Brendan, thank you so much for being here. Welcome to the podcast.

Brendan Foody (00:05:45):
Thank you so much for having me, Lenny. I'm a huge fan, and so excited to have a conversation.

Lenny Rachitsky (00:05:51):
I'm really excited to have this conversation as well. I'm a huge fan of yours. I'm excited for more people to learn about you and what you're building.

(00:05:57):
I want to start with a tweet that you have pinned at the top of your Twitter feed right now, and here's the tweet. "We are now working with six out of the Magnificent 7, all of the top five AI labs, most of the AI application layer companies. One trend is common across every customer. We are entering the era of evals."

(00:06:19):
The reason this caught my attention is that's one of the most recurring trends on this podcast, people talking about the increasing value of learning how to do evals well and the value of evals for companies. It feels like still people don't know what the hell this is what we're talking about, why this is so important. Talk about just what you think people are still missing, what they need to know, what this era of evals means.

Brendan Foody (00:06:39):
If the model is the product, then the eval is the product requirement document. And the way that researchers' day-to-day looks is that they'll run dozens of experiments where they'll make small improvements on an eval set. And reinforcement learning is becoming so effective that once they have an eval, they can help climb it. If you look at just how fast people were able to saturate Olympiad Math once they focused on it, how fast we're even saturating SWE-bench once we focus on it. And so in many ways, the barrier to applying agents the entire economy to automate every workflow is how do we measure success? How do we eval it? And write the PRDs for everything that we want agents to do, which Mercor is obviously a huge part of doing.

Lenny Rachitsky (00:07:25):
So people hearing this, they're like, "Oh, yeah. Okay, shit. I got to really pay attention to this eval stuff." Any advice about learning how to do this well? What companies that are doing this well are doing differently? Help people get better at this thing.

Brendan Foody (00:07:39):
Yeah. I think that for enterprises especially, the core way to think about it is how can they build a test or systematic way to measure how well AI automates their core value chain? So if it's an architecture firm that's producing these architecture diagrams of what they provide to their end customer, how can they effectively measure that? And each company has its own value chain or maybe a handful of them if it's a multi-product company. And just thinking about how they measure that is the prerequisite to really effectively applying AI throughout their entire business.

Lenny Rachitsky (00:08:21):
I saw you talking about this on the No Priors podcast with Sarah and Elad, and I don't know if it was after this or before this, but Sarah tweeted, "Evals equals your new marketing." What does that mean? What do you think she's saying there?

Brendan Foody (00:08:32):
Yeah. Well, it ties to what I said earlier about how if the model is the product, evals are the PRD, but also subsequently the sales collateral, right? Because evals are what you give to researchers to show them what they should be building and going on, but they're also the way that you demonstrate the efficacy of capabilities.

(00:08:51):
And historically, everyone's been pointing to these academic evals of PhD level reasoning with GPQA, Humanity's Last Exam, or Olympiad Math, but now it's moving towards the capabilities that people practically care about of how do we get models to automate the way that we build a software platform or automate the way that we do an investment banking analysis. And I think labs as well as application layer companies will increasingly use evals to demonstrate the capabilities of their models and their products.

Lenny Rachitsky (00:09:26):
Okay. So let's build on this and zoom out a little bit and talk about the landscape of the market that you're in. And I was just reflecting on this as I was preparing for this conversation. If you think about the companies growing faster than any company's ever grown in history, there's essentially three buckets. There's the foundational model companies, there's vibe coding apps, Cursor and Loveable and Bolt and Replit and all these here, and then there's data labeling data companies like you. So I've had the CEO of Handshake on the podcast. I have the CEO of Scale coming on. There's also Surge. There's you guys. Help us just understand the landscape of what this is all about because I think people don't really know what the hell's going on and see all these companies growing like crazy.

Brendan Foody (00:10:06):
Yeah, I'll give a little bit of the origin story, incorporate in that and how it frames the landscape. Because when we started the company, I met my co-founders when we were 14 years old. We started the company together when we were 19 initially, in January 2023, initially hiring people internationally, matching them with our friends and automating all the processes of how we did that. So similar to how a human would review a resume, conduct an interview, and decided to hire. We automated all of those processes with LLMs, bootstrap the company to a million dollar revenue run rate before we dropped out of college.

(00:10:40):
And then a handful of other things happened, but we met OpenAI and we saw that there was this enormous transition in the human data market where it was moving away from this crowdsourcing problem of how do you find low and medium skilled people that can write barely grammatically correct sentences for early versions of LLMs and moving towards this sourcing and vetting problem. How do we source and assess the best professionals, the experienced? Think software engineers, the investment bankers and doctors and lawyers that can actually help to evaluate and interpret all of the capabilities that people want models to have.

(00:11:21):
So from there, we start working with all of the top AI labs. We grew from 1 to 400 million in revenue run rate in 16 months, and it's been an extraordinary journey and super exciting.

Lenny Rachitsky (00:11:36):
Okay. First of all, that is out of control. I don't know if people understand. I think this is the first time you're sharing that number. I know we're recording this, you'll have announced it by now, but 1 to 400 million in revenue in 16 months.

Brendan Foody (00:11:49):
Exactly. So fastest ascent in history, which is an exciting statistic we're very proud of.

Lenny Rachitsky (00:11:57):
Okay. So something big is happening here. Why is this so valuable? What is going on here? So it's just to try to summarize what you guys do simply is you help hire people for labs to help them train their models, and you help them find not just generalist labor, but experts, helping them with very specific gaps in the model's knowledge.

Brendan Foody (00:12:21):
Yeah, precisely. And so it really ties to your first question around the era of evals that's framing all of this, which is that the lab's primary bottleneck to being able to improve models is how they can effectively have some way of measuring what success looks like for the model, both to use it as the eval for the tests that they're measuring their progress against, as well as the verifiers in an RL environment to then reward the model, improve capabilities, et cetera. And they need this across every domain for every capability that models don't know how to use. And the wealthiest companies in the world are willing to spend whatever it takes to improve model capabilities where Mercor is sitting at the forefront and the primary bottleneck.

Lenny Rachitsky (00:13:12):
Okay, what are these people actually doing? So what's an example of a kind of person that is sought after? And then what are they doing sitting there at the computer?

Brendan Foody (00:13:19):
Effectively, the market is bound by the amount of things where humans can do something that models can't. So I'll make that very concrete. Say you have a model that you want to write a red line for a contract in the way that a lawyer would, and it makes a handful of mistakes, misses a bunch of key points in doing so. What you could do is have a lawyer create a rubric similar to how a professor might create a rubric to create a deliverable for what are the things we want the model to be able to do?

(00:13:50):
So it can effectively score that, right? Plus however much of it identifies this or XYZ key point. And that's really the foundation to measuring what does progress look like for models? Is this model achieving the capabilities that these professionals want? As well as how do we use this as training data to reward and to reinforce a lot of the capabilities that people want models to achieve.

Lenny Rachitsky (00:14:19):
Okay, so they're essentially writing evals just to connect it back to original conversation.

Brendan Foody (00:14:23):
Exactly. Well, that's an interesting thing is everyone talks about RL environment. I feel like the two hot button things are like RL environments and evals, but one thing like Andrej Karpathy's tweeted out about a bunch is there's not actually a nuance. It's in the data type. It's more just a different semantic way of describing what it's being used for. But ultimately, it's just some stasis point for how do you measure what good looks like? And you can use that either as the benchmark to the sales collateral, as Sarah was saying, to say, here is why are models the best model in the world and here's the capabilities that we've been working towards, or you can use it on the post-training side to reward certain model trajectories and achieve those capabilities.

Lenny Rachitsky (00:15:08):
Okay. So say this lawyer, this person is writing, "Here's what a great red line contract looks like and here's the rubric of what excellent is." Then are they also providing data, like actual examples of red line documents as a part of that?

Brendan Foody (00:15:22):
They may. The data landscape historically has included two kinds of data. The first is supervised fine-tuning data, which is input/output. When people think about fine-tuning in the historical sense, that's what it is. The second is RLHF where the model will generate a couple of examples. We'll choose which is the most popular example.

(00:15:43):
What everyone is generally moving towards is reinforcement learning from AI feedback instead of human feedback where you have instead the human defined some sort of success criteria, some way to measure that. And examples in code, it could be a unit test. We can scalably measure success and other domains that could be a rubric. And then you use that to incentivize model capabilities. And it's far more scalable and data-efficient, and so that's why a lot of the broader trend in the market across the board is moving towards RLHF to both eval models as well as improved capabilities.

Lenny Rachitsky (00:16:24):
I had one of the co-founders of Anthropic on. He said exactly the same thing. That's what they've done at Anthropic, is move towards AI-driven reinforcement learning.

(00:16:32):
So essentially, if I can understand this correctly, I'm the lay person here trying to understand this on behalf of the audience. So essentially a lawyer is like, "Here's what correct looks like for redlining," and then it's AI is just on its own almost, just like, "I'm going to try to get this. I'm going to try to improve on this and I know if I'm heading the right direction based on this eval/rubric I've been given."

Brendan Foody (00:16:55):
Exactly. Applying all of the criteria of what good looks like similar to how the TA might apply the professor's criteria of does the student's response meet this criteria or this criteria plus however many planes, et cetera.

Lenny Rachitsky (00:17:10):
Awesome, okay. Let me shift to talking about the broader labor market here. So there's two parts to this question as we talk about this. One is just how long will we need to do this? You guys grew so incredibly fast. Is there a point of like, "Okay, we don't need humans. We're tapped out." So let's start there and then I'll ask a broader question.

Brendan Foody (00:17:29):
So the key question is how long there's going to be things in the economy that humans can do that AI can't do? And I think there's certainly a bucket of people that say we're going to have superintelligence within three years and humans won't play a role in the economy. And that's one school of thought.

(00:17:46):
Our perspective is very different. Our perspective is that these models are extraordinary and automating a lot of things very quickly, but there's a lot of things that they're horrible at. Even still, it can't schedule time on my calendar. It can't draft emails for me. It can't use basic tools. And we need evals for everything. For everything that the models can't do, we need evals for the tool use, evals for the long horizon reasoning.

(00:18:12):
Imagine in 10 years when we want models to be able to go out and build a startup for 30 days. We need evals for that to effectively reward it. And I think that that road to improving models will last for as long as there is anything in the economy that humans can do which models can't and be a huge portion of what the future of work looks like. And so our mission is creating the future of work, and I think that this is a really exciting industry and giving us a glimpse into the direction that everything is headed towards.

Lenny Rachitsky (00:18:49):
There's this tweet that you retweeted that I want to ask you about. "If you really think about it, we were put on Earth to create reinforcement learning training data for labs."

Brendan Foody (00:18:59):
Yeah.

Lenny Rachitsky (00:19:00):
What does that mean to you? What is this person implying? And it's basically what you're saying is we're just helping train models.

Brendan Foody (00:19:06):
It speaks to conversations I've had with a lot of researchers and executives at top labs, which is that it's highly likely that the entire economy will become an aural environment machine, building out all of these worlds and contexts for us to then have rubrics or other kinds of verifiers. And that is really exciting in so many ways.

(00:19:32):
Because I think let's draw an analog to other revolutions where when we had the industrial revolution, everyone was freaking out about losing their jobs, but there was this whole new class of jobs of how do we build the machines? How do we have knowledge work? How do we create everything new? And I think that the narrative in AI over the last three years has almost entirely been one of job displacement, right? Sure, there's ChatGPT is growing fast and it's very cool that everyone loves using it, but from an economic standpoint, people talking a lot about job displacement. But very few companies and people have talked about this new category of jobs that's being created and what that's going to mean and how people can prepare and upskill for that. And I think that the most exciting thing possible is creating that future of how do humans fit into the economy and how will that evolve over time?

Lenny Rachitsky (00:20:22):
I talk to a lot of people about just what should I be studying? Where should I be getting better? People in school right now are just like, "What is even going to be valuable in the future?" You're at the center of a lot of just what jobs are most in demand, how hiring is evolving. So let me just ask you a very concrete question. What jobs do you think will remain in the future/what skills are still worth investing in for younger people, especially?

Brendan Foody (00:20:47):
In terms of jobs, I would respond with a category of things that have very elastic demand are going to be super exciting. Because when we make people 10 times more productive, we'll build 10 times, if not 100 times as much software as an example. And so I think the product managers that can now do so much more are going to be extremely well-positioned. And so far as the skills, I think it's people that can leverage AI to do whatever their day-to-day workflows are.

(00:21:16):
I have had a couple conversations with teachers where they get my thoughts on how they should be assessing their students because we originally started out curating all of these AI interviews and assessments for people and have thought about this immensely. And what we realized is that you don't want to fight against them using the models. It's similar to when the calculator came out, you don't want to give people all of this arithmetic work of how do you get them to do it and not use the calculator. You want to tell them, "Use the tools and let's see what you can do."

(00:21:49):
And so we'll give people interviews where we say, "Use ChatGPT and Kodak. Use Claude code. Use whatever tool cursor and whatever tools are available to build a website and let's see what product you're able to build in an hour." And so I think that I give that an example in so far as talent assessment because I think it pertains also to the skills that people should be honing in on of how can they leverage this technology to do so much more in whatever industry or vertical they're operating in.

Lenny Rachitsky (00:22:17):
When you talk about elastic, being elastic, is it generalists being good at just a bunch of different things, or what do you say? What do you mean when you think elastic?

Brendan Foody (00:22:25):
So I more mean how much capacity for demand there is in that industry. So I'll give a couple of examples. In accounting, I think realistically we only need so much accounting in the world. Maybe there's areas where we can do more and that'll be good, but it doesn't feel like the world needs 100 times more accounting.

(00:22:46):
On the other hand, in software development, I think we can ship 100 times more features for our products, move 100 times faster, build so much more. There's just it feels like there's unlimited demand for the industry. And I think Mark Andreessen tweeted about this recently, that software is the most elastic industry of all where when we increase productivity, there's so much more that will be built. And it's definitely characteristic of a lot of other domains as well. And so I would focus on those domains where if we make everyone 10 times more productive, that'll increase demand, not reduce it.

Lenny Rachitsky (00:23:23):
Okay. So you're in the bucket of learn to code, still useful as a skill. You take computer science. And so in terms of elastic categories of jobs, sounds like engineering, product management is in that bucket. Great. A lot of people listening to this are PMs. What else, like design users? I don't know. What else do you feel is in that bucket from what you've seen?

Brendan Foody (00:23:44):
Yeah, I think that there's a lot of things where the whole value chain of building companies has a lot of these variable costs, even large portions of operations or consulting. Imagine if we could have 10 times as many McKinsey consultants, what would be possible in so far as the research we could do, the analysis, et cetera. But I think the companies and people that are going to succeed are those that lean into this narrative of abundance of how do we do so much more rather than fighting back against it of how do we try to stop displacement.

Lenny Rachitsky (00:24:20):
So along those lines, I think about your second bucket, which is the people that will be most successful. It's not like a specific skill, but it's being good with AI, using AI to become better at what you're already doing. This reminds me of Elon's whole thing with Neuralink, which I don't know if this is how we put it, but the way I've always heard it is you wanted to build Neuralink because in the future when AGI and superintelligence is around, we need a way to compete and the best way to compete is plug our brains into a superintelligence so we have a chance. And it feels like that's what AI is. Getting good at AI tools is essentially is having this super superpower.

Brendan Foody (00:24:58):
Figuring out how to leverage them and incorporate it will definitely be of paramount importance.

Lenny Rachitsky (00:25:04):
It just comes back to this almost cliche quote now. It's, "AI won't replace you. People that are really good with AI will replace you."

Brendan Foody (00:25:10):
I think it's totally spot on. And I've definitely seen this at the enterprise level as well where there's certain enterprises we talk to that are almost fearful not wanting to engage, not wanting to eval their businesses because that'll provide the evidence that their value chain is being automated. And there's others that... Literally some of the most recognized sophisticated Fortune 500 businesses that have this mentality and there's others that are leaning into it of if we have the ability to do 10 or 100 times more, what will that mean and how do we lean into that future? Because there's so many things that are going to change over the next 10 years, and I think those are the kinds of businesses that are going to be successful.

Lenny Rachitsky (00:25:54):
Let's talk about labor markets more broadly. You guys, so it's interesting though. You started not feeding people to AI labs, not training models. It was just like help people find jobs, help companies hire, and then you're like, "Oh wow, this whole opportunity." You have this really interesting view on the future of just labor markets and hiring. Talk about that.

Brendan Foody (00:26:14):
Yeah, it's interesting. I remember when we started the company, as I mentioned, we were 19, and just had this gut intuition that it felt so wildly inefficient that labor markets are so disaggregated. And what I mean by that is when we would hire someone internationally, they would apply to a dozen jobs. When we as a company in the Bay Area were considering candidates, we would consider a fraction of a percent of candidates that were available in the market. And the reason for that is that there was this matching problem that everyone's solving manually where they'll manually review resumes, they'll manually conduct interviews, and manually decide who to hire. But when we're able to automate that matching problem at the cost of software, it makes way for this global unified labor market that every candidate applies to and every company hires from facilitating a perfect flow of information in the economy.

(00:27:08):
And I think that that future is undoubtedly what we're heading towards, but what we've realized over time is that the nature of work is also changing dramatically. And part of building that future over a 10-year time horizon is creating that future of work and all of the more tactical things we do and building these incredible data sets across evals and RL environments for our customers.

Lenny Rachitsky (00:27:35):
What I've seen in how hiring has changed, I'm doing research on this with a partner, Gnome, it's so much easier to apply for companies that everyone's just applying now, to hundreds of companies. AI is just making it easy to adjust their resumes and cover letters and make it feel like, "Oh, I applied to more of course very specifically, but it was one of 100 places." And then on the flip side, hiring managers are getting flooded with applications and so now they need AI to filter. So even if we didn't want to get to this place, we're almost being pushed into this direction of so much volume on both sides. We need something really smart at filtering and helping us hire and select, and this is exactly what you guys have been building for a long time.

Brendan Foody (00:28:13):
Precisely, yeah. And the fascinating thing a lot of people ask, do we think about ourselves as a labor marketplace or do we think about ourselves as a data company? And I think that the reason it's an interesting question is our realization on from what the labs need is that they actually need a labor marketplace. They actually need these exceptionally high caliber people. And of course we'll layer on some project management and some software platform associated with it. But the really core thing that they want is how do they find these extraordinary professionals across all of these different domains that can measure model capabilities and work to build that future work together?

Lenny Rachitsky (00:28:56):
This episode is brought to you by Enterpret. Enterpret is a customer intelligence platform used by our leading CXN product orgs like Canva, Notion, Perplexity, Strava, Hinge, and Linear to leverage the voice of the customer and build best in class products. Enterpret unifies all customer conversations in real time, from Gong recordings to Zendesk tickets to Twitter threads, and makes it available for your team for analysis and for action.

(00:29:21):
What makes Enterpret unique is its ability to build and update a customer-specific knowledge graph that provides the most granular and accurate categorization of all customer feedback and connects that customer feedback to critical metrics like revenue and CSAT. If modernizing your voice of customer program to a generational upgrade is a 2025 priority, customer-centric industry leaders like Canva, Notion, Perplexity, and Linear, reach out to the team at enterpret.com/lenny. That's E-N-T-E-R-P-R-E-T.com/lenny.

(00:29:55):
Going back to just how this all works and what you guys do for models, I was talking to a friend who had an ankle sprain or his foot was hurting and he got an x-ray and he fed the x-ray into ChatGPT and then asked him, "Give me this specific x-ray." And it's like, "Okay, sure." And then it gave him, "Here's what you have." And he was talking to me, he's like, "What is out there on the internet that trained this model to know this stuff?" And I was like, "No, it's actually somebody sitting there helping the model understand this. Once they recognize, it doesn't fully understand this. Humans are actually helping them learn these things."

Brendan Foody (00:30:29):
Exactly. Well, so the way it works, at least what most people's understanding is there's a lot of complexity in how the models work, is that pre-training gets a lot of the knowledge into the model of what are all the different things that see into the world. And then post-training and reinforcement learning is for all of the reasoning of what are the pieces of knowledge that are accurate, what are inaccurate, and what to prioritize at any given time to make a decision. And so behind that, there would've been radiologists that worked on the post-training data set to create some stasis point for here's the diagnosis and rewards and penalties associated with it. And it's really the quality of those people that went into the quality of the decision and recommendation that ChatGPT ultimately made.

Lenny Rachitsky (00:31:14):
So let's actually follow that, right, because that's really interesting and I don't know how many people understand it. I understand it. So the work that you do and these experts do is post-training. It's not feeding data into the model that it's trained on. It's, "We have this model GPT-5. Now here's all the things that's missing. Let's add to it."

Brendan Foody (00:31:31):
Exactly, yeah. It's really unlocking, allowing the model to focus on all the right tokens, from pre-training all the right things in model context, up weighting the effective reasoning chains to enable the models to reason better in a more generalized way.

Lenny Rachitsky (00:31:48):
What's the scale of people just working on the stuff. It's like thousands, tens of thousands, hundreds of thousands?

Brendan Foody (00:31:53):
Tens of thousands at any given time, hundreds of thousands more generally. It's huge. And the most exciting thing is that it's growing really quickly. I think that to your question also about the competitive landscape, historically there were all these crowdsourcing companies that would get these super high volumes of low-skilled people. I think Scale and Surge were the primary companies that pioneered that industry. And then in this transition to higher-skilled labor, what people realized is that actually you can go a lot further with just getting higher caliber people even in smaller amounts initially, and now subsequently scaling that back up once they're able to meet the quality bar.

(00:32:35):
And I think that there's a bunch of companies that after our success and very rapid revenue growth that started early last year have chased after that, which makes sense. And seeing that the market was changing very quickly, we were taking off, and trying to pursue a similar thesis on the market.

Lenny Rachitsky (00:32:56):
It's interesting. There's always been these companies, AlphaSights and GLG, that did this before AI or is paid to connect to an expert and ask them questions about stuff. And essentially, okay, it turns out this is really useful for models. We don't need the person in the middle.

Brendan Foody (00:33:11):
Exactly, yeah. Well, but one core difference is that AlphaSights would generally be a one-off call versus a lot of our work is really hiring people for projects of how do they work on something for a longer period of time. And so that's, I think, one of the reasons that some of the traditional expert networks have struggled to get into this. And also how do you retain those people and think about all the incentives where it actually looks more similar in some ways to one of the traditional labor marketplaces of an Uber or DoorDash, just with much higher-skilled talent that's treated exceptionally well?

Lenny Rachitsky (00:33:50):
It's such a good opportunity for me to learn so much about this, so I'm going to ask questions.

Brendan Foody (00:33:55):
Yeah.

Lenny Rachitsky (00:33:55):
It's so interesting to me. How much of the experts are focused on specific concrete knowledge versus personality and softer skills? How much of it's like, "Here's how you do an exam. Here's how you do an x-ray"?

Brendan Foody (00:34:09):
It depends on the lab. It's a lot of both. I think that previously it might've been more softer skills, but now a lot of the labs are focused on their business models of what are the economically valuable capabilities that drive revenue and leaning a lot into these professional domains. But I think the creative side is also still really important to everyone. And so we're seeing a meaningful amount of both. We hired all the people from the Harvard Lampoon a couple of months ago, their comedy club, to help with making models funnier. And so do all sorts of stuff like that, hiring Emmy award-winning screenwriters and everything across the board on creative capabilities that you'd look for.

Lenny Rachitsky (00:34:51):
That is amazing. What a cool story. I'm excited for this to kick in. How fast do these things turn around? Say you hired this team, how fast are we going to see the impact potential? Is like months? Is it years?

Brendan Foody (00:35:03):
Well, so it depends, because some models or some labs will release iteratively where they'll just improve the model behind the scenes.

Lenny Rachitsky (00:35:11):
Without announcing a new model?

Brendan Foody (00:35:12):
Exactly. Every couple of weeks versus others do these big releases. And so it depends a lot. We're behind all of them, but we move really fast. It would be a customer gives us a request of we need these award-winning screenwriters, and within 24 hours we'll turn around the experts. And then there's also this really interesting dynamic where in a set of 100 people that we hire, oftentimes the top 10% of people will drive majority of the model improvement. It's like a company. If you have 100-person company, oftentimes the top 10% of the company will drive majority of the impact. And what that means is that when we're able to build proprietary advantages in identifying who are those top 10% of people, both in so far as how do we have them on our platform but also identify and match them effectively, it creates so much value for customers that it's difficult to compete against.

(00:36:08):
And so it really does tie back to the founding thesis of the company, which is how do we find these extraordinary people and identify them so that we can reliably deliver these top 10% or top 10X experiences for our customers.

Lenny Rachitsky (00:36:25):
So on that, so is the idea, you hire Jane. She's incredible at coding and she now works for Anthropic and that's her full-time job doing this? Or is this a part-time thing? Is this a project thing mostly?

Brendan Foody (00:36:38):
It would sometimes be part-time. Sometimes it would be full-time. I would say most often it's part-time where it's like someone might work at a thing company where they're underemployed, maybe one of the ones that's moving slower where they have an extra 20 hours a week and then they're able to do this on the side or whatever the equivalent is across a bunch of different industries. But we also do a lot of 40 hour a week roles as well.

Lenny Rachitsky (00:37:08):
And how much are they making? Is it meaningful enough for a AI engineer to spend time on this?

Brendan Foody (00:37:13):
Yeah, very meaningful. So our median pay rate in the marketplace is $95 an hour, but it can flex up, well up into $500 an hour based on the depth of someone's expertise. And one thing that highlights this difference relative to a lot of the crowdsourcing companies is if you look at the economics of the crowdsourcing companies, oftentimes they would pay $30 an hour to town as the average. And so think about the people that you can hire, the undergrads for $30 now versus the Goldman bankers, the McKinsey analysts, the Fang software engineers. And ultimately it comes down to what are the capabilities that labs want their models to have? And it much more falls in the latter bucket than the former one.

Lenny Rachitsky (00:38:02):
I know there's only so much you can talk about with this stuff, but so Anthropic, Claude has been so good at coding so much better historically than other models. I also use it for writing, giving feedback on writing. What is it that allowed them to get so good at this and continue to be so good at this?

Brendan Foody (00:38:19):
Well, I can't go too much into detail about customer work, but I think that it's this trend of reinforcement learning and being very thoughtful about defining the right rewards that we're releasing across the board. And how we could mitigate reward hacking, set up the right rewards, that's super impactful.

Lenny Rachitsky (00:38:42):
Evals. Again, evals is all you need.

Brendan Foody (00:38:44):
Back to evals.

Lenny Rachitsky (00:38:45):
Yeah.

Brendan Foody (00:38:45):
One of my favorite quotes from customers is that, "Models are only as good as their evals," which has always held true.

Lenny Rachitsky (00:38:53):
I think Greg Brockman tweeted this once. "Evals are all you need."

Brendan Foody (00:38:56):
Yeah, truly.

Lenny Rachitsky (00:38:58):
Let's talk about Mercor a little bit more. One of the maybe, not even maybe, I believe the data tells us it's the fastest growing company in history.

Brendan Foody (00:39:07):
Yeah.

Lenny Rachitsky (00:39:09):
I want to understand what you did to make this happen. So let me just ask, what do you think are some of the core tenets of how you built Mercor that most contributed to being this successful?

Brendan Foody (00:39:20):
I think the most important thing is looking at the leading indicators in fast-moving markets. I remember when I used to think... Everyone in venture talks about the why now, and I used to think about the why now of how from a product standpoint, less from a market standpoint of now we can automate the way that we review resumes or the way that we conduct interviews, et cetera. But ultimately there is this legacy market that's has all these incumbents and it's relatively stagnant. But what matters a ton is actually figuring out what are the new markets, the new pockets of demand that are changing very quickly where the wealthiest customers in the world are willing to pay whatever it takes to improve model capabilities, and how do we focus on the leading indicators of those markets to make sure that we have the best solution for the flagship customers in the market and optimize everything around that.

(00:40:18):
And that's what I found has been most impactful in building the business. I think maybe that's one thing is leading indicators in markets. If I had to choose another, it's customer obsession. We have had for the last... We're starting to have a couple of product managers help out with go-to-market, but for the last year and a half of the business, we've had no one in sales and marketing. And so we're immature from a sales and marketing standpoint because we focused 100% of company resources on how do we build great products and experiences for our customers. Just getting word of mouth, the people that have worked with us at other businesses want to keep working with us and leaning into creating those great experiences. And so that's where I spend all my time. And I think that some founders can get caught up in how do they get really good at marketing before they've figured out the thing that really drives a lot of customer love and creates the six-star experiences that you're used to building.

Lenny Rachitsky (00:41:19):
I'm going to go back to that first point, which is like, okay, you found this pocket, maybe the biggest business opportunity in history. How did you first find... What was that moment of, "Wait, this could be really big"?

Brendan Foody (00:41:31):
So there's some crazy stories here. I remember we started the company as I mentioned in January 2023. And then in August 2023 when I was still in college, one of our customers introduced us to the co-founders of xAI over a Zoom call saying how we had these really smart Indian software engineers that were great at math and coding. So we met them and we explained how the software engineers we had were really good at math and coding because they weren't distracted by all the humanities. They didn't have to study history and English and all these other things, and they loved it. So they had us in two days later to the Tesla office and we met the entire xAI co-founding team except for Elon, while I was still a college student. And xAI was just getting started at that point and they were super excited about our focus on the quality of the experts.

(00:42:22):
And so while they were still doing pre-training, they weren't ready for human data at the time and we didn't start working with them at that point. We just knew from that point forward before we even dropped out that the market was about to change radically and we needed to be at the frontier of that. And so then fast-forward a few months, one of the crowdsourcing players came to us and actually used our platform to hire over 1,000 people where this is very interesting experience because we started getting flooded with support tickets about how those people weren't getting paid. And we obviously felt horrible because we had referred them to this opportunity. It was this reputable company. And we realized that a lot of the incumbents were resting on their laurels with respect to what was needed in the experiences they were creating for talent in their marketplaces to help improve models. And there was this opportunity to work directly with the labs in a way that kept the dignity of the experts in the marketplace, paid them extremely well, and cut out the middlemen.

(00:43:31):
And so we started doing that in May of last year, and then the rest is history.

Lenny Rachitsky (00:43:37):
Wow, okay. Hundreds of millions of dollars in revenue since. So what I'm hearing here is you were very open to looking for poll. You saw some poll, you explored it. And then once you saw that there was something really meaningful there, you just went deep on making that an incredible experience as amazing as possible.

Brendan Foody (00:43:57):
Exactly. I think if I had to distill it into advice for founders, one thing I've realized is that I spent a lot of time trying forced product-market fit. And in some ways you should be persistent. You should have these theses that you have conviction about how the world will change. But sometimes you just need to sheer it from the market and know that it's there, the poll, to know the right places to focus. Because if it's difficult to sell, if it's extremely difficult to sell the marginal customer, you're not going to be able to grow a huge business. What you actually need to find is the customer that's surprisingly easy to sell into where you're going to be able to grow with them. You know that it's a large pain point. And so it's some combination of being stubborn with respect to your thesis around how the world will change, but also very open-minded with respect to exactly what form that takes and how the market's developing and how your company will fit into it.

Lenny Rachitsky (00:44:55):
That's an amazing insight. In the moments you described, felt like it was a combination of this xAI meeting feeling like, "Oh wow, they really, really want this thing that we have. We're now doing an amazing job," and then it's 1,000 people hiring in the platform. Was that those two moments that are like, "Wow"?

Brendan Foody (00:45:09):
Exactly. And those happened, keep in mind, while we were a seed company, right? Well, so the first one was before we even raised any seed funding, we were totally bootstrapped because we bootstrapped the company to a million dollar revenue run rate and have always remained super capital-efficient. We've never burned money. We were lifetime profitable. And then we raised our seed round in September from General Catalyst, and it was the other experience after we raised our seed round where we really knew that there was an enormous amount of demand in this market where we saw the volume and we saw that the incumbents were sleeping with respect to how the market was changing and the kinds of people that were needed to make that change happen.

Lenny Rachitsky (00:45:50):
It's one thing to see this opportunity and start to execute on it. It's another to actually succeed at this scale and consistently win. You guys have very specific values within the business. Talk about those. It feels like that's a big part of your success too.

Brendan Foody (00:46:04):
It totally is. So I'll give the three and maybe a brief story associated with each of them.

(00:46:10):
So the first one is having a can-do attitude, which everyone gives me a little bit of a hard time for because it's a funny saying, but we've always set these ridiculously ambitious goals, and then somehow the trajectory of the company forms around those goals. Where I remember when we were talking to Benchmark before they led our Series A, we were at 1.5 million in run rate. And I said we'd be at 50 million in run rate by the end of the year. And they said we were absolutely insane, right, as anyone would. And plus or minus two weeks, we hit it. And then we've now well blown past the tracking to 500 million in run rate, which was initially our goal for this year. So setting these incredibly ambitious goals with respect to the revenue scale of the business, the caliber of experiences for talent, all those dimensions is super important to first have a can-do attitude.

(00:47:04):
The second thing is really high standards, which is who we hire and what we expect of them. We have an incredibly high hiring bar where we hire tons of former founders, people that have incredible experiences. We just hired or partnered with Sundeep Jain who joined us as president. He was previously the chief product officer and chief technology officer at Uber and joined our relatively small in the grand scheme of things company to help scale up all the processes where Uber is of course the largest labor marketplace in the world. So super high standards is of paramount importance.

(00:47:41):
And then the third one that we really lean on significantly is intensity. And that if you look at the early cultures of the legendary companies, thinking of Meta or Google, they have these incredible, intense early-stage cultures of people just moving heaven and earth and doing whatever it takes to push the frontier of model capabilities. And so still very much output-oriented of what do people achieve rather than input-oriented of the specific hours they work, but recognizing that it takes a lot to build a legendary business, and that's ultimately what we're optimizing for.

Lenny Rachitsky (00:48:18):
I could see why this works. Can-do attitude plus high standards plus intensity, I could see how that leads to success. There's a lot of talk these days about this 6-9-9 culture, working six days a week, 9:00 AM to 9:00 PM. A lot of people are like, "Why? That's terrible. Why would you make people do that?" But at the same time, I'm just constantly hearing this from the most successful AI companies. This is just the way it is to be successful. Things are moving so fast. This is an opportunity you'll never see again. Just talk about your thoughts on that.

Brendan Foody (00:48:50):
Yeah. Well, to clarify, we've never mandated hours. It's more been a byproduct of people that care a lot where we care a lot about the trajectory of the business. And so a lot of people come into the office and stay late. But if they need to leave early and get dinner with their kids or travel on the weekend, of course that's totally fine. And for us, it's much more about finding people who have a lot of ownership and are really bought in, less so about the specific hours in the office, even though we found that oftentimes it's the people that are most bought in, not always, but oftentimes it's the people that are most bought in and that burn the midnight oil with us.

Lenny Rachitsky (00:49:30):
When you say high standards, is there something you could share that gives us an example of what you mean there? Because a lot of people think they have high standards and they don't.

Brendan Foody (00:49:37):
If you are very patient, there's always some trade-off between speed and quality when hiring. And I remember especially for our first 10 people, we were just so patient and disciplined about finding some of the best people in the world. Half of them are... Our second employee, Sid, as an example, our second employee in the US, Sid was previously the head of growth at Scale who joined us when we were a seed stage company. Daniel who joined us was previously scaled to consumer apps to over 100,000 users and all sorts of just extraordinary backgrounds of our first 10 hires. And I think that that initial talent density shaped so much of what the rest of the org looks like as you scale it up.

Lenny Rachitsky (00:50:28):
I know you also have this perspective that people talk about waiting to hire, to hire really slowly, but it's actually not necessarily the right advice. Talk about that.

Brendan Foody (00:50:39):
It's painful because it's a double-edged sword. On one hand, I'm thrilled that our first 10 people are so phenomenal and I think that that has paid dividends for the business. But on the other hand, I think that companies do get to the point where you just need to hire really fast. And there's some things where you need a lot of people to do them and you need to recognize that there's going to be some variants associated with hiring, but moving quickly is the priority.

(00:51:07):
And I think that in some ways, we move too slowly with how we scaled out the team. And so the benefit is that everyone is extraordinary. We have this super high bar and we want to maintain that over time. But I think the downside is that while the company has grown incredibly quickly, we likely could have grown even faster if we had moved a little bit more quickly with especially ramping from call, like 10 to 100 people.

Lenny Rachitsky (00:51:37):
Okay, I was going to ask. So it sounds like the first 10, be very careful, take your time, 10 to 100, maybe speed up a bit.

Brendan Foody (00:51:44):
Yes, though I wouldn't say it's necessarily 10. It's determined by the point where you know it's really working. And I know that's still not a bright line, but it's like once you know that there's so much more demand than you can handle, that's when you want to step on the gas and optimize for speed in a lot of ways. But I think especially until then, it's important to be patient, be disciplined. Get the best people is always important, but speed becomes more important once you find the market opportunity, the market vacuum.

Lenny Rachitsky (00:52:20):
I know you've started a couple companies in the past, much smaller scale. In this new role as CEO of this massive hyper growth company, what surprised you most about where you spend the time most or just what the role involves? Because a lot of people want to start companies dream about being in your shoes. What are they maybe not understanding about where a lot of your time goes?

Brendan Foody (00:52:42):
Yeah, it's actually not too surprising. The top two buckets are always working on hiring and time with customers of how do I really deeply understand what customers need and how we can support them? And then how do I build the team and a lot of the processes around that? Of course, there's all of the ad hoc things I didn't expect of dealing with the people questions of how do we set up our levels and our comp bands and all of that, which you learn as you scale a business. But I think that the core places that I spend my time are in line with what I expected as well as what I love doing, which is very fortunate.

Lenny Rachitsky (00:53:27):
So these two companies you've started in the past, maybe share what they work because they're fun, and then how do they help you be successful in this? What's something that they taught you that helped you in your current role?

Brendan Foody (00:53:38):
Yeah, so there's been like a dozen, but I'll choose my favorite two. So when I was in eighth grade, I started Donut Dynasty where I saw that Safeway Donuts were selling for $5 a dozen, and I was amazed because I felt like as an eighth grader, this was such an incredible deal. And I started to bike down to Safeway, buy Safeway Donuts for $5 a dozen, and then go back to my middle school and then sell them for $2 each, running really good margins of course. It sold out super quickly. And so then I need to scale up. So I would pay my mom $20 to drive me in her minivan down to Safeway, buy 10 dozen donuts, go to my middle school, sell them all out.

(00:54:19):
And then the school tried to shut me down because I was selling food on school campus, which they didn't like. So they had me in the principal's office asking me to not do that. And then I moved my donut stand over 50 feet, so it was off school campus, saying that they could no longer police me. I remember we had competitors pop up where the competitors were charging. They bought these Chuck's Donuts, which if anyone in the Bay Area knows, are higher end donuts than Safeway Donuts, but they have a higher cost basis. They cost a dollar per. And so I dropped my prices to $1 for two weeks to run them out of business before I knew what anti-competitive practices were. And I'd hire all my friends, paying my friends in donuts because they perceived the donuts as $2 each where they could sell them throughout the school and I could have a lower cost basis on them.

(00:55:12):
So I had all of these fun experiences in selling donuts, and then I could talk more about my high school business as well, which was a more significant scale. But I think the takeaway from that was just like you can just do things. So many people have ideas, but the barrier to more companies being built, I think, is just initiative and taking the steps to build the product or experience that customers want and investing the time and the ambition to scale that up. And so I think it was really getting reps of that that enabled me to realize that I should do it later on at a much larger scale.

Lenny Rachitsky (00:55:51):
Amazing story. I love how wholesome that is versus drugs, selling donuts.

Brendan Foody (00:55:56):
Then my mom was very worried. She was like, "Oh, is there any pot of these donuts?" I was like, "No, mom, I assure you these are pure donuts."

Lenny Rachitsky (00:56:05):
I love that you paid your mom $20 to drive.

Brendan Foody (00:56:07):
Yeah. She was adamant it couldn't be a handout that she was taking her time to drive me, so she needed to make a little bit of money off of it. We haggled over her title where eventually she wanted to be head of global operations, which we found very entertaining.

Lenny Rachitsky (00:56:22):
I hope that's on her LinkedIn.

Brendan Foody (00:56:24):
Not yet. Maybe she'll have to add it.

Lenny Rachitsky (00:56:27):
So you said that you've started a dozen companies?

Brendan Foody (00:56:29):
Yeah.

Lenny Rachitsky (00:56:29):
Wow. Okay.

Brendan Foody (00:56:30):
Well, a dozen projects, but I think it was that, and then my AWS company were the two that I scaled up.

Lenny Rachitsky (00:56:39):
What's the story behind Mercor as the name?

Brendan Foody (00:56:42):
Mercor means marketplace in Latin or to buy, sell, trade. And we want to build the largest marketplace in the world, the marketplace for how everyone finds jobs, and that was really the draw to it.

Lenny Rachitsky (00:56:55):
Okay, maybe a last question. This is going back to earlier in discussion because it's something I've been thinking about as we're talking. There's been this shift from data as the fuel for models, and now it's experts. Do you think there's a next step, or is this just will take us to AGI, superintelligence?

Brendan Foody (00:57:15):
I don't think it's necessarily changing from data to experts. It's more just the paradigm of realizing that labs need this close collaboration with experts to help understand what are the evals that they're building and how can they push the frontier. But I think it's very clear that evals are evergreen, that so long as we want to improve models, we'll need experts to create evals for them and to create the post-training data for them to learn those capabilities. And of course there might be changes in the exact way that people do training with RL or otherwise, but they will always need an eval to measure what does success look like across every domain that they want to build.

Lenny Rachitsky (00:58:01):
Okay. So then building on that, a question that comes up a lot these days is, and I know we're talking about fun stuff but I'm getting to serious stuff again, scaling laws and just progression of model intelligence. A lot of people are feeling like, "I don't know, it's slowing down. We're not going to really get to superintelligence at this rate." What is your sense?

Brendan Foody (00:58:21):
I totally agree with that. I know there's been some executives to big labs that say we'll have superintelligence in three years, but I think the truth is that it's a longer road. And that's not to diminish from how extraordinary the models are. I think we'll be able to automate a majority of knowledge work tasks in the next 10 years for sure, but that long road is paved with all of the evals that help to make those capabilities possible. And it's not going to be 10X more pre-training data that gets those capabilities. It's much more going to be all of the post-training data sets that are far more data-efficient and thoughtful that help us get there.

Lenny Rachitsky (00:59:05):
David Sachs tweeted this interesting point that the situation we're now is almost the best case scenario where AI is not in this fast takeoff to superintelligence. There's a lot of competitors keeping each other in check. Models are already very valuable and only getting valuable, more valuable, but there's not just this winner superintelligence taking over the world situation.

Brendan Foody (00:59:26):
Yeah, I think that's true. I think a lot of the super intelligence fearmongering is probably overrated, but at the same time a lot of people's framing around that is even if there is a 5 to 10% chance of this P-Doom, then we should be careful, which seems logical. But I think that it's going to be an extraordinary 10 years for all of Silicon Valley and all of the world as this technology is able to create abundance and giving everyone better medical treatment, the best access to legal recommendations, and the ability to build great products more than we've ever seen before.

Lenny Rachitsky (01:00:06):
And education feels like is transforming.

Brendan Foody (01:00:08):
Absolutely, right. I even have felt bits of this over the last 10 years where I remember ever... My parents would give me a hard time for not going to classes in college and I'd be like, well, there's way better lectures on YouTube. Why not just listen there? But I can only imagine as the models get extremely good at conveying information, better than the best professor, what that'll mean and access to all sorts of information to better forward humanity and upskill everyone.

Lenny Rachitsky (01:00:41):
So I'll use that as a segue to a final question. I'm going to take us to AI Corner, which is a recurring segment on the podcast. What's some way that you personally use AI to do better work to help you in life?

Brendan Foody (01:00:52):
Well, let's see. I use it a lot to write documents, as you would expect. I also talk to get advice on problems. I find it helpful to just reason through almost as a thought partner because, yeah, I don't know. I find I think better sometimes when I'm talking something through, but I can't talk through everything with colleagues or people around me.

Lenny Rachitsky (01:01:15):
And so this is like ChatGPT Voice Mode mostly or something else.

Brendan Foody (01:01:16):
Yeah, I like ChatGPT Voice Mode a lot. There's stuff-

Lenny Rachitsky (01:01:16):
Me too.

Brendan Foody (01:01:21):
... or room for improvement, but I am very excited about the future of Voice.

Lenny Rachitsky (01:01:25):
Let me show you something I built, actually. I wasn't planning to talk about this, but there's this guy, Eric Antonow, who's been recommended by a lot of people to get him on this podcast. He's this creative product person that's under the radar now. He's at Facebook for a long time. He built this project called Pirate GPT, which is you basically put ChatGPT into a stuffed animal to talk to it. So built a little wise owl. I don't have it on right now.

Brendan Foody (01:01:25):
Wow.

Lenny Rachitsky (01:01:49):
But basically you sew in a little speaker right here and you put a little magnet underneath and you can put it on your shoulder and then you just talk to it.

Brendan Foody (01:01:57):
That's so cute. Wow. I love it. I'll have to get one of those. Because I have some of the voice assistants in my apartment, but I really want a ChatGPT voice assistant, so I'm excited for-

Lenny Rachitsky (01:02:07):
I was just thinking that. Yeah, just come on. Why can't we have a ChatGPT voice just sitting around listening to us all the time. And you can't on your phone because it goes to sleep and it's like, "Hello, what?"

Brendan Foody (01:02:17):
Exactly. Yeah.

Lenny Rachitsky (01:02:18):
Yeah, so it's what this is trying to be. Well, there's a kickstarter he started that we'll link to that. You could help out.

Brendan Foody (01:02:22):
There we go.

Lenny Rachitsky (01:02:23):
That's really easy.

(01:02:25):
Brendan, is there anything else that you wanted to share or touch on or maybe leave listeners with before we get to a very exciting lighting round?

Brendan Foody (01:02:32):
Tying to the point around initiative and that you can just do things, I encourage everyone, especially with AI and it being so much easier to build, just take the initiative to go out and build products and talk with customers and take that leap of faith because I think that that is in so many ways, the largest barrier to more innovation, the economy in any way that we can support that.

Lenny Rachitsky (01:02:58):
Yeah. There's so many people that just, let's not bash the podcast, but just listen to podcasts, read posts, just keep reading and listening and don't do anything with that information. And there's never been an easier time to actually build stuff and try stuff.

Brendan Foody (01:03:12):
Totally.

Lenny Rachitsky (01:03:12):
So definitely take that advice. Just you can do things. You can move your donut stand 50 feet and get out of their jurisdiction.

Brendan Foody (01:03:21):
Yeah.

Lenny Rachitsky (01:03:21):
Okay, Brendan, with that, we've reached a very exciting lightning round. I've got five questions for you. Are you ready?

Brendan Foody (01:03:26):
All set.

Lenny Rachitsky (01:03:27):
What are two or three books that you find yourself recommending most to other people?

Brendan Foody (01:03:31):
Let's see. I would say in order, High Output Management is a phenomenal book on running companies. Second is Zero to One, which of course is a classic. And then third is Shoe Dog, where I just find it to be a really inspirational story.

Lenny Rachitsky (01:03:46):
What is a recent movie or TV show you really enjoyed?

Brendan Foody (01:03:49):
I really liked Oppenheimer. My favorite TV show of all time is Suits, so I know not recent, but if I had to choose a recent one, probably Oppenheimer.

Lenny Rachitsky (01:03:58):
Very cool. Suits, first time someone's mentioned that. Favorite product you recently discovered that you really love?

Brendan Foody (01:04:05):
I love using Codex, like the new version. I know it's sort of new in terms of version. Yeah, I think it's incredible and just a huge, huge improvement. So yeah.

Lenny Rachitsky (01:04:19):
Do you have a life motto that you find yourself coming back to, sharing with folks, finding useful in work or in life?

Brendan Foody (01:04:25):
I think it's you can just do stuff, what we were talking about earlier. Take the leap of faith.

Lenny Rachitsky (01:04:31):
I thought you were going to say can do, which is in your Twitter profile.

Brendan Foody (01:04:34):
Can do as well, yeah.

Lenny Rachitsky (01:04:36):
Two great ones. Final question. So we were chatting before this about things that we could talk about and you shared this interesting thing that you haven't shared anywhere else, which is that you're dyslexic. Why don't you share that with folks? And just how do you get around that having built the fastest-growing company in history?

Brendan Foody (01:04:55):
I don't hide it at all. I think a lot of my colleagues know. And I think on one hand it definitely makes it difficult to go through 1,000 emails a day or read every document that I'm supposed to, but on the other hand, I feel like it helps me to think a little bit differently, to be more creative, and perhaps see that markets are changing that not everyone sees. And so it's turned out okay so far. And so I think one thing it's helped me realize from a management standpoint is that we focus much more on how we can leverage people's strengths rather than helping to improve weaknesses, because there's some things that I'm not great at and I'll never be the best in the world at, and there's others that I can hopefully refine and strive to be.

Lenny Rachitsky (01:05:46):
That's such a also recurring theme on this podcast of just focusing on strengths and not focusing over all your focus on weaknesses.

(01:05:53):
Brendan, this was incredible. I learned so much. I have a billion more questions, but you got shit to do. Two final questions. What should people know about what you're doing and roles you're hiring for? And then how can listeners be useful to you?

Brendan Foody (01:06:06):
Absolutely. We're hiring a ton across the board on our team. We're hiring strategic project leads on our operations team, software engineers in our engineering team, as well as researchers. And so please go to mercor.com and we would love to work with you, and that's the largest way that you can help us. Share it with your friends as well. Over half of people in our marketplace come from referrals because we have a platform of people that love us. And so any jobs that you want to apply to or send your friends to, we would love to have you.

Lenny Rachitsky (01:06:37):
Brendan, thank you so much for joining me.

Brendan Foody (01:06:39):
Thank you for having me.

Lenny Rachitsky (01:06:41):
Bye, everyone.

(01:06:43):
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

