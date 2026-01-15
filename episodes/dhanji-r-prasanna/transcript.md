---
guest: Dhanji R. Prasanna
title: How Block is becoming the most AI-native enterprise in the world | Dhanji R.
  Prasanna
youtube_url: https://www.youtube.com/watch?v=JMeXWVw0r3E
video_id: JMeXWVw0r3E
description: 'Dhanji R. Prasanna is the chief technology officer at Block (formerly
  Square), where he’s managed more than 4,000 engineers over the past two years. Under
  his leadership, Block has become...

  '
duration_seconds: 5202.0
duration: '1:26:42'
view_count: 31288
channel: Lenny's Podcast
keywords:
- growth
- metrics
- roadmap
- experimentation
- revenue
- hiring
- culture
- leadership
- management
- strategy
- vision
- mission
- competition
- market
- persona
---

# How Block is becoming the most AI-native enterprise in the world | Dhanji R. Prasanna

## Transcript

Lenny Rachitsky (00:00:00):
There's a lot of talk about productivity gains through AI. There's this camp of people that are so overhyped, nothing's working, nobody's actually adopting this at scale.

Dhanji R. Prasanna (00:00:07):
We see a significant amount of games. We find engineering teams that are very, very AI forward are reporting about eight to 10 hours save per week. Whenever I hear a stat like this, I think an important element is this is the worst it will ever be. This is now the baseline. The truth is the value is changing every day, so you need to ride that wave along with it.

Lenny Rachitsky (00:00:27):
There's a story I heard you share on a different podcast where there's an engineer who has Goose watching.

Dhanji R. Prasanna (00:00:31):
You'll be talking to a colleague on Slack or an email, and they'll be discussing some feature that they think is useful to implement. Now a few hours later, he'll find that Goose has already tried to build that feature and opened a PR for it on Git.

Lenny Rachitsky (00:00:43):
What level of engineer is most benefiting from these tools?

Dhanji R. Prasanna (00:00:47):
What's been surprising and really amazing, the non-technical people using AI agents and programming tools to build things, the people that are able to embrace it to optimize for their particular workday and their particular set of tasks are really showing the most impact from these tools.

Lenny Rachitsky (00:01:07):
How do you think things will look in a couple of years in terms of how engineers work that's different from today?

Dhanji R. Prasanna (00:01:12):
All these LLMs are sitting idle overnight and on weekends, while humans aren't there. There's no need for that. They should be working all the time. They should be trying to build in anticipation of what we want.

Lenny Rachitsky (00:01:24):
What's maybe the most counterintuitive lesson you've learned about building products or building teams?

Dhanji R. Prasanna (00:01:29):
A lot of engineers think that code quality is important to building a successful product. The two have nothing to do with each other.

Lenny Rachitsky (00:01:37):
Today my guest is Dhanji Prasanna. Dhanji is Chief Technology Officer at Block, where he oversees a team of over 3,500 people. With Dhanji's leadership, Block has become one of the most AI-native large companies in the world and has basically achieved what many eng and product leaders are trying to achieve within their companies.

(00:01:55):
In our conversation, we chat about their internal open source agent called Goose, that by their measure is saving employees on average eight to 10 hours a week of work time, and that number is going up, how AI specifically making their teams more productive and the teams that are benefiting most. Interestingly, it's not the engineering team, what it took to shift the culture to be very AI-oriented, the very boring change they made internally that boosted productivity even more than any AI tool.

(00:02:24):
Also, lessons from building Google Wave and Google Plus and Cash app and so much more. This episode is for anyone curious to see what a highly AI-forward technology-driven large company looks like and can act like. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It helps tremendously.

(00:02:45):
Also, if you become an annual subscriber of my newsletter, you get a year free of 16 incredible products including Devin, Replit, Lovable, Bolt, n8n, Linear, Superhuman, Descript, Wispr Flow, Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD and Mobbin. Head on over to Lennysnewsletter.com and click Product Pass. With that, I bring you Dhanji Prasanna after a short word from our sponsors.

(00:03:12):
This episode is brought to you by Sinch the Customer Communications Cloud. Here's the thing about digital customer communications. Whether you're sending marketing campaigns, verification codes, or account alerts, you need them to reach users reliably, that's where Sinch comes in. Over 150,000 businesses, including eight of the top 10 largest tech companies globally use Sinch's API to build messaging, email and calling into their products.

(00:03:38):
And there's something big happening in messaging that product teams need to know about. Rich Communication Services or RCS. Think of RCS as SMS 2.0. Instead of getting texts from a random number, your users will see your verified company name and logo without needing to download anything new. It's a more secure and branded experience, plus you get features like interactive carousels and suggested replies, and here's why this matters. US carriers are starting to adopt RCS.

(00:04:06):
Sinch is already helping major bands send RCS messages around the world and they're helping Lenny's podcast listeners get registered first before the rush hits the US market. Learn more and get started at sinch.com/lenny. That's S-I-N-C-H .com/lenny. This episode is brought to you by Figma, makers of Figma Make. When I was a PM at Airbnb, I still remember when Figma came out and how much it improved how we operated as a team.

(00:04:35):
Suddenly, I could involve my whole team in the design process, give feedback on design concepts really quickly, and it just made the whole product development process so much more fun. But Figma never felt like it was for me. It was great for giving feedback and designs, but as a builder, I wanted to make stuff. That's why Figma built Figma Make. With just a few prompts, you can make any idea or design into a fully functional prototype or app that anyone can iterate on and validate with customers.

(00:05:02):
Figma Make is a different kind of vibe coding tool, because it's all in Figma. You can use your team's existing design building blocks, making it easy to create outputs that look good and feel real and are connected to how your team builds. Stop spending so much time telling people about your product vision and instead show it to them. Make code back prototypes and apps fast with Figma Make. Check it out at figma.com/lenny. Dhanji, thank you so much for being here and welcome to the podcast.

Dhanji R. Prasanna (00:05:34):
Thank you Lenny. It's a great pleasure to be here.

Lenny Rachitsky (00:05:37):
I want to start with a letter that I hear you wrote to Jack Dorsey to convince him that he and that Block needed to take AI a lot more seriously. I think you called it your AI manifesto and it seems like it really worked. We're going to talk a lot about the changes that came as a result of that. So let me just ask, what did you say in this letter and what happened right after you sent that letter to him?

Dhanji R. Prasanna (00:06:00):
So about two and a half years ago or so, Jack really felt like things needed to change. I think he had a sense that the industry was going in a different direction. So he got about 40 of the company's top executives into a room on a weekly basis, and they all used to sort of talk everything through that was going on and he added me to that group.

(00:06:26):
So at some point, I observed that we were talking about lots of deep things, lots of relevant things, but no one was really paying attention to AI, and so that's when I wrote that letter. And to be honest, it's I think taken on a life of its own, but there wasn't much to the letter other than I think we should do this. I think we should do it centrally and it's important for us to be ahead of the game and be an AI native company because that's where the industry is heading.

Lenny Rachitsky (00:06:55):
Let me just say it's important to note you were not CTO at this point. You were just a senior engineer kind of person?

Dhanji R. Prasanna (00:07:00):
No, yeah, in fact, I was part-time at the time because I had just had a kid and I was coming back in and I was helping out one of the engineering teams and then Jack came over to Sydney and spent two days with me and both of us like long walks. So we walked all around Sydney and talked it through up and down, and then yeah, he offered me the job and I thought it was a great opportunity once in a lifetime, so I took it.

Lenny Rachitsky (00:07:30):
It's like be careful what you're good at sort of situation. Okay. So what were some of the bigger changes that you made after Jack is on board and Block execs are on board of are, "Cool, this is completely right. We need to go much bigger and think much more deeply about how AI is changing, how we build and how we should build." Or some of the bigger changes that you made from a perspective of other companies listening to this, trying to think about what they should be doing?

Dhanji R. Prasanna (00:07:53):
At the start, my main focus was to get block to think like a technology company. And for a long time we had had a little bit of, I'm going to call it identity drift, maybe. We were talking about ourselves as a financial services company. Some people called us FinTech, all of this stuff. But when I started working at what was then known as Square, we were always thought of as a technology company just like Google or Facebook or any of the others.

(00:08:25):
And so I wanted to get us back to that. And so the first thing I did was to try and institute a number of programs that focused on that. So everything from getting the top ICs in the company together to talk to each other, to starting a whole bunch of special projects. So we got about two to five engineers per project. There were about eight or nine different projects and we had reinstituted, the company-wide hack week.

