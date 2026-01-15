---
guest: Asha Sharma
title: 'How 80,000 companies build with AI: Products as organisms and the death of
  org charts | Asha Sharma'
youtube_url: https://www.youtube.com/watch?v=J9UWaltU-7Q
video_id: J9UWaltU-7Q
description: 'Asha Sharma leads AI product strategy at Microsoft, where she works
  with thousands of companies building AI products and has unique visibility into
  what’s working (and what’s not) across...

  '
duration_seconds: 3431.0
duration: '57:11'
view_count: 29562
channel: Lenny's Podcast
keywords:
- growth
- retention
- onboarding
- metrics
- okrs
- kpis
- roadmap
- user research
- iteration
- conversion
- revenue
- culture
- leadership
- strategy
- vision
---

# How 80,000 companies build with AI: Products as organisms and the death of org charts | Asha Sharma

## Transcript

Lenny Rachitsky (00:00):
He said that we're just starting to scratch the surface of what an agentic society actually looks like.

Asha Sharma (00:04):
We're approaching this world in which the marginal cost of the good output is approaching zero. We're going to see exponential demand for productivity and outputs. The way that you scale to that is with agents. When all of that happens, the org chart starts to become the work chart. You just don't need as many layers.

Lenny Rachitsky (00:23):
We were chatting about this concept you have that we're moving from product as artifact to product as organism.

Asha Sharma (00:29):
Because these models are so effective at this point, you want to start to tune them to certain types of outcomes. All of a sudden, these are these living organisms that just get better with the more interactions that happen. I think this is the new IP of every single company products that think and live and learn.

Lenny Rachitsky (00:45):
Planning right now is just crazy. How does anyone plan a roadmap when there's just like, "Okay, GPT-5 is out."

Asha Sharma (00:50):
We think about it as what season are we in? Season one might've been prototyping of AI and then it was all around models and reasoning models, and now it's the advent of agents.

Lenny Rachitsky (01:03):
Today, my guest is Asha Sharma. Asha is Chief Vice President of Product for Microsoft's AI platform where she oversees their AI infrastructure, foundation models and agent tool chains, while also leading applied engineering, responsible AI and growth for the core AI division. She was previously COO at Instacart and VPR product at Meta where she ran Messenger, Instagram Direct, Messenger Kids and Remote Presence. She also sits on the boards of the Home Depot and Coupang, and she's a second degree black belt in Taekwondo.

(01:32):
Asha has a really unique and rare role that allows her to see more than most anyone else in the world, where things are heading with AI and what works and doesn't work for companies that are building large-scale AI products. In our conversation, Asha shares a bunch of trends and predictions that she's seeing that I haven't heard anyone else talk about, why we're moving from a product as artifact to product as organism world, why GUIs are being replaced by code native interfaces, why post-training is the new pre-training, the coming age agentic society, what it takes to be a successful builder today and going forward, and also her single biggest leadership lesson that she learned from Satya who she works closely with.

(02:09):
If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. Also, if you become an annual subscriber of my newsletter, you get a year free of 15 incredible products including Lovable, Replit, Bolt, n8n, Linear, Superhuman, Descript, Wispr Flow, Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD and Mobbin. Check it out at lennysnewsletter.com and click product pass. With that, I bring you Asha Sharma.

(02:35):
This episode is brought to you by Enterpret. Enterpret is a customer intelligence platform used by a leading CXN product orgs like Canva, Notion, Perplexity, Strava, Hinge and Linear. To leverage the voice of the customer and build best-in-class products, Enterpret unifies all customer conversations in real time, from Gong recordings to Zendesk tickets to Twitter threads, and makes it available for your team for analysis and for action.

(03:01):
What makes Enterpret unique is its ability to build and update a customer-specific knowledge graph that provides the most granular and accurate categorization of all customer feedback and connects that customer feedback to critical metrics like revenue and CSAT. If modernizing your voice-of-customer program to a generational upgrade is a 2025 priority, like customer-centric industry leaders like Canva, Notion, Perplexity and Linear, reach out to the team at enterpret.com/Lenny. That's E-N-T-E-R-P-R-E-T.com/lenny.

(03:35):
Today's episode is brought to you by DX, the developer intelligence platform designed by leading researchers. To thrive in the AI era, organizations need to adapt quickly, but many organization leaders struggle to answer pressing questions like which tools are working, how are they being used? What's actually driving value? DX provides the data and insights that leaders need to navigate this shift.

(03:58):
With DX, companies like Dropbox, Booking.com, Adyen, and Intercom get a deep understanding of how AI is providing value to their developers and what impact AI is having on engineering productivity. To learn more, visit DX's website at getdx.com/lenny, that's getdx.com/lenny. Asha, thank you so much for being here, and welcome to the podcast.

Asha Sharma (04:25):
Thanks for having me.

Lenny Rachitsky (04:26):
I want to start with something that we were chatting about before this that I've never heard about as a concept that I think is going to be really helpful for people to think about, which is this concept you have that we're moving from product as artifact to product as organism. Talk about what that means and what people need to understand here.

Asha Sharma (04:45):
It's been a pretty interesting shift, especially over the last year or so because when I got to Microsoft, it was right after OpenAI and the large foundation models happened, and then immediately after there was this explosion of models, proprietary open frontier models that were pushing the frontier curve and so they were both more efficient and then we're starting to see domain level expertise in a bunch of them and then even more recently, models now can tool call and they can function call and they can take action, and I think that's just giving way to a new type of products that are starting to see some success.

(05:26):
And so all of a sudden products aren't just like these static artifacts that we start to ship that's not just like, "Hey, come up with an idea or an insight. Go solve a problem, ship it into the world, maybe make it a little bit better and then have a dashboard." All of a sudden, the whole KPI is what is the metabolism of a product team to be able to ingest data and then digest the rewards model and then create some sort of outcome? Because these models are so effective at this point, you want to start tune them to certain types of outcomes, whether it's price or performance or quality. And so it's pretty exciting because all of a sudden these are these living organisms that just get better with the more interactions that happen and in many ways I think this is the new IP of every single company and it's a completely different way to build product and to even think about products that think and live and learn, which is kind of exciting.

Lenny Rachitsky (06:21):
So when I hear this, what I'm thinking about is when I had Michael Truell in the podcast, the Cursor CEO, he talked a lot about how their big moat is the data that they capture from people using Cursor, accepting certain suggestions, not accepting other suggestions. Is that what you're talking about here? Just the proprietary data that companies gather from people using their product or is there something beyond that even?

Asha Sharma (06:40):
I think why we're seeing the rise of post-training happen is just that the models themselves are so powerful. As of this year, Nathan Lambert did this study that I thought was pretty interesting of all the top leader boards and it showed that once a model hits 30 billion parameters, the CapEx to actually train a model and put billions of tokens into a pre-run doesn't economically make sense and you can start to optimize on the loop. And so yeah, in many ways, I think using your own data is the best way to do that, but you can synthetically generate data.

(07:16):
You have to come up with the rewards design, you have to actually roll it out, you have to A/B test it rigorously. You have to find the job to be done or the use case that it makes the most sense for. And then yes, that generates data that you can learn from. I haven't ever seen it be one loop for any product. I think it's multiple tracks running in parallel that are like assembly lines, if you will, and producing that.

Lenny Rachitsky (07:43):
And so is this thesis that we're moving towards product as organism, is this basically for model companies or is this also true for, I don't know, SaaS businesses and tools and user tools?

Asha Sharma (07:54):
Look, I think that software as a primitive is changing and the artifact inside of it is a model alongside the software components itself. And so in many ways I think that software products will all be model forward products, if you will.

Lenny Rachitsky (08:12):
This reminds me what I just had Nick Turley on the podcast who we were talking about before we started recording head of ChatGPT and I was asking just like how much does ChatGPT change with GPT-5 coming out, and he's just like, "It's the same thing, they're the same product. It's just the model tells us what to do in the product of ChatGPT."

(08:32):
And it makes me think about something else of just you would think why can't just GPT-5 build its own user interface just like as you use it, it just evolve. It's sort of what it's doing with Canvas and all these things, but that's another way I think about when you talk about this idea of product as organism is the product, the UX can shift based on how you're using it and evolve automatically without having product teams have to do anything.

Asha Sharma (08:53):
I 100% believe that's where the world is going, and then my experience should look and feel different than yours. That's been I've been in personalization, but now you can do it on the fly in the future. So I think that'll be a pretty fun world. I also think it will look different for agents and it will look different for power users and new users and all of those things too.

Lenny Rachitsky (09:12):
Let me zoom out a little bit and ask you this question. You work with a bunch of companies that are building AI products on your platform, other platforms. I imagine some just do an awesome job and are killing it, some are struggling. What do you find are common patterns across the companies that do really well and have a lot of success building really successful AI products and ones that don't?

Asha Sharma (09:35):
Yeah, so I think there's things that are more broadly applying to the organization themselves and then there's things that are applying to the people who are building the AI products too. So more broadly, I think there's a pattern that's starting to emerge for successful companies. One is they are embracing AI and everybody becomes AI fluent.

(09:58):
So I think everybody is using some sort of co-pilot or sort of AI in their day-to-day workflows like job one, so everyone's not afraid of it, understands how we can raise the ceiling and lower the floor for all sorts of skills and tasks. Number two, from there, they start to say, "Okay, how can I take a process that already exists and apply AI to making it better?" That might be something like customer support or taking fraud down from 15 days to cure to 10 days.

(10:26):
In going through that entire loop of mapping out the process, applying AI to it, seeing some sort of impact, and then feeling the P&L or the intrinsic benefits that looks like. The third thing then is like, "Okay, great. Now that you've seen impact, everybody is using it, how do you actually use it to inflect growth?" And that can be something like improving the customer experience, so your LTV or retention improves. It could be co-creating a new set of concepts or categories.

(10:56):
It could be going from agents that are embedded to agents that are embodied and then being able to take on exponential number of tasks. I think that where companies fail is that they're doing AI for AI's sake. They have a ton of projects that they're kicking off at the same time without a blueprint to understand how it actually worked and what their Stack looks like and they aren't treating it like a real investment, and so they don't have the measurement and the observability and the evals all set up.

(11:24):
It's going to do that end to end. I think the tricky thing is for enterprises is the technology is changing. There's something like 70,000 enterprise tools in the AI space launched last year. It's really hard to know which one you should use for what outcome. And so you really need to bet on a platform or some app server type layer that allows you to swap things in and out and not really be beholden to anything, any one technology or any one tool because the reality is the whole thing is going to change.

(11:54):
I feel like you have to actually build for the slope instead of the snapshot of where you are. So that's kind of what I see at the enterprise level. I think the builders themselves are actually changing pretty fundamentally too. Every single advent change a technology has invented a changing set of roles like mainframes to PCs like the whole garage engineers, and then when we went from server to cloud and mobile, there was like SEO specialists and CDNs and growth VMs and UXR and front end, back end, and yada yada.

(12:30):
And now I think we're seeing this advent of the polymath and where I think that full stack builders are kind of having their renaissance where if you take an average organization, it takes probably 10 steps to launch a product. It could be security review, it could be spec, it could be user research, and there's what? Five plus functions, maybe six or seven. I'm being generous for a normal organization, and then you have six or seven layers. So all of a sudden, you have 500 different touch points that have to happen to get a product out and when there are 500 models available a week or 500 new technologies, that is insufficient.