(00:08:55):
And so all of this just kind of created a little bit of a spark of, "Hey, we're building technology again, we're trying to push the frontier again." And that's how it started, and then there were a whole number of steps after that where we went from a GM structure to a functional org structure, which was I think the key to making our transformation into being more of an AI-native company.

Lenny Rachitsky (00:09:19):
Okay, talk more about that. What does that mean? What does that look like? Why is that so important?

Dhanji R. Prasanna (00:09:23):
Absolutely. So when we were in our mature phase, so when Square was working quite well, it was a very large business, and then we had started Cash App and that also followed suit. We had spun them out almost as what we call a GM structure. So they were effectively run as a portfolio of independent companies and they had their own CEOs who all reported to Jack and it was still one single executive team, but they had separate engineering practices, they had separate design teams.

(00:10:00):
They were kind of separate in almost every way except for some shared resources like our foundational resources like legal and some platforms and things like that. So I think that that was very useful for us for the stage of company that we were in, but when you really want to go deep in technology, when you really want to connect with these things that are industry changing events that are happening, you need a singular focus, and we changed the organization.

(00:10:32):
So all engineers report into one single team now, all designers report into one single team and there's single head of engineering, single head of design, et cetera. And so that was the big transformation that we made, and that meant we could really drive forward AI, we could drive forward platform and just technical depth generally.

Lenny Rachitsky (00:10:51):
For companies that are struggling with this potentially or trying to figure out how to do this, two things I'm hearing here is start to see yourself as a technology company. It doesn't necessarily apply to every company, but seems like an important element is like we're building technology, we're not a financial company, we're not a real estate company, we're not a technology company. And then two is organize the team such that say engineers report up to an engineering leader versus a GM who maybe doesn't understand engineering as well or doesn't take it as seriously as they should.

Dhanji R. Prasanna (00:11:19):
Yeah, I think that's pretty much what we did. And not to lean too heavily on this, but this is what jobs did when he came back to Apple as well. He reorganized Apple to be functional, and it wasn't like we were following a playbook. We discovered this as we were investigating what it's going to take to make these teams more tech-focused and to bring our DNA back to our roots, which really was putting engineering and design first, which is what technology first means to me. So yeah, I would say to companies, find your DNA and really try to optimize for what that is in a very simple and clear way.

Lenny Rachitsky (00:12:00):
Okay, so you made a bunch of changes, you had this manifesto, everyone's on board, you made a bunch of changes. Functional technology first, comparing the way that your say engineering team works today versus two or three years ago, what is most different?

Dhanji R. Prasanna (00:12:13):
Not everyone was on board, I'll tell you that. It was quite a painful transformation. I think that one of the things that I learned the most throughout this process is that Conway's Law can be really, really powerful. So it's the law that basically says you ship your org structure. So what you're organized as in terms of teams, in terms of collaborating groups and your operating model matters a lot to what you build.

(00:12:45):
And so I think that that was essentially the biggest change is we had a lot of momentum in each of these silos, be it Cash App, be it Afterpay, be it Square or even TIDAL or music streaming service. And no one was really talking to each other, no one was really aligned on technical strategy on what we even wanted to be five years from now as a collective team. And so all those things are different now. I'm not saying it's perfect, there's still a long road ahead of us, but we at least speak the same language.

(00:13:24):
We're all have access to the same tools, we share the same policies. So a certain level of senior engineer means the same thing across the whole company. People can move from one team to another's into an area of need. All of these things are very different. But to sum it up, I would say we're technically focused and we're focused on advancing technical excellence as a goal. And that just really wasn't that true two to three years ago. There were other things we were optimizing for then.

Lenny Rachitsky (00:13:58):
Maybe going one level deeper in terms of how people actually work at a day. So if you're looking at an engineering team, say the average engineering team and maybe also the top most optimal engineering team, how is the way they work today different from a couple of years ago?

Dhanji R. Prasanna (00:14:12):
In the small, certain teams that are very, very AI natives or teams that are building AI first everywhere are working much differently than before because they're using vibe code tools and they're essentially building without writing lines of code by hand, and that just wasn't true through the three years ago. I don't think it was true anywhere in the world. So that's dramatically different in teams that are still working with very heavy legacy code bases.

(00:14:47):
It's less true, but they're also encountering these background AI processes. So we have these tools that run 24/7 or run in the CI pipeline and they're analyzing vulnerabilities. They're looking at even bugs filed on tickets and trying to build patches while engineers are asleep. So they come in the next day and look at it. So I would say there are a number of ways in which they're different, but different teams have adapted in different ways depending on how close they are to the tools.

Lenny Rachitsky (00:15:25):
Okay, so let me lean into that AI piece, which is I think where you guys are most ahead of a lot of other companies. You guys built your own agent I think is how you describe Goose. So there's a lot of talk about productivity gains through AI. There's this camp of people are like, you don't understand how much productivity there is to gain from AI. It's the future, this is the way it's all going to work.

(00:15:46):
We're all accelerating 10X. There's also this camp where people are like, I'm so overhyped, nothing's working. People talk about it. All these pilots are failing. Nobody's actually adopting this at scale. I feel like you're probably in that first camp. What sort of gains have you seen practically from AI tools on your teams?

Dhanji R. Prasanna (00:16:03):
Our number one priority is through automate Block, which means getting AI and getting AI forms of automation through our entire company. And we feel that that's just at the beginning of where the utility is with all these large language models, and I think we're going to continue to see that improve. But even now, we find engineering teams that are very, very AI forward that are using Goose every day are reporting about eight to 10 hours saved per week, and this is self-reported. And then we also have a number of check metrics to try and validate that.

(00:16:45):
So we look at PRs, we look at throughput of features, we look at a whole bunch of things and we have our data scientists come up with a complicated formula that tries to distill it all into something meaningful. And we feel across the whole company, we're probably trending towards 20 to 25% of manual hours saved. And I think that's just the start of all of this. I do feel that the more AI-native companies are doing a better job of realizing this.

(00:17:17):
So companies that started just with AI startups mostly, but there is some truth to this notion that AI isn't a panacea and it's growing as well in capability. So you need to ride that wave along with it. And I think a lot of the companies aren't realizing this. They're like, "Well, where's the value?" And the truth is the value is changing every day. And so you need to be adaptable and look at what the value is today and plan for what the value will be tomorrow and then slowly expand to the areas where it's most efficacious.

(00:17:54):
I'll give you an example. One area in which we find that it's really good is for non-technical teams to be able to build little software tools for themselves. So this has been one of the most surprising and energizing uses of Goose within Block is we'll have our enterprise risk management team build a whole system for self-servicing enterprise risk, and this is compressing weeks of work into hours, or ordinarily, they would be waiting for an internal apps team or something to go and build that and they would put that on their Q2 roadmap and everyone would be twiddling their thumbs until it all clicked into place, but now you can just go and do it.

(00:18:42):
And so a lot of these kinds of use cases we're seeing an enormous amount of productivity gain in the other area, which I'm really excited about is we have this other tool called Gosling, which is a goose for mobile effectively. So it operates your Android OS at a native level using the accessibility API. And we use that for automating UI tests.

(00:19:09):
So before, you would have to hire an army of contractors or QAs who would go and click through every screen, but now we can just bake those into automated tests and then give you a report at the end. So we're seeing a lot of advantages in those types of areas, but where you have a lot of depth and a lot of really strong people come together is where AI, I think still underperforms humans. And that's something that's probably going to get better over time, but it's also something where we should lean into as humans.

(00:19:45):
So when you have some very senior engineers and they're thinking about things like architecture and design and race conditions, orchestration, things like this, that's still an area where AI isn't quite there. And so I think the companies that aren't feeling the success in AI are trying to just throw these tools at their giant code bases and hoping good things will happen, and that's not how it's playing out. Eventually, I do think it'll get there, but right now we're still in the early utility phase.

Lenny Rachitsky (00:20:18):
Holy moly, there's so much there in what you just shared. There's like five things I want to follow up on. Okay, so one is this metric you kind of alluded to, which is how you measure the impact of AI in your team. So it was human manual hours saved, is that how you describe it?

Dhanji R. Prasanna (00:20:35):
That's correct. Yeah.

Lenny Rachitsky (00:20:36):
So it's roughly a fourth of an engineer's time currently is being saved by AI tooling.

Dhanji R. Prasanna (00:20:43):
That metric is across all teams. So that would be our support teams, our legal teams, our risk teams, all of them together.

Lenny Rachitsky (00:20:51):
Wow.

Dhanji R. Prasanna (00:20:52):
And then on the engineering side, it's very variable because like I said before, it matters how big and how complex the code base is. And so if you're building a totally new Greenfields code base or you're building an app for a new platform, then we're seeing those pretty aggressive gains, but in very complex code bases that already exist, those gains are not quite there yet.

Lenny Rachitsky (00:21:18):
That's amazing. And whenever I hear a stat like this, I think an important element that people need to think about is this is the worst it will ever be. This is the lowest, this is now the baseline. And so it may not sound that crazy yet, but it's going to get crazy. Okay, the other thing that you talked about is Goose, you haven't explained what Goose is. This is a huge deal. Explain what Goose is and how important this has become to you guys.

Dhanji R. Prasanna (00:21:49):
So Goose is a general purpose AI agent. So you can think of it as a desktop tool or a program that you can download and install on your computer and then it has a UI. You can talk to it just like a chatbot and you can say anything from, "Hey Goose, organize my photos by category, and it has the ability to look within your photos and if there are a lot of trees, it'll organize them as nature photos. And there are a lot of people, it'll organize them as portraiture." All of this sort of stuff to writing software for you.

(00:22:30):
So it can do all of these tasks, and the way we've been able to do this is through something called a model context protocol or the MCP, which a lot of your listeners might've heard. And this is something that Anthropic came up with that we were a very early contributor to. And the model context protocol is very simply just a set of formalized wrappers around existing tools or existing capabilities. So if you have tools that you use in the enterprise, be it Salesforce or be it Snowflake or SQL, any of these things, you can wrap them in the MCP and then it exposes them to your LLM to be able to manipulate.

(00:23:16):
So until that point, the LLMs were not really able to do much other than chat, but Goose gives these brains arms and legs to go out and act in our digital world, and that's where we find it's had most impact and it's built on this fairly open protocol that anyone can implement. There have been an explosion of MCPs. Goose is entirely open source, by the way, so any of you can download it and extend it, write your own MCPs, and that's been our core successes through Goose.

Lenny Rachitsky (00:23:54):
Okay. So essentially like Claude code with a UI, desktop app sort of thing built on top of Claude and OpenAI ChatGPT and a bunch of open source models. Is that right?

Dhanji R. Prasanna (00:24:06):
Yeah, it can use any model. So we have a pluggable provider system and you can either bring your own API keys and use the Claude family models or OpenAI's family models, or you can use open source models and you can download them and use them directly or via Ollama and other, there are several tools that help you do that, but essentially it's taking the capability of these models to generate text and to interpret text and applying them to real world situations.

(00:24:42):
So one example that I really like is you can ask Goose to go and build your marketing report and it has MCPs to connect to Snowflake and Tableau and Looker. So it'll write SQL to pull out data from there, it'll do some analysis and a CSV so it can write Python code on your desktop to do all that. It will generate some graphs using some JavaScript charting library that it knows about.

(00:25:11):
And then finally, it'll put this all into a PDF or Google Doc or whatever and it can even email it for you or upload it somewhere. And it's doing all of this on its own, by the way. No one's sitting here telling it that, you're just saying, "Hey, I want this report, I want this emailed here, I want these pretty charts." And it's orchestrating across all these systems.

Lenny Rachitsky (00:25:31):
So essentially at Block, instead of using Claude or ChatGPT directly or even Cursor and all these apps, they use Goose?

Dhanji R. Prasanna (00:25:40):
Yeah, we allow our engineers and our general employee population to use any tools that they want. Goose is the one that's most well-integrated into all of our systems because it's built on the MCP and it's so easy to create an MCP for an existing system. So for example, if you're using a issue tracking tool and you want some AI automation added to it, before Goose, our teams would have to wait for the vendor to build that AI capability in there, or maybe there's some way in which OpenAI or Anthropic or Google would provide a general purpose capability where we could plug those in. But with Goose, that's no longer necessary with a few lines of code that an MCP represents. All these systems are orchestratable with AI basically overnight, and Goose can write its own MCPs. So it's pretty bootstrappable as well.

Lenny Rachitsky (00:26:43):
And this is open source and basically you've spent all this time building this thing, any other company can now implement it and build on all the work you've done?

Dhanji R. Prasanna (00:26:51):
Yeah, and we have a lot of companies using Goose pretty actively. I don't want to name too many names, but from our competitors to our close partners, a lot of them are using Goose pretty regularly on their teams. I know Databricks talks about it a lot, but everyone you can think of in this mid-tech tier is using Goose in some form.

Lenny Rachitsky (00:27:15):
That's insane. This feels like it could've been a massive business of its own, some of the fastest growing companies in the world, basically this is their product and you've built it and given away.

Dhanji R. Prasanna (00:27:23):
Yeah, we believe in the power of open source and one of our core missions is to increase openness, and that means contributing to open protocols and contributing to open source. And as a tech company, we're built on a lot of open source software. I think pretty much every tech company is whether you're talking about Linux or Java or MySQL or any of these essential components, and so we feel like we have a strong imperative to give back.

(00:27:57):
We want to build things that not only are good for us and our customers, but that outlast Block and outgrow Block, that's certainly a core value for us and has been from the beginning even long before this whole AI phase. So yeah, Goose follows in that proud tradition and yeah, we're very excited that its had the success it's had.

Lenny Rachitsky (00:28:18):
What's the story with the name Goose, by the way? Can't help but ask.

Dhanji R. Prasanna (00:28:21):
Goose is a Top Gun reference. So our engineer that came up with it. He also looks exactly like Goose, so it's kind of crazy if you put them side to side, he's going to be really embarrassed with my sharing this, but that's the reason why they call it Goose, and then we lent into the whole bird theme after that.

Lenny Rachitsky (00:28:41):
That's incredible. There's a story I heard you share on a different podcast where there's an engineer who takes this to the extreme and has Goose watch him. Talk about that, share that story.

Dhanji R. Prasanna (00:28:50):
Yeah, absolutely. So he is very, very AI-focused and he's trying to extract all these crazy ideas from Goose and Goose can do all of the things that I described through specific interactions with tools, but it can also just watch your screen so it understands how to process images and process the things that it's looking at through screenshots. And so he built this system where it's essentially just watching everything he does all the time and he'll be talking to a colleague on Slack or an email and they'll be discussing some feature that they think is useful to implement.

(00:29:30):
And then a few hours later he'll find that Goose has already tried to build that feature and opened a PR for it on Git and all sorts of other wacky things like that. So it'll try to nudge him out of a workflow. If he's running over on a meeting and he's late for something else, it comes up with these creative things that he didn't program or he didn't write prompts for, but that it thinks will help him improve his productivity or improve his work day. So yeah, it's pretty crazy. You have to have the stomach for it to be that level of tied into your working tools, but it kind of shows you what's possible with tools like this.

Lenny Rachitsky (00:30:14):
Clearly this is where things are going. Once this gets good enough, I love this guy is just trying it. So it's basically watching him work and anticipating what he should be doing and does the work for him as a first draft so that he's like, "Oh, the PR is already done on this thing. We were just talking about it at this meeting." That's incredible.

Dhanji R. Prasanna (00:30:31):
Exactly.

Lenny Rachitsky (00:30:32):
How good is it? Where's it at? If you had to go zero to a hundred of like, "Okay, going to, all you have to do is now think and talk and that'll just do your job."

Dhanji R. Prasanna (00:30:41):
Yeah, so voice is the other big part of it. It has voice processing capability, so it's always listening to what he's saying as well and trying to interpret that. I would say that this is mostly an experiment, given that he's on our core Goose team and he contributes to Goose, so he has a day job. This is a kind of thing on the side that he was developing.

(00:31:04):
So once this evolves into more of a native feature of Goose itself or other tools that we use in the enterprise, I think it can have a lot of legs, but it's already pretty good. It's probably cutting down enormous amounts of busy work that he has to do. So for example, one thing he'll do is he'll say, "Oh, I have a meeting conflict. I can't make it that time, or I have to go pick up my kid."