(13:15):
And so I really believe in the concept of the full stack builder. You're seeing it with a bunch of the AI native companies that are coming up. I'm even seeing it in enterprises that have been around for 50 years starting to operate in that way. And I think that gives you velocity and throughput and then gives you the whole loop to start to actually metabolize and go through that much faster.

Lenny Rachitsky (13:35):
That's definitely a recurring theme in these conversations is just the Venn diagrams of PM engineering design or starting to converge and more and more of other disciplines within your role. So PM needs to level up on design or engineering.

Asha Sharma (13:50):
Yeah, I completely agree. I think it's all about the loop, not the lane here. And so I think that whatever function you are, you have to be obsessed with trying to understand the efficiency or the cost of the product, the actual rewards or system design that you're going after, the actual UI, UX, how that actually manifests for agents or people. You have to start to get really good at that really quickly.

Lenny Rachitsky (14:21):
I like this phrase that you just use, the loop and not the lane. Can you say more about that?

Asha Sharma (14:21):
Oh, it's just going back to our previous discussion on the signals loop and products evolving and becoming these living organisms and not these artifacts. And if you think about getting really good at that loop, I think that is the product, that is the IP, that is the future of every organization and I think feedback becomes continuous and observability becomes the culture, and I think that functions start to blur in future workforces.

Lenny Rachitsky (14:49):
To make this even more real, is there an example of a product or a company that is a really good example of doing this well, living this kind of loop life?

Asha Sharma (14:57):
I think most companies that we're seeing in the space from an AI perspective are doing this. I can tell you about a couple that we are working on. Obviously in the coding space, you mentioned Cursor. GitHub has very similar features that we're using as an ensemble of models that have been fine-tuned across 30 different countries. All of the languages to actually then go iterate in a loop for next set of suggestions or code completions and things like that.

(15:25):
We've got in AI product called Dragon that's for physicians and we saw a massive difference from when we used synthetic fine-tuning to when we annotated 600,000 patient-physician interactions by experts and actually fed that into the model and continuously optimized it to then produce. I think we were sitting between 30 and 60 character acceptance rate depending on the run to something like 83%. And so that required a small group of individuals, not a large organization that were able to actually iterate in this loop across functions and all of those lines dissolving.

Lenny Rachitsky (16:07):
That's super interesting. So what I'm hearing here is if you can gather data on how things are going and then spend a lot of time creating high-quality labeling to feed back into it, to fine-tune it is basically the big advantage is how you win in a lot of this stuff. Okay. Along these lines, something else that you told me that you've been noticing that I want to hear more about is the shift from GUIs and you reference this from GUIs to code-native interfaces. Talk about what that means, what that looks like and what this means for folks building product.

Asha Sharma (16:38):
I think it goes back to what does it mean to be a product maker in the future. I think that everybody's instinct is a GUI, but if you think back in history, databases went from the desktop down into SQL, I think cloud was all about consoles and now it's about Terraform. And so I think we're literally just seeing the same pattern that's played out in history, start to play out in AI and everything else in AI, it's like Moore's law and it's getting faster. And so I think that's just accelerating and if you think about a stream of text just connects better with LLMs.

(17:14):
And so I think that there's a bunch of trends that are working in the favor for the future of products being about composability and not the canvas. And I think that product makers really need to rewire their mindset around this because I think we spend an inordinate amount of time thinking about the UI of something rather than how something composes, how an agent's going to be able to read something. How do you actually get infinite scale? How does that collaboration start to work? And so I think it's just a new way of thinking even though it's long been a trend that's happened in these changes.

Lenny Rachitsky (17:49):
So is the prediction here that it's terminals like Claude code sort of experiences or is it that it's agents that are taking or is it both? Is that what you're just sharing?

Asha Sharma (18:02):
Yeah, look, if any of us knew, that would be amazing. I just think that the reason why terminals are great and it feels really great when you code is because of the way it can interact with an LLM with the text stream. And I think that both can be true that humans will continue to commit code and will find new ways to actually do that, whether it's in the IDE, whether it's in GitHub, Copilot, whether it's in some new development environment, and I think that we'll do that with agents and agents will do that with each other and we'll continue to evolve from there.

Lenny Rachitsky (18:36):
We had Bret Taylor in the podcast, founder of Sierra, and he had a similar prediction that all software companies are going to become agent companies and it's essentially what you're saying here is that your software will just be this thing that's running in the background and there's much less of a GUI. Do you think it still becomes this chat interface the way we're getting used to? Is that the primary interface with agents or is anything something else happening there?

Asha Sharma (18:58):
I think the conversation is a really powerful interface. I worked on messaging. I think it's great for lots of forms of communication, but it's not the only form of communication. We use email today to collaborate with each other. We use docs. Everybody uses Word and PowerPoint. There's a billion people living in places of artifacts that I think can become really important composable pieces of the picture and I think they should be. So I'm excited about that. I think that chat will be important, but certainly not sufficient.

Lenny Rachitsky (19:35):
What's interesting is ChatGPT, the number one fastest growing product of all time, maybe the most important consequential product of all time is chat.

Asha Sharma (19:44):
Yeah, it's great.

Lenny Rachitsky (19:45):
It works.

Asha Sharma (19:46):
I think the question we have to ask ourselves is will it only always be chat?

Lenny Rachitsky (19:49):
Yeah, yeah. The way Nick described it is we're in the MS-DOS era of ChatGPT, which is interesting. It's like the reverse of what you're saying, so it's like maybe if you start as that and then you have to move to GUI and then maybe it'll go back, but he said there's going to be a Windows version where it's much easier to understand what the hell is going on.