(00:31:32):
And Goose will automatically reschedule that meeting without him ever sitting in front of his calendar and clicking through 10 times. Yeah, so these are things that I think we were waiting for the calendar vendor to build as features into calendar, but we don't need to do that anymore because AI is able to orchestrate this for us.

Lenny Rachitsky (00:31:53):
This isn't that guy that had four jobs at four different startups that he was able to paralyze all his work and hire people.

Dhanji R. Prasanna (00:31:58):
No, it's not. He's someone that I've worked with for a long time and he's been at Block for a long time. He just loves experimenting and he embodies that culture of experimentation just like our creator of Goose who did the same thing.

Lenny Rachitsky (00:32:16):
So let me pull on that thread a little bit. You're kind of seeing a glimpse of where things are going. You're very ahead of the curve in a lot of ways at Block. How do you think things will look in a couple of years in terms of how engineers work, how product teams work that's different from today?

Dhanji R. Prasanna (00:32:32):
I think a lot of it is dependent on the improvement of LLM performance, but I can tell you the way I'm trying to change how I work and how I'm trying to change our immediate team's way of working. So I think vibe coding has been an interesting, exciting thing, which is you talk to a chatbot essentially and it goes and builds software for you, but I think this is highly limiting.

(00:32:59):
It's very ping pong. You do something, you wait for three or four minutes and it comes back with something sort of half-baked and you have to nudge it and guide it and massage it to get where it needs to be. I think that we're going to see much more autonomy. So where we're working on a couple of experiments with Goose, with the next version of Goose where we're really trying to push it to work not just for two or three or five minutes at a time, our median session length is five minutes and on average, seven, but we're trying to push it to hours.

(00:33:36):
We're trying to say, "Hey, all these LLMs are sitting idle overnight and on weekends while humans aren't there, there's no need for that." They should be working all the time. They should be trying to build in anticipation of what we want if we go back to the earlier part of the conversation. But also I think that they should be able to build in ways that were never possible before.

(00:34:04):
Before as humans, we had limited resources, limited bandwidth, and a lot of coordination overhead. So we would have to choose the best path to try in an experiment, and I don't think we need that anymore. We need instead to be able to describe multiple different experiments in a great amount of detail. And then maybe we go to sleep and then in the morning, all those experiments are built and we can sort of throw away five or six of them.

(00:34:34):
So one of the things that I do regularly, so I write code every day, but one of the things that I do regularly is just throw away huge, huge amounts of code, and it's kind of hard for me because I've never done that before. I mean obviously engineers love deleting code, but this is different. You build a whole new system or a whole new feature and you're like, "Ah, it doesn't feel exactly right. I'm just going to delete and start over."

(00:35:00):
So I think you're going to see a lot more of that way of working. And I think that you're going to see instead of us, for example, refactoring an app to have a different UI or to evolve into its new version, we're just going to rewrite that app from scratch. And one of the things I'm really pushing our teams to think about is what would our world look like if every single release, RM minus RF deleted the entire app and rebuilt it from scratch? And so we can't really do that today, but I think this shows you some of the direction of what's possible and where these tools are taking us.

Lenny Rachitsky (00:35:42):
What's interesting about that is that there's this common rule in software engineering and just product, don't ever just rewrite. Don't try to rewrite your thing. You're going to forget all of the small improvements and tweaks and bug fixes people have made over the years, and you think it's going to be the simple straightforward thing. It ends up being now it's like a year or more of just getting it back to where it was. And so interesting that AI now can make that possible, and what you're saying is that's actually maybe the way you should be working.

Dhanji R. Prasanna (00:36:09):
I think so. And I think that the trick is getting the AI to respect all of those incremental improvements, yeah, and sort of bake those in as a part of the specification, if you will. Yeah.

Lenny Rachitsky (00:36:25):
Also, the point you made about this agent, just you give it a bunch of ideas that builds them overnight and then you could see, I imagine it goes even further up the stack and comes up with the ideas and then starts building them and then you're like, "Okay, oh, that was a great idea. Now I can see it immediately in the same workflow."

Dhanji R. Prasanna (00:36:39):
Yeah, that's true. I was actually literally trying what you're saying just last week. And so I have this new version of Goose that we're working on and I was asking it to come up with ideas to improve itself and implement it overnight. And sometimes-

Lenny Rachitsky (00:36:57):
Slip problem.

Dhanji R. Prasanna (00:36:59):
... Sometimes it kind of goes off the script entirely and you have to sort of pull it back a bit. So I think we're not quite at that era where it's completely self-improving and completely autonomous, but I do think we're in a transition phase where we can give it that nudge and say, "Hey, here's my wishlist of 10 things that I wish you could do. Go and figure out the best way to do them." And it's successful I would say on 60% of those things, if the features are well enough described and it struggles on the remaining 40 where you have to kind of intervene and massage it. Yeah.

Lenny Rachitsky (00:37:43):
Oh man, I'm just imagining this feature where you give it the goal of drive revenue and growth and then it's just like, "Okay, everyone's fired. Here's your paychecks. I'll take it from here."

Dhanji R. Prasanna (00:37:56):
I don't think we're going to be there. I do think we're going to need a lot of human taste to anchor these AIs so they don't go off script to be honest. And that's really where our design lead and our design teams are pushing us to think, and that's a differentiator that I think will push us beyond this era of AI slop that everyone's talking about. So yeah, it's very much anchoring it into a thing that matters to people and the thing that's tasteful and useful and has value.

Lenny Rachitsky (00:38:30):
To make that even more concrete, is there an example of something maybe AI was trying to, or a team was trying to pitch where you had to just know this is where humans are going to step in and keep things on track?

Dhanji R. Prasanna (00:38:43):
I'd say it was more around things like process automation or a lot of times I'll get this sort of request where a team will say, "We need to buy this new tool from this vendor because our current tool is entering X, Y and Z." Another team will say, "No, no, no, we can just use Goose to build an app that will do the same thing for us in half the time or less." And then as a human, you're sitting there thinking, "Is any of this necessary? If we just change the process, do we even need to think about building tools?" And this is the thing that AI isn't good at, it's not able to have this portfolio judgment or judgment across a global sense of what's important and what matters.

(00:39:40):
So a lot of times, I tell teams just question the base assumption, particularly our InfoSec teams because they'll twist themselves into knot sometimes trying to secure something and you'll be like, "We'll just ask the team that's building it to do it differently or to not build that at all if it doesn't matter, and then you won't have to increase your surface area of securing it." So I think those are the areas where it's better for a human to use judgment and AI has not done a great job.

Lenny Rachitsky (00:40:11):
You make this point about building your own software, your own tools instead of buying stuff. This is a big question with AI, is it's going to replace all these SaaS apps to Salesforce over. Is there a sense of just either how much money you guys have maybe saved building your own stuff, or have you built a new-found respect for the existing SaaS software that everyone's using and pays lots of money for?

Dhanji R. Prasanna (00:40:31):
I think there's a trap in getting away from your core purpose as a company. And our core purpose is economic empowerment. So getting customers or merchants or artists the ability to make a sale or pay their rent or upload their latest creation to TIDAL. And I think that anything that serves that purpose, we should encourage and we should invest in, but if we're just purely looking at dollars versus dollars, then that's pulling us off that purpose.

(00:41:12):
The savings and costs that there might be in replacing a vendor tool by something you build in-house is probably not worth it in the mental bandwidth that you've lost and the amount of the team's technical focus that's being taken away. So yeah, I would say it just keep coming to the thing that matters to you as a company and then the rest will follow from that.

Lenny Rachitsky (00:41:38):
Yeah, I think people forget just how much maintenance it takes to keep something you've built. Like, "Okay, cool, we built it in a weekend and now it's years of endless maintenance and requests and support." And also to your point, it feels like it comes back to the always motto of just focus on your core competencies and then buy everything else.

Dhanji R. Prasanna (00:41:57):
Yeah, it's the classic 80/20 problem, and we have that enough with the apps that we build for our customers. We'll build some great experiments that really resonate, and then we have to spend a lot of time ironing out the long tail of problems. So in Cash Card, for example, we built the entire functionality of Cash Card, I would say pretty much in a weekend or maybe a week of integration and work.

(00:42:26):
And then it took a really long time to iron out all these edge cases where someone would tip twice the value of the bill and then it would completely break something in the back end, or people would use it as a gas station and they have a different way of billing your card. So yeah, it's very much that. And to your point, I would always come back to what is the reason we're doing this? Why does it matter to us and to our customers? And if it doesn't clearly satisfy that, I would just push it off as a not interesting thing.

Lenny Rachitsky (00:43:04):
This episode is brought to you by Persona, the verified identity platform, helping organizations onboard users fight fraud and build trust. We talk a lot on this podcast about the amazing advances in ai, but this can be a double-edged sword. For every wow moment, there are fraudsters using the same tech to wreak havoc, laundering money, taking over employee identities and impersonating businesses.

(00:43:27):
Persona helps combat these threats with automated user business and employee verification. Whether you're looking to catch candidate fraud, meet age restrictions or keep your platform safe, Persona helps you verify users in a way that's tailored to your specific needs. Best of all, Persona makes it easy to know who you're dealing with without adding friction for good users. This is why leading platforms like Etsy, LinkedIn, Square and Lyft trust Persona to secure their platform persona is also offering my listeners 500 free services per month for one full year, just head to withpersona.com/lenny to get started, that's withpersona.com/lenny.

(00:44:06):
Thanks again to Persona for sponsoring this episode. One of the biggest parts of the conversation around AI is hiring jobs, things like that. So I have two kind of this two-part question. One is just how has the rise of all these AI tools, this increased productivity impacted the way you plan head counts and hire? And then what do you look for that's different in people you're hiring now that AI is such a big part of the way you guys work?

Dhanji R. Prasanna (00:44:34):
I don't think that things have progressed far enough that it's really impacted in a fundamental way how many people you would need to build an app of the scale of Cash App, for example. I think what's changed for us is much different and it has nothing to do with AI, it's what we talked about earlier is moving from our GM structure to a functional structure. And in our GM structure, our incentives were always to think of engineering headcount as a commodity.

(00:45:09):
And so we would just add more engineers if we wanted to build more features and the classic mythical man person month trap or whatever it's called. And I think that moving to a functional structure completely changes that and you're like, "Well, we can leverage common platforms, common modules, we can bring in experts from across the company to advise us on how better to do this."

(00:45:38):
And so those kinds of things I think have made it much different and how we hire and we no longer see engineers as a commodity to just add 100 people to go and build the next product in Cash App. But on the AI side, we're very much looking for people that are embracing these tools and that are eager to try and learn from it. We're not looking for people who are amazing AI practitioners on the get-go.

(00:46:14):
I think we have those people and we're interested in those people if they ever want to work with us. But I'm much more keen on looking for that college grad who just really is eager to learn about these tools and open to it, or even the veteran who has embraced these tools and figured it out. And that's kind of where we're optimizing for who we look for rather than a specific set of skills.

Lenny Rachitsky (00:46:44):
So essentially the biggest change is just looking for people that are embracing AI, not being like, "No, I don't need this stuff. I'm an amazing engineer. I don't need to use Cursor or Goose or all these things."

Dhanji R. Prasanna (00:46:55):
Yeah, a learning mindset is how I would put it. This is something that Jack our CEO talks about a lot is he wants us to be a learning first company. So everything we do, every experiment that we ship, what can we learn from it and did we feel that we gave it our best shot? And I think that that's more important to him than even sort of coming up with the right business answer every time.

Lenny Rachitsky (00:47:25):
What about when you're interviewing? Are you encouraging engineers to use AI tools as they're doing exercises? How did that change over the past year or two?

Dhanji R. Prasanna (00:47:33):
Yeah, we're starting to do that now. So traditionally we would just use CoderPad or something like that to wipe boards or a problem or even program it in Pseudocode or near Pseudocode. But now we're looking at can you use Vibe code to build something? How comfortable are you with these tools or how are you thinking about evolving with them as well?

(00:48:04):
But it's early days yet I would say that it's not clear to me that necessarily how someone knows how to use, be it Goose or Cursor or any of these other tools matters that much to whether they're a good engineer. I still think that things that we interviewed for in the past, a critical mindset, the ability to really understand deeply the technical nature of a problem is still much more important than whether you're a fully AI native programmer or not.

Lenny Rachitsky (00:48:37):
Another question that I've always been thinking about a lot of people wonder is what level of engineer is most benefiting from these tools? You could argue it's the junior engineers now, they could just get all this work done. You could argue it's senior engineers because they know so much more about how things work and now they could just orchestrate thousands of agents doing their bidding. What have you seen in terms of which level is benefiting most?

Dhanji R. Prasanna (00:48:56):
Yeah, so two answers to that. One is you're definitely right that the more senior and the more junior they are, the more comfortable or the more eager they are to adopt these AI tools. And I think that's for a variety of reasons, including some of them that you named. I think the senior people really understand in great depth how everything works.

(00:49:18):
And so they're almost relieved that this tool exists that can go and do all these things that they've done a million times before and couldn't be bothered. And then the junior people are like my niece and nephew on a BlackBerry or something, they're just blitzing through things, not BlackBerry in the early days and iPhones now, they're blitzing through a text message when I'm still seek and destroying through my keyboard, shows you how old I am.

(00:49:50):
So I think there's that, but I think the non-technical people using AI agents and programming tools to build things is really what's been surprising and really amazing. And I think that speaks to how these roles are going to evolve in the future. The lines are going to be blurred between whether you're in legal or in risk or in engineering and design even. And so I think that the people that are able to embrace it to optimize for their particular work day and their particular set of tasks are really who are showing the most impact from these tools.

Lenny Rachitsky (00:50:36):
It's interesting. No one talks about that element of engineering productivity, which is the reduction of asks from all the other parts of the company to build random one-off things. That feels like a huge productivity gain for engineers.

Dhanji R. Prasanna (00:50:47):
It is massive, although I think that it's a little bit like the analogy of if you build a bigger highway, you'll just get more cars on the road. So I think the fact that everyone's building software means that there's more software to be built, more coordination to happen, and everyone's more eager to ship things faster and with greater results. And so we're just seeing an overall uptake in velocity and the ask for more features, if that makes sense. Yeah.

Lenny Rachitsky (00:51:22):
Absolutely. And it connects to your point about you're not slowing hiring. What I'm hearing is just headcount, hiring desires for more engineers, more product people is not slowing at all. You're basically, it's as if AI wasn't really there.

Dhanji R. Prasanna (00:51:37):
We're being more thoughtful about it. So like I said, we were looking at as a commodity in the GM era, and now that we're functional, it's much less about how many engineers we need as a function of the number of features we have in Square or Cash App and in the functional org structure, we think of it much more as what are the areas of optimization? Where can we build depth and what really accelerates our priorities through things like modularization reuse and going deep into platforms.

Lenny Rachitsky (00:52:12):
I love this hot take of if you're trying to be more productive, forget AI, just re-org into a functional structure.

Dhanji R. Prasanna (00:52:21):
It's not wrong in some ways. So here's another really interesting example where we are trying to improve our build times and you were using Goose and a lot of other tools to help us with this too, and they've done remarkable things. So we have this really cool tool that analyzes our test suites and selects the right test to run for changes that were made.

(00:52:50):
So we cut down basically 50% of test runs this way, which is pretty great, and we're not warming the planet as much with all these unnecessary CPU cycles being wasted on tests. But then things like offloading tests to the cloud or simply just deleting tests that don't make sense anymore, probably save you two to three times that.

(00:53:14):
So there is still a portfolio approach that you need to take for lack of a better term. It's like that example I told you earlier about should we buy a vendor tool? Should we build this in-house? It's like, "Well, do we even need to do this process at all?" So in some ways, structure matters more than the efficacy of the tools you have.

Lenny Rachitsky (00:53:34):
Wise words makes me think about Elon has this whole process for optimize stuff and one of the steps is like, "Do we even need this thing before we start out optimizing and automating it?" Before I zoom out and ask about just general lessons that you've learned over the course of your career, is there anything else that you think might be really valuable or useful to folks that are trying to lean in further into AI or just help their teams think a little bit more forward thinking?

Dhanji R. Prasanna (00:54:04):
I would say really try and use these tools yourself. So the way in which I think we've been able to drive most of the adoption is Jack uses Goose, I use Goose, our executive team all have used Goose and use it regularly and use other AI programming tools and assistance as well, and we do it every single day.