Asha Sharma (20:07):
Yeah. Look, I think that it's smart. Every company should be bringing AI to where their users are and ChatGPT has all of their users using chat and it's a phenomenal product and we've got lots of people around the world that do work in many different ways and we should be thinking about how we use AI to enable that.

Lenny Rachitsky (20:28):
So let's talk about agents. You spent a lot of time working with agents, building agents, helping companies build agents. Yeah. There's a really great quote that I love. You said that we're just starting to scratch the surface of what an agentic society actually looks like. I just love this idea of an agentic society. What does that actually look like in the future?

Asha Sharma (20:47):
Oh gosh. It's funny you were telling me about your two-year-old and I have my son Ron just turned one and I can't even imagine life at two. I'm just like that is so far away and what will have been developed. Look, I think that in the future, work will look really different. I think that we're approaching this world in which the marginal cost of a good output is approaching zero. And I think when that happens, we're going to see exponential demand for productivity and outputs.

(21:20):
And I think that the way that you scale to that is with agents and it's agents that are embedded and their tools and their pieces of software. And I think there's going to be a ton of those far more than the software that we use today. And then I think there could be a set of embodied agents that are developed and we start to see that now, right? You can assign a pull request to Copilot. You can create a software development rep that's agentic that can do some of the lead generation and mining for you.

(21:50):
And so I think that when all of that happens, the work chart starts to become the work chart. I think that tasks and throughput become more important than they have been before. I also think that you just don't need as many layers. I think the whole organizational construct might start to look different in a few years, and so I'm pretty excited about it. I think meetings will still be meetings and there'll be weird, but I think that will be a bit better and I think there'll be lots of changes.

(22:24):
I think that for the average employee, my hope and my optimistic view is that they will be able to expand their skill set because now they have their own agents stack that they can bring with them to work just like you can bring your own device and you can start to have access to a set of skills that you never had before. And so if you think about the 20 million people that maybe sit in that space across America and they get 20% more skilled, it's pretty exponential for GDP, and so it's pretty fun.

Lenny Rachitsky (22:59):
This comment you made about the work chart becomes the org chart is such a profound concept because I don't know if this is what you meant, but what I'm imagining is you build these teams and here's your mission and goal and KPIs and it's humans and like, "Oh cool, go do this first." And what I'm recognizing as you're talking is like, "Okay, but if you have agents doing that, that is their prompt, go drive conversion." And then you have all these agents and that's the org. This is the conversion onboarding team and that's like a bunch of agents off doing their work. Is that what you mean?

Asha Sharma (23:33):
Yeah, I think today we think in terms of, "Hey, who reports to who in the org chart and who's responsible for these areas?" And I think at the end of the day, when you have a set of capable agents and people are capable of more things, you're not going to start to think in hierarchy and communicating up or during start to figure out outward task base type of opportunities. I think that humans will always decide in organizations how AI is used and what we want to apply it to.

(23:58):
But yeah, it's exciting when a new issue comes up or new tasks comes up, how do you actually automatically decide where to route it? Who's working on that task? How do you actually go work on it? How do you observe if they, it's doing the right thing, how do you fine-tune it if they're not, all of those things. So I think that I'm just speculating that there's a world in which that could be pretty exciting and I think that's great because we can just accomplish more.

Lenny Rachitsky (24:25):
You touch on this point that reviewing the work is going to be increasingly important. If you have a thousand agents off doing work, it's just like holy moly, that's a lot to look at and make sure they're doing the right thing. How do you think that evolves? Just being able to scale your ability to review the work that's being done?

Asha Sharma (24:40):
Yeah, I think that the same kind of loop that we talked about becomes increasingly important, like fine-tuning and self-healing observability, really good evals, all of that. The good news is that there are systems that manage this for billions of people today that already exists, and so I think that we don't have to reinvent the wheel. There's certainly going to be a bunch of new things to learn if that world ever plays out, but I think managing devices and policies and group access, all those things are solved problems, which is good.

Lenny Rachitsky (25:17):
This episode is brought to you by Fin, the number one AI agent for customer service. If your customer support tickets are piling up, then you need Fin. Fin is the highest performing AI agent on the market with a 59% average resolution rate. Fin resolves even the most complex customer queries. No other AI agent performs better. In head head bake offs with competitors, Fin wins every time.

(25:39):
Yes, switching to a new tool can be scary, but Fin works on any help desk with no migration needed, which means you don't have to overhaul your current system or deal with delays in service for your customers. And Fin is trusted by over 5,000 customer service leaders and top AI companies like Anthropic and Synthesia. And because Fin is powered by the Fin AI engine, which is a continuously improving system that allows you to analyze, train, test, and deploy with ease, Fin can continuously improve your results too.

(26:07):
So if you're ready to transform your customer service and scale your support, give Fin a try for only 99 cents per resolution. Plus, Fin comes with a 90-day money back guarantee. Find out how Fin can work for your team at fin.ai/lenny, that's fin.ai/lenny. So a lot of this, it feels like it's in the future. I know a lot of this already happening, people are using agents in all these different ways. Is there any way you and your team have found a value in working with agents of some kind other than coding I imagine is a big part of it, but just anything there that's like, "Wow, that's a big deal."

Asha Sharma (26:40):
At this point, we have AI and agents and many of our workflows, one of my favorite ones, so right now are my engineering partners out. So I jump on the live site bridges when something goes down and as something as simple as you can automatically get a summary of everything that just happened because usually, there's 15 people talking, you don't actually know where the incident started, where it's going to end and everything and then all of a sudden I have that and I can figure out and ask questions and get updates. Awesome. I think that the entire DevOps areas is changing.

(27:17):
We use use Spark to create prototypes so everybody on the team is expected to code, but sometimes just chatting in and talking in real words actually gets you to a prototype that's more interesting and more expressive and reflective of your creativity. So we use that. I think everybody's using AI to write. Everybody is using AI to find ways to have efficiencies and coming up with documentation and things like that, and so I think it's everywhere, which is cool. I think that we're just scratching the surface though for what's possible in terms of working with agents.

Lenny Rachitsky (27:58):
That's how I always feel when people ask me how I use AI. It's just like everywhere. It's just in every little sprinkled in everything I do now. I don't even know how to describe it.

Asha Sharma (28:06):
Yeah, it's hard to remember a world where it didn't really exist.

Lenny Rachitsky (28:09):
Yeah, there's a product manager that I collab with, Peter Yang who talks about how he just, "I don't even know how to do a strategy doc anymore without AI. How did people do this without having someone-"

Asha Sharma (28:20):
Do you think there will be strategy docs in the future? That's going to be interesting.

Lenny Rachitsky (28:25):
I wrote this post once of which skills of a PM job will be most replaced by AI, and strategy is the one that people are the most have the biggest debate on. You could argue, I don't know, let's get into it briefly. You would think if some AI had all of the information you had about where the market is going, your metrics, your product today, it would be so good at developing a strategy for you. Many people think that's the one thing AI will be really not good at for a long time because that's where we need all this human judgment stuff. I don't know, do you have any thoughts?

Asha Sharma (28:59):
I think that some of the most consequential products in the world required a bunch of deterministic, logical sets of inputs and sparks of creativity and imagination and judgment and vision that could not be achieved without humans. Microsoft is the vision of a software factory and creating what Microsoft did wasn't inevitable. Instacart, there was web bands and web bands didn't work, but Instacart did work because of a different way of thinking about it.

(29:40):
That came through and iteration and a bunch of things that you couldn't have learned unless you actually went through the process, the iPod, you go forward. So I think it's there. I think docs themselves for every idea, for every need will just start to fade into applications and different artifacts in the productivity suite, which is just a different way of working.

Lenny Rachitsky (30:06):
Yeah. Your original question, which I didn't quite answer, but I think is important. You're asking do we even need strategy docs? And I guess it's just somehow everyone needs to be aligned on the strategy, maybe it's not a doc.

Asha Sharma (30:17):
Correct.

Lenny Rachitsky (30:17):
Yeah, it could be some other artifact.

Asha Sharma (30:20):
If you architect an organization the right way to keep up with AI, you need a different alignment mechanisms than traditional ways of actually work.

Lenny Rachitsky (30:34):
So let me ask you actually about that. So planning right now is just crazy. How does anyone plan a roadmap when there's just like, "Okay, GPT-5 is out." Okay, great. What works for you for setting actual a roadmap and a strategy for your team? How far out do you plan? How often do you have to rethink everything?

Asha Sharma (30:49):
I'll caveat this by saying everyone's just figuring it out and it's a lot harder to figure it out when you're a larger organization than when you're much smaller and you get to run something yourself and there's pros and cons to both. So here's what we do. The company historically, at least in our product teams had semesters that they planned against.

(31:10):
So think of that as every six months there's a strategy to look back, look forward, all of those things. I think that's very valuable. I think the idea of six months though and really understanding what's changing out in front is truly challenging to have a overbaked situation. And so we think about it as what season are we in? And so a season which is very uncomfortable can be denoted by a set of secular changes that are happening in the industry or that are happening from customers.

(31:40):
And so you can think about season one might've been the prototyping of AI and the early GPT work and then it was all around models and reasoning models and now it's the advent of agents and so that can last a year, that can last six months, that can last three months. But grounding everybody on the ethos of what are the secular changes? What are the customer problems we need to solve? What does winning look like?

(32:06):
So everybody has that shared sense. What is the north star metric is something that we do. The second thing that we do is that we have kind of loose quarterly OKR. So like, "Okay, if we believe that, what do we need to do next quarter to actually put ourselves on a path to that?" And then from there, teams are operating in squads and they're kind of setting out four to six week goals that they're trying to go after for problem areas to go ladder up to that and especially as the platform for the company and the platform for our Azure customers with AI, I'll say we go through lots of changes to that all the time and I think we have to just have an openness that that is the business that we're in.

(32:47):
I think the other thing is just we try to leave Slack in the system, not just for the unplanned, but for the slope. I think that we have to continuously be thinking about how we're going to disrupt the platform in our thinking and what we need to be investing in to make that possible. And so we try to do a little bit of both.

Lenny Rachitsky (33:06):
This is awesome. So what I'm hearing here is there's this concept of seasons and everyone's aligned, "Okay, this is time for agents, this is what's happening right now. We're going to center around our strategy around agents." And then there's these loose quarterly OKRs. You plan for three months roughly and then you leave some Slack in the system for things to change.

Asha Sharma (33:24):
Yes.

Lenny Rachitsky (33:24):
Is the current season agents, how would you describe what season we're in right now?

Asha Sharma (33:27):
Yeah, it's agents. The rise of agents.

Lenny Rachitsky (33:31):
The rise of agents. It sounds like a Terminator movie. Do you have a sense of what the next season might be? Is there any like, "Oh, this might be coming next."

Asha Sharma (33:39):
Gosh, I don't, but I think that, look, we have more than 15,000 agents that are deployed on our service today, at least at the Azure service. There's a bunch of other platforms in the company and I would just say that I think that we should really focus on making sure that we have all of the alignment, accountability, observability, evals to making those agents great.

(34:11):
I think that Manus breakthrough in the space was that they could do these tool calling loops and have agents do longer running tasks that really no other platform was able to do. I think stuff like that is critical. Memory is critical. There's still a bunch of building blocks that I think are leaving agents incomplete in the wild that I think we have to really sweat the details on before we move on.

Lenny Rachitsky (34:37):
So it's just like agents until the end of time until super intelligence and then we're just on beaches chilling.