(00:54:31):
And so we learn a lot about how our own workflow can change, and that's going to tell you so much more about how are you going to change your organization's workflow than if you're reading a bunch of think pieces on LinkedIn or Harvard Business Review or whatever it is, and then trying to get your teams to follow suit. So I think we do this with everything. It's feel it, use the product yourself, feel it, understand its strengths and weaknesses and its ergonomics, and then figure out how to apply it to your teams.

Lenny Rachitsky (00:55:06):
Something I've found helpful in doing that, which I completely agree with, which is stop reading about it, stop listening to us talking about it, just build some stuff. The thing that I found really helpful there is have a specific task or problem you want to solve for yourself because that really motivates you and makes it very real.

(00:55:21):
For example, just the other day, I was trying to pull images out of a Google Doc. Google Doc, it's like I think of it as Hotel California. You put images in there, but there's no way to get them back out unless you do some crazy stuff. So I just went to Lovable and like Bill an app, or I can give you a Google Doc URL and let me download the images real easily and bam. Perfect.

Dhanji R. Prasanna (00:55:41):
Yeah, great example. I did something like this a couple months ago as well, where my son has a whole bunch of therapies, he has additional needs, and so I was trying to gather the receipts for all these therapies and share them with my wife and she will claim it from our insurer, and I was really struggling to do this because they're in various forms.

(00:56:05):
There are screenshots in some cases or PDFs or whatever. So I asked Goose to do this and it was all sitting on my laptop and Goose figured out that it could put all of these receipts into my Apple Notes app into a single note. It converted it to HTML so it would sync seamlessly to my phone and then I could email it or share it with her from there.

(00:56:30):
And that's just something I just never would've thought of. And it did this using Apple Script, so it just controlled my computer for me in the background. Yeah, so these are surprising ways in which these tools help us, and the more you use them to solve real problems to your point, the more you understand what their strengths are and where you can deploy them.

Lenny Rachitsky (00:56:51):
I love this example. So did you just go to Goose and be like, "Here's the problem I have, how would you solve it?"

Dhanji R. Prasanna (00:56:56):
Yeah, pretty much. I said, "I have all these receipts there in Google Drive, so we have similar origin problem there and I need to get them into a single form and I need to collate the totals and do all this." So it tried a few approaches first. It tried to download them and it tried to read them using a PDF reader and this and that. And then the thing about Goose that I think a lot of the other AI agents learn from us as well is if it tries a few things and fails, it'll back up and it'll try a different route and it'll just keep going until it makes some progress.

(00:57:33):
And that's what it did. Then it picked Apple Script as a way to do it because it had the MCP extension to control my computer, and this is the same thing that our engineer, we were talking about the other day uses to watch his screen and things like that, but this was a very focused problem and it managed to do that. So yeah, it's surprising what these tools can do and allowing them the flexibility to do that is a big part of learning how to use them.

Lenny Rachitsky (00:58:02):
That's cool. I love the, by the way, can you run Goose as a regular person? Can you just download Goose and use that instead of Claude?

Dhanji R. Prasanna (00:58:08):
Yeah, absolutely. Yeah. You can just download it from our URL. We can share it in the show notes for you and yeah, you can install it. It comes for Mac and Windows and Linux I believe. It's an electron app, so it'll work on all of them. It also has a command line, so for people who are more comfortable using that, we have that UI as well.

Lenny Rachitsky (00:58:32):
Wow, you really are competing with these massive foundational model companies building. What's the simplest way to compare Goose to something else? Is it like this Claude code, this simplest comparison or something else?

Dhanji R. Prasanna (00:58:43):
I think it's a bit different than Claude Code because at its core, Goose is a platform that implements MCPs. So MCPs give it this dynamically extensible nature so it can do all of these things for you, whether it's automating things like we were talking about with Google Docs and notes and things like that, or it can do straight up programming tasks for you using other MCPs.

(00:59:11):
It can index code and do it that way. So it's really more of an extensible platform. So I would say it sits somewhere between your classic AI assistant where you just ask it, "What's the weather today? Can you calculate how many months it's been since this date?" Or whatever it is, to the more focused cursors and Claude codes of the world.

Lenny Rachitsky (00:59:39):
Basically, it's everything combined wholly and free. You pay for the LM tokens, but yeah.

Dhanji R. Prasanna (00:59:46):
Yeah, there's not like an open source models which-

Lenny Rachitsky (00:59:50):
Oh my God, this is crazy. What a cool team to be on building Goose at Block. Must having must be having so much fun. Oh man. Okay. Let me zoom out a little bit. So you've been CTO in LinkedIn right now for just about two years. What's something that you wish you knew before you stepped in this role? If you could go back a couple years and just whisper a few tips and tricks or lessons into your ear, what would they be?

Dhanji R. Prasanna (01:00:13):
I think maybe two different things. One is just the power of Conway's Law, like we talked about before. It's like how difficult it is to change outcomes without changing the structure of relationships between people in an organization. And I think I always kind of knew that at some level, but really appreciating it in a visceral way is big. The other thing that I really learned the hard way maybe is you only hear about it when things are going wrong.

(01:00:49):
So when things are going well, you kind of have this eerie silence and you're like, "Well, am I doing the right things here? Am I focusing on the right problems?" So having a bit of judgment, having a bit of time to step back and look at things holistically, those are things that you really need to make time for and do on a regular basis, which I wish I had known when I took up the role.

Lenny Rachitsky (01:01:15):
Looking back at your time at Block, I keep trying to, I almost say Square because I'm so used to that over the air, but I know Block is the name of the broader company and Square is just one. Just so people understand, Square is one business unit, one product within Block.

Dhanji R. Prasanna (01:01:28):
Correct, yeah, we have Square, Afterpay, Cash App and TIDAL are four major brands, and then we also have Bitkey and Proto that are focused on Bitcoin for us and we chip hardware in those two brands.

Lenny Rachitsky (01:01:44):
Okay, great. I think that some people are like, what are you guys talking about? Okay, cool. So reflecting back on your time at Block, what's maybe the most counterintuitive lesson you've learned about building products or building teams that goes against what most people believe, say common startup wisdom?

Dhanji R. Prasanna (01:02:02):
I think code quality is one. Being an engineer. I learned this very early on and it keeps coming true over and over and over again. A lot of engineers think that code quality is important to building a successful product. The two have nothing to do with each other, but my favorite example is YouTube. I was working at Google around the time YouTube was acquired and I just remember there was this whole wash of angst about how horrible the YouTube code base is and how terrible their architecture is, and they're storing videos as blobs in MySQL and whatnot.

(01:02:41):
And you could argue that YouTube is the most successful product at Google by a long way, maybe more successful than many of their others combined. And so it really has very little to do with how well it was architected because the flip side of that Google video, which is product that I don't know if people remember, it existed before YouTube. It supported more formats, it supported higher resolution.

(01:03:11):
You could upload hour long videos, YouTube had none of this. It just had the one or two minute quick video thing and it's far and away, blown away its competition. And so I think just keeping that front and center is why are we building these tools or these apps or these products? They're for people to solve a specific problem. So in our case, it's for a square merchant to make a sale, to sell coffee to you or to sell something they've made. And that's really what's important.

(01:03:49):
It's not really important how well our Android platform performs unless it's serving that need. And so I think that's been a really hard one for me over my career. And I continually encounter engineers who think we need to refactor, we need to do this in a better way. And then I'm like, "No, all this code could be thrown away tomorrow. So just focus on what we're trying to build and whom we're trying to build for."

Lenny Rachitsky (01:04:19):
That is an incredible insight and lesson. This YouTube story is so fun and such a good example. You're saying they were storing the video content in a MySQL set like row and column as a blob data.

Dhanji R. Prasanna (01:04:34):
Yeah, this is what, I didn't actually look the code so I couldn't verify it, but this was the common wisdom. And then they had an entirely Python stack that was incredibly slow compared to the state-of-the-art C++ and Java servers that we had hyper-optimized at Google back in those days.

Lenny Rachitsky (01:04:57):
That is hilarious. It makes me think about also companies when you look inside a company, if you work at a company, you're just like, "This is just pure chaos. No one knows what's going on. This is just about to all fall apart." And that's basically what it's like at every successful hyper-growth company.

Dhanji R. Prasanna (01:05:14):
Yeah, there's some truth to that for sure. Yeah.

Lenny Rachitsky (01:05:17):
And so I think again, it's just there's so much more that is more important to the success of a business. And it's what you said is are you solving a real problem for people? Can you get in their hands? Can you continue solving real problems for them? It's not about the quality of the code, it's not how well you operate internally.