Asha Sharma (34:44):
Yes, agents until dank memes look. Yeah, I think the cool thing is something new could come in three months. Something new could come in 13 months. I think we have this conviction on a set of building blocks that we want to provide to enable these agents to endure and have high endurance and so that's what we're focused on.

Lenny Rachitsky (35:07):
When you said there's 15,000 agents, what does that mean? Is that 15,000 types of agents you can use or is it like that's how many processes are?

Asha Sharma (35:13):
No, that's customers. 15,000 I think I should re-reference the numbers. 15,000 customers who have produced agents. I think the number of agents is actually millions.

Lenny Rachitsky (35:24):
15,000 customers that are building a specific kind of agent on your platform and they're running and the number of agents is in the millions just running in the cloud.

Asha Sharma (35:32):
Yes. Exactly.

Lenny Rachitsky (35:33):
Okay. It's wild. Some crazy numbers here. Okay, so let me just go in a slightly different direction. You're in the center of the storm of a lot of AI, just seeing everything else going on. Is there something you wish you'd known before stepping into this role that you're just like, "Okay, I see. I didn't expect this."

Asha Sharma (35:52):
When I first took the role, it was described as the belly of the beast and I had spent most of my career building products at the center of machine learning and applications or businesses and I think that to my surprise, a lot of the learnings have translated in terms of what makes a great platform is what makes a great product. And the thing for me is it's often in the invisible work or not the pixels that actually drives that.

(36:26):
So for example, one of the first companies that I worked at was a company called Porch Group. I was employee seven and we knew we wanted to help people take care of their home and I think we invented so many features like the home report or a way to manage your home or house style inspiration where you could see all of the houses and it's map every single room. And the single most important thing that we could have done and did during my time there was create a matching platform that matched the 6 million professionals with the 1,300 service types with the 37,000 zip codes and all of the homeowners in North America to actually take care of their home, and that was just the game of inches and optimizing that engine in order to create higher quality leads essentially.

(37:15):
That's what got us to the first $500 million valuation. That's eventually what we built on to actually have other vertical services and software platforms that IP of the company. Same with messaging. The number one learning that I had was look like WhatsApp didn't win because it had stickers or stories or dark mode. In fact, I don't even think it had all of those things when it won. It won on a few premises because one was the phone book, you knew that when you use WhatsApp, you could reach every single person because you had their phone number and those are the people that you care about when you're using messaging.

(37:54):
It was the reliability and how fast it was. I could text my grandmother in India and know that she would get my text message all the time, and then it was the privacy. When you are sending 200 messages a day to the four people you care about most, you want to make sure no one else can read the messages and so the end-to-end encryption really mattered. And so it wasn't the hundreds of features, it was all in the infrastructure and the platform.

(38:21):
Same Instacart, there are so many loved features of Instacart, but at the end of the day, it's a billion items that updates 3,000 times every single minute to get homeowners their groceries from the store that they love. And so I think I wish I had known that because I think it would've curtailed my learning curve to say that it's not all the features for the platform that matters, it's the data residency.

(38:46):
So the hospital in Germany that's fine-tuning the model can do so in confidence and the data isn't going to leave the region, it's the availability, it's the reliability. It's making sure you have the right selection of the tools that enterprises need and the right way to retrieve the knowledge and that's the platform that we've built but just didn't fully have that picture that those learnings would translate.

Lenny Rachitsky (39:07):
Mm-hmm. That's really interesting. So what I'm hearing is people undervalue who just the simple bottom of the Maslow hierarchy of things that help you win in platforms, especially in messaging platforms including so it's like reliability, privacy, I don't know, availability.

Asha Sharma (39:26):
Yeah, performance, reliability, privacy, safety, all of those things.

Lenny Rachitsky (39:31):
Mm-hmm. Let me ask you a totally different question. When we were going to record this previously and you're like, "Oh, I have a big meeting with Satya I got to do instead." And so we moved at a different time. Very few people get to work with Satya, he's quite a successful leader. What's something you've learned from him about? I don't know, leadership or product building?

Asha Sharma (39:52):
I've learned that optimism is a renewable resource. This company for 50 years has had every reason not to succeed and it has even as it's had early success in the AI era and challenges and other successes and the space is developing so quickly, I think that his ability to generate energy and to use his optimism to renew everybody's dedication to the mission is unbelievable and I think it's such an important part of the culture. Everybody talks about the growth mindset, that's real, huge part of the culture, but I think the ability to generate energy and clarity on what we need to go do and use optimism to renew the commitment every single day for every single person in an entirely competitive talent space is pretty amazing.

Lenny Rachitsky (40:54):
Is that something you think that is just innate to him or it's something that he's worked on to just generate this optimism on behalf of everyone?

Asha Sharma (40:59):
I have no idea. We should ask him, but I'm deeply impressed by it.

Lenny Rachitsky (41:04):
It's interesting that a lot of this comes down to just vibes. There's just this vibe of imagine it's not him just the words he uses, it's just this energy that he exudes optimism and energy.

Asha Sharma (41:16):
Think about it. We all choose to someone who just said this to me and I thought it was great, "We all choose to close the door on our kids every single day to go work on something." And so you have to work on something that is deeply moving to you and you have a deep belief that is going to make the world a better place and I think that's why it's vibes. I think you have to follow and have a sense of duty towards a mission that is bigger than yourself.

Lenny Rachitsky (41:45):
It makes me think of a line that I've referenced a couple of times on this podcast that hits people really hard that the only people that'll remember you working late are your kids.

Asha Sharma (41:54):
Okay. I don't know where we're going with that, but that was like, now you're like, yeah.

Lenny Rachitsky (42:02):
It's too much. We've gone too far. Oh man. Okay. Well let ask you this. What's driving you?

Asha Sharma (42:04):
We could have said our customers, we could have gone a different route on that one.

Lenny Rachitsky (42:09):
This is the real stuff. What's driving you? What's driving you? What's keeping you excited about the work that you're doing?

Asha Sharma (42:17):
What AI will help us do from a workforce perspective, what it will help us do from a healthcare perspective. My mom has cancer and I think a lot about how we might find a way to solve the form of cancer she has in my lifetime and I never thought that was possible three years ago. All of that's deeply profound and the thing that I personally think a lot about now that we know that we're living in this time working with such powerful technology is the effects of it and how I can best build a platform where people can make use of it.

(42:52):
So the reason why I work at Microsoft is because the whole ethos of the company is how do I help people and businesses achieve more and more for me in the thing I think about at night outside of GPUs is I think about will my son have classmates in the future? And that's not because agents are going to replace them, it's because the fertility rates are declining. The average birth rate in the '90s when we were growing up was like three and now it's 2.3 and in 2050, it's estimated to be below replacement and I think that AI can have such a big effect on it and already is.

(43:42):
It was just reading about a hospital in London that's able to improve pregnancy rates by using AI to match eggs and sperms and their cutting costs at the same time. You saw with the ChatGPT-5 launch yesterday. Such an amazing story about how ChatGPT is helping in healthcare. Stanford is one of our big customers with the platform that I build and they're working on using AI for tumor reviews and it's just like, it is these sets of things that will move humanity forward and expand our lifetime and give us the privilege to solve 100-year problems. And so that's why I'm excited and that's why I do what I do.

Lenny Rachitsky (44:22):
Yeah, especially in your role where you're building the platform that enables all of this, I could see how impactful that could be. Asha, is there anything else that you wanted to touch on or share or double down on of anything we've talked about before we get to our very exciting lightning round?

Asha Sharma (44:39):
We touched on it a little bit, but I think that with the advent of agents and products that think and can act and reason, there's going to be this new wave around RL and I have a deep belief that that will become one of the most important product techniques of the next season or at least the next few seasons.

Lenny Rachitsky (45:00):
And RL is reinforcement learning?

Asha Sharma (45:02):
Yes. Yes, exactly. I believe we will see just as much money spent on post-training as we will on pre-training and in the future, more on post-training. We talked a little bit about Nathan Lambert's study where his review was that when a model hits 30 billion parameters, it makes more sense to fine-tune and optimize that 50% of developers according to surveys are now fine-tuning and we know fine-tuning is good, but if you actually go through the full loop, you can get better results.

(45:30):
So I think there's a bunch there and I think there's a whole new set of infrastructure and platforms and companies that will be created that are all around this part of the stack. And so I think it's an exciting time to be in the platform space, but it's also an exciting time to be starting companies and be thinking about those problems.

Lenny Rachitsky (45:48):
I want to make sure people truly understand what you're saying here because not everyone truly understands post-training, pre-training. What's the simplest way to understand the difference there and just why it's such a big deal that investment is moving to post-training?

Asha Sharma (46:02):
The way that I think about it is to create a foundation model, it requires a tremendous amount of compute, a tremendous amount of science. Expertise as we're seeing which the cost for scientists or the average value is raising dramatically and I think an expertise that we've seen isn't everywhere in the world right now. And so it's just a big CapEx investment to do that.

(46:33):
With this explosion of models that we talked about in the beginning, there's a lot of good models to choose from for different domains. And so I think that you just get more leverage economically, you get more leverage from a taste perspective of how you actually want to steer a model if you're actually doing reinforcement learning or some sort of fine-tuning to actually start to optimize what's off the shelf for some outcome like price, performance, quality.

(46:58):
If you think about that, that's not crazy, right? Ranking is an age-old optimization problem where you don't want to just take what's off the shelf because there's amazing frameworks and UI and components that the world is react components that are out there. You still want to tailor the experience to a set of use cases or a set of people. I think it's just the same industrial logic.

Lenny Rachitsky (47:22):
So in practice, what this means is there's a GPT-5 model. You're saying there's a lot of opportunity and a much more efficient way to spend money, which is take something like that and then train that on additional custom data that you have, whether it's data or just reinforcement learning, maybe even with humans to align it with what you wanted to achieve?

Asha Sharma (47:41):
Yep, and it could be your own data, it could be data that you buy, it could be synthetic data, it could be something else, but I think that we're going to start to see more and more companies and organizations start to think about how do I adapt a model rather than how do I take something off the shelf as is or invest a bunch of money and building my own models.

Lenny Rachitsky (48:06):
Yeah, I forget. I know Cursor, when he was on the podcast, he shared that they have a bunch of models that support your experience with Cursor and over time, they're just going to have their own thing. I forget who it was, Windsor for one of those guys just uses their own model now, they don't just plug into Claude.

Asha Sharma (48:22):
I'm much more in the model system camp. I believe in model diversity. I think that in experience like Claude, like Sonnet 4 is awesome for a set of use cases versus GPT-5 is different for different use cases. I think that there's some tasks where you care about the latency of the model. You're cool with the thinking time or you want a quick retrieval and things like that. I think the beauty is there's a lot of models that can help you achieve that, and so I'm much more in the model system rather than one model to rule them all.

Lenny Rachitsky (48:58):
Is that the right term? I've also heard ensemble model, ensemble of models.

Asha Sharma (49:01):
I think about an ensemble of models as a set of multiple models that then you can fine-tune and deploy independently, but at this point, we're all making up different terminology to define things that we have deep beliefs on that have limited sets of data points because everything is moving so fast.

Lenny Rachitsky (49:18):
Yeah. With that, we've reached our very exciting lightning round.

Asha Sharma (49:23):
I'm very excited for our lightning round and I'm turning down the lights