Dhanji R. Prasanna (01:05:32):
Absolutely. I think on Cash App we had that as well. So in the early days of Cash App, I was head of engineering from when we were about 10 engineers to 200 plus and took us to about 10 plus or 20 million users thereabouts. And there was a very similar thing there. From the outside it looked like everything was really chaotic. It's like people would build random experiments and ship them and it just didn't look like we were following strict policies on things like software life cycle and stuff like that, and it was kind of true.

(01:06:13):
And my philosophy was always, we have all these brilliant engineers and I'm going to do more harm than good by trying to harness them into very strict blinkered areas. If they want to spin their wheels building something that is a complete waste of time for a little bit. But at the same time, if they're delivering these amazing things on the flip side, then I'll almost allow that. I'll be okay with that.

(01:06:44):
And it's a fine balance because engineers can really go off and into rabbit holes if you let them. But yeah, there's a certain amount of creativity that chaos breeds and you have to know how to build controlled chaos in some ways. So you have to create a foundation that isn't liable to rupture. You have major liability problems or something like that, or you're going to lose money in our case. And so as long as those things are bedded down and you allow your engineers to have the freedom to experiment and iterate and do the things that energizes them, that's the ideal.

Lenny Rachitsky (01:07:26):
Speaking of controlled chaos, one of your titles during your time at Block, I guess this was while you were actually at Square, was Mad Scientist for four and a half years.

Dhanji R. Prasanna (01:07:38):
Yeah, that was a time when I was working part-time, mostly because I had very young kids with lots of additional needs and I was a consultant on various different projects and I was trying to help some wacky things get off the ground. And yeah, I'm really grateful to Block that they afforded me the freedom to have that role in my career as well.

Lenny Rachitsky (01:08:08):
Maybe one more question before I take us to Fail Corner, which I'll explain. So you've shared a few lessons of things you've learned over the course of your career. Are there any other, just let's say core leadership lessons that you've learned that you think have been important to you being successful at the work that you've done?

Dhanji R. Prasanna (01:08:26):
I think start small with everything. If you try to boil the ocean to make a cup of tea, I don't know who said that, but it's a really a useful phrase that I keep coming back to. You'll never get there. So if you're making a cup of tea, just make the cup of tea. You don't need to boil all the water that there is.

Lenny Rachitsky (01:08:47):
That sounds like really not delicious tea. Ocean water.

Dhanji R. Prasanna (01:08:52):
Yeah, I think there's another one of, I think Carl Sagan said, "If you want to make an apple pie from scratch, you have to first invent the universe." So it's like narrow your scope to the thing that's in front of you and that's achievable. And so that I think is really important and that's one of our core tenets and always has been even when we were just Square in the early days, start small.

Lenny Rachitsky (01:09:19):
Is there an example that maybe worked really well or maybe didn't work?

Dhanji R. Prasanna (01:09:23):
Yeah, Goose started small. It was just an engineer working on their own time trying to build something that was useful and that satisfied a thesis that they had. So Brad, our creator of Goose, believed very early on, I think long before we heard the buzzword going around that agents would be how we unlock value from LLMs. And he built a proof concept and he shared it with a bunch of people. He shared it with Databricks and Anthropic, got them excited and learned a lot from them.

(01:09:59):
And so it just sort of built momentum from there. And even internally, it was quite a similar thing. Cash App itself was like that and Cash App started more or less as a hack week sort of idea and grew into a bigger and bigger and bigger thing. So a lot of our projects start with these small experiments that we try to then build on top of. We became the very first company that was a public company to launch a Bitcoin product. And that was again a hack week idea that actually Jack and me and another engineer worked on.

Lenny Rachitsky (01:10:40):
That was the hackathon team? You and Jack Dorsey and an engineer?

Dhanji R. Prasanna (01:10:44):
Yeah, it was the three of us.

Lenny Rachitsky (01:10:46):
Unreal.

Dhanji R. Prasanna (01:10:48):
Yeah, and it was great. We went and bought a cup of coffee, a blue bottle, and it was bought using Bitcoin over cash card. And I'll tell you those in hindsight, probably the most expensive cup of coffee.

Lenny Rachitsky (01:11:02):
What was Bitcoin at? 20,000?

Dhanji R. Prasanna (01:11:02):
I think it was 6,000 or 7,000 back then. I don't know.

Lenny Rachitsky (01:11:07):
It's like 120,000 now. Great.

Dhanji R. Prasanna (01:11:12):
But yeah, it's an example of how you get to a working useful product to people if you focus on a small thing first in a build.

Lenny Rachitsky (01:11:22):
And just to double down on this counter too. "Okay, we have a big idea, we're just going to put a bunch of resources on it and go big immediately."

Dhanji R. Prasanna (01:11:29):
Yeah, absolutely. And I've been part of teams like that too. So in my career, I worked at Google on this product called Google Wave, which was trying to be everything to everyone and we were 70, 80 engineers building this thing before it even really had any users outside Google. And so I think that's an example of something that started big, tried to go big on day one and probably lacked some of that meeting the earth where reality lies and adapting accordingly.

Lenny Rachitsky (01:12:08):
I remember Google Wave. Absolutely. It was beautiful. A lot of hype. I don't remember what it was for specifically, but it looked really nice.

Dhanji R. Prasanna (01:12:15):
Yeah, a lot of learnings from that one for me. Yeah.

Lenny Rachitsky (01:12:19):
What else? Any other big lessons?

Dhanji R. Prasanna (01:12:21):
Those two are the big ones, but I would also say question base assumptions on everything. Sometimes we get into traps where we are as professionals, hyper focused on what we're building that day, that week, that month. And we don't stop to think should we even build this at all? Or what's the purpose of building this?

(01:12:46):
Could we build something completely different that would matter more to our core reason for being? So I would say, yeah, question the sort of base assumptions. It's somewhat of a cliche, but you really need to remind yourself to apply it over and over and over again.

Lenny Rachitsky (01:13:03):
I had a colleague of yours on the podcast back in the day, IO, who worked with you on Cash App.

Dhanji R. Prasanna (01:13:08):
Yeah.

Lenny Rachitsky (01:13:09):
He's a friend of mine, he's amazing. He had a quote along those lines of just like, I forget exactly what it was, but it was just get to the bare metal of the thing that you're working on, just touch the thing that you're building and go to the base of it to really understand what's going on. And I imagine that was really important with Building Cash App and Cash Card.

Dhanji R. Prasanna (01:13:26):
Yeah, IO is one of the best product people I've ever worked with and one of my closest friends actually. So absolutely with him, and you on that one, yeah.

Lenny Rachitsky (01:13:38):
Okay. I'm going to take us to a recurring segment on the podcast I call Fail Corner. You already shared one example of a product that failed that you worked on. I'm curious if there's another, and the question is just what's the product you worked on that did not work out? Because people listening to this hear all these amazing successful people come on the podcast, share all these stories of success, endless success, but they don't hear the stories when things don't work out. And so this question is just, "What's a product you worked on that didn't work out and what did that teach you?"

Dhanji R. Prasanna (01:14:08):
It's a very valuable point. My career has basically been a string of failed product on top of failed product. And I think that, "Yeah, the Google wave example's there." I worked for Hot Minute on Google+, which was another epic failure.

Lenny Rachitsky (01:14:23):
Good one.

Dhanji R. Prasanna (01:14:23):
I worked at this social networking startup called Secret, which burned hot for a bright minute and then blew up. And then there was an email startup that we did, and that was, again, very promising, and then that fizzled. So the co-founder of Canva and I worked on that one. So there's been a whole string of failures, but at each point, I think I learned something and I learned that I need to never make that class of failures or errors again.

(01:15:01):
And so Cash App was probably the big success for me that a product that I worked on that was very early on and grew to be this giant business and product that people love. So yeah, been my career is essentially taking the learnings from all these failures, getting some humility out of it in the process too, coming into things, willing to listen to other people's points of view, critical points of view, and not just thinking that I have all the answers, yeah.

Lenny Rachitsky (01:15:36):
And I bet all these products that failed had really beautiful code. A lot of really good architecture decisions were made. Some of them, some of them were awful in every way. So many reasons for it to fail. Incredible. Dhanji, is there anything else that you wanted to share or I don't know, double down on before we get to our very exciting lightning round?

Dhanji R. Prasanna (01:15:59):
I would say I think that we're in this era of a lot of change and people are scared or reticent or uncertain about where things are going. And I think that look at the things that matter to you. For us, it's open source, open protocols, improving access for everyone. I've been very lucky in my career to only work on products that are either free or almost free to anyone or they have a free tier and then you pay for some premium services and that are usable by everyone. So anyone can become a Square seller.

(01:16:42):
I remember even in the early days, people used it to pay each other as a peer-to-peer money transfer system and that's why we built Cash App and that was really successful on the back of that. So I think it's really look at the things that are important to you and optimize for them. It's not really that important that the technology trends are growing in a certain way because technology is here to serve us, and if we have an important reason for being and an important purpose, then we can make that technology serve us. And that's much more important than being deep with the technology or being at the forefront of every trend.

Lenny Rachitsky (01:17:27):
Such great advice when there's so much to pay attention to and so much happening. So stressful to feel like I'm just not aware of all the things. I'm not as good as all these people I'm seeing on social media, but what's happening with AI, I'm just so behind. What I'm hearing from you is just like what is actually important to you? And just do that. Don't feel like you need to be the best at everything that's happening on top of all the latest AI news.

Dhanji R. Prasanna (01:17:51):
Yeah, exactly. And if it's not meaningful and fun, then you shouldn't be doing it probably.

Lenny Rachitsky (01:17:58):
With that Dhanji, we've reached our very exciting lightning round. I've got five questions for you. Are you ready?

Dhanji R. Prasanna (01:18:03):
Okay. Shoot.

Lenny Rachitsky (01:18:04):
I see so many books behind you. So I love this first question. I'm excited to see what you pick. What are two or three books that you find yourself recommending most to other people?

Dhanji R. Prasanna (01:18:12):
Yeah, so I very much of the opinion that you shouldn't read books that are about your daily work or your professional life. I read fiction, I read the classics, I read poetry, philosophy, history. These are the books I really enjoy. And I think it expands your mind and gives you creative ideas and helps you question things about the human condition.

(01:18:39):
And that's much more valuable than some self-help book or some get good at being an engineering manager book. So yeah, having said that, the Master in Margarita by Mikhail Bulgakov is one that I really love. It's a masterpiece of Russian literature. And then I've always been drawn to Tennyson's poetry and I find that in the times when I'm most uncertain or grieving, Tennyson's poetry has always resonated with me and helped me find a center.

Lenny Rachitsky (01:19:16):
Wow. Never heard these recommendations before. I'm really excited to check these out. Very cool for a CTO of a big tech company. What is a favorite recent movie or TV show you've really enjoyed?

Dhanji R. Prasanna (01:19:30):
Alien Earth I think is pretty awesome. It's by Noah Hawley who did the Fargo TV series. And so it's someone with all of these incredible skills in high art filmmaking who's doing a pulp sci-fi show, and it just looks stunning and it feels stunning and it captures all of that essential alien pulpiness that makes it so interesting and fun. So I really like that, and I'm also watching Slow Horses, which I think is one of the better shows on TV.

Lenny Rachitsky (01:20:04):
Love Slow Horses. The new season's Out, think the fifth episode just dropped the day we're recording this. So I love that show. Alien Earth also just watched it, so creepy and just like all these slimy, gooey little creatures just crawling around.

Dhanji R. Prasanna (01:20:16):
Yeah, I just love the aesthetic and they captured something essential about the original Alien and yeah, they do it, but every scene in Alien Earth feels like you're watching a painting or something or someone's reading a novel to you. It's really unfolds very thoughtfully.

Lenny Rachitsky (01:20:36):
I've never watched any alien content in my life and I really enjoyed Alien Earth. I will say the ending, I was just like, it felt like it kind of slowed down a bit. I'm just like, "All right, I guess I see where it's going now." But it was really fun to watch. Okay, next question. Do you have a favorite product you really enjoyed? Sorry, a favorite product you've recently discovered that you really enjoy? It could be an app, could be an gadget, could be some kitchen thing.

Dhanji R. Prasanna (01:20:58):
Well, I'm a gamer. I love playing games. So for me it's the Steam Deck, the Steam Deck OLED, which is their latest version. It's like this gorgeous piece of hardware that lets you play the best games out there, but it's totally extensible and customizable. And in this era where we're constantly told by big tech companies that we need to lock everything down, we need to lock down the user experience and customizability in order to have things work for people.

(01:21:28):
I think Valve showed that's totally unnecessary and totally wrong, and you can build the Steam Deck. You can install competing app stores, you can install Windows on it. You can treat it like a computer, write programs, which I have done to run on it. So yeah, I think it's an incredible thing and it looks beautiful and it works great. So yeah, big fan.

Lenny Rachitsky (01:21:50):
Do you have a favorite life motto that you find yourself coming back to often in work or in life?

Dhanji R. Prasanna (01:21:55):
If you're not waking up in the morning feeling energized about what you're going to do that day in your professional life, then change something, quit if that's what it comes down to, or find a new way of doing what you're doing. Just don't accept what's meted out to you. So that's how I've tried to do things, and sometimes it works, sometimes not, but yeah, it's a good thing to ask yourself.

Lenny Rachitsky (01:22:25):
I really love this advice. It's really hard to do that for a lot of people. Is there anything that has helped you get over that fear of just like, "Oh man, I'm going to quit this thing. I don't know where I'm going to go next."

Dhanji R. Prasanna (01:22:36):
The main thing is telling yourself that a year from now, you're going to look back on what looks like a monumental problem, a life-changing thing, and you're going to be like, "Oh, that was so trivial." A lot of times we get into these traps where we're overthinking something or really nervous about making a change, but in hindsight, those don't seem that big.

(01:23:05):
And all the time that's passed since and all the events that have happened teach you that there's more to the world and it's never too late to do something useful or never too late to do something that's for yourself and improving yourself. So yeah, I think just kind of remembering that things are not as big or bleak or decisive as they seem in the moment is always important.

Lenny Rachitsky (01:23:30):
Final question. So you were a mad scientist at Square for many years. Do you have another favorite mad scientist from pop culture or real life?

Dhanji R. Prasanna (01:23:41):
That's an interesting one. I think the image that always comes to my mind is Doc Brown from Back to the Future. I feel like he's the canonical mad scientist of my generation anyway, but there've been a lot in video games and stuff too, but he was the one that was like, "I'm just going to do this crazy thing because I almost have this burning desire, need to do it, and whether I want to or not, I must build this time machine." And he spends the entire movie trying to fix the problems that it creates. But yeah, he has always been a really fun character for me.

Lenny Rachitsky (01:24:20):
You know what? I think about Pinky from Pinky in the Brain.

Dhanji R. Prasanna (01:24:24):
Oh yeah, that's a good one too. Yeah.

Lenny Rachitsky (01:24:27):
Oh man. Dhanji, this was awesome. You were wonderful. Thank you so much for being here. Two final questions before we actually wrap up. Where can folks find you online if they want to reach out, learn more about say Goose or anything else going on at Block? And how can listeners be useful to you?

Dhanji R. Prasanna (01:24:43):
Check out our GitHub pages for Goose and all of the other open source projects we have at Block. So there's a lot that's useful there. We do a lot on Android open source as well, so check that stuff out. You can always find me on LinkedIn, so feel free to connect. I'm very happy to be contacted.

(01:25:06):
And I would say the way people can be useful is, again, going back to this era we're in of a lot of change and uncertainty, I think people that demand more of their companies, of their employers, of their teams, demand something better. At Block, we always ask, "Can we default to making this open source? Can we build this for people that are not just us or our customers? Can everyone benefit?"

(01:25:37):
And I think that's particularly important in this era of AI where everyone's locking themselves in walled gardens and trying to capture parts of the platform that are emerging. So yeah, just demand more of people. The internet was created as a promise for open sharing of information to the benefit of all, and I think that AI should realize that for us. And so yeah, just demand that of people.

Lenny Rachitsky (01:26:07):
A really beautiful way to end it. Dhanji, thank you so much for being here.

Dhanji R. Prasanna (01:26:11):
Thank you, Lenny. I really appreciated it. Thank you.

Lenny Rachitsky (01:26:14):
I appreciate you.

Dhanji R. Prasanna (01:26:15):
Cheers.

Lenny Rachitsky (01:26:15):
Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.