Lenny Rachitsky (49:27):
And then it'll come back on I imagine in one second. Okay. First question, what are two or three books you find yourself recommending most to other people?

Asha Sharma (49:34):
At work? It's probably Thinking Machines, so it's all about treating the cause, not the symptoms. The prototypical example is if you want to solve traffic, you don't actually put up speed bumps or speed limits, you actually have to solve walkability and mobility and why people actually use cars. Outside of that, personally, the CMO of Instacart recommended to me Tomorrow, and tomorrow, and tomorrow and I read it last month and last year and the year before because I love it so much. It's like this beautiful story over 10 years.

Lenny Rachitsky (50:12):
Mm-hmm. What are some favorite recent movie or TV shows you really enjoyed?

Asha Sharma (50:18):
Formula One, saw it twice for all mankind. For all Mankind, I like season four. I don't know, I like playing alternative theories to how the space race might have looked.

Lenny Rachitsky (50:32):
Do you have a favorite product? That you recently discovered that you really love? Could be tech, could be gadgets, could be clothing.

Asha Sharma (50:36):
So I just joined the board of the Home Depot and we're doing a little renovation project and so there's this new, well, new to me DEWALT power pack and they use pouch cells and so it's like 50% lighter, but with all the power and it's awesome for drills and things that I need to lift up with one hand that feel heavy. So I love that.

(50:59):
We also are testing out this new brilliant, smart home kind of system. So it's four inches of high-res middleware that allows you to connect to everything and I've reached peak dissat with the explosion of all the technology required to actually use your home. So it just might be the middleware that sticks, but we'll see.

Lenny Rachitsky (51:22):
Did you say dissat? Is that short for dissatisfaction?

Asha Sharma (51:26):
Yes. Sorry. I'm speaking in acronyms.

Lenny Rachitsky (51:28):
Whoa, I've never heard that dissat. I love that. By the way, I love that you're on the board of the Home Depot. What a different part of the spectrum of work.

Asha Sharma (51:40):
Yeah, it's been awesome. The very first board meeting, the head of philanthropy has been at the company for decades and she said, "Welcome to the greatest company on the planet." It's pretty special.

Lenny Rachitsky (51:52):
They're like, "Microsoft." Is there something you've learned from working with them that you've brought to Microsoft?

Asha Sharma (52:00):
Look, it's new, it's this year, but I've long worked on products that had that impact. So when I was at Porch, it was pros. At Instacart, we had 600,000 shoppers and obviously, the Home Depot has associates. One of my favorite things about the company culturally is they have this inverted pyramid where instead of having executives at the top, the associates are at the top and the stores themselves are headquarters and then the traditional HQ is support.

(52:35):
And so it's so customer-centric and when I think about amazing execution and creating these durable long-term institutions and how culture and ideology and leadership is formed, I think about that and I think about at the end of the day, AI is going to have an impact on every single person and every single job. And it's amazing to just spend time with people outside of our bubble and really try and learn what their real pain and problems and how they think about AI and how they think about technology and what we need to do.

Lenny Rachitsky (53:09):
Okay, two more questions. Do you have a favorite life motto that you find yourself coming back to? Sharing with friends or family?

Asha Sharma (53:18):
I used to use the minimize regret framework and it's great, and I've used that for a long time. I think that probably once I got into my adult years and started to have a family and things like that, my just worldview changed a little bit and it was all about maximizing option value and it just gave the things that I naturally cared about like family and health and trust and relationships.

(53:51):
It was just a new level of value associated with those because all of a sudden, learning rest on the weekend can compound in the future or having good health can compound in the future. You don't have to trade that off of working extra hours or the importance of family and all of those things. And so I think that my worldview is when I'm 70, it's not about what do I look back on in my life and count the number of regrets, it's really about looking forward in the number of adventures I will still have because I have accumulated this wealth of skills and trust and people and family and impact and things like that.

Lenny Rachitsky (54:31):
Speaking of skills, the internet tells me that you're a second degree black belt in Taekwondo. Why? Oh gosh. Is this true? And then I have a question about it.

Asha Sharma (54:44):
This is true.

Lenny Rachitsky (54:45):
Okay. That's incredible. Why is this embarrassing? That's an incredible thing.

Asha Sharma (54:52):
I am generally embarrassed anytime anything is discussed about me.

Lenny Rachitsky (54:56):
Okay, great. No problem. What's something that you learned from Taekwondo that has helped you with life or work?

Asha Sharma (55:03):
Taekwondo is more mental than it is physical. And so I think that's the same with all of our jobs and making product. I think it's like mental clarity, it's courage. It's the ambition to see things through and be unwavering. And so I think that's literally what it taught me outside of meditating, which probably took me the entire time to actually learn to meditate and clear my head. But yeah, I think it's awesome. I think everybody imagines flying psychics or running up a wall and you can do those things too, but the real value is the mental pursuit of it all.

Lenny Rachitsky (55:47):
And you can do those things too. Wow. Okay. I'm good. I got to get into this. Asha, this was awesome. Is there, oh, actually two final questions. Where can folks find you online if they want to maybe follow up on anything, if you want people to reach out and how can listeners be useful to you?

Asha Sharma (56:02):
You can hit me up on LinkedIn or email or text. I think all of those are traceable. Look, how can you be helpful to me? I think we're all early in this journey and great platforms that are built on great use cases and built on great customers, and so if you have feedback, you have ideas, you have things want AI to be able to do to help you achieve more, I'd love to hear it. I think the thing about all of these changes is that all of these new products and use cases will be developed everywhere, and so I'm always just thinking about how can we be the platform to support that.

Lenny Rachitsky (56:40):
Amazing. Asha, thank you so much for being here.

Asha Sharma (56:42):
Thanks for having me.

Lenny Rachitsky (56:44):
Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

